---
title: "钉钉智能财务收支类别信息变更事件"
source_url: "https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-revenue-and-expenditure-category-information-change-event"
namespace: "development"
slug: "dingtalk-intelligent-financial-revenue-and-expenditure-category-information-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 钉钉智能财务收支类别信息变更事件"
doc_id: "HKo01y4DbB"
updated_at: "2025-08-28 19:47:12"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-revenue-and-expenditure-category-information-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 钉钉智能财务收支类别信息变更事件
> Updated: 2025-08-28 19:47:12

# 钉钉智能财务收支类别信息变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉智能财务收支类别信息变更事件 |
| 英文名称 | smart\_finance\_category\_change |

## 功能描述

数据为智能财务的收支类别变更相关数据。该数据用于告知合作伙伴，企业的收支类别进行了更新，便于数据实时同步。

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
- `data.changeType`（string）：变更类型：  
  - add：新增。  
  - update：更新。  
  - delete：移除。
- `data.category`（object）：收支类别数据。
- `data.category.createTime`（long，必填）：创建时间。
- `data.category.code`（string，必填）：收支类别code。
- `data.category.parentCode`（string，必填）：父类code。
- `data.category.name`（string，必填）：供应商名称。
- `data.category.dir`（string，必填）：是否为根节点。
- `data.category.type`（string，必填）：类别：  
  - income：收入。  
  - expense： 支出。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "smart_finance_category_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "changeType": "add",
    "category": {
      "code": "INC_XXXXX",
      "createTime": 1656646242898,
      "parentCode": "INC_YYYYYY",
      "name": "外层目录示例",
      "dir": "false",
      "type": "income"
    }
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.changeType`（string）：变更类型：  
  - add：新增。  
  - update：更新。  
  - delete：移除。
- `biz_data.category`（object）：收支类别数据。
- `biz_data.category.createTime`（long，必填）：创建时间。
- `biz_data.category.code`（string，必填）：收支类别code。
- `biz_data.category.parentCode`（string，必填）：父类code。
- `biz_data.category.name`（string，必填）：供应商名称。
- `biz_data.category.dir`（string，必填）：是否为根节点。
- `biz_data.category.type`（string，必填）：类别：  
  - income：收入。  
  - expense： 支出。

### **biz\_data数据示例(biz\_type=207)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 207,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "smart_finance_category_change",
    "changeType": "add",
    "category": {
      "code": "INC_XXXXX",
      "createTime": 1656646242898,
      "parentCode": "INC_YYYYYY",
      "name": "外层目录示例",
      "dir": "false",
      "type": "income"
    }
  }
}
```
