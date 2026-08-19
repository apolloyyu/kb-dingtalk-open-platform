---
title: "查询用户详情"
source_url: "https://open.dingtalk.com/document/development/query-user-details"
namespace: "development"
slug: "query-user-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 查询用户详情"
doc_id: "UbRx6mZowM"
updated_at: "2026-06-08 09:28:32"
---

> Source: https://open.dingtalk.com/document/development/query-user-details
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 查询用户详情
> Updated: 2026-06-08 09:28:32

# 查询用户详情

调用本接口获取指定用户的详细信息。

## **接口调用说明**

调用本接口可以实现查询普通账号用户详情或查询企业账号用户详情。由于在调用时参数使用有较多区别，为便于开发者查看，按照新用户的账号类型进行拆分优化：

- 查询普通账号用户详情，接口说明文档请查看本文介绍。
- 查询企业账号用户详情，接口说明文档请参见[查询企业账号用户详情](0108-queries-the-details-of-a-dedicated-account.md)。

如果需要获取手机号和邮箱等权限，不同的应用类型获取方式不同。

- 企业内部应用如需获取用户的手机号、邮箱信息，需要添加获取通讯录中手机号和邮箱的权限。添加方法如下：

  登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/corpeapp) > **企业内部开发** > **找到需添加权限的应用** > **权限管理** > **通讯录管理**页面，勾选**企业员工手机号信息**和**邮箱等个人信息**，单击申请权限。![未标题-1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3187780561/p433431.gif)
- 第三方企业应用如需获取用户手机号、邮箱信息，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager4220 | 用户的userId。 |
| language | String | 否 | zh\_CN | 通讯录语言。   - **zh\_CN**：中文（默认值） - **en\_US**：英文 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b97a231d-7dd8-4243-ac4e-6b75b2a1e28a' \
-d 'language=zh_CN' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
OapiV2UserGetRequest req = new OapiV2UserGetRequest();
req.setUserid("001");
req.setLanguage("zh_CN");
OapiV2UserGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserGetRequest("https://oapi.dingtalk.com/topapi/v2/user/get")

