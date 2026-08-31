---
title: "更新用户信息"
source_url: "https://open.dingtalk.com/document/development/user-information-update"
namespace: "development"
slug: "user-information-update"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 更新用户信息"
doc_id: "ECZ9YgDoW3"
updated_at: "2026-06-08 09:28:29"
---

> Source: https://open.dingtalk.com/document/development/user-information-update
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 更新用户信息
> Updated: 2026-06-08 09:28:29

# 更新用户信息

调用本接口更新指定的用户信息。

## **接口调用说明**

调用本接口可以实现更新普通账号用户信息或更新企业账号用户信息。由于在调用时参数使用有较多区别，为便于开发者查看，按照新用户的账号类型进行拆分优化：

- 更新普通用户信息，接口说明文档请查看本文介绍。
- 更新企业账号用户信息，接口说明文档请参见[更新企业账号用户信息](0107-update-dedicated-accounts-information.md)。

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
| hide\_mobile | Boolean | 否 | false | 是否号码隐藏：   - **true**：隐藏  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 - **false**：不隐藏 |
| telephone | String | 否 | 010-86123456-2345 | 分机号，长度最大50个字符。  **[!NOTE]**  分机号是唯一的，企业内不能重复。 |
| job\_number | String | 否 | 4 | 员工工号，长度最大50个字符。 |
| manager\_userid | String | 否 | 0001 | 直属主管的userId。 |
| title | String | 否 | 技术总监 | 职位，长度最大200个字符。 |
| email | String | 否 | test@xxx.com | 员工邮箱，长度最大50个字符。  **[!NOTE]**  员工邮箱是唯一的，企业内不能重复。 |
| org\_email | String | 否 | test@xxx.com | 员工的企业邮箱。  **[!NOTE]**  需满足以下条件，此字段才生效：员工的企业邮箱已开通。 |
| work\_place | String | 否 | 未来park | 办公地点，长度最大100个字符。 |
| remark | String | 否 | 备注信息 | 备注，长度最大2000个字符。 |
| dept\_id\_list | String | 否 | "2,3,4" | 所属部门ID列表。 |
| dept\_order\_list | DeptOrder[] | 否 |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| order | Number | 否 | 1 | 员工在部门中的排序。数值越大，排序越靠前。 |
| extension | String | 否 | {"爱好":"旅游","年龄":"24"} | 扩展属性，长度最大2000个字符。  **[!NOTE]**   - 手机上最多只能显示10个扩展属性。 - 如果给员工设置有10个扩展属性字段，更新时即使扩展属性字段值没变，也必须要将10个扩展属性字段都传进去。如果只传其中1个，那么剩下9个字段都会被清空。 - 在使用该参数前，需要先在[**钉钉管理后台**](https://oa.dingtalk.com/index.htm#/setting#setOrgInfo) > **通讯录** > **内部通讯录设置** > **成员字段管理**增加该属性。 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid和corpid。示例： `[工位地址](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)`。 |
| ext\_attrs\_update\_mode | Number | 否 | 1 | 拓展属性自定义字段更新模式：   - 0：覆盖方式 - 1：追加方式   默认是覆盖。 |
| senior\_mode | Boolean | 否 | false | 是否开启高管模式，默认值false。   - **true**：开启。  **[!NOTE]**      - 开启后，手机号码对所有员工隐藏。   - 普通员工无法对其发DING、发起钉钉商务电话。   - 高管之间可以发DING、发起钉钉商务电话。 - **false**：不开启。 |
| hired\_date | Number | 否 | 1597573616828 | 入职时间，UNIX时间戳，单位毫秒。 |
| language | String | 否 | zh\_CN | 通讯录语言，取值。   - **zh\_CN**：中文（默认值）。 - **en\_US**：英文。 |
| force\_update\_fields | String | 否 | manager\_userid | 强制更新的字段，支持清空指定的字段，多个字段之间使用逗号分隔。目前支持字段: `manager_userid`。 |
| dept\_position\_list | DeptPosition[] | 否 |  | 部门内任职信息。 |
| extension\_i18n | Json | 否 | {"爱好":  {"zh\_ CN":  "旅游",  "en\_ US":  "travel",  "aJP":"旅  行"} | 扩展属性的国际化值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c6c3c34d-23dd-4da7-9901-0af1ebceaf80' \
-d 'name=%E5%BC%A0%E4%B8%89' \
-d 'telephone=010-86123456-2345' \
-d 'hide_mobile=false' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/update");
OapiV2UserUpdateRequest req = new OapiV2UserUpdateRequest();
req.setUserid("zhangsan");
req.setName("张三");
req.setHideMobile(false);
req.setTelephone("010-86123456-2345");
req.setJobNumber("4");
req.setManagerUserid("0001");
req.setTitle("技术总监");
req.setEmail("test@xxx.com");
req.setOrgEmail("test@xxx.com");
req.setWorkPlace("未来park");
req.setRemark("备注备注");
req.setDeptIdList("2,3,4");
List<DeptOrder> list2 = new ArrayList<DeptOrder>();
DeptOrder obj3 = new DeptOrder();
list2.add(obj3);
obj3.setDeptId(2L);
obj3.setOrder(1L);
req.setDeptOrderList(list2);
req.setExtension("{\"爱好\":\"旅游\",\"年龄\":\"24\"}");
req.setSeniorMode(false);
req.setHiredDate(1597573616828L);
req.setLanguage("zh_CN");
req.setForceUpdateFields("manager_userid");
OapiV2UserUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserUpdateRequest("https://oapi.dingtalk.com/topapi/v2/user/update")

req.userid="zhangsan"
req.name="张三"
req.hide_mobile=false
req.telephone="010-86123456-2345"

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
$req->setHideMobile("false");
$req->setTelephone("010-86123456-2345");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/update");
OapiV2UserUpdateRequest req = new OapiV2UserUpdateRequest();
req.Userid = "zhangsan";
req.Name = "张三";
req.Mobile = "18513027676";
req.HideMobile = false;
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
  "errcode": 0,
  "request_id": "55o5i31j4cg8"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
