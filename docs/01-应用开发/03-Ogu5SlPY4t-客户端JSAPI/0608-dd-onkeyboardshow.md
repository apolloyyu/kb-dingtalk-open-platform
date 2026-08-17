---
title: "监听键盘弹起事件"
source_url: "https://open.dingtalk.com/document/development/dd-onkeyboardshow"
namespace: "development"
slug: "dd-onkeyboardshow"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 键盘 > 监听键盘弹起事件"
doc_id: "qMPAK4iymj"
updated_at: "2025-09-17 20:59:45"
---

> Source: https://open.dingtalk.com/document/development/dd-onkeyboardshow
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 键盘 > 监听键盘弹起事件
> Updated: 2025-09-17 20:59:45

# 监听键盘弹起事件

调用**dd.onKeyboardShow**监听键盘弹起事件，并返回键盘高度。

## **示例****代码**

```
Page({
    onKeyboardShow(res) {
        dd.alert({
            content: 'keyboard show, height = ' + res.data.height
        })
    }
})
```

## 入参

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data.height | Number | 获取键盘高度，单位为px。  **[!IMPORTANT]**  需要在page中设置该回调。 |
