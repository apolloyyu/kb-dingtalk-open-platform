---
title: "向本地用户文件末尾添加内容"
source_url: "https://open.dingtalk.com/document/development/append-content-to-the-end-of-the-local-user-file"
namespace: "development"
slug: "append-content-to-the-end-of-the-local-user-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 向本地用户文件末尾添加内容"
doc_id: "tlbPPYrEuG"
updated_at: "2025-09-17 21:01:05"
---

> Source: https://open.dingtalk.com/document/development/append-content-to-the-end-of-the-local-user-file
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 向本地用户文件末尾添加内容
> Updated: 2025-09-17 21:01:05

# 向本地用户文件末尾添加内容

调用**FileSystemManager.appendFile**，向本地用户文件末尾添加内容。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
fileManager.appendFile({
     filePath:`${dd.env.USER_DATA_PATH}/test.txt`,
     data:data,
     encoding:'utf8',
     success: (res) => {
            console.log(res);
        },
      fail:(err)=>{
            console.log(err);
          }
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| filePath | String | 是 | 要添加内容的文件路径。 |
| data | String | 是 | 要写入的文本内容或二进制数据。 |
| encoding | String | 否 | 指定写入文件的字符编码。   - ascii - base64 - hex - binary - ucs2/ucs-2/utf16le/utf-16le - utf-8/utf8，默认值 - latin1 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 向本地用户文件末尾添加内容成功时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 文件不存在 | filePath指定的文件路径错误。 |
