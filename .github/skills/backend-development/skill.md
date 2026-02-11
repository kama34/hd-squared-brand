# Backend Development Skill

## Overview

**Purpose**: Comprehensive backend development expertise для создания, редактирования и оптимизации серверных приложений, APIs, баз данных и infrastructure. Включает Node.js/Express, Python/Django/Flask, REST/GraphQL APIs, database design, authentication, security, caching, background jobs.

**Target Users**: CTO (primary), DevOps Engineer (collaboration)

**Capabilities**:
- Server-side frameworks (Node.js/Express, Python/Django/Flask, Go)
- RESTful API design & GraphQL
- Database design (SQL: PostgreSQL, MySQL; NoSQL: MongoDB, Redis)
- Authentication & Authorization (JWT, OAuth 2.0, sessions, RBAC)
- Security (OWASP Top 10 backend-specific, input validation, rate limiting)
- Caching strategies (Redis, CDN, HTTP caching)
- Background jobs & message queues (Bull, Celery, RabbitMQ)
- Testing (unit, integration, e2e)
- Logging & monitoring (Winston, Sentry, Prometheus)
- Deployment (Docker, CI/CD, environment management)

## Required Tools

- `Read` - Read backend code files
- `Edit` - Modify server code
- `Write` - Create new endpoints, models
- `Grep` - Search for security patterns, unused code
- `Glob` - Find files by type
- `Bash` - Run servers, tests, migrations
- `mcp__ide__getDiagnostics` - Get linter/type errors

## Core Knowledge Areas

### 1. RESTful API Design

#### REST Best Practices

**✅ GOOD** - Well-designed REST API:

**Resource Naming**:
```
GET    /api/users              # List all users
GET    /api/users/:id          # Get specific user
POST   /api/users              # Create new user
PUT    /api/users/:id          # Update entire user
PATCH  /api/users/:id          # Partial update
DELETE /api/users/:id          # Delete user

# Nested resources
GET    /api/users/:id/posts    # Get user's posts
POST   /api/users/:id/posts    # Create post for user

# Filtering, sorting, pagination
GET    /api/users?role=admin&sort=created_at&page=2&limit=20
```

**❌ BAD** - Poor REST design:
```
GET    /api/getAllUsers        # Use GET /api/users
POST   /api/user/create        # Use POST /api/users
GET    /api/deleteUser/:id     # Use DELETE /api/users/:id (GET should not mutate)
POST   /api/users/search       # Use GET /api/users?q=query
```

#### HTTP Status Codes

```javascript
// Success
200 OK           // Successful GET, PUT, PATCH, DELETE
201 Created      // Successful POST with new resource
204 No Content   // Successful request with no response body

// Client Errors
400 Bad Request       // Invalid request data
401 Unauthorized      // Not authenticated
403 Forbidden         // Authenticated but not authorized
404 Not Found         // Resource doesn't exist
409 Conflict          // Resource conflict (e.g., duplicate email)
422 Unprocessable     // Validation errors
429 Too Many Requests // Rate limit exceeded

// Server Errors
500 Internal Server Error  // Generic server error
502 Bad Gateway           // Upstream server error
503 Service Unavailable   // Server temporarily down
```

#### Node.js/Express Example

**✅ GOOD** - Production-ready Express API:

