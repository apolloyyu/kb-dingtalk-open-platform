---
title: "输入框"
source_url: "https://open.dingtalk.com/document/development/input-box"
namespace: "development"
slug: "input-box"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > UI控件 > 输入框"
doc_id: "vgViHrk3NH"
updated_at: "2025-09-17 20:57:08"
---

> Source: https://open.dingtalk.com/document/development/input-box
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > UI控件 > 输入框
> Updated: 2025-09-17 20:57:08

# 输入框

调用**ui.input.plain**设置输入框基本信息。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=ui.input.plain)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.ui.input.plain({
    placeholder: '说点什么吧', //占位符
    text: '', //默认填充文本
    onSuccess: function(data) {
        //onSuccess将在点击发送之后调用
        /*{
            text: String
        }*/
    },
    onFail: function() {
 
    }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| placeholder | String | 占位符。 |
| text | String | 默认填充文本。 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| text | String | 返回文本。 |
