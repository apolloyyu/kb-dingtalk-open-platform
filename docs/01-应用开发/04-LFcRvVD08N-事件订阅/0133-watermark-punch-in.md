---
title: "水印打卡签到"
source_url: "https://open.dingtalk.com/document/development/watermark-punch-in"
namespace: "development"
slug: "watermark-punch-in"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 水印打卡签到"
doc_id: "mcB3JSXDQw"
updated_at: "2026-08-28 10:26:33"
---

> Source: https://open.dingtalk.com/document/development/watermark-punch-in
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 水印打卡签到
> Updated: 2026-08-28 10:26:33

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.waterMarkModel`（object）：水印拍照信息。
- `data.waterMarkModel.mediaIdV2`（string，必填）：水印拍照地址2
- `data.waterMarkModel.mediaIdV1`（string，必填）：水印拍照地址
- `data.waterMarkModel.deviceId`（string，必填）：设备id
- `data.openConversationId`（string）：水印打卡群id。
- `data.extraInfo`（object）：扩展数据。
- `data.formCode`（string）：水印签到所使用的表单code。
- `data.formDataLists`（array）：表单数据。
- `data.formDataLists[].label`（string，必填）：表单单项item 的名称。
- `data.formDataLists[].value`（string，必填）：表单单项item的value。
- `data.formDataLists[].key`（string，必填）：表单单项item的key。
- `data.positionDataModel`（object）：位置信息。
- `data.positionDataModel.country`（string，必填）：国家
- `data.positionDataModel.detailPlace`（string，必填）：详细地址
- `data.positionDataModel.province`（string，必填）：省
- `data.positionDataModel.city`（string，必填）：市
- `data.positionDataModel.street`（string，必填）：街道
- `data.positionDataModel.district`（string，必填）：区
- `data.positionDataModel.latitude`（string，必填）：维度
- `data.positionDataModel.place`（string，必填）：短地址
- `data.positionDataModel.longitude`（string，必填）：经度

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `waterMarkModel`（object，必填）：水印拍照信息。
- `waterMarkModel.mediaIdV2`（string，必填）：水印拍照地址2
- `waterMarkModel.mediaIdV1`（string，必填）：水印拍照地址
- `waterMarkModel.deviceId`（string，必填）：设备id
- `openConversationId`（string，必填）：水印打卡群id。
- `extraInfo`（object，必填）：扩展数据。
- `formCode`（string，必填）：水印签到所使用的表单code。
- `formDataLists`（array，必填）：表单数据。
- `formDataLists[].label`（string，必填）：表单单项item 的名称。
- `formDataLists[].value`（string，必填）：表单单项item的value。
- `formDataLists[].key`（string，必填）：表单单项item的key。
- `positionDataModel`（object，必填）：位置信息。
- `positionDataModel.country`（string，必填）：国家
- `positionDataModel.detailPlace`（string，必填）：详细地址
- `positionDataModel.province`（string，必填）：省
- `positionDataModel.city`（string，必填）：市
- `positionDataModel.street`（string，必填）：街道
- `positionDataModel.district`（string，必填）：区
- `positionDataModel.latitude`（string，必填）：维度
- `positionDataModel.place`（string，必填）：短地址
- `positionDataModel.longitude`（string，必填）：经度

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.waterMarkModel`（object）：水印拍照信息。
- `biz_data.waterMarkModel.mediaIdV2`（string，必填）：水印拍照地址2
- `biz_data.waterMarkModel.mediaIdV1`（string，必填）：水印拍照地址
- `biz_data.waterMarkModel.deviceId`（string，必填）：设备id
- `biz_data.openConversationId`（string）：水印打卡群id。
- `biz_data.extraInfo`（object）：扩展数据。
- `biz_data.formCode`（string）：水印签到所使用的表单code。
- `biz_data.formDataLists`（array）：表单数据。
- `biz_data.formDataLists[].label`（string，必填）：表单单项item 的名称。
- `biz_data.formDataLists[].value`（string，必填）：表单单项item的value。
- `biz_data.formDataLists[].key`（string，必填）：表单单项item的key。
- `biz_data.positionDataModel`（object）：位置信息。
- `biz_data.positionDataModel.country`（string，必填）：国家
- `biz_data.positionDataModel.detailPlace`（string，必填）：详细地址
- `biz_data.positionDataModel.province`（string，必填）：省
- `biz_data.positionDataModel.city`（string，必填）：市
- `biz_data.positionDataModel.street`（string，必填）：街道
- `biz_data.positionDataModel.district`（string，必填）：区
- `biz_data.positionDataModel.latitude`（string，必填）：维度
- `biz_data.positionDataModel.place`（string，必填）：短地址
- `biz_data.positionDataModel.longitude`（string，必填）：经度

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
