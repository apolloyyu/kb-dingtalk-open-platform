---
title: "createDing"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-ding"
namespace: "development"
slug: "jsapi-create-ding"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "DING > createDing"
doc_id: "H4xMePjdmM"
updated_at: "2025-08-27 18:08:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-ding
> Path: 应用开发 / 客户端 JSAPI / DING > createDing
> Updated: 2025-08-27 18:08:56

# createDing

调用createDing，发起DING。

发钉接口支持唤起DING、任务、日程等创建界面

> 目前发钉只支持客户端发钉，不支持直接通过服务端发钉。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10313) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10313) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `taskInfo`（object）：任务信息。
- `taskInfo.ccUsers`（array）：抄送用户列表。
- `taskInfo.taskRemind`（number）：任务提醒时间：  
    
  \* 0：不提醒；  
  \* 15：提前15分钟；  
  \* 60：提前1个小时；  
  \* 180：提前3个小时；  
  \* 1440：提前一天
- `taskInfo.deadlineTime`（object）：任务截止时间。
- `taskInfo.deadlineTime.format`（string）：日期格式
- `taskInfo.deadlineTime.value`（string）：日期时间和格式要对应
- `users`（array，必填）：需要发送到的用户的userid列表。
- `type`（number）：附件类型：  
    
  \* 1：图片  
  \* 2：链接
- `alertType`（number）：钉提醒类型：  
    
  \* 0：电话  
  \* 1：短信  
  \* 2：应用内
- `alertDate`（object）：钉提醒时间
- `alertDate.format`（string）：日期格式
- `alertDate.value`（string）：日期时间和格式要对应
- `attachment`（object）：附件信息。
- `attachment.images`（array）：图片附件列表
- `text`（string）：消息体。
- `confInfo`（object）：会议信息。
- `confInfo.bizSubType`（number）：会议类型  
    
  \* 0：预约会议；  
  \* 1：预约电话会议；  
  \* 2：预约视频会议；
- `confInfo.remindType`（number）：会议提前提醒方式。  
    
  \* 0:电话  
  \* 1:短信  
  \* 2:应用内
- `confInfo.location`（string）：会议地点
- `confInfo.startTime`（object）：会议开始时间
- `confInfo.startTime.format`（string）：日期格式
- `confInfo.startTime.value`（string）：日期时间和格式要对应
- `confInfo.endTime`（object）：会议结束时间
- `confInfo.endTime.format`（string）：日期格式
- `confInfo.endTime.value`（string）：日期时间和格式要对应
- `confInfo.remindMinutes`（number）：会前提醒  
    
  \*1：不提醒；  
  \* 0：事件发生时提醒；  
  \* 5：提前5分钟；  
  \* 15：提前15分钟；  
  \* 30：提前30分钟；  
  \* 60：提前1个小时；  
  \* 1440：提前一天；
- `corpId`（string）：企业corpId。  
    
  > H5微应用必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.createDing({
  text: '钉消息内容',
  type: 1,
  users: ['03333', '04333'],
  corpId: `corpId示例值`,
  confInfo: {
    endTime: { value: '2015-05-09 08:00', format: 'yyyy-MM-dd HH:mm' },
    location: `location示例值`,
    startTime: { value: '2015-05-09 08:00', format: 'yyyy-MM-dd HH:mm' },
    bizSubType: 27,
    remindType: 2,
    remindMinutes: 30,
  },
  taskInfo: {
    ccUsers: ['100', '101'],
    taskRemind: 30,
    deadlineTime: { value: '2015-05-09 08:00', format: 'yyyy-MM-dd HH:mm' },
  },
  alertDate: { value: '2015-05-09 08:00', format: 'yyyy-MM-dd HH:mm' },
  alertType: 1,
  attachment: { images: ['https://xxx.com/example1.png'] },
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
