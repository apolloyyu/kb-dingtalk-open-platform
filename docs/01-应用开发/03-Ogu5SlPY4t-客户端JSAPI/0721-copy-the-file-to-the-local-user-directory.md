---
title: "复制文件保存到本地用户目录内"
source_url: "https://open.dingtalk.com/document/development/copy-the-file-to-the-local-user-directory"
namespace: "development"
slug: "copy-the-file-to-the-local-user-directory"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 复制文件保存到本地用户目录内"
doc_id: "MXZeHMts3C"
updated_at: "2025-09-17 21:01:03"
---

> Source: https://open.dingtalk.com/document/development/copy-the-file-to-the-local-user-directory
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 复制文件保存到本地用户目录内
> Updated: 2025-09-17 21:01:03

# 复制文件保存到本地用户目录内

调用**FileSystemManager.copyFile**，复制文件保存到本地用户目录。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

> **[!NOTE]**
>
> 调用本接口可以将本地临时文件、本地缓存文件和本地用户文件复制保存到本地用户目录内。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
    fileManager.copyFile({
            srcPath: srcPath,
            destPath: `${dd.env.USER_DATA_PATH}/newDir/a.jpg`,
            success: (res) => {
                 console.log(res)
            },
            fail: (err) => {
                 console.log(err)
            }
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| srcPath | String | 是 | 源文件路径。 |
| destPath | String | 是 | 需要复制存储的目标本地用户目录，该参数值建议指定复制文件名称和后缀。例如：`${dd.env.USER_DATA_PATH}/newDir/test.jpg`。  **[!NOTE]**  如果destPath路径不存在，本接口会执行创建。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 成功复制文件保存到本地用户目录时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 2 | 接口参数无效 | 需要检查srcPath和destPath参数值是否正确。 |
| 10022 | 源文件不存在 | srcPath指定的文件路径错误。 |
