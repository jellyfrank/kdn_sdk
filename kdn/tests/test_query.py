#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from kdn.api.kdn import KDN
import json


class TestQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client_id = "test1624824"
        cls.api_key = "f6bc7c23-7d7c-4dc8-9a73-506519393f6a"
        cls.kdn = KDN(cls.client_id, cls.api_key, sandbox=True)

    def test_get_express_routes(self):
        res = self.kdn.query.get_express_routes("SF", "1234561", "111")
        self.assertTrue(res["Success"], res)

    def test_subscribe_route(self):
        res = self.kdn.query.subscribe_express_routes(
            "ZTO", "1234561", "测试", "广东省", "深圳市", "福田区", "腾讯大厦", "赵敏", "北京市", "北京市", "朝阳区", "三里屯SOHO", "18512345678", None, "18511112222", None)
        self.assertTrue(res["Success"], res)


if __name__ == "__main__":
    unittest.main()
