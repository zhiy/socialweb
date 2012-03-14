#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
import json
import time,sys
sys.path.append("..")
from helper import httpclient
from helper.utils import *
class sohu:
    def __init__(self):
        self.prefix="http://api.t.sohu.com/"
        self.http=httpclient.httpclient()
