---
title: "创建钉钉自建企业账号"
source_url: "https://open.dingtalk.com/document/development/create-dingtalk-user-created-dedicated-account"
namespace: "development"
slug: "create-dingtalk-user-created-dedicated-account"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 创建钉钉自建企业账号"
doc_id: "AU7fEEmkyB"
updated_at: "2026-05-27 13:09:03"
---

> Source: https://open.dingtalk.com/document/development/create-dingtalk-user-created-dedicated-account
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 创建钉钉自建企业账号
> Updated: 2026-05-27 13:09:03

# 创建钉钉自建企业账号

调用本接口，创建钉钉自建企业账号用户接口，仅支持购买开通的组织使用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | BE3xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 否 | zhangsan | 员工唯一标识ID（不可修改），长度为1~64个字符。  **[!NOTE]**   - 企业内必须唯一。 - 如果不传，将自动生成一个userId。 |
| exclusive\_account | Boolean | 是 | true | 必须填true，表示要创建企业账号。  **[!NOTE]**  仅适用于企业账号。 |
| exclusive\_account\_type | String | 是 | dingtalk | 必须填dingtalk，表示钉钉自建企业账号。  **[!NOTE]**  仅适用于钉钉自建企业账号。 |
| login\_id | String | 是 | login\_id3 | 钉钉自建企业账号的登录名。  **[!NOTE]**  建议不要携带手机号、邮箱链接等信息，避免注册短信被运营商管控拦截， |
| init\_password | String | 是 | init\_password220 | 钉钉自建企业账号的初始密码，初始密码至少8个字符。  **[!NOTE]**   - 不能全是字母或者数字。 - 建议不要携带手机号、邮箱、链接等信息，避免注册短信被运营商管控拦截， |
| send\_password\_to\_user | Boolean | 否 | false | 发送账密，默认值false：   - **false**：不发送 - **true**：发送   **[!NOTE]**   - 发送时，会通过员工手机号发送短消息或个人邮箱发送电子邮件。 - 该参数为**true**时，`init_password`参数必填，否则不会发送。 |
| name | String | 是 | 张三 | 员工名称，长度最大80个字符。 |
| dept\_id\_list | String | 是 | "2,3,4" | 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。 |
| telephone | String | 否 | 010-86123456-2345 | 分机号，长度最大50个字符。  **[!NOTE]**  分机号是唯一的，企业内不能重复。 |
| job\_number | String | 否 | 4 | 员工工号，长度最大为50个字符。 |
| title | String | 否 | 技术总监 | 职位，长度最大为200个字符。 |
| email | String | 否 | test@xxx.com | 员工个人邮箱，长度最大50个字符。  **[!NOTE]**  员工邮箱是唯一的，企业内不能重复。 |
| org\_email | String | 否 | test@xxx.com | 员工的企业邮箱，长度最大100个字符。  **[!NOTE]**  需满足以下条件，此字段才生效：员工已开通企业邮箱。 |
| org\_email\_type | String | 否 | profession | 员工的企业邮箱类型：   - **profession:** 标准版。 - **base：**基础版。 |
| work\_place | String | 否 | 未来park | 办公地点，长度最大100个字符。 |
| remark | String | 否 | 备注信息 | 备注，长度最大2000个字符。 |
| dept\_order\_list | Object[] | 否 |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| order | Number | 否 | 1 | 员工在部门中的排序，数值越大，排序越靠前。 |
| dept\_title\_list | Object[] | 否 |  | 员工在对应的部门中的职位。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| title | String | 否 | 资深产品经理 | 员工在部门中的职位。 |
| extension | String | 否 | {"爱好":"旅游","年龄":"24"} | 扩展属性，可以设置多种属性，最大长度2000个字符。  **[!NOTE]**   - 手机上最多只能显示10个扩展属性。 - 在使用该参数前，需要先在[钉钉管理后台](https://oa.dingtalk.com/index_new.htm#/setting/contactInfo)增加该属性，然后再调用接口进行赋值，例如，在**通讯录** > **内部通讯录设置** > **通讯录信息**页面，单击**添加自定义字段**按钮。如下图所示，新增字段名称为“爱好”，字段类型为“文本”的自定义字段。爱好 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid，corpid。例如：     ```    {   "爱好":"[爱好](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)"    }   ``` |
| senior\_mode | Boolean | 否 | false | 是否开启高管模式，默认值false。   - **true**：开启。  **[!NOTE]**    - 开启后，手机号码对所有员工隐藏   - 普通员工无法对其发DING、发起钉钉商务电话。   - 高管之间可以发DING、发起钉钉商务电话。 - **false**：不开启。 |
| hired\_date | Number | 否 | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。 |
| manager\_userid | String | 否 | 001 | 直属主管的userId。 |
| exclusive\_mobile | String | 否 | +86-13412341234 | 企业账号手机号。  **[!NOTE]**  仅适用于企业账号。 |
| avatarMediaId | String | 否 | @lALPDfmVUw19YdrNA-jNA-g | 创建本组织企业账号时可指定头像MediaId，只支持jpg/png。  可调用[上传媒体文件](0646-upload-media-files.md)接口获取。  **[!NOTE]**  仅适用于企业账号。 |
| nickname | String | 否 | 昵称 | 创建本组织企业账号时可指定昵称。  **[!NOTE]**  仅适用于企业账号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3e4fcfdc-0d84-4124-9600-9456f89a42ef' \
-d 'exclusive_account_type=dingtalk' \
-d 'login_id=login_id3' \
-d 'extension=%7B%5C%22%E7%88%B1%E5%A5%BD%5C%22%3A%5C%22%E6%97%85%E6%B8%B8%5C%22%2C%5C%22%E5%B9%B4%E9%BE%84%5C%22%3A%5C%2224%5C%22%7D' \
-d 'exclusive_account=true' \
-d 'manager_userid=001' \
-d 'remark=%E5%A4%87%E6%B3%A8%E5%A4%87%E6%B3%A8' \
-d 'telephone=010-86123456-2345' \
-d 'hired_date=1597573616828' \
-d 'title=%E6%8A%80%E6%9C%AF%E6%80%BB%E7%9B%91' \
-d 'org_email_type=profession' \
-d 'userid=zhangsan' \
-d 'avatarMediaId=%40lALPDfmVUw19YdrNA-jNA-g' \
-d 'dept_title_list=null' \
-d 'work_place=%E6%9C%AA%E6%9D%A5park' \
-d 'dept_order_list=null' \
-d 'senior_mode=false' \
-d 'org_email=test%40xxx.com' \
-d 'name=%E5%BC%A0%E4%B8%89' \
-d 'nickname=%E6%98%B5%E7%A7%B0' \
-d 'exclusive_mobile=%2B86-13412341234' \
-d 'dept_id_list=%5C%222%2C3%2C4%5C%22' \
-d 'job_number=4' \
-d 'init_password=init_password220' \
-d 'email=test%40xxx.com'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
req.setUserid("123456789");
req.setExclusiveAccount(true);
req.setExclusiveAccountType("dingtalk");
req.setLoginId("xiaodingding");
req.setInitPassword("12345678dingding");
req.setName("钉钉自建企业账号");
req.setDeptIdList("486882146,609916162");
req.setTelephone("123");
req.setJobNumber("123");
req.setTitle("技术总监");
req.setEmail("test@xxx.com");
req.setOrgEmail("ceshi2");
req.setOrgEmailType("base");
req.setWorkPlace("北京");
req.setRemark("备注信息");
OapiV2UserCreateRequest.DeptOrder deptOrder1 = new OapiV2UserCreateRequest.DeptOrder();
deptOrder1.setDeptId(486882146L);
deptOrder1.setOrder(2L);
OapiV2UserCreateRequest.DeptOrder deptOrder2 = new OapiV2UserCreateRequest.DeptOrder();
deptOrder2.setDeptId(609916162L);
deptOrder2.setOrder(1L);
ArrayList<OapiV2UserCreateRequest.DeptOrder> deptOrderList = new ArrayList<>();
deptOrderList.add(deptOrder1);
deptOrderList.add(deptOrder2);
req.setDeptOrderList(deptOrderList);
OapiV2UserCreateRequest.DeptTitle deptTitle1 = new OapiV2UserCreateRequest.DeptTitle();
deptTitle1.setTitle("测试");
deptTitle1.setDeptId(486882146L);
OapiV2UserCreateRequest.DeptTitle deptTitle2 = new OapiV2UserCreateRequest.DeptTitle();
deptTitle2.setTitle("总监");
deptTitle2.setDeptId(609916162L);
ArrayList<OapiV2UserCreateRequest.DeptTitle> deptTitleList = new ArrayList<>();
deptTitleList.add(deptTitle1);
deptTitleList.add(deptTitle2);
req.setDeptTitleList(deptTitleList);
req.setExtension("{\"爱好\":\"旅游\",\"年龄\":\"24\"}");
req.setSeniorMode(false);
req.setHiredDate(1650351000000l);
req.setManagerUserid("001");
req.setExclusiveMobile("150xxxx");
req.setAvatarMediaId("@lADPDfYH3A-xxxx");
req.setNickname("小钉1");
OapiV2UserCreateResponse rsp = client.execute(req, accessToken);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiV2UserCreateRequest("https://oapi.dingtalk.com/topapi/v2/user/create")

req.userid="zhangsan"
req.name="张三"
req.telephone="010-86123456-2345"
req.job_number="4"
req.title="技术总监"
req.email="test@xxx.com"
req.org_email="test@xxx.com"
req.work_place="未来park"
req.remark="备注备注"
req.dept_id_list=""2,3,4""
req.dept_order_list=""
req.dept_title_list=""
req.extension="{\"爱好\":\"旅游\",\"年龄\":\"24\"}"
req.senior_mode=false
req.hired_date=1597573616828
req.exclusive_account=false
req.exclusive_account_type="dingtalk"
req.login_id="login_id3"
req.init_password="init_password220"
req.org_email_type="profession"
req.manager_userid="001"
req.exclusive_mobile="+86-13412341234"
req.outer_exclusive_corpid="corpid"
req.outer_exclusive_userid="userid"
req.avatarMediaId="@lALPDfmVUw19YdrNA-jNA-g"
req.nickname="昵称"
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
$req = new OapiV2UserCreateRequest;
$req->setUserid("zhangsan");
$req->setExclusiveAccount("true");
$req->setExclusiveAccountType("dingtalk");
$req->setLoginId("login_id3");
$req->setInitPassword("init_password220");
$req->setName("张三");
$req->setDeptIdList("\"2,3,4\"");
$req->setTelephone("010-86123456-2345");
$req->setJobNumber("4");
$req->setTitle("技术总监");
$req->setEmail("test@xxx.com");
$req->setOrgEmail("test@xxx.com");
$req->setWorkPlace("未来park");
$req->setRemark("备注备注");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
req.Userid = "zhangsan";
req.Name = "张三";
req.Mobile = "18513027676";
req.Telephone = "010-86123456-2345";
req.JobNumber = "4";
req.Title = "技术总监";
req.Email = "test@xxx.com";
req.OrgEmail = "test@xxx.com";
req.WorkPlace = "未来park";
req.Remark = "备注备注";
req.DeptIdList = "\"2,3,4\"";
req.ExclusiveAccount = true;
req.ExclusiveAccountType = "dingtalk";
req.LoginId = "login_id3";
req.InitPassword = "init_password220";
req.OrgEmailType = "profession";
req.ManagerUserid = "001";
req.AvatarMediaId = "@lALPDfmVUw19YdrNA-jNA-g";
OapiV2UserCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 错误码。0代表成功。 |
| errmsg | String | ok | 错误信息。 |
| result | Object |  | 返回结果。 |
| userid | String | zhangsan | 员工id。 |
| unionId | String | xxxx | 员工唯一id。 |

### **响应体示例**

```
{
  "errcode":"0",
  "result":{
    "unionId":"xxxx",
    "userid":"zhangsan"
  },
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
