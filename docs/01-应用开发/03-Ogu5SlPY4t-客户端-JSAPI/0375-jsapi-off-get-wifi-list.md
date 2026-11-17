---
title: "offGetWifiList"
source_url: "https://open.dingtalk.com/document/development/jsapi-off-get-wifi-list"
namespace: "development"
slug: "jsapi-off-get-wifi-list"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > Wi-Fi > offGetWifiList"
doc_id: "agcp1PDXVZ"
updated_at: "2025-08-27 18:07:38"
---

> Source: https://open.dingtalk.com/document/development/jsapi-off-get-wifi-list
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > Wi-Fi > offGetWifiList
> Updated: 2025-08-27 18:07:38

# offGetWifiList

停止监听已获取 Wi-Fi 列表数据事件。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11477) |

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

### 入参

（object）回调事件内的对象

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.offGetWifiList();
```

`success`返回对象示例：

```
{}
```
