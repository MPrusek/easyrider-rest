MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'apitest'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
schema_point = {
    'uuid4': {
        'type': 'string',
        'required': True,
    },
    'point': {
        'type': 'dict',
        'schema': {
            'lat': {'type': 'string'},
            'lon': {'type': 'string'},
        }
    },
    'time': {'type': 'string'},
    'worker_id': {'type': 'string'}
}
schema_track = {
    'uuid4': {
        'type': 'string',
        'required': True,
    },
    'point': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'lat': {'type': 'string'},
                'lon': {'type': 'string'},
                'time': {'type': 'integer'}
            }
        }
    },
    'distance': {'type': 'integer'},
    'name': {'type': 'string'},
    'timestart': {'type': 'integer'},
    'timestop': {'type': 'integer'}
}
point = {
    'item_title': 'point',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'uuid4',
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': schema_point
}
track = {
    'item_title': 'track',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'uuid4',
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': schema_track
}

DOMAIN = {
    'point': point,
    'track': track
}
