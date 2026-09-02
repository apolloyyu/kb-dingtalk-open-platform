---
title: "previewImage"
source_url: "https://open.dingtalk.com/document/development/jsapi-preview-image"
namespace: "development"
slug: "jsapi-preview-image"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 图片 > previewImage"
doc_id: "GdfU6ZybFR"
updated_at: "2025-08-27 18:06:34"
---

> Source: https://open.dingtalk.com/document/development/jsapi-preview-image
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 图片 > previewImage
> Updated: 2025-08-27 18:06:34

# previewImage

调用previewImage，预览图片。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10197) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10197) |

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

- `urls`（array，必填）：要预览的图片链接列表。
- `current`（number）：当前显示图片索引，默认值：0。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.previewImage({
  urls: [
    'https://gw.alicdn.com/imgextra/i3/O1CN01Eg6xCm1nnsXZCnkP4_!!6000000005135-2-tps-200-200.png',
    'https://gw.alicdn.com/imgextra/i1/O1CN01ug6HAx1eAe42KAHSF_!!6000000003831-2-tps-200-200.png',
  ],
  current: 1,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
