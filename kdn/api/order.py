#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

# 快递鸟 下单类接口

from .comm import Comm


class Order(Comm):

    def order(self, order_code, pay_type, receiver_name, receiver_tel, receiver_mobile,
              province, city, address, sender_name, sender_tel, sender_mobile, sender_province, sender_city,
              sender_address, goods_name, warehouse_id=None, warehouse_address=None, callback=None, member_id=None,
              month_code=None, is_return_sign_bill=0, receiver_company=None, receiver_post_code=None, receiver_district=None,
              exp_type=1, sender_company=None, sender_post_code=None, sender_district=None,
              sender_show_address=None, start_date=None, end_date=None, weight=None, quantity=None, volume=None, remark=None,
              service_name=None, service_value=None, service_customer_id=None,
              goods_code=None, goods_quantity=None, goods_price=None, goods_weight=None, goods_desc=None,
              goods_vol=None, picking_type=None, delivery_mode=None):
        """
        上门取件
        order_code: 订单编号	
        pay_type： 邮费支付方式:1-现付，2-到付，3-月结，4-第三方支付
        receiver_name: 收件人
        receiver_tel：收件人电话
        receiver_mobile: 收件人手机
        province: 收件省（如广东省，不要缺少“省”）
        city：收件市（如深圳市，不要缺少“市”）
        address： 收件人详细地址
        sender_name：发件人
        sender_tel: 发件人电话
        sender_mobile: 发件人手机
        sender_province：发件人省份
        sender_city：发件人城市
        sender_address： 发件人地址
        goods_name： 商品名称

        warehouse_id: 仓库标识
        warehouse_address： 仓库地址
        callback: 商户标识
        member_id: 会员标识
        month_code: 月结编码
        receiver_company: 收件人公司
        receiver_post_code： 收件人邮编
        receiver_district： 收件人县区
        sender_company: 发件人公司
        sender_post_code: 发件人邮编
        sender_district: 发件人县区
        sender_show_address: 发件人详细地址
        start_date: 上门取货时间段:"yyyy-MM-dd
        end_date: 上门取货时间段:"yyyy-MM-dd HH:mm:ss"格式化
        weight: 物品总重量kg
        quantity: 件数/包裹数
        volume: 物品总体积m3
        remark: 备注
        service_name: 增值服务名称
        service_value: 增值服务值
        service_customer_id: 客户标识（选填）
        goods_code: 商品编码
        goods_quantity: 商品数量
        goods_price: 商品价格
        goods_weight: 商品重量
        goods_desc: 商品描述
        goods_vol: 商品体积m3
        picking_type: 包装类型：包装类型(快运字段)默认为 0； 0- 纸 1- 纤 2- 木 3- 托膜 4- 木托 99-其他
        delivery_mode: 送货方式：0-自提，1-送货上门（不含上楼）2-送货上楼。（适用于快运类型订单，物流公司可能会收取费用），默认为0
        is_return_sign_bill: 签单回收
        exp_type: 快递类型：1-标准快件
        """
