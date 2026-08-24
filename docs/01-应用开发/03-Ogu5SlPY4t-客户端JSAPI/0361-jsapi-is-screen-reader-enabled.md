---
title: "isScreenReaderEnabled"
source_url: "https://open.dingtalk.com/document/development/jsapi-is-screen-reader-enabled"
namespace: "development"
slug: "jsapi-is-screen-reader-enabled"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 系统信息 > isScreenReaderEnabled"
doc_id: "5sRHpjCBdT"
updated_at: "2025-08-27 18:07:31"
---

> Source: https://open.dingtalk.com/document/development/jsapi-is-screen-reader-enabled
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 系统信息 > isScreenReaderEnabled
> Updated: 2025-08-27 18:07:31

# isScreenReaderEnabled

调用isScreenReaderEnabled，判断是否开启无障碍模式。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.5.60 | 6.5.60 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11627) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11627) |

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

- `screenReaderEnabled`（boolean，必填）：是否开启无障碍模式。

## **示例****代码**

### 默认出入参

```
dd.isScreenReaderEnabled({
  success: (res) => {
    const { screenReaderEnabled } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "screenReaderEnabled": true }
```
