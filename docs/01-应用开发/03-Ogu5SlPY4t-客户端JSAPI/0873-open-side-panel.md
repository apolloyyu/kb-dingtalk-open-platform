---
title: "打开侧边面板"
source_url: "https://open.dingtalk.com/document/development/open-side-panel"
namespace: "development"
slug: "open-side-panel"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开侧边面板"
doc_id: "LU2u9bbcwm"
updated_at: "2025-09-17 20:57:28"
---

> Source: https://open.dingtalk.com/document/development/open-side-panel
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开侧边面板
> Updated: 2025-09-17 20:57:28

# 打开侧边面板

调用**biz.util.openSlidePanel**打开侧边面板。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
dd.biz.util.openSlidePanel({
    url: 'about:blank', //打开侧边栏的url
    title: 'title', //侧边栏顶部标题
    onSuccess : function(result) {
       /*
            调用biz.navigation.quit接口进入onSuccess, result为调用biz.navigation.quit传入的数值
        */
    },
    onFail : function() {
        /*
            tips:点击右上角上角关闭按钮会进入onFail
         */
    }
})
```
