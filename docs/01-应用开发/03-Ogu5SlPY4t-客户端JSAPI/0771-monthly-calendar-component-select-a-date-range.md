---
title: "月历组件：选择半天"
source_url: "https://open.dingtalk.com/document/development/monthly-calendar-component-select-a-date-range"
namespace: "development"
slug: "monthly-calendar-component-select-a-date-range"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 月历组件：选择半天"
doc_id: "PSiYs7ihC0"
updated_at: "2025-09-17 20:56:13"
---

> Source: https://open.dingtalk.com/document/development/monthly-calendar-component-select-a-date-range
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 月历组件：选择半天
> Updated: 2025-09-17 20:56:13

# 月历组件：选择半天

调用**biz.calendar.chooseHalfDay**月历组件，选择半天。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.calendar.chooseHalfDay)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.calendar.chooseHalfDay({
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
| chosen | 时间戳，用户选择的时间，单位为毫秒。 |
| timezone | 整型，用户当前所在时区。 |
