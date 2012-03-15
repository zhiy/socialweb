#!/usr/bin/env python
# -*- coding: utf-8 -*-
class country:
    def render(self,country):
        return self.render_string("templates/module-country.html", country=country)

