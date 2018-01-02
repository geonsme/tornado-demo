# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop
import tornado.web
import tornado.autoreload   

settings = {'debug' : True}
DEBUG = False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print 'hello'
        self.write('hello world')

class NewStoreHandler(tornado.web.RequestHandler):
    def get(self):
        print 'new'
        self.write({'text': 'zdfasdfadsf'})
    
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/new", NewStoreHandler),
        ], **settings)

def main():
    app = make_app()
    if DEBUG:
        app.listen(5000)
        IOLoop.current().start()
    else:
        server = tornado.httpserver.HTTPServer(app)
        server.listen(8000)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()