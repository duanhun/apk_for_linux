# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from urls import urls


from tornado.options import define, options
define("port", default=12345, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=urls)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()