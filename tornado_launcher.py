from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app

port_number=8080

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port_number)
IOLoop.instance().start()
