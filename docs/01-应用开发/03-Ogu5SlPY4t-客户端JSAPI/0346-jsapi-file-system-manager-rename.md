---
title: "FileSystemManager.rename"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-rename"
namespace: "development"
slug: "jsapi-file-system-manager-rename"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.rename"
doc_id: "nnZkpSKpav"
updated_at: "2025-08-27 18:08:28"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-rename
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.rename
> Updated: 2025-08-27 18:08:28

# FileSystemManager.rename

调用FileSystemManager.rename，重命名本地用户文件或目录的名称并且可以移动到新目录下。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10273) |

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

- `newPath`（string，必填）：目标路径，如果目标目录不存在会自动创建。
- `oldPath`（string，必填）：文件或目录的源路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.rename({
  newPath: '${dd.env.USER_DATA_PATH}/newDir/test_new.txt',
  oldPath: '${dd.env.USER_DATA_PATH}/test.txt',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
