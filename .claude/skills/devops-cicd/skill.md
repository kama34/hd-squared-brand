# DevOps & CI/CD Skill

## Overview

**Purpose**: Comprehensive DevOps expertise для настройки CI/CD pipelines, containerization (Docker), automated deployment, environment management (production/staging), monitoring и infrastructure as code. Позволяет CTO автоматизировать deployment: push на main → production deploy, push на другие ветки → staging deploy в отдельном контейнере.

**Target Users**: CTO (primary), DevOps Engineer (collaboration)

**Capabilities**:
- Docker (Dockerfile, docker-compose, multi-stage builds, optimization)
- CI/CD pipelines (GitHub Actions, GitLab CI/CD, Jenkins)
- Automated deployment (SSH, webhooks, zero-downtime deployment)
- Environment management (production, staging, development)
- Secrets management (environment variables, GitHub Secrets, vault)
- Monitoring & logging (Docker logs, health checks, Prometheus, Grafana)
- Infrastructure as Code (docker-compose, basic Terraform)
- Security (container security, secrets, SSL/TLS)
- Reverse proxy setup (Nginx, Traefik, SSL certificates)

## Required Tools

- `Read` - Read Dockerfile, CI/CD configs
- `Write` - Create CI/CD pipelines, Dockerfiles
- `Edit` - Modify deployment configs
- `Bash` - Run Docker commands, deployment scripts
- `Grep` - Search for hardcoded secrets, config issues
- `Glob` - Find Docker/config files

## Core Knowledge Areas

### 1. Docker Fundamentals

#### Dockerfile Best Practices

**✅ GOOD** - Multi-stage build for Node.js app:

```dockerfile
# Stage 1: Build
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files first (better caching)
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build application (if needed)
RUN npm run build

# Stage 2: Production
FROM node:18-alpine

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/package*.json ./

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Start application
CMD ["node", "dist/server.js"]
```

**✅ GOOD** - Python/Flask Dockerfile:

```dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1001 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
```

**✅ GOOD** - Static website (HTML/CSS/JS):

```dockerfile
# Build stage (if using build tools)
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built files from builder
COPY --from=builder /app/dist /usr/share/nginx/html

# Add health check
HEALTHCHECK --interval=30s --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**❌ BAD** - Poor Dockerfile practices:

```dockerfile
FROM node:latest  # ❌ Don't use 'latest' tag

WORKDIR /app

# ❌ Running as root user
# ❌ Copying entire directory (including node_modules, .git)
COPY . .

# ❌ Installing dev dependencies in production
RUN npm install

EXPOSE 3000

# ❌ No health check
CMD ["npm", "start"]
```

#### .dockerignore

**Always create .dockerignore**:

```
# .dockerignore
node_modules
npm-debug.log
.git
.gitignore
.env
.env.local
*.md
.vscode
.idea
dist
build
coverage
*.log
.DS_Store
Dockerfile
docker-compose.yml
```

#### docker-compose.yml for Local Development

**✅ GOOD** - Complete docker-compose setup:

```yaml
version: '3.8'

