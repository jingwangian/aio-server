import random
import time
import logging
from flask import request
import connexion


logger = logging.getLogger(__name__)

ENTITY_TAGS = [
    {
        "entity": "Donald Trump",
        "tag": "Scott Morrison"
    },
    {
        "entity": "Malcolm Turnbull",
        "tag": "Donald Trump"
    },
    {
        "entity": "Scott Morrison",
        "tag": "Commonwealth Bank"
    },
    {
        "entity": "XiJinPing1",
        "tag": "Google"
    },
    {
        "entity": "Trump",
        "tag": "Apple Inc"
    }
]

ErrorReturnMediaItemIds = ['294292334', '294292330', '294292331']


def get_entity_tags(media_item_id, user, token_info):
    logger.info('Enter get_entity_tags')

    # print(f"get_entity_tags is invoked with id {media_item_id}")
    # print(f'user info-->{user}')
    # print(f'token_info-->{token_info}')
    # print('request-->', request.remote_addr)
    # print('connexion.request-->', connexion.request.remote_addr)

    time.sleep(1)

    if media_item_id in ErrorReturnMediaItemIds:
        return '', 404, {'Access-Control-Allow-Credentials': 'true'}

    # n = random.randrange(1, 10)
    # print(f'choice number is {n}')

    # if n > 6:
    #     return '', 404

    logger.info('Exit get_entity_tags')
    return ENTITY_TAGS, 200, {'Access-Control-Allow-Credentials': 'true'}
