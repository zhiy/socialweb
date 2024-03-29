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
access_token="2.00NDjtACBrzXgEf010e7fa5fh3_RtB"
class sina:
    def __init__(self):
        self.prefix="https://api.weibo.com/2/"
        self.http=httpclient.httpclient()
        self.access_token=access_token
    def login():
        pass
    def get_public_timeline(self,count=50,page=1,base_app=0):
        """
        返回最新的公共微博 http://open.weibo.com/wiki/2/statuses/public_timeline
        count 单页返回的记录条数，默认为50
        page 返回结果的页码，默认为1。
        base_app 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        """
        request_url=self.prefix+"statuses/public_timeline.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_repost_daily(self,count=50,page=1,base_app=0):
        """
        按天返回热门微博转发榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/repost_daily.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_repost_weekly(self,count=50,page=1,base_app=0):
        """
        按周返回热门微博转发榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/repost_weekly.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_comments_daily(self,count=50,page=1,base_app=0):
        """
        按天返回热门微博评论榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/comments_daily.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))
    
    def hot_comments_weekly(self,count=50,page=1,base_app=0):
        """
        按周返回热门微博评论榜的微博列表
        """
        request_url=self.prefix+"statuses/hot/comments_weekly.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))

    def hot_users(self,category="default"):
        """
        返回系统推荐的热门用户列表 http://open.weibo.com/wiki/2/suggestions/users/hot
        """
        request_url=self.prefix+"suggestions/users/hot.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"category":category})
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
    # 用户相关 API
    ##################################

    def friends_timeline_ids(self,feature=0,page=1,count=50,max_id=0,since_id=0,base_app=0):
        """
        获取当前登录用户及其所关注用户的最新微博的ID
        since_id int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count 单页返回的记录条数，默认为50。
        page 返回结果的页码，默认为1。
        base_app 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature 过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        """
        request_url=self.prefix+"statuses/friends_timeline/ids.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"feature":feature,"max_id":max_id,"since_id":since_id,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))

    def friends_timeline(self,feature=0,page=1,count=1,max_id=0,since_id=0,base_app=0):
        """
        获取当前登录用户及其所关注用户的最新微博
        since_id int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count 单页返回的记录条数，默认为50。
        page 返回结果的页码，默认为1。
        base_app 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature 过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        """
        request_url=self.prefix+"statuses/friends_timeline.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"feature":feature,"max_id":max_id,"since_id":since_id,"base_app":base_app})
        print request_url
        return json.loads(self.http.get(request_url))

    def user_timeline(self,trim_user=0,feature=0,page=1,count=1,max_id=0,since_id=0,base_app=0,uid='',screen_name=''):
        """
        获取某个用户最新发表的微博列表
        uid 需要查询的用户ID。
        screen_name 需要查询的用户昵称。
        trim_user 返回值中user信息开关，0：返回完整的user信息、1：user字段仅返回user_id，默认为0。
        since_id int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        max_id int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        count 单页返回的记录条数，默认为50。
        page 返回结果的页码，默认为1。
        base_app 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        feature 过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        参数uid与screen_name二者必选其一，且只能选其一
        参数uid与screen_name都没有或错误，则默认返回当前登录用户的数据
        """
        request_url=self.prefix+"statuses/user_timeline.json?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"count":count,"page":page,"feature":feature,"max_id":max_id,"since_id":since_id,"base_app":base_app,"trim_user":trim_user})
        print request_url
        return json.loads(self.http.get(request_url))

    def new_tweet(self,text,lat=0,long=0):
        """
        发布一条新微博
        status 要发布的微博文本内容，必须做URLencode，内容不超过140个汉字。
        lat float	纬度，有效范围：-90.0到+90.0，+表示北纬，默认为0.0。
        long float	经度，有效范围：-180.0到+180.0，+表示东经，默认为0.0。
        annotations	string	元数据，主要是为了方便第三方应用记录一些适合于自己使用的信息，每条微博可以包含一个或者多个元数据，必须以json字串的形式提交，字串长度不超过512个字符，具体内容可以自定。
        """
        request_url=self.prefix+"statuses/update.json"
        data=urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"lat":lat,"long":long,"status":text})
        print request_url
        return json.loads(self.http.post(request_url,data))
    
    def new_tweet_pic(self,text,pic_path,lat=0,long=0):
        """
        发布一条新微博并上传图片
        status 要发布的微博文本内容，必须做URLencode，内容不超过140个汉字。
        pic	true	binary	要上传的图片，仅支持JPEG、GIF、PNG格式，图片大小小于5M。
        lat float	纬度，有效范围：-90.0到+90.0，+表示北纬，默认为0.0。
        long float	经度，有效范围：-180.0到+180.0，+表示东经，默认为0.0。
        annotations	string	元数据，主要是为了方便第三方应用记录一些适合于自己使用的信息，每条微博可以包含一个或者多个元数据，必须以json字串的形式提交，字串长度不超过512个字符，具体内容可以自定。
        """
        request_url=self.prefix+"statuses/upload.json"
        pic_binary=open(pic_path,"rb")
        form = httpclient.MultiPartForm()
        #form.add_field('source', APP_KEY)
        #form.add_field('access_token', self.access_token)
        form.add_field('lat', lat)
        form.add_field('long', long)
        form.add_field('status', text)
        # Add a file
        form.add_file('pic', pic_path,pic_binary)
        # Build the request
        request = urllib2.Request(request_url+"?"+urllib.urlencode({"source":APP_KEY,"access_token":self.access_token}))
        body = str(form)
        request.add_header('Content-type', 'multipart/form-data')
        request.add_header('Content-length', len(body))
        request.add_data(body)
        print 'OUTGOING DATA:'
        print request.get_data()
        print 'SERVER RESPONSE:'
        try:
            print urllib2.urlopen(request).read()
        except urllib2.HTTPError, error:
            print error.read()

    def comments_create(self,id,text,comment_ori=0):
        """
        对一条微博进行评论
        """
        request_url=self.prefix+"comments/create.json"
        data=urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"id":id,"comment":text,"comment_ori":comment_ori})
        print request_url
        return json.loads(self.http.post(request_url,data))

    def statuses_repost(self,id,text,is_comment=0):
        """
        转发一条微博
        """
        request_url=self.prefix+"statuses/repost.json"
        data=urllib.urlencode({"source":APP_KEY,"access_token":self.access_token,"id":id,"status":text,"is_comment":is_comment})
        print request_url
        return json.loads(self.http.post(request_url,data))
    ##################################
    # 公共服务 API
    ##################################
    def get_province(self,country,language="zh-cn",capital=''):
        """获取省份列表
        capital 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        country code
        """
        request_url=''
        if capital=='':
            request_url=self.prefix+"common/get_province.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language,"country":country})
        else:
            request_url=self.prefix+"common/get_province.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language,"capital":capital,"country":country})
        print request_url
        provinces=json.loads(self.http.get(request_url))
        result=[]
        for province in provinces:
            item={}
            item["id"]=province.keys()[0]
            item["name"]=province.values()[0]
            result.append(item)
        return result
    def get_country(self,language="zh-cn",capital=''):
        """获取国家列表
        capital 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        """
        request_url=''
        if capital=='':
            request_url=self.prefix+"common/get_country.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language})
        else:
            request_url=self.prefix+"common/get_country.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language,"capital":capital})
        print request_url
        countries=json.loads(self.http.get(request_url))
        result=[]
        for country in countries:
            item={}
            item["id"]=country.keys()[0]
            item["name"]=country.values()[0]
            result.append(item)
        return result

    def get_city(self,province,language="zh-cn",capital=''):
        """获取城市列表
        capital 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        province code
        """
        request_url=''
        if capital=='':
            request_url=self.prefix+"common/get_city.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language,"province":province})
        else:
            request_url=self.prefix+"common/get_city.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language,"capital":capital,"province":province})
        print request_url
        cities=json.loads(self.http.get(request_url))
        result=[]
        for city in cities:
            item={}
            item["id"]=city.keys()[0]
            item["name"]=city.values()[0]
            result.append(item)
        return result

    def get_timezone(self,language="zh-cn"):
        """get_timezone
        language 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        """
        request_url=self.prefix+"common/get_timezone.json?"+urllib.urlencode({"access_token":self.access_token,"source":APP_KEY,"language":language})
        print request_url
        return json.loads(self.http.get(request_url))

    def test_oauth(self):
        request_url="https://api.weibo.com/oauth2/authorize?"+urllib.urlencode({"client_id":client_id,"redirect_uri":"http://122.248.200.28:8888"})
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
    #print pprint(client.get_public_timeline())
    #print pprint(client.hot_comments_weekly(access_token="2.00NDjtACBrzXgEc4afeab580X2PnKB"))
    print client.test_oauth()
    #print pprint(client.new_tweet_pic("hello world","pic.png"))
    #tweets_ids=client.friends_timeline_ids()["statuses"]
    #for id in tweets_ids:
    #   print client.statuses_repost(id,"I like it!!!!")
    #  time.sleep(3)
