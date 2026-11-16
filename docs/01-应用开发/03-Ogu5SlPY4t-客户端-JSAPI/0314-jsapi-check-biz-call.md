---
title: "checkBizCall"
source_url: "https://open.dingtalk.com/document/development/jsapi-check-biz-call"
namespace: "development"
slug: "jsapi-check-biz-call"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "办公电话 > checkBizCall"
doc_id: "NzE4pW2DkG"
updated_at: "2025-08-27 18:08:35"
---

> Source: https://open.dingtalk.com/document/development/jsapi-check-biz-call
> Path: 应用开发 / 客户端 JSAPI / 办公电话 > checkBizCall
> Updated: 2025-08-27 18:08:35

# checkBizCall

调用checkBizCall，检查某企业办公电话开通状态。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10315) |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10315) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `corpId`（string，必填）：被检测企业的corpId。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `isSupport`（boolean，必填）：是否已开通。

## **示例****代码**

### 默认出入参

```
dd.checkBizCall({
  corpId: 'ding1234xxxx',
  success: (res) => {
    const { isSupport } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "isSupport": true }
```
