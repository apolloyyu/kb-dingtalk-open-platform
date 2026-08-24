---
title: "onRecordEnd"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-record-end"
namespace: "development"
slug: "jsapi-on-record-end"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 录音 > onRecordEnd"
doc_id: "22oZMOwmi7"
updated_at: "2025-08-27 18:06:37"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-record-end
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 录音 > onRecordEnd
> Updated: 2025-08-27 18:06:37

# onRecordEnd

调用onRecordEnd，监听录音自动停止。

当语音录制时间超过60秒时，钉钉会自动停止语音录制，同时将录制的语音上传到服务端，返回音频资源的MediaID。推荐在调用startRecord前设置监听录音自动停止的回调。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11680) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `mediaId`（string，必填）：停止播放音频MediaId。
- `duration`（string，必填）：返回音频的时长，单位：秒。

## **示例****代码**

### 默认出入参

```
dd.onRecordEnd({
  success: (res) => {
    const { mediaId, duration } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "mediaId": "@media***", "duration": "60" }
```
