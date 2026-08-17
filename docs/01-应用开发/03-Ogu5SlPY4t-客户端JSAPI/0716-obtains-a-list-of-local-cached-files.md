---
title: "获取本地缓存文件列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-local-cached-files"
namespace: "development"
slug: "obtains-a-list-of-local-cached-files"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 获取本地缓存文件列表"
doc_id: "nO0J0AtxYv"
updated_at: "2025-09-17 21:01:00"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-local-cached-files
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 获取本地缓存文件列表
> Updated: 2025-09-17 21:01:00

# 获取本地缓存文件列表

调用**FileSystemManager.getSavedFileList**，获取本地缓存文件列表。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

> **[!NOTE]**
>
> 本接口获取的是调用[保存文件](https://open.dingtalk.com/document/orgapp/save-file)接口保存为本地缓存的文件，保存为本地用户的文件不支持获取。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
 fileManager.getSavedFileList({
      success: (res) => {
        console.log(res.fileList);
      },
      fail: (err) => {
        console.log(err);
      }
    });
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 成功获取本地缓存文件列表时，返回true。 |
| fileList | Array<Object> | 本地缓存的文件列表。 |
| filePath | String | 本地缓存文件的路径。 |
| size | Number | 文件大小，单位Byte。 |
| createTime | Number | 文件保存的时间戳，单位毫秒。 |
