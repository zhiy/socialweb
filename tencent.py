#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
import json
#import oauth2 as oauth
import time,sys
sys.path.append("..")
from helper import httpclient
from helper.utils import *
# tencent weibo client
class tencent:
    def __init__(self):
        self.prefix="http://open.t.qq.com/api/"
        self.http=httpclient.httpclient()
    ############
    #话题相关API
    ###########
    def getHtIds(self,httexts,format=json):
        """根据话题名称查询话题id
        httexts: 话题名字列表，用“,”分隔，如abc,efg（最多30个）
        """
        request_url=self.prefix+"ht/ids?"+urllib.urlencode({"format":format,"httexts":httexts})
        return json.loads(self.http.get(request_url))
    def getHtInfo(self,ids,format=json):
        """根据话题id获取话题相关信息
        ids: 话题id列表，用“,”分隔，如12345,12345（最多30个)
        """
        request_url=self.prefix+"ht/info?"+urllib.urlencode({"format":format,"ids":ids})
        return json.loads(self.http.get(request_url))
    ############
    #trends api 热度，趋势
    ###########
    def getTrendsFamouslist(self,classid='',subclassid=''):
        """get famouslist
        http://wiki.open.t.qq.com/index.php/%E7%83%AD%E5%BA%A6%EF%BC%8C%E8%B6%8B%E5%8A%BF/%E6%8E%A8%E8%8D%90%E5%90%8D%E4%BA%BA%E5%88%97%E8%A1%A8
        """
        request_url=self.prefix+"trends/famouslist?"+urllib.urlencode({"format":"json","classid":classid,"subclassid":subclassid})
        return json.loads(self.http.get(request_url))
    def getTrendsHt(self,type=1,format=json,reqnum=20,pos=0):
        """get hot topic
        热度，趋势/话题热榜
        type 请求类型（1-话题名，2-搜索关键字，3-两种类型都有）
        reqnum: 0-20
        """
        request_url=self.prefix+"trends/ht?"+urllib.urlencode({"format":format,"type":type,"reqnum":reqnum,"pos":pos})
        return json.loads(self.http.get(request_url))
    def getTrendsT(self,type,format=json,reqnum=20,pos=0):
        """get topic
        http://wiki.open.t.qq.com/index.php/%E7%83%AD%E5%BA%A6%EF%BC%8C%E8%B6%8B%E5%8A%BF/%E8%BD%AC%E6%92%AD%E7%83%AD%E6%A6%9C
        type: 0x1-带文本 0x2-带链接 0x4-带图片 0x8-带视频 如需拉取多个类型请使用|，如(0x1|0x2)得到3，此时type=3即可，填零表示拉取所有类型
        pos: 翻页标识
        reqnum: 1-100
        """
        request_url=self.prefix+"trends/t?"+urllib.urlencode({"format":format,"type":type,"reqnum":reqnum,"pos":pos})
        return json.loads(self.http.get(request_url))

if __name__=="__main__":
    client=tencent()
    print pprint(client.getTrendsFamouslist(101))

