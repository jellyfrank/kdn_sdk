#!/usr/bin/python3
# @Time    : 2021-11-29
# @Author  : Kevin Kong (kfx2007@163.com)

# 物流跟踪 API

from requests.api import get
from .query import Query
# from .comm import Comm
# UPGRADE = {
#     1002: 8001,
# }


# def logistic(func):
#     def wrapper(*args, **kwargs):
#         print(getattr(func,'request_type'))
#         func.request_type = UPGRADE[func.request_type]
#         return func(*args, **kwargs)
#     return wrapper


class Logistic(Query):

    def __init__(self, *args, **kwargs):
        self.express_code = 8001
        self.subsribe_code = 8008

    # def get_express_routes(self, *args, **kwargs):
    #     """
    #     获取即时物流轨迹
    #     params:
    #     shipper_code: 快递公司编码
    #     logistic_code: 快递单号
    #     order_code: 订单编号
    #     customer_name: ShipperCode 为 JD，必填，对应京东的青龙配送编码，也叫商家编码.
    #     """
    #     func = Query.get_express_routes
    #     func.request_type = 8001
    #     return func(self, *args, **kwargs)

    # def subscribe_express_routes(self, *args, **kwargs):
    #     """
    #     轨迹订阅接口
    #     params:
    #     shipper_code: 快递公司编码
    #     logistic_code: 快递单号
    #     recevier_name: 收件人姓名
    #     province_name: 收件人省份
    #     city_name: 收件人城市
    #     district_name: 收件人区域
    #     address: 收件人详细地址
    #     sender_name: 发件人姓名
    #     sender_tel: 发件人电话
    #     sender_mobile: 发件人手机 (电话或手机必填一个)
    #     sender_province: 发件人省份
    #     sender_city:发件人城市
    #     sender_district: 发件人区域
    #     sender_address: 发件人详细地址
    #     recevier_tel: 收件人电话
    #     receiver_mobile: 收件人手机 (电话或手机必填一个)
    #     member_id: ERP 系统、电商平台等系统或平台类型用户的会员ID或店铺账号等唯一性标识，用于区分其用户
    #     warehouse_id: 仓库标志
    #     customer_name: ShipperCode 为 JD，必填，对应京东的青龙配送编码，也叫商家编码
    #     order_code: 订单编号
    #     month_code: 月结单号
    #     pay_type: 运费支付方式：1-现付，2-到付，3-月结，4- 第三方付(仅 SF、KYSY 支持)
    #     exp_type：详细快递类型
    #     cost: 快递运费
    #     other_cost: 其他费用
    #     receiver_company: 收件人公司
    #     receiver_post_code：收件人邮编
    #     sender_company： 发件人公司
    #     sender_post_code： 发件人邮编
    #     is_notice：是否通知快递员上门揽件 0-通知，1-不通知，不填则 默认为 1
    #     start_date: 上门揽件时间段，格式：YYYY-MM-DD HH24:MM:SS
    #     end_date: 上门揽件时间段
    #     weight: 重量
    #     quantity： 包裹数量
    #     volume： 体积
    #     remark: 备注
    #     is_sender_message: 是否订阅短信 0-不需要，1-需要
    #     service_name：增值服务名称
    #     service_value: 增值服务值
    #     service_customer_id: 增值服务客户id
    #     goods_name： 商品名称
    #     goods_code： 商品编码
    #     goods_quantity：商品数量
    #     goods_price： 商品价格
    #     goods_weight：商品重量
    #     goods_desc：商品描述
    #     goods_vol: 商品体积
    #     """
    #     func = Query.subscribe_express_routes
    #     func.request_type = 8008
    #     return func(self, *args, **kwargs)
