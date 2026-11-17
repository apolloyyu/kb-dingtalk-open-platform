---
title: "openLocalFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-local-file"
namespace: "development"
slug: "jsapi-open-local-file"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "文件存储 > 文件 > openLocalFile"
doc_id: "EK9CyceHKr"
updated_at: "2025-08-27 18:07:12"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-local-file
> Path: 应用开发 / 客户端 JSAPI / 文件存储 > 文件 > openLocalFile
> Updated: 2025-08-27 18:07:12

# openLocalFile

调用openLocalFile，打开本地文件。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11663) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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

- `url`（string，必填）：url是缓存文件的key。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.openLocalFile({
  url: `url示例值`,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
