---
title: "share"
source_url: "https://open.dingtalk.com/document/development/jsapi-share"
namespace: "development"
slug: "jsapi-share"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 分享 > share"
doc_id: "D6cWdk20le"
updated_at: "2025-08-27 18:08:13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-share
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 分享 > share
> Updated: 2025-08-27 18:08:13

# share

调用share，实现分享功能。

![调用示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0605834061/p177828.png)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11673) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11673) |

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

- `type`（number，必填）：分享类型：  
    
  \* 0：全部组件默认  
  \* 1：只能分享到钉钉  
  \* 2：不能分享，只有刷新按钮
- `url`（string）：url地址。
- `title`（string，必填）：分享标题。
- `content`（string）：分享内容。
- `image`（string）：分享的图片url地址。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.share({
  url: 'https://www.dingtalk.com',
  type: 0,
  image:
    'https://img.alicdn.com/imgextra/i1/O1CN01SNHEw41ysQFPN5Ql6_!!6000000006634-55-tps-176-31.svg',
  title: '钉钉官网',
  content: '钉钉官网',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
