#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
class country:
    def render(self,country):
        return self.render_string("templates/module-country.html", country=country)
class Entry(tornado.web.UIModule):
    def embedded_css(self):
        return ".entry { margin-bottom: 1em; }"

    def render(self, show_comments=False):
        return self.render_string("templates/test.html")

