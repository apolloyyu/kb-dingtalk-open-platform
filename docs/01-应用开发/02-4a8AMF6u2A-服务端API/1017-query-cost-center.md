---
title: "查询成本中心"
source_url: "https://open.dingtalk.com/document/development/query-cost-center"
namespace: "development"
slug: "query-cost-center"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 查询成本中心"
doc_id: "Aw1q47TJKb"
updated_at: "2026-06-03 09:58:23"
---

> Source: https://open.dingtalk.com/document/development/query-cost-center
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 查询成本中心
> Updated: 2026-06-03 09:58:23

# 查询成本中心

通过此接口查询企业成本中心信息，支持按成本中心名称、第三方ID或用户身份进行筛选，适用于企业财务系统与钉钉成本中心数据同步的场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenCostCenterQueryRq | 是 |  | 请求对象。 |
| title | String | 否 | 测试成本中心 | 成本中心名称。 |
| thirdpart\_id | String | 否 | cost1 | 第三方成本中心ID，不填写的时候userid必填。 |
| userid | String | 否 | user1 | 用户的userid，不填的时候thirdpart\_id必填。 |
| need\_org\_entity | Boolean | 否 | false | 是否需要展示成员信息，当成本中心为部分人员适用的时候有返回。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=355e61exxxx093221' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query");
OapiAlitripBtripCostCenterQueryRequest req = new OapiAlitripBtripCostCenterQueryRequest();
OpenCostCenterQueryRq obj1 = new OpenCostCenterQueryRq();
obj1.setTitle("测试成本中心");
obj1.setThirdpartId("cost1");
obj1.setUserid("user1");
obj1.setNeedOrgEntity(false);
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripCostCenterQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripCostCenterQueryRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query")

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
$req = new OapiAlitripBtripCostCenterQueryRequest;
$rq = new OpenCostCenterQueryRq;
$rq->title="测试成本中心";
$rq->thirdpart_id="cost1";
$rq->userid="user1";
$rq->need_org_entity="false";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/query");
OapiAlitripBtripCostCenterQueryRequest req = new OapiAlitripBtripCostCenterQueryRequest();
OapiAlitripBtripCostCenterQueryRequest.OpenCostCenterQueryRqDomain obj1 = new OapiAlitripBtripCostCenterQueryRequest.OpenCostCenterQueryRqDomain();
obj1.Title = "测试成本中心";
obj1.ThirdpartId = "cost1";
obj1.Userid = "user1";
obj1.NeedOrgEntity = false;
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripCostCenterQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| cost\_center\_list | OpenCostCenterQueryRs[] | costCenterList | 成本中心列表。 |
| id | Number | 123456 | 商旅成本中心ID。 |
| corpid | String | corp1 | 企业的corpid。 |
| title | String | 阿里商旅 | 成本中心名称。 |
| number | String | 123456 | 成本中心编号。 |
| thirdpart\_id | String | cost1 | 第三方成本中心ID。 |
| scope | Number | 1 | 适用范围：   - **1**：全员 - **2**：部分员工 |
| alipay\_no | String | a@alipay.com | 绑定支付宝账号。 |
| entity\_list | OpenOrgEntityDo[] | entityList | 绑定人员信息。 |
| entity\_type | String | 1 | 人员类型：   - **1**：用户 - **2**：部门 - **3**：角色 |
| entity\_id | String | 12345 | 用户/部门/角色ID。 |
| corpid | String | corp1 | 企业的corpid。 |
| name | String | 张三 | 用户/部门/角色名称。 |
| user\_num | Number | 10 | 角色/部门下面员工人数。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "cost_center_list":{
    "number":"123456",
    "thirdpart_id":"cost1",
    "corpid":"corp1",
    "scope":"1",
    "id":"123456",
    "entity_list":{
      "user_num":"10",
      "entity_type":"1",
      "corpid":"corp1",
      "name":"张三",
      "entity_id":"12345"
    },
    "title":"阿里商旅",
    "alipay_no":"a@alipay.com"
  },
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
