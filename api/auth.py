import jwt
import time
import logging

logger = logging.getLogger(__name__)

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def login(user_id, password):
    logger.info(f'login with user{user_id} and password {password}')
    if (user_id != '12345' or password != '123456'):
        return 'Invalid user id or password', 401, {'Access-Control-Allow-Credentials': 'true'}

    return generate_token(user_id), 200, {'Access-Control-Allow-Credentials': 'true'}


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": {'id': user_id, 'name': 'ian.wang', 'role': 'admin'},
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.exceptions.InvalidTokenError as e:
        # six.raise_from(Unauthorized, e)
        raise Exception(f'Invalid Token:{e}')


def get_secret(user, token_info) -> str:
    logger.info('Enter get_secret function')
    return '''
    You are user_id {user} and the secret is 'wbevuec'.
    Decoded token claims: {token_info}.
    '''.format(user=user['id'], token_info=token_info)


def _current_timestamp() -> int:
    return int(time.time())
