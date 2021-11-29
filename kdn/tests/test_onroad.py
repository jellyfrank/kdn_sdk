#!/usr/bin/python3
# @Time    : 2020-06-30
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from kdn.api.kdn import KDN

class TestOnroad(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client_id = "test1624824"
        cls.api_key = "f6bc7c23-7d7c-4dc8-9a73-506519393f6a"
        cls.kdn = KDN(cls.client_id, cls.api_key, sandbox=True)

    def test_get_express_routes(self):
        #[HACK] 快递鸟沙箱环境不支持 在途监控
        res = self.kdn.logistic.get_express_routes("1234561", "SF", "111")
        self.assertTrue(res["Success"],res)


if __name__ == "__main__":
    unittest.main()
