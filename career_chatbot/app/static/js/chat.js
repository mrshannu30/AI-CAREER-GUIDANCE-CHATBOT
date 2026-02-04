// Global variables
let currentUserId = null;
let messageCount = 0;
let chatSessions = []; // Store all chat sessions
let currentChatId = null; // Current chat session ID

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is already logged in
    const savedUserId = localStorage.getItem('userId');
    if (savedUserId) {
        currentUserId = savedUserId;
        currentChatId = generateChatId();
        loadChatSessions();

        document.getElementById('setupModal').classList.add('hidden');
        loadUserProfile();
    } else {
        document.getElementById('setupModal').classList.remove('hidden');
    }
});

// Setup user
function setupUser(event) {
    event.preventDefault();

    const email = document.getElementById('userEmail').value;
    const name = document.getElementById('userName').value;

    if (!email || !name) {
        alert('Please enter both email and name');
        return;
    }

    fetch('/api/user/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            name: name
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.user_id) {
            currentUserId = data.user_id;
            localStorage.setItem('userId', currentUserId);
            document.getElementById('setupModal').classList.add('hidden');
            loadUserProfile();
            addBotMessage(`Welcome, ${name}! I'm your AI Career Guidance Assistant. Tell me about yourself - What are you studying or what skills do you have?`);
        } else if (data.error) {
            alert(`Error: ${data.error}`);
        }
    })
    .catch(error => {
        console.error('Setup Error:', error);
        alert(`Error setting up user: ${error.message}`);
    });
}

// Load user profile
function loadUserProfile() {
    if (!currentUserId) {
        console.warn('No user ID available for loading profile');
        return;
    }

    fetch(`/api/user/get/${currentUserId}`)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.email) {
            document.getElementById('profileName').textContent = data.name || 'Not set';
            document.getElementById('profileStudy').textContent = data.current_study || 'Not set';
            
            const skills = data.current_skills || [];
            document.getElementById('profileSkills').textContent = skills.length > 0 ? skills.join(', ') : 'No skills added yet';
            
            document.getElementById('profileStatus').textContent = data.study_status === 'completed' ? 'Studies Completed' : 'Studying';
        }
    })
    .catch(error => console.error('Error loading profile:', error));
}

// Send message
function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();

    if (!message) {
        console.warn('Empty message');
        return;
    }
    
    if (!currentUserId) {
        alert('Please complete the setup first');
        document.getElementById('setupModal').classList.remove('hidden');
        return;
    }

    // Add user message to chat
    addUserMessage(message);
    input.value = '';

    // Show typing indicator
    showTypingIndicator();

    // Send to backend
    fetch('/api/chat/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: message,
            user_id: currentUserId
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        removeTypingIndicator();
        
        if (data.error) {
            console.error('API Error:', data.error);
            addBotMessage(`Sorry, I encountered an error: ${data.error}`);
        } else if (data.bot_response) {
            addBotMessage(data.bot_response);
            
            // Show quick suggestion buttons based on intent
            if (data.suggestions && data.suggestions.length > 0) {
                showSuggestions(data.suggestions);
            }
            
            // Update profile if new information was extracted
            loadUserProfile();
            
            // Load recommendations if career exploration
            if (data.intent === 'career_exploration' || data.intent === 'career_guidance') {
                loadRecommendations();
            }
        } else {
            console.error('Unexpected response:', data);
            addBotMessage('Sorry, I received an unexpected response. Please try again.');
        }
    })
    .catch(error => {
        removeTypingIndicator();
        console.error('Chat Error:', error);
        addBotMessage(`Sorry, I encountered an error: ${error.message}. Please try again.`);
    });
}

// Add user message to chat
function addUserMessage(message) {
    const container = document.getElementById('messagesContainer');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user-message';
    
    const p = document.createElement('p');
    p.textContent = message;
    
    messageDiv.appendChild(p);
    container.appendChild(messageDiv);
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
}

// Add bot message to chat
function addBotMessage(message) {
    const container = document.getElementById('messagesContainer');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    
    const p = document.createElement('p');
    
    // Format markdown-like content
    p.innerHTML = formatMessage(message);
    
    messageDiv.appendChild(p);
    container.appendChild(messageDiv);
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
}

// Format message with basic markdown support
function formatMessage(message) {
    // Convert **text** to <strong>text</strong>
    message = message.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convert line breaks
    message = message.replace(/\n/g, '<br>');
    
    // Convert bullet points
    message = message.replace(/^- /gm, '• ');
    
    return message;
}

// Show typing indicator
function showTypingIndicator() {
    const container = document.getElementById('messagesContainer');
    const indicatorDiv = document.createElement('div');
    indicatorDiv.className = 'message bot-message';
    indicatorDiv.id = 'typingIndicator';
    
    const p = document.createElement('p');
    p.className = 'typing-indicator';
    p.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
    
    indicatorDiv.appendChild(p);
    container.appendChild(indicatorDiv);
    
    container.scrollTop = container.scrollHeight;
}

// Remove typing indicator
function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

