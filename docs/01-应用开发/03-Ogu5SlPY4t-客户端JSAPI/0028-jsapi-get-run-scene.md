---
title: "getRunScene"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-run-scene"
namespace: "development"
slug: "jsapi-get-run-scene"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 基础 > getRunScene"
doc_id: "ncN1DJEi8Q"
updated_at: "2025-08-27 18:04:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-run-scene
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 基础 > getRunScene
> Updated: 2025-08-27 18:04:56

# getRunScene

使用getRunScene，获取当前小程序的运行版本。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10003) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 字段说明

- `envVersion`（string，必填）：小程序当前运行的版本，小程序版本说明请查看[版本管理与发布](https://open.dingtalk.com/document/org/publish-orgapp?spm=ding\_open\_doc.document.0.0.5755722fyMtHci#topic-2024351)：  
    
  \* debug：开发版  
  \* trial：体验版  
  \* release：线上版

## **示例****代码**

### 默认出入参

```
dd.getRunScene({
  success: (res) => {
    const { envVersion } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "envVersion": "release" }
```
