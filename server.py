from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer 
from geventwebsocket.handler import WebSocketHandler
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
            try:
                msg = input('>')
                if msg == 'exit': sys.exit()
                ws.send(msg)
            except KeyboardInterrupt:
                print('Closed')
                sys.exit()


if __name__ == "__main__":
    app.debug = True

    host = 'localhost'
    port = 5000
    host_port = (host, port)

    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()

