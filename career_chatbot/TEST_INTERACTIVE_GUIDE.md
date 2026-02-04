# 🎯 Quick Test Guide - Interactive Suggestions

## ⚡ Quick Setup (2 minutes):

```bash
cd "d:\Final Year Project\career_chatbot"
python run.py
```

Then open: `http://localhost:5000`

---

## 📝 Test Scenarios:

### Scenario 1: Complete Career Guidance Journey
```
1. Open chatbot at http://localhost:5000
2. Click "Start Chatting" button (setup form)
3. Type: "im pursuing bca"
   → Bot shows 3 suggestion buttons
   
4. Click: "💻 My skills: Python, Java..."
   → Bot shows skill-based recommendations
   
5. Click: "📖 Tell me more about Web Developer"
   → Bot shows detailed career info & roadmap
   
6. Observe: Personalized suggestions guide you through the entire journey
```

### Scenario 2: Test Different Career Paths
```
1. Tell bot: "im pursuing engineering"
2. Click suggestion about interests
3. Choose: "Data Science & AI"
4. View career recommendations for Data Scientist
```

### Scenario 3: Test Job Search Path
```
1. After setup, click: "💼 Start job search"
2. Bot asks about skills and experience
3. Shows job-matching careers
```

---

## 🔍 What to Look For:

✅ **Buttons appear below bot response**
✅ **Buttons have emoji icons**
✅ **Clicking button sends message automatically**
✅ **Different questions get different suggestions**
✅ **Suggestions guide the conversation flow**
✅ **Recommendations show salary & growth rate**

---

## 🎨 Visual Checklist:

- [ ] Purple gradient buttons visible
- [ ] Buttons have hover effect (darker on mouse over)
- [ ] Smooth animation when buttons appear
- [ ] Text is readable and properly formatted
- [ ] Mobile view works (if testing on mobile)
- [ ] Suggestions update based on bot response

---

## 🧪 Frontend Testing (in browser):

Open DevTools (`F12`) and check **Console** for:
- ✅ No red errors
- ✅ Fetch requests successful (200 status)
- ✅ Suggestions data received
- ✅ Button clicks logged

---

## 📊 Expected API Response:

```json
{
  "user_message": "im pursuing bca",
  "bot_response": "Great! I see you're pursuing **BCA**!...",
  "intent": "career_guidance",
  "confidence": 0.79,
  "suggestions": [
    {
      "label": "💻 My skills: Python, Java, Web Development",
      "text": "I have skills in Python, Java, and Web Development"
    },
    {
      "label": "🎯 I'm interested in: Data Science & AI",
      "text": "I'm most interested in Data Science and AI careers"
    },
    {
      "label": "📝 Tell me what I should learn",
      "text": "What skills should I develop for a good career"
    }
  ]
}
```

---

## 🐛 Troubleshooting:

### Buttons not appearing?
- [ ] Clear browser cache: `Ctrl+F5`
- [ ] Check Console for JavaScript errors
- [ ] Verify response includes `suggestions` field

### Buttons not working?
- [ ] Check network tab in DevTools
- [ ] Verify POST request is successful
- [ ] Check that `selectSuggestion()` function is defined

### Bot not responding to button clicks?
- [ ] Ensure `user_id` is set in localStorage
- [ ] Check that message was sent (in Conversation History)
- [ ] Verify Flask is running (no errors in terminal)

---

## 📱 Mobile Testing:

Buttons should:
- ✅ Stack vertically
- ✅ Be touchable (large enough)
- ✅ Responsive text
- ✅ No overflow issues

---

## 🎯 Success Indicators:

1. **User clicks button** → Message is sent automatically
2. **Bot responds** → New suggestions appear
3. **Conversation flows** → User is guided through career discovery
4. **Recommendations** → Based on user's skills & interests
5. **Roadmap** → Personalized next steps shown

---

## 💾 Database Check:

Verify data is saved:
```bash
python test_db_connection.py
```

Should show:
- ✅ Conversation records increase
- ✅ Career recommendations saved
- ✅ User profile updated with skills

---

**Everything is ready! Just refresh your browser and enjoy the interactive experience!** 🚀
