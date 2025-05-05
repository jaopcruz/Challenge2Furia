import os

# Configurações básicas
SECRET_KEY = os.urandom(24)

# Configurações de upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

# Configurações de API (simuladas)
DOCUMENT_VERIFICATION_API_KEY = 'simulated_key'
SOCIAL_MEDIA_API_KEY = 'simulated_key'