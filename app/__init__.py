from flask import Flask
from .config.environment import ProductionEnvironment
from .routes.index import blueprint as index

def create_app():
    app = Flask(__name__)
    #config params
    app.config.from_object(ProductionEnvironment)
    
    #blueprints
    app.register_blueprint(index)

    return app