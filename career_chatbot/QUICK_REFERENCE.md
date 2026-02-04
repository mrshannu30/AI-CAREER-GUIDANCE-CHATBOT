# ⚡ Quick Reference Guide

## 🚀 Getting Started (30 seconds)

### Windows
```bash
cd "d:\Final Year Project\career_chatbot"
start.bat
# Then open http://localhost:5000
```

### Mac/Linux
```bash
cd "d:/Final Year Project/career_chatbot"
chmod +x start.sh
./start.sh
# Then open http://localhost:5000
```

---

## 📋 Common Commands

| Task | Command |
|------|---------|
| **Install dependencies** | `pip install -r requirements.txt` |
| **Start app** | `python run.py` |
| **Run tests** | `python test_models.py` |
| **Reset database** | `rm career_chatbot.db` |
| **Activate venv (Win)** | `venv\Scripts\activate` |
| **Activate venv (Mac/Linux)** | `source venv/bin/activate` |
| **Deactivate venv** | `deactivate` |

---

## 🎯 Key Features at a Glance

| Feature | Purpose |
|---------|---------|
| **Chat Interface** | Talk to the AI career advisor |
| **Profile Panel** | View and manage your info |
| **Recommendations** | See career suggestions |
| **Skill Extraction** | Auto-detect mentioned skills |
| **Intent Recognition** | Understand user questions |
| **Career Matching** | Find best-fit careers |

---

## 🔑 Important Directories

```
career_chatbot/
├── app/             ← Flask app and UI
├── ml_models/       ← AI/ML components
├── data/            ← Data storage
└── templates/       ← HTML pages
```

---

## 📱 Browser Access

**Home Page**: http://localhost:5000
**Chat**: http://localhost:5000/chat

---

## 💬 Sample User Inputs

```
"Hello"
"I'm studying computer science"
"I know Python and machine learning"
"What careers suit me?"
"I'm intermediate level"
"What's my next step?"
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port in use** | Kill process on port 5000 |
| **Module not found** | Run `pip install -r requirements.txt` |
| **DB error** | Delete `career_chatbot.db` and restart |
| **No response** | Check if Flask is running |
| **Slow bot** | First response may be slower |

---

## 📊 API Quick Reference

### Create User
```bash
curl -X POST http://localhost:5000/api/user/create \
  -H "Content-Type: application/json" \
  -d '{"email":"user@test.com","name":"John"}'
```

### Send Message
```bash
curl -X POST http://localhost:5000/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message":"I study CS","user_id":1}'
```

### Get Recommendations
```bash
curl http://localhost:5000/api/chat/get-recommendations/1
```

---

## 🎓 Understanding the Flow

```
User Types Message
        ↓
NLP Processor Extracts Intent & Info
        ↓
Career Recommender Calculates Match
        ↓
Response Generator Creates Reply
        ↓
Database Saves History
        ↓
Bot Responds to User
```

---

## ⚙️ Configuration

Main config file: `config.py`

Key settings:
- `DEBUG` - Enable debug mode
- `DATABASE_URL` - Database connection
- `SECRET_KEY` - Session encryption
- `FLASK_ENV` - development/production

---

## 📈 Performance Tips

✅ First response: ~1-2 seconds
✅ Subsequent: < 500ms
✅ Database optimized
✅ Responses cached in browser

---

## 🔒 Default Settings

- **Database**: SQLite (local file)
- **Port**: 5000
- **Debug**: Enabled (development only)
- **Sessions**: Browser storage
- **CORS**: Enabled

---

## 📚 Documentation Map

| File | Content |
|------|---------|
| **README.md** | Quick start |
| **DOCUMENTATION.md** | Complete guide |
| **PROJECT_SUMMARY.md** | Overview |
| **this file** | Quick reference |

---

## 🆘 If Something Breaks

1. **Check logs** in terminal
2. **Restart Flask** - Ctrl+C then `python run.py`
3. **Clear cache** - Hard refresh browser (Ctrl+Shift+R)
4. **Reset DB** - `rm career_chatbot.db`
5. **Reinstall deps** - `pip install -r requirements.txt`

---

## 💡 Pro Tips

- Type `Ctrl+L` to clear input field
- Use `Ctrl+C` to stop the server
- Browser console (F12) shows errors
- Each user session is independent
- Data persists in SQLite database

---

## 🎯 Test Phrases

Try these to see different responses:

```
"Hello"
"I'm studying data science"
"I have Python skills"
"What career suits me?"
"Help me plan my career"
"What's the next step?"
"Tell me about developer roles"
```

---

## 📞 Quick Fixes

### 504 Error (Timeout)
Solution: Restart Flask server

### Database locked
Solution: Close all instances and restart

### Static files not loading
Solution: Hard refresh (Ctrl+Shift+R)

### Chat not responding
Solution: Check browser console (F12)

---

## ⭐ Features Checklist

- ✅ NLP Intent Recognition
- ✅ Skill Extraction
- ✅ Career Recommendations
- ✅ Profile Management
- ✅ Conversation Tracking
- ✅ Responsive UI
- ✅ REST API
- ✅ SQLite Database
- ✅ ML Models
- ✅ Real-time Chat

---

## 🎓 Learning Path

**Beginner** → Explore careers
**Intermediate** → Share skills
**Advanced** → Get recommendations
**Expert** → Plan detailed steps

---

## 📦 All Dependencies

```
Flask==2.3.0
scikit-learn==1.2.2
numpy==1.24.3
pandas==2.0.3
nltk==3.8.1
spacy==3.5.0
And more...
```

See `requirements.txt` for complete list.

---

## 🔐 Security Notes

- ✅ Input validation enabled
- ✅ Session management included
- ✅ Error handling implemented
- ⚠️ Change SECRET_KEY in production
- ⚠️ Use HTTPS in production

---

## 📊 Architecture Overview

```
Frontend (HTML/CSS/JS)
    ↕
REST API (Flask)
    ↕
Business Logic (Python)
    ├── NLP Processor
    ├── Career Engine
    └── Response Generator
    ↕
Database (SQLite)
```

---

**Created**: January 2025
**Version**: 1.0
**Status**: Ready to Use 🚀
