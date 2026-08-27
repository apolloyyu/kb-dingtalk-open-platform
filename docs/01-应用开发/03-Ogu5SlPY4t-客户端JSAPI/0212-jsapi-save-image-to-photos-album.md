---
title: "saveImageToPhotosAlbum"
source_url: "https://open.dingtalk.com/document/development/jsapi-save-image-to-photos-album"
namespace: "development"
slug: "jsapi-save-image-to-photos-album"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 图片 > saveImageToPhotosAlbum"
doc_id: "anPRiOAauf"
updated_at: "2025-08-27 18:06:35"
---

> Source: https://open.dingtalk.com/document/development/jsapi-save-image-to-photos-album
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 图片 > saveImageToPhotosAlbum
> Updated: 2025-08-27 18:06:35

# saveImageToPhotosAlbum

保存图片到系统相册

保存图片到系统相册，仅支持本地图片。保存结果会有Toast提示。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11752) |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11752) |

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

- `filePath`（string，必填）：图片文件路径，仅支持本地虚拟路径。例如: https://resource/xxxx.image

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 3 | 系统异常 |
| 17 | 保存失败 |

## **示例****代码**

### 默认Demo标题

```
dd.saveImageToPhotosAlbum({
  filePath: '/data/path/to/image',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
