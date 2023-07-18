import logging

from src.app import create_app

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('start app')

    app = create_app()
    app.run(
        port=app.config['APP_PORT'],
        host=app.config['APP_HOST'],
        debug=False
    )
    return app


if __name__ == "__main__":
    main()
