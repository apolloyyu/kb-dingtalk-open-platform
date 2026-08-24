---
title: "chooseFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-file"
namespace: "development"
slug: "jsapi-choose-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > chooseFile"
doc_id: "mQQNtnYY0B"
updated_at: "2025-12-08 16:47:04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-file
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > chooseFile
> Updated: 2025-12-08 16:47:04

# chooseFile

选择本地文件。

调用dd.chooseFile，选择本地文件，返回其虚拟路径。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.1.5 | 7.1.5 | 不支持 | 7.1.10 | 7.1.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11736) |
| 小程序 | 7.1.5 | 7.1.5 | 不支持 | 7.1.10 | 7.1.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11736) |

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

- `count`（number）：最多可以选择的文件个数，取值范围[1,9]，默认值1。
- `multiSelection`（boolean）：是否允许多选，默认值false。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### files

- `files`（object，必填）：文件对象。
- `files.name`（string，必填）：文件名。
- `files.path`（string，必填）：文件虚拟路径。
- `files.size`（number，必填）：文件大小。

## **示例****代码**

### 默认出入参

```
dd.chooseFile({
  count: 1,
  multiSelection: false,
});
```

返回对象示例：

```
{
  "files": {
    "name": `name示例值`,
    "path": "https://resource/bc222c20be849b002903a686f3921a9f.file",
    "size": 84
  }
}
```
