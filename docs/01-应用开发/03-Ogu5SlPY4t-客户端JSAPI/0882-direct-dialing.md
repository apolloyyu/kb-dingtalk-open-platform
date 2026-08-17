---
title: "发起办公电话呼叫"
source_url: "https://open.dingtalk.com/document/development/direct-dialing"
namespace: "development"
slug: "direct-dialing"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 办公电话 > 发起办公电话呼叫"
doc_id: "1g2ouEoLV0"
updated_at: "2025-09-17 20:57:35"
---

> Source: https://open.dingtalk.com/document/development/direct-dialing
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 办公电话 > 发起办公电话呼叫
> Updated: 2025-09-17 20:57:35

# 发起办公电话呼叫

调用**biz.conference.createCloudCall**发起办公电话呼叫。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥6.0.0） | 支持（钉钉版本≥6.0.0） | 支持（钉钉版本≥6.0.9） |

```
dd.biz.conference.createCloudCall ({
  "corpId":"xxx",
  "bizNumber":"057xxxx188",
  "calleeNumber":"158xxxx9339",
  "closePushCallRecord":false,
  "openCallRecord":false,
  "hideCalleeNumber":false,
  onSuccess:function() {
},
  onFail:function() {
}
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业corpId。 |
| bizNumber | String | 是 | 指定外呼的号码。 |
| calleeNumber | String | 是 | 外呼的被叫号码。 |
| closePushCallRecord | Boolean | 否 | 是否关闭推送钉钉通话记录：   - **false**（默认）：不关闭 - **true**：关闭推送 |
| openCallRecord | Boolean | 否 | 打开通话录音：   - **false**（默认）：关闭 - **true**：打开 |
| hideCalleeNumber | Boolean | 否 | 拨打面板是否完整显示被叫号码 ：   - **false**（默认）：不显示 - **true**：显示 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 返回码。  **200**：正常 |
| cause | String | 异常描述。 |
| sessionId | Boolean | 会话ID。 |
