#!/usr/bin/python3
# @Time    : 2020-06-30
# @Author  : Kevin Kong (kfx2007@163.com)

# 在途监控

from .comm import Comm


class Onroad(Comm):

    def get_express_routes(self, order_code, shipper_code, logistic_code):
        """
        即时查询
        order_code: 订单编号
        shipper_code: 快递公司编码
        logistic_code: 快递单号
        """

        request_type = 8001

        if not self.sandbox:
            self.url = f"{self.url}/Ebusiness/EbusinessOrderHandle.aspx"

        data = {
            "OrderCode": order_code,
            "ShipperCode": shipper_code,
            "LogisticCode": logistic_code
        }

        return self.post(request_type, data)
