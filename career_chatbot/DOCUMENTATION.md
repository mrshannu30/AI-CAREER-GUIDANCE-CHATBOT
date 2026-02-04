# AI Career Guidance Chatbot - Complete Documentation

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Usage Guide](#usage-guide)
5. [API Reference](#api-reference)
6. [Machine Learning Models](#machine-learning-models)
7. [Database Schema](#database-schema)
8. [Frontend Features](#frontend-features)
9. [Configuration](#configuration)
10. [Troubleshooting](#troubleshooting)

---

## Overview

The **AI Career Guidance Chatbot** is an intelligent system designed to help students and professionals:

- Discover their career potential based on skills and education
- Get personalized career recommendations
- Receive step-by-step guidance for career development
- Plan their educational journey
- Understand job market trends and salary expectations

### Key Features

✅ **Natural Language Processing** - Understands student queries in conversational language
✅ **ML-Based Recommendations** - Intelligent career suggestions based on profile
✅ **Skill Assessment** - Analyzes skills and identifies gaps
✅ **Study Planning** - Creates personalized educational roadmaps
✅ **Progress Tracking** - Maintains conversation history and user profile
✅ **Real-time Guidance** - Immediate contextual responses

---

## Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Web UI)                     │
│  HTML/CSS/JavaScript - Interactive Chat Interface       │
└─────────────────┬───────────────────────────────────────┘
                  │
                  │ HTTP/REST API
                  │
┌─────────────────┴───────────────────────────────────────┐
│                  Flask Application                       │
│  ┌──────────────────────────────────────────────────┐   │
│  │  API Routes                                      │   │
│  │  • /api/chat/* - Chat operations                │   │
│  │  • /api/user/* - User management               │   │
│  └──────────────────────────────────────────────────┘   │
└──────┬──────────────────────────────────┬────────────────┘
       │                                  │
   ┌───┴──────────────────────────┐   ┌──┴───────────────────┐
   │   ML/AI Components           │   │  Database            │
   │  • NLP Processor             │   │  SQLAlchemy Models   │
   │  • Intent Classifier         │   │  • Users             │
   │  • Career Recommender        │   │  • Conversations     │
   │  • Response Generator        │   │  • Careers           │
   │                              │   │  • Recommendations   │
   └──────────────────────────────┘   └──────────────────────┘
```

### Component Breakdown

#### 1. Frontend Layer
- Responsive HTML5 UI
- Real-time chat interface
- User profile management
- Career recommendations display
- JavaScript for interactive features

#### 2. API Layer
- RESTful endpoints for chat and user management
- JSON request/response format
- Error handling and validation

#### 3. Business Logic Layer
- NLP processing and intent classification
- Career matching algorithm
- Response generation
- User profile management

#### 4. Data Layer
- SQLAlchemy ORM models
- SQLite database
- Conversation history tracking
- Career database

---

## Installation

### System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Storage**: 500MB free space

### Step-by-Step Installation

#### 1. Download Project

```bash
# Navigate to your workspace
cd "d:\Final Year Project"
```

#### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependency Overview

| Package | Purpose | Version |
|---------|---------|---------|
| Flask | Web framework | 2.3.0 |
| Flask-SQLAlchemy | Database ORM | 3.0.5 |
| Flask-CORS | Enable CORS | 4.0.0 |
| scikit-learn | ML algorithms | 1.2.2 |
| numpy | Numerical computing | 1.24.3 |
| pandas | Data processing | 2.0.3 |
| nltk | NLP toolkit | 3.8.1 |
| spacy | Advanced NLP | 3.5.0 |

#### 4. Download NLP Models (Optional but Recommended)

```bash
python -m nltk.downloader punkt averaged_perceptron_tagger
python -m spacy download en_core_web_sm
```

---

## Usage Guide

### Starting the Application

#### Option 1: Using Startup Script

**Windows:**
```bash
start.bat
```

**macOS/Linux:**
```bash
chmod +x start.sh
./start.sh
```

#### Option 2: Manual Start

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run application
python run.py
```

### Accessing the Application

1. Open browser and go to: **http://localhost:5000**
2. Click "Start Chatting Now"
3. Fill in your email and name
4. Start the conversation!

### User Workflow

#### Phase 1: User Registration
```
1. Enter email address
2. Enter your name
3. System creates user profile
4. Bot greets you
```

#### Phase 2: Profile Building
```
1. Tell bot about your studies
   "I'm studying computer science"
   
2. Share your skills
   "I know Python, Java, and SQL"
   
3. Describe experience level
   "I'm intermediate with 2 years experience"
```

#### Phase 3: Get Recommendations
```
1. Ask for career guidance
   "What careers suit me?"
   "Guide me on building a career"
   
2. Receive recommendations
   Top 3-5 careers with match scores
   
3. Get actionable next steps
   Skills to learn, projects to build
```

#### Phase 4: Track Progress
- View profile in right panel
- Check conversation history
- See updated recommendations

### Example Conversation

```
User: Hello!
Bot: Hello! I'm your AI Career Guidance Assistant. I'm here to help you plan 
     your career journey. How can I assist you today?

User: I'm studying computer science and want career guidance
Bot: That's great! I'd like to learn more about you to provide better guidance.
     Tell me about your skills and experience level.

User: I have skills in Python, machine learning, and data analysis. 
      I'm intermediate level.
Bot: Excellent! Based on your profile, here are your top career recommendations:
     
     1. **Data Scientist** (Match: 95%)
        - Description: Analyze data and build ML models for insights
        - Salary Range: $90000-$160000
        - Growth Rate: Very High
     
     [Additional recommendations...]

User: What should I do next?
Bot: Here's your personalized career development roadmap:
     
     1. **Complete relevant education** (Priority: High)
        - Ensure completion in Computer Science
        - Timeline: 6-12 months
     
     2. **Develop key skills** (Priority: High)
        - Learn: Deep Learning, Big Data, Cloud Technologies
        - Timeline: 6-12 months
     
     [Additional steps...]
```

---

## API Reference

### User Management APIs

#### Create User
```http
POST /api/user/create
Content-Type: application/json

{
  "email": "student@example.com",
  "name": "John Doe"
}

Response:
{
  "user_id": 1,
  "email": "student@example.com",
  "name": "John Doe",
  "message": "User created successfully!"
}
```

#### Get User Profile
```http
GET /api/user/get/<user_id>

Response:
{
  "id": 1,
  "email": "student@example.com",
  "name": "John Doe",
  "current_study": "Computer Science",
  "current_skills": ["python", "machine learning"],
  "work_experience": [],
  "study_status": "studying",
  "preferences": {}
}
```

#### Update User Profile
```http
PUT /api/user/update/<user_id>
Content-Type: application/json

{
  "current_study": "Computer Science",
  "current_skills": ["python", "machine learning", "sql"],
  "study_status": "completed"
}

Response:
{
  "message": "User updated successfully",
  "user": { ... }
}
```

#### Get Complete Profile
```http
GET /api/user/profile/<user_id>

Response:
{
  "profile": {
    "id": 1,
    "email": "student@example.com",
    "name": "John Doe",
    "current_study": "Computer Science",
    "current_skills": ["python", "machine learning"],
    "created_at": "2025-01-28T10:00:00",
    "updated_at": "2025-01-28T10:30:00"
  }
}
```

### Chat APIs

#### Send Message
```http
POST /api/chat/message
Content-Type: application/json

{
  "message": "I'm studying computer science",
  "user_id": 1
}

Response:
{
  "user_message": "I'm studying computer science",
  "bot_response": "That's great! Tell me more...",
  "intent": "career_guidance",
  "confidence": 0.95
}
```

#### Get Recommendations
```http
GET /api/chat/get-recommendations/<user_id>

Response:
{
  "recommendations": [
    {
      "career": "Data Scientist",
      "score": 95.0,
      "description": "Analyze data and build ML models",
      "salary_range": "$90000-$160000",
      "growth_rate": "Very High",
      "missing_skills": ["deep learning", "spark"]
    },
    ...
  ]
}
```

#### Get Conversation History
```http
GET /api/chat/get-conversation-history/<user_id>

Response:
{
  "history": [
    {
      "user_message": "Hello",
      "bot_response": "Hello! How can I help?",
      "intent": "greetings",
      "timestamp": "2025-01-28T10:00:00"
    },
    ...
  ]
}
```

---

## Machine Learning Models

### 1. Intent Classification Model

**Purpose**: Understand what the user wants

**Algorithm**: Random Forest Classifier + TF-IDF

**Training Data**: 100+ labeled examples

**Intent Classes**:
- `greetings` - Simple greeting
- `career_guidance` - Asking for career advice
- `skill_assessment` - Evaluating skills
- `career_exploration` - Exploring different careers
- `study_path` - Questions about education
- `job_search` - Job hunting related
- `skill_development` - Learning new skills
- `salary_info` - Salary inquiries
- `education_path` - Education planning
- `general_info` - General questions

**Example**:
```python
Input: "I want to become a data scientist, what should I do?"
Output: Intent: career_guidance, Confidence: 0.92
```

### 2. Career Recommendation Engine

**Purpose**: Match user profile with suitable careers

**Algorithm**: Weighted scoring with cosine similarity

**Matching Factors**:
1. **Skill Match** (40% weight)
   - Compares user skills with career requirements
   - Score: 0-100%

2. **Education Match** (30% weight)
   - Matches educational background
   - Score: 0-100%

3. **Experience Level** (30% weight)
   - Evaluates career readiness
   - Score: 0-100%

**Formula**:
```
Total Score = (Skill Score × 0.4) + (Education Score × 0.3) + (Experience Score × 0.3)
```

**Example**:
```python
User Profile:
- Skills: Python, Machine Learning, SQL
- Education: Computer Science
- Experience: Intermediate

Top Match: Data Scientist (95%)
- Skill Match: 100%
- Education Match: 100%
- Experience Match: 85%
```

### 3. Information Extraction

**Purpose**: Extract relevant information from user messages

**Methods**:
- Keyword matching for skills
- String similarity for field of study
- Pattern matching for experience level

**Extracted Information**:
- Field of study
- Skills mentioned
- Experience level (beginner/intermediate/advanced)
- Career interests

---

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    name VARCHAR(120) NOT NULL,
    current_study VARCHAR(200),
    current_skills TEXT,  -- JSON array
    work_experience TEXT, -- JSON array
    study_status VARCHAR(50),
    preferences TEXT,     -- JSON object
    created_at DATETIME,
    updated_at DATETIME
);
```

### Conversation History Table
```sql
CREATE TABLE conversation_history (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    intent VARCHAR(100),
    timestamp DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Careers Table
```sql
CREATE TABLE careers (
    id INTEGER PRIMARY KEY,
    title VARCHAR(120) UNIQUE NOT NULL,
    description TEXT,
    required_skills TEXT,  -- JSON array
    required_education TEXT, -- JSON array
    average_salary VARCHAR(100),
    job_growth_rate VARCHAR(50),
    related_fields TEXT,   -- JSON array
    created_at DATETIME
);
```

### Career Recommendations Table
```sql
CREATE TABLE career_recommendations (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    career_id INTEGER NOT NULL,
    match_score FLOAT,
    reasoning TEXT,
    next_steps TEXT,       -- JSON array
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (career_id) REFERENCES careers(id)
);
```

---

## Frontend Features

### 1. Home Page
- Welcome message
- Feature highlights
- How it works section
- Call-to-action button

### 2. Chat Interface

**Components**:
- **Message Container**: Displays conversation
- **Input Field**: User message entry
- **Profile Panel**: Shows user information
- **Recommendations Panel**: Career suggestions
- **Setup Modal**: Initial user registration

**Features**:
- Real-time message sending
- Automatic scroll to latest message
- Typing indicator while bot processes
- Message formatting (bold, lists, etc.)
- Responsive design for mobile

### 3. User Profile Panel
Displays:
- User name
- Current field of study
- Skills
- Study status

### 4. Recommendations Panel
Shows:
- Career title
- Match percentage
- Description
- Salary range
- Job growth rate
- Skills to learn

---

## Configuration

### Environment Variables (.env)

```
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=sqlite:///career_chatbot.db

# Debug Mode
DEBUG=True
```

### Flask Configuration (config.py)

**Development**:
```python
DEBUG = True
TESTING = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///career_chatbot.db'
```

**Production**:
```python
DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@host/dbname'
SECRET_KEY = 'your-production-secret-key'
```

---

## Troubleshooting

### Common Issues & Solutions

#### 1. Port 5000 Already in Use

**Error**: `Address already in use`

**Solution**:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

#### 2. Module Import Errors

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt

# Verify installation
pip list | grep Flask
```

#### 3. Database Errors

**Error**: `OperationalError: database is locked`

**Solution**:
```bash
# Reset database
rm career_chatbot.db
python run.py
```

#### 4. NLP Model Not Found

**Error**: `ResourceNotFoundError` from nltk

**Solution**:
```bash
python -m nltk.downloader punkt averaged_perceptron_tagger
```

#### 5. Slow Response Times

**Causes**:
- Large conversation history
- Slow database queries
- ML model loading

**Solutions**:
- Clear old conversations
- Add database indexes
- Use caching

### Debugging Mode

Enable detailed logging:
```python
# In run.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Testing Models

Run the test script:
```bash
python test_models.py
```

---

## Performance Optimization

### Database Optimization
```python
# Add indexes for faster queries
db.Index('idx_user_email', User.email)
db.Index('idx_conversation_user', ConversationHistory.user_id)
```

### Caching
- Browser caching for static files
- Session caching for user data
- In-memory caching for ML models

### Load Reduction
- Paginate conversation history
- Lazy load recommendations
- Compress API responses

---

## Future Enhancement Ideas

1. **Advanced Features**
   - Voice input/output
   - Video tutorials
   - Resume analysis
   - Job posting integration

2. **ML Improvements**
   - Deep learning models
   - Sentiment analysis
   - Behavioral prediction
   - Personalized learning paths

3. **Scaling**
   - Multi-language support
   - Database sharding
   - Microservices architecture
   - Cloud deployment (AWS, Azure, GCP)

4. **Analytics**
   - User engagement metrics
   - Career path success rates
   - Model performance tracking
   - User satisfaction scoring

---

## Support & Resources

### Documentation Files
- `README.md` - Quick start guide
- `ARCHITECTURE.md` - System design
- `API_DOCS.md` - Complete API reference
- `DEPLOYMENT.md` - Production setup

### External Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Guide](https://scikit-learn.org/)
- [NLTK Book](https://www.nltk.org/book/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)

---

**Last Updated**: January 28, 2025
**Version**: 1.0.0
