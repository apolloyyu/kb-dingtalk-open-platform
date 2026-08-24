---
title: "getNetworkType"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-network-type"
namespace: "development"
slug: "jsapi-get-network-type"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 网络状态 > getNetworkType"
doc_id: "eCpl8Y9dVK"
updated_at: "2025-08-27 18:07:33"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-network-type
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 网络状态 > getNetworkType
> Updated: 2025-08-27 18:07:33

# getNetworkType

调用getNetworkType，获取当前网络状态。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10142) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10142) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `key`（string，必填）：缓存数据的key。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `networkAvailable`（boolean）：网络是否可用。
- `networkType`（string）：网络类型值，\*\*UNKNOWN / NOTREACHABLE / WIFI / 3G / 2G / 4G / WWAN\*\*。  
    
  > 桌面端不支持该字。

## **示例****代码**

### 默认出入参

```
dd.getNetworkType({
  key: 'key1',
  success: (res) => {
    const { networkType, networkAvailable } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "networkType": "WIFI", "networkAvailable": true }
```
