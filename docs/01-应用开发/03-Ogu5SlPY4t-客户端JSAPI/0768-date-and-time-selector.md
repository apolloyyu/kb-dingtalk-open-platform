---
title: "日期及时间选择器"
source_url: "https://open.dingtalk.com/document/development/date-and-time-selector"
namespace: "development"
slug: "date-and-time-selector"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 日期及时间选择器"
doc_id: "AZluCjhJea"
updated_at: "2025-09-17 20:56:11"
---

> Source: https://open.dingtalk.com/document/development/date-and-time-selector
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 日期及时间选择器
> Updated: 2025-09-17 20:56:11

# 日期及时间选择器

调用**biz.util.datetimepicker**日期及时间选择器。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.datetimepicker)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.datetimepicker({
    format: 'yyyy-MM-dd HH:mm',
    value: '2015-04-17 08:00', //默认显示
    onSuccess : function(result) {
        //onSuccess将在点击完成之后回调
        /*{
            value: "2015-06-10 09:50"
        }
        */
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| format | String | 日期和时间的格式：yyyy-MM-dd HH:mm。 |
| value | String | 默认显示的日期和时间。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| value | 返回选择的日期和时间。 |
