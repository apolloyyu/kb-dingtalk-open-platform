---
title: "解压本地用户文件"
source_url: "https://open.dingtalk.com/document/development/unzip-local-user-files"
namespace: "development"
slug: "unzip-local-user-files"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 解压本地用户文件"
doc_id: "aKFOv9QCrW"
updated_at: "2025-09-17 21:01:06"
---

> Source: https://open.dingtalk.com/document/development/unzip-local-user-files
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 解压本地用户文件
> Updated: 2025-09-17 21:01:06

# 解压本地用户文件

调用**FileSystemManager.unzip**，解压本地用户文件。

## **扫码体验**qrcode

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager()
fileManager.unzip({
  zipFilePath: `${dd.env.USER_DATA_PATH}/test.zip`,
  targetPath: `${dd.env.USER_DATA_PATH}/test`,
  success:(res) => {
    console.log(res)
  },
  fail:(err) => {
    console.log(err)
  }
})
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| zipFilePath | String | 是 | 压缩文件的路径，只允许是zip压缩文件。 |
| targetPath | String | 是 | 解压后存放文件的目录。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 解压成功时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 3 | 解压失败 | zipFilePath指定的文件非压缩文件。 |
| 10022 | 源文件不存在 | zipFilePath指定的压缩文件路径错误。 |
