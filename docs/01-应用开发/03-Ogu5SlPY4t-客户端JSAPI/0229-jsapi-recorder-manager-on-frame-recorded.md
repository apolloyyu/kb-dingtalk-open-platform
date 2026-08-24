---
title: "RecorderManager.onframerecorded"
source_url: "https://open.dingtalk.com/document/development/jsapi-recorder-manager-on-frame-recorded"
namespace: "development"
slug: "jsapi-recorder-manager-on-frame-recorded"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 录音 > RecorderManager.onframerecorded"
doc_id: "8lACZYOIQe"
updated_at: "2025-08-27 18:06:45"
---

> Source: https://open.dingtalk.com/document/development/jsapi-recorder-manager-on-frame-recorded
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 录音 > RecorderManager.onframerecorded
> Updated: 2025-08-27 18:06:45

# RecorderManager.onframerecorded

监听已录制完制定帧大小的文件事件。

> 如果设置了 frameSize，则会回调此事件。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11484) |

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

- `type`（string，必填）：类型。
- `isLastFrame`（boolean，必填）：当前帧是否正常录音结束前的最后一帧。
- `frameBuffer`（string，必填）：录音分片数据。

## **示例****代码**

### 默认出入参

```
const recorderManager = dd.getRecorderManager();

recorderManager.onframerecorded = (res) => {
  console.log('onFrameRecorded', JSON.stringify(res));
  console.log('onFrameRecorded arraybuffer', JSON.stringify(res.frameBuffer));
};
recorderManager.start({ duration: 10, frameSize: 50 });
```

`success`返回对象示例：

```
{
  "type": "onframerecorded",
  "frameBuffer": "Base64格式数据",
  "isLastFrame": true
}
```
