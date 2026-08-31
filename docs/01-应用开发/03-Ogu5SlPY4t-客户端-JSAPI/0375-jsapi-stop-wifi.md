---
title: "stopWifi"
source_url: "https://open.dingtalk.com/document/development/jsapi-stop-wifi"
namespace: "development"
slug: "jsapi-stop-wifi"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > Wi-Fi > stopWifi"
doc_id: "yWymIyYAD5"
updated_at: "2025-08-27 18:07:40"
---

> Source: https://open.dingtalk.com/document/development/jsapi-stop-wifi
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > Wi-Fi > stopWifi
> Updated: 2025-08-27 18:07:40

# stopWifi

关闭 Wi-Fi 模块。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11470) |

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

（object）

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
const res = dd.stopWifi();
const {} = res;
```

返回对象示例：

```
{}
```
