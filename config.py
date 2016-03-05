class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret!'

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig,
}
