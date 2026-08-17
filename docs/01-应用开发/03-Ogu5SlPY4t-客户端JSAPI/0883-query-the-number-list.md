---
title: "查询话单列表"
source_url: "https://open.dingtalk.com/document/development/query-the-number-list"
namespace: "development"
slug: "query-the-number-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 办公电话 > 查询话单列表"
doc_id: "9tE9ibx1nj"
updated_at: "2025-09-17 20:57:35"
---

> Source: https://open.dingtalk.com/document/development/query-the-number-list
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 办公电话 > 查询话单列表
> Updated: 2025-09-17 20:57:35

# 查询话单列表

调用**biz.conference.getCloudCallList**查询话单列表。

## 使用说明

查询话单列表。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥6.0.0） | 支持（钉钉版本≥6.0.0） | 支持（钉钉版本≥6.0.9） |

```
dd.biz.conference.getCloudCallList ({
     "corpId":"xxx",
     "sessionId":"xxx",
     "bizNumber":"057xxxx5188",
     "startTime":"2020-12-01 00:00:00",
     "endTime":"2020-12-31 23:59:59",
     "staffIdList":["xxx","xxx"],
     "direction":0,
     "index":0,
     "pageSize":100,
      onSuccess:function(result) {
      // onSuccess将在查询成功之后回调
       /* 话单result结构
      {
          gmtCreate:long,
          sessionId:String,
          bizNumber:String,
          callerStaffId:String,
          callerName:String,
          callerNumber:String,
          calleeName:String,
          calleeNumber:String,
          calleeStaffId:String,
          billsec:long,
          billsecMin:long,
          business:String,
          relation:int,  //关系   1：同事，2：外部联系人 3：Other
          direction:int, //类型，0打出,1打入
          calleeType:String,//拨打类型 0手机 1 固话
          sndRecStatus:Integer, //录音状态 0：无录音，1：录音生成中，2：录音已生成，3：录音已删除
          recordUrl:String //录音地址
      }
     */
   },
  onFail:function(err) {
}
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业corpId。 |
| sessionId | String | 否 | 指定会议Id。 |
| bizNumber | String | 否 | 外呼的被叫号码。 |
| startTime | String | 是 | 开始时间 |
| endTime | String | 是 | 结束时间 |
| staffIdList | Array<String> | 否 | 指定查询员工列表 |
| direction | Number | 是 | - **0**（默认）：外呼 - **1**：呼入 |
| index | Number | 是 | 起始页，从0开始。 |
| pageSize | Number | 是 | 每页个数，最大100。 |

## 返回结果

**成功**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 返回码。  **200**：正常 |
| cause | String | 异常描述。 |
| total | Number | 查询总数。 |
| hasMore | Boolean | 是否还有下一页。 |
| currentIndex | Number | 当前查询页。 |
| callList | Array<Object> | 话单列表。 |

**失败**

| error | 描述 |
| --- | --- |
| 1001 | 参数无效。 |
| 3003 | 没有权限。 |
