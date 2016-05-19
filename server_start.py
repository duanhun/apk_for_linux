# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from urls import urls


from tornado.options import define, options
define("port", default=12345, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=urls,
                                  static_path=os.path.join(os.path.dirname(__file__), "static"),)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port + 'command?cmd=echo11'
    print 'Quit the server with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()