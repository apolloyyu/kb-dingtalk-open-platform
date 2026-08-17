---
title: "水印打卡签到"
source_url: "https://open.dingtalk.com/document/development/watermark-punch-in"
namespace: "development"
slug: "watermark-punch-in"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 水印打卡签到"
doc_id: "mcB3JSXDQw"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/watermark-punch-in
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 水印打卡签到
> Updated: 2022-01-19 19:29:22

# 水印打卡签到

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 水印打卡签到 |
| 英文名称 | watermark\_check\_in |

## 功能描述

该事件用于对外开放水印打卡。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "watermark_check_in",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "positionDataModel": {
      "country": "中国",
      "detailPlace": "xxx路xx号",
      "province": "浙江省",
      "city": "杭州",
      "street": "xxx街道",
      "district": "西湖区",
      "latitude": "102.742288682725",
      "place": "杭州",
      "longitude": "38.34643"
    },
    "waterMarkModel": {
      "mediaIdV2": "https://down.dingtalk.com/ddmedia/dddddd2.jpg",
      "mediaIdV1": "https://down.dingtalk.com/ddmedia/dddddd.jpg",
      "deviceId": "124"
    },
    "formCode": "asdadasdfaf",
    "formDataLists": [
      {
        "label": "拜访人",
        "value": "dddd",
        "key": "sdfgsrgag"
      }
    ],
    "openConversationId": "BHjdHfv\u003d\u003d",
    "extraInfo": {}
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "watermark_check_in",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "positionDataModel": {
    "country": "中国",
    "detailPlace": "xxx路xx号",
    "province": "浙江省",
    "city": "杭州",
    "street": "xxx街道",
    "district": "西湖区",
    "latitude": "102.742288682725",
    "place": "杭州",
    "longitude": "38.34643"
  },
  "waterMarkModel": {
    "mediaIdV2": "https://down.dingtalk.com/ddmedia/dddddd2.jpg",
    "mediaIdV1": "https://down.dingtalk.com/ddmedia/dddddd.jpg",
    "deviceId": "124"
  },
  "formCode": "asdadasdfaf",
  "formDataLists": [
    {
      "label": "拜访人",
      "value": "dddd",
      "key": "sdfgsrgag"
    }
  ],
  "openConversationId": "BHjdHfv\u003d\u003d",
  "extraInfo": {}
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=204)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 204,
  "biz_data": {
    "positionDataModel": {
      "country": "中国",
      "detailPlace": "xxx路xx号",
      "province": "浙江省",
      "city": "杭州",
      "street": "xxx街道",
      "district": "西湖区",
      "latitude": "102.742288682725",
      "place": "杭州",
      "longitude": "38.34643"
    },
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "waterMarkModel": {
      "mediaIdV2": "https://down.dingtalk.com/ddmedia/dddddd2.jpg",
      "mediaIdV1": "https://down.dingtalk.com/ddmedia/dddddd.jpg",
      "deviceId": "124"
    },
    "syncAction": "watermark_check_in",
    "formCode": "asdadasdfaf",
    "formDataLists": [
      {
        "label": "拜访人",
        "value": "dddd",
        "key": "sdfgsrgag"
      }
    ],
    "openConversationId": "BHjdHfv\u003d\u003d",
    "extraInfo": {}
  }
}
```
