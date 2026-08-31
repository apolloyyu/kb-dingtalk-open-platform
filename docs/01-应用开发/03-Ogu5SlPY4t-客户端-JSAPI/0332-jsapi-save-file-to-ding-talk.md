---
title: "saveFileToDingTalk"
source_url: "https://open.dingtalk.com/document/development/jsapi-save-file-to-ding-talk"
namespace: "development"
slug: "jsapi-save-file-to-ding-talk"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "文件存储 > 钉盘 > saveFileToDingTalk"
doc_id: "09eHyTI9aq"
updated_at: "2025-08-27 18:08:21"
---

> Source: https://open.dingtalk.com/document/development/jsapi-save-file-to-ding-talk
> Path: 应用开发 / 客户端 JSAPI / 文件存储 > 钉盘 > saveFileToDingTalk
> Updated: 2025-08-27 18:08:21

# saveFileToDingTalk

调用saveFileToDingTalk，转存文件到钉盘。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10316) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10316) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `url`（string，必填）：文件在第三方服务器上的url地址或通过单步文件上传获取到的media\_id。  
    
  > 如果是url地址，要求资源请求返回消息头中需要包含Content-Length字段，且>0。
- `name`（string，必填）：文件保存的名字。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `data`（array，必填）：文件数据。
- `data[].spaceId`（string，必填）：钉盘空间id。
- `data[].fileId`（string，必填）：钉盘文件id。
- `data[].fileName`（string，必填）：文件名。
- `data[].fileSize`（string，必填）：文件大小，单位比特。
- `data[].fileType`（string，必填）：文件类型。

## **示例****代码**

### 默认出入参

```
dd.saveFileToDingTalk({
  url: 'https://ringnerippca.files.wordpress.com/20.pdf',
  name: '大合照.png',
  success: (res) => {
    const { data } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "data": [
    {
      "fileId": "3333",
      "spaceId": "xxxx",
      "fileName": "集体合照.png",
      "fileSize": "1024",
      "fileType": "png"
    }
  ]
}
```
