---
title: "压缩图片"
source_url: "https://open.dingtalk.com/document/development/dd-compressimage"
namespace: "development"
slug: "dd-compressimage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 压缩图片"
doc_id: "2UVcoMbA61"
updated_at: "2025-09-17 20:58:58"
---

> Source: https://open.dingtalk.com/document/development/dd-compressimage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 压缩图片
> Updated: 2025-09-17 20:58:58

# 压缩图片

调用dd.compressImage压缩图片。

## 扫码体验

![1595557858453-2 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2579903061/p171726.png)

## **示例代码**

```
dd.compressImage({
    filePaths:['https://resource/apmlcc0ed184daffc5a0d8da86b2f518cf7b.image'],
    compressLevel:1,
    success:(res)=>{
        console.log(JSON.stringify(res))
    }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| filePaths | String Array | 是 | 要压缩的图片地址数组。 |
| compressLevel | Number | 否 | 压缩级别，支持 0 ~ 4 的整数，默认 4。   - **0**：低质量。 - **1**：中等质量。 - **2**：高质量。 - **3**：不压缩。 - **4**：根据网络适应。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| filePaths | String Array | 压缩后的路径数组。 |