services:
  # Application
  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: sales-ai-app
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: production
      DATABASE_URL: postgres://user:password@db:5432/salesai
      REDIS_URL: redis://redis:6379
      JWT_SECRET: ${JWT_SECRET}  # From .env file
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - app-network
    volumes:
      - ./logs:/app/logs
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    container_name: sales-ai-db
    restart: unless-stopped
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: salesai
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - app-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: sales-ai-redis
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    networks:
      - app-network

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: sales-ai-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
      - ./static:/var/www/static:ro
    depends_on:
      - app
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
```

### 2. CI/CD with GitHub Actions

#### Main → Production, Other Branches → Staging

**✅ GOOD** - Complete GitHub Actions workflow:

```yaml
# .github/workflows/deploy.yml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
      - develop
      - 'feature/**'
  pull_request:
    branches:
      - main

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # Step 1: Run tests
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run tests
        run: npm test

      - name: Run security audit
        run: npm audit --production

  # Step 2: Build Docker image
  build:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: test
    permissions:
      contents: read
      packages: write

    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=sha,prefix={{branch}}-

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # Step 3: Deploy to Production (only main branch)
  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    environment:
      name: production
      url: https://salesai.com

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Deploy to production server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.PROD_HOST }}
          username: ${{ secrets.PROD_USER }}
          key: ${{ secrets.PROD_SSH_KEY }}
          port: 22
          script: |
            # Navigate to deployment directory
            cd /opt/salesai/production

            # Pull latest image
            docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:main

            # Stop old container (if exists)
            docker-compose down

            # Start new container
            docker-compose up -d

            # Wait for health check
            sleep 10

            # Verify deployment
            curl -f http://localhost:3000/health || exit 1

            # Cleanup old images
            docker image prune -af --filter "until=24h"

      - name: Notify deployment success
        if: success()
        run: |
          echo "✅ Production deployment successful!"
          # Add Slack/Discord notification here

      - name: Rollback on failure
        if: failure()
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.PROD_HOST }}
          username: ${{ secrets.PROD_USER }}
          key: ${{ secrets.PROD_SSH_KEY }}
          script: |
            cd /opt/salesai/production
            docker-compose down
            docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:previous
            docker-compose up -d

  # Step 4: Deploy to Staging (all non-main branches)
  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: build
    if: github.ref != 'refs/heads/main' && github.event_name == 'push'
    environment:
      name: staging
      url: https://staging-${{ github.ref_name }}.salesai.com

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Deploy to staging server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.STAGING_HOST }}
          username: ${{ secrets.STAGING_USER }}
          key: ${{ secrets.STAGING_SSH_KEY }}
          script: |
            # Create branch-specific directory
            BRANCH_NAME="${{ github.ref_name }}"
            BRANCH_DIR="/opt/salesai/staging/${BRANCH_NAME}"

            mkdir -p "${BRANCH_DIR}"
            cd "${BRANCH_DIR}"

            # Create docker-compose.yml for this branch
            cat > docker-compose.yml <<EOF
            version: '3.8'
            services:
              app:
                image: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${BRANCH_NAME}
                container_name: salesai-staging-${BRANCH_NAME}
                restart: unless-stopped
                ports:
                  - "0:3000"  # Random port mapping
                environment:
                  NODE_ENV: staging
                  DATABASE_URL: \${STAGING_DATABASE_URL}
                labels:
                  - "traefik.enable=true"
                  - "traefik.http.routers.${BRANCH_NAME}.rule=Host(\`staging-${BRANCH_NAME}.salesai.com\`)"
            EOF

            # Pull and start
            docker-compose pull
            docker-compose up -d

            # Get assigned port
            PORT=$(docker-compose port app 3000 | cut -d: -f2)
            echo "Staging deployed on port: ${PORT}"
            echo "URL: https://staging-${BRANCH_NAME}.salesai.com"

      - name: Comment PR with staging URL
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '🚀 Staging deployment ready!\n\nURL: https://staging-${{ github.ref_name }}.salesai.com'
            })
