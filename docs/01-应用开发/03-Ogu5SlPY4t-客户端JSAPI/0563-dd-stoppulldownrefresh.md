---
title: "停止下拉刷新"
source_url: "https://open.dingtalk.com/document/development/dd-stoppulldownrefresh"
namespace: "development"
slug: "dd-stoppulldownrefresh"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 下拉刷新 > 停止下拉刷新"
doc_id: "4kZyClbhqq"
updated_at: "2025-09-17 20:59:19"
---

> Source: https://open.dingtalk.com/document/development/dd-stoppulldownrefresh
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 下拉刷新 > 停止下拉刷新
> Updated: 2025-09-17 20:59:19

# 停止下拉刷新

当处理完数据刷新后，调用**dd.stopPullDownRefresh**可停止当前页面的下拉刷新。

## **示例****代码**

```
Page({
  onPullDownRefresh(){
    dd.stopPullDownRefresh()
  }
})
```
