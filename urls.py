# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

from views import (IndexHandler,
                   CommandHandler,
                   GameHandler,
                   HomeHandler)

urls = [
    # (r'/', IndexHandler),
    (r'^/command$', CommandHandler),
    (r'^/game$', GameHandler),
    (r'^/index$', HomeHandler)
]