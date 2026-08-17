---
title: "上传文件"
source_url: "https://open.dingtalk.com/document/development/upload-objects-jsapi"
namespace: "development"
slug: "upload-objects-jsapi"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 上传文件"
doc_id: "MBV3FYafYt"
updated_at: "2025-09-17 20:56:44"
---

> Source: https://open.dingtalk.com/document/development/upload-objects-jsapi
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 上传文件
> Updated: 2025-09-17 20:56:44

# 上传文件

调用**biz.util.uploadFile**方法，实现上传本地资源到开发者服务器。

> **[!NOTE]**
>
> 目前仅支持上传图片。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 支持(钉钉版本≥6.5.35) | 支持(钉钉版本≥6.5.35) | 不支持 |

```
 dd.biz.util.uploadFile({
      url: 'http://xxxxx.dingtalk.com/xxx/xxx',
      filePath: 'https://resource/b1328xxx.image',
      fileName: '123',
      onSuccess: (res) => {
             console.log(JSON.stringify(res))
        },
      onFail:(err) =>{
             console.log(JSON.stringify(err))
        }
})
```

## 参数说明

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 开发者上传文件的服务器地址。 |
| filePath | String | 是 | 文件的虚拟地址，如[选择图片](https://open.dingtalk.com/document/orgapp/select-picture)方法获取的图片虚拟路径。 |
| fileName | String | 是 | 文件名，即对应的key, 开发者在服务器端通过key可以获取到文件二进制内容。 |
| header | Object | 否 | HTTP请求的Header。 |
| formData | Object | 否 | HTTP请求中其他额外的form数据。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用完成的回调函数，不管失败还是成功都会执行。 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | String | 开发者上传服务器返回的信息。 |
| statusCode | String | HTTP状态码。 |
| header | Object | 开发者服务器返回的header。 |
| size | Number | 文件大小，单位Byte。 |
| fileType | String | 文件类型。 |

## 错误码

| 参数 | 说明 |
| --- | --- |
| 2 | 参数不合法。 |
| 3 | 文件不存在。 |
