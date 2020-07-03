#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from kdn.api.kdn import KDN
import json


class TestComm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client_id = "test1624824"
        cls.api_key = "f6bc7c23-7d7c-4dc8-9a73-506519393f6a"
        cls.kdn = KDN(cls.client_id, cls.api_key)

    def test_sign(self):
        """
        测试签名
        """
        data = {"OrderCode": "111", "ShipperCode": "SF",
                "LogisticCode": "1234561", "IsHandleInfo": "0"}
        data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        sign = self.kdn.comm._sign(data)

        self.assertEqual(
            sign, "ZTc1MjdjN2Y1YmVlMjJmOWY4N2E0ZGI2YmZhNzIzZmI=", sign)

    def test_read_list(self):
        res = self.kdn.get_express_list()
        self.assertTrue(len(res))

    def test_eorder_list(self):
        res = self.kdn.get_eorder_express()
        self.assertTrue(len(res))

    def test_templates(self):
        res = self.kdn.get_templates()
        self.assertTrue(len(res))

    def test_exp_types(self):
        res = self.kdn.get_express_types()
        print('-------')
        print(res)
        # self.assertTrue()


if __name__ == "__main__":
    unittest.main()