```javascript
// server.js
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { body, validationResult } = require('express-validator');
const jwt = require('jsonwebtoken');

const app = express();

// Security middleware
app.use(helmet()); // Sets security headers
app.use(express.json({ limit: '10mb' })); // Body parsing with size limit
app.use(express.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});
app.use('/api/', limiter);

// CORS
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', process.env.ALLOWED_ORIGIN);
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN

  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid or expired token' });
    }
    req.user = user;
    next();
  });
};

// Authorization middleware (Role-Based Access Control)
const requireRole = (...roles) => {
  return (req, res, next) => {
    if (!req.user || !roles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    next();
  };
};

// Validation middleware
const validateUser = [
  body('email').isEmail().normalizeEmail(),
  body('password').isLength({ min: 8 }).matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/),
  body('name').trim().isLength({ min: 2, max: 100 })
];

// Routes
app.post('/api/auth/register', validateUser, async (req, res) => {
  try {
    // Check validation results
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(422).json({ errors: errors.array() });
    }

    const { email, password, name } = req.body;

    // Check if user exists
    const existingUser = await db.query('SELECT id FROM users WHERE email = $1', [email]);
    if (existingUser.rows.length > 0) {
      return res.status(409).json({ error: 'Email already registered' });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 12);

    // Insert user
    const result = await db.query(
      'INSERT INTO users (email, password, name) VALUES ($1, $2, $3) RETURNING id, email, name',
      [email, hashedPassword, name]
    );

    const user = result.rows[0];

    // Generate JWT
    const token = jwt.sign(
      { id: user.id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: '7d' }
    );

    res.status(201).json({
      user: {
        id: user.id,
        email: user.email,
        name: user.name
      },
      token
    });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/users', authenticateToken, requireRole('admin'), async (req, res) => {
  try {
    const { page = 1, limit = 20, sort = 'created_at', order = 'DESC' } = req.query;

    // Validate sort parameter to prevent SQL injection
    const allowedSortFields = ['created_at', 'name', 'email'];
    const sortField = allowedSortFields.includes(sort) ? sort : 'created_at';
    const sortOrder = order.toUpperCase() === 'ASC' ? 'ASC' : 'DESC';

    const offset = (page - 1) * limit;

    const result = await db.query(
      `SELECT id, email, name, role, created_at
       FROM users
       ORDER BY ${sortField} ${sortOrder}
       LIMIT $1 OFFSET $2`,
      [limit, offset]
    );

    const countResult = await db.query('SELECT COUNT(*) FROM users');
    const total = parseInt(countResult.rows[0].count);

    res.json({
      data: result.rows,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total,
        pages: Math.ceil(total / limit)
      }
    });
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/users/:id', authenticateToken, async (req, res) => {
  try {
    const { id } = req.params;

    // Validate ID is a number
    if (isNaN(id)) {
      return res.status(400).json({ error: 'Invalid user ID' });
    }

    // Users can only view their own profile unless admin
    if (req.user.role !== 'admin' && req.user.id !== parseInt(id)) {
      return res.status(403).json({ error: 'Access denied' });
    }

    const result = await db.query(
      'SELECT id, email, name, role, created_at FROM users WHERE id = $1',
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.json({ data: result.rows[0] });
  } catch (error) {
    console.error('Error fetching user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.patch('/api/users/:id', authenticateToken, async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email } = req.body;

    // Authorization check
    if (req.user.role !== 'admin' && req.user.id !== parseInt(id)) {
      return res.status(403).json({ error: 'Access denied' });
    }

    // Build update query dynamically
    const updates = [];
    const values = [];
    let paramCount = 1;

    if (name) {
      updates.push(`name = $${paramCount++}`);
      values.push(name);
    }

    if (email) {
      updates.push(`email = $${paramCount++}`);
      values.push(email);
    }

    if (updates.length === 0) {
      return res.status(400).json({ error: 'No fields to update' });
    }

    values.push(id);

    const query = `
      UPDATE users
      SET ${updates.join(', ')}, updated_at = NOW()
      WHERE id = $${paramCount}
      RETURNING id, email, name, updated_at
    `;

    const result = await db.query(query, values);

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.json({ data: result.rows[0] });
  } catch (error) {
    console.error('Error updating user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.delete('/api/users/:id', authenticateToken, requireRole('admin'), async (req, res) => {
  try {
    const { id } = req.params;

    const result = await db.query('DELETE FROM users WHERE id = $1 RETURNING id', [id]);

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(204).send();
  } catch (error) {
    console.error('Error deleting user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware (must be last)
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);

  // Don't leak error details in production
  const message = process.env.NODE_ENV === 'production'
    ? 'Internal server error'
    : err.message;

  res.status(err.status || 500).json({ error: message });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

#### Python/Flask Example

**✅ GOOD** - Production-ready Flask API:

```python
# app.py
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET')

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            # Remove 'Bearer ' prefix
            token = token.split()[1] if token.startswith('Bearer ') else token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = get_user_by_id(data['user_id'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# Role-based access control
def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            if current_user['role'] not in roles:
                return jsonify({'error': 'Insufficient permissions'}), 403
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator

# Input validation
def validate_user_input(data):
    errors = []

    if 'email' not in data or not data['email']:
        errors.append('Email is required')
    elif not is_valid_email(data['email']):
        errors.append('Invalid email format')

    if 'password' not in data or len(data['password']) < 8:
        errors.append('Password must be at least 8 characters')

    return errors

@app.route('/api/auth/register', methods=['POST'])
@limiter.limit("5 per hour")  # Stricter limit for registration
def register():
    data = request.get_json()

    # Validate input
    errors = validate_user_input(data)
    if errors:
        return jsonify({'errors': errors}), 422

    email = data['email']
    password = data['password']
    name = data.get('name', '')

    # Check if user exists
    if user_exists(email):
        return jsonify({'error': 'Email already registered'}), 409

    # Hash password
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # Create user
    user_id = create_user(email, hashed_password, name)

    # Generate JWT
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        'user': {
            'id': user_id,
            'email': email,
            'name': name
        },
        'token': token
    }), 201

