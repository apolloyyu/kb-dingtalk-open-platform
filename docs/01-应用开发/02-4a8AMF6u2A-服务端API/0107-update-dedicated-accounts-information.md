---
title: "更新企业账号用户信息"
source_url: "https://open.dingtalk.com/document/development/update-dedicated-accounts-information"
namespace: "development"
slug: "update-dedicated-accounts-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 企业账号 > 更新企业账号用户信息"
doc_id: "XT62t9idMV"
updated_at: "2026-05-27 13:09:06"
---

> Source: https://open.dingtalk.com/document/development/update-dedicated-accounts-information
> Path: 应用开发 / 服务端API / 通讯录管理 > 企业账号 > 更新企业账号用户信息
> Updated: 2026-05-27 13:09:06

# 更新企业账号用户信息

调用本接口，更新指定的企业账号用户信息，仅支持购买开通企业账号的组织使用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3Fxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user123 | 员工的userId。 |
| name | String | 否 | 张三 | 员工名称，长度最大80个字符。 |
| hide\_mobile | Boolean | 否 | false | 是否号码隐藏：   - **true**：隐藏  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉商务电话。 - **false**：不隐藏 |
| telephone | String | 否 | 010-86123456-2345 | 分机号，长度最大50个字符。  **[!NOTE]**  分机号是唯一的，企业内不能重复。 |
| job\_number | String | 否 | 4 | 员工工号，长度最大50个字符。 |
| manager\_userid | String | 否 | 0001 | 直属主管的userId。 |
| title | String | 否 | 技术总监 | 职位，长度最大200个字符。 |
| email | String | 否 | test@xxx.com | 员工邮箱，长度最大50个字符。  **[!NOTE]**  员工邮箱是唯一的，企业内不能重复。 |
| org\_email | String | 否 | test@xxx.com | 员工的企业邮箱。  **[!NOTE]**  需满足以下条件，此字段才生效：员工的企业邮箱已开通。 |
| work\_place | String | 否 | 未来park | 办公地点，长度最大100个字符。 |
| remark | String | 否 | 备注信息 | 备注，长度最大2000个字符。 |
| dept\_id\_list | String | 是 | "2,3,4" | 所属部门ID列表。 |
| dept\_order\_list | DeptOrder[] | 否 |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| order | Number | 否 | 1 | 员工在部门中的排序。 |
| dept\_title\_list | DeptTitle[] | 否 |  | 员工在对应的部门中的职位。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| title | String | 否 | 资深产品经理 | 员工在部门中的职位。 |
| extension | String | 否 | {"爱好":"旅游","年龄":"24"} | 扩展属性，长度最大2000个字符。  **[!NOTE]**     - 手机上最多只能显示10个扩展属性。 - 如果给员工设置有10个扩展属性字段，更新时即使扩展属性字段值没变，也必须要将10个扩展属性字段都传进去。如果只传其中1个，那么剩下9个字段都会被清空。 - 在使用该参数前，需要先在[**钉钉管理后台**](https://oa.dingtalk.com/index.htm#/setting#setOrgInfo) > **设置** > **通讯录信息**增加该属性。 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid和corpid。示例： `[工位地址](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)`。 |
| ext\_attrs\_update\_mode | Number | 否 | 1 | 拓展属性自定义字段更新模式：   - 0：覆盖方式 - 1：追加方式   默认是覆盖。 |
| senior\_mode | Boolean | 否 | false | 是否开启高管模式，默认值false。   - **true**：开启。  **[!NOTE]**      - 开启后，手机号码对所有员工隐藏。   - 普通员工无法对其发DING、发起钉钉商务电话。   - 高管之间可以发DING、发起钉钉商务电话。 - **false**：不开启。 |
| hired\_date | Number | 否 | 1597573616828 | 入职时间，UNIX时间戳，单位毫秒。 |
| language | String | 否 | zh\_CN | 通讯录语言，取值。   - **zh\_CN**：中文（默认值）。 - **en\_US**：英文。 |
| force\_update\_fields | String | 否 | manager\_userid | 强制更新的字段，支持清空指定的字段，多个字段之间使用逗号分隔。目前支持字段: `manager_userid`、`org_email`。  **[!NOTE]**   - 若强制更新字段中包含 org\_email 且传参中 org\_email 字段为空，则将解除员工与企业邮箱的绑定关系，并对企业邮箱账号进行冻结或删除操作。 - 若强制更新字段中包含 org\_email 且员工已绑定了其他企业邮箱，则将解除员工与原企业邮箱的绑定关系，对原企业邮箱账号进行冻结或删除操作，并建立员工与新企业邮箱的绑定关系。 - 若强制更新字段中包含 org\_email 且对应的邮箱账号为公共邮箱或服务邮箱，则将邮箱类型转换为普通邮箱，并建立员工与企业邮箱的绑定关系。 |
| org\_email\_type | String | 否 | profession | 企业账号员工的企业邮箱类型。   - profession: 标准版 - base: 基础版 |
| loginId | String | 否 | loginId123 | 钉钉企业账号的登录名，仅支持钉钉企业账号更新该字段，SSO企业账号暂不支持。  **[!NOTE]**  建议不要携带手机号、邮箱、链接等联系信息，避免短信被运营商管控拦截。 |
| init\_password | String | 否 | init\_password220 | 钉钉企业账号的初始密码，初始密码至少8个字符。  **[!NOTE]**   - 不能全是字母或者数字。 - 仅支持钉钉企业账号更新该字段，SSO企业账号暂不支持 - 建议不要携带手机号、邮箱、链接等联系信息，避免短信被运营商管控拦截。 |
| send\_password\_to\_user | Boolean | 否 | false | 发送账密，默认值false：   - **false**：不发送 - **true**：发送   **[!NOTE]**   - 该参数为**true**时，`init_password`参数必填，否则不会发送。 - 发送时，会通过员工手机号发送短消息或个人邮箱发送电子邮件。 - 仅支持钉钉企业账号设置该字段，SSO企业账号暂不支持。 |
| exclusive\_mobile | String | 否 | 150xxxxxxx | 企业账号手机号。 |
| avatarMediaId | String | 否 | @lALPDfmVUw19YdrNA-jNA-g | 更新本组织企业账号时可指定头像MediaId，只支持jpg/png格式，可调用[上传媒体文件](https://open.dingtalk.com/document/orgapp/upload-media-files)接口获取。  **[!NOTE]**  支持自建企业账号和 SSO 企业账号 |
| nickname | String | 否 | 昵称 | 企业账号的昵称。  **[!NOTE]**  支持自建企业账号和 SSO 企业账号 |
| dept\_position\_list | DeptPosition[] | 否 |  | 部门内任职信息。 |
| extension\_i18n | Json | 否 | {"爱好":  {"zh\_ CN":  "旅游",  "en\_ US":  "travel",  "aJP":"旅  行"} | 扩展属性的国际化值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9321cd22-5087-4456-969a-190ad398e925' \
-d 'userid=zhangsan' \
-d 'name=%E5%BC%A0%E4%B8%89' \
-d 'mobile=1851xxxx676' \
-d 'hide_mobile=false' \
-d 'telephone=010-86123456-2345' \
-d 'job_number=4' \
-d 'title=%E6%8A%80%E6%9C%AF%E6%80%BB%E7%9B%91' \
-d 'email=test%40xxx.com'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/update");
OapiV2UserUpdateRequest req = new OapiV2UserUpdateRequest();
req.setUserid("user001");
req.setName("小钉dingtalk");
req.setHideMobile(true);
req.setTelephone("456");
req.setJobNumber("456");
req.setManagerUserid("001");
req.setTitle("title");
req.setEmail("xxx@xxx.com");
req.setOrgEmail("1111");
req.setWorkPlace("北京");
req.setRemark("备注");
req.setDeptIdList("486882146,609916162");
List<OapiV2UserUpdateRequest.DeptOrder> deptOrderList = new ArrayList<OapiV2UserUpdateRequest.DeptOrder>();
OapiV2UserUpdateRequest.DeptOrder deptOrder1 = new OapiV2UserUpdateRequest.DeptOrder();
deptOrder1.setDeptId(486882146l);
deptOrder1.setOrder(1L);
OapiV2UserUpdateRequest.DeptOrder deptOrder2 = new OapiV2UserUpdateRequest.DeptOrder();
deptOrder2.setDeptId(609916162l);
deptOrder2.setOrder(1L);
deptOrderList.add(deptOrder1);
deptOrderList.add(deptOrder2);
req.setDeptOrderList(deptOrderList);
List<OapiV2UserUpdateRequest.DeptTitle> deptTitleList = new ArrayList<OapiV2UserUpdateRequest.DeptTitle>();
OapiV2UserUpdateRequest.DeptTitle deptTitle1 = new OapiV2UserUpdateRequest.DeptTitle();
deptTitle1.setDeptId(486882146l);
deptTitle1.setTitle("资深产品经理");
OapiV2UserUpdateRequest.DeptTitle deptTitle2 = new OapiV2UserUpdateRequest.DeptTitle();
deptTitle2.setDeptId(609916162l);
deptTitle2.setTitle("资深产品经理");
deptTitleList.add(deptTitle1);
deptTitleList.add(deptTitle2);
req.setDeptTitleList(deptTitleList);
req.setExtension("{\"爱好\":\"旅游\",\"年龄\":\"24\"}");
req.setSeniorMode(false);
req.setHiredDate(1650351000000l);
req.setForceUpdateFields("manager_userid");
req.setLanguage("zh_CN");
req.setOrgEmailType("profession");
req.setLoginId("test");
req.setExclusiveMobile("183xxxx");
req.setAvatarMediaId("@lADPDfYH3A-xxxx");
req.setNickname("测试");
OapiV2UserUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiV2UserUpdateRequest("https://oapi.dingtalk.com/topapi/v2/user/update")

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
req.language="zh_CN"
req.init_password="Password123"
req.loginId="loginId123"
req.dept_position_list="[2,"资深产品经理",true,"未来park","100",{},{}]"
req.org_email_type="profession"
req.force_update_fields="manager_userid"
req.manager_userid="0001"
req.exclusive_mobile="+86-19812341234"
req.exclusive_mobile_verify_status="verified/notVerified"
req.nickname="昵称"
req.avatarMediaId="@lALPDfmVUw19YdrNA-jNA-g"
req.ext_attrs_update_mode=0
req.ext_attrs="["emp:xxx",{"images":["https://img.alicdn.com/imgextra/i2/O1CN01IVwD5w1mqnRxmUBng_!!6000000005006-2-tps-64-64.png"],"text":"点击前往钉钉官网","url":"www.dingtalk.com"}]"
req.gender="F"
req.limited=false
req.has_subordinate=false
req.dept_name="部门1-部门11-部门111"
req.flower_name="花名"
req.send_password_to_user=false
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
$req = new OapiV2UserUpdateRequest;
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
$req->setLanguage("zh_CN");
$req->setInitPassword("Password123");
$req->setLoginId("loginId123");
$dept_position_list = new DeptPosition;
$req->setDeptPositionList(array($dept_position_list));
$req->setOrgEmailType("profession");
$req->setForceUpdateFields("manager_userid");
$req->setManagerUserid("0001");
$req->setExclusiveMobile("+86-19812341234");
$req->setExclusiveMobileVerifyStatus("verified/notVerified");
$req->setNickname("昵称");
$req->setAvatarMediaId("@lALPDfmVUw19YdrNA-jNA-g");
$req->setExtAttrsUpdateMode("0");
$ext_attrs = new EmpExtAttr;
$req->setExtAttrs(array($ext_attrs));
$req->setGender("F");
$req->setLimited("false");
$req->setHasSubordinate("false");
$req->setDeptName("部门1-部门11-部门111");
$req->setFlowerName("花名");
$req->setSendPasswordToUser("false");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/update");
OapiV2UserUpdateRequest req = new OapiV2UserUpdateRequest();
req.Userid = "zhangsan";
req.Name = "张三";
req.Mobile = "185xxxx676";
req.HideMobile = false;
req.Telephone = "010-86123456-2345";
req.JobNumber = "4";
req.Title = "技术总监";
req.Email = "test@xxx.com";
req.OrgEmail = "test@xxx.com";
req.WorkPlace = "未来park";
req.Remark = "备注备注";
req.DeptIdList = "\"2,3,4\"";
OapiV2UserUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码，0代表成功。 |
| errmsg | String | 找不到该用户 | 调用失败时返回的错误信息。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "request_id":"55o5i31j4cg8"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
