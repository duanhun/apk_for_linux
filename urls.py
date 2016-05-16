# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

from models import (IndexHandler,
                    CommandHandler,)

urls = [
    # (r'/', IndexHandler),
    (r'^/command$', CommandHandler),
]