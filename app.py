#!/usr/bin/env python
import logging
import connexion
from flask_cors import CORS
import jwt
import time
from logging.config import dictConfig
from log import configure_logger

# logging.basicConfig(level=logging.INFO)

logger = configure_logger(__name__)

print('test', __name__)


def hello():
    print('name is ', __name__)
    logger.info('hello: Welcome to related-media server info')
    logger.warning('hello: Welcome to related-media server warning')
    logger.error('hello: Welcome to related-media server, error')
    print('hello: Welcome to related-media server - print')
    return 'Welcome to related-media server'


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/', debug=True)

    options = {"swagger_ui": True}
    app.add_api('swagger.yaml',
                options=options,
                arguments={'title': 'Hello World Example'})

    CORS(app.app, resources={r"/*": {"origins": "*"}})
    app.run(port=8080)
