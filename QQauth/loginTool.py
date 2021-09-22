from django.conf import settings
from urllib.parse import urlencode,parse_qs
import json
import requests

class QQAuth(object):
    def __init__(self,clientId=None,clientSecret=None,redirectUrl=None):
        self.clientId=clientId
        self.clientSecret=clientSecret
        self.redirectUrl=redirectUrl#重定向的url内容


    def createURL(self):
        dataDict={
            "response_type":"code",
            "client_id":self.clientId,
            "redirect_url":self.redirectUrl,
        }
        #根据数据构建形成访问的url
        QQAuthUrl= 'https://graph.qq.com/oauth2.0/authorize?' + urlencode(dataDict)

        return QQAuthUrl

    #这里返回一个认证token
    def getAccessToken(self,code):
        dataDict={
            "grant_type":"authorization_code",
            "client_id":self.clientId,
            "client_secret":self.clientSecret,
            "redirect_url":self.redirectUrl,
            "code":code
        }
        #构建认证的url
        accessUrl = 'https://graph.qq.com/oauth2.0/token?' + urlencode(dataDict)
        try:
            res= requests.get(accessUrl)#请求该连接
            data=parse_qs(res.text)#将数据转换为字典
            # 将认证token提取出来，数据没有时默认为none
            accessToken = data.get("access_token", None)
            if not accessToken:
                raise Exception("获取token报错")
            #正常获取token时将数据进行返回
            return accessToken[0]
        except Exception as e:
            print(e)
            raise Exception("请求qq认证内容时报错")

    def getOpenId(self,accessToken):
        #请求url
        url = 'https://graph.qq.com/oauth2.0/me?access_token=' + accessToken
        try:
            res=requests.get(url)
            data=res.text[10:-3]
            dataDict=json.loads(data)
            openId=dataDict.get("openid")
            return openId
        except Exception as e:
            print(e)
            raise Exception("返回qq认证token报错")