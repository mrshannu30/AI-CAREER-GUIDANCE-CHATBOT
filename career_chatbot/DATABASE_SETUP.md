# Database Setup & Configuration Guide

## Current Status: ✅ SQLite Database Ready

Your chatbot is currently set up with **SQLite** database, which is perfect for development and local testing.

---

## 📊 Current Database Setup

### SQLite (Default)
- **File Location**: `d:\Final Year Project\career_chatbot\career_chatbot.db`
- **File Size**: 36 KB
- **Status**: ✅ Active and running
- **Tables**: 4 (Users, Conversations, Careers, CareerRecommendations)
- **Records**: 12 careers loaded

---

## 🔄 Switch to MySQL (Optional)

If you want to use MySQL instead of SQLite, follow these steps:

### Step 1: Install MySQL

**Windows**:
1. Download from: https://dev.mysql.com/downloads/mysql/
2. Run installer and follow setup
3. Remember the root password
4. Default port: 3306

**macOS**:
```bash
brew install mysql
brew services start mysql
```

**Linux (Ubuntu)**:
```bash
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
```

### Step 2: Create Database

Open terminal/command prompt and run:
```bash
mysql -u root -p
```

Then execute:
```sql
-- Create database
CREATE DATABASE career_chatbot;

-- Create user
CREATE USER 'chatbot_user'@'localhost' IDENTIFIED BY 'chatbot_password_123';

-- Grant permissions
GRANT ALL PRIVILEGES ON career_chatbot.* TO 'chatbot_user'@'localhost';

-- Apply
FLUSH PRIVILEGES;

-- Exit
EXIT;
```

### Step 3: Update `.env` Configuration

Edit `.env` file and change:

```env
# Change from SQLite to MySQL
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_USER=chatbot_user
DB_PASSWORD=chatbot_password_123
DB_NAME=career_chatbot
DATABASE_URL=mysql+pymysql://chatbot_user:chatbot_password_123@localhost:3306/career_chatbot
```

### Step 4: Initialize Database

```bash
cd "d:\Final Year Project\career_chatbot"
python init_db.py
```

### Step 5: Verify Connection

```bash
python test_db_connection.py
```

Should show:
```
✅ Successfully connected to MySQL database!
📚 Career records: 12
```

---

## 📂 Database Files & Locations

### SQLite
- **Main DB File**: `career_chatbot.db` (in project root)
- **Config**: `.env` with `DB_TYPE=sqlite`

### MySQL
- **Server**: localhost:3306
- **Database**: career_chatbot
- **Config**: `.env` with `DB_TYPE=mysql`

---

## 🗄️ Database Tables

### 1. Users Table
```
Stores user profiles
├── id (primary key)
├── email (unique)
├── name
├── current_study
├── current_skills (JSON)
├── work_experience (JSON)
├── study_status
├── preferences (JSON)
├── created_at
└── updated_at
```

### 2. Careers Table
```
Career information database
├── id (primary key)
├── title (unique)
├── description
├── required_skills (JSON)
├── required_education (JSON)
├── average_salary
├── job_growth_rate
├── related_fields (JSON)
└── created_at
```

### 3. ConversationHistory Table
```
Chat history tracking
├── id (primary key)
├── user_id (foreign key → users.id)
├── user_message
├── bot_response
├── intent
└── timestamp
```

### 4. CareerRecommendations Table
```
Stored recommendations
├── id (primary key)
├── user_id (foreign key → users.id)
├── career_id (foreign key → careers.id)
├── match_score
├── reasoning
├── next_steps (JSON)
└── created_at
```

---

## 🧪 Database Testing

### Test Connection
```bash
python test_db_connection.py
```

### Test with Sample Data
```bash
# Create a test user
python -c "
from app import create_app
from app.models.database import db, User
import json

app = create_app()
with app.app_context():
    user = User(
        email='test@example.com',
        name='Test User',
        current_study='Computer Science',
        current_skills=json.dumps(['Python', 'JavaScript']),
        work_experience=json.dumps([]),
        preferences=json.dumps({})
    )
    db.session.add(user)
    db.session.commit()
    print(f'✓ Test user created with ID: {user.id}')
"
```

