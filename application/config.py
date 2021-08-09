import os

class Config(object):
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = True

class DevelopmentConfig(Config):
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    database_name = os.getenv('DB_NAME')
    port = os.getenv('PORT')


class ProductionConfig(Config):
    pass

class TestConfig(Config):
    pass