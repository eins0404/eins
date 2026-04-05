import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/concept')
def concept():
    return send_from_directory(BASE_DIR, 'PID의_개념.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
