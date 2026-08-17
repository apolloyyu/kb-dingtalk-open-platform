---
title: "保存文件"
source_url: "https://open.dingtalk.com/document/development/save-file"
namespace: "development"
slug: "save-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 保存文件"
doc_id: "DMPYt8Q5qL"
updated_at: "2025-09-17 21:00:58"
---

> Source: https://open.dingtalk.com/document/development/save-file
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 保存文件
> Updated: 2025-09-17 21:00:58

# 保存文件

调用**FileSystemManager.saveFile**，将本地临时文件保存为本地缓存文件或本地用户文件。

## **扫码体验**

![qrcode  ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795915661/p497732.png)

> **[!NOTE]**
>
> 本接口会移动临时文件，因此调用成功后，本地临时路径的tempFilePath将不可用。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.26) | 支持(钉钉版本≥6.5.25) | 不支持 |

## **示例代码**

```
let fileManager = dd.getFileSystemManager();
dd.chooseImage({
  count: 1,
  success(res) {
    fileManager.saveFile({
      tempFilePath: res.apFilePaths[0],
      filePath: `${dd.env.USER_DATA_PATH}/newDir/img.png`,
      success: (result) => {
        console.log(result.savedFilePath);
      },
      fail:(err) => {
        console.log(err)
      }
    })
  }
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| tempFilePath | String | 是 | 本地临时文件路径。 |
| filePath | String | 否 | 要存储的目标路径。   - 指定该参数，本地临时文件存储为本地用户文件。 - 不指定该参数，本地临时文件存储为本地缓存文件。   **[!NOTE]**   - 指定该参数存储为本地用户文件时，该参数需要指定存储后文件的名称和后缀。例如`${dd.env.USER_DATA_PATH}/newDir/img.png`。 - filePath指定的目录如果不存在，该接口会按照指定的路径创建目录并保存文件。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **说明** |
| --- | --- | --- |
| success | Boolean | 目录创建成功时，返回true。 |
| savedFilePath | String | 文件保存的路径。 |

### **失败**

| **返回信息** | **类型** | **说明** |
| --- | --- | --- |
| Object | Object | 错误信息。 |

## **错误码**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 10022 | 指定的路径找不到文件 | tempFilePath参数不正确或者已失效。 |
| 3 | 保存文件失败 | 需要检查filePath参数是否带文件名称和后缀。 |
