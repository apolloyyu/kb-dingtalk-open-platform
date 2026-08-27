---
title: "onAudioInterruptionEnd"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-audio-interruption-end"
namespace: "development"
slug: "jsapi-on-audio-interruption-end"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 音频 > onAudioInterruptionEnd"
doc_id: "92ZC20egMj"
updated_at: "2025-08-27 18:07:03"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-audio-interruption-end
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 音频 > onAudioInterruptionEnd
> Updated: 2025-08-27 18:07:03

# onAudioInterruptionEnd

调用onAudioInterruptionEnd，监听音频被中断的结束事件。

在收到 [onAudioInterruptionBegin](https://open.dingtalk.com/document/orgapp/jsapi-onAudioInterruptionBegin) 事件之后，小程序内的所有音频会暂停，收到此事件之后可再次播放成功，为异步接口

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11518) |

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

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.onAudioInterruptionEnd({
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
