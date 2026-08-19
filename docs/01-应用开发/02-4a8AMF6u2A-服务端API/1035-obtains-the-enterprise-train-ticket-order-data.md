---
title: "获取企业火车票订单数据"
source_url: "https://open.dingtalk.com/document/development/obtains-the-enterprise-train-ticket-order-data"
namespace: "development"
slug: "obtains-the-enterprise-train-ticket-order-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取企业火车票订单数据"
doc_id: "3JpnNp1Vds"
updated_at: "2026-06-08 09:47:17"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-enterprise-train-ticket-order-data
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取企业火车票订单数据
> Updated: 2026-06-08 09:47:17

# 获取企业火车票订单数据

通过此接口获取企业火车票订单数据，支持根据时间范围、审批单、用户、部门等条件筛选订单，适用于企业差旅管理系统中的财务对账、报销审核、出行统计分析等业务场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenSearchRq | 是 |  | 请求对象。 |
| start\_time | Date | 否 | 2017-05-01 00:00:00 | 开始时间。 |
| apply\_id | Number | 否 | 7438532 | 商旅审批单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| page | Number | 否 | 1 | 页数，从1开始。 |
| userid | String | 否 | user1 | 用户的userid。 |
| page\_size | Number | 否 | 10 | 每页返回数量，默认10，最大50。 |
| deptid | String | 否 | -1 | 部门ID。 |
| end\_time | Date | 否 | 2017-05-01 00:00:00 | 结束时间。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |
| update\_end\_time | Date | 否 | 2017-05-01 00:00:00 | 更新结束时间。 |
| update\_start\_time | Date | 否 | 2017-05-01 00:00:00 | 更新开始时间 |
| all\_apply | Boolean | 否 | true | **false：**仅搜索未报销的订单。 |
| thirdpart\_apply\_id | String | 否 | 123 | 第三方申请单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3e932xxxx1a838e' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search");
OapiAlitripBtripTrainOrderSearchRequest req = new OapiAlitripBtripTrainOrderSearchRequest();
OpenSearchRq obj1 = new OpenSearchRq();
obj1.setStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setApplyId(123L);
obj1.setPage(1L);
obj1.setUserid("user1");
obj1.setPageSize(10L);
obj1.setDeptid("dept1");
obj1.setEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setCorpid("corp1");
obj1.setUpdateEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setUpdateStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setAllApply(true);
obj1.setThirdpartApplyId("123");
req.setRq(obj1);
OapiAlitripBtripTrainOrderSearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripTrainOrderSearchRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search")

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
$req = new OapiAlitripBtripTrainOrderSearchRequest;
$rq = new OpenSearchRq;
$rq->start_time="2017-05-01 00:00:00";
$rq->apply_id="123";
$rq->page="1";
$rq->userid="user1";
$rq->page_size="10";
$rq->deptid="dept1";
$rq->end_time="2017-05-01 00:00:00";
$rq->corpid="corp1";
$rq->update_end_time="2017-05-01 00:00:00";
$rq->update_start_time="2017-05-01 00:00:00";
$rq->all_apply="true";
$rq->thirdpart_apply_id="123";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/train/order/search");
OapiAlitripBtripTrainOrderSearchRequest req = new OapiAlitripBtripTrainOrderSearchRequest();
OapiAlitripBtripTrainOrderSearchRequest.OpenSearchRqDomain obj1 = new OapiAlitripBtripTrainOrderSearchRequest.OpenSearchRqDomain();
obj1.StartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.ApplyId = 123L;
obj1.Page = 1L;
obj1.Userid = "user1";
obj1.PageSize = 10L;
obj1.Deptid = "dept1";
obj1.EndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.Corpid = "corp1";
obj1.UpdateEndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.UpdateStartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.AllApply = true;
obj1.ThirdpartApplyId = "123";
req.Rq_ = obj1;
OapiAlitripBtripTrainOrderSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| train\_order\_list | OpenTrainOrderRs[] | module | 火车票订单列表。 |
| id | Number | 7438532 | 订单ID。 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 创建时间。 |
| gmt\_modified | Date | 2017-05-01 00:00:00 | 更新时间。 |
| corpid | String | corp1 | 企业的corpid。 |
| corp\_name | String | 阿里巴巴 | 企业名称。 |
| userid | String | user1 | 用户的userid。 |
| user\_name | String | 张三 | 用户姓名。 |
| deptid | String | -1 | 部门ID。 |
| dept\_name | String | 淘宝 | 部门名称。 |
| apply\_id | Number | 123456 | 商旅审批单ID。 |
| contact\_name | String | 张三 | 联系人姓名。 |
| dep\_station | String | 北京南 | 出发站。 |
| arr\_station | String | 杭州东 | 到达站。 |
| dep\_time | Date | 2017-05-01 00:00:00 | 出发时间。 |
| arr\_time | Date | 2017-05-01 00:00:00 | 到达时间。 |
| train\_number | String | G106 | 车次。 |
| train\_type | String | 高速动车 | 车次类型。 |
| seat\_type | String | 二等座 | 座位类型。 |
| run\_time | String | 5时32分 | 运行时长。 |
| ticket\_no\_12306 | String | E952714184 | 12306票号。 |
| dep\_city | String | 北京 | 出发城市。 |
| arr\_city | String | 杭州 | 到达城市。 |
| rider\_name | String | 张三/李四 | 乘客姓名。 |
| ticket\_count | Number | 2 | 票的数量。 |
| status | Number | 0 | 订单状态：   - 0：待支付 - 1：出票中 - 2：已关闭 - 3：改签成功 - 4：退票成功 - 5：出票完成 - 6：退票申请中 - 7：改签申请中 - 8：已出票/已发货 - 9：出票失败 - 10：改签失败 - 11：退票失败 |
| invoice | OpenInvoiceDo |  | 发票对象。 |
| id | String | 82559 | 商旅发票ID。 |
| title | String | 阿里巴巴 | 发票抬头。 |
| cost\_center | OpenCostCenterDo |  | 成本中心对象。 |
| id | String | 96011 | 商旅成本中心ID。 |
| corpid | String | ding3cb4exxxx | 企业的corpid。 |
| number | String | abcdef | 成本中心编号。 |
| name | String | 测试成本中心 | 成本中心名称。 |
| price\_info\_list | OpenPriceInfo[] |  | 价目信息。 |
| price | String | 100.0 | 价格。 |
| type | Number | 1 | 资金流向：   - 1：支出 - 2：收入 |
| category | String | 预定成功 | 消费类型。 |
| pay\_type | Number | 1 | 结算方式：   - 1：个人现付 - 2：企业现付 - 4：企业月结 - 8：企业预存 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 流水创建时间。 |
| passenger\_name | String | 张三、李四 | 乘车人名称，多个用‘,’分割。 |
| thirdpart\_itinerary\_id | String | c6d69cf99391480e829ee99fc4496825 | 第三方行程ID。 |
| user\_affiliate\_list | OpenUserAffiliateDo[] |  | 乘车人列表。 |
| userid | String | 123 | 乘车人userid。 |
| user\_name | String | 张三 | 乘车人姓名。 |
| thirdpart\_apply\_id | String | 123 | 第三方申请单ID。 |
| btrip\_title | String | 出差 | 申请单名称。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "train_order_list": [
    {
      "apply_id": 7438532,
      "arr_city": "上海",
      "arr_station": "上海虹桥",
      "arr_time": "2018-09-21 12:40:00",
      "btrip_title": "出差办公",
      "contact_name": "",
      "corp_name": "以升crop_0513",
      "corpid": "ding3cb4e74a88d5a55535c2f4657eb63xxxx",
      "cost_center": {
        "corpid": "ding3cb4e74a88d5a55535c2f4657eb63xxxx",
        "id": "96011",
        "name": "以升crop"
      },
      "dep_city": "北京",
      "dep_station": "北京南",
      "dep_time": "2018-09-21 06:43:00",
      "dept_name": "以升crop",
      "deptid": "-1",
      "gmt_create": "2018-09-19 14:10:15",
      "gmt_modified": "2018-09-19 14:11:33",
      "id": 1311633798275,
      "invoice": {
        "id": "82559",
        "title": "以升crop"
      },
      "price_info_list": [],
      "rider_name": "张三",
      "run_time": "5小时57分",
      "seat_type": "二等座",
      "status": 2,
      "thirdpart_apply_id": "8a5043a0-5395-475f-b884-5b3e4768b6a4",
      "thirdpart_itinerary_id": "bd9a2296a9c14e2ba04785edfd1b1804",
      "ticket_count": 1,
      "train_number": "G101",
      "train_type": "高铁",
      "user_affiliate_list": [
        {
          "user_name": "张三",
          "userid": "0214591437658482"
        }
      ],
      "user_name": "李四",
      "userid": "0214591437658482"
    }
  ],
  "request_id": "8e0xemuu9dbt"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
