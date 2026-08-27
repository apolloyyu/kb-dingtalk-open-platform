---
title: "downloadFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-download-file"
namespace: "development"
slug: "jsapi-download-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 网络 > 上传下载 > downloadFile"
doc_id: "22fDJkzjEx"
updated_at: "2025-08-27 18:07:19"
---

> Source: https://open.dingtalk.com/document/development/jsapi-download-file
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 网络 > 上传下载 > downloadFile
> Updated: 2025-08-27 18:07:19

# downloadFile

调用downloadFile，下载文件资源到本地。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10282) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10282) |

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

- `url`（string，必填）：下载文件地址。
- `header`（object）：HTTP 请求 Header。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `filePath`（string）：文件临时存放的位置。

## **示例****代码**

### 默认出入参

```
dd.downloadFile({
  url: 'https://gw.alicdn.com/imgextra/i3/O1CN01Eg6xCm1nnsXZCnkP4_!!6000000005135-2-tps-200-200.png',
  header: { 'content-type': 'image/jpeg' },
  success: (res) => {
    const { filePath } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "filePath": "https://resource/apml31fc26337c885be15b4fd1c0abefee8f.image" }
```
