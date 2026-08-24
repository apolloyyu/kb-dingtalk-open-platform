---
title: "BackgroundAudioManager.onPrev"
source_url: "https://open.dingtalk.com/document/development/jsapi-background-audio-manager-on-prev"
namespace: "development"
slug: "jsapi-background-audio-manager-on-prev"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 音频 > BackgroundAudioManager.onPrev"
doc_id: "MEGRWE9z5t"
updated_at: "2025-08-27 18:06:57"
---

> Source: https://open.dingtalk.com/document/development/jsapi-background-audio-manager-on-prev
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 音频 > BackgroundAudioManager.onPrev
> Updated: 2025-08-27 18:06:57

# BackgroundAudioManager.onPrev

监听用户在系统音乐播放面板点击上一曲事件。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 不支持 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11492) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

（object）

## **示例****代码**

### 默认出入参

```
dd.BackgroundAudioManager.onPrev({
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
