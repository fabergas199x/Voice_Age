from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
from main import age

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
	print('Client connected')

@socketio.on('audio')
def audio(message):
	audio = message['audio']
	print("receive")
	f = open('./audio.wav', 'wb')
	f.write(audio)
	f.close
	print(age())
	emit('age', {'age': age()})

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', debug=True)
	# app.run(port=5005)