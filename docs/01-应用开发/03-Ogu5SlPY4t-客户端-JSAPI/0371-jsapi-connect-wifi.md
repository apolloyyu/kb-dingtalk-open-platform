---
title: "connectWifi"
source_url: "https://open.dingtalk.com/document/development/jsapi-connect-wifi"
namespace: "development"
slug: "jsapi-connect-wifi"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > Wi-Fi > connectWifi"
doc_id: "CZYs3CQnhs"
updated_at: "2025-08-27 18:07:35"
---

> Source: https://open.dingtalk.com/document/development/jsapi-connect-wifi
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > Wi-Fi > connectWifi
> Updated: 2025-08-27 18:07:35

# connectWifi

连接 Wi-Fi 。

> 若已知 Wi-Fi 信息，可以直接利用该接口连接。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11471) |

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

- `SSID`（string，必填）：Wi-Fi 设备 SSID。
- `isWEP`（boolean，必填）：Wi-Fi 是否为 WEP。  
    
  > 默认是 false。
- `password`（string，必填）：Wi-Fi 设备密码。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.connectWifi({
  SSID: 'dingtalk',
  isWEP: false,
  password: '12345678',
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
