import json

import requests


class Servers(object):
    def __init__(self, corpid, corpsecret, agentid):
        self.access_token = ""
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.agentid = agentid

    def get_access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}".format(
            ID=self.corpid, SECRET=self.corpsecret)
        rsp = requests.get(url)
        try:
            if rsp.json()["errcode"] == 0:
                okJson = rsp.json()
                self.access_token = okJson["access_token"]
        except KeyError:
            print("获取access_token失败")

    def send_text(self, text):
        json = {
            "touser": "@all",
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": text
            }
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}".format(
            ACCESS_TOKEN=self.access_token)
        rsp = requests.post(url, json=json)
        try:
            if rsp.json()["errcode"] == 0:
                return True
        except:
            return False