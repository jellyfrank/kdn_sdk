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
        print(data)
        self.assertTrue(data['Success'])


if __name__ == "__main__":
    unittest.main()
