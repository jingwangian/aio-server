import time

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

def get_entity_tags(media_item_id):
    print(f"get_entity_tags is invoked with id {media_item_id}")

    time.sleep(1)

    # return [],404, {'Access-Control-Allow-Credentials':'true'}
    return ENTITY_TAGS, 200, {'Access-Control-Allow-Credentials':'true'}
