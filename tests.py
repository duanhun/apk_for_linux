# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

import commands


if __name__ == "__main__":
    (status, output) = commands.getstatusoutput("dir")
    print  output.decode('gbk').encode('utf8')