---
title: "获取用车订单数据"
source_url: "https://open.dingtalk.com/document/development/vehicle-order-query-interface"
namespace: "development"
slug: "vehicle-order-query-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取用车订单数据"
doc_id: "0OK1r47iEE"
updated_at: "2026-06-08 09:47:19"
---

> Source: https://open.dingtalk.com/document/development/vehicle-order-query-interface
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取用车订单数据
> Updated: 2026-06-08 09:47:19

# 获取用车订单数据

通过此接口获取企业用车订单数据，适用于企业差旅管理中的订单查询、财务对账、数据分析等场景。例如：当企业需要同步员工打车记录至内部报销系统时，可调用本接口批量获取订单数据，实现自动化对账与费用管控。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search |
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
| start\_time | Date | 否 | 2017-05-01 00:00:00 | 创建开始时间。 |
| update\_end\_time | Date | 否 | 2017-05-01 00:00:00 | 更新结束时间。 |
| apply\_id | Number | 否 | 123 | 商旅审批单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| page | Number | 否 | 1 | 页数，从1开始。 |
| userid | String | 否 | user1 | 用户userid。 |
| page\_size | Number | 否 | 10 | 每页数量，默认10，最大50。 |
| deptid | String | 否 | -1 | 部门ID。 |
| end\_time | Date | 否 | 2017-05-01 00:00:00 | 创建结束时间。 |
| update\_start\_time | Date | 否 | 2017-05-01 00:00:00 | 更新开始时间。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |
| all\_apply | Boolean | 否 | true | **false**：仅搜索未报销订单。 |
| thirdpart\_apply\_id | String | 否 | 123 | 第三方申请单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=385348xxxx5f2616b' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search");
OapiAlitripBtripVehicleOrderSearchRequest req = new OapiAlitripBtripVehicleOrderSearchRequest();
OpenSearchRq obj1 = new OpenSearchRq();
obj1.setStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setUpdateEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setApplyId(123L);
obj1.setPage(1L);
obj1.setUserid("user1");
obj1.setPageSize(10L);
obj1.setDeptid("dept1");
obj1.setEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setUpdateStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setCorpid("corp1");
obj1.setAllApply(true);
obj1.setThirdpartApplyId("123");
req.setRq(obj1);
OapiAlitripBtripVehicleOrderSearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripVehicleOrderSearchRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search")

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
$req = new OapiAlitripBtripVehicleOrderSearchRequest;
$rq = new OpenSearchRq;
$rq->start_time="2017-05-01 00:00:00";
$rq->update_end_time="2017-05-01 00:00:00";
$rq->apply_id="123";
$rq->page="1";
$rq->userid="user1";
$rq->page_size="10";
$rq->deptid="dept1";
$rq->end_time="2017-05-01 00:00:00";
$rq->update_start_time="2017-05-01 00:00:00";
$rq->corpid="corp1";
$rq->all_apply="true";
$rq->thirdpart_apply_id="123";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/vehicle/order/search");
OapiAlitripBtripVehicleOrderSearchRequest req = new OapiAlitripBtripVehicleOrderSearchRequest();
OapiAlitripBtripVehicleOrderSearchRequest.OpenSearchRqDomain obj1 = new OapiAlitripBtripVehicleOrderSearchRequest.OpenSearchRqDomain();
obj1.StartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.UpdateEndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.ApplyId = 123L;
obj1.Page = 1L;
obj1.Userid = "user1";
obj1.PageSize = 10L;
obj1.Deptid = "dept1";
obj1.EndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.UpdateStartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.Corpid = "corp1";
obj1.AllApply = true;
obj1.ThirdpartApplyId = "123";
req.Rq_ = obj1;
OapiAlitripBtripVehicleOrderSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| success | Boolean | true | 操作是否成功。 |
| vehicle\_order\_list | OpenVehicleOrderRs[] |  | 订单列表。 |
| id | Number | 12345 | 订单ID。 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 订单创建时间。 |
| gmt\_modified | Date | 2017-05-01 00:00:00 | 订单更新时间。 |
| passenger\_name | String | 李四 | 乘客名称。 |
| corpid | String | ding3cb4e7xxxx | 企业的corpid。 |
| corp\_name | String | 阿里巴巴 | 企业名称。 |
| user\_name | String | 张三 | 预定人姓名。 |
| userid | String | user1 | 预定人userid。 |
| dept\_name | String | 钉钉 | 部门名称。 |
| deptid | String | -1 | 部门ID。 |
| apply\_show\_id | String | 201802031353000525653 | 商旅审批单展示ID。 |
| apply\_id | Number | 27239497 | 商旅系统审批单ID。 |
| real\_from\_city\_name | String | 杭州 | 实际出发城市。 |
| real\_to\_city\_name | String | 杭州 | 实际到达城市。 |
| from\_address | String | 阿里巴巴西溪园区 | 出发地。 |
| to\_address | String | 乐佳国际 | 目的地。 |
| from\_city\_name | String | 杭州 | 出发城市。 |
| to\_city\_name | String | 杭州 | 目的城市。 |
| memo | String | 加班 | 打车事由。 |
| order\_status | Number | 2 | 订单状态：   - **0**：初始状态 - **1**：已超时 - **2**：派单成功 - **3**：派单失败 - **4**：已退款 - **5**：已支付 - **6**：已取消 |
| car\_level | String | 3 | 类型级别：   - **1**：经济型 - **2**：舒适型 - **3**：豪华型 |
| car\_info | String | 白色本田 | 车辆类型。 |
| estimate\_price | String | 100.0 | 订单预估价格。 |
| publish\_time | Date | 2017-05-01 00:00:00 | 乘客发布用车时间。 |
| taken\_time | Date | 2017-05-01 00:00:00 | 乘客上车时间。 |
| driver\_confirm\_time | Date | 2017-05-01 00:00:00 | 司机到达目的地时间。 |
| cancel\_time | Date | 2017-05-01 00:00:00 | 取消时间。 |
| travel\_distance | String | 1.2 | 行驶公里数。 |
| pay\_time | Date | 2017-05-01 00:00:00 | 支付时间。 |
| service\_type | Number | 1 | 打车服务类型：   - **1**：出租车 - **2**：专车 - **3**：快车 |
| business\_category | String | TRAVEL | 用车原因：   - **TRAVEL**：差旅 - **TRAFFIC**：市内交通 - **WORK**：加班 - **OTHER**：其它 |
| cost\_center\_id | Number | 12345 | 商旅成本中心ID。 |
| cost\_center\_number | String | abcde | 成本中心编号。 |
| cost\_center\_name | String | 测试成本中心 | 成本中心名称。 |
| invoice\_id | Number | 12345 | 商旅发票ID。 |
| invoice\_title | String | 阿里巴巴 | 发票抬头。 |
| project\_code | String | abcef | 项目编号。 |
| project\_title | String | 北京项目 | 项目名称。 |
| price\_info\_list | OpenPriceInfo[] |  | 价目详情列表。 |
| price | String | 100.0 | 价格。 |
| type | Number | 1 | 资金流向：   - **1**：支出 - **2**：收入 |
| category | String | 用车支付 | 交易类型：   - 用车支付, 服务费 - 用车取消后收费 - 用车退款, 用车赔付 |
| pay\_type | Number | 1 | 结算方式：   - **1**：个人现付 - **2**：企业现付 - **4**：企业月结 - **8**：企业预存 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 流水创建时间。 |
| passenger\_name | String | 张三,李四 | 出行人，多个用‘,’分割。 |
| thirdpart\_itinerary\_id | String | abcdefg | 第三方行程ID。 |
| user\_affiliate\_list | OpenUserAffiliateDo[] |  | 出行人列表。 |
| userid | String | 123 | 出行人userid。 |
| user\_name | String | 张三 | 出行人姓名。 |
| user\_confirm | Number | 1 | 用户确认状态：   - **0**：未确认 - **1**：已确认 - **2**：有异议 - **3**：系统检查不合理 |
| provider | Number | 2 | 服务商：   - **2**：滴滴 - **3**：曹操 - **4**：首汽 - **5**：阳光 |
| real\_from\_address | String | 高新文教区东部软件园创新大厦(马塍路) | 真实出发地。 |
| real\_to\_address | String | 联创街 | 真实到达地。 |
| thirdpart\_apply\_id | String | 123 | 第三方申请单ID。 |
| btrip\_title | String | 出差 | 申请单名称。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "vehicle_order_list": [
    {
      "apply_id": 0,
      "car_level": "3",
      "corpid": "ding3cb4e74a88d5a55535c2f4657eb6xxxx",
      "dept_name": "以升crop_0513_1",
      "deptid": "1",
      "estimate_price": "0.0",
      "from_address": "良睦路997乐佳国际",
      "from_city_name": "杭州市",
      "gmt_create": "2019-10-29 22:32:55",
      "gmt_modified": "2019-10-29 22:32:55",
      "memo": "测试",
      "order_status": 1,
      "passenger_name": "张三",
      "publish_time": "2019-10-29 22:32:55",
      "real_from_address": "",
      "real_from_city_name": "杭州市",
      "real_to_city_name": "杭州市",
      "service_type": 3,
      "to_address": "杭州城站火车站地下停车场(入口)",
      "to_city_name": "杭州市",
      "user_affiliate_list": [
        {
          "user_name": "张三",
          "userid": "0214591437658482"
        }
      ],
      "userid": "0214591437658482"
    }
  ],
  "request_id": "579juiw6xaz6"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