@app.route('/api/auth/login', methods=['POST'])
@limiter.limit("10 per hour")
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    user = get_user_by_email(email)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode({
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        'user': {
            'id': user['id'],
            'email': user['email'],
            'name': user['name']
        },
        'token': token
    })

@app.route('/api/users', methods=['GET'])
@token_required
@role_required('admin')
def get_users(current_user):
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)

    # Pagination
    offset = (page - 1) * limit
    users = get_users_paginated(limit, offset)
    total = get_users_count()

    return jsonify({
        'data': users,
        'pagination': {
            'page': page,
            'limit': limit,
            'total': total,
            'pages': (total + limit - 1) // limit
        }
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
@token_required
def get_user(current_user, user_id):
    # Authorization check
    if current_user['role'] != 'admin' and current_user['id'] != user_id:
        return jsonify({'error': 'Access denied'}), 403

    user = get_user_by_id(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'data': user})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f'Internal error: {error}')
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
```

### 2. Database Design

#### SQL Schema Design Best Practices

**✅ GOOD** - Well-designed schema:

```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(100) NOT NULL,
  role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('user', 'admin', 'moderator')),
  email_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP NULL,  -- Soft deletes

  -- Indexes for performance
  INDEX idx_users_email (email),
  INDEX idx_users_created_at (created_at),
  INDEX idx_users_role (role)
);

-- Posts table (one-to-many with users)
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
  published_at TIMESTAMP NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_posts_user_id (user_id),
  INDEX idx_posts_status (status),
  INDEX idx_posts_published_at (published_at),
  FULLTEXT INDEX idx_posts_content (title, content)
);

-- Tags table (many-to-many with posts)
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL,
  slug VARCHAR(50) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_tags_slug (slug)
);

-- Junction table for many-to-many
CREATE TABLE post_tags (
  post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
  tag_id INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
  PRIMARY KEY (post_id, tag_id),

  INDEX idx_post_tags_post_id (post_id),
  INDEX idx_post_tags_tag_id (tag_id)
);

-- Sessions table for authentication
CREATE TABLE sessions (
  id VARCHAR(128) PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  expires_at TIMESTAMP NOT NULL,
  data JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_sessions_user_id (user_id),
  INDEX idx_sessions_expires_at (expires_at)
);

-- Audit log table
CREATE TABLE audit_logs (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
  action VARCHAR(50) NOT NULL,
  table_name VARCHAR(50) NOT NULL,
  record_id INTEGER,
  old_values JSONB,
  new_values JSONB,
  ip_address INET,
  user_agent TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_audit_logs_user_id (user_id),
  INDEX idx_audit_logs_table_name (table_name),
  INDEX idx_audit_logs_created_at (created_at)
);
```

#### Database Migrations (Node.js example with node-pg-migrate)

```javascript
// migrations/1707500000000_create_users_table.js
exports.up = (pgm) => {
  pgm.createTable('users', {
    id: 'id',
    email: { type: 'varchar(255)', notNull: true, unique: true },
    password_hash: { type: 'varchar(255)', notNull: true },
    name: { type: 'varchar(100)', notNull: true },
    role: {
      type: 'varchar(20)',
      default: 'user',
      check: "role IN ('user', 'admin', 'moderator')"
    },
    email_verified: { type: 'boolean', default: false },
    created_at: {
      type: 'timestamp',
      notNull: true,
      default: pgm.func('current_timestamp')
    },
    updated_at: {
      type: 'timestamp',
      notNull: true,
      default: pgm.func('current_timestamp')
    }
  });

  pgm.createIndex('users', 'email');
  pgm.createIndex('users', 'role');
};

exports.down = (pgm) => {
  pgm.dropTable('users');
};
```

**Run migrations**:
```bash
# Create new migration
npx node-pg-migrate create create-posts-table

# Run migrations
npx node-pg-migrate up

# Rollback last migration
npx node-pg-migrate down
```

#### ORM Usage (Sequelize example)

```javascript
// models/User.js
const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {
  const User = sequelize.define('User', {
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
      validate: {
        isEmail: true
      }
    },
    passwordHash: {
      type: DataTypes.STRING,
      allowNull: false,
      field: 'password_hash'
    },
    name: {
      type: DataTypes.STRING,
      allowNull: false,
      validate: {
        len: [2, 100]
      }
    },
    role: {
      type: DataTypes.ENUM('user', 'admin', 'moderator'),
      defaultValue: 'user'
    }
  }, {
    tableName: 'users',
    underscored: true,
    timestamps: true,
    paranoid: true // Enables soft deletes
  });

  User.associate = (models) => {
    User.hasMany(models.Post, {
      foreignKey: 'user_id',
      as: 'posts'
    });
  };

  return User;
};

