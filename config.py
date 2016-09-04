import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'mingyuejishiyou'

class DevelopmentConfig(Config):
    DEBUG=True

config={
    'default':DevelopmentConfig
}