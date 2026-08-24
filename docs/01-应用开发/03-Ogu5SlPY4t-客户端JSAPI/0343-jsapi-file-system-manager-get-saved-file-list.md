---
title: "FileSystemManager.getSavedFileList"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-get-saved-file-list"
namespace: "development"
slug: "jsapi-file-system-manager-get-saved-file-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.getSavedFileList"
doc_id: "f59RsSuZHN"
updated_at: "2025-08-27 18:08:27"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-get-saved-file-list
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.getSavedFileList
> Updated: 2025-08-27 18:08:27

# FileSystemManager.getSavedFileList

调用FileSystemManager.getSavedFileList，获取本地缓存文件列表。

> 本接口获取的是调用保存文件接口保存为本地缓存的文件，保存为本地用户的文件不支持获取。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10268) |

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

### 出参

- `success`（boolean，必填）：成功获取本地缓存文件列表时，返回true。
- `fileList`（array，必填）：本地缓存的文件列表。
- `fileList[].filePath`（string，必填）：本地缓存文件的路径。
- `fileList[].size`（number，必填）：文件大小，单位Byte。
- `fileList[].createTime`（number，必填）：文件保存的时间戳，单位毫秒。

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.getFileSystemManager();

fileSystemManager.getSavedFileList({
  success: (res) => {
    const { success, fileList } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "success": true,
  "fileList": [
    {
      "size": 10,
      "filePath": "本地缓存文件的路径示例值",
      "createTime": 1688350073000
    }
  ]
}
```
