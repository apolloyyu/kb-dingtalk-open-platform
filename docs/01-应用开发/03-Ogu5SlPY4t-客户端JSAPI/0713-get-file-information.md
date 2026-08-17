---
title: "获取文件信息"
source_url: "https://open.dingtalk.com/document/development/get-file-information"
namespace: "development"
slug: "get-file-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 获取文件信息"
doc_id: "VbXmvsOjvn"
updated_at: "2025-09-17 21:00:58"
---

> Source: https://open.dingtalk.com/document/development/get-file-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 获取文件信息
> Updated: 2025-09-17 21:00:58

# 获取文件信息

调用**FileSystemManager.getFileInfo**，获取本地临时文件、本地缓存文件和本地用户文件的信息。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
fileManager.getFileInfo({
  filePath: `${dd.env.USER_DATA_PATH}/test.txt`,
  success:(res) => {
    console.log(res);
  },
  fail:(err) => {
    console.log(err)
  }
})
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| filePath | String | 是 | 文件的路径。   - 本地临时文件路径，可调用[选择图片](https://open.dingtalk.com/document/orgapp/dd-chooseimage)或[选择视频](https://open.dingtalk.com/document/orgapp/dd-choosevideo)获取。 - 本地缓存文件和本地用户文件路径，可调用[保存文件](https://open.dingtalk.com/document/orgapp/save-file)获取。 |
| digestAlgorithm | String | 否 | 文件编码，默认md5。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| size | Number | 文件大小，单位Byte。 |
| digest | String | 文件md5加密后的信息。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 12 | 文件不存在 | filePath路径错误或者没有对应的文件。 |
