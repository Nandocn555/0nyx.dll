// Base de datos de tokens (en un caso real, esto estaría en un servidor)
const validTokens = {
    // Formato: "TOKEN": { "file": "URL_DESCARGAS", "expires": "YYYY-MM-DD", "desc": "Descripción" }
    "ABC1DEF2GHI3JKL4": {
        file: "https://drive.google.com/uc?export=download&id=TU_ID_DE_DRIVE_AQUI",
        expires: "2024-12-31",
        desc: "Token de prueba - 1 año"
    },
    "TEST1234TEST5678": {
        file: "https://drive.google.com/uc?export=download&id=OTRO_ID_AQUI",
        expires: "2023-12-25",
        desc: "Token Navidad - 1 semana"
    }
};

// Configuración
const CONFIG = {
    minTokenLength: 16,
    maxTokenLength: 16,
    tokenFormat: /^[A-Z0-9]{16}$/,
    downloadDelay: 2000, // 2 segundos
    adminPassword: "mr3lit1221"
};

// Elementos del DOM
let tokenInput, messageBox, messageText, messageIcon;

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    // Obtener elementos
    tokenInput = document.getElementById('tokenInput');
    messageBox = document.getElementById('messageBox');
    messageText = document.getElementById('messageText');
    messageIcon = document.getElementById('messageIcon');
    
    // Configurar fecha actual
    updateDates();
    
    // Configurar auto-focus en el input
    tokenInput.focus();
    
    // Permitir Enter para validar
    tokenInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            validateToken();
        }
    });
    
    // Mostrar caracteres del token
    tokenInput.addEventListener('input', function() {
        formatTokenInput();
    });
});

// Formatear input del token
function formatTokenInput() {
    let token = tokenInput.value.toUpperCase().replace(/[^A-Z0-9]/g, '');
    tokenInput.value = token;
    
    // Limitar longitud
    if (token.length > CONFIG.maxTokenLength) {
        tokenInput.value = token.substring(0, CONFIG.maxTokenLength);
    }
}

// Limpiar input
function clearToken() {
    tokenInput.value = '';
    tokenInput.focus();
    closeMessage();
}

// Cerrar mensaje
function closeMessage() {
    messageBox.classList.add('hidden');
}

// Mostrar mensaje
function showMessage(type, text) {
    messageBox.className = 'message-box ' + type;
    messageText.textContent = text;
    messageIcon.className = getMessageIcon(type);
    messageBox.classList.remove('hidden');
    
    // Auto cerrar mensajes de éxito después de 5 segundos
    if (type === 'success') {
        setTimeout(closeMessage, 5000);
    }
}

// Obtener icono según tipo
function getMessageIcon(type) {
    switch(type) {
        case 'success': return 'fas fa-check-circle';
        case 'error': return 'fas fa-exclamation-circle';
        default: return 'fas fa-info-circle';
    }
}

// Validar token
function validateToken() {
    const token = tokenInput.value.trim().toUpperCase();
    
    // Validaciones básicas
    if (!token) {
        showMessage('error', '❌ Por favor, introduce un token');
        tokenInput.focus();
        return;
    }
    
    if (token.length !== CONFIG.minTokenLength) {
        showMessage('error', `❌ El token debe tener ${CONFIG.minTokenLength} caracteres`);
        return;
    }
    
    if (!CONFIG.tokenFormat.test(token)) {
        showMessage('error', '❌ Formato de token inválido (solo letras y números)');
        return;
    }
    
    // Verificar si el token existe
    if (!validTokens[token]) {
        showMessage('error', '❌ Token no válido o no encontrado');
        return;
    }
    
    const tokenData = validTokens[token];
    
    // Verificar fecha de expiración
    const today = new Date().toISOString().split('T')[0];
    if (today > tokenData.expires) {
        showMessage('error', `❌ Token expirado el ${formatDate(tokenData.expires)}`);
        return;
    }
    
    // Token válido - proceder con descarga
    showMessage('success', `✅ Token válido! Descargando herramienta...`);
    
    // Deshabilitar botón temporalmente
    const validateBtn = document.querySelector('.validate-btn');
    const originalText = validateBtn.innerHTML;
    validateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> DESCARGANDO...';
    validateBtn.disabled = true;
    
    // Esperar y descargar
    setTimeout(() => {
        downloadFile(tokenData.file);
        
        // Restaurar botón
        setTimeout(() => {
            validateBtn.innerHTML = originalText;
            validateBtn.disabled = false;
            showMessage('success', '✅ Descarga completada. Extrae el ZIP y ejecuta la herramienta.');
        }, 1000);
        
        // Registrar uso (en un caso real, enviarías esto a un servidor)
        logTokenUsage(token);
        
    }, CONFIG.downloadDelay);
}

// Descargar archivo
function downloadFile(url) {
    const link = document.createElement('a');
    link.href = url;
    link.download = 'Cyb3rtech_Tool.zip';
    link.target = '_blank';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Registrar uso del token
function logTokenUsage(token) {
    const logs = JSON.parse(localStorage.getItem('tokenLogs') || '[]');
    logs.push({
        token: token.substring(0, 8) + '...', // Solo primeros 8 chars por seguridad
        date: new Date().toISOString(),
        ip: 'WebApp'
    });
    localStorage.setItem('tokenLogs', JSON.stringify(logs.slice(-50))); // Guardar últimos 50
}

// Actualizar fechas en la página
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
    
    const dateStr = now.toLocaleDateString('es-ES', options);
    document.getElementById('currentDate').textContent = dateStr;
    document.getElementById('footerDate').textContent = now.toLocaleDateString('es-ES');
}

// Formatear fecha
function formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('es-ES');
}

// Verificar si es admin (para área admin)
function checkAdminAccess() {
    const password = prompt('Contraseña de administrador:');
    if (password === CONFIG.adminPassword) {
        return true;
    } else {
        alert('Contraseña incorrecta');
        return false;
    }
}

// Generar token aleatorio (para área admin)
function generateToken(days = 7) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let token = '';
    
    for (let i = 0; i < 16; i++) {
        token += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    
    // Calcular fecha de expiración
    const expireDate = new Date();
    expireDate.setDate(expireDate.getDate() + days);
    const expireStr = expireDate.toISOString().split('T')[0];
    
    return {
        token: token,
        expires: expireStr,
        days: days
    };
}
