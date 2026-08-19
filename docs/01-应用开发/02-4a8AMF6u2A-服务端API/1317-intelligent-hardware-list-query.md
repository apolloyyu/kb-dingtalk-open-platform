---
title: "查询设备列表"
source_url: "https://open.dingtalk.com/document/development/intelligent-hardware-list-query"
namespace: "development"
slug: "intelligent-hardware-list-query"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 智能硬件 > 设备管理 > 查询设备列表"
doc_id: "PTEZl1JYFe"
updated_at: "2026-06-03 09:53:24"
---

> Source: https://open.dingtalk.com/document/development/intelligent-hardware-list-query
> Path: 应用开发 / 服务端API / 更多开放 > 智能硬件 > 设备管理 > 查询设备列表
> Updated: 2026-06-03 09:53:24

# 查询设备列表

调用本接口，根据产品的唯一标识，分页查询企业下的智能设备列表。

## **接口调用说明**

该接口适用于企业智能设备管理中的设备信息同步与分页查询场景。典型使用场景包括：

- **统一设备管理平台**：企业可集成此接口，构建内部智能硬件统一管理后台，实时获取所有已绑定设备的详细信息（如设备ID、MAC地址、绑定员工等）。
- **分页与游标翻页支持**：支持通过 `cursor` 和 `size` 参数实现大数据量下的高效分页查询，适用于设备数量较多的企业环境。
- **设备状态监控系统**：第三方ISV可基于此接口开发设备健康度监测、在线状态追踪等功能模块。

> **[!IMPORTANT]**
>
> 调用本接口前请完成对接，请填写[表单](https://ding.aliwork.com/o/dingtalk_smartdevice_interface_apply)并详细描述智能硬件接口的应用场景，以确保正常调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/device/querylist |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_smart\_device\_base-智能设备访问权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| page\_query\_vo | PageQueryVo | 是 |  | 列表查询对象，包含分页参数和产品标识。 |
| pk | String | 是 | pk\_01 | 产品的唯一标识。该参数需线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。 |
| cursor | Number | 是 | 0 | 游标地址，第一页填0。 |
| size | Number | 是 | 20 | 分页大小，最大支持20条记录每页。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/device/querylist" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7206e7cxxxx349b03' \
-d 'page_query_vo=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/querylist");
OapiSmartdeviceDeviceQuerylistRequest req = new OapiSmartdeviceDeviceQuerylistRequest();
PageQueryVo pageQueryVo = new PageQueryVo();
pageQueryVo.setPk("pk_01");
pageQueryVo.setCursor(0L);
pageQueryVo.setSize(20L);
req.setPageQueryVo(pageQueryVo);
OapiSmartdeviceDeviceQuerylistResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceDeviceQuerylistRequest("https://oapi.dingtalk.com/topapi/smartdevice/device/querylist")

req.page_query_vo=""
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
$req = new OapiSmartdeviceDeviceQuerylistRequest;
$page_query_vo = new PageQueryVo;
$page_query_vo->pk="yourproductkey";
$page_query_vo->cursor="0";
$page_query_vo->size="20";
$req->setPageQueryVo($page_query_vo);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/device/querylist");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/querylist");
OapiSmartdeviceDeviceQuerylistRequest req = new OapiSmartdeviceDeviceQuerylistRequest();
OapiSmartdeviceDeviceQuerylistRequest.PageQueryVoDomain obj1 = new OapiSmartdeviceDeviceQuerylistRequest.PageQueryVoDomain();
obj1.Pk = "yourproductkey";
obj1.Cursor = 0L;
obj1.Size = 20L;
req.PageQueryVo_ = obj1;
OapiSmartdeviceDeviceQuerylistResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult | result | 返回结果对象，封装分页数据。 |
| next\_cursor | Number | 1 | 下一页的游标。 |
| has\_more | Boolean | false | 是否有下一页。 |
| list | DeviceDetailVO[] |  | 结果列表。 |
| corp\_id | String | ding9f5xxxx | 企业的corpid。 |
| device\_mac | String | 11.11.11.11 | 设备的mac地址。 |
| nick | String | ding | 设备的昵称。 |
| device\_id | String | QWR45GT | 设备的id。 |
| device\_name | String | 产品智能 | 设备名称。 |
| pk | String | pk\_01 | 产品的唯一标识。 |
| userid | String | user01 | 绑定的员工的userid。 |
| ext | String | 智能产品 | 备注信息。 |
| sn | String | sdx123d123asdf | 设备序列号。 |
| success | Boolean | true | 请求是否成功。   - **true**：请求成功 - **false**：请求失败，并配合errcode返回具体错误原因 |
| errcode | Number | 0 | 返回码，表示调用结果状态。 |
| errmsg | String | ok | 返回码描述信息。 |
| request\_id | String | exz1t52e9awo | 当前请求的唯一标识ID，用于问题排查和日志追踪。 |

### **响应体示例**

```
{
  "result": {
    "next_cursor": 0,
    "has_more": false,
    "list": [
      {
        "nick": "ding",
        "ext": "智能产品",
        "device_mac": "11.11.11.11",
        "device_name": "产品智能",
        "device_id": "QWR45GT",
        "pk": "pk_01",
        "sn": "sdx123d123asdf",
        "corp_id": "ding9f5xxxx",
        "userid": "user01"
      }
    ]
  },
  "errcode": 0,
  "success": true,
  "request_id": "exz1t52e9awo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