```

#### GitLab CI/CD Alternative

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG

# Test stage
test:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run lint
    - npm test
    - npm audit --production
  artifacts:
    reports:
      junit: test-results.xml

# Build Docker image
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG
  only:
    - main
    - develop
    - /^feature\/.*/

# Deploy to production (main branch only)
deploy:production:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client
    - eval $(ssh-agent -s)
    - echo "$PROD_SSH_KEY" | tr -d '\r' | ssh-add -
    - mkdir -p ~/.ssh
    - chmod 700 ~/.ssh
  script:
    - ssh -o StrictHostKeyChecking=no $PROD_USER@$PROD_HOST "
        cd /opt/salesai/production &&
        docker pull $IMAGE_TAG &&
        docker-compose down &&
        docker-compose up -d &&
        docker image prune -af
      "
  environment:
    name: production
    url: https://salesai.com
  only:
    - main

# Deploy to staging (all other branches)
deploy:staging:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client
    - eval $(ssh-agent -s)
    - echo "$STAGING_SSH_KEY" | tr -d '\r' | ssh-add -
  script:
    - |
      ssh -o StrictHostKeyChecking=no $STAGING_USER@$STAGING_HOST "
        BRANCH_NAME='${CI_COMMIT_REF_SLUG}'
        BRANCH_DIR='/opt/salesai/staging/\${BRANCH_NAME}'

        mkdir -p \${BRANCH_DIR}
        cd \${BRANCH_DIR}

        # Create docker-compose.yml
        cat > docker-compose.yml <<EOF
        version: '3.8'
        services:
          app:
            image: $IMAGE_TAG
            container_name: salesai-staging-\${BRANCH_NAME}
            ports:
              - '0:3000'
            environment:
              NODE_ENV: staging
        EOF

        docker-compose pull
        docker-compose up -d
      "
  environment:
    name: staging/$CI_COMMIT_REF_SLUG
    url: https://staging-$CI_COMMIT_REF_SLUG.salesai.com
    on_stop: cleanup:staging
  except:
    - main

# Cleanup staging when branch deleted
cleanup:staging:
  stage: deploy
  image: alpine:latest
  script:
    - |
      ssh $STAGING_USER@$STAGING_HOST "
        cd /opt/salesai/staging/${CI_COMMIT_REF_SLUG}
        docker-compose down -v
        cd ..
        rm -rf ${CI_COMMIT_REF_SLUG}
      "
  when: manual
  environment:
    name: staging/$CI_COMMIT_REF_SLUG
    action: stop
```

### 3. Server Setup & Deployment

#### Initial Server Setup (Ubuntu/Debian)

```bash
#!/bin/bash
# server-setup.sh - Run on fresh Ubuntu 22.04 server

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Nginx
sudo apt install -y nginx certbot python3-certbot-nginx

# Create deployment directories
sudo mkdir -p /opt/salesai/{production,staging}
sudo chown -R $USER:$USER /opt/salesai

# Setup firewall
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable

# Setup automatic security updates
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades

echo "✅ Server setup complete!"
echo "Next steps:"
echo "1. Add SSH key for CI/CD: cat ~/.ssh/id_rsa.pub"
echo "2. Setup SSL: sudo certbot --nginx -d salesai.com -d www.salesai.com"
```

#### Nginx Reverse Proxy Configuration

**Production setup**:

```nginx
# /etc/nginx/sites-available/salesai-production
server {
    listen 80;
    server_name salesai.com www.salesai.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name salesai.com www.salesai.com;

    # SSL certificates (managed by certbot)
    ssl_certificate /etc/letsencrypt/live/salesai.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/salesai.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;

    # Logging
    access_log /var/log/nginx/salesai-production-access.log;
    error_log /var/log/nginx/salesai-production-error.log;

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
    limit_req zone=api_limit burst=20 nodelay;

    # Proxy to Docker container
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;

        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # Static files (if needed)
    location /static {
        alias /opt/salesai/production/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Health check endpoint (no rate limit)
    location /health {
        proxy_pass http://localhost:3000/health;
        access_log off;
    }
}
```

**Staging setup** (wildcard subdomain):

```nginx
# /etc/nginx/sites-available/salesai-staging
server {
    listen 80;
    server_name ~^staging-(?<branch>.+)\.salesai\.com$;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name ~^staging-(?<branch>.+)\.salesai\.com$;

    # Wildcard SSL certificate
    ssl_certificate /etc/letsencrypt/live/salesai.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/salesai.com/privkey.pem;

    # Security headers (less strict than production)
    add_header X-Robots-Tag "noindex, nofollow" always;
    add_header X-Frame-Options "SAMEORIGIN" always;

    # Logging
    access_log /var/log/nginx/salesai-staging-$branch-access.log;
    error_log /var/log/nginx/salesai-staging-$branch-error.log;

    # Proxy to branch-specific container
    location / {
        # This requires custom logic to map branch to port
        # Alternative: Use Traefik instead of Nginx for dynamic routing
        proxy_pass http://localhost:3001;  # Adjust per branch
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

#### Alternative: Traefik for Dynamic Routing

**docker-compose.yml with Traefik**:

```yaml
version: '3.8'

