from flask import Flask
from app.config.settings import Config
from app.database import db
from app.routes.alunos import alunos_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(alunos_bp)

    return app
