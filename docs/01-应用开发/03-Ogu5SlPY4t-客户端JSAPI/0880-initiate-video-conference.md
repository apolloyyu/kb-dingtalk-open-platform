---
title: "发起视频会议"
source_url: "https://open.dingtalk.com/document/development/initiate-video-conference"
namespace: "development"
slug: "initiate-video-conference"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 视频会议 > 发起视频会议"
doc_id: "FZEY857kDt"
updated_at: "2025-09-17 20:57:33"
---

> Source: https://open.dingtalk.com/document/development/initiate-video-conference
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 视频会议 > 发起视频会议
> Updated: 2025-09-17 20:57:33

# 发起视频会议

调用**biz.conference.videoConfCall**发起视频会议。

## 使用说明

使用该接口，可以向企业内用户发起视频会议。

> **[!IMPORTANT]**
>
> - 调用发起后不会立即返回，需要等到会议结束（包括发起失败和正常结束），才会执行回调函数，返回对应的会议详细信息。
> - 只支持**企业内部应用**调用。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥5.0.8） | 支持（钉钉版本≥5.0.8） | 支持（钉钉版本≥5.1.28） |

```
dd.biz.conference.videoConfCall({
    title: "a meaningful title",
    calleeCorpId: "corpid****",
    calleeStaffIds: ["65790xxxx","46206xxxx","54878xxxx"],
    onSuccess : function() {},
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| title | String | 通话主题，建议传入有实际意义的简短描述，便于之后查看通话记录时快速筛选。 |
| calleeCorpId | String | 参会人所在企业的企业id。 |
| calleeStaffIds | Array | 参会人在企业中的userid列表。多个参会人使用逗号分隔。 |
