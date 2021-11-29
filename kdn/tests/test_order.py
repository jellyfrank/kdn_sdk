#!/usr/bin/python3
# @Time    : 2020-03-26
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from kdn.api.kdn import KDN


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client_id = "test1624824"
        cls.api_key = "f6bc7c23-7d7c-4dc8-9a73-506519393f6a"
        cls.kdn = KDN(cls.client_id, cls.api_key, sandbox=True)

    def test_order(self):
        res = self.kdn.order.order("1234561", "SF", 1, "张三", "0755-0907283",
                                   "13709076789", "广东省", "深圳市", "深南大道2009号", "李四", "0755-1111111",
                                   "13932080778", "广东省", "深圳市", "福田保税区", "书本", "9999999", "深圳市福田区福田保税区", start_date="2022-05-16 09:00:00",
                                   end_date="2022-05-16 12:00:00", service_value=1000, service_name="INSURE")
        self.assertTrue(res['Success'], msg=res)

    def test_eorder(self):
        res = self.kdn.order.eorder(
            "STO", "126546", 1, 1, "张三", "18512345678", "18512345678", "广东省", "深圳市", "福田区", "腾讯大厦", "希格格", "18511112222", "18522223333",
            "北京市", "北京市", "朝阳区", "三里屯soho", 1, "TNT", customer_name="11111", customer_pwd="2222", send_site="1001")
        self.assertTrue(res['Success'], msg=res)

    def test_eorder_error(self):
        res = self.kdn.order.eorder(
            "CG", "126546", 1, 1, "张三", "18512345678", "18512345678", "广东省", "深圳市", "福田区", "腾讯大厦", "希格格", "18511112222", "18522223333",
            "北京市", "北京市", "朝阳区", "三里屯soho", 1, "TNT")
        self.assertFalse(res['Success'], msg=res)

    def test_preoder(self):
        res = self.kdn.order.preorder("1234561", "ZTO", 1, "张三", "0755-0907283",
                                      "13709076789", "广东省", "深圳市", "深南大道2009号", "李四", "0755-1111111",
                                      "13932080778", "广东省", "深圳市", "福田保税区", "书本", "9999999", "深圳市福田区福田保税区",
                                      start_date="2090-06-15 12:00:00", receiver_district="福田区", sender_district="福田区",service_value=1000, service_name="INSURE",service_customer_id="1111112222")
        self.assertTrue(res['Success'], msg=res)


if __name__ == "__main__":
    unittest.main()
