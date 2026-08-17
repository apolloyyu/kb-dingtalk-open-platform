---
title: "删除本地用户文件目录"
source_url: "https://open.dingtalk.com/document/development/delete-local-user-file-directory"
namespace: "development"
slug: "delete-local-user-file-directory"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 删除本地用户文件目录"
doc_id: "eThJPekt7z"
updated_at: "2025-09-17 21:01:02"
---

> Source: https://open.dingtalk.com/document/development/delete-local-user-file-directory
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 删除本地用户文件目录
> Updated: 2025-09-17 21:01:02

# 删除本地用户文件目录

调用**FileSystemManager.rmdir**，删除本地用户文件目录。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

> **[!NOTE]**
>
> 本接口只支持删除目录，不支持删除文件。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
    fileManager.rmdir({
      dirPath: `${dd.env.USER_DATA_PATH}/newDir`,
      recursive: false,
      success: (res) => {
        console.log(res)
      },
      fail:(err) =>{
         console.log(err)
      }
    });
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| dirPath | String | 是 | 本地用户文件目录路径。 |
| recursive | Boolean | 否 | 是否递归删除目录。   - true：是 - false：否，默认值   **[!NOTE]**  例如，dirPath值为a/b/c，实际完整的目录为a/b/c/d。   - 如果recursive值为true，则会删除目录c和d。 - 如果recursive值为false，接口会提示**目录不存在**，因为传的不是完整的路径。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 成功删除本地用户文件目录时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 目录不存在 https://usr/xxx | dirPath本地用户文件目录不存在。 |
