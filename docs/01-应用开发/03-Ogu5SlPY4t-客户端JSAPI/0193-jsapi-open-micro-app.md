---
title: "openMicroApp"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-micro-app"
namespace: "development"
slug: "jsapi-open-micro-app"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 跳转 > openMicroApp"
doc_id: "0VcIfda6NO"
updated_at: "2025-08-27 18:06:29"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-micro-app
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 跳转 > openMicroApp
> Updated: 2025-08-27 18:06:29

# openMicroApp

调用openMicroApp，打开应用。

在企业自建工作主页中添加钉钉原生微应用（如审批、日志等）或已上架的第三方微应用，可使用该JSAPI打开应用

---

开发者有两种方式来打开应用：

- 通过agentId打开应用。
- 通过appId和corpId打开应用。

---

如果提供了正确的agentId，系统将直接根据agentId打开应用，不会再使用appId和corpId参数。

如果使用agentId无法打开应用，系统将根据appId和corpId来打开应用，否则返回错误。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11692) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `agentId`（string）：要打开应用的agentId，第三方企业应用需要
- `appId`（string）：要打开应用的appId，可以在开发者后台应用详情页获取
- `corpId`（string）：要打开的应用所属的corpId

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.openMicroApp({
  agentId: '2612559674',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
