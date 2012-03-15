#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.options
import os,sys
from sina import *
import json
tornado.options.parse_command_line()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        sina_client=sina()
        country=sina_client.get_country()
        return self.render("templates/index.html",country=country)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": False,
    "debug": True,
    }
application = tornado.web.Application([
    (r"/", MainHandler),],**settings)

if __name__ == "__main__":
    port=int(sys.argv[1])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
