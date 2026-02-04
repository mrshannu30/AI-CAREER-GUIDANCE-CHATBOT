# System Architecture & Diagrams

## 1. High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE LAYER                         │
│ ┌───────────────────────────────────────────────────────────┐   │
│ │  Browser (HTML5/CSS3/JavaScript)                         │   │
│ │  ├─ Chat Interface                                        │   │
│ │  ├─ User Profile Panel                                   │   │
│ │  ├─ Recommendations Display                              │   │
│ │  └─ Setup Modal                                          │   │
│ └───────────────────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP/REST
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                    API LAYER (Flask)                             │
│ ┌───────────────────────────────────────────────────────────┐   │
│ │ Routes                                                    │   │
│ │ ├─ /api/user/* (User Management)                         │   │
│ │ └─ /api/chat/* (Chat Operations)                         │   │
│ └───────────────────────────────────────────────────────────┘   │
└──────────────┬───────────────────────────────────┬────────────────┘
               │                                   │
               ▼                                   ▼
     ┌─────────────────────┐       ┌──────────────────────────┐
     │  BUSINESS LOGIC     │       │   DATA LAYER             │
     │                     │       │                          │
     │ ┌─────────────────┐ │       │ ┌────────────────────┐   │
     │ │ NLP Processor   │ │       │ │ SQLAlchemy Models  │   │
     │ │ ├─ Intent Class │ │       │ │ ├─ User            │   │
     │ │ └─ Information  │ │       │ │ ├─ Career          │   │
     │ │   Extraction    │ │       │ │ ├─ Conversation    │   │
     │ └─────────────────┘ │       │ │ └─ Recommendation  │   │
     │                     │       │ └────────────────────┘   │
     │ ┌─────────────────┐ │       │                          │
     │ │ Career          │ │       │ ┌────────────────────┐   │
     │ │ Recommender     │ │       │ │ SQLite Database    │   │
     │ │ ├─ Skill Match  │ │       │ │                    │   │
     │ │ ├─ Education    │ │       │ │ career_chatbot.db  │   │
     │ │ │   Matching    │ │       │ └────────────────────┘   │
     │ │ └─ Scoring      │ │       │                          │
     │ └─────────────────┘ │       └──────────────────────────┘
     │                     │
     │ ┌─────────────────┐ │
     │ │ Response        │ │
     │ │ Generator       │ │
     │ │ ├─ Templates    │ │
     │ │ └─ Formatting   │ │
     │ └─────────────────┘ │
     └─────────────────────┘
```

## 2. Data Flow Diagram

```
                    START
                      │
                      ▼
            ┌─────────────────┐
            │  User Sends     │
            │  Message        │
            └────────┬────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Message Received at   │
        │  /api/chat/message     │
        └────────┬───────────────┘
                 │
                 ▼
      ┌──────────────────────────┐
      │  NLP Processor:          │
      │  1. Tokenize text        │
      │  2. Extract intent       │
      │  3. Classify intent      │
      │  4. Extract information: │
      │     - Field of study     │
      │     - Skills             │
      │     - Experience level   │
      └────────┬─────────────────┘
               │
               ▼
     ┌──────────────────────────┐
     │  Update User Profile     │
     │  in Database             │
     └────────┬─────────────────┘
              │
              ▼
   ┌──────────────────────────────┐
   │  Route Based on Intent:      │
   │  ├─ greetings →              │
   │  │  Generate greeting        │
   │  ├─ career_guidance →        │
   │  │  Get recommendations      │
   │  ├─ skill_assessment →       │
   │  │  Assess skills            │
   │  └─ ... other intents        │
   └────────┬──────────────────────┘
            │
            ▼
 ┌──────────────────────────────┐
 │ If career_guidance:          │
 │                              │
 │ Career Recommender:          │
 │ 1. Get user profile          │
 │ 2. Load career database      │
 │ 3. Calculate matches:        │
 │    - Skill match (40%)       │
 │    - Education (30%)         │
 │    - Experience (30%)        │
 │ 4. Generate recommendations │
 │ 5. Create next steps         │
 └────────┬─────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│ Response Generator:             │
│ 1. Format recommendations       │
│ 2. Create readable response     │
│ 3. Add actionable steps         │
└────────┬────────────────────────┘
         │
         ▼
 ┌──────────────────────────┐
 │ Save Conversation to DB  │
 │ - User message           │
 │ - Bot response           │
 │ - Intent detected        │
 │ - Timestamp              │
 └────────┬─────────────────┘
          │
          ▼
┌──────────────────────────┐
│ Return JSON Response:    │
│ - bot_response           │
│ - intent                 │
│ - confidence             │
└────────┬─────────────────┘
         │
         ▼
   ┌──────────────┐
   │ Send to UI   │
   │ Display      │
   │ Message      │
   └──────────────┘
```

## 3. Database Schema Diagram

```
┌─────────────────────────────────┐
│         USERS TABLE             │
├─────────────────────────────────┤
│ id (PK)                         │
│ email (UNIQUE)                  │
│ name                            │
│ current_study                   │
│ current_skills (JSON)           │
│ work_experience (JSON)          │
│ study_status                    │
│ preferences (JSON)              │
│ created_at                      │
│ updated_at                      │
└──────────────┬────────────────────┐
               │ 1:N               │
               │                   ▼
┌──────────────────────────────┐  ┌─────────────────────────────────┐
│ CONVERSATION_HISTORY TABLE   │  │ CAREER_RECOMMENDATIONS TABLE    │
├──────────────────────────────┤  ├─────────────────────────────────┤
│ id (PK)                      │  │ id (PK)                         │
│ user_id (FK)                 │  │ user_id (FK)                    │
│ user_message                 │  │ career_id (FK)                  │
│ bot_response                 │  │ match_score                     │
│ intent                       │  │ reasoning                       │
│ timestamp                    │  │ next_steps (JSON)               │
└──────────────────────────────┘  │ created_at                      │
                                  └──────────┬──────────────────────┘
                                             │ N:1
                                             │
                                  ┌──────────▼─────────────────────┐
                                  │    CAREERS TABLE                │
                                  ├─────────────────────────────────┤
                                  │ id (PK)                         │
                                  │ title (UNIQUE)                  │
                                  │ description                     │
                                  │ required_skills (JSON)          │
                                  │ required_education (JSON)       │
                                  │ average_salary                  │
                                  │ job_growth_rate                 │
                                  │ related_fields (JSON)           │
                                  │ created_at                      │
                                  └─────────────────────────────────┘
```

## 4. NLP Processing Pipeline

```
                INPUT TEXT
                    │
                    ▼
        ┌────────────────────────┐
        │  Text Preprocessing    │
        │ - Lowercase            │
        │ - Tokenization         │
        │ - Remove special chars  │
        └────────┬───────────────┘
                 │
                 ▼
    ┌────────────────────────────┐
    │  TF-IDF Vectorization      │
    │ (Convert text to numbers)  │
    └────────┬───────────────────┘
             │
             ▼
  ┌─────────────────────────────┐
  │  Random Forest Classifier   │
  │ - Input: Vector             │
  │ - Processing: 100 trees     │
  │ - Output: Intent + score    │
  └────────┬────────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  Information Extraction      │
│ - Keyword matching for skills│
│ - String matching for fields │
│ - Pattern matching for exp   │
└────────┬─────────────────────┘
         │
         ▼
    OUTPUT: Processed Data
    ├─ Intent
    ├─ Confidence
    ├─ Skills
    ├─ Field of study
    └─ Experience level
```

## 5. Career Matching Algorithm

```
USER PROFILE
├─ Skills: [python, ml, sql]
├─ Education: computer science
└─ Experience: intermediate

                    │
                    ▼

┌──────────────────────────────────────┐
│  For Each Career in Database:        │
└──────────────────────────────────────┘

        │
        ▼

┌─────────────────────────────────┐
│  SKILL MATCH (40% weight)       │
│                                 │
│  User Skills: {python, ml, sql} │
│  Career Req: {python, ml, java} │
│                                 │
│  Intersection: {python, ml}     │
│  Match = 2/3 = 66%              │
│  Score: 66 * 0.4 = 26.4         │
└─────────────────────────────────┘

        │
        ▼

┌─────────────────────────────────┐
│  EDUCATION MATCH (30% weight)   │
│                                 │
│  User: computer science         │
│  Career needs: {cs, eng}        │
│                                 │
│  Found: YES (100%)              │
│  Score: 100 * 0.3 = 30          │
└─────────────────────────────────┘

        │
        ▼

┌─────────────────────────────────┐
│  EXPERIENCE MATCH (30% weight)  │
│                                 │
│  User level: intermediate (2)   │
│  Career req: intermediate (2)   │
│                                 │
│  Match: 100%                    │
│  Score: 100 * 0.3 = 30          │
└─────────────────────────────────┘

        │
        ▼

┌─────────────────────────────────┐
│  TOTAL MATCH SCORE              │
│                                 │
│  26.4 + 30 + 30 = 86.4%         │
└─────────────────────────────────┘

        │
        ▼

[Sort by score and return top 5]
```

## 6. Intent Classification Tree

```
                    USER TEXT
                         │
            Is it a greeting?
            ├─ YES → GREETINGS
            └─ NO
                │
            Does it mention career path?
            ├─ YES → CAREER_GUIDANCE
            └─ NO
                │
            Does it ask about skills?
            ├─ YES → SKILL_ASSESSMENT
            └─ NO
                │
            Does it explore options?
            ├─ YES → CAREER_EXPLORATION
            └─ NO
                │
            Does it ask about education?
            ├─ YES → STUDY_PATH
            └─ NO
                │
            Does it ask about jobs?
            ├─ YES → JOB_SEARCH
            └─ NO
                │
            Does it focus on learning?
            ├─ YES → SKILL_DEVELOPMENT
            └─ NO
                │
            Does it ask about money?
            ├─ YES → SALARY_INFO
            └─ NO
                │
            Does it focus on education?
            ├─ YES → EDUCATION_PATH
            └─ NO
                │
            GENERAL_INFO (default)
```

## 7. User Journey Timeline

```
Timeline: User Interaction with Chatbot

T=0s   ┌─────────────────────┐
       │ User opens website  │
       │ http://localhost:5000
       └────────┬────────────┘
               │
T=1s   ┌────────▼────────────┐
       │ Home page loads     │
       │ Shows features      │
       └────────┬────────────┘
               │
T=3s   ┌────────▼────────────┐
       │ User clicks chat    │
       └────────┬────────────┘
               │
T=4s   ┌────────▼─────────────────┐
       │ Setup modal opens        │
       │ Email & name input       │
       └────────┬─────────────────┘
               │
T=6s   ┌────────▼──────────────────┐
       │ User submits form         │
       │ API creates user          │
       │ Session started           │
       └────────┬──────────────────┘
               │
T=7s   ┌────────▼──────────────────┐
       │ Chat interface loads      │
       │ Bot greets user           │
       │ Input field active        │
       └────────┬──────────────────┘
               │
T=10s  ┌────────▼──────────────────┐
       │ User types first message  │
       │ "I'm studying CS"         │
       └────────┬──────────────────┘
               │
T=11s  ┌────────▼──────────────────┐
       │ Message sent to API       │
       │ NLP processing begins     │
       └────────┬──────────────────┘
               │
T=12s  ┌────────▼──────────────────┐
       │ Intent detected           │
       │ Info extracted            │
       │ Response generated        │
       └────────┬──────────────────┘
               │
T=13s  ┌────────▼──────────────────┐
       │ Response displayed        │
       │ Profile updated           │
       │ Ready for next input      │
       └──────────────────────────┘
```

## 8. Error Handling Flow

```
           API REQUEST
                │
                ▼
        ┌──────────────┐
        │ Validate     │
        │ Input        │
        └────┬─────┬──┘
             │     │
          PASS    FAIL
             │     │
             │     ▼
             │  ┌──────────────────┐
             │  │ 400: Bad Request │
             │  │ Return error msg │
             │  └──────────────────┘
             │
             ▼
        ┌──────────────┐
        │ Check User   │
        │ Exists       │
        └────┬─────┬──┘
             │     │
          FOUND   NOT FOUND
             │     │
             │     ▼
             │  ┌──────────────────┐
             │  │ 404: Not Found   │
             │  │ Return error msg │
             │  └──────────────────┘
             │
             ▼
        ┌──────────────┐
        │ Process      │
        │ Request      │
        └────┬─────┬──┘
             │     │
          SUCCESS  ERROR
             │     │
             │     ▼
             │  ┌──────────────────┐
             │  │ 500: Server Error│
             │  │ Log error        │
             │  │ Return error msg │
             │  └──────────────────┘
             │
             ▼
        ┌──────────────┐
        │ Return 200   │
        │ Success      │
        │ Response     │
        └──────────────┘
```

---

**Diagrams Version**: 1.0
**Last Updated**: January 28, 2025
