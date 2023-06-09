# app.py is the main entry point to set up Flask application

# import Flask and blueprint from the api module
from flask import Flask
from api import api

# create a Flask application instance
app = Flask(__name__)

# Register the blueprint. This allows the routes defined in api blueprint to be accessible through the application
app.register_blueprint(api)

# run the application
if __name__ == '__main__':
    app.run()
