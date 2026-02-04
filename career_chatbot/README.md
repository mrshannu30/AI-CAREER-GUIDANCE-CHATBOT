# 🎯 AI Career Guidance Chatbot

An intelligent chatbot powered by machine learning and natural language processing to help students and professionals plan their career paths.

## Features

- **Intelligent Conversation**: Natural language processing to understand user queries
- **Skill Assessment**: Analyzes user skills and experience level
- **Career Recommendations**: ML-based recommendations tailored to user profile
- **Study Path Planning**: Personalized educational roadmaps
- **Progress Tracking**: Stores conversation history and user profile
- **Real-time Guidance**: Contextual responses based on user input

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy with SQLite
- **Machine Learning**: scikit-learn for ML models
- **NLP**: NLTK and spaCy for natural language processing
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: RESTful Flask API

## Project Structure

```
career_chatbot/
├── app/
│   ├── models/
│   │   └── database.py          # Database models (User, Career, etc.)
│   ├── routes/
│   │   ├── chat.py              # Chat API endpoints
│   │   └── user.py              # User management endpoints
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css        # Main styles
│   │   │   └── chat.css         # Chat page styles
│   │   └── js/
│   │       └── chat.js          # Frontend logic
│   ├── templates/
│   │   ├── index.html           # Home page
│   │   ├── chat.html            # Chat interface
│   │   ├── 404.html             # Error pages
│   │   └── 500.html
│   ├── utils/
│   │   └── response_generator.py # Response templates
│   └── __init__.py              # Flask app initialization
├── ml_models/
│   ├── nlp_processor.py         # NLP and intent classification
│   └── career_recommender.py    # Career recommendation engine
├── data/                        # Data storage
├── config.py                    # Configuration
├── run.py                       # Application entry point
├── requirements.txt             # Python dependencies
└── README.md
```

## Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Clone/Setup Project
```bash
cd d:\Final Year Project\career_chatbot
```

### 3. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Download NLP Models (Optional but recommended)
```bash
python -m nltk.downloader punkt averaged_perceptron_tagger wordnet stopwords
python -m spacy download en_core_web_sm
```

### 6. Run the Application
```bash
python run.py
```

The application will be available at: **http://localhost:5000**

## Usage

### 1. Home Page
- Visit the home page to learn about the chatbot
- Click "Start Chatting Now" to begin

### 2. Chat Interface
- Enter your email and name in the setup modal
- Start chatting with the AI assistant
- Tell the bot about your:
  - Current field of study
  - Skills and experience
  - Career interests

### 3. Get Recommendations
- The bot will analyze your profile
- Receive personalized career recommendations
- Get step-by-step guidance on:
  - Skills to develop
  - Educational paths
  - Job search strategies
  - Salary expectations

### 4. Track Progress
- View your profile in the right panel
- Check conversation history
- Get updated recommendations as you learn more

## API Endpoints

### User Management
- `POST /api/user/create` - Create a new user
- `GET /api/user/get/<user_id>` - Get user information
- `PUT /api/user/update/<user_id>` - Update user profile
- `GET /api/user/profile/<user_id>` - Get complete user profile

### Chat
- `POST /api/chat/message` - Send a message and get response
- `GET /api/chat/get-recommendations/<user_id>` - Get career recommendations
- `GET /api/chat/get-conversation-history/<user_id>` - Get chat history

## Key Components

### 1. NLP Processor (`ml_models/nlp_processor.py`)
- **IntentClassifier**: Classifies user intent (career guidance, skill assessment, etc.)
- **NLPProcessor**: Extracts information like field of study, skills, and experience level
- Uses scikit-learn's TF-IDF and Random Forest for classification

### 2. Career Recommender (`ml_models/career_recommender.py`)
- **CareerRecommendationEngine**: 
  - Calculates skill match scores
  - Evaluates education compatibility
  - Assesses experience level alignment
  - Generates personalized next steps
  - Provides 12+ career paths with detailed info

### 3. Response Generator (`app/utils/response_generator.py`)
- Generates contextual responses based on intent
- Creates formatted career recommendations
- Builds actionable next steps
- Provides study plans

### 4. Database Models (`app/models/database.py`)
- **User**: Stores user profile and preferences
- **ConversationHistory**: Tracks all conversations
- **Career**: Career information database
- **CareerRecommendation**: Stores recommendations with match scores

## ML Models Used

### Intent Classification
- **Algorithm**: Random Forest Classifier
- **Features**: TF-IDF vectorized text
- **Classes**: 10 intent categories
  - greetings
  - career_guidance
  - skill_assessment
  - career_exploration
  - study_path
  - job_search
  - skill_development
  - salary_info
  - education_path
  - general_info

### Career Recommendation
- **Matching Algorithm**: Cosine similarity with weighted scoring
- **Factors Considered**:
  - Skill match (40% weight)
  - Education compatibility (30% weight)
  - Experience level (30% weight)

## Career Database

The system includes 12 pre-configured careers:
1. Software Engineer
2. Data Scientist
3. AI/ML Engineer
4. Web Developer
5. Mobile App Developer
6. Cloud Architect
7. DevOps Engineer
8. Business Analyst
9. UX/UI Designer
10. Product Manager
11. Database Administrator
12. Security Engineer

Each career includes:
- Required skills
- Education requirements
- Salary range
- Job growth rate
- Career description

## Configuration

Edit `.env` for environment variables:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///career_chatbot.db
DEBUG=True
```

## Database

The application uses SQLite by default. The database file `career_chatbot.db` is created automatically in the project root.

To reset the database:
```bash
rm career_chatbot.db
python run.py
```

## Future Enhancements

1. **Advanced ML Models**
   - Deep learning models for better NLP
   - Personalized ranking algorithms
   - Predictive career path analysis

2. **Additional Features**
   - Job marketplace integration
   - Resume builder
   - Interview preparation
   - Salary negotiation guidance

3. **Scalability**
   - PostgreSQL for production
   - Caching with Redis
   - API rate limiting
   - Multi-language support

4. **Analytics**
   - User engagement metrics
   - Career path success rates
   - Recommendation accuracy tracking

## Troubleshooting

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

### Database Issues
```bash
# Reset database
rm career_chatbot.db
python run.py
```

### Import Errors
```bash
# Reinstall requirements
pip install --force-reinstall -r requirements.txt
```

## Performance Tips

1. **Caching**: Responses are cached in the browser
2. **Database**: Indexes on frequently queried columns
3. **ML Models**: Pre-trained models are loaded once at startup
4. **Frontend**: Lazy loading of recommendations

## Security Notes

- Change `SECRET_KEY` in production
- Use HTTPS for deployed applications
- Implement user authentication
- Validate all user inputs
- Use environment variables for sensitive data

## Contributors

This project was developed as a Final Year Project for AI career guidance.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please refer to the documentation or create an issue in the project repository.

---

**Happy Career Planning! 🚀**
