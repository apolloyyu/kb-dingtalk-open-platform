---
title: "获取部门用户详情"
source_url: "https://open.dingtalk.com/document/development/queries-the-complete-information-of-a-department-user"
namespace: "development"
slug: "queries-the-complete-information-of-a-department-user"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 获取部门用户详情"
doc_id: "fPaCqtLCEL"
updated_at: "2026-06-08 09:28:35"
---

> Source: https://open.dingtalk.com/document/development/queries-the-complete-information-of-a-department-user
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 获取部门用户详情
> Updated: 2026-06-08 09:28:35

# 获取部门用户详情

调用本接口获取指定部门中的用户详细信息。

## **接口调用说明**

- 本接口只支持获取指定部门下的员工详情信息，子部门员工信息获取不到。
- 调用本接口可以实现获取部门普通账号用户详情或获取部门企业账号用户详情。由于在调用时参数使用有较多区别，为便于开发者查看，按照新用户的账号类型进行拆分优化：

  - 如果是获取部门普通账号用户详情，接口说明文档请查看本文介绍。
  - 如果是获取部门企业账号用户详情（一般是企业钉钉用户），接口说明文档请参见[获取部门企业账号用户详情](0116-queries-account-details.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_member-通讯录部门成员读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 10 | 部门ID，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)获取，如果是根部门，该参数传1。  **[!NOTE]**  只获取当前部门下的员工信息，不包含子部门内的员工。 |
| cursor | Number | 是 | 0 | 分页查询的游标，最开始传0，后续传返回参数中的next\_cursor值。 |
| size | Number | 是 | 10 | 分页大小。 |
| order\_field | String | 否 | modify\_desc | 部门成员的排序规则，默认不传是按自定义排序（custom）：   - **entry\_asc**：代表按照进入部门的时间升序 - **entry\_desc**：代表按照进入部门的时间降序 - **modify\_asc**：代表按照部门信息修改时间升序 - **modify\_desc**：代表按照部门信息修改时间降序 - **custom**：代表用户定义(未定义时按照拼音)排序 |
| contain\_access\_limit | Boolean | 否 | false | 是否返回访问受限的员工：   - true：返回 - false：不返回 |
| language | String | 否 | zh\_CN | 通讯录语言，取值。   - **zh\_CN**：中文（默认值）。 - **en\_US**：英文。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=834f6b00-25b8-4484-a89d-595d1f7fa0a7' \
-d 'contain_access_limit=false' \
-d 'cursor=0' \
-d 'dept_id=10' \
-d 'language=zh_CN' \
-d 'order_field=modify_desc' \
-d 'size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/list");
OapiV2UserListRequest req = new OapiV2UserListRequest();
req.setDeptId(1L);
req.setCursor(0L);
req.setSize(10L);
req.setOrderField("modify_desc");
req.setContainAccessLimit(false);
req.setLanguage("zh_CN");
OapiV2UserListResponse rsp = client.execute(req, "");
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserListRequest("https://oapi.dingtalk.com/topapi/v2/user/list")

