---
title: "移除tabBar页面"
source_url: "https://open.dingtalk.com/document/development/dd-removetabbaritem"
namespace: "development"
slug: "dd-removetabbaritem"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > TabBar > 移除tabBar页面"
doc_id: "SAAEFN2sXU"
updated_at: "2025-09-17 20:59:11"
---

> Source: https://open.dingtalk.com/document/development/dd-removetabbaritem
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > TabBar > 移除tabBar页面
> Updated: 2025-09-17 20:59:11

# 移除tabBar页面

调用**dd.removeTabBarItem**移除tabBar页面。

> **[!IMPORTANT]**
>
> 使用该接口请注意：
>
> - removeTabBarItem 不可在非 tabBar 页面调用。
> - removeTabBarItem 不可移除自身。
> - removeTabBarItem 不可移除主 tab 页。

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| index | number | 是 | 要删除的 item 对应的位置，从 0 开始。 |
| success | function | 否 | 接口调用成功的回调函数。 |
| fail | function | 否 | 接口调用失败的回调函数。 |
| complete | function | 否 | 接口调用结束的回调函数（调用成功、失败都会执行）。 |

## **什么是主 tabbar 页面**

当小程序被启动后，第一个被初始化的 tabBar 页面。

## **兼容性判断**

使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('removeTabBarItem')进行兼容性判断。
