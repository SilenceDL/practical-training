
import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from machine_learning.load_model.loadModel import lrModel


# 127.0.0.1:8888/jb?txt=他来到了网易杭研大厦
define("port", default=8888, help="run on the given port", type=int)


class lrHandler(tornado.web.RequestHandler):

    def post(self):
        lr = lrModel()
        city = self.get_argument('city')
        experience = float(self.get_argument('experience'))
        education = self.get_argument('education')
        result = str(lr.wage_pred(city, experience, education))
        self.set_header("Content-Type", "Application/json")
        self.write(json.dumps(result, ensure_ascii=False))
        self.finish()

    def get(self):
        lr = lrModel()
        city = self.get_argument('city')
        experience = float(self.get_argument('experience'))
        education = self.get_argument('education')
        result = str(lr.wage_pred(city, experience, education))
        self.set_header("Content-Type", "Application/json")
        self.write(json.dumps(result, ensure_ascii=False))
        self.finish()





if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/lr', lrHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
