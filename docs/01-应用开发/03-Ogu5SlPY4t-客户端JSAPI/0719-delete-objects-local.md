---
title: "删除本地用户文件"
source_url: "https://open.dingtalk.com/document/development/delete-objects-local"
namespace: "development"
slug: "delete-objects-local"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 删除本地用户文件"
doc_id: "7rqJZrtSw3"
updated_at: "2025-09-17 21:01:02"
---

> Source: https://open.dingtalk.com/document/development/delete-objects-local
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 删除本地用户文件
> Updated: 2025-09-17 21:01:02

# 删除本地用户文件

调用**FileSystemManager.unlink**，删除本地用户文件。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

> **[!IMPORTANT]**
>
> 调用本接口，只支持删除本地用户文件。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
    fileManager.unlink({
      filePath: `${dd.env.USER_DATA_PATH}/a.jpg`,
      success(res) {
        console.log(res)
      },
      fail(err) {
        console.error(res)
      }
    })
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| filePath | String | 是 | 本地用户文件路径。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 成功删除本地用户文件时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 文件不存在 https://usr/xxx.txt | filePath指定的文件路径错误。 |
| 10023 | 传入的路径是一个目录 https://usr/xxx | filePath只能传文件路径。 |
