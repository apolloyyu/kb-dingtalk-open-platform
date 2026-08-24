---
title: "previewImagesInDingTalkBatch"
source_url: "https://open.dingtalk.com/document/development/jsapi-preview-images-in-ding-talk-batch"
namespace: "development"
slug: "jsapi-preview-images-in-ding-talk-batch"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 钉盘 > previewImagesInDingTalkBatch"
doc_id: "6D5A0G3trO"
updated_at: "2025-08-27 18:08:20"
---

> Source: https://open.dingtalk.com/document/development/jsapi-preview-images-in-ding-talk-batch
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 钉盘 > previewImagesInDingTalkBatch
> Updated: 2025-08-27 18:08:20

# previewImagesInDingTalkBatch

调用previewImagesInDingTalkBatch，实现批量预览钉盘图片。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317877661/p512977.png)
调用失败时，比如图片参数spaceId和dentryId错误时，会出现以下情况：

- index对应的图片元素参数无误，但images内其他图片元素参数错误，该错误元素对应的图片不会被预览。
- index对应的图片元素参数错误，调用本接口会出现强提示“文件不存在或已删除”。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317877661/p512976.png)

> 调用本接口只预览参数无误的图片。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.3.30 | 6.3.30 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11646) |
| 小程序 | 6.3.30 | 6.3.30 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11646) |

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

- `images`（array，必填）：图片信息。
- `images[].spaceId`（string，必填）：图片所在的钉盘空间ID，调用[获取文件或文件夹列表](https://open.dingtalk.com/document/orgapp/obtain-the-file-list-storage?spm=ding\_open\_doc.document.0.0.7d53722fl9fKSv)接口获取spaceId参数值。
- `images[].dentryId`（string，必填）：图片在钉盘空间内的节点ID，可调用[获取文件或文件夹列表](https://open.dingtalk.com/document/orgapp/obtain-the-file-list-storage?spm=ding\_open\_doc.document.0.0.7d53722fl9fKSv)接口获取id参数值。
- `index`（number）：从第几张开始预览。第一张index等于0，依次类推。  
    
  > 如果index超出images中图片的数量，默认从第一张开始预览。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.previewImagesInDingTalkBatch({
  index: 1,
  images: [{ spaceId: 'xxxxx', dentryId: '33333' }],
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
