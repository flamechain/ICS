from flask import Flask
from flask_socketio import SocketIO
from app import create_app
from app.database import Database
import config

app = create_app()
socketio = SocketIO(app)
db = Database()
del db

@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    data = dict(json)

    if "name" in data:
        db = Database()
        db.save_card(data["name"], data["quantity"])

    print(data)

if __name__ == "__main__":
    socketio.run(app, host=config.Config.SERVER, port=config.Config.PORT, debug=config.Config.DEBUG)
