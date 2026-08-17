---
title: "关闭页面"
source_url: "https://open.dingtalk.com/document/development/close-page"
namespace: "development"
slug: "close-page"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 关闭页面"
doc_id: "Wf7mc2y4dQ"
updated_at: "2025-09-17 20:56:26"
---

> Source: https://open.dingtalk.com/document/development/close-page
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 关闭页面
> Updated: 2025-09-17 20:56:26

# 关闭页面

调用**biz.navigation.quit**关闭页面。

## 使用说明

> **[!IMPORTANT]**
>
> 只在SlidePanel和Modal里起作用。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
dd.biz.navigation.quit({
    message: "quit message",//退出信息，传递给openModal或者openSlidePanel的onSuccess函数的result参数
    onSuccess : function(result) {
        /**/
    },
    onFail : function() {}
})
```

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | String | 退出信息，传递给openModal或者openSlidePanel的onSuccess函数的result参数：   - message参数仅支持字符串或者数字。 - 如果未传入message，则传递给openModal的值为随机值。 |
