#!/usr/bin/env python
import logging
import connexion
from flask_cors import CORS
import jwt
import time

logging.basicConfig(level=logging.INFO)


def hello():
    print('hello: Welcome to related-media server')
    return 'Welcome to related-media server'


JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.exceptions.InvalidTokenError as e:
        # six.raise_from(Unauthorized, e)
        raise Exception(f'Invalid Token:{e}')


def get_secret(user, token_info) -> str:
    return '''
    You are user_id {user} and the secret is 'wbevuec'.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def _current_timestamp() -> int:
    return int(time.time())


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/', debug=True)

    options = {"swagger_ui": True}
    app.add_api('swagger.yaml',
                options=options,
                arguments={'title': 'Hello World Example'})

    CORS(app.app, resources={r"/*": {"origins": "*"}})
    app.run(port=8080)
