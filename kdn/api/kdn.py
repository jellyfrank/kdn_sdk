#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .query import Query
from .order import Order
from .service import Service
from .logistic import Logistic
import csv
import os


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

    @classmethod
    def get_express_list(cls):
        """
        获取支持的公司列表
        返回包含代码和名称的字典
        """
        express = {}
        csv_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(csv_path, "data/express.csv")) as f:
            for row in csv.reader(f):
                express[row[1].strip()] = row[0].strip()
        return express

    @classmethod
    def get_eorder_express(cls):
        """
        获取支持电子面单的物流公司
        """
        codes = []
        filelist = ('direct.csv', 'eorder.csv',
                    'kdn.csv', 'month.csv', 'offline.csv')
        csv_path = os.path.dirname(os.path.dirname(__file__))
        for file in filelist:
            with open(os.path.join(csv_path, f"data/{file}")) as f:
                for row in csv.reader(f):
                    codes.append(row[0])
        return set(list(codes))

    @classmethod
    def get_templates(cls):
        """
        获取电子面单模板
        """
        templates = []
        csv_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(csv_path, "data/templates.csv")) as f:
            for row in csv.reader(f):
                templates.append(tuple(row))
        return templates

    @classmethod
    def get_express_types(self):
        """获取快递公司业务类型"""
        types = []
        csv_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(csv_path, "data/exptype.csv")) as f:
            for row in csv.reader(f):
                types.append(tuple(row))
        return types

    @classmethod
    def get_preorder_express(self):
        """get express list which supported preordering"""
        expresses =[]
        csv_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(csv_path, "data/preorder.csv")) as f:
            for row in csv.reader(f):
                expresses.append(row[0])
        return expresses

    comm = Comm()
    query = Query()
    order = Order()
    service = Service()
    logistic = Logistic()
