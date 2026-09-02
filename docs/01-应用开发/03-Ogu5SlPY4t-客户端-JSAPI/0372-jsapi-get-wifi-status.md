---
title: "getWifiStatus"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-wifi-status"
namespace: "development"
slug: "jsapi-get-wifi-status"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > Wi-Fi > getWifiStatus"
doc_id: "AQ2XBCkKkW"
updated_at: "2025-08-27 18:07:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-wifi-status
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > Wi-Fi > getWifiStatus
> Updated: 2025-08-27 18:07:36

# getWifiStatus

调用getWifiStatus，获取wifi状态。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11666) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11666) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `status`（number，必填）：当前连接wifi的状态：  
    
  \* 1：已连接wifi  
  \* 0：未连接wifi

## **示例****代码**

### 默认出入参

```
dd.getWifiStatus({
  success: (res) => {
    const { status } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "status": 1 }
```
