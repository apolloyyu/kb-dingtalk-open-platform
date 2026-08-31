---
title: "uploadFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-upload-file"
namespace: "development"
slug: "jsapi-upload-file"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 网络 > 上传下载 > uploadFile"
doc_id: "QGcTcYgEAb"
updated_at: "2025-08-27 18:07:19"
---

> Source: https://open.dingtalk.com/document/development/jsapi-upload-file
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 网络 > 上传下载 > uploadFile
> Updated: 2025-08-27 18:07:19

# uploadFile

调用uploadFile，上传本地资源到开发者服务器。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10281) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10281) |

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

- `url`（string，必填）：开发者服务器地址。
- `header`（object）：HTTP 请求 Header。  
    
  > \*\*注意：\*\*不携带cookie信息
- `formData`（object）：HTTP 请求中其他额外的 form 数据。
- `filePath`（string，必填）：文件的虚拟地址，如[选择图片](https://open.dingtalk.com/document/orgapp/jsapi-chooseImage)方法获取的图片虚拟路径。
- `fileName`（string，必填）：文件名，即对应的 key, 开发者在服务器端通过这个 key 可以获取到文件二进制内容。
- `fileType`（string，必填）：文件类型：  
    
  \* image：图片  
  \* video：视频  
  \* audio：音频

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `data`（string）：服务器返回的数据。
- `header`（object）：服务器返回的 header。
- `statusCode`（string）：HTTP 状态码。

## **示例****代码**

### 默认出入参

```
dd.uploadFile({
  url: 'https://xxx.org/uploadFile',
  header: {},
  fileName: 'xxx',
  filePath: 'https://resource/apml31fc26337c885be15b4fd1c0abefee8f.image',
  fileType: 'image',
  formData: {},
  success: (res) => {
    const { data, header, statusCode } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "data": "success",
  "header": { "content-type": "application/json" },
  "statusCode": "200"
}
```
