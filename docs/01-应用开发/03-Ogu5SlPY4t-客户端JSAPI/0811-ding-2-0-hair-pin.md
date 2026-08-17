---
title: "DING 2.0 发钉"
source_url: "https://open.dingtalk.com/document/development/ding-2-0-hair-pin"
namespace: "development"
slug: "ding-2-0-hair-pin"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > DING > DING 2.0 发钉"
doc_id: "N1HWiaWluf"
updated_at: "2025-09-17 20:56:41"
---

> Source: https://open.dingtalk.com/document/development/ding-2-0-hair-pin
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > DING > DING 2.0 发钉
> Updated: 2025-09-17 20:56:41

# DING 2.0 发钉

调用**biz.ding.create**实现DING 2.0 发钉。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.ding.create)在线调试该接口。

## 使用说明

DING 2.0发钉接口支持打开DING、任务、会议界面。

> **[!IMPORTANT]**
>
> 目前发钉只支持客户端发钉，不支持直接通过服务端发钉。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 4.5.9版本以上支持 |

```
dd.biz.ding.create({
    users : ['100', '101'],
    corpId: '', 
    type: 1, 
    alertType: 2, 
    alertDate: {"format":"yyyy-MM-dd HH:mm","value":"2015-05-09 08:00"},
    attachment: {
        images: [''],
    }, 
    text: '',  
    bizType :0, 
    confInfo:{
       bizSubType:0, //子业务类型如会议：0：预约会议；1：预约电话会议；2：预约视频会议；（注：目前只有会议才有子业务类型）
       location:'某某会议室' ,  //会议地点；（非必填）
       startTime:{"format":"yyyy-MM-dd HH:mm","value":"2015-05-09 08:00"},  //会议开始时间
       endTime:{"format":"yyyy-MM-dd HH:mm","value":"2015-05-09 08:00"},   //会议结束时间
       remindMinutes:30,  //会前提醒。单位分钟-1：不提醒；0：事件发生时提醒；5：提前5分钟；15：提前15分钟；30：提前30分钟；60：提前1个小时；1440：提前一天；
       remindType:2   //会议提前提醒方式。0:电话, 1:短信, 2:应用内
    },
 
    taskInfo:{
       ccUsers: ['100', '101'],  //抄送用户列表，工号
       deadlineTime:{"format":"yyyy-MM-dd HH:mm","value":"2015-05-09 08:00"} ,   //任务截止时间
       taskRemind:30  //任务提醒时间，单位分钟0：不提醒；15：提前15分钟；60：提前1个小时；180：提前3个小时；1440：提前一天；
    },
 
    onSuccess:function() {
         //onSuccess将在点击发送之后调用
    },
    onFail:function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| users | Array[String] | 用户的userid列表。 |
| corpId | String | 企业的corpId。 |
| type | Number | 附件类型：   - **1**：图片 - **2**：链接 |
| alertType | Number | 钉提醒类型：   - **0**：电话 - **1**：短信 - **2**：应用内 |
| alertDate | Object | 钉提醒时间，格式为yyyy-MM-dd HH:mm。 |
| attachment | Object | 附件信息。 |
| text | String | 消息体。 |
| bizType | Number | 业务类型：   - **0**：通知DING - **1**：任务 - **2**：会议 |
| confInfo | Object | 会议信息。 |
| taskInfo | Object | 任务信息。 |
