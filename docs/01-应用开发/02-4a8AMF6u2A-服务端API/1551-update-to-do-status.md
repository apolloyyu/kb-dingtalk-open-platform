---
title: "更新钉钉待办任务"
source_url: "https://open.dingtalk.com/document/development/update-to-do-status"
namespace: "development"
slug: "update-to-do-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 待办任务 > 更新钉钉待办任务"
doc_id: "jvZjcwNuS9"
updated_at: "2026-08-25 09:38:11"
---

> Source: https://open.dingtalk.com/document/development/update-to-do-status
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 待办任务 > 更新钉钉待办任务
> Updated: 2026-08-25 09:38:11

# 更新钉钉待办任务

调用本接口更新钉钉待办任务。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新钉钉待办任务](0796-updates-dingtalk-to-do-tasks.md)接口，已接入用户不受影响。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/workrecord/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager7078 | 任务执行人的userid。 |
| record\_id | String | 是 | recordfcf7403667fcd9 | 待办任务唯一ID，可使用[新增钉钉待办任务](1550-new-to-do-items.md)中传入的biz\_id，也可以使用返回中的record\_id。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| request\_id | String | f8zya4r96der | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/workrecord/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "record_id":"recordfcf7403667fcd9",
  "userid":"manager7078"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/workrecord/update");
OapiWorkrecordUpdateRequest req = new OapiWorkrecordUpdateRequest();
req.setUserid("manager7078");
req.setRecordId("recordfcf7403667fcd9");
OapiWorkrecordUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": true,
  "request_id": "f8zya4r96der"
}
```

## 错误码

| 错误码 | 错误码说明 | 排查方法 |
| --- | --- | --- |
| 33012 | 无效的userid | 请检查userid参数是否合法。 |
