---
title: "confirm"
source_url: "https://open.dingtalk.com/document/development/confirm"
namespace: "development"
slug: "confirm"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > confirm"
doc_id: "iAFlVT4YMa"
updated_at: "2025-09-17 20:56:34"
---

> Source: https://open.dingtalk.com/document/development/confirm
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > confirm
> Updated: 2025-09-17 20:56:34

# confirm

调用**device.notification.confirm**显示确认框，可以配置确认框的标题、内容、按钮的文字等。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.confirm)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
    dd.device.notification.confirm({
    message: "确认取消吗",
    title: "提示",
    buttonLabels: ['是', '否'],
    onSuccess : function(result) {
        //onSuccess将在点击button之后回调
        /*
        {
            buttonIndex: 0 //被点击按钮的索引值，Number类型，从0开始
        }
        */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | String | 消息内容。 |
| title | String | 标题。 |
| buttonLabels | Array[String] | 按钮名称。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| buttonIndex | 被点击按钮的索引值，Number类型，从0开始。 |
