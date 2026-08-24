---
title: "FileSystemManager.rmdir"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-rmdir"
namespace: "development"
slug: "jsapi-file-system-manager-rmdir"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.rmdir"
doc_id: "23KNvUGB2w"
updated_at: "2025-08-27 18:08:28"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-rmdir
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.rmdir
> Updated: 2025-08-27 18:08:28

# FileSystemManager.rmdir

调用FileSystemManager.rmdir，删除本地用户文件目录。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10274) |

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

- `dirPath`（string，必填）：本地用户文件目录路径。
- `recursive`（boolean）：是否递归删除目录：  
    
  \* true：是   
  \* false：否，默认值

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `success`（boolean，必填）：成功删除本地用户文件目录时，返回true。

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.rmdir({
  dirPath: '${dd.env.USER_DATA_PATH}/newDir',
  recursive: true,
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
