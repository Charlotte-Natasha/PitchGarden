class Config:
    SECRET_KEY= '0725932962'

class ProdConfig(Config):
    """"""
    
class DevConfig(Config):
    DEBUG = True

config_options = {
    'prod':ProdConfig, 
    'dev':DevConfig
}    