// Load recommendations
function loadRecommendations() {
    if (!currentUserId) return;

    fetch(`/api/chat/get-recommendations/${currentUserId}`)
    .then(response => response.json())
    .then(data => {
        if (data.recommendations && data.recommendations.length > 0) {
            let recommendationsHtml = '';
            
            data.recommendations.forEach(rec => {
                recommendationsHtml += `
                    <div class="recommendation-item">
                        <h4>${rec.career}</h4>
                        <p><span class="match-score">${rec.score.toFixed(0)}% Match</span></p>
                        <p><strong>Description:</strong> ${rec.description}</p>
                        <p><strong>Salary:</strong> ${rec.salary_range}</p>
                        <p><strong>Growth:</strong> ${rec.growth_rate}</p>
                        ${rec.missing_skills.length > 0 ? `<p><strong>Skills to learn:</strong> ${rec.missing_skills.slice(0, 3).join(', ')}</p>` : ''}
                    </div>
                `;
            });
            
            document.getElementById('recommendationsContent').innerHTML = recommendationsHtml;
            document.getElementById('recommendationsPanel').classList.add('active');
        }
    })
    .catch(error => console.error('Error loading recommendations:', error));
}

// Toggle profile panel
function toggleProfilePanel() {
    const panel = document.getElementById('profilePanel');
    const recommendations = document.getElementById('recommendationsPanel');
    
    panel.classList.toggle('active');
    
    // Close recommendations if profile is opened
    if (panel.classList.contains('active')) {
        recommendations.classList.remove('active');
    }
}

// Toggle recommendations panel
function toggleRecommendationsPanel() {
    const panel = document.getElementById('recommendationsPanel');
    const profile = document.getElementById('profilePanel');
    
    panel.classList.toggle('active');
    
    // Close profile if recommendations is opened
    if (panel.classList.contains('active')) {
        profile.classList.remove('active');
    }
}

// Show suggestion buttons
function showSuggestions(suggestions) {
    const container = document.getElementById('messagesContainer');
    const suggestionsDiv = document.createElement('div');
    suggestionsDiv.className = 'suggestions-container';
    suggestionsDiv.id = 'suggestionButtons';
    
    let suggestionsHtml = '<div class="suggestions-label">📌 Quick Options:</div><div class="suggestions-buttons">';
    
    suggestions.forEach((suggestion, index) => {
        suggestionsHtml += `<button class="suggestion-btn" onclick="selectSuggestion('${suggestion.text}')">${suggestion.label}</button>`;
    });
    
    suggestionsHtml += '</div>';
    suggestionsDiv.innerHTML = suggestionsHtml;
    container.appendChild(suggestionsDiv);
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
}

// Handle suggestion selection
function selectSuggestion(text) {
    // Remove suggestion buttons
    const suggestionsDiv = document.getElementById('suggestionButtons');
    if (suggestionsDiv) {
        suggestionsDiv.remove();
    }
    
    // Send the suggestion text as a message
    document.getElementById('messageInput').value = text;
    sendMessage();
}

// Handle Enter key in input
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
}

// Logout function
function logout() {
    localStorage.removeItem('userId');
    currentUserId = null;
    location.reload();
}
// Generate unique chat ID
function generateChatId() {
    return `chat_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
}

// Save current chat to history
function saveChatSession() {
    const messages = document.querySelectorAll('.message');
    if (messages.length === 0) return;

    const session = {
        id: currentChatId,
        title: `Chat - ${new Date().toLocaleTimeString()}`,
        timestamp: new Date().toISOString(),
        messages: Array.from(messages).map(msg => ({
            type: msg.classList.contains('bot-message') ? 'bot' : 'user',
            text: msg.innerText
        }))
    };

    // Get existing sessions from localStorage
    const existing = JSON.parse(localStorage.getItem(`chatSessions_${currentUserId}`) || '[]');
    existing.unshift(session); // Add to beginning
    localStorage.setItem(`chatSessions_${currentUserId}`, JSON.stringify(existing.slice(0, 20))); // Keep last 20
}

// Load chat sessions from localStorage
function loadChatSessions() {
    const sessions = JSON.parse(localStorage.getItem(`chatSessions_${currentUserId}`) || '[]');
    chatSessions = sessions;
    displayChatHistory();
}

// Display chat history
function displayChatHistory() {
    const historyContent = document.getElementById('historyContent');
    
    if (chatSessions.length === 0) {
        historyContent.innerHTML = '<p style="color: #999; text-align: center; padding: 1rem;">No chat history yet</p>';
        return;
    }

    historyContent.innerHTML = chatSessions.map(session => `
        <div class="chat-session" onclick="loadChatSession('${session.id}')">
            <div class="chat-session-title">📌 ${session.title}</div>
            <div class="chat-session-time">${new Date(session.timestamp).toLocaleDateString()}</div>
        </div>
    `).join('');
}

// Load a chat session
function loadChatSession(sessionId) {
    const session = chatSessions.find(s => s.id === sessionId);
    if (!session) return;

    const container = document.getElementById('messagesContainer');
    container.innerHTML = '';

    session.messages.forEach(msg => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${msg.type === 'bot' ? 'bot-message' : 'user-message'}`;
        msgDiv.innerHTML = `<p>${msg.text}</p>`;
        container.appendChild(msgDiv);
    });

    // Close history panel
    toggleChatHistory();
}

// Toggle chat history panel
function toggleChatHistory() {
    const panel = document.getElementById('historyPanel');
    if (panel.classList.contains('hidden')) {
        loadChatSessions();
        panel.classList.remove('hidden');
    } else {
        panel.classList.add('hidden');
    }
}

// Start new chat
function startNewChat() {
    // Save current chat before starting new one
    saveChatSession();

    // Clear current messages
    const container = document.getElementById('messagesContainer');
    container.innerHTML = '';

    // Generate new chat ID
    currentChatId = generateChatId();

    // Add initial message
    addBotMessage('👋 Hello! I\'m your AI Career Guidance Assistant. Tell me about yourself to get started!');

    // Clear input
    document.getElementById('messageInput').value = '';
}