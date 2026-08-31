---
title: "通过指定Range下载部分内容"
source_url: "https://open.dingtalk.com/document/development/use-range-download-a-part-of-content"
namespace: "development"
slug: "use-range-download-a-part-of-content"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件传输 > 通过指定Range下载部分内容"
doc_id: "PAkAlDxrKC"
updated_at: "2025-09-10 19:36:07"
---

> Source: https://open.dingtalk.com/document/development/use-range-download-a-part-of-content
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件传输 > 通过指定Range下载部分内容
> Updated: 2025-09-10 19:36:07

# 通过指定Range下载部分内容

本文主要介绍如何通过指定Range下载部分内容。

## **什么是指定HTTP Range下载内容**

下载OSS中的大文件（超过100M）时，如果传输过程中受到网络环境影响，则会传输失败。这时，可以通过HTTP Range请求获取大文件的部分内容，示例如下。

```
Get /ObjectName HTTP/1.1
Host:xxxx.oss-cn-hangzhou.aliyuncs.com
Date:Tue, 17 Nov 2015 17:27:45 GMT
Authorization:SignatureValue
Range:bytes=[$ByteRange]
```

> **[!NOTE]**
>
> [$ByteRange]指请求资源的范围，单位为“Byte（字节）”。示例如下。
>
> - `Range: bytes=0-499`表示第0~499字节范围的内容。
> - `Range: bytes=500-999`表示第500~999字节范围的内容。
> - `Range: bytes=-500`表示最后500字节的内容。
> - `Range: bytes=500-`表示从第500字节开始到文件结束部分的内容。
> - `Range: bytes=0-`表示第一个字节到最后一个字节，即完整的文件内容。
> - OSS不支持多Range参数，即不支持指定多个范围。如果指定多个范围，OSS只返回第一个Range的数据，例如：`Range:bytes=0-499,500-999`，OSS只返回0-499字节范围的内容。
> - [$ByteRange]有效区间在0至`content-length - 1`的范围内。

如果HTTP Range请求合法，响应返回值为`206`并在响应头中包含`Content-Range`。如果HTTP Range请求不合法，或者指定范围不在有效区间，会导致Range不生效，响应返回值为`200`，并传送整个Object内容。如下为HTTP Range请求不合法的示例及错误说明。

> **[!NOTE]**
>
> 此处假设Object资源大小为1000字节，Range有效区间为0~999。

- `Range: byte=0-499`：格式错误，byte应为bytes。
- `Range: bytes=0-1000`：末字节1000超出有效区间。
- `Range: bytes=1000-2000`：指定范围超出有效区间。
- `Range: bytes=1000-`：首字节超出有效区间。
- `Range: bytes=-2000`：指定范围超出有效区间。

### **兼容行为**

使用HTTP Range时，增加请求头`x-oss-range-behavior:standard`，可以改变指定范围不在有效区间时OSS的行为。行为改变的示例如下：

> **[!NOTE]**
>
> 此处假设Object资源大小为1000字节，Range有效区间为0-999。如通过HTTP Range请求获取大文件的部分内容时，因选取了无效的范围，导致OSS返回InvalidRange错误码，详细错误信息如下：`The requested range cannot be satisfied`

- `Range: bytes=500-2000`：末字节超出有效区间，返回500-999字节范围内容。
- `Range: bytes=1000-2000`：首字节超出有效区间，返回错误`416 (InvalidRange)`。
- `Range: bytes=1000-`：首字节超出有效区间，返回错误`416 (InvalidRange)`。
- `Range: bytes=-2000`：指定范围超出有效区间，返回0-999字节，即完整的文件内容。

## **示例**

针对上述内容，本文提供如下HTTP Range请求示例。

> **[!NOTE]**
>
> 此处假设Object资源大小为1000字节，Range有效区间为0-999。

### **正常请求示例**

- 请求Object资源0-499字节范围内的内容。

  ```
  GET /ObjectName
  Range: bytes=0-499
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 02:51:30 GMT
  Authorization: Sigature

  206 (Partial Content)
  content-length: 500
  content-range: bytes 0-499/1000
  connection: keep-alive
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA928B227D52731327DE078
  date: Fri, 18 Oct 2019 02:51:30 GMT
  [500 bytes of object data]
  ```
