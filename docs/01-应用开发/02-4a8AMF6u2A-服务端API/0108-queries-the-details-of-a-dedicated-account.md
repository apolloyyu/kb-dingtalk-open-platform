---
title: "查询企业账号用户详情"
source_url: "https://open.dingtalk.com/document/development/queries-the-details-of-a-dedicated-account"
namespace: "development"
slug: "queries-the-details-of-a-dedicated-account"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 企业账号 > 查询企业账号用户详情"
doc_id: "7TMeqD6H0C"
updated_at: "2026-05-27 13:09:07"
---

> Source: https://open.dingtalk.com/document/development/queries-the-details-of-a-dedicated-account
> Path: 应用开发 / 服务端API / 通讯录管理 > 企业账号 > 查询企业账号用户详情
> Updated: 2026-05-27 13:09:07

# 查询企业账号用户详情

调用本接口获取指定企业账号用户的详细信息，仅支持购买开通企业账号的组织使用。

## **接口调用说明**

如果需要获取手机号和邮箱等权限，不同的应用类型获取方式不同。

- 企业内部应用

  企业内部应用如需获取用户的手机号、邮箱信息，需要添加获取通讯录中手机号和邮箱的权限。添加方法如下：

  登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/corpeapp) > **企业内部开发** > **找到需添加权限的应用** > **权限管理** > **通讯录管理**页面，勾选**企业员工手机号信息**和**邮箱等个人信息**，单击申请权限。![未标题-1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3187780561/p433431.gif)
- 第三方企业应用

  第三方企业应用如需获取用户手机号、邮箱信息，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。

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
| access\_token | String | 是 | be3Fxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager4220 | 用户的UserId。 |
| language | String | 否 | zh\_CN | 通讯录语言。   - **zh\_CN**：中文（默认值） - **en\_US**：英文 |
| login\_id | String | 否 | test | 登录名，非空则忽略userid。  **[!NOTE]**  使用登录名进行查询，仅限归属于本企业的钉钉自建企业账号 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a894388c-a1b9-4ab4-8623-99cd0502019f' \
-d 'language=zh_CN' \
-d 'login_id=zhangsan' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
OapiV2UserGetRequest req = new OapiV2UserGetRequest();
req.setUserid("zhangsan");
req.setLanguage("zh_CN");
req.setLoginId("zhangsan");
OapiV2UserGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserGetRequest("https://oapi.dingtalk.com/topapi/v2/user/get")

