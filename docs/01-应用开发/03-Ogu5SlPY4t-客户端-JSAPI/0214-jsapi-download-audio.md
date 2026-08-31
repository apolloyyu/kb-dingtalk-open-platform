---
title: "downloadAudio"
source_url: "https://open.dingtalk.com/document/development/jsapi-download-audio"
namespace: "development"
slug: "jsapi-download-audio"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 录音 > downloadAudio"
doc_id: "dUqp0xTO5a"
updated_at: "2025-08-27 18:06:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-download-audio
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 录音 > downloadAudio
> Updated: 2025-08-27 18:06:36

# downloadAudio

调用downloadAudio，下载音频。

使用 `stopRecord` 或者 `onRecordEnd` 获取的`MediaId`下载音频资源。下载完成后返回音频在本地的`MediaId`。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11681) |
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

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `mediaId`（string，必填）：音频在服务端的标识。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.downloadAudio({
  mediaId: '@lATOCLhLfc46kUl8zlUmRlM',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
