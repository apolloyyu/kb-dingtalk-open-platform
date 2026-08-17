---
title: "小程序运行机制"
source_url: "https://open.dingtalk.com/document/development/mini-app-small-program-running-mechanism"
namespace: "development"
slug: "mini-app-small-program-running-mechanism"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序运行/更新机制 > 小程序运行机制"
doc_id: "QIpRF8paqI"
updated_at: "2025-09-17 20:58:15"
---

> Source: https://open.dingtalk.com/document/development/mini-app-small-program-running-mechanism
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序运行/更新机制 > 小程序运行机制
> Updated: 2025-09-17 20:58:15

# 小程序运行机制

本文介绍小程序运行时的各种状态。

## 下载

小程序无需安装，用户第一次使用小程序时，钉钉会从服务器下载小程序的资源，下载后的小程序资源会缓存在钉钉客户端一段时间。当用户再次打开已经缓存资源的小程序时，会跳过下载过程，更快地打开小程序。

## 小程序启动

小程序启动可以分为两种情况，一种是**冷启动**，一种是**热启动**。

- **冷启动**

  如果用户首次打开，或小程序销毁后被用户再次打开，此时小程序需要重新加载启动，即冷启动。此时小程序会执行初始化，初始化完成后，会触发 `onLaunch` 回调函数。
- **热启动**

  如果用户已经打开过某小程序，在一定时间内再次打开该小程序，此时小程序并未被销毁，只是从后台状态进入前台状态，这个过程称为热启动。此时，`onShow` 函数会触发，`onLaunch` 回调函数不会被触发。

## 前台/后台状态

- **前台状态：**小程序启动后，界面被展示给用户，此时小程序处于**前台**状态。
- **后台状态**：当用户点击右上角按钮关闭小程序，或者按了设备 Home 键离开钉钉时，小程序并没有完全终止运行，而是进入了**后台**状态，小程序还可以运行一小段时间。
- **终止状态：**当用户再次进入钉钉或再次打开小程序，小程序又会从后台进入**前台**。但如果用户很久没有再进入小程序，或者系统资源紧张，小程序可能被**销毁**，即完全终止运行。

## 缓存

开启本地缓存数据，进行存储、获取和删除等控制。 单个小程序的缓存总上限为 10MB。 同步方法会阻塞当前任务，直到同步方法处理返回。异步方法不会阻塞当前任务。

| **操作** | **同步** | **异步** | **描****述** |
| --- | --- | --- | --- |
| 存储 | dd.setStorageSync | dd.setStorage | 数据存储在本地缓存中指定的 key 中的接口，会覆盖掉原来该 key 对应的数据。 |
| 读取 | dd.getStorageSync | dd.getStorage | 获取缓存数据的接口。 |
| 清除 | dd.clearStorageSync | dd.clearStorage | 清除本地数据缓存的接口。 |
| 删除 | dd.removeStorageSync | dd.removeStorage | 删除缓存数据的接口。 |
| 获取相关信息 | dd.getStorageInfoSync | dd.getStorageInfo | 获取当前 storage 的相关信息的接口。 |

## 小程序销毁时机

用户点击右上角关闭按钮关闭小程序时，小程序仅是进入后台运行，不会被销毁。只有当小程序进入后台运行状态一定时间，或者占用系统资源过高时，才会被真正销毁。
