from flask import Flask

from src.config import config
from src.db import create_all
from src.views import view


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE_URL=config.db.url,
        APP_PORT=config.server.port,
        APP_HOST=config.server.host
    )

    create_all()

    app.register_blueprint(view, url_prefix='/api')

    return app