- 请求Object资源第500字节到文件结尾的内容。

  ```
  GET /ObjectName
  Range: bytes=500-
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 03:24:39 GMT
  Authorization: Signature

  206 (Partial Content)
  content-length: 500
  content-range: bytes 500-999/1000
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA9307750EBE33332E3720A
  date: Fri, 18 Oct 2019 03:24:39 GMT
  [500 bytes of object data]
  ```
- 请求Object资源最后500字节的内容。

  ```
  GET /ObjectName
  Range: bytes=-500
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 03:23:22 GMT
  Authorization: Signature

  206 (Partial Content)
  content-length: 500
  content-range: bytes 500-999/1000
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA9302A6646AC37397F7039
  date: Fri, 18 Oct 2019 03:23:22 GMT
  [500 bytes of object data]
  ```

### **超出范围的请求示例**

- 末字节1000超出有效区间，导致Range不生效，响应返回值为`200`，并传送整个Object内容。

  ```
  GET /ObjectName
  Range: bytes=0-1000
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 03:00:02 GMT
  Authorization: Signature

  200 (OK)
  content-length: 1000
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA92AB204321E36347F3E7D
  date: Fri, 18 Oct 2019 03:00:02 GMT
  [1000 bytes of object data]
  ```
- 指定范围超出有效区间，导致Range不生效，响应返回值为`200`，并传送整个Object内容。

  ```
  GET /ObjectName
  Range: bytes=1000-2000
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 02:56:24 GMT
  Authorization: Sigature

  200 (OK)
  content-length: 1000
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA929D9CCCC823835CBE134
  date: Fri, 18 Oct 2019 02:56:25 GMT
  [1000 bytes of object data]
  ```

### **兼容行为请求示例**

- 增加`x-oss-range-behavior:standard`请求头，末字节超出有效区间，返回500-999字节范围的内容。

  ```
  GET /ObjectName
  x-oss-range-behavior: standard
  Range: bytes=500-2000
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 07:02:23 GMT
  Authorization: Signature

  206 (Partial Content)
  content-length: 500
  content-range: bytes 500-999/1000
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA9637FB3B1C73234CC59EB
  date: Fri, 18 Oct 2019 07:02:23 GMT
  [500 bytes of object data]
  ```
- 增加`x-oss-range-behavior:standard`请求头，首字节超出有效区间，返回`416`错误。

  ```
  GET /ObjectName
  x-oss-range-behavior: standard
  Range: bytes=1000-2000
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 07:04:23 GMT
  Authorization: Signature

  416 (Requested Range Not Satisfiable)
  content-length: 345
  x-oss-request-id: 5DA963F7CEBFAA3931BF91F5
  date: Fri, 18 Oct 2019 07:04:23 GMT
  content-type: application/xml
  <?xml version="1.0" encoding="UTF-8"?>
  <Error>
    <Code>InvalidRange</Code>
    <Message>The requested range cannot be satisfied</Message>
    <RequestId>5DA963F7CEBFAA3931BF91F5</RequestId>
    <HostId>bucket.oss-cn-hangzhou.aliyuncs.com</HostId>
    <ActualObjectSize>1000</ActualObjectSize>
    <RangeRequested>bytes=1000-2000</RangeRequested>
  </Error>
  ```
- 增加`x-oss-range-behavior:standard`请求头，指定范围超出有效区间，返回0-999字节，即完整的文件内容。

  ```
  GET /ObjectName
  x-oss-range-behavior: standard
  Range: bytes=-2000
  Host: bucket.oss-cn-hangzhou.aliyuncs.com
  Date: Fri, 18 Oct 2019 07:06:39 GMT
  Authorization: Signature

  206 (Partial Content)
  content-length: 1000
  content-range: bytes 0-999/1000
  etag: "CACF99600561A31D494569C979E6FB81"
  x-oss-request-id: 5DA9647FC4334F3534AF9A83
  date: Fri, 18 Oct 2019 07:06:39 GMT
  [1000 bytes of object data]
  ```
