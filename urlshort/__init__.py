from flask import Flask
def create(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'vaishnavikale'
    from . import urlshort
    app.register_blueprint(urlshort.bp)
    return app