---
title: "服务号菜单更新"
source_url: "https://open.dingtalk.com/document/development/service-number-menu-update"
namespace: "development"
slug: "service-number-menu-update"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 菜单管理 > 服务号菜单更新"
doc_id: "bt4AXxlQCm"
updated_at: "2026-06-01 09:15:49"
---

> Source: https://open.dingtalk.com/document/development/service-number-menu-update
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 菜单管理 > 服务号菜单更新
> Updated: 2026-06-01 09:15:49

# 服务号菜单更新

调用本接口更新服务号的会话菜单。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/serviceaccount/menu/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_menu-服务号菜单管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| menu | MenuConfigDTO | 否 |  | 菜单。 |
| button | MenuButtonDTO[] | 否 |  | 菜单按钮列表。 |
| name | String | 是 | 今日天气 | 菜单名称。 |
| type | String | 否 | view | 菜单类型，如果是 一级菜单则不填，代表这是一个父菜单：   - **click**：拉取自定义消息 - **view**：跳转链接 - **media\_id**：拉取站内消息，包括消息卡片和图片  **[!NOTE]**  配合media\_id字段使用，填写卡片id或图片id。 - **view\_article**：跳转站内文章  **[!NOTE]**  配合media\_id字段使用，填写为相应的文章id。 |
| key | String | 否 | KEY\_WEATHER | 菜单绑定的key值，用于点击菜单拉取自定义消息的场景。 |
| url | String | 否 | https://www.taobao.com | 菜单绑定的URL，用于链接跳转。 |
| media\_id | String | 否 | mvFiiRhuwt5IiE | 素材id，用于拉取站内消息的场景。  **[!NOTE]**  如果菜单类型为media\_id或view\_article类型，则该字符为必填项。 |
| sub\_button | MenuSubButtonDTO[] | 否 |  | 子菜单按钮列表。 |
| name | String | 是 | 杭州天气 | 按钮名称。 |
| type | String | 是 | click | 按钮类型：   - **click**：拉取自定义消息 - **view**：跳转链接 - **media\_id**：拉取站内消息，包括消息卡片和图片  **[!NOTE]**  配合media\_id字段使用，填写卡片id或图片id。 - **view\_article**：跳转站内文章  **[!NOTE]**  配合media\_id字段使用，填写为相应的文章id。   其中media\_id类型会在内部转化为click类型，view\_article类型会在内部转化为view类型。 |
| key | String | 否 | WEATHER\_HANGZHOU | 子菜单绑定的key值。 |
| url | String | 否 | https://www.taobao.com | 子菜单绑定的URL。 |
| media\_id | String | 否 | mvFiiRhuwt5IiE | 子菜单素材id。  **[!NOTE]**  如果子菜单类型为media\_id或view\_article类型，则该参数为必填项。 |
| enable\_input | Boolean | 是 | false | 是否允许用户输入：   - **true**：允许 - **false**：不允许 |
| status | Number | 是 | 0 | 状态：   - **0**：正常 - **1**：停用 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/serviceaccount/menu/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=5fd8dxxxx9e5ce3' \
-d 'menu=null' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
 DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/menu/update");
 OapiServiceaccountMenuUpdateRequest req = new OapiServiceaccountMenuUpdateRequest();
 req.setUnionid("IlrIsTHaiSYXluZP61h0zxgiEiE");
 MenuConfigDTO menuConfigDTO = new MenuConfigDTO();
 List<MenuButtonDTO> menuButtonDTOs = new ArrayList<MenuButtonDTO>();
 MenuButtonDTO menuButtonDTO = new MenuButtonDTO();
 menuButtonDTOs.add(menuButtonDTO);
 menuButtonDTO.setName("今日天气");
 menuButtonDTO.setType("view");
 menuButtonDTO.setKey("KEY_WEATHER");
 menuButtonDTO.setUrl("https://www.taobao.com");
 menuButtonDTO.setMediaId("mvFiiRhuwt5IiE");
 List<MenuSubButtonDTO> menuSubButtonDTOs = new ArrayList<MenuSubButtonDTO>();
 MenuSubButtonDTO menuSubButtonDTO = new MenuSubButtonDTO();
 menuSubButtonDTOs.add(menuSubButtonDTO);
 menuSubButtonDTO.setName("杭州天气");
 menuSubButtonDTO.setType("click");
 menuSubButtonDTO.setKey("WEATHER_HANGZHOU");
 menuSubButtonDTO.setUrl("https://www.taobao.com");
 menuSubButtonDTO.setMediaId("mvFiiRhuwt5IiE");
 menuButtonDTO.setSubButton(menuSubButtonDTOs);
 menuConfigDTO.setButton(menuButtonDTOs);
 menuConfigDTO.setEnableInput(false);
 menuConfigDTO.setStatus(0L);
 req.setMenu(menuConfigDTO);
 OapiServiceaccountMenuUpdateResponse rsp = client.execute(req, access_token);
 System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceaccountMenuUpdateRequest("https://oapi.dingtalk.com/topapi/serviceaccount/menu/update")

