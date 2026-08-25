---
title: "新增钉钉待办任务"
source_url: "https://open.dingtalk.com/document/development/new-to-do-items"
namespace: "development"
slug: "new-to-do-items"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 待办任务 > 新增钉钉待办任务"
doc_id: "ypO6yjZVTm"
updated_at: "2026-08-25 09:38:10"
---

> Source: https://open.dingtalk.com/document/development/new-to-do-items
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 待办任务 > 新增钉钉待办任务
> Updated: 2026-08-25 09:38:10

# 新增钉钉待办任务

调用本接口，发起一个待办任务。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)接口，已接入用户不受影响。

目前待办任务有防骚扰控制，具体为：

- 每人每天最多收到一条表单内容相同的待办。触发这个限制，会返回错误码400001。
- 每人每天最多收到100条待办。触发这个限制，会返回错误码400002。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/workrecord/add`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager4220 | 任务的执行人userid。 |
| create\_time | Number | 是 | 1599580799000 | 待办时间，Unix时间戳。  **[!NOTE]**  该参数只影响待办显示的先后顺序。 |
| title | String | 是 | 新人学习 | 待办任务的标题，最多50个字符。 |
| url | String | 是 | https://oa.dingtalk.com | 待办任务的跳转链接。当链接是某个微应用链接时，希望在PC端工作台打开，可通过[消息链接在PC端工作台打开](0776-message-link-description.md#section-6s1-jif-wyt)实现。  **[!NOTE]**  待办跳转地址不支持跳转进入小程序。 |
| pcUrl | String | 否 | https://oa.dingtalk.com | PC端跳转URL，不传则使用URL参数。 |
| formItemList | FormItemVo[] | 是 |  | 表单列表。 |
| title | String | 是 | 标题 | 表单标题。 |
| content | String | 是 | 内容 | 表单内容。 |
| originator\_user\_id | String | 否 | manager7078 | 发起人的userid。 |
| source\_name | String | 否 | 人事 | 待办来源名称。该名称会显示在待办的“来源”位置。 |
| pc\_open\_type | Number | 否 | 2 | 待办的PC打开方式:   - **2**：在PC端打开 - **4**：在浏览器打开 |
| biz\_id | String | 否 | 11 | 外部业务ID，建议带上业务方来源字段，防止与其他业务方冲突。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 不合法的access\_token | 调用接口失败时返回的错误信息。创建成功不会返回。 |
| request\_id | String | 7jtw2fl4kmlm | 请求ID。 |
| record\_id | String | recordbc83ea0f6aexxxx | 待办任务ID。  **[!NOTE]**  待办创建后，若两个小时内未处理，则两小时后会被计入已逾期。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/workrecord/add?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "create_time": 1599580799000,
  "pcUrl": "https://oa.dingtalk.com",
  "pc_open_type": 2,
  "formItemList": [
    {
      "title": "新人学习2",
      "content": "产品学习"
    }
  ],
  "title": "学习任务",
  "biz_id": "1112",
  "userid": "manager4220",
  "url": "https://oa.dingtalk.com",
  "originator_user_id": "manager7078",
  "source_name": "学习"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/workrecord/add");
OapiWorkrecordAddRequest req = new OapiWorkrecordAddRequest();
req.setUserid("manager4220");
req.setCreateTime(1599580799000L);
req.setTitle("学习任务");
req.setUrl("https://oa.dingtalk.com");
req.setPcUrl("https://oa.dingtalk.com");
List<FormItemVo> list2 = new ArrayList<FormItemVo>();
FormItemVo obj3 = new FormItemVo();
list2.add(obj3);
obj3.setTitle("新人学习2");
obj3.setContent("产品学习");
req.setFormItemList(list2);
req.setOriginatorUserId("manager7078");
req.setSourceName("学习");
req.setPcOpenType(2L);
req.setBizId("1112");
OapiWorkrecordAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "record_id": "recordbc83ea0f6aexxxx",
  "request_id": "7jtw2fl4kmlm"
}
```

## 错误码

| 参数 | 说明 | 排查方法 |
| --- | --- | --- |
| 33012 | 无效的userid | 请检查userid参数是否合法。 |
| 40035 | 参数不合法 | - 请检查title参数是否小于50个字符。 - formItemList数组长度是否小于20。 |
| 400002 | 参数错误 | 请检查title或者content参数是否为空。 |
| 854001 | 待办任务重复 | 每人每天最多收到一条表单内容相同的待办，这里的表单内容，包括title和formItemList参数。还有一种情况，当传了biz\_id参数时，每个用户的biz\_id不能重复。 |
| 854002 | 待办任务超过每日限额 | 每人每天最多收到100条待办。 |