// Usage
const user = await User.findOne({
  where: { email: 'user@example.com' },
  include: [{
    model: Post,
    as: 'posts',
    where: { status: 'published' },
    required: false
  }]
});
```

### 3. Authentication & Authorization

#### JWT Authentication

**✅ GOOD** - Secure JWT implementation:

```javascript
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

// Generate JWT
function generateToken(user) {
  const payload = {
    id: user.id,
    email: user.email,
    role: user.role
  };

  return jwt.sign(payload, process.env.JWT_SECRET, {
    expiresIn: '7d',
    issuer: 'salesai.com',
    audience: 'salesai-api'
  });
}

// Generate refresh token (store in database)
function generateRefreshToken() {
  return crypto.randomBytes(40).toString('hex');
}

// Verify JWT
function verifyToken(token) {
  try {
    return jwt.verify(token, process.env.JWT_SECRET, {
      issuer: 'salesai.com',
      audience: 'salesai-api'
    });
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      throw new Error('Token expired');
    }
    throw new Error('Invalid token');
  }
}

// Password hashing
async function hashPassword(password) {
  // 12 rounds = good balance between security and performance
  return await bcrypt.hash(password, 12);
}

async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

// Login endpoint
app.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body;

  // Get user from database
  const user = await db.getUserByEmail(email);

  if (!user || !(await verifyPassword(password, user.password_hash))) {
    // Don't reveal whether email or password was wrong
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Generate tokens
  const accessToken = generateToken(user);
  const refreshToken = generateRefreshToken();

  // Store refresh token in database with expiry
  await db.saveRefreshToken(user.id, refreshToken, {
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000) // 30 days
  });

  res.json({
    accessToken,
    refreshToken,
    user: {
      id: user.id,
      email: user.email,
      name: user.name,
      role: user.role
    }
  });
});

// Refresh token endpoint
app.post('/api/auth/refresh', async (req, res) => {
  const { refreshToken } = req.body;

  if (!refreshToken) {
    return res.status(401).json({ error: 'Refresh token required' });
  }

  // Verify refresh token in database
  const tokenData = await db.getRefreshToken(refreshToken);

  if (!tokenData || tokenData.expiresAt < new Date()) {
    return res.status(401).json({ error: 'Invalid or expired refresh token' });
  }

  const user = await db.getUserById(tokenData.user_id);

  // Generate new access token
  const accessToken = generateToken(user);

  res.json({ accessToken });
});
```

#### OAuth 2.0 Integration (Google example)

```javascript
const { OAuth2Client } = require('google-auth-library');

const client = new OAuth2Client(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

// Step 1: Redirect to Google OAuth
app.get('/api/auth/google', (req, res) => {
  const authorizeUrl = client.generateAuthUrl({
    access_type: 'offline',
    scope: ['profile', 'email'],
    state: generateRandomState() // CSRF protection
  });

  res.redirect(authorizeUrl);
});

// Step 2: Handle OAuth callback
app.get('/api/auth/google/callback', async (req, res) => {
  const { code, state } = req.query;

  // Verify state for CSRF protection
  if (!verifyState(state)) {
    return res.status(400).json({ error: 'Invalid state' });
  }

  try {
    // Exchange code for tokens
    const { tokens } = await client.getToken(code);
    client.setCredentials(tokens);

    // Get user info
    const ticket = await client.verifyIdToken({
      idToken: tokens.id_token,
      audience: process.env.GOOGLE_CLIENT_ID
    });

    const payload = ticket.getPayload();
    const { email, name, picture } = payload;

    // Find or create user
    let user = await db.getUserByEmail(email);

    if (!user) {
      user = await db.createUser({
        email,
        name,
        avatar: picture,
        oauth_provider: 'google',
        oauth_id: payload.sub
      });
    }

    // Generate our own JWT
    const accessToken = generateToken(user);

    // Redirect to frontend with token
    res.redirect(`${process.env.FRONTEND_URL}/auth/callback?token=${accessToken}`);
  } catch (error) {
    console.error('OAuth error:', error);
    res.redirect(`${process.env.FRONTEND_URL}/login?error=oauth_failed`);
  }
});
```

### 4. Security Best Practices

#### Input Validation & Sanitization

**✅ GOOD** - Comprehensive validation:

```javascript
const { body, param, query, validationResult } = require('express-validator');
const createDOMPurify = require('dompurify');
const { JSDOM } = require('jsdom');

const window = new JSDOM('').window;
const DOMPurify = createDOMPurify(window);

// Validation rules
const userValidation = {
  register: [
    body('email')
      .trim()
      .isEmail().withMessage('Invalid email format')
      .normalizeEmail(),

    body('password')
      .isLength({ min: 8 }).withMessage('Password must be at least 8 characters')
      .matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])/)
      .withMessage('Password must contain uppercase, lowercase, number, and special character'),

    body('name')
      .trim()
      .isLength({ min: 2, max: 100 }).withMessage('Name must be 2-100 characters')
      .matches(/^[a-zA-Z\s-']+$/).withMessage('Name contains invalid characters')
      .customSanitizer(value => DOMPurify.sanitize(value))
  ],

  updateProfile: [
    body('bio')
      .optional()
      .trim()
      .isLength({ max: 500 }).withMessage('Bio too long')
      .customSanitizer(value => DOMPurify.sanitize(value, {
        ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],
        ALLOWED_ATTR: ['href']
      }))
  ]
};

