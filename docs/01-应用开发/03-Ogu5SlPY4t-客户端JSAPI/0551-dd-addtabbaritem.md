---
title: "添加tabBar页面"
source_url: "https://open.dingtalk.com/document/development/dd-addtabbaritem"
namespace: "development"
slug: "dd-addtabbaritem"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > TabBar > 添加tabBar页面"
doc_id: "xdGFbWTcEy"
updated_at: "2025-09-17 20:59:10"
---

> Source: https://open.dingtalk.com/document/development/dd-addtabbaritem
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > TabBar > 添加tabBar页面
> Updated: 2025-09-17 20:59:10

# 添加tabBar页面

调用**dd.addTabBarItem**添加tabBar页面。

> **[!IMPORTANT]**
>
> 使用该接口请注意：
>
> - addTabBarItem最多调用90次。
> - addTabBarItem 调用时，要保证当前小程序展示的是TabBar上的页面；否则调用会报错，错误码 11。
> - addTabBarItem 不可对主 tabBar 页面进行替换。
> - tabBar 最多为 5个。

## **入参说明**

| **参数名** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| name | String | 是 | tab标题。 |
| icon | String | 否 | 图标。 |
| activeIcon | String | 否 | 选中时的图标。 |
| pagePath | String | 是 | TabItem对应的页面路径，需要配置在小程序配置文件中。 |
| index | Number | 是 | Item插入位置，原位置的页面将后移一个位置，从 0 开始。 |
| success | Function | 否 | 成功回调。 |
| fail | Function | 否 | 失败回调。 |
| complete | Function | 否 | 成功或失败回调。 |

## **什么是主 tabbar 页面**

当小程序被启动后，第一个被初始化的 tabBar 页面。

## **兼容性判断**

使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('addTabBarItem')进行兼容性判断 。
