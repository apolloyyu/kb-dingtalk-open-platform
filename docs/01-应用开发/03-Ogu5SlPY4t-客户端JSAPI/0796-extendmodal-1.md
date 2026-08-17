---
title: "extendModal"
source_url: "https://open.dingtalk.com/document/development/extendmodal-1"
namespace: "development"
slug: "extendmodal-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > extendModal"
doc_id: "Li6A05iNij"
updated_at: "2025-09-17 20:56:31"
---

> Source: https://open.dingtalk.com/document/development/extendmodal-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > extendModal
> Updated: 2025-09-17 20:56:31

# extendModal

调用**device.notification.extendModal**增强版modal弹浮层，支持自定义每一个Cell的内容。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.extendModal)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.notification.extendModal({
    cells: [
        {
        "image":"https://img.alicdn.com/tfs/TB1KzrwRFXXXXasXXXXXXXXXXXX-540-380.png",
        "title":"DEMO版本更新",
        "content":"图片尺寸是540x380;"
        },
        {
        "image":"https://img.alicdn.com/tfs/TB1KzrwRFXXXXasXXXXXXXXXXXX-540-380.png",
        "title":"DEMO版本更新",
        "content":"图片尺寸是540x380;"
        }
    ],
    buttonLabels:["了解更多","知道了"],// 最多两个按钮，至少有一个按钮。
    onSuccess : function(result) {
        //onSuccess将在点击button之后回调
        /*{
            buttonIndex: 0 //被点击按钮的索引值，Number，从0开始
        }*/
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| cells | Array | 浮层元素数组，每一个item为一个包含image、title、content内容的对象。 |
| image | String | 图片地址。 |
| title | String | 标题。 |
| content | String | 文本内容。 |
| buttonLabels | Array[String] | 按钮列表。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| buttonIndex | 被点击按钮的索引值，Number，从0开始。 |
