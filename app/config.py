class Config:
    SECRET_KEY= '0725932962'

class ProdConfig(Config):
    """"""
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://natasha245:123456@localhost:5432/pitches'
    DEBUG = True

config_options = {
    'prod':ProdConfig, 
    'dev':DevConfig
}    