services:
  # Traefik reverse proxy
  traefik:
    image: traefik:v2.10
    container_name: traefik
    restart: unless-stopped
    command:
      - "--api.insecure=false"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.letsencrypt.acme.httpchallenge=true"
      - "--certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web"
      - "--certificatesresolvers.letsencrypt.acme.email=admin@salesai.com"
      - "--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./letsencrypt:/letsencrypt"
    networks:
      - traefik-network

  # Production app
  app-production:
    image: ghcr.io/your-org/salesai:main
    container_name: salesai-production
    restart: unless-stopped
    environment:
      NODE_ENV: production
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.production.rule=Host(`salesai.com`, `www.salesai.com`)"
      - "traefik.http.routers.production.entrypoints=websecure"
      - "traefik.http.routers.production.tls.certresolver=letsencrypt"
      - "traefik.http.services.production.loadbalancer.server.port=3000"
    networks:
      - traefik-network

networks:
  traefik-network:
    external: true
```

### 4. Zero-Downtime Deployment

#### Blue-Green Deployment Script

```bash
#!/bin/bash
# deploy-blue-green.sh

set -e

IMAGE="ghcr.io/your-org/salesai:main"
CURRENT_CONTAINER="salesai-blue"
NEW_CONTAINER="salesai-green"

# Check which container is currently active
if docker ps --format '{{.Names}}' | grep -q "^${CURRENT_CONTAINER}$"; then
    OLD_CONTAINER=$CURRENT_CONTAINER
    NEW_CONTAINER="salesai-green"
    NEW_PORT=3001
    OLD_PORT=3000
else
    OLD_CONTAINER="salesai-green"
    NEW_CONTAINER="salesai-blue"
    NEW_PORT=3000
    OLD_PORT=3001
fi

echo "📦 Pulling latest image..."
docker pull $IMAGE

echo "🚀 Starting new container: $NEW_CONTAINER on port $NEW_PORT"
docker run -d \
    --name $NEW_CONTAINER \
    --restart unless-stopped \
    -p $NEW_PORT:3000 \
    -e NODE_ENV=production \
    -e DATABASE_URL=$DATABASE_URL \
    $IMAGE

echo "⏳ Waiting for health check..."
for i in {1..30}; do
    if curl -f http://localhost:$NEW_PORT/health &>/dev/null; then
        echo "✅ Health check passed!"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "❌ Health check failed after 30 attempts"
        docker logs $NEW_CONTAINER
        docker stop $NEW_CONTAINER
        docker rm $NEW_CONTAINER
        exit 1
    fi
    sleep 2
done

echo "🔄 Updating Nginx to route to new container..."
sudo sed -i "s/:$OLD_PORT/:$NEW_PORT/g" /etc/nginx/sites-available/salesai
sudo nginx -t && sudo nginx -s reload

echo "⏳ Waiting 10 seconds before stopping old container..."
sleep 10

echo "🗑️ Stopping old container: $OLD_CONTAINER"
docker stop $OLD_CONTAINER
docker rm $OLD_CONTAINER

echo "🧹 Cleanup old images"
docker image prune -af --filter "until=24h"

echo "✅ Deployment complete! Active container: $NEW_CONTAINER"
```

#### Rolling Update (Docker Swarm)

```bash
# Initialize Docker Swarm
docker swarm init

# Create service with rolling update strategy
docker service create \
  --name salesai \
  --replicas 3 \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-failure-action rollback \
  --rollback-parallelism 1 \
  --publish 3000:3000 \
  ghcr.io/your-org/salesai:main

# Update service (rolling update)
docker service update --image ghcr.io/your-org/salesai:main salesai
```

### 5. Environment Management

#### .env Files Structure

```bash
# Production: .env.production
NODE_ENV=production
PORT=3000
DATABASE_URL=postgresql://user:pass@db-prod.internal:5432/salesai
REDIS_URL=redis://redis-prod.internal:6379
JWT_SECRET=your-super-secret-key-min-32-chars
ALLOWED_ORIGIN=https://salesai.com
SENTRY_DSN=https://xxx@sentry.io/xxx
LOG_LEVEL=info

