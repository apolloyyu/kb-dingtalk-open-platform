---
title: "获取公告详情"
source_url: "https://open.dingtalk.com/document/development/obtains-the-details-of-a-bulletin-that-is-not-deleted"
namespace: "development"
slug: "obtains-the-details-of-a-bulletin-that-is-not-deleted"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 公告 > 获取公告详情"
doc_id: "vWebo1XTiO"
updated_at: "2026-08-25 09:38:09"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-details-of-a-bulletin-that-is-not-deleted
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 公告 > 获取公告详情
> Updated: 2026-08-25 09:38:09

# 获取公告详情

调用本接口，根据公告ID获取未删除的公告的详情。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取公告详情](0282-obtains-the-details-get-blackboard.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> 公告的保密级别和查看权限要求如下：
>
> - 非保密公告，可查看人员：
>
>   - 全公司员工
> - 保密公告，可查看人员：
>
>   - 公告管理员
>   - 公告的接收人

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/blackboard/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| blackboard\_id | String | 是 | 9uiuihhgui989huh | 公告id，可以通过[获取公告ID列表](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口获取id参数值。 |
| operation\_userid | String | 是 | manager01 | 操作人userId。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Object | OapiBlackboardVo | 公告详情。 |
| id | String | 9uiuihhgui989huh | 公告id。 |
| author | String | 小明 | 公告作者。 |
| title | String | 入职须知 | 公告标题。 |
| content | String | 欢迎加入我们的大家庭 | 公告内容。 |
| category\_id | String | 09ui87hgyytg463634 | 公告分类ID。 |
| private\_level | Number | 0 | 保密等级。   - **0**：普通公告 - **20**：保密公告 |
| depname\_list | String[] | 人事部 | 接收部门列表。 |
| username\_list | String[] | 小明 | 接收人列表。 |
| gmt\_create | String | 2019-10-22 14:43:07 | 公告创建时间。 |
| gmt\_modified | String | 2019-11-22 10:43:07 | 公告最后修改时间。 |
| read\_count | Number | 10 | 已读人数。 |
| unread\_count | Number | 1 | 未读人数。 |
| coverpic\_url | String | https://gw.alicdn.com/tfs/TB1ayl9mpYqK1RjSZLeXXbXppXa-170-62.png | 封面图的url链接。 |
| user\_list | Object[] | ["user\_list":{"staff\_id":"001","name":"小明"}] | 接收人列表。 |
| staff\_id | String | 001 | 员工userId。 |
| name | String | 小明 | 员工名字。 |
| deptList | Object[] | ["user\_list":{"dept\_id":"001","name":"人事部"}] | 接收部门列表。 |
| dept\_id | String | hbjev8364 | 部门ID，该参数已加密。 |
| name | String | 人事部 | 部门名称。 |
| success | Boolean | true | 本次调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | q5ddepxxxx | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/blackboard/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "operation_userid":"manager01",
  "blackboard_id":"09iu8y7ghft654"
}
```

**请求示例（JAVA SDK）**

```
public class Main {
  public static void main(String[] args) {
    try {
      DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/get");
      OapiBlackboardGetRequest req = new OapiBlackboardGetRequest();
      req.setBlackboardId("09iu8y7ghft654");
      req.setOperationUserid("manager01");
      OapiBlackboardGetResponse rsp = client.execute(req, access_token);
      System.out.println(rsp.getBody());
    } catch (ApiException e) {
      e.printStackTrace();
    }
  }
}
```

**返回示例**

```
{
  "result":{
    "gmt_create":"2019-10-22 14:43:07",
    "coverpic_url":"https://gw.alicdn.com/tfs/TB1ayl9mpYqK1RjSZLeXXbXppXa-170-62.png",
    "username_list":"李四",
    "author":"张三",
    "depname_list":"人事部",
    "user_list":{
      "staff_id":"001",
      "name":"小明"
    },
    "title":"入职须知",
    "gmt_modified":"2019-11-22 10:43:07",
    "content":"欢迎加入我们的大家庭",
    "unread_count":"1",
    "deptList":{
      "name":"人事部",
      "dept_id":"hbjev8364"
    },
    "category_id":"09ui87hgyytg463634",
    "private_level":"0",
    "id":"9uiuihhgui989huh",
    "read_count":"10",
  },
  "errcode":"0",
  "success":"true",
  "request_id":"q5ddepxxxx"
}
```
