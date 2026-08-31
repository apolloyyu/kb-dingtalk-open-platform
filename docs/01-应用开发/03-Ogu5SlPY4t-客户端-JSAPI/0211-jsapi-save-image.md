---
title: "saveImage"
source_url: "https://open.dingtalk.com/document/development/jsapi-save-image"
namespace: "development"
slug: "jsapi-save-image"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 图片 > saveImage"
doc_id: "a2R52u2nd8"
updated_at: "2025-08-27 18:06:35"
---

> Source: https://open.dingtalk.com/document/development/jsapi-save-image
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 图片 > saveImage
> Updated: 2025-08-27 18:06:35

# saveImage

调用saveImage，保存在线、本地临时或者永久地址图片到手机相册。

> 回调success表示保存成功，回调fail表示保存失败。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10198) |

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

- `url`（string，必填）：要保存的图片地址。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 15 | 没有开启相册权限(ios only) |
| 16 | 手机相册存储空间不足(ios only) |

## **示例****代码**

### 默认出入参

```
dd.saveImage({
  url: 'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
