# 快递鸟 Python SDK

## requirements

python >= 3.6

基于快递鸟v5.22开发

## 已实现接口列表

### 下单类(Order)

* 上门取件 order

### 查询类（Query)

* 获取即时物流轨迹 get_express_routes
* 接口订阅轨迹 subscribe_express_routes
  
更多功能持续更新中...

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