req.userid="zhangsan"
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
$req = new OapiV2UserGetRequest;
$req->setUserid("zhangsan");
$req->setLanguage("zh_CN");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
OapiV2UserGetRequest req = new OapiV2UserGetRequest();
req.Userid = "zhangsan";
req.Language = "zh_CN";
OapiV2UserGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4e7exhl6pm0t | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | Object |  | 返回结果。 |
| userid | String | zhangsan | 员工的userId。 |
| unionid | String | z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ | 员工在当前开发者企业账号范围内的唯一标识。 |
| name | String | 张三 | 员工姓名。 |
| avatar | String | xxx | 头像。  **[!NOTE]**  员工使用默认头像，不返回该字段，手动设置头像会返回。 |
| state\_code | String | 86 | 国际电话区号。  **[!NOTE]**  第三方企业应用不返回该字段；如需获取state\_code，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| manager\_userid | String | user01 | 员工的直属主管。  **[!NOTE]**  员工在企业管理后台个人信息面板中，**直属主管**内有值，才会返回该字段。 |
| mobile | String | 18513027676 | 手机号码。  **[!NOTE]**   - 企业内部应用，只有应用开通通讯录**企业员工手机号信息**权限，才会返回该字段。  image - 第三方企业应用不返回该字段，如需获取mobile，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| hide\_mobile | Boolean | false | 是否号码隐藏：   - **true**：隐藏 - **false**：不隐藏  **[!NOTE]**  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 |
| telephone | String | 010-86123456-2345 | 分机号。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| job\_number | String | 4 | 员工工号。 |
| title | String | 技术总监 | 职位。 |
| email | String | test@xxx.com | 员工邮箱。  **[!NOTE]**   - 企业内部应用，只有应用开通通讯录**邮箱等个人信息**权限，才会返回该字段。 - 第三方企业应用，不返回该参数；如需获取email，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| work\_place | String | 未来park | 办公地点。  **[!NOTE]**   - 员工信息面板中该字段必须有值，才正常返回。如果无值，则不返回该字段。 - 企业内部应用，只有应用开通通讯录**邮箱等个人信息**权限，才会返回该字段。 - 第三方企业应用，不返回该参数。 |
| remark | String | 备注备注 | 备注。  **[!NOTE]**   - 员工信息面板中该字段必须有值，才正常返回。如果无值，则不返回该字段。 - 企业内部应用，只有应用开通通讯录**邮箱等个人信息**权限，才会返回该字段。 - 第三方企业应用，不返回该参数。 |
| exclusive\_account | Boolean | false | 是否为企业账号：   - true：是 - false：不是 |
| org\_email | String | test@xxx.com | 员工的企业邮箱。  如果员工的企业邮箱没有开通，返回信息中不包含该数据。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| dept\_id\_list | Number[] | [2,3,4] | 所属部门id列表。 |
| dept\_order\_list | Object[] |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 2 | 部门id。 |
| order | Number | 1 | 员工在部门中的排序。 |
| extension | String | {"爱好":"旅游","年龄":"24"} | 扩展属性，最大长度2000个字符。  **[!NOTE]**   - 员工信息面板中添加的拓展字段内有值才返回。 - 企业内部应用，只有应用开通通讯录**邮箱等个人信息**权限，才会返回该字段。 - 第三方企业应用，不返回该字段。 - **重要提示**：直接添加新属性会覆盖原有属性值，需要先获取现有属性，然后将新属性追加到已有属性上，再进行整体更新。 |
| hired\_date | Number | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。  **[!NOTE]**   - 信息面板中**入职时间**字段内有值才返回。 - 第三方企业应用，不返回该参数。 |
| active | Boolean | true | 是否激活了钉钉：   - **true**：已激活 - **false**：未激活 |
| real\_authed | Boolean | true | 是否完成了实名认证：   - **true**：已认证 - **false**：未认证 |
| senior | Boolean | true | 是否为企业的高管：   - **true**：是 - **false**：不是 |
| admin | Boolean | true | 是否为企业的管理员：   - **true**：是 - **false**：不是 |
| boss | Boolean | true | 是否为企业的老板：   - **true**：是 - **false**：不是 |
| leader\_in\_dept | Object[] |  | 员工所在部门信息及是否是领导：   - 员工所在部门的部门ID。 - 员工在对应的部门中是否是领导：    - true：是   - false：不是 |
| dept\_id | Number | 2 | 部门ID。 |
| leader | Boolean | true | 是否是领导：   - **true**：是 - **false**：不是 |
| role\_list | Object[] |  | 角色列表。 |
| id | Number | 100 | 角色ID。 |
| name | String | 总监 | 角色名称。 |
| group\_name | String | 职务 | 角色组名称。 |
| union\_emp\_ext | Object |  | 当用户来自于关联组织时的关联信息。  **[!NOTE]**  用户所在企业存在关联关系的企业，返回该字段。 |
| userid | String | 500 | 员工id的userId。 |
| union\_emp\_map\_list | Object[] |  | 关联映射关系。 |
| userid | String | 5000 | 关联分支组织中的员工userId。 |
| corp\_id | String | dingxxx | 关联分支组织的企业corpId。 |
| corp\_id | String | dingxxx | 当前用户所属的组织的企业corpId。 |
| dept\_position\_list | DeptPosition[] |  | 部门内任职信息。 |
| extension\_i18n | Json | {"爱好":  {"zh\_ CN":  "旅游",  "en\_ US":  "travel",  "aJP":"旅  行"} | 扩展属性的国际化值。 |

### **响应体示例**

```
{
  "errcode":"0",
  "result":{
    "extension":"{\"爱好\":\"旅游\",\"年龄\":\"24\"}",
    "unionid":"z21HjQliSzpw0YWxxxxx",
    "boss":"true",
    "role_list":{
      "group_name":"职务",
      "name":"总监",
      "id":"100"
    },
    "exclusive_account":false,
    "manager_userid":"manager240",
    "admin":"true",
    "remark":"备注备注",
    "title":"技术总监",
    "hired_date":"1597573616828",
    "userid":"zhangsan",
    "work_place":"未来park",
    "dept_order_list":{
      "dept_id":"2",
      "order":"1"
    },
    "real_authed":"true",
    "dept_id_list":"[2,3,4]",
    "job_number":"4",
    "email":"test@xxx.com",
    "leader_in_dept":{
      "leader":"true",
      "dept_id":"2"
    },
    "mobile":"18513027676",
    "active":"true",
    "org_email":"test@xxx.com",
    "telephone":"010-86123456-2345",
    "avatar":"xxx",
    "hide_mobile":"false",
    "senior":"true",
    "name":"张三",
    "union_emp_ext":{
      "union_emp_map_list":{
        "userid":"5000",
        "corp_id":"dingxxx"
      },
      "userid":"500",
      "corp_id":"dingxxx"
    },
    "state_code":"86"
  },
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33012 | 无效的userId | 请检查userId是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后再试 |
