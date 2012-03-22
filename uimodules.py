#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
class Country:
    def render(self,country):
        return self.render_string("templates/module-country.html", country=country)

class User(tornado.web.UIModule):
    def render(self,user):
        return self.render_string("templates/module_user.html",user=user)

class Tweet(tornado.web.UIModule):
    def render(self,tweet):
        return self.render_string("templates/module_tweet.html",tweet=tweet)



