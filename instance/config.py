import os


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('MY_SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_data'


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
