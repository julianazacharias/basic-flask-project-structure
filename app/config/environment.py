import os

class Environment:
    DEBUG=True
    ENV='development'
    SECRET_KEY='development_key'
    #database

class ProductionEnvironment(Environment):
    DEBUG=False
    ENV='production'
    SECRET_KEY=os.getenv('SECRET')
    #database

#database URI