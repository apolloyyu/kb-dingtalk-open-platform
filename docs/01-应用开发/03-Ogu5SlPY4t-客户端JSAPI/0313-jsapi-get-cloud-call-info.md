---
title: "getCloudCallInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-cloud-call-info"
namespace: "development"
slug: "jsapi-get-cloud-call-info"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "办公电话 > getCloudCallInfo"
doc_id: "YLMYW51llU"
updated_at: "2025-08-27 18:08:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-cloud-call-info
> Path: 应用开发 / 客户端JSAPI / 办公电话 > getCloudCallInfo
> Updated: 2025-08-27 18:08:36

# getCloudCallInfo

调用getCloudCallInfo，查询企业是否已开办公电话。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11650) |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11650) |

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

- `corpId`（string，必填）：当前企业的corpId。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `code`（number，必填）：返回码，200表示正常。
- `bizNumberList`（array，必填）：开户的电话号码。
- `cause`（string，必填）：异常描述。
- `hasOpen`（boolean，必填）：是否开户。

## **示例****代码**

### 默认出入参

```
dd.getCloudCallInfo({
  corpId: 'ding1234',
  success: (res) => {
    const { code, cause, hasOpen, bizNumberList } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "code": 200,
  "cause": "内部异常",
  "hasOpen": true,
  "bizNumberList": ["711xxxxx", "712xxxxx"]
}
```
