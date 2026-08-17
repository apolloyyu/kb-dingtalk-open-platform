---
title: "打开模态框"
source_url: "https://open.dingtalk.com/document/development/open-modal-box"
namespace: "development"
slug: "open-modal-box"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开模态框"
doc_id: "0r6eUl5wvi"
updated_at: "2025-09-17 20:57:27"
---

> Source: https://open.dingtalk.com/document/development/open-modal-box
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开模态框
> Updated: 2025-09-17 20:57:27

# 打开模态框

调用**biz.util.openModal**打开模态框。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
dd.biz.util.openModal({
    size:'middle',  // modal的尺寸
    url:'https://test.dingtalk.com/modal.html', //打开modal的内容的url
    title: 'modal title', //顶部标题
    onSuccess : function(result) {
       /*
            调用biz.navigation.quit接口进入onSuccess, result为调用biz.navigation.quit传入的数值
        */
    },
    onFail : function() {
        /*
            tips:点击左上角关闭按钮会进入onFail
         */
    }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| size | String | 模态框的尺寸大小有三种选择，具体看下表。 |
| url | String | 模态框内部显示内容的url。 |
| title | String | 模态框标题。 |

**尺寸选择详情**：

| 名称 | size输入 | 尺寸长宽 |
| --- | --- | --- |
| 大模态框（默认） |  | 包括标题 676px \* 545px |
| 中模态框 | “middle” | 包括标题 440px \* 300px |
| 小模态框 | “mini” | 包括标题 366px \* 120px |
