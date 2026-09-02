---
title: "openLink"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-link"
namespace: "development"
slug: "jsapi-open-link"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 跳转 > openLink"
doc_id: "kWje2uGErw"
updated_at: "2025-08-27 18:06:29"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-link
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 跳转 > openLink
> Updated: 2025-08-27 18:06:29

# openLink

调用openLink打开目标页面。

- PC端调用时，调用此接口跳转到外部浏览器打开目标页面，若开启【工作台应用内所有页面都在钉钉内打开】开关，则目标页面在端内工作台打开
- 开关设置入口示意图：![示意图](https://img.alicdn.com/imgextra/i2/O1CN01U005Cv1y9Xg6L8w8n_!!6000000006536-0-tps-1336-1116.jpg)
- 手机端调用时，调用此接口由钉钉客户端内置浏览器打开目标页面。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11711) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11711) |

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

- `url`（string，必填）：要打开链接的地址。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.openLink({
  url: 'https://www.dingtalk.com',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
