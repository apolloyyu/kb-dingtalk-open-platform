---
title: "FileSystemManager.readFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-read-file"
namespace: "development"
slug: "jsapi-file-system-manager-read-file"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.readFile"
doc_id: "rVI6c18CJw"
updated_at: "2025-08-27 18:08:30"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-read-file
> Path: 应用开发 / 客户端 JSAPI / 文件存储 > 文件 > FileSystemManager.readFile
> Updated: 2025-08-27 18:08:30

# FileSystemManager.readFile

调用FileSystemManager.readFile，读取本地用户文件的内容。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10272) |

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

- `encoding`（string）：指定读物文件的字符编码，如果不传该参数，则以ArrayBuffer格式读取文件的二进制内容。 可选值有：  
  \* \*\*ascii\*\* ：基于拉丁字母的单字节编码方式，以 0-127 编码为 ascii 字符集。举例：二进制（01100001），十进制（97），编码字符为 a 。  
  \* \*\*latin1\*\* ：向下兼容 ascii（0x00-0x7F），从 0x00-0xFF 的单字节编码方式。举例：二进制（10000000），十六进制为 0x80，编码字符为 latin1 第 129 个字符。  
  \* \*\*hex\*\* ：将任意一个字节以两个 16 进制数字编码的方式。举例：二进制（00001111），16 进制为 0x0f，编码字符为 0f。  
  \* \*\*binary\*\* ：编码方式和 latin1 相同。  
  \* \*\*utf8 / utf-8\*\*：按照 utf8 的一个或多个字节的编码方式（0 ~ 127为单字节，和 ascii 一致），将二进制数据转换为 unicode 编码的编码方式。举例：二进制 11100110 10110001 10001001，转换 unicode 后为 110110001001001 对应 16 进制为 0x6c49，\u6c49 对应字符为 “汉”。  
  \* \*\*ucs2 / ucs-2\*\*：将二进制的高位字节放后面，低位字节放前面，以两个字节转为 unicode 的编码方式。举例：二进制 0110000001001111，16 进制 0x604f，编码转换后为 0100111101100000，16 进制为 0x4f60，\u4f60 的字符为“你”。  
  \* \*\*utf16le / utf-16le\*\*：可看成是 UCS-2 的父集。在没有辅助平面字符前，UTF-16 与 UCS-2 所指的是同一的意思。  
  \* \*\*base64\*\*：基于 64 个可打印字符来表示二进制数据的编码方式。举例：二进制（01101001 10110111 00011101）base64 编码转换后为（00011010 00011011 00011100 00011101），对应字符为 abcd 。
- `filePath`（string，必填）：本地用户文件路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `success`（boolean，必填）：成功读取本地用户文件内容时，返回true。
- `data`（string，必填）：文件的读取内容。

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.readFile({
  encoding: 'base64',
  filePath: '${dd.env.USER_DATA_PATH}/a.jpg',
  success: (res) => {
    const { data, success } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "data": "abc", "success": true }
```
