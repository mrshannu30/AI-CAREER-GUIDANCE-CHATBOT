# MySQL Setup Guide for Career Chatbot

## Step 1: Download and Install MySQL

### Windows
1. Download MySQL Community Server from: https://dev.mysql.com/downloads/mysql/
2. Run the installer and follow the setup wizard
3. Remember your password for the root user
4. MySQL will default to port 3306
5. Complete the installation

### macOS
```bash
# Using Homebrew
brew install mysql
brew services start mysql
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
```

---

## Step 2: Create Database and User

### Option A: Using Command Line

Open Command Prompt/Terminal and run:
```bash
mysql -u root -p
```

Enter your root password, then run these SQL commands:

```sql
-- Create database
CREATE DATABASE career_chatbot;

-- Create user (change password to your preference)
CREATE USER 'chatbot_user'@'localhost' IDENTIFIED BY 'chatbot_password_123';

-- Grant privileges
GRANT ALL PRIVILEGES ON career_chatbot.* TO 'chatbot_user'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Exit
EXIT;
```

### Option B: Using MySQL Workbench (GUI)
1. Open MySQL Workbench
2. Right-click Schemas → Create Schema
3. Name: `career_chatbot`
4. Apply

---

## Step 3: Configure the Application

### Edit `.env` file in the project root:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here-change-in-production

# MySQL Configuration
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_USER=chatbot_user
DB_PASSWORD=chatbot_password_123
DB_NAME=career_chatbot
DATABASE_URL=mysql+pymysql://chatbot_user:chatbot_password_123@localhost:3306/career_chatbot

DEBUG=True
```

**Important**: Update `DB_PASSWORD` with the password you created in Step 2.

---

## Step 4: Initialize MySQL Database

Run the initialization script:

```bash
cd "d:\Final Year Project\career_chatbot"
python init_db.py
```

This will create all tables and seed the career data.

---

## Step 5: Verify Connection

To test the MySQL connection:

```bash
python test_db_connection.py
```

You should see:
```
✅ Successfully connected to MySQL database
📊 Career records: 12
```

---

## Verify MySQL is Running

### Windows
```bash
# Check if MySQL is running
tasklist | find "mysqld"

# Or start MySQL service
net start MySQL80
```

### macOS/Linux
```bash
# Check status
sudo systemctl status mysql

# Start MySQL
sudo systemctl start mysql
```

---

## Connection String Format

The connection format is:
```
mysql+pymysql://username:password@hostname:port/database_name
```

Example:
```
mysql+pymysql://chatbot_user:chatbot_password_123@localhost:3306/career_chatbot
```

---

## Troubleshooting

### "Connection refused"
- Check MySQL is running
- Verify hostname, port, username, password
- Check firewall settings

### "Access denied for user"
- Verify credentials in .env
- Recreate the user with correct password
- Run: `FLUSH PRIVILEGES;`

### "Database does not exist"
- Create the database
- Run: `CREATE DATABASE career_chatbot;`

### "Module 'pymysql' not found"
- Install: `pip install PyMySQL`

---

## Switch Back to SQLite

To switch back to SQLite, edit `.env`:

```env
DB_TYPE=sqlite
DATABASE_URL=sqlite:///career_chatbot.db
```

---

## Common MySQL Commands

```sql
-- Show all databases
SHOW DATABASES;

-- Use a database
USE career_chatbot;

-- Show all tables
SHOW TABLES;

-- Show table structure
DESCRIBE users;

-- Count records
SELECT COUNT(*) FROM careers;

-- Delete all data (careful!)
TRUNCATE TABLE users;

-- Drop database
DROP DATABASE career_chatbot;
```

---

## Security Notes

⚠️ **For Production**:
- Change default password
- Use strong passwords
- Restrict user privileges
- Use SSL connections
- Don't commit .env to version control

---

## Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [PyMySQL Documentation](https://pymysql.readthedocs.io/)
- [SQLAlchemy MySQL Guide](https://docs.sqlalchemy.org/en/14/dialects/mysql.html)

---

**Need Help?** Run: `python test_db_connection.py`
