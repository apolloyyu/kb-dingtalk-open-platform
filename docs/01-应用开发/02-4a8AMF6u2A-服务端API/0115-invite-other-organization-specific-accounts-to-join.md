---
title: "邀请其他组织企业账号加入"
source_url: "https://open.dingtalk.com/document/development/invite-other-organization-specific-accounts-to-join"
namespace: "development"
slug: "invite-other-organization-specific-accounts-to-join"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 企业账号 > 邀请其他组织企业账号加入"
doc_id: "sHc62E5rcu"
updated_at: "2026-05-27 13:09:04"
---

> Source: https://open.dingtalk.com/document/development/invite-other-organization-specific-accounts-to-join
> Path: 应用开发 / 服务端API / 通讯录管理 > 企业账号 > 邀请其他组织企业账号加入
> Updated: 2026-05-27 13:09:04

# 邀请其他组织企业账号加入

调用本接口加入其他组织企业账号进入本组织。

## 接口调用说明

加入其他组织企业账号进入本组织，仅支持购买开通的组织使用。

调用本接口加入其他组织企业账号进入本组织，需要注意如下事项：

1. 本接口不支持加入其他企业的非企业账号。
2. 需要其他企业调用接口【[授权企业账号可加入多组织](0114-authorize-a-dedicated-account-to-join-multiple-organizations.md)】授权其他企业的企业账号加入本组织。 授权完成后，表示其他企业允许本企业将其他企业的企业账号加入到本企业。
3. 本接口调用成功后，其他企业的企业账号直接进入本组织，不需要其他企业的企业账号确认同意（完成第二项授权后，表示其他企业已同意，不需要账号维度的再次同意）。

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
| access\_token | String | 是 | BE3xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 否 | zhangsan | 员工唯一标识ID（不可修改），长度为1~64个字符。  **[!NOTE]**   - 企业内必须唯一。 - 如果不传，将自动生成一个userid。 |
| outer\_exclusive\_corpid | String | 是 | ding12345 | 需要添加的企业账号所属的corpId。 |
| outer\_exclusive\_userid | String | 是 | user01 | 需要添加的企业账号所属的userId。 |
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
| extension | String | 否 | {"爱好":"旅游","年龄":"24"} | 扩展属性，可以设置多种属性，最大长度2000个字符。  **[!NOTE]**   - 手机上最多只能显示10个扩展属性。 - 在使用该参数前，需要先在[钉钉管理后台](https://oa.dingtalk.com/index_new.htm#/setting/contactInfo)增加该属性，然后再调用接口进行赋值，例如，在**通讯录** > **内部通讯录设置** > **通讯录信息**页面，单击**添加自定义字段**按钮。如下图所示，新增字段名称为“爱好”，字段类型为“文本”的自定义字段。爱好 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid，corpid。例如： {"爱好":"[爱好](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)"} |
| senior\_mode | Boolean | 否 | false | 是否开启高管模式，默认值false。   - **true**：开启。  **[!NOTE]**    - 开启后，手机号码对所有员工隐藏。   - 普通员工无法对其发DING、发起钉钉商务电话。   - 高管之间可以发DING、发起钉钉商务电话。 - **false**：不开启。 |
| hired\_date | Number | 否 | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。 |
| manager\_userid | String | 否 | 001 | 直属主管的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/create" \
  -H 'Content-Type: application/x-www-form-urlencoded;charset=utf-8' \
  -d 'access_token=YOUR_ACCESS_TOKEN' \
  -d 'outer_exclusive_corpid=ding12345' \
  -d 'outer_exclusive_userid=user01' \
  -d 'name=张三' \
  -d 'dept_id_list=2,3,4' \
  -d 'userid=zhangsan' \
  -d 'telephone=010-86123456-2345' \
  -d 'job_number=4' \
  -d 'title=技术总监' \
  -d 'email=test@xxx.com' \
  -d 'work_place=未来park' \
  -d 'remark=备注信息'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
req.setUserid("zhangsan");
req.setName("张三");
req.setMobile("18513027676");
req.setHideMobile(false);
req.setTelephone("010-86123456-2345");
req.setJobNumber("4");
req.setTitle("技术总监");
req.setEmail("test@xxx.com");
req.setOrgEmail("test@xxx.com");
req.setWorkPlace("未来park");
req.setRemark("备注备注");
req.setDeptIdList("2,3,4");
List<DeptOrder> list2 = new ArrayList<DeptOrder>();
DeptOrder obj3 = new DeptOrder();
list2.add(obj3);
req.setDeptOrderList(list2);
List<DeptTitle> list5 = new ArrayList<DeptTitle>();
DeptTitle obj6 = new DeptTitle();
list5.add(obj6);
req.setDeptTitleList(list5);
req.setSeniorMode(false);
req.setHiredDate(1597573616828L);
req.setLoginEmail("test@xxx.com");
req.setExclusiveAccount(false);
req.setExclusiveAccountType("dingtalk");
req.setLoginId("login_id3");
req.setInitPassword("init_password220");
List<DeptPosition> list8 = new ArrayList<DeptPosition>();
DeptPosition obj9 = new DeptPosition();
list8.add(obj9);
req.setDeptPositionList(list8);
req.setOrgEmailType("profession");
req.setManagerUserid("001");
req.setExclusiveMobile("+86-13412341234");
req.setExclusiveMobileVerifyStatus("verified/notVerified");
req.setOuterExclusiveCorpid("corpid");
req.setOuterExclusiveUserid("userid");
req.setAvatarMediaId("@lALPDfmVUw19YdrNA-jNA-g");
req.setNickname("昵称");
req.setExtAttrsUpdateMode(0L);
List<EmpExtAttr> list11 = new ArrayList<EmpExtAttr>();
EmpExtAttr obj12 = new EmpExtAttr();
list11.add(obj12);
req.setExtAttrs(list11);
req.setGender("F/M/none");
req.setLimited(false);
req.setHasSubordinate(false);
req.setDeptName("部门1-部门11-部门111");
req.setFlowerName("花名");
req.setSendPasswordToUser(false);
req.setCheckUserProtect(true);
OapiV2UserCreateResponse rsp = client.execute(req, "");
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiV2UserCreateRequest("https://oapi.dingtalk.com/topapi/v2/user/create")

req.userid="zhangsan"
req.name="张三"
req.mobile="18513027676"
req.hide_mobile=false
req.telephone="010-86123456-2345"
req.job_number="4"
req.title="技术总监"
req.email="test@xxx.com"
req.org_email="test@xxx.com"
req.work_place="未来park"
req.remark="备注备注"
req.dept_id_list="2,3,4"
req.dept_order_list="[2,1]"
req.dept_title_list="[2,"资深产品经理"]"
req.senior_mode=false
req.hired_date=1597573616828
req.login_email="test@xxx.com"
req.exclusive_account=false
req.exclusive_account_type="dingtalk"
req.login_id="login_id3"
req.init_password="init_password220"
req.dept_position_list="[true,"未来park","资深产品经理",2,"100"]"
req.org_email_type="profession"
req.manager_userid="001"
req.exclusive_mobile="+86-13412341234"
req.exclusive_mobile_verify_status="verified/notVerified"
req.outer_exclusive_corpid="corpid"
req.outer_exclusive_userid="userid"
req.avatarMediaId="@lALPDfmVUw19YdrNA-jNA-g"
req.nickname="昵称"
req.ext_attrs_update_mode=0
req.ext_attrs="["emp:xxx",{"images":["https://img.alicdn.com/imgextra/i2/O1CN01IVwD5w1mqnRxmUBng_!!6000000005006-2-tps-64-64.png"],"text":"点击前往钉钉官网","url":"www.dingtalk.com"}]"
req.gender="F/M/none"
req.limited=false
req.has_subordinate=false
req.dept_name="部门1-部门11-部门111"
req.flower_name="花名"
req.send_password_to_user=false
req.check_user_protect=true
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
$req->setName("张三");
$req->setMobile("18513027676");
$req->setHideMobile("false");
$req->setTelephone("010-86123456-2345");
$req->setJobNumber("4");
$req->setTitle("技术总监");
$req->setEmail("test@xxx.com");
$req->setOrgEmail("test@xxx.com");
$req->setWorkPlace("未来park");
$req->setRemark("备注备注");
$req->setDeptIdList("2,3,4");
$dept_order_list = new DeptOrder;
$req->setDeptOrderList(array($dept_order_list));
$dept_title_list = new DeptTitle;
$req->setDeptTitleList(array($dept_title_list));
$req->setSeniorMode("false");
$req->setHiredDate("1597573616828");
$req->setLoginEmail("test@xxx.com");
$req->setExclusiveAccount("false");
$req->setExclusiveAccountType("dingtalk");
$req->setLoginId("login_id3");
$req->setInitPassword("init_password220");
$dept_position_list = new DeptPosition;
$req->setDeptPositionList(array($dept_position_list));
$req->setOrgEmailType("profession");
$req->setManagerUserid("001");
$req->setExclusiveMobile("+86-13412341234");
$req->setExclusiveMobileVerifyStatus("verified/notVerified");
$req->setOuterExclusiveCorpid("corpid");
$req->setOuterExclusiveUserid("userid");
$req->setAvatarMediaId("@lALPDfmVUw19YdrNA-jNA-g");
$req->setNickname("昵称");
$req->setExtAttrsUpdateMode("0");
$ext_attrs = new EmpExtAttr;
$req->setExtAttrs(array($ext_attrs));
$req->setGender("F/M/none");
$req->setLimited("false");
$req->setHasSubordinate("false");
$req->setDeptName("部门1-部门11-部门111");
$req->setFlowerName("花名");
$req->setSendPasswordToUser("false");
$req->setCheckUserProtect("true");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
req.OuterExclusiveCorpid = "ding12345"; 
req.OuterExclusiveUserid = "user01";  
req.Name = "张三"; 
req.DeptIdList = "2,3,4"; 
req.Userid = "zhangsan"; 
req.Telephone = "010-86123456-2345";
req.JobNumber = "4"; 
req.Title = "技术总监";  
req.Email = "test@xxx.com";  
req.OrgEmail = "test@xxx.com"; 
req.OrgEmailType = "profession";
req.WorkPlace = "未来park"; 
req.Remark = "备注信息"; 
List<OapiV2UserCreateRequest.DeptOrderDomain> deptOrderList = new List<OapiV2UserCreateRequest.DeptOrderDomain>();
OapiV2UserCreateRequest.DeptOrderDomain orderObj = new OapiV2UserCreateRequest.DeptOrderDomain();
orderObj.DeptId = 2L;
orderObj.Order = 1L;
deptOrderList.Add(orderObj);
req.DeptOrderList_ = deptOrderList;
List<OapiV2UserCreateRequest.DeptTitleDomain> deptTitleList = new List<OapiV2UserCreateRequest.DeptTitleDomain>();
OapiV2UserCreateRequest.DeptTitleDomain titleObj = new OapiV2UserCreateRequest.DeptTitleDomain();
titleObj.DeptId = 2L;
titleObj.Title = "资深产品经理";
deptTitleList.Add(titleObj);
req.DeptTitleList_ = deptTitleList;
req.Extension = "{\"爱好\":\"旅游\",\"年龄\":\"24\"}"; 
req.SeniorMode = false;  
req.HiredDate = 1597573616828L;    
req.ManagerUserid = "001";             
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
| userid | String | zhangsan | 员工userId。 |
| unionId | String | xxxx | 员工unionId。 |

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
