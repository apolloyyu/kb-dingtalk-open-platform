---
title: "上传附件"
source_url: "https://open.dingtalk.com/document/development/upload-attachment"
namespace: "development"
slug: "upload-attachment"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "AI 表格 > 上传附件"
doc_id: "IeKFCarUJR"
updated_at: "2025-09-10 19:35:01"
---

> Source: https://open.dingtalk.com/document/development/upload-attachment
> Path: 应用开发 / 服务端 API / AI 表格 > 上传附件
> Updated: 2025-09-10 19:35:01

# 上传附件

该文档介绍如何在AI表格中上传附件。

在AI表格中上传附件，类似于如下图所示操作：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5066362571/p979058.png)

上传附件需要三步：

1. 获取上传信息，请参考[获取资源上传信息](0581-api-getresourceuploadinfo.md)接口。
2. 将本地文件上传到第一步返回的`uploadUrl`中，可以使用 `PUT` 请求上传本地文件。

   下面是一个使用`cURL`命令的示例（示例中的@符号不可省略）。

   ```
   curl -X PUT -H "Content-Type: image/jpeg" --data-binary @/path/to/your/image.jpg {第一步返回的uploadUrl}
   ```
3. 调用[新增记录](0468-api-notable-insertrecords.md)和[更新多行记录](0471-api-noatable-updaterecords.md)接口将附件写入AI表格。

   记录值的格式如下所示。

   ```
   [
     {
         "filename": "pikaqiu.jpg", // 第一步传入的resourceName
         "size": 200, // 第一步传入的 size
         "type": "image/jpeg", // 第一步传入的mediaType
         "url": "xxx"，// 第一步返回的 resourceUrl，注意不是uploadUrl，例如 /core/api/resources/img/xxx
         "resourceId": "xxx" // 第一步返回的 resourceId，例如 9ee6c515-4ebd-47a0-b8c3-5383c4241d84
     }
   ]
   ```
