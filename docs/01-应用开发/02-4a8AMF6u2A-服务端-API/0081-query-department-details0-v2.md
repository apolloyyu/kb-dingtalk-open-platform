---
title: "获取部门详情"
source_url: "https://open.dingtalk.com/document/development/query-department-details0-v2"
namespace: "development"
slug: "query-department-details0-v2"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 部门管理 > 获取部门详情"
doc_id: "vzI36OIKQo"
updated_at: "2026-06-08 09:22:39"
---

> Source: https://open.dingtalk.com/document/development/query-department-details0-v2
> Path: 应用开发 / 服务端 API / 通讯录管理 > 部门管理 > 获取部门详情
> Updated: 2026-06-08 09:22:39

# 获取部门详情

调用本接口，根据部门ID获取指定部门详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_list-通讯录部门信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 100 | 部门ID，根部门ID为1，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |
| language | String | 否 | zh\_CN | 通讯录语言：   - **zh\_CN**（默认）：中文 - **en\_US**：英文 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d3daxxxx51990' \
-d 'dept_id=100' \
-d 'language=zh_CN'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/get");
OapiV2DepartmentGetRequest req = new OapiV2DepartmentGetRequest();
req.setDeptId(100L);
req.setLanguage("zh_CN");
OapiV2DepartmentGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentGetRequest("https://oapi.dingtalk.com/topapi/v2/department/get")

