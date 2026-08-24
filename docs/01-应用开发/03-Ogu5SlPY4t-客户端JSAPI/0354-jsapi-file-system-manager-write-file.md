---
title: "FileSystemManager.writeFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-write-file"
namespace: "development"
slug: "jsapi-file-system-manager-write-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.writeFile"
doc_id: "Cpm9mal3HB"
updated_at: "2025-08-27 18:08:33"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-write-file
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.writeFile
> Updated: 2025-08-27 18:08:33

# FileSystemManager.writeFile

调用FileSystemManager.writeFile，向本地用户目录内写入文件。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10276) |

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
- `filePath`（string，必填）：写入文件的本地用户目录路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.writeFile({
  data: 'some text or arrayBuffer',
  encoding: 'base64',
  filePath: '${dd.env.USER_DATA_PATH}/test.txt',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
