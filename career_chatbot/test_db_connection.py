"""
Database Connection Test Script
Tests MySQL or SQLite connection
"""
import os
import sys
from dotenv import load_dotenv

# Fix Windows encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load environment variables
load_dotenv()

def test_connection():
    """Test database connection"""
    
    db_type = os.environ.get('DB_TYPE', 'sqlite')
    
    print("="*60)
    print("Database Connection Test")
    print("="*60)
    print(f"\n📊 Database Type: {db_type.upper()}")
    
    try:
        if db_type == 'mysql':
            print("\n🔗 Testing MySQL Connection...")
            print("-" * 60)
            
            import pymysql
            
            # Get connection parameters
            host = os.environ.get('DB_HOST', 'localhost')
            port = int(os.environ.get('DB_PORT', 3306))
            user = os.environ.get('DB_USER', 'root')
            password = os.environ.get('DB_PASSWORD', '')
            database = os.environ.get('DB_NAME', 'career_chatbot')
            
            print(f"Host: {host}:{port}")
            print(f"User: {user}")
            print(f"Database: {database}")
            
            # Try to connect
            connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                charset='utf8mb4'
            )
            
            print("\n✅ Successfully connected to MySQL database!")
            
            # Count records
            cursor = connection.cursor()
            
            # Check tables
            cursor.execute("""
                SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_SCHEMA = %s
            """, (database,))
            
            tables = cursor.fetchall()
            print(f"\n📋 Tables in database:")
            for table in tables:
                print(f"   ✅ {table[0]}")
            
            # Count careers
            cursor.execute("SELECT COUNT(*) FROM careers;")
            career_count = cursor.fetchone()[0]
            print(f"\n📚 Career records: {career_count}")
            
            # Count users
            cursor.execute("SELECT COUNT(*) FROM users;")
            user_count = cursor.fetchone()[0]
            print(f"👥 User records: {user_count}")
            
            # Count conversations
            cursor.execute("SELECT COUNT(*) FROM conversation_history;")
            convo_count = cursor.fetchone()[0]
            print(f"💬 Conversation records: {convo_count}")
            
            cursor.close()
            connection.close()
            
        else:
            print("\n🔗 Testing SQLite Connection...")
            print("-" * 60)
            
            from app.models.database import db
            from app import create_app
            
            app = create_app('development')
            
            with app.app_context():
                db_path = 'career_chatbot.db'
                if os.path.exists(db_path):
                    print(f"Database File: {os.path.abspath(db_path)}")
                    print(f"File Size: {os.path.getsize(db_path) / 1024:.2f} KB")
                    
                    # Import models to check tables
                    from app.models.database import Career, User, ConversationHistory
                    
                    # Count records
                    career_count = db.session.query(Career).count()
                    user_count = db.session.query(User).count()
                    convo_count = db.session.query(ConversationHistory).count()
                    
                    print("\n✅ Successfully connected to SQLite database!")
                    print(f"\n📚 Career records: {career_count}")
                    print(f"👥 User records: {user_count}")
                    print(f"💬 Conversation records: {convo_count}")
                else:
                    print(f"❌ Database file not found: {db_path}")
                    print("Run: python init_db.py")
                    return False
        
        print("\n" + "="*60)
        print("✅ CONNECTION TEST PASSED!")
        print("="*60)
        print("\nYour application is ready to use! 🚀")
        return True
        
    except Exception as e:
        print(f"\n❌ Connection failed!")
        print(f"Error: {str(e)}")
        print("\n" + "="*60)
        print("Troubleshooting:")
        print("-" * 60)
        
        if db_type == 'mysql':
            print("1. Check MySQL is running")
            print("2. Verify credentials in .env file")
            print("3. Ensure database exists: career_chatbot")
            print("4. Run: python init_db.py")
            print("5. See MYSQL_SETUP.md for detailed instructions")
        else:
            print("1. Run: python init_db.py")
            print("2. Check if career_chatbot.db exists")
            print("3. Verify requirements are installed: pip install -r requirements.txt")
        
        print("="*60)
        return False


if __name__ == '__main__':
    success = test_connection()
    sys.exit(0 if success else 1)
