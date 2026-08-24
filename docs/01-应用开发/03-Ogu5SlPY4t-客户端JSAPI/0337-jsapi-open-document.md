---
title: "openDocument"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-document"
namespace: "development"
slug: "jsapi-open-document"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > openDocument"
doc_id: "JLWTZaS4fe"
updated_at: "2025-08-27 18:07:12"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-document
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > openDocument
> Updated: 2025-08-27 18:07:12

# openDocument

在新页面打开文档。

调用dd.openDocument，在新页面打开文档。安卓端仅支持端内打开预览 pdf 格式文件，其他文件格式不支持端内访问。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11464) |
| 小程序 | 6.5.60 | 6.5.60 | 7.0.0 | 6.5.60 | 6.5.60 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11464) |

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

- `filePath`（string，必填）：文件路径（仅支持本地路径）
- `fileType`（string）：文件类型，已支持类型：  
    
  \* doc  
  \* docx  
  \* xls  
  \* xlsx  
  \* ppt  
  \* pptx  
  \* pdf  
  \* zip

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |
| 2 | 参数无效 |

## **示例****代码**

### 默认出入参

```
dd.openDocument({
  filePath: '本地路径',
  fileType: 'doc',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
