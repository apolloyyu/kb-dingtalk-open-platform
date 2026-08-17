---
title: "压缩图片"
source_url: "https://open.dingtalk.com/document/development/compress-images"
namespace: "development"
slug: "compress-images"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 图片 > 压缩图片"
doc_id: "Mwe1WxW3z8"
updated_at: "2025-09-17 20:56:53"
---

> Source: https://open.dingtalk.com/document/development/compress-images
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 图片 > 压缩图片
> Updated: 2025-09-17 20:56:53

# 压缩图片

调用**biz.util.compressImage**，压缩图片。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥5.1.1) | 支持(钉钉版本≥5.1.1) | 不支持 |

```
dd.biz.util.compressImage({
      filePaths:["https://resource/MTY1Oxxxxx==.image"],
      compressLevel:4,
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
| filePaths | String Array | 是 | 要压缩的图片地址数组（只支持虚拟路径），可调用[选择图片](https://open.dingtalk.com/document/orgapp/select-picture)获取。 |
| compressLevel | Number | 否 | 压缩级别，支持0~4的整数，默认4。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| filePaths | String Array | 压缩后的图片虚拟路径列表。 |

## 错误码

| 参数 | 说明 |
| --- | --- |
| 3 | 内部异常。 |
