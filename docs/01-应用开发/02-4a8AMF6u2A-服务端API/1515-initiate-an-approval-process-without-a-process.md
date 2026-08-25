---
title: "创建实例"
source_url: "https://open.dingtalk.com/document/development/initiate-an-approval-process-without-a-process"
namespace: "development"
slug: "initiate-an-approval-process-without-a-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 创建实例"
doc_id: "EDXy7St1jE"
updated_at: "2026-08-25 09:37:55"
---

> Source: https://open.dingtalk.com/document/development/initiate-an-approval-process-without-a-process
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 创建实例
> Updated: 2026-08-25 09:37:55

# 创建实例

调用本接口创建不带流程的审批实例。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建实例](0513-create-a-ticket-approval-instance.md)接口，已接入用户不受影响。

## **接口说明**

- 调用该接口创建实例，接口返回的**审批实例ID**请务必注意保存，方便后续调用其他接口使用。
- 创建实例后，根据**审批实例ID**调用服务端API-[创建待办事项](1521-create-a-to-do-task.md)接口，可以在钉钉客户端待办中查看审批实例。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | SaveFakeProcessInstanceRequest | 是 |  | 请求对象。 |
| agentid | Number | 是 | 1234 | 应用标识。可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。应用的agentid。   - 企业内部应用可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。  image - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取   **[!IMPORTANT]**  如果是第三方企业应用必须指定该参数。 |
| process\_code | String | 是 | PROC-EF6YJL35P2xxxx | 审批模板唯一码，调用[创建或更新审批模板](1530-save-approval-template.md)接口获取process\_code参数值。 |
| originator\_user\_id | String | 是 | manager | 审批实例接收人的userid。 |
| form\_component\_values | FormComponentValueVo[] | 是 |  | 表单参数列表。 |
| name | String | 是 | 请假类型 | 表单名称。表单每一栏的名称，对应表单组件的label字段。 |
| value | String | 是 | 事假 | 表单值。 |
| url | String | 是 | http://www.dingtalk.com | 实例在审批应用里的跳转url，需要同时适配移动端和pc端。 |
| title | String | 否 | xxx的审批 | 实例标题。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4if3sjyrfqnr | 请求ID。 |
| success | Boolean | true | 接口调用状态。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | SaveFaceProcessInstanceResponse |  | 实例信息。 |
| process\_instance\_id | String | proc | 审批实例ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "agentid": 836390886,
    "form_component_values": [
      {
        "name": "单行输入框",
        "value": "a"
      }
    ],
    "title": "给你的审批",
    "process_code": "PROC-9FFE8121-xxxx-xxxx-xxxx-19658EB7CA3A",
    "originator_user_id": "user123",
    "url": "http://www.dingtalk.com"
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/create");
OapiProcessWorkrecordCreateRequest req = new OapiProcessWorkrecordCreateRequest();
SaveFakeProcessInstanceRequest obj1 = new SaveFakeProcessInstanceRequest();
obj1.setAgentid(836390886L);
obj1.setProcessCode("PROC-9FFE8121-xxxx-xxxx-xxxx-19658EB7CA3A");
obj1.setOriginatorUserId("user123");
List<FormComponentValueVo> list3 = new ArrayList<FormComponentValueVo>();
FormComponentValueVo obj4 = new FormComponentValueVo();
list3.add(obj4);
obj4.setName("单行输入框");
obj4.setValue("a");
obj1.setFormComponentValues(list3);
obj1.setUrl("http://www.dingtalk.com");
obj1.setTitle("xxx的审批");
req.setRequest(obj1);
OapiProcessWorkrecordCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "process_instance_id": "c186baff-xxxx-xxxx-xxxx-7901a8646975"
  },
  "success": true,
  "request_id": "4if3sjyrfqnr"
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
| 830001 | 审批流不存在 | 模板code参数错误 | 请确认表单code参数是否正确 |
| 8100017 | 无操作审批流的权限，请检查审批实例或者模板是否正确 | processCode参数不正确 | processCode必须使用[创建或更新审批模板](1530-save-approval-template.md)接口返回的processCode，并且参数fake\_mode必须传true。 |
| 810003 | 审批流的表单格式错误 | 审批流的表单格式错误 | 请参照本文中「支持的表单参数」部分进行传值 |

## 支持的表单参数

表单参数采用key/value的形式，其中key是每个控件对应的名字，value可以是普通字符串，也可以是json字符串。

| 控件 | 使用说明 |
| --- | --- |
| 输入框 | value是普通字符串。 |
| 图片 | value是json数组，每个数组元素必须为图片的URL。例如：   ``` ["http://url1","http://url2","http://url3"] ``` |
| 金额/数字 | value是数字。 |
| 单选框 | value是字符串，必须是在审批模板设计时预设值的单选框的值。 |
| 日期 | value是字符串，根据日期类型来传值，分别为“yyyy-MM-dd hh:mm” 和“yyyy-MM-dd”。 |
| 日期区间 | name是一个数组，value也是对应数组，格式如下：   ``` {       "name": "[\"开始时间\",\"结束时间\"]",       "value": "[\"2019-02-19\",\"2019-02-25\"]" } ``` |

## 常见问题

**Q：调用这个接口后，会有什么效果？**

调用该接口后，发起人打开钉钉审批应用“我发起的”页面，新增一条审批记录。

**Q：url中的参数有什么要求？**

接口中的url，是审批单的跳转url。发起人和审批人在钉钉审批的各个列表页点击后，会跳转到该url。因此，为确保跳转正确，该url需要在钉钉移动端和PC端都能正确打开。
