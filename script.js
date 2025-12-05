// Token database
const validTokens = {
    // Format: "TOKEN": { "file": "DOWNLOAD_URL", "expires": "YYYY-MM-DD", "desc": "Description" }
    // Example tokens - ADD YOUR REAL TOKERS HERE
    "ABC1DEF2GHI3JKL4": {
        file: "https://github.com/Nandocn555/0nyx.dll/raw/main/Cyb3rtech_Tool.zip",
        expires: "2024-12-31",
        desc: "Test token - 1 year"
    },
    "TEST1234TEST5678": {
        file: "https://github.com/Nandocn555/0nyx.dll/raw/main/Cyb3rtech_Tool.zip",
        expires: "2023-12-25",
        desc: "Christmas token - 1 week"
    }
};

// Configuration
const CONFIG = {
    minTokenLength: 16,
    maxTokenLength: 16,
    tokenFormat: /^[A-Z0-9]{16}$/,
    downloadDelay: 2000, // 2 seconds
    adminPassword: "mr3lit1221",
    toolName: "Cyb3rtech_Tool.zip",
    mainFile: "start.bat",
    // GitHub repository information
    githubRepo: "Nandocn555/0nyx.dll",
    githubRawUrl: "https://github.com/Nandocn555/0nyx.dll/raw/main/"
};

// DOM Elements
let tokenInput, messageBox, messageText, messageIcon;

// Initialization
document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    tokenInput = document.getElementById('tokenInput');
    messageBox = document.getElementById('messageBox');
    messageText = document.getElementById('messageText');
    messageIcon = document.getElementById('messageIcon');
    
    // Set current date
    updateDates();
    
    // Auto-focus on input
    tokenInput.focus();
    
    // Allow Enter key to validate
    tokenInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            validateToken();
        }
    });
    
    // Format token input
    tokenInput.addEventListener('input', function() {
        formatTokenInput();
    });
});

// Format token input
function formatTokenInput() {
    let token = tokenInput.value.toUpperCase().replace(/[^A-Z0-9]/g, '');
    tokenInput.value = token;
    
    // Limit length
    if (token.length > CONFIG.maxTokenLength) {
        tokenInput.value = token.substring(0, CONFIG.maxTokenLength);
    }
}

// Clear input
function clearToken() {
    tokenInput.value = '';
    tokenInput.focus();
    closeMessage();
}

// Close message
function closeMessage() {
    messageBox.classList.add('hidden');
}

// Show message
function showMessage(type, text) {
    messageBox.className = 'message-box ' + type;
    messageText.textContent = text;
    messageIcon.className = getMessageIcon(type);
    messageBox.classList.remove('hidden');
    
    // Auto-close success messages after 5 seconds
    if (type === 'success') {
        setTimeout(closeMessage, 5000);
    }
}

// Get icon based on message type
function getMessageIcon(type) {
    switch(type) {
        case 'success': return 'fas fa-check-circle';
        case 'error': return 'fas fa-exclamation-circle';
        default: return 'fas fa-info-circle';
    }
}

