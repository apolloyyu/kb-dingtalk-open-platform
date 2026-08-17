---
title: "监听键盘收起事件"
source_url: "https://open.dingtalk.com/document/development/dd-onkeyboardhide"
namespace: "development"
slug: "dd-onkeyboardhide"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 键盘 > 监听键盘收起事件"
doc_id: "6e4qvWs1c0"
updated_at: "2025-09-17 20:59:46"
---

> Source: https://open.dingtalk.com/document/development/dd-onkeyboardhide
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 键盘 > 监听键盘收起事件
> Updated: 2025-09-17 20:59:46

# 监听键盘收起事件

调用**dd.onKeyboardHide**监听键盘收起事件。需要在page中设置该回调。

## **示例代码**

```
Page({
    onKeyboardHide() {
        dd.alert({
            content: 'keyboard hide'
        })
    },
})
```
