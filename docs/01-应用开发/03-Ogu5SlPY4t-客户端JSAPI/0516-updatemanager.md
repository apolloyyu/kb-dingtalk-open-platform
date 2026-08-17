---
title: "使用UpdateManager更新小程序"
source_url: "https://open.dingtalk.com/document/development/updatemanager"
namespace: "development"
slug: "updatemanager"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 更新管理小程序 > 使用UpdateManager更新小程序"
doc_id: "r9vzszbxeu"
updated_at: "2025-09-17 20:58:46"
---

> Source: https://open.dingtalk.com/document/development/updatemanager
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 更新管理小程序 > 使用UpdateManager更新小程序
> Updated: 2025-09-17 20:58:46

# 使用UpdateManager更新小程序

使用UpdateManager对象，用来管理小程序更新。

## 创建UpdateManager对象

调用**dd.getUpdateManager**创建一个**UpdateManager**对象，获取全局唯一的版本更新管理器，用于管理小程序更新。

> **[!IMPORTANT]**
>
> 基础库 1.24.3 开始支持，低版本需做兼容处理（dd.canIUse('getUpdateManager')）

## 方法

| 方法 | | 说明 |
| --- | --- | --- |
| 强制小程序重启并使用新版本 | UpdateManager.applyUpdate() | 当小程序新版本下载完成后（即收到 onUpdateReady 回调），强制小程序重启并使用新版本。 |
| 监听向钉钉后台请求检查更新结果事件 | UpdateManager.onCheckForUpdate(function callback) | 监听向钉钉后台请求检查更新结果事件。钉钉在小程序冷启动时自动检查更新，不需由开发者主动触发。 |
| 监听小程序有版本更新事件 | UpdateManager.onUpdateReady(function callback) | 监听小程序有版本更新事件。客户端主动触发下载（无需开发者触发），下载成功后回调。 |
| 监听小程序更新失败事件 | UpdateManager.onUpdateFailed(function callback) | 小程序有新版本，客户端主动触发下载（无需开发者触发），下载失败（可能是网络原因等）后回调。 |

## 示例代码

```
const updateManager = dd.getUpdateManager()

updateManager.onCheckForUpdate(function (res) {
  // 请求完新版本信息的回调
  console.log(res.hasUpdate) // 是否有更新
})

updateManager.onUpdateReady(function (ret) {
  console.log(ret.version) // 更新版本号
  dd.confirm({
    title: '更新提示',
    content: '新版本已经准备好，是否重启应用？',
    success: function (res) {
      if (res.confirm) {
        // 新的版本已经下载好，调用 applyUpdate 应用新版本并重启
        updateManager.applyUpdate()
      }
    }
  })
})

updateManager.onUpdateFailed(function () {
  // 新版本下载失败
})
```