req.userid="zhangsan"
req.language="zh_CN"
req.login_id="zhangsan"
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
$req->setLoginId("zhangsan");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
OapiV2UserGetRequest req = new OapiV2UserGetRequest();
req.Userid = "zhangsan";
req.Language = "zh_CN";
req.LoginId = "zhangsan";
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
| userid | String | zhangsan | 员工的UserId。 |
| unionid | String | z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ | 员工在当前开发者企业账号范围内的唯一标识。 |
| name | String | 张三 | 员工姓名。 |
| avatar | String | xxx | 头像。  **[!NOTE]**     - 员工使用默认头像，不返回该字段。 - 员工手动设置头像会返回该字段。 |
| state\_code | String | 86 | 国际电话区号。  **[!NOTE]**  第三方企业应用不返回该字段；如需获取state\_code，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| mobile | String | 18513027676 | 手机号码。  **[!NOTE]**     - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**企业员工手机号信息权限**是否开启。 - 第三方企业应用不返回该字段；如需获取mobile，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| hide\_mobile | Boolean | false | 是否号码隐藏：   - **true**：隐藏 - **false**：不隐藏  **[!NOTE]**  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉商务电话。 |
| telephone | String | 010-86123456-2345 | 分机号。  **[!NOTE]**  第三方企业应用不返回该字段。 |
| job\_number | String | 4 | 员工工号。 |
| title | String | 技术总监 | 职位。 |
| email | String | test@xxx.com | 员工邮箱。  **[!NOTE]**     - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启。 - 第三方企业应用不返回该字段；如需获取email，可以使用[钉钉统一授权套件](0007-function-description.md)方式获取。 |
| org\_email | String | test@xxx.com | 员工的企业邮箱。  如果员工的企业邮箱没有开通，返回信息中不包含该数据。  **[!NOTE]**  第三方企业应用不返回该字段。 |
| work\_place | String | 未来park | 办公地点。  **[!NOTE]**     - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启。 - 员工信息面板中该字段内有值才返回å。 - 第三方企业应用不返回该字段。 |
| remark | String | 备注备注 | 备注。  **[!NOTE]**     - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启。 - 员工信息面板中该字段内有值才返回。 - 第三方企业应用不返回该字段。 |
| dept\_id\_list | Number[] | [2,3,4] | 所属部门id列表。 |
| dept\_order\_list | Object[] |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 2 | 部门id。 |
| order | Number | 1 | 员工在部门中的排序。 |
| extension | String | {"爱好":"旅游","年龄":"24"} | 扩展属性，最大长度2000个字符。  **[!NOTE]**     - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启。 - 员工信息面板中添加的拓展字段内有值才返回。 - 第三方企业应用不返回该字段。 |
| hired\_date | Number | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。  **[!NOTE]**     - 第三方企业应用不返回该字段。 - 信息面板中**入职时间**字段内有值才返回该字段。 |
| active | Boolean | true | 是否已激活钉钉：   - **true**：已激活 - **false**：未激活 |
| real\_authed | Boolean | true | 是否已完成实名认证：   - **true**：已认证 - **false**：未认证 |
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
| exclusive\_account | Boolean | true | 是否为企业账号：   - true：是 - false：不是 |
| union\_emp\_ext | Object |  | 当用户来自于关联组织时的关联信息。  **[!NOTE]**  用户所在企业存在关联关系的企业，返回该字段。 |
| userid | String | 500 | 员工的UserId。 |
| union\_emp\_map\_list | Object[] |  | 关联映射关系。 |
| userid | String | 5000 | 关联分支组织中的员工UserId。 |
| corp\_id | String | dingxxx | 关联分支组织的企业CorpId。 |
| corp\_id | String | dingxxx | 当前用户所属的组织的企业CorpId。 |
| exclusive\_account\_type | String | dingtalk | 企业账号类型：   - **sso**：企业自建企业账号 - **dingtalk**：钉钉自建企业账号  **[!NOTE]**  仅企业账号返回该字段。 |
| login\_id | String | login\_id3 | 钉钉自建企业账号的登录名。  **[!NOTE]**  仅归属于本企业的钉钉企业账号号返回该字段。 |
| manager\_userid | String | manager240 | 员工的直属主管。  **[!NOTE]**  员工在企业管理后台个人信息面板中，**直属主管**内有值，才会返回该字段。 |
| org\_email\_type | String | profession | 员工的企业邮箱类型：   - **profession**：标准版 - **base**：基础版 |
| nickname | String | 昵称 | 员工昵称。  **[!NOTE]**  仅归属于本企业的钉钉企业账号返回该字段。 |
| exclusive\_account\_corp\_name | String | 组织名称 | 企业账号归属组织的组织名称。  **[!NOTE]**  仅适用于企业账号，返回创建该企业账号的组织。 |
| exclusive\_account\_corp\_id | String | dingxxx | 企业账号归属组织的组织CorpId。  **[!NOTE]**  仅适用于企业账号，返回创建该企业账号的组织。 |
| disable\_status | Boolean | false | 本组织企业账号的停用状态：   - **true**：停用 - **false**：启用   **[!NOTE]**  仅归属于本企业的钉钉企业账号返回该字段。 |

### **响应体示例**

```
{
  "errcode":"0",
  "result":{
    "exclusive_account_type":"dingtalk",
    "extension":"{\"爱好\":\"旅游\",\"年龄\":\"24\"}",
    "unionid":"z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ",
    "boss":"true",
    "role_list":{
      "group_name":"职务",
      "name":"总监",
      "id":"100"
    },
    "exclusive_account":"true",
    "manager_userid":"manager240",
    "admin":"true",
    "remark":"备注备注",
    "title":"技术总监",
    "hired_date":"1597573616828",
    "userid":"zhangsan",
    "org_email_type":"profession",
    "work_place":"未来park",
    "dept_order_list":{
      "dept_id":"2",
      "order":"1"
    },
    "real_authed":"true",
    "nickname":"昵称",
    "dept_id_list":"[2,3,4]",
    "job_number":"4",
    "email":"test@xxx.com",
    "leader_in_dept":{
      "leader":"true",
      "dept_id":"2"
    },
    "login_id":"login_id3",
    "exclusive_account_corp_name":"组织名称",
    "mobile":"18513027676",
    "active":"true",
    "telephone":"010-86123456-2345",
    "avatar":"xxx",
    "hide_mobile":"false",
    "exclusive_account_corp_id":"dingxxx",
    "senior":"true",
    "org_email":"test@xxx.com",
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
