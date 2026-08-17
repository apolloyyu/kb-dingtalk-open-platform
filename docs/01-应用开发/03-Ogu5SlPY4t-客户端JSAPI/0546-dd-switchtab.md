---
title: "跳转到指定tabBar页面"
source_url: "https://open.dingtalk.com/document/development/dd-switchtab"
namespace: "development"
slug: "dd-switchtab"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > TabBar > 跳转到指定tabBar页面"
doc_id: "Zwvwp34kat"
updated_at: "2025-09-17 20:59:08"
---

> Source: https://open.dingtalk.com/document/development/dd-switchtab
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > TabBar > 跳转到指定tabBar页面
> Updated: 2025-09-17 20:59:08

# 跳转到指定tabBar页面

调用**dd.switchTab**跳转到指定 tabBar 页面，并关闭其他所有非 tabBar 页面。

## 扫码体验

![1595557193914-1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9306803061/p172077.png)

## **示例代码**

```
// app.json
{
  "tabBar": {
    "items": [{
      "pagePath": "home",
      "name": "首页"
    },{
      "pagePath": "user",
      "name": "用户"
    }]
  }
}
```

```
dd.switchTab({
  url: '/home'
})
```

## **入参**

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| url | String | 是 | 跳转的 tabBar 页面的路径（需在 app.json 的 tabBar 字段定义的页面）。  **[!IMPORTANT]**  路径后不能带参数。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
