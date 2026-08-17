---
title: "标题栏添加问号图标"
source_url: "https://open.dingtalk.com/document/development/title-bar-add-question-mark-icon"
namespace: "development"
slug: "title-bar-add-question-mark-icon"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 标题栏添加问号图标"
doc_id: "UTTgIYcB5U"
updated_at: "2025-09-17 20:56:24"
---

> Source: https://open.dingtalk.com/document/development/title-bar-add-question-mark-icon
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 标题栏添加问号图标
> Updated: 2025-09-17 20:56:24

# 标题栏添加问号图标

调用**biz.navigation.setIcon**标题栏添加问号图标。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.navigation.setIcon)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

此JSAPI在iOS和Android上的显示不同，如下图所示：

- 显示在导航栏标题的旁边，紧靠着标题。

  ![ios导航栏标题](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177931.png)
- 显示在导航栏右侧按钮组的最左边。

  ![android公告](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177932.png)

```
dd.biz.navigation.setIcon({
    showIcon : true,//是否显示icon
    iconIndex : 1,//显示的iconIndex, 如上图
    onSuccess : function(result) {
        /*结构
        {
        }*/
        //点击icon之后将会回调这个函数
    },
    onFail : function(err) {
    //jsapi调用失败将会回调此函数
    }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| showIcon | Boolean | 是否显示icon。 |
| iconIndex | Number | 显示的iconIndex，如下图。 |

![图标 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177951.png)
