---
title: "查询待办列表"
source_url: "https://open.dingtalk.com/document/development/query-a-user-s-to-do-items"
namespace: "development"
slug: "query-a-user-s-to-do-items"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 查询待办列表"
doc_id: "w8VdPjes6f"
updated_at: "2026-08-25 13:50:01"
---

> Source: https://open.dingtalk.com/document/development/query-a-user-s-to-do-items
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 查询待办列表
> Updated: 2026-08-25 13:50:01

# 查询待办列表

调用本接口，查询用户待办任务。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/task/query`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager7078 | 要查询的执行人userid。 |
| offset | Number | 是 | 0 | 分页游标。支持分页查询，与count参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| count | Number | 是 | 20 | 分页大小，最大50。 |
| status | Number | 是 | 0 | 待办事项的状态：   - **0**：待处理 - **-1**：已经移除 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult | {} | 查询结果。 |
| has\_more | Boolean | true | 是否有更多数据。   - **true**：有更多的数据 - **false**：无更多数据 |
| list | WorkRecordVo[] | [] | 事项列表。 |
| url | String | http://www | 待办跳转链接。 |
| task\_id | String | 65429579088 | 待办任务ID。 |
| instance\_id | String | 673c9677-8b4e-13xxxx | 实例ID。 |
| title | String | xxx提交的入职审批 | 待办标题。 |
| forms | FormItemVo[] | [] | 表单列表。 |
| title | String | 入职员工姓名 | 表单标题。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| request\_id | String | 107anigl5ekxg | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/task/query?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "offset":"0",
  "count":"20",
  "userid":"manager7078",
  "status":"0"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/task/query");
OapiProcessWorkrecordTaskQueryRequest req = new OapiProcessWorkrecordTaskQueryRequest();
req.setUserid("manager7078");
req.setOffset(0L);
req.setCount(20L);
req.setStatus(0L);
OapiProcessWorkrecordTaskQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "has_more": true,
    "list": [
      {
        "forms": [
          {
            "content": "杨xx",
            "title": "入职员工姓名"
          },
          {
            "content": "技术支持",
            "title": "用人部门"
          },
          {
            "content": "测试",
            "title": "职位"
          }
        ],
        "instance_id": "b6a42e32-1867-499c-94f2-e0b221423313",
        "task_id": "65429579088",
        "title": "xx提交的入职审批",
        "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?xxx"
      },
      {
        "forms": [
          {
            "content": "北京",
            "title": "出差地点"
          },
          {
            "content": "2018-08-21",
            "title": "开始时间"
          },
          {
            "content": "2018-08-25",
            "title": "结束时间"
          }
        ],
        "instance_id": "673c9677-8b4e-4013-82a3-838fddf62187",
        "task_id": "65394649400",
        "title": "xx提交的出差申请",
        "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?xxx"
      }
    ]
  },
  "request_id": "107anigl5ekxg"
}
```

## 错误码

| **错误码（errorcode）** | **错误码描述（errmsg）** | **错误原因** | **解决方案** |
| --- | --- | --- | --- |
| 43007 | 需要授权 | access\_token不正确 | 请确认access\_token是否正确 |
| 40056 | 无效的微应用ID | 微应用ID参数错误 | 请确认微应用ID是否正确 |
| 40083 | 无效的suiteKey | 应用suiteKey参数错误 | 请确认应用suiteKey是否正确 |
| -1 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400001 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400002 | 用户ID不能为空，请检查 | 用户ID参数错误 | 请确认用户ID是否正确 |
| 40035 | 参数非法，请检查分页参数跟起始时间 | 分页参数跟起始时间参数错误 | 请检查分页参数跟起始时间 |
