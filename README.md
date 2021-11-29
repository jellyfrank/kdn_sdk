[![Actions Status](https://github.com/block-cat/kdn_sdk/workflows/KDN%20SDK/badge.svg)](https://github.com/block-cat/kdn_sdk/actions)

# 快递鸟 Python SDK

## requirements

python >= 3.6

基于快递鸟v5.41开发

## 已实现接口列表

### 下单类(Order)

* 上门取件 order
* 预约取件 preorder
* 电子面单 eorder

### 查询类（Query)

* 获取即时物流轨迹 get_express_routes
* 接口订阅轨迹 subscribe_express_routes

### 增值接口类 (Service)

* 单号识别 recognize_logistic_code

## 安装

```
pip install kdn
```

## 使用

```python
from kdn.api.kdn import KDN

kdn = KDN(client_id, api_key)
kdn.query.get_express_routes("SF", "1234561", "111")

```

