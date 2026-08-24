---
title: "getBatteryInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-battery-info"
namespace: "development"
slug: "jsapi-get-battery-info"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 设备电量 > getBatteryInfo"
doc_id: "Xt5RB5ZWmC"
updated_at: "2025-08-27 18:08:09"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-battery-info
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 设备电量 > getBatteryInfo
> Updated: 2025-08-27 18:08:09

# getBatteryInfo

调用getBatteryInfo，获取设备电量。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.5.60 | 6.5.60 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11625) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11625) |

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

- `level` （number，必填）：当前设备电量[0,100]。
- `isCharging`（boolean，必填）：当前设备是否充电中。

## **示例****代码**

### 默认出入参

```
dd.getBatteryInfo({
  success: (res) => {
    const { level, isCharging } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "level": 8, "isCharging": true }
```
