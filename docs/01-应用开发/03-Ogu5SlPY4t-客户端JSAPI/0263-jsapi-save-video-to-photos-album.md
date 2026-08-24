---
title: "saveVideoToPhotosAlbum"
source_url: "https://open.dingtalk.com/document/development/jsapi-save-video-to-photos-album"
namespace: "development"
slug: "jsapi-save-video-to-photos-album"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 音频 > saveVideoToPhotosAlbum"
doc_id: "Sc3ivq7fFT"
updated_at: "2025-08-27 18:07:04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-save-video-to-photos-album
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 音频 > saveVideoToPhotosAlbum
> Updated: 2025-08-27 18:07:04

# saveVideoToPhotosAlbum

调用saveVideoToPhotosAlbum，保存视频到系统相册。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10210) |

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

- `filePath`（string，必填）：视频文件路径，支持本地虚拟路径和网络地址。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.saveVideoToPhotosAlbum({
  filePath: '/data/path/to/file',
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{}
```
