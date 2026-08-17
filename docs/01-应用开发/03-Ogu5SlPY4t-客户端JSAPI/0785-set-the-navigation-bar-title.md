---
title: "设置导航栏标题"
source_url: "https://open.dingtalk.com/document/development/set-the-navigation-bar-title"
namespace: "development"
slug: "set-the-navigation-bar-title"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 设置导航栏标题"
doc_id: "MyP46Qr3TA"
updated_at: "2025-09-17 20:56:23"
---

> Source: https://open.dingtalk.com/document/development/set-the-navigation-bar-title
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 设置导航栏标题
> Updated: 2025-09-17 20:56:23

# 设置导航栏标题

调用**biz.navigation.setTitle**设置导航栏标题。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.navigation.setTitle)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

此JSAPI在iOS和Android上的显示不同，如下图所示：

- 根据iOS的设计规范，iOS的标题在导航栏正中央。

  ![ios导航栏标题](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177931.png)
- 根据Android的设计规范，标题显示在导航栏左侧。

  ![android公告](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177932.png)
- PC端：只在SlidePanel和Modal里起作用。

```
dd.biz.navigation.setTitle({
    title : '邮箱正文',//控制标题文本，空字符串表示显示默认文本
    onSuccess : function(result) {
        /*结构
        {
        }*/
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| title | String | 控制标题文本，空字符串表示显示默认文本。 |
