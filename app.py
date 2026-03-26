from flask import Flask, jsonify
from blueprints.rooms import rooms_bp
from blueprints.devices import devices_bp
from db import load_db

def create_app():
    load_db()

    app = Flask(__name__)

    app.register_blueprint(rooms_bp, url_prefix='/rooms')
    app.register_blueprint(devices_bp, url_prefix='/devices')

    @app.get('/')
    def index():
        return jsonify({'message': 'Welcome to your smart home! Use /rooms or /devices to explore.'})
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)