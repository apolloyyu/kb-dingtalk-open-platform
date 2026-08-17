---
title: "重命名并移动本地用户文件或目录"
source_url: "https://open.dingtalk.com/document/development/rename-and-move-local-user-files-or-directories"
namespace: "development"
slug: "rename-and-move-local-user-files-or-directories"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 重命名并移动本地用户文件或目录"
doc_id: "ZeNItEvgwl"
updated_at: "2025-09-17 21:01:04"
---

> Source: https://open.dingtalk.com/document/development/rename-and-move-local-user-files-or-directories
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 重命名并移动本地用户文件或目录
> Updated: 2025-09-17 21:01:04

# 重命名并移动本地用户文件或目录

调用**FileSystemManager.rename**，重命名本地用户文件或目录的名称并且可以移动到新目录下。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

> **[!NOTE]**
>
> 调用本接口可以实现以下功能：
>
> - 重命名本地用户文件或目录。
> - 移动本地用户文件或目录。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
fileManager.rename({
  oldPath: `${dd.env.USER_DATA_PATH}/test.txt`,
  newPath: `${dd.env.USER_DATA_PATH}/newDir/test_new.txt`,
  success: (res) => {
    consoloe.log(res);
  },
  fail:(err) => {
    console.log(err)
  }
})
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| oldPath | String | 是 | 文件或目录的源路径。 |
| newPath | String | 是 | 目标路径，如果目标目录不存在会自动创建。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 成功重命名并移动本地用户文件或目录时，返回true。 |
| files | Array<String> | 本地用户目录下的文件或目录列表。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 源不存在 https://usr/xxx | oldPath本地用户文件目录不存在。 |
