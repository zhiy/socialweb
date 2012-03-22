#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.options
import os,sys
from sina import *
from tencent import *
import json
import uimodules
tornado.options.parse_command_line()

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("templates/main.html")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        sina_client=sina()
        country=sina_client.get_country()
        return self.render("templates/index.html",country=country)
class countryhandler(tornado.web.RequestHandler):
    def get(self):
        sina_client=sina()
        country=sina_client.get_country()
        return self.render("templates/country.html",country=country)
class provincehandler(tornado.web.RequestHandler):
    def get(self,id):
        sina_client=sina()
        provinces=sina_client.get_province(id)
        return self.render("templates/provinces.html",provinces=provinces)

class cityhandler(tornado.web.RequestHandler):
    def get(self,id):
        sina_client=sina()
        cities=sina_client.get_city(id)
        return self.render("templates/cities.html",cities=cities)

class hotusers_handler(tornado.web.RequestHandler):
    def get(self,category='default'):
        sina_client=sina()
        sina_users=sina_client.hot_users(category)
        #tencent_client=tencent()
        #tencent_users=tencent_client.getTrendsFamouslist(101)["data"]["info"]
        return self.render("templates/users.html",category=category,users=sina_users)

class new_public_tweets_handler(tornado.web.RequestHandler):
    def get(self):
        sina_client=sina()
        tweets=sina_client.get_public_timeline()["statuses"]
        return self.render("templates/new_tweets.html",tweets=tweets)
        
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": False,
    "debug": True,
    "ui_modules": uimodules,
    }
application = tornado.web.Application([
    (r"/test", TestHandler),
    (r"/", MainHandler),
    (r"/get_country",countryhandler),
    (r"/get_province/(.*)",provincehandler),
    (r"/get_cities/(.*)",cityhandler),
    (r"/hotusers/(.*)",hotusers_handler),
    (r"/new_public_tweets",new_public_tweets_handler)],**settings)

if __name__ == "__main__":
    port=int(sys.argv[1])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
