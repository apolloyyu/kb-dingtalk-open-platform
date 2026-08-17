---
title: "上传文件"
source_url: "https://open.dingtalk.com/document/development/dd-upload-objects"
namespace: "development"
slug: "dd-upload-objects"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > 上传文件"
doc_id: "NwUsMvaUqK"
updated_at: "2025-09-17 20:58:48"
---

> Source: https://open.dingtalk.com/document/development/dd-upload-objects
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > 上传文件
> Updated: 2025-09-17 20:58:48

# 上传文件

调用dd.uploadFile上传本地资源到开发者服务器。

## 扫码体验

![1595558281666-02](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2617472061/p170889.png)

## **示例****代码**

```
dd.uploadFile({
  url: '请使用自己服务器地址',
  fileType: 'image',
  fileName: 'file',
  filePath: '...',
  success: (res) => {
    dd.alert({
      content: '上传成功'
    });
  },
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| url | String | 是 | 开发者服务器地址。 |
| filePath | String | 是 | 要上传文件资源的本地定位符。 |
| fileName | String | 是 | 文件名，即对应的 key, 开发者在服务器端通过这个 key 可以获取到文件二进制内容。 |
| fileType | String | 是 | 文件类型：   - image - video - audio |
| header | Object | 否 | HTTP 请求 Header。 |
| formData | Object | 否 | HTTP 请求中其他额外的 form 数据。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| data | String | 服务器返回的数据。 |
| statusCode | String | HTTP 状态码。 |
| header | Object | 服务器返回的 header。 |

## **错误码**

| **error** | **描述** |
| --- | --- |
| 4 | 无权跨域调用，需要在开发者后台将上传URL设置为HTTP安全域名。 |
| 11 | 文件不存在。 |
| 12 | 上传文件失败。 |
| 13 | 没有文件权限。 |
