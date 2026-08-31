---
title: "创建用户"
source_url: "https://open.dingtalk.com/document/development/user-information-creation"
namespace: "development"
slug: "user-information-creation"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 创建用户"
doc_id: "wBWOPgQnfQ"
updated_at: "2026-06-30 17:29:32"
---

> Source: https://open.dingtalk.com/document/development/user-information-creation
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 创建用户
> Updated: 2026-06-30 17:29:32

# 创建用户

调用本接口创建新用户。

## **接口调用说明**

调用本接口可以实现创建普通用户或创建企业账号用户。由于在调用时参数使用有较多区别，为便于开发者查看，按照新用户的账号类型进行拆分优化：

- 如果是创建普通用户，接口说明文档请查看本文介绍。
- 如果是创建企业账号用户（仅支持购买开通的组织使用），接口说明文档请参见：

  - [创建SSO企业账号](0104-create-an-sso-account.md)
  - [创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md)
  - [邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md)

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
| userid | String | 否 | zhangsan | 员工唯一标识ID（不可修改），企业内必须唯一。  长度为1~64个字符，如果不传，将自动生成一个userid。 |
| name | String | 是 | 张三 | 员工名称，长度最大80个字符。 |
| mobile | String | 是 | 185xxxx | 手机号码，企业内必须唯一，不可重复。   - 如果是国际号码、中国香港、中国澳门和中国台湾地区号码，请使用+xx-xxxxxx的格式。 - 如果公司注册地址是非中国大陆地区，则在添加用户时，手机号要使用+86-xxxxxx格式。   **[!NOTE]**  登录[钉钉管理后台](https://oa.dingtalk.com)，查看企业注册地址。iShot2022-05-31 15 |
| hide\_mobile | Boolean | 否 | false | 是否号码隐藏：   - **true**：隐藏  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 - **false**：不隐藏 |
| telephone | String | 否 | 010-86123456-2345 | 分机号，长度最大50个字符。  **[!NOTE]**  分机号是唯一的，企业内不能重复。 |
| job\_number | String | 否 | 4 | 员工工号，长度最大为50个字符。 |
| title | String | 否 | 技术总监 | 职位，长度最大为200个字符。 |
| email | String | 否 | test@xxx.com | 员工个人邮箱，长度最大50个字符。  **[!NOTE]**  员工邮箱是唯一的，企业内不能重复。 |
| org\_email | String | 否 | test@xxx.com | 员工的企业邮箱，长度最大100个字符。  **[!NOTE]**  需满足以下条件，此字段才生效：员工的企业邮箱已开通。 |
| org\_email\_type | String | 否 | profession | 员工的企业邮箱类型。   - **profession:** 标准版 - **base：**基础版 |
| work\_place | String | 否 | 未来park | 办公地点，长度最大100个字符。 |
| remark | String | 否 | 备注备注 | 备注，长度最大2000个字符。 |
| dept\_id\_list | String | 是 | "2,3,4" | 所属部门id列表，每次调用最多传100个部门ID。 |
| dept\_order\_list | Object[] | 否 |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| order | Number | 否 | 1 | 员工在部门中的排序。 |
| dept\_title\_list | Object[] | 否 |  | 员工在对应的部门中的职位。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| title | String | 否 | 资深产品经理 | 员工在部门中的职位。 |
| extension | Object | 否 | {"爱好":"旅游","年龄":"24"} | 扩展属性，可以设置多种属性，最大长度2000个字符。  **[!NOTE]**   - 手机上最多只能显示10个扩展属性。 - 在使用该参数前，需要先在[钉钉管理后台](https://oa.dingtalk.com/index_new.htm#/setting/contactInfo)> 内部通讯录设置 > 成员字段管理中增加该属性，然后再调用接口进行赋值。详情请参见下文**关于extension参数的使用**。 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid，corpid。例如： {"爱好":"[爱好](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)"} - **重要提示：**直接添加新属性会覆盖原有属性值，需要先获取现有属性，然后将新属性追加到已有属性上，再进行整体更新。 |
| senior\_mode | Boolean | 否 | false | 是否开启高管模式，默认值false。   - **true**：开启。  **[!NOTE]**    - 开启后，手机号码对所有员工隐藏。   - 普通员工无法对其发DING、发起钉钉商务电话。   - 高管之间可以发DING、发起钉钉商务电话。 - **false**：不开启。 |
| hired\_date | Number | 否 | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。 |
| manager\_userid | String | 否 | 001 | 直属主管的userId。 |
| login\_email | String | 否 | test@xxx.com | 登录邮箱。  **[!NOTE]**  仅适用于邮箱账号，非邮箱账号设置该字段不生效。 |
| dept\_position\_list | DeptPosition[] | 否 |  | 部门内任职信息。 |
| extension\_i18n | Json | 否 | {"爱好":  {"zh\_ CN":  "旅游",  "en\_ US":  "travel",  "aJP":"旅  行"} | 扩展属性的国际化值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1c016742-9383-4276-beb1-ebb375acc454' \
-d 'name=%E5%BC%A0%E4%B8%89' \
-d 'mobile=18513027676' \
-d 'dept_id_list=%5C%222%2C3%2C4%5C%22'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
req.setUserid("002");
req.setName("测试");
req.setSeniorMode(false);
req.setMobile("184806*****");
req.setTitle("教职人员");
req.setEmail("test@xx.com");
req.setOrgEmail("test@xxx.com");
req.setOrgEmailType("profession");
req.setDeptIdList("1");
ArrayList<OapiV2UserCreateRequest.DeptTitle> deptTitles = new ArrayList<>();
OapiV2UserCreateRequest.DeptTitle deptTitle = new OapiV2UserCreateRequest.DeptTitle();
deptTitle.setDeptId(1L);
deptTitle.setTitle("测试");
OapiV2UserCreateRequest.DeptTitle deptTitle1 = new OapiV2UserCreateRequest.DeptTitle();
deptTitle1.setDeptId(1L);
deptTitle1.setTitle("专员");
deptTitles.add(deptTitle);
deptTitles.add(deptTitle1);
req.setDeptTitleList(deptTitles);
req.setHideMobile(false);
req.setTelephone("010-8xxxxx6-2345");
req.setJobNumber("100828");
req.setHiredDate(1615219200000L);
req.setWorkPlace("未来park");
req.setRemark("备注备注");
List<OapiV2UserCreateRequest.DeptOrder> deptOrderList = new ArrayList<OapiV2UserCreateRequest.DeptOrder>();
OapiV2UserCreateRequest.DeptOrder deptOrder = new OapiV2UserCreateRequest.DeptOrder();
deptOrder.setDeptId(1L);
deptOrder.setOrder(1L);
OapiV2UserCreateRequest.DeptOrder deptOrder1 = new OapiV2UserCreateRequest.DeptOrder();
deptOrder1.setDeptId(1L);
deptOrder1.setOrder(1L);
deptOrderList.add(deptOrder);
deptOrderList.add(deptOrder1);
req.setDeptOrderList(deptOrderList);
req.setExtension("{\"爱好\":\"[爱好](http://test.com?userid=#userid#&corpid=#corpid#)\"}");
req.setManagerUserid("001");
req.setLoginEmail("test@xxx.com");
OapiV2UserCreateResponse rsp = client.execute(req, "");
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserCreateRequest("https://oapi.dingtalk.com/topapi/v2/user/create")

req.userid="zhangsan"
req.name="张三"
req.mobile="18513027676"
req.job_number="4"
req.title="技术总监"
req.email="test@xxx.com"
req.org_email="test@xxx.com"
req.work_place="未来park"
req.remark="备注备注"
req.dept_id_list="2,3,4"
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
$req->setTelephone("010-86123456-2345");
$req->setTitle("技术总监");
$req->setEmail("test@xxx.com");
$req->setWorkPlace("未来park");
$req->setRemark("备注备注");
$req->setDeptIdList("\"2,3,4\"");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
req.Userid = "zhangsan";
req.Name = "张三";
req.Mobile = "18513027676";
req.Title = "技术总监";
req.Email = "test@xxx.com";
req.OrgEmail = "test@xxx.com";
req.WorkPlace = "未来park";
req.Remark = "备注备注";
req.DeptIdList = "\"2,3,4\"";
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

## extension参数说明

如果想要展示扩展字段**extension**中设置的用户属性，您还需要完成以下操作。

1. 登录[钉钉管理后台](https://login.dingtalk.com/)**。**
2. 单击内部通讯录设置，然后单击**成员字段管理** > **添加自定义字段**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8379572961/p709664.png)
