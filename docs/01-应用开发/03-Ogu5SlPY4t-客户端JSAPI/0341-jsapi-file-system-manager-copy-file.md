---
title: "FileSystemManager.copyFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-copy-file"
namespace: "development"
slug: "jsapi-file-system-manager-copy-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.copyFile"
doc_id: "NY0J6wwMyd"
updated_at: "2025-08-27 18:08:25"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-copy-file
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.copyFile
> Updated: 2025-08-27 18:08:25

# FileSystemManager.copyFile

调用FileSystemManager.copyFile，复制文件保存到本地用户目录。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10266) |

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

- `srcPath`（string，必填）：源文件路径。
- `destPath`（string，必填）：需要复制存储的目标本地用户目录，该参数值建议指定复制文件名称和后缀。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.copyFile({
  srcPath: 'https://resource/43fbb13460c2c917ef7d0370d9bf09f0.file',
  destPath: '${dd.env.USER_DATA_PATH}/newDir/a.jpg',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
