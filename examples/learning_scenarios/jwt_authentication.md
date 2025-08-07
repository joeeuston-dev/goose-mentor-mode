# Authentication JWT Learning Scenario

## Overview
This scenario teaches JWT authentication implementation through guided discovery, focusing on security principles and best practices.

## Learning Objectives
- Understand JWT structure and purpose
- Implement secure token validation
- Handle token expiration and refresh
- Apply security best practices for token management

## Scenario Context
**Developer Request**: "I need to add JWT authentication to this API"

**Context**:
- Junior developer, 6 months experience
- Working on REST API project
- Timeline: Normal development pace (no rush)
- Previous auth experience: Basic session-based auth

## Interaction Flow

### Phase 1: Discovery Questions (Guided Level)

**Mentor**: "Great! Authentication is a critical security layer. Before we implement JWT, let's explore what you already know. Can you tell me what JWT stands for and why we might choose it over traditional session-based authentication?"

**Expected Developer Response**: Basic understanding or uncertainty

**Follow-up Questions**:
1. "What information do you think should be stored in a JWT token?"
2. "What security risks should we consider when using JWTs?"
3. "How do you think token expiration should be handled?"

### Phase 2: Concept Building

**Key Concepts to Cover**:
- JWT structure (header.payload.signature)
- Stateless vs. stateful authentication
- Security considerations (never store sensitive data)
- Token expiration and refresh strategies
- Signing algorithms (RS256 vs HS256)

**Teaching Approach**:
```
Start with basic structure → Build to security considerations → Advanced patterns
```

### Phase 3: Progressive Implementation

#### Step 1: Token Structure Understanding
```javascript
// Show JWT structure first
const exampleJWT = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.signature"

// Ask: "What do you notice about this structure?"
// Guide to understanding the three parts separated by dots
```

#### Step 2: Implementation with Questions
```javascript
// Question: "What library should we use for JWT handling?"
const jwt = require('jsonwebtoken');

// Question: "What information belongs in the payload?"
const payload = {
    userId: user.id,
    email: user.email,
    // Question: "Should we include the password hash here?"
    // Guide to understanding: NEVER include sensitive data
};

// Question: "How should we sign this token?"
const token = jwt.sign(payload, process.env.JWT_SECRET, {
    expiresIn: '1h'  // Question: "Why do tokens need expiration?"
});
```

#### Step 3: Validation Implementation
```javascript
// Question: "Where in our middleware should we validate tokens?"
function authenticateToken(req, res, next) {
    // Question: "How does the client send us the token?"
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN
    
    if (!token) {
        // Question: "What HTTP status should we return for missing tokens?"
        return res.sendStatus(401);
    }
    
    // Question: "What could go wrong during verification?"
    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) {
            // Question: "How should we handle expired vs invalid tokens?"
            return res.sendStatus(403);
        }
        req.user = user;
        next();
    });
}
```

### Phase 4: Knowledge Validation

**Comprehension Questions**:
1. "Can you explain why we use Bearer tokens in the Authorization header?"
2. "What would happen if we stored the JWT secret in our code instead of environment variables?"
3. "How would you handle a user logging out with JWT tokens?"
4. "What's the security difference between RS256 and HS256 signing?"

**Scenario Testing**:
1. "A user reports they keep getting logged out after an hour. How would you investigate?"
2. "You need to revoke a user's access immediately. How would you handle this with JWTs?"
3. "The mobile team wants tokens that last 30 days. What security considerations should you discuss?"

### Phase 5: Advanced Concepts (If Understanding Demonstrated)

**Refresh Token Pattern**:
```javascript
// Question: "Why might we want two different types of tokens?"
const accessToken = jwt.sign(payload, process.env.ACCESS_SECRET, { expiresIn: '15m' });
const refreshToken = jwt.sign(payload, process.env.REFRESH_SECRET, { expiresIn: '7d' });

// Explain the security benefits of short-lived access tokens
```

**Error Handling Best Practices**:
```javascript
// Question: "What information should we include in error responses?"
function handleJWTError(error) {
    if (error.name === 'TokenExpiredError') {
        // Don't reveal internal details to potential attackers
        return { message: 'Token expired' };
    } else if (error.name === 'JsonWebTokenError') {
        return { message: 'Invalid token' };
    }
    // Question: "Should we log the actual error somewhere?"
    console.error('JWT validation error:', error); // For debugging
    return { message: 'Authentication failed' };
}
```

## Success Criteria

**Understanding Indicators**:
- Can explain JWT vs session trade-offs
- Understands why sensitive data shouldn't be in JWTs
- Knows how to handle token expiration
- Recognizes security implications of signing algorithms

**Implementation Indicators**:
- Correctly implements token validation middleware
- Properly handles error cases
- Uses environment variables for secrets
- Implements appropriate HTTP status codes

**Advanced Indicators**:
- Suggests refresh token pattern for improved security
- Considers token revocation strategies
- Understands CORS implications for token-based auth
- Can debug token-related issues independently

## Common Mistakes & Guidance

**Mistake**: "Let me put the user's password in the JWT payload"
**Guidance**: "Great question! What kind of information do you think attackers could access if they got hold of a JWT token? Remember, JWTs are encoded, not encrypted."

**Mistake**: "I'll use a simple string like 'secret' for the JWT secret"
**Guidance**: "Security-wise, what makes a good secret? Think about what an attacker might try to guess or find in your codebase."

**Mistake**: "Tokens should never expire so users don't get logged out"
**Guidance**: "What would happen if someone stole a user's token? How could we limit the damage?"

## Extension Opportunities

**If Developer Shows Advanced Interest**:
- OAuth2 flows and JWT usage
- Microservices authentication patterns
- Token introspection and revocation
- Security scanning for JWT vulnerabilities

**Real-World Applications**:
- Mobile app authentication strategies
- Single Sign-On (SSO) implementations
- API gateway authentication patterns
- Serverless authentication with JWTs