// Use in routes
app.post('/api/auth/register', userValidation.register, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() });
  }

  // Proceed with validated and sanitized data
});
```

#### SQL Injection Prevention

**❌ BAD** - Vulnerable to SQL injection:
```javascript
// NEVER DO THIS
const query = `SELECT * FROM users WHERE email = '${email}'`;
db.query(query);
```

**✅ GOOD** - Using parameterized queries:
```javascript
// PostgreSQL
const query = 'SELECT * FROM users WHERE email = $1';
const result = await db.query(query, [email]);

// MySQL
const query = 'SELECT * FROM users WHERE email = ?';
const result = await db.query(query, [email]);

// ORM (Sequelize)
const user = await User.findOne({
  where: { email: email }
});
```

#### Rate Limiting

```javascript
const rateLimit = require('express-rate-limit');
const RedisStore = require('rate-limit-redis');
const redis = require('redis');

const redisClient = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT
});

// General API rate limit
const apiLimiter = rateLimit({
  store: new RedisStore({
    client: redisClient,
    prefix: 'rl:api:'
  }),
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests, please try again later',
  standardHeaders: true,
  legacyHeaders: false
});

// Stricter limit for authentication endpoints
const authLimiter = rateLimit({
  store: new RedisStore({
    client: redisClient,
    prefix: 'rl:auth:'
  }),
  windowMs: 15 * 60 * 1000,
  max: 5, // Only 5 attempts per 15 minutes
  skipSuccessfulRequests: true, // Don't count successful requests
  message: 'Too many login attempts, please try again later'
});

app.use('/api/', apiLimiter);
app.use('/api/auth/', authLimiter);
```

#### CORS Configuration

```javascript
const cors = require('cors');

// Production CORS configuration
const corsOptions = {
  origin: function (origin, callback) {
    const allowedOrigins = [
      'https://salesai.com',
      'https://app.salesai.com',
      'https://admin.salesai.com'
    ];

    // Allow requests with no origin (mobile apps, Postman)
    if (!origin) return callback(null, true);

    if (allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true, // Allow cookies
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  exposedHeaders: ['X-Total-Count'], // Headers accessible to client
  maxAge: 600 // Cache preflight request for 10 minutes
};

app.use(cors(corsOptions));
```

### 5. Caching Strategies

#### Redis Caching

```javascript
const redis = require('redis');
const { promisify } = require('util');

const redisClient = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
  password: process.env.REDIS_PASSWORD
});

const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);
const delAsync = promisify(redisClient.del).bind(redisClient);

// Cache middleware
function cacheMiddleware(duration = 300) {
  return async (req, res, next) => {
    // Only cache GET requests
    if (req.method !== 'GET') {
      return next();
    }

    const key = `cache:${req.originalUrl}`;

    try {
      const cached = await getAsync(key);

      if (cached) {
        return res.json(JSON.parse(cached));
      }

      // Store original res.json
      const originalJson = res.json.bind(res);

      // Override res.json
      res.json = (data) => {
        // Cache the response
        setAsync(key, JSON.stringify(data), 'EX', duration);
        return originalJson(data);
      };

      next();
    } catch (error) {
      console.error('Cache error:', error);
      next();
    }
  };
}

// Usage
app.get('/api/posts', cacheMiddleware(600), async (req, res) => {
  // This will be cached for 10 minutes
  const posts = await db.getPosts();
  res.json({ data: posts });
});

// Invalidate cache on updates
app.post('/api/posts', async (req, res) => {
  const post = await db.createPost(req.body);

  // Invalidate posts list cache
  await delAsync('cache:/api/posts*');

  res.status(201).json({ data: post });
});
```

#### HTTP Caching Headers

```javascript
// Cache-Control for static assets
app.use('/static', express.static('public', {
  maxAge: '1y', // Cache for 1 year
  immutable: true
}));

