#!/usr/bin/python3
# @Time    : 2020-06-30
# @Author  : Kevin Kong (kfx2007@163.com)

# 在途监控

from .comm import Comm


class Onroad(Comm):

    def get_express_routes(self, order_code, shipper_code, logistic_code,customer_name=None):
        """
        即时查询
        order_code: 订单编号
        shipper_code: 快递公司编码
        logistic_code: 快递单号
        customer_name: 京东、顺丰 必填，京东对应商家编码，顺丰为收件人或发件人手机号后四位
        """

        request_type = 8001

        if not self.sandbox:
            self.url = f"{self.url}/Ebusiness/EbusinessOrderHandle.aspx"

        data = {
            "OrderCode": order_code,
            "ShipperCode": shipper_code,
            "LogisticCode": logistic_code,
            "CustomerName": customer_name
        }

        return self.post(request_type, data)
