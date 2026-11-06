---
title: "CRM客户动态事件"
source_url: "https://open.dingtalk.com/document/development/crm-customer-dynamic-events"
namespace: "development"
slug: "crm-customer-dynamic-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 客户管理事件 > CRM客户动态事件"
doc_id: "jtI8ULLzy2"
updated_at: "2025-10-16 15:06:38"
---

> Source: https://open.dingtalk.com/document/development/crm-customer-dynamic-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 客户管理事件 > CRM客户动态事件
> Updated: 2025-10-16 15:06:38

# CRM客户动态事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM客户动态事件 |
| 英文名称 | crm\_customer\_track |
| 事件BizType | 133 |

## 功能描述

当CRM客户动态相关信息发生变更时，钉钉通过事件订阅的方式将CRM客户动态相关变更内容推送给开发者。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## 事件体描述

### 第三方企业应用(biz\_type=293)

数据为RDS和SyncHTTP推送的事件体，当为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例如下:**

```
{
 "syncAction": "crm_customer_track",
 "tracks": [
 {
 "corpId": "ding9axxx",
 "customerId": "84c75568-xxx-xxx",
 "subType": 0,
 "gmtCreate": 1630474492814,
 "type": 107,
 "creator": "manager1234"
 }
 ],
 "syncSeq": "7C0F83xxx"
}
```

参数说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 取值为`crm_customer_track`时，表示客户动态相关的数据变更。 |
| corpId | String | 客户所在组织的corpId。 |
| customerId | String | 客户ID。 |
| subType | Number | 客户动态子类型。 |
| gmtCreate | Number | 动态创建时间。 |
| type | Number | 客户动态类型。 |
| creator | String | 动态创建者的userid。 |
