---
title: "isLocalFileExist"
source_url: "https://open.dingtalk.com/document/development/jsapi-is-local-file-exist"
namespace: "development"
slug: "jsapi-is-local-file-exist"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "文件存储 > 文件 > isLocalFileExist"
doc_id: "taCmp1FPQP"
updated_at: "2025-08-27 18:07:11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-is-local-file-exist
> Path: 应用开发 / 客户端 JSAPI / 文件存储 > 文件 > isLocalFileExist
> Updated: 2025-08-27 18:07:11

# isLocalFileExist

调用isLocalFileExist，批量检测本地文件是否存在。

PC端使用downLoadFile接口下载后的URL在本地是否存在来判断。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11664) |
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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 字段说明

（array）

## **示例****代码**

### 默认出入参

```
const res = dd.isLocalFileExist({
  url: 'http://static.dingtalk.com/media/lADOADTWJM0C2M0C7A_748_728.jpg_60x60q90.jpg',
});
console.log(res);
// res: [{url: 'url示例值',path: 'path示例值',isExist: true,}]
```

返回对象示例：

```
[{ "url": "url示例值", "path": "path示例值", "isExist": true }]
```
