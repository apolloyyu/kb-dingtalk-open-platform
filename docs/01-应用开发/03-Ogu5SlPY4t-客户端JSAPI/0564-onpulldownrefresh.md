---
title: "下拉刷新"
source_url: "https://open.dingtalk.com/document/development/onpulldownrefresh"
namespace: "development"
slug: "onpulldownrefresh"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 下拉刷新 > 下拉刷新"
doc_id: "DzgO3yfU1r"
updated_at: "2025-09-17 20:59:20"
---

> Source: https://open.dingtalk.com/document/development/onpulldownrefresh
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 下拉刷新 > 下拉刷新
> Updated: 2025-09-17 20:59:20

# 下拉刷新

调用**onPullDownRefresh**下拉刷新。

在 Page 中自定义 onPullDownRefresh 函数，可以监听该页面用户的下拉刷新事件：

1. 需要在页面对应的`.json`配置文件中配置`"pullRefresh": true`选项，才能开启下拉刷新事件
2. 当处理完数据刷新后，调用dd.stopPullDownRefresh可以停止当前页面的下拉刷新。

## 扫码体验

![1595556694933-1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5278903061/p171189.png)

## **示例****代码**

pull-down-refresh.json 配置文件中的代码配置如下：

```
{
    "pullRefresh": true
}
```

Page 中定义 onPullDownRefresh 处理函数：

```
onPullDownRefresh() {
    console.log('onPullDownRefresh', new Date())
}
```
