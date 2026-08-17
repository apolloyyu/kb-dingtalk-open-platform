---
title: "月历组件：选择日期区间"
source_url: "https://open.dingtalk.com/document/development/month-calendar-component-select-date-range"
namespace: "development"
slug: "month-calendar-component-select-date-range"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 月历组件：选择日期区间"
doc_id: "GGSBC3JEhk"
updated_at: "2025-09-17 20:56:14"
---

> Source: https://open.dingtalk.com/document/development/month-calendar-component-select-date-range
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 月历组件：选择日期区间
> Updated: 2025-09-17 20:56:14

# 月历组件：选择日期区间

调用**biz.calendar.chooseInterval**月历组件，选择日期区间。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.calendar.chooseInterval)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.calendar.chooseInterval({
    defaultStart:1494415396228,
    defaultEnd:1494415396228,
    onSuccess : function(result) {
        //onSuccess将在点击确定之后回调
        /*{
            start: 1514908800000,
            end: 1514995200000,
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
| defaultStart | Long | 时间戳，默认选中时间，单位为毫秒。 |
| defaultEnd | Long | 时间戳，默认选中时间，单位为毫秒。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| start | 时间戳，为起始当日0点的时间，单位为毫秒。 |
| end | 时间戳，为截止当日0点的时间，单位为毫秒。 |
| timezone | 整型，用户当前所在时区。 |
