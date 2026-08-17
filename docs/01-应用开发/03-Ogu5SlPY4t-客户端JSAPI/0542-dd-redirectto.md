---
title: "页面跳转（关闭当前页）"
source_url: "https://open.dingtalk.com/document/development/dd-redirectto"
namespace: "development"
slug: "dd-redirectto"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 导航栏 > 页面跳转（关闭当前页）"
doc_id: "ingyz6qoi0"
updated_at: "2025-09-17 20:59:05"
---

> Source: https://open.dingtalk.com/document/development/dd-redirectto
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 导航栏 > 页面跳转（关闭当前页）
> Updated: 2025-09-17 20:59:05

# 页面跳转（关闭当前页）

调用**dd.redirectTo**跳转到应用内的某个指定页面，并关闭当前页面。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4354199951/p163551.png)

## 示例代码

```
dd.redirectTo({
  url: 'new_page?count=100'
})
```

## 入参

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| url | String | 是 | 需要跳转的应用内非 tabBar 的目标页面路径，路径后可以带参数。  参数规则如下：路径与参数之间使用`?`分隔，参数键与参数值用`=`相连，不同参数必须用`&`分隔；如`path?key1=value1&key2=value2。` |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