// Cache-Control for API responses
app.get('/api/posts/:id', async (req, res) => {
  const post = await db.getPost(req.params.id);

  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }

  // Cache for 5 minutes, can be stale for 1 hour while revalidating
  res.set('Cache-Control', 'public, max-age=300, stale-while-revalidate=3600');

  // ETag for conditional requests
  const etag = generateETag(post);
  res.set('ETag', etag);

  // Check If-None-Match header
  if (req.headers['if-none-match'] === etag) {
    return res.status(304).send(); // Not Modified
  }

  res.json({ data: post });
});
```

### 6. Background Jobs & Queues

#### Bull Queue (Node.js)

```javascript
const Queue = require('bull');
const nodemailer = require('nodemailer');

// Create queue
const emailQueue = new Queue('email', {
  redis: {
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT
  }
});

// Define job processor
emailQueue.process(async (job) => {
  const { to, subject, html } = job.data;

  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  });

  await transporter.sendMail({
    from: process.env.EMAIL_FROM,
    to,
    subject,
    html
  });

  console.log(`Email sent to ${to}`);
});

// Add job to queue
async function sendEmail(to, subject, html) {
  await emailQueue.add({
    to,
    subject,
    html
  }, {
    attempts: 3, // Retry 3 times on failure
    backoff: {
      type: 'exponential',
      delay: 2000 // Start with 2s delay
    },
    removeOnComplete: true
  });
}

// Usage in API
app.post('/api/auth/register', async (req, res) => {
  const user = await db.createUser(req.body);

  // Send welcome email asynchronously
  await sendEmail(
    user.email,
    'Welcome to Sales AI',
    `<h1>Welcome, ${user.name}!</h1>`
  );

  res.status(201).json({ data: user });
});

// Monitor queue
emailQueue.on('completed', (job) => {
  console.log(`Job ${job.id} completed`);
});

emailQueue.on('failed', (job, err) => {
  console.error(`Job ${job.id} failed:`, err);
});
```

### 7. Error Handling & Logging

#### Centralized Error Handling

```javascript
// Custom error class
class AppError extends Error {
  constructor(message, statusCode, isOperational = true) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = isOperational;
    Error.captureStackTrace(this, this.constructor);
  }
}

// Error handling middleware
function errorHandler(err, req, res, next) {
  err.statusCode = err.statusCode || 500;
  err.status = err.status || 'error';

  if (process.env.NODE_ENV === 'production') {
    // Don't leak error details in production
    if (err.isOperational) {
      res.status(err.statusCode).json({
        status: err.status,
        message: err.message
      });
    } else {
      // Programming or unknown error: don't leak details
      console.error('ERROR:', err);
      res.status(500).json({
        status: 'error',
        message: 'Something went wrong'
      });
    }
  } else {
    // Development: send full error
    res.status(err.statusCode).json({
      status: err.status,
      message: err.message,
      stack: err.stack,
      error: err
    });
  }
}

// Async error wrapper
const catchAsync = (fn) => {
  return (req, res, next) => {
    fn(req, res, next).catch(next);
  };
};

// Usage
app.get('/api/users/:id', catchAsync(async (req, res, next) => {
  const user = await db.getUserById(req.params.id);

  if (!user) {
    return next(new AppError('User not found', 404));
  }

  res.json({ data: user });
}));

app.use(errorHandler);
```

#### Logging with Winston

```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'sales-ai-api' },
  transports: [
    // Write all logs to console
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    }),
    // Write errors to file
    new winston.transports.File({
      filename: 'logs/error.log',
      level: 'error'
    }),
    // Write all logs to file
    new winston.transports.File({
      filename: 'logs/combined.log'
    })
  ]
});

// HTTP request logging middleware
const morgan = require('morgan');

app.use(morgan('combined', {
  stream: {
    write: (message) => logger.info(message.trim())
  }
}));

// Usage
logger.info('Server started', { port: 3000 });
logger.error('Database connection failed', { error: err.message });
logger.warn('High memory usage', { usage: process.memoryUsage() });
```

## Usage Examples

### Example 1: Create RESTful API for Sales AI

**Trigger**: CEO requests API for dashboard data

**Process**:

1. **Design API endpoints**:
```
GET    /api/dashboard/metrics      # Get key metrics (MRR, churn, etc.)
GET    /api/dashboard/insights     # Get AI-generated insights
GET    /api/customers              # List customers
GET    /api/customers/:id          # Get customer details
POST   /api/integrations/salesforce # Connect Salesforce
```

2. **Create database schema**:
```sql
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  company_name VARCHAR(200) NOT NULL,
  industry VARCHAR(100),
  mrr DECIMAL(10, 2),
  churn_risk DECIMAL(3, 2),
  last_activity TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_customers_churn_risk ON customers(churn_risk);
