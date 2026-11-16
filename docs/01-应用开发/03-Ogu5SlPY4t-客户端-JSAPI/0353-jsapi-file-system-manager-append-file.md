---
title: "FileSystemManager.appendFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-append-file"
namespace: "development"
slug: "jsapi-file-system-manager-append-file"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.appendFile"
doc_id: "mKQ8zQYUW8"
updated_at: "2025-08-27 18:08:25"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-append-file
> Path: 应用开发 / 客户端 JSAPI / 文件存储 > 文件 > FileSystemManager.appendFile
> Updated: 2025-08-27 18:08:25

# FileSystemManager.appendFile

调用FileSystemManager.appendFile，向本地用户文件末尾添加内容。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10264) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `data`（string，必填）：要写入的文本内容或二进制数据。
- `encoding`（string）：指定写入文件的字符编码：  
    
  \* ascii  
    
  \* base64  
    
  \* hex  
    
  \* binary  
    
  \* ucs2/ucs-2/utf16le/utf-16le  
    
  \* utf-8/utf8，默认值  
    
  \* latin1
- `filePath`（string，必填）：要添加内容的文件路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.appendFile({
  data: 'content',
  encoding: 'utf8',
  filePath: '${dd.env.USER_DATA_PATH}/test.txt',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
