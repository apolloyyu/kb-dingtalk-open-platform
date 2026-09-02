---
title: "页面事件监听"
source_url: "https://open.dingtalk.com/document/dingstart/webapp-page-event-monitoring"
namespace: "dingstart"
slug: "webapp-page-event-monitoring"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 开发参考 > 页面事件监听"
doc_id: "UAB4lFB7m1"
updated_at: "2025-09-03 15:56:12"
---

> Source: https://open.dingtalk.com/document/dingstart/webapp-page-event-monitoring
> Path: 应用开发 / 开发指南 / 开发网页应用 > 开发参考 > 页面事件监听
> Updated: 2025-09-03 15:56:12

# 页面事件监听

当页面进行某些特殊操作时，钉钉会产生回调，开发者可监控该操作，并处理开发者自己的业务逻辑。

## 页面返回事件的回调监听

- **使用说明**

  点击页面返回键时，客户端会产生回调，开发者可监控此返回事件，并处理开发者自己的业务逻辑。

  > **[!IMPORTANT]**
  >
  > - 此事件不支持在自定义首页使用。
  > - iOS的返回事件请使用setLeft组件。

  | **客户端** | **Android** | **iOS** | **PC** |
  | --- | --- | --- | --- |
  | 支持说明 | 支持 | 不支持 | 不支持 |
- **示例代码**

  ```
  document.addEventListener('backbutton', function(e) {
                // 在这里处理你的业务逻辑
                e.preventDefault(); //backbutton事件的默认行为是回退历史记录，如果你想阻止默认的回退行为，那么可以通过preventDefault()实现
  });
  ```

## 页面resume事件的回调监听

- **使用说明**

  当页面重新可见并可交互时，钉钉会产生回调，开发者可监听此resume事件，并处理开发者自己的业务逻辑。

  | **客户端** | **Android** | **iOS** | **PC** |
  | --- | --- | --- | --- |
  | 支持说明 | 支持 | 支持 | 不支持 |
- **示例代码**

  ```
  document.addEventListener('resume', function() {
                // 在这里处理你的业务逻辑
     });
  ```

## 页面pause事件的回调监听

- **使用说明**

  当页面不可见时，钉钉会产生回调，开发者可以监听此pause事件，并处理开发者自己的业务逻辑。

  | **客户端** | **Android** | **iOS** | **PC** |
  | --- | --- | --- | --- |
  | 支持说明 | 支持 | 支持 | 不支持 |
- **示例代码**

  ```
  document.addEventListener('pause', function() {
                // 在这里处理你的业务逻辑
     });
  ```

## 页面双击标题事件的回调监听

- **使用说明**

  当双击页面标题时，钉钉会产生回调，开发者可以监听此事件，并处理开发者自己的业务逻辑。

  | **客户端** | **Android** | **iOS** | **PC** |
  | --- | --- | --- | --- |
  | 支持说明 | 支持 | 支持 | 不支持 |
- **示例代码**

  ```
  document.addEventListener('navTitle', function() {
                // 在这里处理你的业务逻辑
     });
  ```

## 网络连接成功事件的回调监听

- **使用说明**

  由无网络到有网络连接时，钉钉会产生回调，开发者可以监听此回调事件，并处理开发者自己的业务逻辑。

  | **客户端** | **Android** | **iOS** | **PC** |
  | --- | --- | --- | --- |
  | 支持说明 | 支持 | 支持 | 不支持 |
- **示例代码**

  ```
  document.addEventListener('online', function() {
                // 在这里处理你的业务逻辑
     });
  ```

## 网络连接断开事件的回调监听

- **使用说明**

  当由有网络连接状态到网络断开时，钉钉会产生回调，开发者可以监听此回调事件，并处理开发者自己的业务逻辑。

  | **客户端** | **Android** | **iOS** | **PC** |
  | --- | --- | --- | --- |
  | 支持说明 | 支持 | 支持 | 不支持 |
- **示例代码**

  ```
  document.addEventListener('offline', function() {
                // 在这里处理你的业务逻辑
     });
  ```

## Demo示例

回调事件监听需要在dd.ready的回调函数触发后，示例如下：

```
dd.ready(function() {
  // 退到后台的事件监听(webview)
  document.addEventListener('pause', function(e) {
      e.preventDefault();
      console.log('事件：pause')
  }, false);

  // 页面被唤醒的事件监听(webview)
  document.addEventListener('resume', function(e) {
      e.preventDefault();
      console.log('事件：resume')
  }, false);

  //返回按钮点击的事件监听(android)
  document.addEventListener('backbutton', function(e) {
      e.preventDefault();
      dd.device.notification.alert({
          message: '哎呀，你不小心点到返回键啦!',
          title: '...警告...'
      });
  }, false);

 //双击标题的事件监听
  document.addEventListener('navTitle', function(e) {
      e.preventDefault();
      console.log('事件：navTitle')      
   },false);

 // 网络连接成功的事件监听
  document.addEventListener('online', function(e) {
      e.preventDefault();
      console.log('事件：online')
  }, false);

 // 网络连接断开的事件监听
  document.addEventListener('offline', function(e) {
      e.preventDefault();
      console.log('事件：offline')
  }, false);
});
```
