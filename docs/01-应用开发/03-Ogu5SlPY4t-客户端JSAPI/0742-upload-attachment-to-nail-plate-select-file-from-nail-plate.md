---
title: "上传附件到钉盘/从钉盘选择文件"
source_url: "https://open.dingtalk.com/document/development/upload-attachment-to-nail-plate-select-file-from-nail-plate"
namespace: "development"
slug: "upload-attachment-to-nail-plate-select-file-from-nail-plate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 上传附件到钉盘/从钉盘选择文件"
doc_id: "owULMnoShY"
updated_at: "2025-09-17 21:01:18"
---

> Source: https://open.dingtalk.com/document/development/upload-attachment-to-nail-plate-select-file-from-nail-plate
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 上传附件到钉盘/从钉盘选择文件
> Updated: 2025-09-17 21:01:18

# 上传附件到钉盘/从钉盘选择文件

调用**dd.uploadAttachmentToDingTalk**上传附件到钉盘，或从钉盘选择文件。

此接口支持照片、拍照、本地系统文件和从已有钉盘文件选择，返回值为文件在钉盘系统内的数据信息，如**spaceId**、**fileId**等。其中照片、拍照和本地系统文件将先上传到参数**spaceId**指定的钉盘空间再返回，上传过程对开发者透明。

根据上传钉盘空间的不同，调用本接口时注意：

- 如果上传时使用的**spaceId**是企业自定义钉盘空间，调用该jsapi之前，需要授予当前用户对该空间的上传操作权限。参见[获取企业下的自定义空间](https://open.dingtalk.com/document/orgapp/obtain-user-space-under-the-enterprise)和[授权用户访问企业的自定义空间](https://open.dingtalk.com/document/orgapp/authorize-a-user-to-access-a-custom-workspace-of-an)接口。
- 如果上传时使用的**spaceId**是审批附件钉盘空间，调用该jsapi之前，需要再次使用当前操作上传员工的userid调用一次获取审批钉盘空间接口，参见[获取审批钉盘空间信息](https://open.dingtalk.com/document/orgapp/obtains-the-information-about-approval-nail-disk)。

## 示例代码

```
dd.uploadAttachmentToDingTalk({
    image:{multiple:true,compress:false,max:9,spaceId: "12345"},
    space:{spaceId:"12345",isCopy:1 , max:9},
    file: {spaceId:"12345",max:1},
    types:["photo","camera","file","space"],//PC端仅支持["photo","file","space"]
    success: (res) => {
       /*
       {
          type:'', // 用户选择了哪种文件类型 ，image（图片）、file（手机文件）、space（钉盘文件）
          data: [
             {
               spaceId: "232323",
               fileId: "DzzzzzzNqZY",
               fileName: "审批流程.docx",
               fileSize: 1024,
               fileType: "docx"
            },
            {
               spaceId: "232323",
               fileId: "DzzzzzzNqZY",
               fileName: "审批流程1.pdf",
               fileSize: 1024,
               fileType: "pdf"
            },
            {
               spaceId: "232323",
               fileId: "DzzzzzzNqZY",
               fileName: "审批流程3.pptx",
               fileSize: 1024,
               fileType: "pptx"
             }
          ]
 
       }
        */
    },
    fail: (err) =>{
        dd.alert({
            content:JSON.stringify(err)
        })
    }
})
```

## 参数说明

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| types | String[] | 支持上传附件的文件类型，至少一个。   - **photo**: 相册 - **camera**: 摄像头 - **file**: android是“本地文件”， iOS表示从“文件”上传 - **space**: 钉盘   **[!NOTE]**   - **Android&iOS端**：最多支持四种类型["photo","camera","file","space"] - **PC端**：最多支持["photo","file","space"] |
| image | JsonObject | types这个数组里有photo、camera参数需要构建这个数据。 |
| compress | Boolean | 是否压缩。  **默认值**：true。 |
| multiple | Boolean | 是否多选。  **默认值**：false。 |
| max | Int | 最多选择的图片数目，最多支持9张。 |
| isCopy | Int | - **1**：复制 - **0**：不复制(**PC端不支持此参数**) |
| spaceId | String | 企业自定义空间。  **[!IMPORTANT]**  参数**spaceid**一定要传**String**格式，否则上传时会报错“操作的文件已删除/不存在”的错误。 |
| space | JsonObject | types这个数组里有space参数需要构建这个数据。 |
| space | JsonObject | types这个数组里有file参数需要构建这个数据。 |

## 返回结果

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| type | String | 支持上传附件的类型，目前有photo、camera、file、space。 |
| data | Object[] | 文件上传成功后的数据信息。 |
| spaceId | String | 目标空间id。 |
| fileId | String | 文件id。 |
| fileName | String | 文件名称。 |
| fileType | String | 文件类型。 |
| fileSize | Long | 文件大小。 |
