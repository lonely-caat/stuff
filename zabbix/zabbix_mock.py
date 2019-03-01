import tornado.ioloop
import tornado.web
import json



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(data))
        self.finish()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()