---
title: "创建本地用户目录"
source_url: "https://open.dingtalk.com/document/development/creat-folder"
namespace: "development"
slug: "creat-folder"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 创建本地用户目录"
doc_id: "wEXnYzPxLB"
updated_at: "2025-09-17 21:00:57"
---

> Source: https://open.dingtalk.com/document/development/creat-folder
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 创建本地用户目录
> Updated: 2025-09-17 21:00:57

# 创建本地用户目录

调用**FileSystemManager.mkdir**，创建本地用户目录。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
    fileManager.mkdir({
      dirPath: `${dd.env.USER_DATA_PATH}/newDir`,
      recursive: false,
      success: (res) => {
        console.log(JSON.stringify(res))
      },
      fail: (err) => {
        console.log(JSON.stringify(err))
      }
    });
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| dirPath | String | 是 | 创建的目录路径。 |
| recursive | Boolean | 否 | 是否递归创建该目录的上级目录后再创建该目录。   - **true**：是 - **false**：否，默认值   **[!NOTE]**  例如，dirPath值为：/a/b/c。   - 如果recursive传true，创建目录时会先创建a，再创建b，最后再创建c。 - 如果recursive传false，a、b、c只要有一个目录不存在，接口会提示父级目录不存在。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 目录创建成功时，返回true。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 上级目录不存在 https://usr/xxx | recursive传false时，dirPath参数值内的目录不存在。 |
| 10025 | 有同名文件或目录 https://usr/xxx | dirPath参数值内的目录已存在。 |
