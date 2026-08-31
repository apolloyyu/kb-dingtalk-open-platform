---
title: "获取填表实例数据"
source_url: "https://open.dingtalk.com/document/development/obtains-multiple-form-filling-records"
namespace: "development"
slug: "obtains-multiple-form-filling-records"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 智能填表 > 获取填表实例数据"
doc_id: "vM9BjJGQZs"
updated_at: "2026-08-25 09:39:18"
---

> Source: https://open.dingtalk.com/document/development/obtains-multiple-form-filling-records
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 智能填表 > 获取填表实例数据
> Updated: 2026-08-25 09:39:18

# 获取填表实例数据

调用本接口根据填表的form\_code获取填表实例数据。

> **[!IMPORTANT]**
>
> - 调用此接口的QPS不能超过20，超过会返回限流错误。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取填表实例列表](0971-obtain-the-table-filling-instance-list-data.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/collection/instance/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| form\_code | String | 是 | PROC-E5BD2166-B6F4-xxxx | 填表模板code，调用[获取用户创建的填表模板](1622-obtains-the-template-that-a-user-creates.md)接口获取。 |
| action\_date | String | 否 | 2019-01-01 | 时间，必须是YYYY-MM-DD的格式。循环填表才需要传这个参数。 |
| offset | Number | 是 | 0 | 分页起始，从0开始。当返回结果中has\_more为false时，表示没有下一页了。否则取返回结果中next\_cursor的值作为下一次请求的offset。 |
| size | Number | 是 | 10 | 分页大小，最大100。 |
| biz\_type | Number | 否 | 0 | 填表类型：   - **0**：通用智能填表 - **1**：教育版填表 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 7vk8g5e4qmpx | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageResult |  | 返回结果。 |
| has\_more | Boolean | true | 是否还有下一页数据。 |
| list | FormInstanceResponse[] |  | 填表列表。 |
| create\_time | Date | 2020-10-15 22:04:1 | 填表提交时间。 |
| submitter\_userid | String | user123 | 提交人的userid。 |
| submitter\_user\_name | String | 杨xx | 提交人姓名。 |
| forms | FormData[] |  | 表单内容列表。 |
| value | String | 操作演示 | 表单的值。 |
| label | String | 你希望的主题 | 表单主题。  当label字段为空或不存在时，忽略这个label和value。 |
| key | String | TextareaField\_KGAW58AQ | 表单控件key。 |
| student\_class\_name | String | 二年一班 | 学生班级名称。 |
| student\_name | String | 赵xx | 学生名称。 |
| student\_class\_id | Number | 1 | 学生班级ID。 |
| student\_user\_id | String | 12345 | 学生ID。 |
| modify\_time | Date | 2020-10-15 22:04:18 | 更新时间。 |
| form\_instance\_id | String | 11125769-fxxxx | 实例ID。 |
| next\_cursor | Number | 1 | 下一次分页offset的值。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/collection/instance/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
 "offset":0,
 "size":10,
 "biz_type":0,
 "action_date":"2019-01-01",
 "form_code":"PROC-E5BD2166-B6F4-xxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/collection/instance/list");
OapiCollectionInstanceListRequest req = new OapiCollectionInstanceListRequest();
req.setFormCode("PROC-E5BD2166-B6F4-xxxx");
req.setActionDate("2019-01-01");
req.setOffset(0L);
req.setSize(10L);
req.setBizType(0L);
OapiCollectionInstanceListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "has_more": false,
    "list": [
      {
        "create_time": "2020-10-15 22:04:18",
        "form_instance_id": "11125769-fa63-4bce-8494-39ea14d5482d",
        "forms": [
          {
            "key": "TextareaField_KGAW58AQ",
            "label": "你希望的主题",
            "value": "操作演示"
          },
          {
            "key": "HiddenField_interval",
            "value": "22644"
          }
        ],
        "modify_time": "2020-10-15 22:04:18",
        "submitter_user_name": "杨xx",
        "submitter_userid": "manager4220"
      }
    ],
    "next_cursor": 1
  },
  "request_id": "7vk8g5e4qmpx"
}
```
