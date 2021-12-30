#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

# 快递鸟查询类接口

from .comm import Comm

STATES = [
    ('0', "未查询到轨迹"),
    ('1', "已揽收"),
    ('2', "在途中"),
    ('3', "已签收"),
    ('4', "问题件")
]

PAY_TYPES = [
    ('1', "现付"),
    ('2', "到付"),
    ('3', "月结"),
    ('4', "第三方支付")
]


class Query(Comm):

    def __init__(self,*args,**kwargs):
        self.express_code = 1002
        self.subsribe_code = 1008

    def get_express_routes(self, shipper_code, logistic_code, order_code=None, customer_name=None):
        """
        获取即时物流轨迹
        params:
        shipper_code: 快递公司编码
        logistic_code: 快递单号
        order_code: 订单编号
        customer_name: ShipperCode 为 JD，必填，对应京东的青龙配送编码，也叫商家编码.
        """

        if not self.sandbox:
            self.url = f"{self.url}/Ebusiness/EbusinessOrderHandle.aspx"

        data = {
            "OrderCode": order_code,
            "ShipperCode": shipper_code,
            "LogisticCode": logistic_code,
            "CustomerName": customer_name,
        }

        return self.post(self.express_code, data)

    def subscribe_express_routes(self, callback, shipper_code, logistic_code, recevier_name, province_name,
                                 city_name, district_name, address, sender_name,  sender_province, sender_city,
                                 sender_district, sender_address, recevier_tel=None, receiver_mobile=None, sender_tel=None, sender_mobile=None,
                                 member_id=None, warehouse_id=None, customer_name=None, order_code=None, month_code=None,
                                 pay_type=1, exp_type=1, cost=None, other_cost=None, receiver_company=None,
                                 receiver_post_code=None, sender_company=None, sender_post_code=None, is_notice=1, start_date=None,
                                 end_date=None, weight=None, quantity=None, volume=None, remark=None, is_sender_message=None,
                                 service_name=None, service_value=None, service_customer_id=None, goods_name=None, sort=0,
                                 goods_code=None, goods_quantity=None, goods_price=None, goods_weight=None, goods_desc=None,
                                 goods_vol=None):
        """
        轨迹订阅接口
        params:
        shipper_code: 快递公司编码
        logistic_code: 快递单号
        recevier_name: 收件人姓名
        province_name: 收件人省份
        city_name: 收件人城市
        district_name: 收件人区域
        address: 收件人详细地址
        sender_name: 发件人姓名
        sender_tel: 发件人电话
        sender_mobile: 发件人手机 (电话或手机必填一个)
        sender_province: 发件人省份
        sender_city:发件人城市
        sender_district: 发件人区域
        sender_address: 发件人详细地址
        recevier_tel: 收件人电话
        receiver_mobile: 收件人手机 (电话或手机必填一个)
        member_id: ERP 系统、电商平台等系统或平台类型用户的会员ID或店铺账号等唯一性标识，用于区分其用户
        warehouse_id: 仓库标志
        customer_name: ShipperCode 为 JD，必填，对应京东的青龙配送编码，也叫商家编码
        order_code: 订单编号
        month_code: 月结单号
        pay_type: 运费支付方式：1-现付，2-到付，3-月结，4- 第三方付(仅 SF、KYSY 支持)
        exp_type：详细快递类型 
        cost: 快递运费
        other_cost: 其他费用
        receiver_company: 收件人公司
        receiver_post_code：收件人邮编
        sender_company： 发件人公司
        sender_post_code： 发件人邮编
        is_notice：是否通知快递员上门揽件 0-通知，1-不通知，不填则 默认为 1
        start_date: 上门揽件时间段，格式：YYYY-MM-DD HH24:MM:SS
        end_date: 上门揽件时间段
        weight: 重量
        quantity： 包裹数量
        volume： 体积
        remark: 备注
        is_sender_message: 是否订阅短信 0-不需要，1-需要
        service_name：增值服务名称
        service_value: 增值服务值
        service_customer_id: 增值服务客户id
        goods_name： 商品名称
        goods_code： 商品编码
        goods_quantity：商品数量
        goods_price： 商品价格
        goods_weight：商品重量
        goods_desc：商品描述
        goods_vol: 商品体积
        """

        if not self.sandbox:
            self.url = f"{self.url}/api/dist"

        data = {
            "Callback": callback,
            "MemberID": member_id,
            "WareHouseID": warehouse_id,
            "ShipperCode": shipper_code,
            "LogisticCode": logistic_code,
            "CustomerName": customer_name,
            "OrderCode": order_code,
            "MonthCode": month_code,
            "PayType": pay_type,
            "ExpType": exp_type,
            "Cost": cost,
            "OtherCost": other_cost,
            "Receiver": {
                "Company": receiver_company,
                "Name": recevier_name,
                "Tel": recevier_tel,
                "Mobile": receiver_mobile,
                "PostCode": receiver_post_code,
                "ProvinceName": province_name,
                "CityName": city_name,
                "ExpAreaName": district_name,
                "Address": address,
            },
            "Sender": {
                "Company": sender_company,
                "Name": sender_name,
                "Tel": sender_tel,
                "Mobile": sender_mobile,
                "PostCode": sender_post_code,
                "ProvinceName": sender_province,
                "CityName": sender_city,
                "ExpAreaName": sender_district,
                "Address": sender_address,
            },
            "IsNotice": is_notice,
            "StartDate": start_date,
            "EndDate": end_date,
            "Weight": weight,
            "Quantity": quantity,
            "Volume": volume,
            "Remark": remark,
            "IsSendMessage": is_sender_message,
            "AddService.Name": service_name,
            "AddService.Value": service_value,
            "AddService.CustomerID": service_customer_id,
            "Commodity.GoodsName": goods_name,
            "Commodity.GoodsCode": goods_code,
            "Commodity.Goodsquantity": quantity,
            "Commodity.GoodsPrice": goods_price,
            "Commodity.GoodsWeight": goods_weight,
            "Commodity.GoodsDesc": goods_desc,
            "Commodity.GoodsVol": goods_vol
        }

        return self.post(self.subsribe_code, data)
