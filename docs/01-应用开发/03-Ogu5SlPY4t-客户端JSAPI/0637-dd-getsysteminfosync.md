---
title: "获取手机系统信息的同步接口"
source_url: "https://open.dingtalk.com/document/development/dd-getsysteminfosync"
namespace: "development"
slug: "dd-getsysteminfosync"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 系统信息 > 获取手机系统信息的同步接口"
doc_id: "EFCxELP03R"
updated_at: "2025-09-17 21:00:06"
---

> Source: https://open.dingtalk.com/document/development/dd-getsysteminfosync
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 系统信息 > 获取手机系统信息的同步接口
> Updated: 2025-09-17 21:00:06

# 获取手机系统信息的同步接口

调用**dd.getSystemInfoSync**获取手机系统信息的同步接口。

## **示例****代码**

```
Page({
  data: {
    systemInfo: {}
  },
  getSystemInfoSyncPage() {
    this.setData({
          systemInfo: dd.getSystemInfoSync()
        })
  }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| model | String | 手机型号。 |
| pixelRatio | Number | 设备像素比。 |
| windowWidth | Number | 窗口宽度。 |
| windowHeight | Number | 窗口高度。 |
| language | String | 钉钉设置的语言。 |
| version | String | 钉钉版本号。 |
| storage | String | 设备磁盘容量。 |
| currentBattery | String | 当前电量百分比。 |
| system | String | 系统版本。 |
| platform | String | 系统名：Android，iOS。 |
| screenWidth | Number | 屏幕宽度。 |
| screenHeight | Number | 屏幕高度。 |
| brand | String | 手机品牌。 |
| fontSizeSetting | Number | 用户设置字体大小。 |
