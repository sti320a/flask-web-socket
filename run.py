from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from app.server import app

if __name__ == '__main__':
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