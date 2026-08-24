---
title: "VideoContext.mute"
source_url: "https://open.dingtalk.com/document/development/jsapi-video-context-mute"
namespace: "development"
slug: "jsapi-video-context-mute"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 视频 > VideoContext.mute"
doc_id: "F12IQNaNZ1"
updated_at: "2025-08-27 18:06:50"
---

> Source: https://open.dingtalk.com/document/development/jsapi-video-context-mute
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 视频 > VideoContext.mute
> Updated: 2025-08-27 18:06:50

# VideoContext.mute

调用VideoContext.mute，切换静音状态。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11514) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `ison`（boolean，必填）：切换静音状态。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.VideoContext.mute({
  ison: true,
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{}
```
