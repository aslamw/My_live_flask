import os, datetime

class DefaultConfig:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    DEVELOPMENT = True
    
    

class TestingConfig(DefaultConfig):
    
    # Configurações gerais
    TESTING = True
    DEBUG = False

    # Chave secreta para proteger a sessão e outros dados sensíveis
    JWT_SECRET_KEY = 'chave_secreta_de_teste'
    JWT_SECRET_KEY = datetime.timedelta(hours=1)

    # Configurações do banco de dados para testes
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração de logging
    LOGGING_LOCATION = 'logs'
    LOGGING_LEVEL = 'ERROR'

    # Configuração para armazenamento de arquivos estáticos e uploads
    UPLOAD_FOLDER = 'test_uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class ProductionConfig(DefaultConfig):
    # Configurações gerais
    DEBUG = True
    TESTING = False

    # Chave secreta para proteger a sessão e outros dados sensíveis
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui'

    # Configurações do banco de dados
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///daily.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração do servidor de e-mail
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@example.com'

    # Configuração de logging
    LOGGING_LOCATION = 'logs'
    LOGGING_LEVEL = 'INFO'

    # Configuração para armazenamento de arquivos estáticos e uploads
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    # Outras configurações específicas da produção
    # SERVER_NAME = 'yourdomain.com'  # Nome do servidor para gerar URLs absolutas
    SESSION_COOKIE_SECURE = True  # Garante que os cookies de sessão sejam enviados apenas por HTTPS
    REMEMBER_COOKIE_SECURE = True  # Garante que os cookies "remember me" sejam enviados apenas por HTTPS
    CSRF_COOKIE_SECURE = True  # Garante que o cookie CSRF seja enviado apenas por HTTPS
    SESSION_COOKIE_HTTPONLY = True  # Impede que os cookies de sessão sejam acessados por JavaScript
    REMEMBER_COOKIE_HTTPONLY = True  # Impede que os cookies "remember me" sejam acessados por JavaScript
    CSRF_COOKIE_HTTPONLY = True  # Impede que o cookie CSRF seja acessado por JavaScript
    PREFERRED_URL_SCHEME = 'https'  # Define o esquema de URL preferido para gerar URLs absolutas

    # Configurações de segurança
    # ...

    # Configurações de cache
    # ...
