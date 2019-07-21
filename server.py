from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer 
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pipe')
def pipe():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']

        while True:
            ws.send(input())


if __name__ == "__main__":
    app.debug = True

    host = 'localhost'
    port = 8080
    host_port = (host, port)

    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()
