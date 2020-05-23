#!/usr/bin/python3
# @Time    : 2020-05-11
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from kdn.api.kdn import KDN
import json


class TestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client_id = "test1624824"
        cls.api_key = "f6bc7c23-7d7c-4dc8-9a73-506519393f6a"
        cls.kdn = KDN(cls.client_id, cls.api_key, sandbox=True)

    def test_recognize_code(self):
        """
        测试单号识别
        """
        data = self.kdn.service.recognize_logistic_code("1234561")
        self.assertTrue(data['Success'])

    def test_safe_phone(self):
        """
        测试隐私API
        """
        data = self.kdn.service.safe_phone("1111", "SF", "11111", "占三", "18512341234", "18511112222",
                                           "北京市", "北京市", "中关村", "里斯", "1851113232", "15911110000", "山东省", '青岛市', "市北区", 1)
        self.assertTrue(data['Success'])

    def test_private_eorder(self):
        """
        隐私电子面单
        """
        data = self.kdn.service.private_eorder("SF", "11111", "1", "张三", "18512341234", "18512341234", "北京市", "北京市", "海淀区1号",
                                               "李四", "18511223344", "18612345678", "山东省", "青岛市", "李沧区", service_value=1.22, service_name="TEST", commodity_goods_name="TTT")

        self.assertTrue(data["Success"])


if __name__ == "__main__":
    unittest.main()