req.dept_id=100
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
$req = new OapiV2DepartmentGetRequest;
$req->setDeptId("100");
$req->setLanguage("zh_CN");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/department/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/get");
OapiV2DepartmentGetRequest req = new OapiV2DepartmentGetRequest();
req.DeptId = 100L;
req.Language = "zh_CN";
OapiV2DepartmentGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4e7ljtq91rgo | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 错误信息。 |
| result | DeptGetResponse |  | 部门详情。 |
| dept\_id | Number | 100 | 部门ID。 |
| name | String | HR | 部门名称。 |
| parent\_id | Number | 50 | 父部门id，根部门为1。 |
| source\_identifier | String | HR | 部门标识字段。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| create\_dept\_group | Boolean | true | 是否同步创建一个关联此部门的企业群：   - **true**：创建 - **false**：不创建 |
| auto\_add\_user | Boolean | false | 当部门群已经创建后，是否有新人加入部门会自动加入该群：   - **true**：自动加入群 - **false**：不会自动加入群 |
| tags | String | campus | 教育部门标签：   - **campus**：校区 - **period**：学段 - **grade**：年级 - **class**：班级   **[!NOTE]**  第三方企业应用不返回该参数。 |
| from\_union\_org | Boolean | false | 部门是否来自关联组织：   - **true**：是 - **false**：不是   **[!NOTE]**  第三方企业应用不返回该参数。 |
| order | Number | 10 | 在父部门中的次序值。 |
| dept\_group\_chat\_id | String | 123 | 部门群ID。 |
| group\_contain\_sub\_dept | Boolean | true | 部门群是否包含子部门：   - **true**：包含 - **false**：不包含 |
| org\_dept\_owner | String | 80 | 企业群群主userId。 |
| dept\_manager\_userid\_list | String[] | ["5","6","7","8"] | 部门的主管userd列表。 |
| outer\_dept | Boolean | true | 是否限制本部门成员查看通讯录：   - **true**：开启限制。开启后本部门成员**只能看到指定部门/人**的通讯录 - **false**：不限制图片 |
| outer\_permit\_depts | Number[] | [500,600] | 配置的部门员工可见部门Id列表。  **[!NOTE]**  企业设置限制本部门成员查看通讯录，即返回**outer\_dept**值。图片   - **限制本部门成员查看通讯录**（即**outer\_dept**为**true**）：outer\_permit\_depts表示设置的**只能看到指定部门/人**的**部门Id列表**。   **[!NOTE]**  例如，企业开启了限制本部门成员查看通讯录，本部门成员设置了只能看到指定的2个部门、2位员工的通讯录，其中测试部门1的部门Id为1，测试部门2的部门Id为2。  调用本接口，获取到设置的部门outer\_permit\_depts的值为[1,2]。不返回员工列表，即不返回员工小钉1、员工小钉2的信息。  部门可见   - **未限制本部门成员查看通讯录**（即**outer\_dept**为**false**）：调用接口不返回outer\_permit\_depts字段。 |
| outer\_permit\_users | String[] | ["78","79"] | 配置的部门员工可见员工userId列表。  **[!NOTE]**  企业设置限制本部门成员查看通讯录，即返回**outer\_dept**值。图片     - **限制本部门成员查看通讯录**（即**outer\_dept**为**true**）：outer\_permit\_users表示设置的**只能看到指定部门/人**的**员工userId列表**。   **[!NOTE]**  例如，企业开启了限制本部门成员查看通讯录，本部门成员设置了只能看到指定的2个部门、2位员工的通讯录，其中员工小钉1的userId为001，员工小钉2的userId为002。  调用本接口，获取到设置的员工  outer\_permit\_users的值为["001","002"]。不返回部门列表，即不返回测试部门1、测试部门2的信息。iShot2022-04-22_12   - **未限制本部门成员查看通讯录**（即**outer\_dept**为**false**）：调用接口不返回outer\_permit\_users字段。 |
| user\_permits | String[] | ["5","9"] | 隐藏部门的员工userId列表。  **[!NOTE]**  企业开启隐藏本部门，即返回**hide\_dept**值。  EE5D7BF8-88D1-4084-B369-F908A75D7333   - **开启隐藏本部门**（即hide\_dept为true）：user\_permits表示设置的**允许指定部门/人可见**的**员工userId列表。**  **[!NOTE]**  例如，企业开启了隐藏本部门，且分别设置2个部门、2位员工允许指定部门/人可见，其中员工小钉1的userId为001，员工小钉2的userId为002。  调用本接口，获取到设置的员工user\_permits的值为["001","002"]。不返回部门列表，即不返回测试部门1、测试部门2的信息。iShot2022-04-21_14 - **未开启隐藏本部门**（即hide\_dept为false）：调用接口不返回user\_permits字段。 |
| hide\_dept | Boolean | false | 是否开启隐藏本部门：   - **true**：开启隐藏本部门。可以设置隐藏范围，如设置向所有人和部门隐藏，或者允许指定部门/人可见。 - **false**：关闭隐藏本部门，即部门在公司通讯录显示。  EE5D7BF8-88D1-4084-B369-F908A75D7333 |
| dept\_permits | Number[] | [3,4,5] | 隐藏部门的部门Id列表。  **[!NOTE]**  企业开启隐藏本部门，即返回**hide\_dept**值。EE5D7BF8-88D1-4084-B369-F908A75D7333   - **开启隐藏本部门**（即hide\_dept为true）：dept\_permits表示设置的**允许指定部门/人可见**的**部门Id列表。**  **[!NOTE]**  例如，企业开启了隐藏本部门，且分别设置2个部门、2位员工允许指定部门/人可见，其中测试部门1的部门Id为1，测试部门2的部门Id为2。  调用本接口，获取到设置的部门dept\_permits的值为[1,2]。不返回员工列表，即不返回员工小钉1、员工小钉2的信息。iShot2022-04-21_14 - **未开启隐藏本部门**（即hide\_dept为false）：调用接口不返回dept\_permits字段。 |
| auto\_approve\_apply | Boolean | true | 是否默认同意加入该部门的申请：   - **true：**表示加入该部门的申请将默认同意 - **false：**表示加入该部门的申请需要有权限的管理员同意 |
| code | String | 10000 | 部门编码。  **[!NOTE]**  该字段需通过[更新部门](0078-address-book-update-department.md)接口，设置部门编码后才会返回。 |
| member\_count | Number | 10 | 部门员工数（包含子部门）。 |
| owning\_member\_count | Number | 8 | 部门直属员工数（不包含子部门）。 |
| union\_dept\_ext | Object |  | 关联部门信息。 |
| deptId | Number | 1234567 | 关联部门ID。 |
| corpId | String | test | 关联部门的企业corpId。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "dept_permits": [
      3,
      4,
      5
    ],
    "outer_permit_users": [
      "user123",
      "1234"
    ],
    "dept_manager_userid_list": [
      "1020302901-431772414"
    ],
    "org_dept_owner": "manager9153",
    "outer_dept": false,
    "dept_group_chat_id": "chat1fccdb4b921f2bde18c26xxxx",
    "group_contain_sub_dept": true,
    "auto_add_user": true,
    "hide_dept": false,
    "name": "测试",
    "outer_permit_depts": [
      500,
      600
    ],
    "user_permits": [],
    "dept_id": 1,
    "create_dept_group": true,
    "order": 0,
    "code":"100",
    "union_dept_ext":{
      "corp_id": "test",
      "dept_id": 1234567
    }
  },
  "request_id": "4e7ljtq91rgo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 需要授权 | 请确认access\_token具有操作权限 |
| 60003 | 未找到对应部门 | 请确认dept\_id是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后再试 |