# Staging: .env.staging
NODE_ENV=staging
PORT=3000
DATABASE_URL=postgresql://user:pass@db-staging.internal:5432/salesai_staging
REDIS_URL=redis://redis-staging.internal:6379
JWT_SECRET=staging-secret-key
ALLOWED_ORIGIN=https://staging-*.salesai.com
LOG_LEVEL=debug
```

#### Secrets Management

**GitHub Secrets** (for CI/CD):

```bash
# Add secrets via GitHub CLI
gh secret set PROD_HOST --body "1.2.3.4"
gh secret set PROD_USER --body "deploy"
gh secret set PROD_SSH_KEY < ~/.ssh/id_rsa
gh secret set DATABASE_URL --body "postgresql://..."
gh secret set JWT_SECRET --body "your-secret"

# Or via GitHub UI:
# Settings → Secrets and variables → Actions → New repository secret
```

**Docker Secrets** (for Docker Swarm):

```bash
# Create secrets
echo "your-db-password" | docker secret create db_password -
echo "your-jwt-secret" | docker secret create jwt_secret -

# Use in docker-compose.yml
version: '3.8'
services:
  app:
    image: salesai:latest
    secrets:
      - db_password
      - jwt_secret
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password
      JWT_SECRET_FILE: /run/secrets/jwt_secret

secrets:
  db_password:
    external: true
  jwt_secret:
    external: true
```

### 6. Monitoring & Logging

#### Docker Logs Management

```bash
# View logs
docker logs salesai-production --tail 100 --follow

# Configure log rotation in docker-compose.yml
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

#### Health Checks in Application

**Node.js/Express**:

```javascript
// Health check endpoint
app.get('/health', async (req, res) => {
  try {
    // Check database connection
    await db.query('SELECT 1');

    // Check Redis connection
    await redis.ping();

    res.status(200).json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
      memory: process.memoryUsage()
    });
  } catch (error) {
    res.status(503).json({
      status: 'unhealthy',
      error: error.message
    });
  }
});
```

**Python/Flask**:

```python
@app.route('/health')
def health():
    try:
        # Check database
        db.session.execute('SELECT 1')

        # Check Redis
        redis_client.ping()

        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 503
```

#### Prometheus + Grafana Monitoring

```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090"
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    ports:
      - "3001:3000"
    networks:
      - monitoring

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    ports:
      - "9100:9100"
    networks:
      - monitoring

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
```

## Usage Examples

### Example 1: Setup CI/CD for New Project

**Trigger**: CTO needs to setup deployment for Sales AI website

**Process**:

1. **Create Dockerfile**:
```bash
# Use frontend-development skill to understand project structure
# Then create appropriate Dockerfile
```

2. **Create .github/workflows/deploy.yml**:
```yaml
# Use the GitHub Actions template above
# Customize for your project (Node.js vs Python vs static HTML)
```

3. **Setup server**:
```bash
# SSH to server
ssh user@server

# Run server-setup.sh script
curl -sSL https://raw.githubusercontent.com/your-org/scripts/main/server-setup.sh | bash
```

4. **Add GitHub Secrets**:
```bash
gh secret set PROD_HOST --body "your-server-ip"
gh secret set PROD_USER --body "deploy"
gh secret set PROD_SSH_KEY < ~/.ssh/id_rsa
```

5. **Push to trigger deployment**:
```bash
git push origin main  # → Production deploy
git push origin feature/new-login  # → Staging deploy
```

### Example 2: Deploy Static Website (HTML/CSS/JS)

**Trigger**: Deploy Sales AI landing page

**Process**:

1. **Create Dockerfile**:
```dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 80
```

2. **Create docker-compose.yml**:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "80:80"
```

3. **Setup CI/CD** with GitHub Actions (use template above)

4. **Deploy**:
```bash
git push origin main  # Automatic deployment!
```

### Example 3: Migrate Existing Project to Docker

**Trigger**: Existing Node.js app needs containerization

**Process**:

1. **Analyze project**:
```bash
# Check dependencies
ls package.json

