---
title: "判断文件或目录是否存在"
source_url: "https://open.dingtalk.com/document/development/determine-whether-a-file-or-directory-exists"
namespace: "development"
slug: "determine-whether-a-file-or-directory-exists"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 判断文件或目录是否存在"
doc_id: "FIxepvpWAO"
updated_at: "2025-09-17 21:00:57"
---

> Source: https://open.dingtalk.com/document/development/determine-whether-a-file-or-directory-exists
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 判断文件或目录是否存在
> Updated: 2025-09-17 21:00:57

# 判断文件或目录是否存在

调用**FileSystemManager.access**，判断文件或者目录是否存在。

## **扫码体验**

![qrcode (1)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
    fileManager.access({
      path:`${dd.env.USER_DATA_PATH}/newDir`,
      success:(res)=>{
        dd.alert({
          title:'文件是否存在',
          content:JSON.stringify(res),
        }); 
      },
      fail:(err) =>{
        dd.alert({
          title:'文件是否存在',
          content:JSON.stringify(err),
        }); 
      }
    })
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| path | String | 是 | 文件夹路径或者文件路径。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 文件或目录存在时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 文件/目录不存在 https://usr/xxx | path参数内的文件或文件夹路径不存在。 |
