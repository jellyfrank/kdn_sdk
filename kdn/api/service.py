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

    def safe_phone(self, order_no, shipper_code, logistic_code, receiver_name,
                   receiver_phone, receiver_mobile, receiver_province, receiver_city, receiver_address,
                   sender_name, sender_phone, sender_mobile, sender_province, sender_city, sender_address,
                   hide_type, receiver_company=None, receiver_post_code=None, receiver_district=None, sender_company=None,
                   sender_post_code=None, sender_district=None):
        """
        安全号码
        params:
        order_no: 订单编号
        shipper_code: 快递公司编码
        logistic_code: 	快递单号
        receiver_name: 收件人
        receiver_phone: 电话与手机
        receiver_mobile: 
        receiver_province: 收件人省份
        receiver_city: 收件人城市
        receiver_address: 收件人地址
        sender_name: 发件人
        sender_phone: 发件人电话
        sender_mobile: 发件人手机
        sender_province: 发件人省份
        sender_city: 发件人城市
        sender_address: 发件人地址
        hide_type: 安全号生成规则（1，隐藏收件人信息，2.隐身发件人信息，3.同时隐藏收件人，发件人信息)
        receiver_company: 收件人公司
        receiver_post_code: 收件人邮编
        receiver_district: 收件人区域
        sender_company: 发件人公司
        sender_post_code: 发件人邮编
        sender_district: 发件人区域
        """

        request_type = "3001"
        if not self.sandbox:
            self.url = f"{self.url}/api/apiservice"

        data = {
            "OrderCode": order_no,
            "ShipperCode": shipper_code,
            "LogisticCode": logistic_code,
            "Receiver": {
                "Company": receiver_company,
                "Name": receiver_name,
                "Tel": receiver_phone,
                "Mobile": receiver_mobile,
                "PostCode": receiver_post_code,
                "ProvinceName": receiver_province,
                "CityName": receiver_city,
                "ExpAreaName": receiver_district,
                "Address": receiver_address
            },
            "Sender": {
                "Company": sender_company,
                "Name": sender_name,
                "Tel": sender_phone,
                "Mobile": sender_mobile,
                "PostCode": sender_post_code,
                "ProvinceName": sender_province,
                "CityName": sender_city,
                "ExpAreaName": sender_district,
                "Address": sender_address
            },
            "HideType": hide_type
        }

        return self.post(request_type, data)