# Check if build step needed
grep "build" package.json
```

2. **Create Dockerfile** (use multi-stage build template)

3. **Create .dockerignore**

4. **Test locally**:
```bash
docker build -t salesai:test .
docker run -p 3000:3000 salesai:test

# Test health endpoint
curl http://localhost:3000/health
```

5. **Setup CI/CD**

## Integration with Other Skills

### frontend-development
- devops-cicd deploys → frontend-development builds
- frontend-development creates health endpoints → devops-cicd monitors

### backend-development
- backend-development builds APIs → devops-cicd deploys
- backend-development configures database → devops-cicd manages migrations

### tech-audit
- devops-cicd secures deployment → tech-audit reviews security
- tech-audit finds vulnerabilities → devops-cicd patches in CI/CD

## Best Practices

### 1. Always Use Multi-Stage Builds

**❌ BAD**:
```dockerfile
FROM node:18
COPY . .
RUN npm install  # Installs ALL dependencies including dev
CMD ["node", "server.js"]
```

**✅ GOOD**:
```dockerfile
FROM node:18 AS builder
COPY package*.json ./
RUN npm ci --only=production
COPY . .

FROM node:18-alpine
COPY --from=builder /app .
CMD ["node", "server.js"]
```

### 2. Never Commit Secrets

**❌ BAD**:
```yaml
# .github/workflows/deploy.yml
env:
  DATABASE_URL: "postgresql://user:password123@localhost/db"  # ❌
```

**✅ GOOD**:
```yaml
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}  # ✅
```

### 3. Always Add Health Checks

**❌ BAD** - No health check:
```dockerfile
FROM node:18
CMD ["node", "server.js"]
```

**✅ GOOD** - With health check:
```dockerfile
FROM node:18
HEALTHCHECK --interval=30s CMD curl -f http://localhost:3000/health || exit 1
CMD ["node", "server.js"]
```

### 4. Use Specific Image Tags

**❌ BAD**:
```dockerfile
FROM node:latest  # ❌ Unpredictable
```

**✅ GOOD**:
```dockerfile
FROM node:18.19-alpine  # ✅ Specific version
```

## Troubleshooting

### Problem: "Docker container exits immediately"

**Solution**:
```bash
# Check logs
docker logs <container-id>

# Run interactively to debug
docker run -it salesai:latest /bin/sh

# Check if application starts
node server.js
```

### Problem: "Port already in use"

**Solution**:
```bash
# Find process using port
lsof -i :3000

# Kill process
kill -9 <PID>

# Or use different port
docker run -p 3001:3000 salesai:latest
```

### Problem: "CI/CD deployment fails with permission denied"

**Solution**:
```bash
# On server, check SSH key permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# Verify SSH key in GitHub Secrets matches server
cat ~/.ssh/id_rsa.pub  # Should match authorized_keys on server
```

### Problem: "Health check failing after deployment"

**Solution**:
```bash
# SSH to server
ssh user@server

# Check container logs
docker logs salesai-production --tail 100

# Check if health endpoint responds
curl http://localhost:3000/health

# Check if container is running
docker ps -a
```

### Problem: "Dependencies lock file is not found" (GitHub Actions)

**Error**:
```
Error: Dependencies lock file is not found in /home/runner/work/...
Supported file patterns: package-lock.json, npm-shrinkwrap.json, yarn.lock
```

**Причина**: `actions/setup-node@v4` с `cache: 'npm'` требует package-lock.json, но файл не закоммичен.

**Solution**:
```bash
# Генерировать и коммитить lock files
npm install
cd api && npm install
git add package-lock.json api/package-lock.json
git commit -m "Add package-lock.json for CI/CD"
```

**Профилактика**: ВСЕГДА коммитить lock files, НИКОГДА не добавлять в .gitignore

---

### Problem: "npm ci fails in Dockerfile" (Missing lock file)

**Error**:
```
npm error The `npm ci` command can only install with an existing package-lock.json
```

**Причина**: Dockerfile копирует только package.json, но не package-lock.json.

**❌ BAD**:
```dockerfile
COPY package.json ./
RUN npm ci
```

**✅ GOOD**:
```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
```

**Профилактика**: ВСЕГДА копировать lock files вместе с package.json

---

### Problem: "Build output directory not found" (Vite/Webpack)

**Error**:
```
ERROR: "/app/dist": not found
```

**Причина**: Build tool создает `build/`, но Dockerfile копирует `dist/`.

**Solution**:
```typescript
// vite.config.ts - использовать стандартный dist/
export default defineConfig({
  build: {
    outDir: 'dist',  // Стандарт для Vite
  }
})
```

**Профилактика**:
- Использовать стандартные output directories (`dist/` для Vite)
- Проверять build logs перед написанием Dockerfile COPY

---

### Problem: "Invalid reference format" (Docker image name)

**Error**:
```
invalid reference format: repository name (InnoSmart-Tech/SalesAI-Website) must be lowercase
```

**Причина**: Docker registry требует ТОЛЬКО lowercase имена.

**Solution в GitHub Actions**:
```yaml
script: |
  IMAGE_NAME_LOWER=$(echo "${{ env.IMAGE_NAME }}" | tr '[:upper:]' '[:lower:]')
  docker pull ghcr.io/${IMAGE_NAME_LOWER}:main
