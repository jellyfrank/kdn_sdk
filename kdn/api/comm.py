#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

# 接口调用公共类

import json
from hashlib import md5
import base64
from urllib.parse import urlencode, quote_plus, quote
import requests
import csv


class Comm(object):

    def __get__(self, instance, owner):
        self.client_id = instance.client_id
        self.api_key = instance.api_key
        self.sandbox = instance.sandbox
        self.url = instance.url
        return self

    def _get_express_list(self):
        """
        获取支持的公司列表
        """
        express = {}
        with open("kdn/data/express.csv") as f:
            for row in csv.reader(f):
                express[row[1].strip()] = row[0].strip()
        return express

    def _get_request_header(self):
        """
        获取固定的header
        """
        header = {
            "Content-Type": "application/x-www-form-urlencoded; charset = utf-8",
        }
        return header

    def _sign(self, data):
        """
        签名逻辑
        """
        to_sign = f"{''.join(str(data).split())}{self.api_key}".encode(
            "utf-8")
        sign = base64.b64encode(
            md5(to_sign).hexdigest().encode("utf-8")).decode("utf-8")
        return sign

    def post(self, request_type, data):
        """
        提交请求
        params:
        data: 提交的数据
        """
        data = json.dumps({key: value for key, value in data.items() if value})
        request_data = {
            "RequestType": request_type,
            "EBusinessID": self.client_id,
            "RequestData": quote(''.join(str(data).split())),
            "DataSign": self._sign(data),
            "DataType": 2
        }
        return requests.post(self.url, data=request_data).json()
