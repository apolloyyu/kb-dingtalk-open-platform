---
title: "钉盘文件预览"
source_url: "https://open.dingtalk.com/document/development/nail-plate-file-preview"
namespace: "development"
slug: "nail-plate-file-preview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 钉盘文件预览"
doc_id: "odqp7v4fSk"
updated_at: "2025-09-17 21:01:17"
---

> Source: https://open.dingtalk.com/document/development/nail-plate-file-preview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 钉盘文件预览
> Updated: 2025-09-17 21:01:17

# 钉盘文件预览

调用**dd.previewFileInDingTal**k预览钉盘文件。

## 代码示例

```
dd.previewFileInDingTalk({
    corpId:"dingf8b3508f3073b265",
    spaceId:"13557022",
    fileId:"11452819",
    fileName:"钉盘快速入门.pdf",
    fileSize:1024,
    fileType:"pdf",
})
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| spaceId | String | 空间ID。 |
| fileId | String | 文件ID。 |
| fileName | String | 文件名称。 |
| fileSize | long | 文件大小，字节数。 |
| fileType | String | 文件扩展名。 |
