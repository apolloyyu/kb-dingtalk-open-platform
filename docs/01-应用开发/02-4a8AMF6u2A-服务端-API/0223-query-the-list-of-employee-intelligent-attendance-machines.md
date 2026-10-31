---
title: "查询员工智能考勤机列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-employee-intelligent-attendance-machines"
namespace: "development"
slug: "query-the-list-of-employee-intelligent-attendance-machines"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤机管理 > 查询员工智能考勤机列表"
doc_id: "DFdxipdXyQ"
updated_at: "2026-05-27 17:06:20"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-employee-intelligent-attendance-machines
> Path: 应用开发 / 服务端 API / 考勤 > 考勤机管理 > 查询员工智能考勤机列表
> Updated: 2026-05-27 17:06:20

# 查询员工智能考勤机列表

调用本接口，可获取员工智能考勤机列表，包括考勤机名称、考勤机类型名称等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get\_by\_userid |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_dingtalk\_attendance\_manage-钉钉考勤机人员管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| param | UserMachineInfoRequestVo | 是 |  | 请求结构。 |
| offset | Number | 是 | 0 | 分页游标，从0开始的非负整数。 |
| size | Number | 是 | 10 | 每页大小，最大值50。 |
| userid | String | 是 | user456 | 员工userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get_by_userid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=102a93xxxx0ebeb' \
-d 'param=null'
```

Java

```
DefaultDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get_by_userid");
OapiSmartdeviceAtmachineGetByUseridRequest request = new OapiSmartdeviceAtmachineGetByUseridRequest();
UserMachineInfoRequestVo requestVo = new UserMachineInfoRequestVo();
requestVo.setUserid("user456");
requestVo.setOffset(0L);
requestVo.setSize(10L);
request.setParam(requestVo);
OapiSmartdeviceAtmachineGetByUseridResponse response = client.execute(request, access_token);
System.out.println(response.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceAtmachineGetByUseridRequest("https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get_by_userid")

req.param=""
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
$req = new OapiSmartdeviceAtmachineGetByUseridRequest;
$param = new UserMachineInfoRequestVo;
$param->offset="0";
$param->size="20";
$param->userid="238923423";
$req->setParam($param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get_by_userid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/atmachine/get_by_userid");
OapiSmartdeviceAtmachineGetByUseridRequest req = new OapiSmartdeviceAtmachineGetByUseridRequest();
OapiSmartdeviceAtmachineGetByUseridRequest.UserMachineInfoRequestVoDomain obj1 = new OapiSmartdeviceAtmachineGetByUseridRequest.UserMachineInfoRequestVoDomain();
obj1.Offset = 0L;
obj1.Size = 20L;
obj1.Userid = "238923423";
req.Param_ = obj1;
OapiSmartdeviceAtmachineGetByUseridResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | MachineInfoResultVo |  | 返回结果。 |
| machine\_list | MachineVo[] |  | 考勤机列表。 |
| deviceid | String | abc123456 | 考勤机唯一ID。 |
| device\_name | String | 东门考勤机 | 考勤机名称。 |
| product\_name | String | M1X | 考勤机类型名称，即考勤机型号。 |
| devid | Number | 123456 | 考勤机唯一ID。 |
| has\_more | Boolean | false | 是否有更多数据。   - **true**：有 - **false**：没有 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "hasMore": false,
    "machineList": [
      {
        "deviceName": "东门考勤机",
        "deviceid": "abc123456",
        "devid": 123456,
        "productName": "M1X"
      }
    ]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
