#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

# 快递鸟 下单类接口

from .comm import Comm


class Order(Comm):

    def order(self, order_code, shipper_code, pay_type, receiver_name, receiver_tel, receiver_mobile,
              province, city, address, sender_name, sender_tel, sender_mobile, sender_province, sender_city,
              sender_address, goods_name, warehouse_id=None, warehouse_address=None, callback=None, member_id=None,
              month_code=None, is_return_sign_bill=0, receiver_company=None, receiver_post_code=None, receiver_district=None,
              exp_type=1, sender_company=None, sender_post_code=None, sender_district=None,
              sender_show_address=None, start_date=None, end_date=None, weight=None, quantity=None, volume=None, remark=None,
              service_name=None, service_value=None, service_customer_id=None,
              goods_code=None, goods_quantity=None, goods_price=None, goods_weight=None, goods_desc=None,
              goods_vol=None, picking_type=None, delivery_method=None):
        """
        上门取件
        order_code: 订单编号	
        shipper_code: 快递公司编码
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
        delivery_method: 送货方式：0-自提，1-送货上门（不含上楼）2-送货上楼。（适用于快运类型订单，物流公司可能会收取费用），默认为0
        is_return_sign_bill: 签单回收
        exp_type: 快递类型：1-标准快件
        """

        request_type = "1801"
        if not self.sandbox:
            self.url = f"{self.url}/api/OOrderService"

        data = {
            "WarehouseID": warehouse_id,
            "WarehouseAddress": warehouse_address,
            "CallBack": callback,
            "MemberID": member_id,
            "OrderCode": order_code,
            "ShipperCode": shipper_code,
            "PayType": pay_type,
            "MonthCode": month_code,
            "ExpType": exp_type,
            "IsReturnSignBill": is_return_sign_bill,
            "Receiver": {
                "Company": receiver_company,
                "Name": receiver_name,
                "Tel": receiver_tel,
                "Mobile": receiver_mobile,
                "PostCode": receiver_post_code,
                "ProvinceName": province,
                "CityName": city,
                "ExpAreaName": receiver_district,
                "Address": address
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
                "Address": sender_address
            },
            "SenderShowAddress": sender_show_address,
            "StartDate": start_date,
            "EndDate": end_date,
            "Weight": weight,
            "Quantity": quantity,
            "Volume": volume,
            "Remark": remark,
            "AddService": [{
                "Name": service_name,
                "Value": service_value,
                "CustomerID": service_customer_id
            }],
            "Commodity": [{
                "GoodsName": goods_name,
                "GoodsCode": goods_code,
                "Goodsquantity": goods_quantity,
                "GoodsPrice": goods_price,
                "GoodsWeight": goods_weight,
                "GoodsDesc": goods_desc,
                "GoodsVol": goods_vol
            }],
            "PackingType": picking_type,
            "DeliveryMethod": delivery_method
        }

        return self.post(request_type, data)

    def eorder(self, shipper_code, order_code, pay_type, exp_type,
               receiver_name, receiver_tel, receiver_mobile, receiver_province, receiver_city,
               receiver_district, receiver_address, sender_name, sender_tel, sender_mobile,
               sender_province, sender_city, sender_district, sender_address,
               quantity, goods_name, member_id=None, customer_name=None, customer_pwd=None,
               send_site=None, send_staff=None, month_code=None, custom_area=None, warehouse_id=None, trans_type=1,
               logistic_code=None, thd_order_code=None, return_sign=0,
               operate_requrie=None, cost=None, other_cost=None,
               receiver_company=None, receiver_post_code=None, sender_company=None, sender_post_code=None,
               is_notice=1, start_date=None, end_date=None, weight=None, volume=None, remark=None,
               add_name=None, add_value=None, add_customer_id=None,
               commodity_goods_code=None, commodity_goods_quantity=None, commodity_goods_price=None,
               commodity_goods_weight=None, commodity_goods_desc=None, commodity_goods_vol=None,
               return_template=None, send_message=None, template_size=None, packing_type=0, delivery_method=0):
        """
        电子面单接口
        params:
        shipper_code: 快递公司编码
        order_code: 订单编号
        pay_type: 邮费支付方式(1 现付,2 到付,3 月结,4 三方支付，仅顺丰)
        exp_type: 快递类型 (1 标快)
        receiver_name: 收件人名称
        receiver_tel： 收件人电话
        receiver_mobile： 收件人手机
        receiver_province： 收件人省份
        receiver_city： 收件人城市
        receiver_district: 收件人县区
        receiver_address: 收件人地址
        sender_name: 发件人姓名
        sender_tel: 发件人电话
        sender_mobile: 发件人手机
        sender_province: 发件人省份
        sender_city: 发件人城市
        sender_district: 发件人县区
        sender_address: 发件人地址
        quantity: 包裹数 最多30
        googds_name: 商品名称
        member_id: 会员ID或账号唯一标识
        customer_name: 电子面单参数
        customer_pwd: 电子面单密码
        send_site: 发送站点
        send_staff: 发送人
        month_code: 月结账号
        custom_area: 商家自定义区域
        warehouse_id: 发货仓编码
        trans_type: 运输方式 (1 陆运 2 空运)
        logistic_code: 快递单号(仅宅急送)
        thd_order_code: 第三方订单号(京东快递必填)
        return_sign: 是否要求回单 (1 要求 0 不要求)
        operate_requrie: 签回单操作要求(如：签名、盖章、身份证复印件等)
        cost： 快递运费
        other_cost： 其他费用
        receiver_company: 收件人公司
        receiver_post_code： 收件人邮编
        sender_company: 发件人公司
        sender_post_code： 发件人邮编
        is_notice: 是否通知快递员上门揽件 0- 通知 1- 不通知 不填则默认为1
        start_date： 上门取货时间段:"yyyy-MM-dd HH:mm:ss"格式化
        end_date：上门取货时间段
        weight： 包裹总重量kg 当为快运的订单时必填，不填时快递鸟将根据各个快运公司要求传对应的默认值
        volume： 包裹总体积m3 当为快运的订单时必填，不填时快递鸟将根据各个快运公司要求传对应的默认值
        remark： 备注
        add_name: 增值服务名称
        add_value: 增值服务值
        add_customer_id: 客户标识（选填）
        commodity_goods_code: 商品编码
        commodity_goods_quantity：商品数量
        commodity_goods_price： 商品价格
        commodity_goods_weight：商品重量kg
        commodity_goods_desc：商品描述
        commodity_goods_vol： 商品体积m3
        return_template: 返回电子面单模板：0-不需要；1-需要
        send_message: 是否订阅短信：0-不需要；1-需要
        template_size: 模板规格(默认的模板无需传值，非默认模板传对应模板尺寸)
        packing_type: 包装类型(快运字段)默认为0； 0- 纸 1- 纤 2- 木 3- 托膜 4- 木托 99-其他
        delivery_method: 送货方式(快运字段)默认为0； 0- 自提 1- 送货上门（不含上楼） 2- 送货上楼
        """

        request_type = "1007"
        if not self.sandbox:
            self.url = f"{self.url}/api/EOrderService"
        data = {
            "MemberID": member_id,
            "CustomerName": customer_name,
            "CustomerPwd": customer_pwd,
            "SendSite": send_site,
            "SendStaff": send_staff,
            "MonthCode": month_code,
            "CustomArea": custom_area,
            "WareHouseID": warehouse_id,
            "TransType": trans_type,
            "ShipperCode": shipper_code,
            "LogisticCode": logistic_code,
            "ThrOrderCode": thd_order_code,
            "OrderCode": order_code,
            "PayType": pay_type,
            "ExpType": exp_type,
            "IsReturnSignBill": return_sign,
            "OperateRequire": operate_requrie,
            "Cost": cost,
            "OtherCost": other_cost,
            "Receiver": {
                "Company": receiver_company,
                "Name": receiver_name,
                "Tel": receiver_tel,
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
                "Tel": sender_tel,
                "Mobile": sender_mobile,
                "PostCode": sender_post_code,
                "ProvinceName": sender_province,
                "CityName": sender_city,
                "ExpAreaName": sender_district,
                "Address": sender_address
            },
            "IsNotice": is_notice,
            "StartDate": start_date,
            "EndDate": end_date,
            "Weight": weight,
            "Quantity": quantity,
            "Volume": volume,
            "Remark": remark,
            "AddService": {
                "Name": add_name,
                "Value": add_value,
                "CustomerID": add_customer_id
            },
            "Commodity": [{
                "GoodsName": goods_name,
                "GoodsCode": commodity_goods_code,
                "Goodsquantity": commodity_goods_quantity,
                "GoodsPrice": commodity_goods_price,
                "GoodsWeight": commodity_goods_weight,
                "GoodsDesc": commodity_goods_desc,
                "GoodsVol": commodity_goods_vol
            }],
            "IsReturnPrintTemplate": return_template,
            "IsSendMessage": send_message,
            "TemplateSize": template_size,
            "PackingType": packing_type,
            "DeliveryMethod": delivery_method
        }

        return self.post(request_type, data)

    def preorder(self, order_code, shipper_code, pay_type, receiver_name, receiver_tel, receiver_mobile,
                 province, city, address, sender_name, sender_tel, sender_mobile, sender_province, sender_city,
                 sender_address, goods_name, warehouse_id=None, warehouse_address=None, callback=None, member_id=None,
                 month_code=None, is_return_sign_bill=0, receiver_company=None, receiver_post_code=None, receiver_district=None,
                 exp_type=1, sender_company=None, sender_post_code=None, sender_district=None,
                 sender_show_address=None, start_date=None, end_date=None, weight=None, quantity=None, volume=None, remark=None,
                 service_name=None, service_value=None, service_customer_id=None,
                 goods_code=None, goods_quantity=None, goods_price=None, goods_weight=None, goods_desc=None,
                 goods_vol=None, picking_type=None, delivery_method=None):
        """
        预约取件
        order_code: 订单编号	
        shipper_code: 快递公司编码
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
        delivery_method: 送货方式：0-自提，1-送货上门（不含上楼）2-送货上楼。（适用于快运类型订单，物流公司可能会收取费用），默认为0
        is_return_sign_bill: 签单回收
        exp_type: 快递类型：1-标准快件
        """

        request_type = "1001"
        if not self.sandbox:
            self.url = f"{self.url}/api/OOrderService"

        data = {
            "WarehouseID": warehouse_id,
            "WarehouseAddress": warehouse_address,
            "CallBack": callback,
            "MemberID": member_id,
            "OrderCode": order_code,
            "ShipperCode": shipper_code,
            "PayType": pay_type,
            "MonthCode": month_code,
            "ExpType": exp_type,
            "IsReturnSignBill": is_return_sign_bill,
            "Receiver": {
                "Company": receiver_company,
                "Name": receiver_name,
                "Tel": receiver_tel,
                "Mobile": receiver_mobile,
                "PostCode": receiver_post_code,
                "ProvinceName": province,
                "CityName": city,
                "ExpAreaName": receiver_district,
                "Address": address
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
                "Address": sender_address
            },
            "SenderShowAddress": sender_show_address,
            "StartDate": start_date,
            "EndDate": end_date,
            "Weight": weight,
            "Quantity": quantity,
            "Volume": volume,
            "Remark": remark,
            "AddService": [{
                "Name": service_name,
                "Value": service_value,
                "CustomerID": service_customer_id
            }],
            "Commodity": [{
                "GoodsName": goods_name,
                "GoodsCode": goods_code,
                "Goodsquantity": goods_quantity,
                "GoodsPrice": goods_price,
                "GoodsWeight": goods_weight,
                "GoodsDesc": goods_desc,
                "GoodsVol": goods_vol
            }],
            "PackingType": picking_type,
            "DeliveryMethod": delivery_method
        }

        return self.post(request_type, data)
