# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

from views import (IndexHandler,
                   CommandHandler,)

urls = [
    # (r'/', IndexHandler),
    (r'^/command$', CommandHandler),
]