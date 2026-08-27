---
title: "设置成本中心人员信息"
source_url: "https://open.dingtalk.com/document/development/set-up-cost-center-personnel-information"
namespace: "development"
slug: "set-up-cost-center-personnel-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 设置成本中心人员信息"
doc_id: "2Su9EEKs9r"
updated_at: "2026-06-03 09:58:29"
---

> Source: https://open.dingtalk.com/document/development/set-up-cost-center-personnel-information
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 设置成本中心人员信息
> Updated: 2026-06-03 09:58:29

# 设置成本中心人员信息

通过此接口设置成本中心的人员信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip\_write-阿里商旅专用写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenCostCenterSetEntityRq | 是 |  | 请求对象，包含成本中心及人员列表信息。 |
| thirdpart\_id | String | 是 | cost1 | 第三方成本中心id。 |
| entity\_list | OpenOrgEntityDo[] | 是 |  | 人员信息列表。 |
| entity\_id | String | 是 | 12345 | 员工/部门/角色id。 |
| entity\_type | String | 是 | 1 | 人员类型：   - **1**：员工 - **2**：部门 - **3**：角色 |
| corpid | String | 是 | corp1 | 企业的corpid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=13e02d26-1fd9-4da9-8f32-b2c4e2336043' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set");
OapiAlitripBtripCostCenterEntitySetRequest req = new OapiAlitripBtripCostCenterEntitySetRequest();
OpenCostCenterSetEntityRq obj1 = new OpenCostCenterSetEntityRq();
obj1.setThirdpartId("cost1");
List<OpenOrgEntityDo> list3 = new ArrayList<OpenOrgEntityDo>();
OpenOrgEntityDo obj4 = new OpenOrgEntityDo();
list3.add(obj4);
obj4.setEntityId("12345");
obj4.setEntityType("1");
obj1.setEntityList(list3);
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripCostCenterEntitySetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripCostCenterEntitySetRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set")

req.rq=""
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
$req = new OapiAlitripBtripCostCenterEntitySetRequest;
$rq = new OpenCostCenterSetEntityRq;
$rq->thirdpart_id="cost1";
$entity_list = new OpenOrgEntityDo;
$entity_list->entity_id="12345";
$entity_list->entity_type="1";
$rq->entity_list = array($entity_list);
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/set");
OapiAlitripBtripCostCenterEntitySetRequest req = new OapiAlitripBtripCostCenterEntitySetRequest();
OapiAlitripBtripCostCenterEntitySetRequest.OpenCostCenterSetEntityRqDomain obj1 = new OapiAlitripBtripCostCenterEntitySetRequest.OpenCostCenterSetEntityRqDomain();
obj1.ThirdpartId = "cost1";
List<OapiAlitripBtripCostCenterEntitySetRequest.OpenOrgEntityDoDomain> list3 = new List<OapiAlitripBtripCostCenterEntitySetRequest.OpenOrgEntityDoDomain>();
OapiAlitripBtripCostCenterEntitySetRequest.OpenOrgEntityDoDomain obj4 = new OapiAlitripBtripCostCenterEntitySetRequest.OpenOrgEntityDoDomain();
list3.Add(obj4);
obj4.EntityId = "12345";
obj4.EntityType = "1";
obj1.EntityList= list3;
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripCostCenterEntitySetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 成本标识。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| result | OpenCostCenterSetEntityRs | result | 结果对象。 |
| add\_num | Number | 1 | 增加的人员信息条数。 |
| remove\_num | Number | 2 | 删除的人员信息条数。 |
| selected\_user\_num | Number | 5 | 该成本中心下员工总数。 |

### **响应体示例**

```
{
  "errcode":"0",
  "result":{
    "remove_num":"2",
    "add_num":"1",
    "selected_user_num":"5"
  },
  "success":"true",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
