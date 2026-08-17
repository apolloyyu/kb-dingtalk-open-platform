---
title: "招聘业务平台权益变更"
source_url: "https://open.dingtalk.com/document/development/change-of-rights-and-interests-of-recruitment-business-platform"
namespace: "development"
slug: "change-of-rights-and-interests-of-recruitment-business-platform"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 招聘业务平台权益变更"
doc_id: "dPPevwIwMM"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/change-of-rights-and-interests-of-recruitment-business-platform
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 招聘业务平台权益变更
> Updated: 2022-01-19 19:29:22

# 招聘业务平台权益变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 招聘业务平台权益变更 |
| 英文名称 | ats\_rights\_change |

## 功能描述

招聘高级版权益变更时会发出事件，如免费变付费，付费到期变免费，仅合作生态需要申请。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ats_rights_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "dingxxxx",
    "bizCode": "xxxx",
    "rightsCode": "rightsxxxxx",
    "free": true,
    "expiredTime": "1672502400000"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=161)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 161,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "dingxxxx",
    "syncAction": "ats_rights_change",
    "bizCode": "xxxx",
    "rightsCode": "rightsxxxxx",
    "free": true,
    "expiredTime": "1672502400000"
  }
}
```