```

3. **Implement endpoints with validation**
4. **Add caching for dashboard metrics**
5. **Test with Jest**

### Example 2: Implement Authentication System

**Trigger**: CTO needs secure authentication

**Process**:

1. **Install dependencies**:
```bash
npm install bcrypt jsonwebtoken express-validator express-rate-limit
```

2. **Create JWT authentication middleware**
3. **Implement register/login/refresh endpoints**
4. **Add rate limiting to prevent brute force**
5. **Test auth flow**

## Integration with Other Skills

### frontend-development
- frontend-development calls APIs → backend-development provides endpoints
- backend-development validates data → frontend-development displays errors

### tech-audit
- backend-development implements security → tech-audit reviews with OWASP checklist
- tech-audit finds vulnerabilities → backend-development patches

### finance-forecasting
- backend-development stores metrics → finance-forecasting calculates runway
- finance-forecasting needs data → backend-development provides API

## Best Practices

### 1. Use Environment Variables

**✅ GOOD** - .env file:
```bash
# .env (never commit to git!)
NODE_ENV=production
PORT=3000
DATABASE_URL=postgresql://user:pass@localhost:5432/salesai
REDIS_URL=redis://localhost:6379
JWT_SECRET=your-secret-key-min-32-chars
SMTP_HOST=smtp.gmail.com
SMTP_USER=noreply@salesai.com
SMTP_PASS=app-password
```

**Load with dotenv**:
```javascript
require('dotenv').config();

const dbUrl = process.env.DATABASE_URL;
```

### 2. Database Connection Pooling

**✅ GOOD** - Use connection pool:
```javascript
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 20, // Maximum connections
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});

// Use pool instead of individual connections
const result = await pool.query('SELECT * FROM users WHERE id = $1', [userId]);
```

### 3. Graceful Shutdown

**✅ GOOD** - Handle shutdown gracefully:
```javascript
const server = app.listen(PORT);

process.on('SIGTERM', () => {
  console.log('SIGTERM received, closing server gracefully');

  server.close(() => {
    console.log('HTTP server closed');

    // Close database connections
    pool.end(() => {
      console.log('Database pool closed');
      process.exit(0);
    });
  });

  // Force shutdown after 10 seconds
  setTimeout(() => {
    console.error('Forcing shutdown');
    process.exit(1);
  }, 10000);
});
```

## Troubleshooting

### Problem: "Database connection pool exhausted"

**Solution**:
1. Check for missing `client.release()` calls
2. Increase pool size: `max: 20` → `max: 50`
3. Add connection timeout: `connectionTimeoutMillis: 2000`
4. Monitor with `pool.totalCount`, `pool.idleCount`

### Problem: "JWT token expired immediately"

**Solution**:
1. Check server clock sync (JWT uses timestamps)
2. Verify `expiresIn` is set correctly
3. Check if frontend is storing token properly

### Problem: "CORS errors in production"

**Solution**:
1. Verify `origin` in CORS config matches frontend domain
2. Check if `credentials: true` is set (for cookies)
3. Ensure preflight OPTIONS requests are handled

### Problem: "npm ci fails in Dockerfile for backend API"

**Error**:
```
npm error The `npm ci` command can only install with an existing package-lock.json
```

**Причина**: Backend API имеет отдельную package.json в `api/` директории, но Dockerfile копирует только package.json.

**❌ BAD**:
```dockerfile
FROM node:18-alpine AS backend-builder
WORKDIR /app
COPY api/package.json ./
RUN npm ci --only=production
```

**✅ GOOD**:
```dockerfile
FROM node:18-alpine AS backend-builder
WORKDIR /app
COPY api/package.json api/package-lock.json ./
RUN npm ci --only=production
```

**Профилактика**:
- ВСЕГДА копировать lock files вместе с package.json
- Для monorepo: копировать lock files из правильной директории
- Backend в `api/` требует `api/package-lock.json`

### Problem: "Backend dependencies missing in production Docker image"

**Причина**: Multi-stage build копирует только production dependencies, но пропускает devDependencies нужные для build.

**Solution**:
```dockerfile
# Stage 1: Build (with ALL dependencies)
FROM node:18-alpine AS builder
COPY package.json package-lock.json ./
RUN npm ci  # Включает devDependencies для build

# Stage 2: Production (only production deps)
FROM node:18-alpine
COPY package.json package-lock.json ./
RUN npm ci --only=production  # Только production
COPY --from=builder /app/dist ./dist
```

**Профилактика**: Разделять build stage (все deps) и production stage (только prod deps)

---

### Problem: "API returns 500 error: Failed to submit request" (Missing environment variables)

**Error в frontend**:
```
Failed to submit request. Please try again later.
```

**Error в backend logs**:
```javascript
❌ Error submitting phone: Error: Telegram configuration missing
```

**Причина**:
- Environment variables (API keys, secrets) не переданы в container
- Backend не может выполнить запрос из-за отсутствия credentials
- В staging/production secrets не настроены в GitHub

**Diagnosis**:
```bash
# Check container logs
docker compose logs | grep "Telegram Bot"

