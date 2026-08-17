---
title: "日期选择器"
source_url: "https://open.dingtalk.com/document/development/date-selector"
namespace: "development"
slug: "date-selector"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 日期选择器"
doc_id: "VdgKr916us"
updated_at: "2025-09-17 20:56:10"
---

> Source: https://open.dingtalk.com/document/development/date-selector
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 日期和月历 > 日期选择器
> Updated: 2025-09-17 20:56:10

# 日期选择器

调用**biz.util.datepicker**日期选择器。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.datepicker)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.datepicker({
    format: 'yyyy-MM-dd',//注意：format只支持android系统规范，即2015-03-31格式为yyyy-MM-dd
    value: '2015-04-17', //默认显示日期
    onSuccess : function(result) {
        //onSuccess将在点击完成之后回调
        /*{
            value: "2015-02-10"
        }
        */
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| format | String | format只支持Android系统规范，即yyyy-MM-dd，例如2020-10-29。 |
| value | String | 默认显示日期。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| value | 返回选择的日期。 |

展示效果如下图所示：

> **[!IMPORTANT]**
>
>  Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

![选择日期](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1505834061/p177573.png)
