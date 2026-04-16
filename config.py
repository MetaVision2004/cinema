import os

DB_HOST = os.environ.get('DB_HOST', 'railway')
DB_PORT = int(os.environ.get('DB_PORT', 3306))
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'cinema')

MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', '1', 't']
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'dev.daviar@gmail.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'xkljhmsavdvbuded')
EMAIL_DEFAULT_SENDER = os.environ.get('EMAIL_DEFAULT_SENDER', 'dev.daviar@gmail.com')
