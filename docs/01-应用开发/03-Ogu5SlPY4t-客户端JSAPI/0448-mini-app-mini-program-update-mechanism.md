---
title: "小程序更新机制"
source_url: "https://open.dingtalk.com/document/development/mini-app-mini-program-update-mechanism"
namespace: "development"
slug: "mini-app-mini-program-update-mechanism"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序运行/更新机制 > 小程序更新机制"
doc_id: "DlZdBZqVNI"
updated_at: "2025-09-17 20:58:15"
---

> Source: https://open.dingtalk.com/document/development/mini-app-mini-program-update-mechanism
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序运行/更新机制 > 小程序更新机制
> Updated: 2025-09-17 20:58:15

# 小程序更新机制

开发者在开发者后台发布新版本之后，并不是用户就会立即使用到最新版的小程序。针对小程序版本的更新，钉钉小程序提供了不同的更新机制。

## **启动时更新**

小程序每次**冷启动**时，都会检查是否有更新版本，如果发现有新版本，将会异步下载新版本的代码包，并同时用客户端本地的包进行启动，即新版本的小程序需要等下一次冷启动才会应用上。如果距离上一次更新版本超过 48 小时，则会等待新版本的代码包被下载后，直接使用新版本启动。

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
