#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
class httpclient:
    def __init__(self):
        pass
    def get(self,url):
        try:
            return urllib2.urlopen(url).read()
        except Exception as e:
            print e
            return ''
    
            
        
    
