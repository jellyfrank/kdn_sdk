#!/usr/bin/python3
# @Time    : 2020-05-11
# @Author  : Kevin Kong (kfx2007@163.com)

# 增值类接口API

from .comm import Comm


class Service(Comm):

    def recognize_logistic_code(self, code):
        """
        params:
        code: 必填，物流单号
        return:
        包含物流公司的json
        {
            "EBusinessID": "1257021",
            "Success": true,
            "LogisticCode": "3967950525457",
            "Shippers": [
                    {
                        "ShipperCode": "YD",
                        "ShipperName": "韵达快递"
                    }
                    ]
        }
        """
        request_type = "2002"
        if not self.sandbox:
            self.url = f"{self.url}/Ebusiness/EbusinessOrderHandle.aspx"

        data = {
            "LogisticCode": code
        }

        return self.post(request_type, data)
