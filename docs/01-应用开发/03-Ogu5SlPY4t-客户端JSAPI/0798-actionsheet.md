---
title: "actionsheet"
source_url: "https://open.dingtalk.com/document/development/actionsheet"
namespace: "development"
slug: "actionsheet"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > actionsheet"
doc_id: "6wTwpR5sDl"
updated_at: "2025-09-17 20:56:32"
---

> Source: https://open.dingtalk.com/document/development/actionsheet
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > actionsheet
> Updated: 2025-09-17 20:56:32

# actionsheet

调用**device.notification.actionSheet**实现actionsheet弹窗。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.actionSheet)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.device.notification.actionSheet({
    title: "谁是最棒哒？", //标题
    cancelButton: '取消', //取消按钮文本
    otherButtons: ["孙悟空","猪八戒","唐僧","沙和尚"],
    onSuccess : function(result) {
        //onSuccess将在点击button之后回调
        /*{
            buttonIndex: 0 //被点击按钮的索引值，Number，从0开始, 取消按钮为-1
        }*/
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| title | String | 标题。 |
| cancelButton | String | 取消按钮文本。 |
| otherButtons | Array[String] | 其他按钮列表。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| buttonIndex | 被点击按钮的索引值，Number，从0开始，取消按钮为-1。 |
