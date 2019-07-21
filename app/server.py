from flask import Flask, request, render_template
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pipe')
def pipe():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        print('Connected')

        while True:
            msg = input('> ')
            if msg == 'exit':
                print('Closed')
                sys.exit()
            ws.send(msg)

