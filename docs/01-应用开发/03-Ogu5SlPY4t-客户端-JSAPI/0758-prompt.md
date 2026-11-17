---
title: "prompt"
source_url: "https://open.dingtalk.com/document/development/prompt"
namespace: "development"
slug: "prompt"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > prompt"
doc_id: "SAXN9qRFIS"
updated_at: "2026-09-01 10:42:01"
---

> Source: https://open.dingtalk.com/document/development/prompt
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > prompt
> Updated: 2026-09-01 10:42:01

# prompt

调用**device.notification.prompt**显示可提示用户进行输入的对话框，可以配置输入框的标题、内容、提示、按钮的文字等。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.prompt)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
    dd.device.notification.prompt({
    message: "再说一遍？",
    title: "提示",
    defaultText:"默认提示",
    buttonLabels: ['继续', '不玩了'],
    onSuccess : function(result) {
        //onSuccess将在点击button之后回调
        /*
        {
            buttonIndex: 0, //被点击按钮的索引值，Number类型，从0开始
            value: '' //输入的值
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
| value | 输入的值。 |