req.dept_id=10
req.cursor=0
req.size=10
req.order_field="modify_desc"
req.contain_access_limit=false
req.language="zh_CN"
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiV2UserListRequest;
$req->setDeptId("10");
$req->setCursor("0");
$req->setSize("10");
$req->setOrderField("modify_desc");
$req->setContainAccessLimit("false");
$req->setLanguage("zh_CN");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/list");
OapiV2UserListRequest req = new OapiV2UserListRequest();
req.DeptId = 10L;
req.Cursor = 0L;
req.Size = 10L;
req.OrderField = "modify_desc";
req.ContainAccessLimit = false;
req.Language = "zh_CN";
OapiV2UserListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | Object |  | 返回结果。 |
| has\_more | Boolean | true | 是否还有更多的数据：   - true：有 - false：没有 |
| next\_cursor | Number | 10 | 下一次分页的游标。  **[!NOTE]**  如果**has\_more**为**false**，表示没有更多的分页数据。 |
| list | Object[] |  | 用户信息列表。 |
| userid | String | zhangsan | 用户的userId。 |
| unionid | String | z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ | 用户在当前开发者企业账号范围内的唯一标识。 |
| name | String | 张三 | 用户姓名。 |
| avatar | String | xxx | 头像地址。 |
| state\_code | String | 86 | 国际电话区号。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**企业员工手机号信息权限**是否开启。 - 第三方企业应用不返回该参数；如需获取state\_code，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| mobile | String | 18513027676 | 手机号码。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**企业员工手机号信息权限**是否开启。 - 第三方企业应用不返回该参数；如需获取mobile，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| hide\_mobile | Boolean | false | 是否号码隐藏：   - **true**：隐藏  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 - **false**：不隐藏 |
| telephone | String | 010-86123456-2345 | 分机号。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| job\_number | String | 4 | 员工工号。 |
| title | String | 技术总监 | 职位。 |
| email | String | test@xxx.com | 员工邮箱。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启 - 员工信息面板中有邮箱字段值才返回该字段 - 第三方企业应用不返回该参数 |
| org\_email | String | test@xxx.com | 员工的企业邮箱。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启 - 员工信息面板中该字段内有值才返回 - 第三方企业应用不返回该参数 |
| work\_place | String | 未来park | 办公地点。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启 - 员工信息面板中该字段内有值才返回 - 第三方企业应用不返回该参数 |
| remark | String | 备注备注 | 备注。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启 - 员工信息面板中该字段内有值才返回 - 第三方企业应用不返回该参数 |
| dept\_id\_list | Number[] | [2,3,4] | 所属部门id列表。 |
| dept\_order | Number | 1 | 员工在部门中的排序。 |
| extension | String | {\"爱好\":\"旅游\",\"年龄\":\"24\"}" | 扩展属性。  **[!NOTE]**   - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启 - 员工信息面板中该字段内有值才返回 - 第三方企业应用不返回该参数 |
| hired\_date | Number | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| active | Boolean | true | 是否激活了钉钉：   - **true**：已激活 - **false**：未激活 |
| admin | Boolean | true | 是否为企业的管理员：   - **true**：是 - **false**：不是 |
| boss | Boolean | true | 是否为企业的老板：   - **true**：是 - **false**：不是 |
| leader | Boolean | true | 是否是部门的主管：   - **true**：是 - **false**：不是 |
| exclusive\_account | Boolean | false | 是否企业账号：   - **true**：是 - **false**：不是   **[!NOTE]**   - 企业账号介绍请参见[企业账号概述](0103-dedicated-account-overview.md)。 - 第三方企业应用不返回该参数。 |

### **响应体示例**

```
{
  "errcode":"0",
  "result":{
    "next_cursor":"10",
    "has_more":"true",
    "list":{
      "leader":"true",
      "extension":"{\"爱好\":\"旅游\",\"年龄\":\"24\"}",
      "unionid":"z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ",
      "boss":"true",
      "exclusive_account":"false",
      "admin":"true",
      "remark":"备注备注",
      "title":"技术总监",
      "hired_date":"1597573616828",
      "userid":"zhangsan",
      "work_place":"未来park",
      "dept_id_list":"[2,3,4]",
      "job_number":"4",
      "email":"test@xxx.com",
      "dept_order":"1",
      "mobile":"18513027676",
      "active":"true",
      "telephone":"010-86123456-2345",
      "avatar":"xxx",
      "hide_mobile":"false",
      "org_email":"test@xxx.com",
      "name":"张三",
      "state_code":"86"
    }
  },
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | 无效的参数 | 请确认参数是否按要求填写 |
| 50004 | 部门不在权限范围内 | 请确认access\_token具有操作权限 |
| 40035 | 参数非法 | dept\_id或cursor或size或order\_field填写不合规范 |
| 60019 | 未能从部门中获取用户 | 请确认相关参数填写正确 |
| -1 | 系统繁忙 | 请稍后再试 |
