from flask import Flask
from flask.ext.socketio import SocketIO as ServerSocketIO, send

socketio = ServerSocketIO()

def create_app(config_name):
    app = Flask(__name__)
    socketio.init_app(app)
    return app, socketio

@socketio.on('message')
def test_message(message):
    send('', "Hello, " + message)
    #emit('my response', {'data': message['data']})

@socketio.on('connect')
def on_connect():
    send('connected')

if __name__ == '__main__':
    app, sockio = create_app('development')
    socketio.run(app)
