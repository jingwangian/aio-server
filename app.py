#!/usr/bin/env python
import logging
import connexion
from flask_cors import CORS
import jwt
import time
from logging.config import dictConfig
from log import configure_logger

from flask.logging import default_handler

# logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


def hello():
    logger.info('hello: Welcome to related-media server info')

    return 'Welcome to related-media server'


def listener_configurer():
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('logconfig.log', 'a', 2048, 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setLevel(logging.INFO)
    h.setFormatter(f)
    root.addHandler(h)
    root.setLevel(logging.INFO)


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/', debug=True)

    listener_configurer()
    options = {"swagger_ui": True}
    app.add_api('swagger.yaml',
                options=options,
                arguments={'title': 'Hello World Example'})

    CORS(app.app, resources={r"/*": {"origins": "*"}})
    app.run(port=8080)
