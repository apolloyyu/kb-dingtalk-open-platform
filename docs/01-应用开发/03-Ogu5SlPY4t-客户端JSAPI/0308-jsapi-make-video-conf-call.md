---
title: "makeVideoConfCall"
source_url: "https://open.dingtalk.com/document/development/jsapi-make-video-conf-call"
namespace: "development"
slug: "jsapi-make-video-conf-call"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "音频会议 > makeVideoConfCall"
doc_id: "2ZXKv0QLBp"
updated_at: "2025-08-27 18:08:39"
---

> Source: https://open.dingtalk.com/document/development/jsapi-make-video-conf-call
> Path: 应用开发 / 客户端JSAPI / 音频会议 > makeVideoConfCall
> Updated: 2025-08-27 18:08:39

# makeVideoConfCall

调用makeVideoConfCall，发起视频会议。

![](https://img.alicdn.com/imgextra/i4/O1CN01Wpx7se1E2hFAAWHng_!!6000000000294-2-tps-3274-1676.png)

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11647) |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11647) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `title`（string，必填）：通话主题，建议传入有实际意义的简短描述，便于之后查看通话记录时快速筛选。
- `calleeStaffIds`（array，必填）：参会人的userId列表。
- `calleeCorpId`（string，必填）：参会人所在的企业corpId。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.makeVideoConfCall({
  title: '测试视频会议',
  calleeCorpId: 'ding1234xxx',
  calleeStaffIds: ['user01', 'user02'],
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
