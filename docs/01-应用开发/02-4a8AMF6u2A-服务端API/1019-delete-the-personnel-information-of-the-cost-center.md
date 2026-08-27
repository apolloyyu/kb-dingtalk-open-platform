---
title: "删除成本中心人员信息"
source_url: "https://open.dingtalk.com/document/development/delete-the-personnel-information-of-the-cost-center"
namespace: "development"
slug: "delete-the-personnel-information-of-the-cost-center"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 删除成本中心人员信息"
doc_id: "cvVkhefH8z"
updated_at: "2026-06-08 09:47:08"
---

> Source: https://open.dingtalk.com/document/development/delete-the-personnel-information-of-the-cost-center
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 删除成本中心人员信息
> Updated: 2026-06-08 09:47:08

# 删除成本中心人员信息

调用本接口可删除指定成本中心下的员工、部门或角色相关的人员信息，适用于企业财务系统对接中对成本数据的清理与维护。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete |
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
| rq | OpenCostCenterDeleteEntityRq | 是 |  | 请求对象，封装删除操作所需的所有参数。 |
| del\_all | Boolean | 否 | false | 是否全部删除。 |
| thirdpart\_id | String | 是 | cost1 | 第三方成本中心id。 |
| entity\_list | OpenOrgEntityDo[] | 否 |  | 删除的成员信息列表，del\_all为**true**时可不填。 |
| entity\_id | String | 是 | 12345 | 员工/部门/角色id。 |
| entity\_type | String | 是 | 1 | 人员类型：   - **1**：员工 - **2**：部门 - **3**：角色 |
| corpid | String | 是 | corp1 | 企业的corpid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=be783dxxxx3c9b2aa7eb' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete");
OapiAlitripBtripCostCenterEntityDeleteRequest req = new OapiAlitripBtripCostCenterEntityDeleteRequest();
OpenCostCenterDeleteEntityRq obj1 = new OpenCostCenterDeleteEntityRq();
obj1.setDelAll(false);
obj1.setThirdpartId("cost1");
List<OpenOrgEntityDo> list3 = new ArrayList<OpenOrgEntityDo>();
OpenOrgEntityDo obj4 = new OpenOrgEntityDo();
list3.add(obj4);
obj4.setEntityId("12345");
obj4.setEntityType("1");
obj1.setEntityList(list3);
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripCostCenterEntityDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripCostCenterEntityDeleteRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete")

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
$req = new OapiAlitripBtripCostCenterEntityDeleteRequest;
$rq = new OpenCostCenterDeleteEntityRq;
$rq->del_all="false";
$rq->thirdpart_id="cost1";
$entity_list = new OpenOrgEntityDo;
$entity_list->entity_id="12345";
$entity_list->entity_type="1";
$rq->entity_list = array($entity_list);
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/entity/delete");
OapiAlitripBtripCostCenterEntityDeleteRequest req = new OapiAlitripBtripCostCenterEntityDeleteRequest();
OapiAlitripBtripCostCenterEntityDeleteRequest.OpenCostCenterDeleteEntityRqDomain obj1 = new OapiAlitripBtripCostCenterEntityDeleteRequest.OpenCostCenterDeleteEntityRqDomain();
obj1.DelAll = false;
obj1.ThirdpartId = "cost1";
List<OapiAlitripBtripCostCenterEntityDeleteRequest.OpenOrgEntityDoDomain> list3 = new List<OapiAlitripBtripCostCenterEntityDeleteRequest.OpenOrgEntityDoDomain>();
OapiAlitripBtripCostCenterEntityDeleteRequest.OpenOrgEntityDoDomain obj4 = new OapiAlitripBtripCostCenterEntityDeleteRequest.OpenOrgEntityDoDomain();
list3.Add(obj4);
obj4.EntityId = "12345";
obj4.EntityType = "1";
obj1.EntityList= list3;
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripCostCenterEntityDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenCostCenterDeleteEntityRs | result | 结果对象，包含本次删除操作的统计信息。 |
| selected\_user\_num | Number | 123 | 该成本中心下员工总数。 |
| remove\_num | Number | 12 | 删除的人员信息条数。 |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 调用是否成功。 |

### **响应体示例**

```
{
  "result":{
    "remove_num":"12",
    "selected_user_num":"123"
  },
  "errcode":"0",
  "success":"true",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
