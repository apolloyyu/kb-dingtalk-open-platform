---
title: "RecorderManager.start"
source_url: "https://open.dingtalk.com/document/development/jsapi-recorder-manager-start"
namespace: "development"
slug: "jsapi-recorder-manager-start"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 录音 > RecorderManager.start"
doc_id: "j7rUz325s9"
updated_at: "2025-08-27 18:06:47"
---

> Source: https://open.dingtalk.com/document/development/jsapi-recorder-manager-start
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 录音 > RecorderManager.start
> Updated: 2025-08-27 18:06:47

# RecorderManager.start

开始录音，当页面不可见时，录音自动停止。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10236) |

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

- `duration`（string）：录音时长，单位为秒（s），最长支持60秒音频录制。  
  该参数在Android端必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const recorderManager = dd.getRecorderManager();

recorderManager.start('60');
```
