---
title: "modal弹浮层"
source_url: "https://open.dingtalk.com/document/development/modal-pop-up-layer"
namespace: "development"
slug: "modal-pop-up-layer"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > modal弹浮层"
doc_id: "2cVyjGOscA"
updated_at: "2025-09-17 20:56:31"
---

> Source: https://open.dingtalk.com/document/development/modal-pop-up-layer
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > modal弹浮层
> Updated: 2025-09-17 20:56:31

# modal弹浮层

调用**device.notification.modal**实现modal弹浮层。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.modal)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.notification.modal({
    image:"http://gw.alicdn.com/tps/i2/TB1SlYwGFXXXXXrXVXX9vKJ2XXX-2880-1560.jpg_200x200.jpg", // 标题图片地址
    banner:["http://gw.alicdn.com/tps/i2/TB1SlYwGFXXXXXrXVXX9vKJ2XXX-2880-1560.jpg_200x200.jpg"],   // 图片地址列表
    title:"2.4版本更新", //标题
    content:"1.功能更新2.功能更新;", //文本内容
    buttonLabels:["了解更多","知道了"],// 最多两个按钮，至少有一个按钮
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
| image | String | 图片地址。  若设置了banner，则image不会生效，默认展示banner图片。 |
| banner | Array | 图片地址数组。 |
| title | String | 标题。 |
| content | String | 文本内容。 |
| buttonLabels | Array[String] | 其他按钮列表。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| buttonIndex | 被点击按钮的索引值，Number，从0开始。 |
