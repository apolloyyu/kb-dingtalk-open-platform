---
title: "VideoContext.requestFullScreen"
source_url: "https://open.dingtalk.com/document/development/jsapi-video-context-request-full-screen"
namespace: "development"
slug: "jsapi-video-context-request-full-screen"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 视频 > VideoContext.requestFullScreen"
doc_id: "azGt3ylcjN"
updated_at: "2025-08-27 18:06:52"
---

> Source: https://open.dingtalk.com/document/development/jsapi-video-context-request-full-screen
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 视频 > VideoContext.requestFullScreen
> Updated: 2025-08-27 18:06:52

# VideoContext.requestFullScreen

通过videoContext控制相应video组件的全屏进入

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 5.1.39 | 5.1.39 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10205) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const videoContext = dd.createVideoContext();

videoContext.requestFullScreen();
```