```

**Профилактика**: ВСЕГДА конвертировать в lowercase перед docker pull/push

---

### Problem: "Permission denied" при создании файлов на сервере

**Error**:
```
sh: 11: cannot create docker-compose.yml: Permission denied
```

**Причина**: SSH пользователь не имеет прав записи в deployment директорию.

**Solution 1 (рекомендуется)**:
```bash
# На сервере - изменить владельца
sudo chown -R deploy:deploy /opt/salesai/production
sudo chown -R deploy:deploy /opt/salesai/staging
```

**Solution 2 (в скрипте)**:
```bash
# Использовать sudo tee вместо cat
sudo tee docker-compose.yml > /dev/null <<EOF
services:
  app:
    image: myapp
EOF
```

**Профилактика**: Настраивать правильные права ПЕРЕД deployment

---

### Problem: "Docker tag contains slash" (Invalid tag format)

**Error**:
```
unable to get image 'ghcr.io/owner/repo:feature/new-feature'
invalid reference format
```

**Причина**: Branch name содержит `/` (feature/new-feature), Docker tags НЕ могут содержать слеши.

**Solution**:
```bash
# Конвертировать branch name в valid Docker tag
BRANCH_TAG=$(echo "${BRANCH_NAME}" | tr '/' '-')
docker pull ghcr.io/owner/repo:feature-new-feature
```

**В GitHub Actions**:
```yaml
- name: Prepare Docker tags
  run: |
    BRANCH_TAG=$(echo "${{ github.ref_name }}" | tr '/' '-')
    echo "tag=${BRANCH_TAG}" >> $GITHUB_OUTPUT
```

**Профилактика**:
- ВСЕГДА конвертировать branch names перед использованием как Docker tags
- Docker tags могут содержать только: `[a-z0-9_.-]`
- Тестировать с feature branches (не только main)

---

### Problem: docker-compose.yml uses `build:` instead of `image:` (CI/CD)

**Проблема**: Docker пытается пересобирать образ на production сервере вместо использования pre-built.

**❌ BAD для CI/CD**:
```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
```

**✅ GOOD для CI/CD**:
```yaml
services:
  app:
    image: ghcr.io/owner/repo:main
```

**Профилактика**:
- CI/CD должен: build → push to registry → deploy использует готовый image
- Production сервер НИКОГДА не должен собирать образы

---

### Problem: "Unauthorized" при docker pull от private registry

**Error**:
```
Error response from daemon: error from registry: unauthorized
```

**Причина**:
- GitHub Container Registry (ghcr.io) packages по умолчанию **private**
- Сервер не авторизован в registry
- `docker pull ghcr.io/owner/repo:tag` требует аутентификации

**Solution в GitHub Actions deployment**:
```bash
# Login перед pull
echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

