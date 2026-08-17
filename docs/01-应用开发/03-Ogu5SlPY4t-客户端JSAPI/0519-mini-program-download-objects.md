---
title: "下载文件"
source_url: "https://open.dingtalk.com/document/development/mini-program-download-objects"
namespace: "development"
slug: "mini-program-download-objects"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > 下载文件"
doc_id: "WXm1aVlYIR"
updated_at: "2025-09-17 20:58:48"
---

> Source: https://open.dingtalk.com/document/development/mini-program-download-objects
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > 下载文件
> Updated: 2025-09-17 20:58:48

# 下载文件

调用dd.downloadFile下载文件资源到本地。

## **扫****码体验**

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5254199951/p163543.png)

## **示例代码**

```
dd.downloadFile({
      url: 'http://img.alicdn.com/tfs/TB1x669SXXXXXbdaFXXXXXXXXXX-520-280.jpg',
      success({ filePath }) {
        dd.previewImage({
          urls: [filePath],
        });
      },
      fail(res) {
        dd.alert({
          content: res.errorMessage || res.error,
        });
      },
    });
```

## **入参**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| url | String | 是 | 下载文件地址。 |
| header | Object | 否 | HTTP 请求 Header。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | 类型 | 描述 |
| --- | --- | --- |
| filePath | String | 文件临时存放的位置。 |

## **错误码**

| **error** | **描述** |
| --- | --- |
| 12 | 下载失败。 |
| 13 | 没有文件权限。 |
