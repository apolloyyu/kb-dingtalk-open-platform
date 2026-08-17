---
title: "预览钉盘文件"
source_url: "https://open.dingtalk.com/document/development/preview-nail-plate-file"
namespace: "development"
slug: "preview-nail-plate-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 预览钉盘文件"
doc_id: "OzRN0MlqOR"
updated_at: "2025-09-17 20:56:50"
---

> Source: https://open.dingtalk.com/document/development/preview-nail-plate-file
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 预览钉盘文件
> Updated: 2025-09-17 20:56:50

# 预览钉盘文件

调用**biz.cspace.preview**预览钉盘文件。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.cspace.preview)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

> **[!NOTE]**
>
> 在调用本接口预览钉盘文件之前，你需要先调用[授权预览审批附件](https://open.dingtalk.com/document/orgapp/preview-authorization-attachment-pop)或[授权用户访问企业的自定义空间](https://open.dingtalk.com/document/orgapp/authorize-a-user-to-access-a-custom-workspace-of-an)进行授权。

| **客户端** | 是否需要鉴权 | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持 | 支持 | 支持 |

```
dd.biz.cspace.preview({
    corpId: "dingf8b3xxxxx",
    spaceId: "13557022",
    fileId: "11452819",
    fileName: "钉盘快速入门",
    fileSize: 1024,
    fileType: "pdf",
    onSuccess : function(res) {

    },
    onFail : function(err) {
   
   }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 用户当前所在企业corpId，此文件预览成功后只能转发或保存到此corpId对应的企业群和个人。 |
| spaceId | String | 空间ID。 |
| fileId | String | 文件ID。 |
| fileName | String | 文件名称。 |
| fileSize | long | 文件大小，字节数。 |
| fileType | String | 文件扩展名。 |
