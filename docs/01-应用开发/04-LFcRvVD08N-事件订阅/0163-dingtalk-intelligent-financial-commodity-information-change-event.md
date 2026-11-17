---
title: "钉钉智能财务商品信息变更事件"
source_url: "https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-commodity-information-change-event"
namespace: "development"
slug: "dingtalk-intelligent-financial-commodity-information-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 钉钉智能财务商品信息变更事件"
doc_id: "o4wkPommCb"
updated_at: "2025-08-28 19:47:09"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-commodity-information-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 钉钉智能财务商品信息变更事件
> Updated: 2025-08-28 19:47:09

# 钉钉智能财务商品信息变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉智能财务商品信息变更事件 |
| 英文名称 | smart\_finance\_product\_change |

## 功能描述

当智能财务商品辅助字段发生增删改时，钉钉会通过事件订阅的方式将商品变更的信息推送给开发者，用于监听商品变更信息。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.data`（object）：变更信息。
- `data.data.changeType`（string）：商品信息变更类型。
- `data.data.productInfo`（object）：商品信息。
- `data.data.productInfo.modifiedTime`（long）：修改时间戳。
- `data.data.productInfo.productCode`（string）：商品code。
- `data.data.productInfo.createTime`（long）：创建时间戳。
- `data.data.productInfo.corpId`（string）：组织id。
- `data.data.productInfo.name`（string）：名称。
- `data.data.productInfo.description`（string）：描述。
- `data.data.productInfo.specification`（string）：备注信息。
- `data.data.productInfo.unit`（string）：单位。
- `data.data.productInfo.userDefineCode`（string）：userDefineCode。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "smart_finance_product_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "data": {
      "changeType": "add",
      "productInfo": {
        "userDefineCode": "12345",
        "modifiedTime": 1692692634000,
        "unit": "双",
        "productCode": "PROD_1024EB8XXXXX10001",
        "corpId": "dingc1c52aaxxxx55b",
        "createTime": 1692692634000,
        "name": "2023车博会 9.17-19",
        "description": "xxx",
        "specification": "xxx"
      }
    }
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.data`（object）：变更信息。
- `biz_data.data.changeType`（string）：商品信息变更类型。
- `biz_data.data.productInfo`（object）：商品信息。
- `biz_data.data.productInfo.modifiedTime`（long）：修改时间戳。
- `biz_data.data.productInfo.productCode`（string）：商品code。
- `biz_data.data.productInfo.createTime`（long）：创建时间戳。
- `biz_data.data.productInfo.corpId`（string）：组织id。
- `biz_data.data.productInfo.name`（string）：名称。
- `biz_data.data.productInfo.description`（string）：描述。
- `biz_data.data.productInfo.specification`（string）：备注信息。
- `biz_data.data.productInfo.unit`（string）：单位。
- `biz_data.data.productInfo.userDefineCode`（string）：userDefineCode。

### **biz\_data数据示例(biz\_type=271)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 271,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "data": {
      "changeType": "add",
      "productInfo": {
        "userDefineCode": "12345",
        "modifiedTime": 1692692634000,
        "unit": "双",
        "productCode": "PROD_1024EB8XXXXX10001",
        "corpId": "dingc1c52aaxxxx55b",
        "createTime": 1692692634000,
        "name": "2023车博会 9.17-19",
        "description": "xxx",
        "specification": "xxx"
      }
    },
    "syncAction": "smart_finance_product_change"
  }
}
```
