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
from copy import deepcopy
import logging

_logger = logging.getLogger(__name__)


class Comm(object):

    def __get__(self, instance, owner):
        self.client_id = instance.client_id
        self.api_key = instance.api_key
        self.sandbox = instance.sandbox
        self.url = instance.url
        return self

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
        to_sign = f"{data}{self.api_key}".encode(
            "utf-8")
        sign = base64.b64encode(
            md5(to_sign).hexdigest().encode("utf-8")).decode("utf-8")
        return sign

    def _remove_none(self, d):
        dx = deepcopy(d)
        for k, v in d.items():
            if v and type(v) is dict:
                r = self._remove_none(v)
                if r:
                    dx[k] = r
                else:
                    dx[k] = ''
            if v and type(v) is list:
                for i in range(len(v)):
                    dx[k][i] = self._remove_none(v[i])
            if not v:
                dx[k] = ''
        return dx

    def post(self, request_type, data):
        """
        提交请求
        params:
        data: 提交的数据
        """
        data = json.dumps(self._remove_none(
            data), separators=(',', ':'), ensure_ascii=False)
        request_data = {
            "RequestType": request_type,
            "EBusinessID": self.client_id,
            "RequestData": quote_plus(data),
            "DataSign": self._sign(data),
            "DataType": 2
        }
        _logger.debug(f"KDN-SDK POST:{request_data}")
        return requests.post(self.url, data=request_data).json()
