---
title: "月历组件：选择某天"
source_url: "https://open.dingtalk.com/document/development/monthly-calendar-component-select-a-certain-day"
namespace: "development"
slug: "monthly-calendar-component-select-a-certain-day"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 月历组件：选择某天"
doc_id: "gPvMhsXyw9"
updated_at: "2025-09-17 20:56:12"
---

> Source: https://open.dingtalk.com/document/development/monthly-calendar-component-select-a-certain-day
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 月历组件：选择某天
> Updated: 2025-09-17 20:56:12

# 月历组件：选择某天

调用**biz.calendar.chooseOneDay**月历组件，选择某天。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.calendar.chooseOneDay)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.calendar.chooseOneDay({
    default:1494415396228,
    onSuccess : function(result) {
        //onSuccess将在点击确定之后回调
        /*{
            chosen:1494345600000,
            timezone:8
        }
        */
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| default | Long | 时间戳，默认选中时间，单位为毫秒。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| chosen | 时间戳，用户选择日期当日0点的时间(在用户时区)，单位为毫秒。 |
| timezone | 整型，用户当前所在时区。 |
