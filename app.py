from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/laptop_Rob")
def receiver_page():
    return render_template('receiver.html')

@socketio.on('offer')
def handle_offer(data):
    socketio.emit('offer', data)

@socketio.on('answer')
def handle_answer(data):
    socketio.emit('answer', data)

@socketio.on('candidate')
def handle_candidate(data):
    socketio.emit('candidate', data)

if __name__ == "__main__":
    socketio.run(app) 