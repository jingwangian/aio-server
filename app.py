#!/usr/bin/env python
import logging
import connexion
# from connexion.resolver import MethodViewResolver
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

def hello():
    print('hello: Welcome to forecast server')
    return 'Welcome to forecast server'

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/', debug=True)

    options = {"swagger_ui": True}
    # app.add_api('forecast.yaml',
    #             # options=options,
    #             strict_validation=True, validate_responses=True )
    app.add_api('swagger.yaml', 
                options=options,
                arguments={'title': 'Hello World Example'})

    CORS(app.app, resources={r"/*": {"origins": "*"}})
    app.run(port=8080)
