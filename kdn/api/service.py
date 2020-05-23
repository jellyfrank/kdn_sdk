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

    def private_eorder(self, shipper_code, order_code, pay_type, receiver_name, receiver_phone,
                       receiver_mobile, receiver_province, receiver_city, receiver_address,
                       sender_name, sender_phone, sender_mobile, sender_province, sender_city, sender_address, exp_type=1,
                       callback=None, member_id=None, customer_name=None, customer_pwd=None, sender_site=None,
                       logistic_code=None, thr_code=None, month_code=None, is_notice=None, cost=None, other_cost=None,
                       receiver_company=None, receiver_post_code=None, receiver_district=None, sender_company=None,
                       sender_post_code=None, sender_district=None, start_date=None, end_date=None, weight=None, quantity=None,
                       volumne=None, remark=None, service_name=None, service_value=None, service_customer_id=None,
                       commodity_goods_name=None, commodity_goods_code=None, commodity_goods_quantity=None, commodity_goods_price=None,
                       commodity_goods_weight=None, commodity_goods_desc=None, commodity_goods_vol=None, is_return_template=0):
        """
        隐私电子面单

        params:
        shipper_code: 快递公司编码
        order_code: 订单编号
        pay_type: 邮费支付方式:1-现付，2-到付，3-月结，4-第三方支付
        receiver_name: 收件人姓名
        receiver_phone: 收件人电话
        receiver_mobile: 收件人手机
        receiver_province: 收件人省份
        receiver_city: 收件人城市
        receiver_address: 收件人地址
        sender_name: 发件人姓名
        sender_phone: 发件人电话
        sender_mobile: 发件人手机
        sender_province: 发件人身份
        sender_city: 发件人城市
        sender_address: 发件人地址
        exp_type: 快递类型：1-标准快件
        callback: 用户自定义回调信息
        member_id: 会员标识
        customer_name: 电子面单客户账号（与快递网点申请
        customer_pwd: 电子面单密码
        sender_site: 收件网点标识
        logistic_code: 快递单号
        thr_code: 第三方订单编号
        month_code: 月结编码
        is_notice: 是否通知快递员上门揽件：0-通知；1-不通知；不填则默认为0
        cost: 寄件费（运费）
        other_cost: 其他费用
        receiver_company: 收件人公司
        receiver_post_code: 收件人邮编
        receiver_district: 收件区（如福田区，不要缺少“区”或“县”）
        sender_company: 发件人公司
        sender_post_code: 发件人邮编
        sender_district: 发件区（如福田区，不要缺少“区”或“县”）
        start_date: 上门取货时间段:"yyyy-MM-dd HH:mm:ss"格式化
        end_date: 上门取货时间段:"yyyy-MM-dd HH:mm:ss"格式化
        weight: 物品总重量kg
        quantity: 件数/包裹数
        volumne: 物品总体积m3
        remark: 备注
        service_name: 增值服务名称
        service_value: 增值服务值
        service_customer_id: 客户标识（选填）
        commodity_goods_name: 商品名称
        commodity_goods_code: 商品编码
        commodity_goods_quantity: 商品数量
        commodity_goods_price: 商品价格
        commodity_goods_weight: 商品重量kg
        commodity_goods_desc: 商品描述
        commodity_goods_vol: 商品体积m3
        is_return_template: 返回电子面单模板：0-不需要；1-需要
        """

        request_type = "1007"

        if not self.sandbox:
            self.url = f"{self.url}/api/EOrderService"

        data = {
            "ShipperCode": shipper_code,
            "OrderCode": order_code,
            "PayType": pay_type,
            "ExpType": exp_type,
            "CallBack": callback,
            "MemberID": member_id,
            "CustomerName": customer_name,
            "CustomerPwd": customer_pwd,
            "SendSite": sender_site,
            "LogisticCode": logistic_code,
            "ThrOrderCode": thr_code,
            "MonthCode": month_code,
            "IsNotice": is_notice,
            "Cost": cost,
            "OtherCost": other_cost,
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
            "StartDate": start_date,
            "EndDate": end_date,
            "Weight": weight,
            "Quantity": quantity,
            "Volume": volumne,
            "Remark": remark,
            "AddService": [{
                "Name": service_name,
                "Value": service_value,
                "CustomerID": service_customer_id
            }],
            "Commodity": [{
                "GoodsName": commodity_goods_name,
                "GoodsCode": commodity_goods_code,
                "Goodsquantity": commodity_goods_quantity,
                "GoodsPrice": commodity_goods_price,
                "GoodsWeight": commodity_goods_weight,
                "GoodsDesc": commodity_goods_desc,
                "GoodsVol": commodity_goods_vol
            }]
        }
        
        return self.post(request_type, data)