req.unionid="jYdrJoCmTo0iE"
req.menu=""
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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST, DingTalkConstant::$FORMAT_JSON);
$req = new OapiServiceaccountMenuUpdateRequest;
$req->setUnionid("IlrIsTHaiSYXluZP61h0zxgiEiE");
$menu = new MenuConfigDTO;
$button = new MenuButtonDTO;
$button->name = "今日天气";
$button->type = "view";
$button->key = "KEY_WEATHER";
$button->url = "https://www.taobao.com";
$button->media_id = "mvFiiRhuwt5IiE";
$sub_button = new MenuSubButtonDTO;
$sub_button->name = "杭州天气";
$sub_button->type = "click";
$sub_button->key = "WEATHER_HANGZHOU";
$sub_button->url = "https://www.taobao.com";
$sub_button->media_id = "mvFiiRhuwt5IiE";
$button->sub_button = array($sub_button);
$menu->button = array($button);
$menu->enable_input = false;
$menu->status = 0;
$req->setMenu($menu);
$resp = $c->execute($req, $access_token);
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/menu/update");
OapiServiceaccountMenuUpdateRequest req = new OapiServiceaccountMenuUpdateRequest();
req.Unionid = "IlrIsTHaiSYXluZP61h0zxgiEiE";
OapiServiceaccountMenuUpdateRequest.MenuConfigDTODomain obj1 = new OapiServiceaccountMenuUpdateRequest.MenuConfigDTODomain();
List<OapiServiceaccountMenuUpdateRequest.MenuButtonDTODomain> list3 = new List<OapiServiceaccountMenuUpdateRequest.MenuButtonDTODomain>();
OapiServiceaccountMenuUpdateRequest.MenuButtonDTODomain obj4 = new OapiServiceaccountMenuUpdateRequest.MenuButtonDTODomain();
list3.Add(obj4);
obj4.Name = "今日天气";
obj4.Type = "view";
obj4.Key = "KEY_WEATHER";
obj4.Url = "https://www.taobao.com";
obj4.MediaId = "mvFiiRhuwt5IiE";
List<OapiServiceaccountMenuUpdateRequest.MenuSubButtonDTODomain> list6 = new List<OapiServiceaccountMenuUpdateRequest.MenuSubButtonDTODomain>();
OapiServiceaccountMenuUpdateRequest.MenuSubButtonDTODomain obj7 = new OapiServiceaccountMenuUpdateRequest.MenuSubButtonDTODomain();
list6.Add(obj7);
obj7.Name = "杭州天气";
obj7.Type = "click";
obj7.Key = "WEATHER_HANGZHOU";
obj7.Url = "https://www.taobao.com";
obj7.MediaId = "mvFiiRhuwt5IiE";
obj4.SubButton = list6;
obj1.Button = list3;
obj1.EnableInput = false;
obj1.Status = 0L;
req.Menu_ = obj1;
OapiServiceaccountMenuUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 5c4hvemrzn9u | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"5c4hvemrzn9u"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
