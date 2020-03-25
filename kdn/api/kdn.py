#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .order import Query


SANDBOXURL = "http://sandboxapi.kdniao.com:8080/kdniaosandbox/gateway/exterfaceInvoke.json"
URL = "http://api.kdniao.com"


class KDN(object):

    def __init__(self, client_id, api_key, sandbox=False):
        """
        params:
        client_id: 商户ID,
        api_key: API KEY,
        sandbox: 是否沙箱测试环境
        """
        self.client_id = client_id
        self.api_key = api_key
        self.sandbox = sandbox
        self.url = SANDBOXURL if self.sandbox else URL

    comm = Comm()
    query = Query()
