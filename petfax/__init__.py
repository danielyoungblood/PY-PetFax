from flask import Flask

app = Flask(__name__)


def create_app():
    from . import pet
    from . import fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    
    return app
