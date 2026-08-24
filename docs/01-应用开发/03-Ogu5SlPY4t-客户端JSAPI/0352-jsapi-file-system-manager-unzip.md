---
title: "FileSystemManager.unzip"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-unzip"
namespace: "development"
slug: "jsapi-file-system-manager-unzip"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.unzip"
doc_id: "CScHyRmJnf"
updated_at: "2025-08-27 18:08:32"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-unzip
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.unzip
> Updated: 2025-08-27 18:08:32

# FileSystemManager.unzip

调用FileSystemManager.unzip，解压本地用户文件。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10278) |

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

- `targetPath`（string，必填）：解压后存放文件的目录。
- `zipFilePath`（string，必填）：压缩文件的路径，只允许是zip压缩文件。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `success`（boolean，必填）：解压成功时，返回true。

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.unzip({
  targetPath: '${dd.env.USER_DATA_PATH}/test',
  zipFilePath: '${dd.env.USER_DATA_PATH}/test.zip',
  success: (res) => {
    const { success } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "success": true }
```
