---
title: "dd.corpId"
source_url: "https://open.dingtalk.com/document/development/dd-corpid"
namespace: "development"
slug: "dd-corpid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > dd.corpId"
doc_id: "e9s7mOhK8t"
updated_at: "2025-09-17 20:58:42"
---

> Source: https://open.dingtalk.com/document/development/dd-corpid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > dd.corpId
> Updated: 2025-09-17 20:58:42

# dd.corpId

使用**dd.corpId**接口获取当前访问用户的企业corpId。

## 示例代码

```
Page({
  onReady() {
    // 页面加载完成
    dd.alert({
      content: dd.corpId,
    })
  },
});
```

## 返回值

为String类型，表示当前访问用户的企业corpId。