# Теперь pull работает
docker pull ghcr.io/owner/repo:tag
```

**Alternative Solution: Сделать package public**:
1. GitHub → Repository → Packages
2. Выбрать package (образ)
3. Package settings → Change visibility → Public

**Профилактика**:
- ВСЕГДА добавлять `docker login` перед `docker pull` от private registry
- Использовать `GITHUB_TOKEN` для аутентификации в ghcr.io
- Или сделать packages public для open source проектов

**Для других registries**:
```bash
# Docker Hub
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

# AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com

# Azure Container Registry
az acr login --name myregistry
```

---

### Problem: "no configuration file provided: not found" (docker compose)

**Error:**
```
no configuration file provided: not found
🛑 Stopping old container...
no configuration file provided: not found
```

**Причина:**
- `docker compose` команда запущена в директории без docker-compose.yml
- Файл не был создан или скопирован на сервер при deployment

**Solution в CI/CD:**
```bash
# Navigate to deployment directory
cd /opt/salesai/production

# CREATE docker-compose.yml on the fly
sudo tee docker-compose.yml > /dev/null <<EOF
services:
  app:
    image: ghcr.io/owner/repo:main
    container_name: app-production
    restart: unless-stopped
    ports:
      - "80:80"
    environment:
      NODE_ENV: production
EOF

# Now docker compose works
docker compose up -d
```

**Профилактика:**
- ВСЕГДА создавать docker-compose.yml на лету в CI/CD deployment скриптах
- Не полагаться на существующие файлы на сервере (могут быть удалены/изменены)
- Генерировать конфигурацию из secrets и переменных окружения

---

### BONUS: Docker Compose `version:` is obsolete

**Warning**:
```
the attribute `version` is obsolete, it will be ignored
```

**Причина**: Docker Compose v2 больше не требует `version:` в docker-compose.yml

**❌ Старый формат**:
```yaml
version: '3.8'
services:
  app:
    image: myapp
```

**✅ Новый формат**:
```yaml
services:
  app:
    image: myapp
```

**Solution**: Удалить строку `version:` из docker-compose.yml

---

### Problem: "Resource not accessible by integration" (GitHub Actions permissions)

**Error:**
```
RequestError [HttpError]: Resource not accessible by integration
status: 403
x-accepted-github-permissions: issues=write; pull_requests=write
```

**Причина:**
- GitHub Actions workflow пытается создать comment на PR/issue
- Но `GITHUB_TOKEN` по умолчанию имеет только `read` права
- Для создания комментариев нужны `write` права

**Solution:**
```yaml
jobs:
  my-job:
    runs-on: ubuntu-latest

    # Add explicit permissions
    permissions:
      contents: read
      pull-requests: write  # For commenting on PRs
      issues: write         # For commenting on issues

    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              body: "My comment"
            })
```

**Профилактика:**
- ВСЕГДА добавлять `permissions` когда workflow использует GitHub API
- Минимальные права: давать только необходимые permissions (principle of least privilege)
- Типичные permissions:
  - `contents: read` - read repository
  - `contents: write` - push commits, create releases
  - `pull-requests: write` - comment on PRs
  - `issues: write` - comment on issues
  - `packages: write` - push Docker images to ghcr.io

---

## Version History

- **2026-02-10**: Created comprehensive devops-cicd skill for CTO
  - Docker (Dockerfile, docker-compose, multi-stage builds)
  - CI/CD (GitHub Actions, GitLab CI/CD)
  - Deployment strategies (blue-green, zero-downtime)
  - Environment management (production vs staging)
  - Monitoring & logging
  - Security best practices
  - Integration with frontend-development, backend-development, tech-audit

- **2026-02-10**: Added 8+ common deployment errors from Sales AI project
  - Missing package-lock.json (CI/CD and Dockerfile)
  - Build output directory mismatch (Vite)
  - Docker lowercase requirement
  - Permission denied on server
  - Docker tag slash problem
  - build: vs image: in docker-compose
  - Docker Compose v2 version obsolete
  - Unauthorized when pulling from private registry (ghcr.io)

- **2026-02-10**: Added staging environment lifecycle management
  - Single staging container architecture (one container for all branches)
  - Automatic cleanup on branch delete workflow
  - Automatic cleanup after merge to main workflow
  - Manual operations and coordination strategies
  - Missing docker-compose.yml in deployment directory error
