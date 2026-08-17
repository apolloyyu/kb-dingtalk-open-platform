---
title: "Wi-Fi概览"
source_url: "https://open.dingtalk.com/document/development/wi-fi-overview"
namespace: "development"
slug: "wi-fi-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > Wi-Fi概览"
doc_id: "uxcmykSVAB"
updated_at: "2025-09-17 21:00:28"
---

> Source: https://open.dingtalk.com/document/development/wi-fi-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > Wi-Fi概览
> Updated: 2025-09-17 21:00:28

# Wi-Fi概览

## **简介**

在小程序中支持搜索周边的 Wi-Fi，同时可以针对指定 Wi-Fi，传入密码发起连接。

## **连接指定 Wi-Fi**

1. [dd.startWifi](https://open.dingtalk.com/document/orgapp/initialize-the-wi-fi-module)：初始化 Wi-Fi 模块。
2. [dd.onWifiConnected](https://open.dingtalk.com/document/orgapp/listening-for-connection-wi-fi-events)：监听连接上 Wi-Fi 事件。
3. [dd.connectWifi](https://open.dingtalk.com/document/orgapp/connection-wi-fi)：连接 Wi-Fi。（仅 iOS 11及以上版本支持）

## **连接周边 Wi-Fi**

小程序可以通过扫描附近的 Wi-Fi 设备，让用户选择某个设备进行连接。

## **Android**

1. [dd.startWifi](https://open.dingtalk.com/document/orgapp/initialize-the-wi-fi-module)：初始化 Wi-Fi 模块。
2. [dd.onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event)：监听获取到 Wi-Fi 列表数据事件。
3. [dd.getWifiList](https://open.dingtalk.com/document/orgapp/get-wi-fi-list)：请求获取 Wi-Fi 列表。
4. [dd.onWifiConnected](https://open.dingtalk.com/document/orgapp/listening-for-connection-wi-fi-events)：监听连接上 Wi-Fi 事件。
5. [dd.connectWifi](https://open.dingtalk.com/document/orgapp/connection-wi-fi)：连接 Wi-Fi。

### **iOS**

> **[!NOTE]**
>
> iOS 11.0及11.1版本因系统原因暂不支持。

1. [dd.startWifi](https://open.dingtalk.com/document/orgapp/initialize-the-wi-fi-module)：初始化 Wi-Fi 模块。
2. [dd.onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event)：监听获取到 Wi-Fi 列表数据事件。
3. [dd.getWifiList](https://open.dingtalk.com/document/orgapp/get-wi-fi-list)：请求获取 Wi-Fi 列表。
4. [dd.onWifiConnected](https://open.dingtalk.com/document/orgapp/listening-for-connection-wi-fi-events)：监听连接上 Wi-Fi 事件。
5. [dd.setWifiList](https://open.dingtalk.com/document/orgapp/set-wi-fi)：设置 wifiList 中 AP 的相关信息。

## **代码示例**

```
// 1、初始化 Wi-Fi 模块。
dd.startWifi({
 success() {
    // 3、请求获取 Wi-Fi 列表。
   dd.getWifiList();
  }
})
// 2、注册获取到 Wi-Fi 列表数据事件回调。
dd.onGetWifiList(res => {
  if (res.wifiList && res.wifiList[0]) {
    const wifiInfo = res.wifiList[0];
  if (dd.env.platform === 'Android') {
     // 5、for android 连接 Wi-Fi。
      dd.connectWifi({
        SSID: wifiInfo.SSID,
        BSSID: wifiInfo.BSSID,
        complete(res) {
          console.log(res);
        }
      });
    } else if (dd.env.platform === 'iOS') {
     // 5、for iOS 设置 wifiList 中 AP 的相关信息。
      dd.setWifiList({
        wifiList: [{
          SSID: wifiInfo.SSID,
          BSSID: wifiInfo.BSSID,
        }],
        complete(res) {
          console.log(res);
        }
      });
    }
  }
});
// 4、注册连接上 Wi-Fi 事件回调。
dd.onWifiConnected(res => {
 dd.alert({
   content: 'onWifiConnected:' + JSON.stringify(res),
  })
});
```

## **使用限制**

- 钉钉版本需在7.0.10及以上。
- Android 6.0 以上版本，在没有打开定位开关的时候会导致设备不能正常获取周边的 Wi-Fi 信息。

## **接口列表**

| **名称** | **iOS** | **Android** | **功能说明** |
| --- | --- | --- | --- |
| [dd.startWifi](https://open.dingtalk.com/document/orgapp/initialize-the-wi-fi-module) | 支持 | 支持 | 初始化 Wi-Fi 模块。 |
| [dd.stopWifi](https://open.dingtalk.com/document/orgapp/close-wi-fi-module) | 支持 | 支持 | 关闭 Wi-Fi 模块。 |
| [dd.connectWifi](https://open.dingtalk.com/document/orgapp/connection-wi-fi) | 支持 | 支持 | 连接 Wi-Fi。若已知 Wi-Fi 信息，可以直接利用该接口连接。 |
| [dd.getWifiList](https://open.dingtalk.com/document/orgapp/get-wi-fi-list) | 支持 | 支持 | 请求获取 Wi-Fi 列表，在 [onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event) 注册的回调中返回 wifiList 数据。iOS 将跳转到系统设置中的钉钉设置页，需要用户手动进入「无线局域网」设置页，Android 不会跳转。 |
| [dd.setWifiList](https://open.dingtalk.com/document/orgapp/set-wi-fi) | 支持 | 不支持 | 在 [onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event) 回调触发后，利用接口设置 wifiList 中 AP 的相关信息。 |
| [dd.onWifiConnected](https://open.dingtalk.com/document/orgapp/listening-for-connection-wi-fi-events) | 支持 | 支持 | 监听连接上 Wi-Fi 的事件。 |
| [dd.offWifiConnected](https://open.dingtalk.com/document/orgapp/stop-listening-for-connection-wi-fi-events) | 支持 | 支持 | 取消监听连接上 Wi-Fi 的事件。 |
| [dd.onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event) | 支持 | 支持 | 监听在获取到 Wi-Fi 列表数据时的事件，在回调中将返回 wifiList。 |
| [dd.offGetWifiList](https://open.dingtalk.com/document/orgapp/stop-listening-to-the-obtained-wi-fi-list-data-event) | 支持 | 支持 | 取消监听在获取到 Wi-Fi 列表数据时的事件。 |
| [dd.getConnectedWifi](https://open.dingtalk.com/document/orgapp/get-connected-wi-fi-information) | 支持 | 支持 | 获取已连接中的 Wi-Fi 信息。 |
| [dd.registerSSID](https://open.dingtalk.com/document/orgapp/trust-ssid) | 支持 | 不支持 | 信任该SSID，对于需要 Portal 认证的 Wi-Fi，不会弹出 Portal 认证页面。 |
| [dd.unregisterSSID](https://open.dingtalk.com/document/orgapp/no-longer-trust-this-ssid) | 支持 | 不支持 | 不再信任该SSID，对于需要 Portal 认证的 Wi-Fi，继续弹出 Portal 认证页面。 |
