---
title: "getCurrentPages 方法"
source_url: "https://open.dingtalk.com/document/development/getcurrentpages-methods-1"
namespace: "development"
slug: "getcurrentpages-methods-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序页面配置 > getCurrentPages 方法"
doc_id: "SsxhMSUHHA"
updated_at: "2025-09-17 20:57:55"
---

> Source: https://open.dingtalk.com/document/development/getcurrentpages-methods-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序页面配置 > getCurrentPages 方法
> Updated: 2025-09-17 20:57:55

# getCurrentPages 方法

getCurrentPages()函数用于获取当前页面栈的实例，以数组形式按栈的顺序给出，第一个元素为首页，最后一个元素为当前页面。

下面代码可以用于检测当前页面栈是否具有5层页面深度：

```
if(getCurrentPages().length === 5) {
  dd.redirectTo({url:'/xx'});
} else {
  dd.navigateTo({url:'/xx'});
}
```

> **[!IMPORTANT]**
>
> 不要尝试修改页面栈，会导致路由以及页面状态错误。

框架以栈的形式维护了当前的所有页面。 当发生路由切换的时候，页面栈的表现如下：

| 路由方式 | 页面栈表现 |
| --- | --- |
| 初始化 | 新页面入栈 |
| 打开新页面 | 新页面入栈 |
| 页面重定向 | 当前页面出栈，新页面入栈 |
| 页面返回 | 当前页面出栈 |
| Tab 切换 | 页面全部出栈，只留下新的 Tab 页面 |