# BAD - credentials missing:
🤖 Telegram Bot: Not configured ❌
💬 Chat ID: Not configured ❌

# GOOD - credentials configured:
🤖 Telegram Bot: Configured ✅
💬 Chat ID: Configured ✅
```

**Solution - Add GitHub Secrets**:
```
GitHub → Repository → Settings → Secrets and variables → Actions

Add secrets:
- TELEGRAM_BOT_TOKEN_STAGING
- TELEGRAM_CHAT_ID_STAGING
- TELEGRAM_BOT_TOKEN_PROD (for production)
- TELEGRAM_CHAT_ID_PROD (for production)
```

**Redeploy после добавления secrets**:
```bash
# Option 1: Git push (triggers CI/CD)
git commit --allow-empty -m "Trigger redeploy with secrets"
git push origin feature/branch

# Option 2: Manual redeploy на сервере
docker compose down && docker compose up -d
```

**Профилактика**:
- ВСЕГДА настраивать secrets ПЕРЕД первым deployment
- Проверять логи при старте backend: "Configured ✅" для всех credentials
- Добавлять startup validation для critical environment variables
- Использовать health check endpoint для проверки configuration

**Backend code pattern для validation**:
```javascript
// Validate required env vars at startup
const REQUIRED_ENV_VARS = ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_CHAT_ID'];
const missing = REQUIRED_ENV_VARS.filter(v => !process.env[v]);
if (missing.length > 0) {
  console.error(`❌ Missing required environment variables: ${missing.join(', ')}`);
  process.exit(1);  // Fail fast
}
```

---

### Problem: "express-rate-limit ValidationError: trust proxy setting is false"

**Error**:
```
ValidationError: The 'X-Forwarded-For' header is set but the Express 'trust proxy' setting is false
```

**Причина**:
- Backend за reverse proxy (Nginx, Traefik, ALB)
- Proxy передает `X-Forwarded-For` header с real IP
- Express по умолчанию не доверяет proxy → rate limiting не работает правильно

**Solution**:
```javascript
const app = express();

// REQUIRED when behind reverse proxy
app.set('trust proxy', true);

// Now rate limiting will use real IP from X-Forwarded-For
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5
});
```

**Профилактика**:
- ВСЕГДА добавлять `app.set('trust proxy', true)` когда backend за proxy
- Без этого: rate limiting блокирует всех пользователей (все видятся как один IP proxy)
- Тестировать rate limiting после deployment

---

### Problem: "Telegram API error: can't parse entities" (Markdown parsing)

**Error**:
```
Telegram API error: Bad Request: can't parse entities: Can't find end of the entity starting at byte offset 253
```

**Причина**:
- Используется `parse_mode: 'Markdown'` в Telegram message
- Но есть неэкранированные специальные символы (`_`, `*`, `[`, `` ` ``, etc.)
- Telegram не может распарсить Markdown

**❌ BAD**:
```javascript
const message = `*Телефон:* ${phone}\n_Источник:_ ${source}`;
fetch(url, {
  body: JSON.stringify({
    text: message,
    parse_mode: 'Markdown'  // Fails if phone contains _
  })
});
```

**✅ GOOD - Option 1 (Plain text)**:
```javascript
const message = `Телефон: ${phone}\nИсточник: ${source}`;
fetch(url, {
  body: JSON.stringify({
    text: message
    // No parse_mode - safe with any characters
  })
});
```

**✅ GOOD - Option 2 (HTML)**:
```javascript
const message = `<b>Телефон:</b> ${phone}\n<b>Источник:</b> ${source}`;
fetch(url, {
  body: JSON.stringify({
    text: message,
    parse_mode: 'HTML'  // More forgiving than Markdown
  })
});
```

**Профилактика**:
- Избегать Markdown если данные содержат user input
- Использовать HTML или plain text
- Если обязательно Markdown - экранировать спецсимволы: `_`, `*`, `[`, `]`, `(`, `)`, `~`, `` ` ``, `>`, `#`, `+`, `-`, `=`, `|`, `{`, `}`, `.`, `!`

---

## Version History

- **2026-02-10**: Created comprehensive backend-development skill for CTO
  - RESTful API design, authentication, database design
  - Security best practices (OWASP, rate limiting, input validation)
  - Caching, background jobs, error handling
  - Integration with frontend-development, tech-audit, finance-forecasting skills

- **2026-02-10**: Added backend Dockerfile and runtime errors
  - Missing api/package-lock.json in Docker build
  - Multi-stage build dependency management
  - Missing environment variables (API keys, secrets) causing 500 errors
  - express-rate-limit ValidationError (trust proxy not set)
  - Telegram Markdown parsing errors with user input