---

## 📋 Database Management

### View Database Info

**SQLite**:
```bash
# Check file size
Get-Item "career_chatbot.db" | Select-Object Length
```

**MySQL**:
```bash
mysql -u chatbot_user -p career_chatbot
SHOW TABLES;
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM careers;
```

### Backup Database

**SQLite**:
```bash
# Copy the file
copy career_chatbot.db career_chatbot_backup.db
```

**MySQL**:
```bash
mysqldump -u chatbot_user -p career_chatbot > backup.sql
```

### Reset Database

**SQLite**:
```bash
# Delete and reinitialize
rm career_chatbot.db
python init_db.py
```

**MySQL**:
```bash
python -c "
from app import create_app
from app.models.database import db

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    print('✓ Database reset')
"
python init_db.py
```

---

## 🔐 Security Notes

### SQLite
- Simple file-based database
- Good for development/testing
- **Limitation**: Not suitable for production with multiple users

### MySQL
- Client-server architecture
- Better for production
- **Security recommendations**:
  - Change default password
  - Use strong passwords
  - Restrict user permissions
  - Use firewall rules
  - Enable SSL connections
  - Don't expose credentials in code (use .env)

---

## ⚡ Performance Comparison

| Feature | SQLite | MySQL |
|---------|--------|-------|
| **Setup Time** | Instant | 5-10 min |
| **Query Speed** | Fast | Very Fast |
| **Concurrent Users** | Limited | Excellent |
| **Storage** | Single file | Server-based |
| **Backup** | Easy (copy file) | Advanced tools |
| **Development** | Excellent | Good |
| **Production** | Not recommended | Recommended |

---

## 🛠️ Troubleshooting

### SQLite Issues

**"Database file not found"**
```bash
python init_db.py
```

**"Database locked"**
- Close all database connections
- Delete lock file if exists
- Restart the app

### MySQL Issues

**"Access denied"**
```bash
# Verify credentials
mysql -u chatbot_user -p career_chatbot
```

**"Connection refused"**
- Check MySQL is running
- Verify host, port, database name
- Check firewall

**"Database does not exist"**
```bash
mysql -u root -p
CREATE DATABASE career_chatbot;
```

### Connection Test Failed?

Run diagnostic:
```bash
python test_db_connection.py
```

This will show:
- Database type
- Connection status
- Record counts
- File location (for SQLite)

---

## 📖 Useful Commands

```bash
# Initialize database
python init_db.py

# Test connection
python test_db_connection.py

# View database stats
python -c "from app import create_app; from app.models.database import db, Career; app = create_app(); print(db.session.query(Career).count(), 'careers')"

# Start Flask app
python run.py

# Backup SQLite (Windows)
copy career_chatbot.db career_chatbot_%date:~10,4%%date:~4,2%%date:~7,2%.db
```

---

## 🎯 Next Steps

1. **For Development**: Keep using SQLite (current setup)
2. **For Testing**: Run `python test_db_connection.py`
3. **For Production**: Set up MySQL following steps above
4. **For Backup**: Regularly copy `career_chatbot.db`

---

## ✅ Verification Checklist

- [ ] Database file exists at: `career_chatbot.db`
- [ ] 12 careers are loaded
- [ ] `python test_db_connection.py` passes
- [ ] `.env` has correct configuration
- [ ] `python run.py` starts without errors
- [ ] `http://localhost:5000` is accessible

---

## 📞 Support

For database issues:
1. Check `.env` configuration
2. Run `python test_db_connection.py`
3. Review logs in terminal
4. Check file permissions
5. Verify MySQL is running (if using MySQL)

---

**Database Status**: ✅ Ready for Use!

Your chatbot is fully configured and ready to handle user interactions with full database support.
