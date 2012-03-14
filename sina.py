#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
import json
import time,sys
sys.path.append("..")
from helper import httpclient
from helper.utils import *
import urlparse
APP_KEY="4293240035"
client_id="4293240035"
consume_key="4293240035"
consume_secret="eb59f40b252b8826646fd457ef9cb4d9"
authorize_url="https://api.weibo.com/oauth2/authorize"
access_token_url="https://api.weibo.com/oauth2/access_token"
class sina:
    def __init__(self):
        self.prefix="https://api.weibo.com/2/"
        self.http=httpclient.httpclient()
    def get_public_timeline(self,access_token,count=50,page=1,base_app=0):
        """
        返回最新的公共微博 http://open.weibo.com/wiki/2/statuses/public_timeline
        count 单页返回的记录条数，默认为50
        page 返回结果的页码，默认为1。
        base_app 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        """
        request_url=self.prefix+"statuses/public_timeline.json?"+urllib.urlencode({"source":APP_KEY,"access_token":access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_repost_daily(self,access_token,count=50,page=1,base_app=0):
        """
        按天返回热门微博转发榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/repost_daily.json?"+urllib.urlencode({"source":APP_KEY,"access_token":access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_repost_weekly(self,access_token,count=50,page=1,base_app=0):
        """
        按周返回热门微博转发榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/repost_weekly.json?"+urllib.urlencode({"source":APP_KEY,"access_token":access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_comments_daily(self,access_token,count=50,page=1,base_app=0):
        """
        按天返回热门微博评论榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/comments_daily.json?"+urllib.urlencode({"source":APP_KEY,"access_token":access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_comments_weekly(self,access_token,count=50,page=1,base_app=0):
        """
        按周返回热门微博评论榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/comments_weekly.json?"+urllib.urlencode({"source":APP_KEY,"access_token":access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))

    def hot_users(self,source,category="default"):
        """
        返回系统推荐的热门用户列表 http://open.weibo.com/wiki/2/suggestions/users/hot
        """
        request_url=self.prefix+"suggestions/users/hot.json?"+urllib.urlencode({"source":APP_KEY,"category":category})
        print request_url
        return json.loads(self.http.get(request_url))

    def hot_tweet(self,source,type=1,is_pic=0,count=20,page=1):
        """
        获取微博精选推荐 http://open.weibo.com/wiki/2/suggestions/statuses/hot
        """
        request_url=self.prefix+"suggestions/statuses/hot.json?"+urllib.urlencode({"source":APP_KEY,"type":type,"is_pic":is_pic,"count":count,"page":page})
        print request_url
        return json.loads(self.http.get(request_url))

    def hot_favorites(self,count=20,page=1):
        """
        返回系统推荐的热门收藏
        """
        request_url=self.prefix+"suggestions/statuses/hot.json?"+urllib.urlencode({"source":APP_KEY,"count":count,"page":page})
        print request_url
        return json.loads(self.http.get(request_url))
    ##################################
    # 公共服务 API
    ##################################
    def get_province(self,access_token,country,language="zh-cn",capital=''):
        """获取省份列表
        capital 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        country code
        """
        request_url=''
        if capital=='':
            request_url=self.prefix+"common/get_province.json?"+urllib.urlencode({"access_token":access_token,"source":APP_KEY,"language":language,"country":country})
        else:
            request_url=self.prefix+"common/get_province.json?"+urllib.urlencode({"access_token":access_token,"source":APP_KEY,"language":language,"capital":capital,"country":country})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def get_country(self,access_token,language="zh-cn",capital=''):
        """获取国家列表
        capital 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        """
        request_url=''
        if capital=='':
            request_url=self.prefix+"common/get_country.json?"+urllib.urlencode({"access_token":access_token,"source":APP_KEY,"language":language})
        else:
            request_url=self.prefix+"common/get_country.json?"+urllib.urlencode({"access_token":access_token,"source":APP_KEY,"language":language,"capital":capital})
        print request_url
        return json.loads(self.http.get(request_url))

    def get_city(self,access_token,province,language="zh-cn",capital=''):
        """获取城市列表
        capital 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        province code
        """
        request_url=''
        if capital=='':
            request_url=self.prefix+"common/get_province.json?"+urllib.urlencode({"access_token":access_token,"source":APP_KEY,"language":language,"province":province})
        else:
            request_url=self.prefix+"common/get_province.json?"+urllib.urlencode({"access_token":access_token,"source":APP_KEY,"language":language,"capital":capital,"province":province})
        print request_url
        return json.loads(self.http.get(request_url))

    def test_oauth(self):
        request_url="https://api.weibo.com/oauth2/authorize?"+urllib.urlencode({"client_id":client_id,"redirect_uri":"http://127.0.0.1:8888"})
        print request_url+"\n"
        print "goto the page"
        accepted = 'n'
        while accepted.lower() == 'n':
            accepted = raw_input('Have you authorized me? (y/n) ')
        # http://122.248.200.28:8888/?code=e6d1c32bc74ba76939e03364347105db
        # get the code
        code=raw_input('what is the code in URL?')
        request_url="https://api.weibo.com/oauth2/access_token"
        data=urllib.urlencode({"client_id":client_id,"client_secret":consume_secret,"grant_type":"authorization_code","redirect_uri":"http://122.248.200.28:8888","code":code})
        print request_url
        #换取Access Token
        resp=self.http.post(request_url,data)
        # {"access_token":"2.00NDjtACBrzXgEc4afeab580X2PnKB","expires_in":86400,"remind_in":"86399","uid":"1845546883"}
        print resp
        access_token=json.loads(resp)["access_token"]
        return access_token

if __name__=="__main__":
    client=sina()
    ##print pprint(client.get_public_timeline())
    #print pprint(client.hot_comments_weekly(access_token="2.00NDjtACBrzXgEc4afeab580X2PnKB"))
    #print client.test_oauth()
    print pprint(client.get_province(access_token="2.00NDjtACBrzXgEc4afeab580X2PnKB",country="001"))
