---
title: "getRecorderManager"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-recorder-manager"
namespace: "development"
slug: "jsapi-get-recorder-manager"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 录音 > getRecorderManager"
doc_id: "eg7Idot2sU"
updated_at: "2025-08-27 18:06:42"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-recorder-manager
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 录音 > getRecorderManager
> Updated: 2025-08-27 18:06:42

# getRecorderManager

调用dd.getRecorderManager获取当前小程序全局唯一的录音管理器 recordManager。

### 使用

```
if (dd.canIUse('getRecorderManager')) {     // 端上支持
    const recorderManager = dd.getRecorderManager()    
} else {     // 端上不支持
    dd.alert({ content: '请升级钉钉版本至4.5.18以支持录音功能' })    
}
```

### recorderManager方法

| 方法名 | 参数 | 说明 |
| --- | --- | --- |
| start | duration：录音时长，单位为秒（s），最长支持60秒音频录制。 | 开始录音，当页面不可见时，录音自动停止。 |
| stop | - | 停止录音。 |
| pause | - | 暂停录音。 |
| resume | - | 继续录音，即恢复之前暂停的录音。 |

### recorderManager回调

| Head | Head | Head |
| --- | --- | --- |
| onstart | - | 录音开始时的回调。 |
| onstop | tempFilePath：录音文件地址 | 录音停止时的回调。 |
| onerror | errorCode：错误码 errorMessage：错误信息 | 录音错误时的回调。 |
| onpause | Data | 监听录音暂停事件。 |
| onresume | Data | 监听录音继续事件。 |
| onframerecorded | Data | 监听已录制完制定帧大小的文件事件。如果设置了 frameSize，则会回调此事件。回调的参数为{frameBuffer: ArrayBuffer, isLastFrame: Boolean} |

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10235) |

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
dd.getRecorderManager();
```
