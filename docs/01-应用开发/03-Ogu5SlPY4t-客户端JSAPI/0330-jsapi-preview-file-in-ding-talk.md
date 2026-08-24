---
title: "previewFileInDingTalk"
source_url: "https://open.dingtalk.com/document/development/jsapi-preview-file-in-ding-talk"
namespace: "development"
slug: "jsapi-preview-file-in-ding-talk"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 钉盘 > previewFileInDingTalk"
doc_id: "D7mwxWfhf1"
updated_at: "2025-08-27 18:08:20"
---

> Source: https://open.dingtalk.com/document/development/jsapi-preview-file-in-ding-talk
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 钉盘 > previewFileInDingTalk
> Updated: 2025-08-27 18:08:20

# previewFileInDingTalk

调用previewFileInDingTalk，预览钉盘文件。

在调用本接口预览钉盘文件之前，你需要：

- 审批：调用[授权预览审批附件](https://open.dingtalk.com/document/orgapp/preview-authorization-attachment-pop)进行授权。
- 其他：调用[添加权限](https://open.dingtalk.com/document/isvapp/add-permissions-storage)进行授权。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10317) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10317) |

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

- `spaceId`（string，必填）：空间ID。
- `fileId`（string，必填）：文件ID。
- `fileName`（string，必填）：文件名称。
- `fileSize`（string，必填）：文件大小，单位比特。
- `corpId`（string）：企业corpId。  
    
  > H5应用必填。
- `fileType`（string，必填）：文件扩展名。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.previewFileInDingTalk({
  corpId: 'ding**',
  fileId: '333222',
  spaceId: '43333',
  fileName: '集体照.png',
  fileSize: '1024',
  fileType: 'png',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
