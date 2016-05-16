# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

import commands

import tornado.web

from utils import logger

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        logger("IndexHandler")
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


class CommandHandler(BaseHandler):
    def get(self):
        command = self.get_argument('cmd', 'echo "error!"')
        logger("command:", command)
        (status, output) = commands.getstatusoutput(command)
        # output = output.decode('gbk').encode('utf8') # windows
        logger("status:", status, "output:", output)
        self.write("Command:" + command)