// Validate token
function validateToken() {
    const token = tokenInput.value.trim().toUpperCase();
    
    // Basic validations
    if (!token) {
        showMessage('error', '❌ Please enter a token');
        tokenInput.focus();
        return;
    }
    
    if (token.length !== CONFIG.minTokenLength) {
        showMessage('error', `❌ Token must be ${CONFIG.minTokenLength} characters`);
        return;
    }
    
    if (!CONFIG.tokenFormat.test(token)) {
        showMessage('error', '❌ Invalid token format (letters and numbers only)');
        return;
    }
    
    // Check if token exists
    if (!validTokens[token]) {
        showMessage('error', '❌ Token not valid or not found');
        return;
    }
    
    const tokenData = validTokens[token];
    
    // Check expiration date
    const today = new Date().toISOString().split('T')[0];
    if (today > tokenData.expires) {
        showMessage('error', `❌ Token expired on ${formatDate(tokenData.expires)}`);
        return;
    }
    
    // Token valid - proceed with download
    showMessage('success', `✅ Token valid! Downloading ${CONFIG.toolName}...`);
    
    // Disable button temporarily
    const validateBtn = document.querySelector('.validate-btn');
    const originalText = validateBtn.innerHTML;
    validateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> DOWNLOADING...';
    validateBtn.disabled = true;
    
    // Wait and download
    setTimeout(() => {
        downloadFile(tokenData.file, CONFIG.toolName);
        
        // Restore button
        setTimeout(() => {
            validateBtn.innerHTML = originalText;
            validateBtn.disabled = false;
            showMessage('success', `✅ Download complete! Extract the ZIP and run ${CONFIG.mainFile}`);
            
            // Show installation instructions
            showInstallInstructions();
        }, 1000);
        
        // Log usage
        logTokenUsage(token);
        
    }, CONFIG.downloadDelay);
}

// Download file
function downloadFile(url, filename) {
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.target = '_blank';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Show installation instructions
function showInstallInstructions() {
    setTimeout(() => {
        const instructions = `
        <div style="margin-top: 20px; padding: 15px; background: rgba(0,212,255,0.1); border-radius: 10px;">
            <h4 style="color: #00d4ff; margin-bottom: 10px;"><i class="fas fa-info-circle"></i> Installation Instructions:</h4>
            <ol style="padding-left: 20px; color: #d0e7ff;">
                <li>Extract <strong>${CONFIG.toolName}</strong></li>
                <li>Open the extracted folder</li>
                <li>Run <code>${CONFIG.mainFile}</code> as Administrator</li>
                <li>Follow the on-screen instructions</li>
                <li>If Python is not installed, install it from python.org</li>
            </ol>
        </div>
        `;
        
        const existingInstructions = document.getElementById('dynamicInstructions');
        if (!existingInstructions) {
            const div = document.createElement('div');
            div.id = 'dynamicInstructions';
            div.innerHTML = instructions;
            document.querySelector('.token-section').appendChild(div);
        }
    }, 3000);
}

// Log token usage
function logTokenUsage(token) {
    const logs = JSON.parse(localStorage.getItem('tokenLogs') || '[]');
    logs.push({
        token: token.substring(0, 8) + '...', // Only first 8 chars for security
        date: new Date().toISOString(),
        userAgent: navigator.userAgent
    });
    localStorage.setItem('tokenLogs', JSON.stringify(logs.slice(-50))); // Keep last 50
}

// Update dates on page
function updateDates() {
    const now = new Date();
    const options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    
    const dateStr = now.toLocaleDateString('en-US', options);
    document.getElementById('currentDate').textContent = dateStr;
    document.getElementById('footerDate').textContent = now.toLocaleDateString('en-US');
}

// Format date
function formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US');
}

// Check admin access (for admin area)
function checkAdminAccess() {
    const password = prompt('Administrator password:');
    if (password === CONFIG.adminPassword) {
        return true;
    } else {
        alert('Incorrect password');
        return false;
    }
}

// Generate random token (for admin area)
function generateToken(days = 7) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let token = '';
    
    for (let i = 0; i < 16; i++) {
        token += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    
    // Calculate expiration date
    const expireDate = new Date();
    expireDate.setDate(expireDate.getDate() + days);
    const expireStr = expireDate.toISOString().split('T')[0];
    
    return {
        token: token,
        expires: expireStr,
        days: days
    };
}

// Add token to database (for admin use)
function addTokenToDatabase(token, expires, desc) {
    validTokens[token] = {
        file: `${CONFIG.githubRawUrl}Cyb3rtech_Tool.zip`,
        expires: expires,
        desc: desc
    };
    console.log(`Token added: ${token} (expires: ${expires})`);
    return token;
}
