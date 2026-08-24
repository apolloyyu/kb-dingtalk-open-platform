---
title: "registerSSID"
source_url: "https://open.dingtalk.com/document/development/jsapi-register-ssid"
namespace: "development"
slug: "jsapi-register-ssid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > Wi-Fi > registerSSID"
doc_id: "zO7h2CbSsZ"
updated_at: "2025-08-27 18:07:39"
---

> Source: https://open.dingtalk.com/document/development/jsapi-register-ssid
> Path: 应用开发 / 客户端JSAPI / 设备能力 > Wi-Fi > registerSSID
> Updated: 2025-08-27 18:07:39

# registerSSID

信任该 SSID(iOS)

信任该 SSID，对于需要 Portal 认证的 Wi-Fi，不会弹出 Portal 认证页面。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 不支持 | 7.0.10 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11478) |

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

- `SSID`（string，必填）：设备 SSID。

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
dd.registerSSID({
  SSID: 'dingtalk',
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{}
```
