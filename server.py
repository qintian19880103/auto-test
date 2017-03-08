#coding:utf-8

import tornado.ioloop
import tornado.options
from tornado.options import define, options
define("port", default=8011, help="run on the given port", type=int)

from application import application


if __name__ == "__main__":
  tornado.options.parse_command_line()
  application.listen(options.port)
  print 'Development server is running at http://127.0.0.1:%s/' % options.port
  print 'Quit the server with CONTROL-C'
  tornado.ioloop.IOLoop.instance().start()
