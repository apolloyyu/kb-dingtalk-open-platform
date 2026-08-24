---
title: "VideoContext.exitFullScreen"
source_url: "https://open.dingtalk.com/document/development/jsapi-video-context-exit-full-screen"
namespace: "development"
slug: "jsapi-video-context-exit-full-screen"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 视频 > VideoContext.exitFullScreen"
doc_id: "kfAcrGmhlz"
updated_at: "2025-08-27 18:06:49"
---

> Source: https://open.dingtalk.com/document/development/jsapi-video-context-exit-full-screen
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 视频 > VideoContext.exitFullScreen
> Updated: 2025-08-27 18:06:49

# VideoContext.exitFullScreen

通过videoContext控制相应video组件的全屏退出

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 5.1.39 | 5.1.39 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10206) |

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

videoContext.exitFullScreen();
```
