---
title: "上传附件到钉盘/从钉盘选择文件"
source_url: "https://open.dingtalk.com/document/development/upload-attachment-to-nail-plate-select-file-from-nail-plate-h5"
namespace: "development"
slug: "upload-attachment-to-nail-plate-select-file-from-nail-plate-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 上传附件到钉盘/从钉盘选择文件"
doc_id: "1SWGgaIqXD"
updated_at: "2025-09-17 20:56:49"
---

> Source: https://open.dingtalk.com/document/development/upload-attachment-to-nail-plate-select-file-from-nail-plate-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 上传附件到钉盘/从钉盘选择文件
> Updated: 2025-09-17 20:56:49

# 上传附件到钉盘/从钉盘选择文件

调用**biz.util.uploadAttachment**上传附件到钉盘、从钉盘选择文件。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.uploadAttachment)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

该接口支持照片、拍照、本地系统文件和从已有钉盘文件选择，返回值为文件在钉盘系统内的数据信息，如**SpaceID**、**FileID**等。其中照片、拍照和本地系统文件将先上传到参数**SpaceID**指定的钉盘空间再返回，上传过程对开发者透明。

> **[!NOTE]**
>
> **使用场景说明：**
>
> 1. 存储空间：调用该jsapi前需要先创建存储空间并授予当前用户对该空间的上传操作权限，请参考[添加空间](https://open.dingtalk.com/document/orgapp/add-space)和[添加权限](https://open.dingtalk.com/document/orgapp/add-storage-permissions)。
> 2. 自定义空间：调用该jsapi前需先获取企业自定义空间并授予当前用户对该空间的上传操作权限，请参考[获取企业下的自定义空间](https://open.dingtalk.com/document/orgapp/obtain-user-space-under-the-enterprise)和[添加自定义空间权限](https://open.dingtalk.com/document/orgapp/add-custom-workspace-permissions)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持 | 支持 | 支持 |

```
dd.biz.util.uploadAttachment({
    image:{multiple:true,compress:false,max:9,spaceId: "12345",folderId:"123"},
    space:{corpId:"xxx3020",spaceId:"12345",folderId:"123",isCopy:1 , max:9},
    file:{spaceId:"12345",folderId:"123",max:1},
    types:["photo","camera","file","space"],//PC端支持["photo","file","space"]
    onSuccess : function(result) {
         //onSuccess将在文件上传成功之后调用
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
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| types | Array[String] | 支持上传附件的文件类型，至少一个。   - **photo**: 相册 - **camera**: 摄像头 - **file**: android是“本地文件”， iOS表示从“文件”上传 - **space**: 钉盘   **[!NOTE]**   - **Android&iOS端**：最多支持四种类型["photo","camera","file","space"] - **PC端**：最多支持["photo","file","space"] |
| image | JsonObject | types这个数组里有photo、camera参数需要构建这个数据。 |
| compress | Boolean | 是否压缩，默认为**true**。 |
| multiple | Boolean | 是否多选，默认为**false**。 |
| max | Int | 最多选择的图片数目，最多支持9张。 |
| isCopy | Int | - **Android&iOS端**：    - **1：**表示复制到钉盘   - **0：**表示返回选中的文件信息 - **PC端**：不支持此参数 |
| spaceId | String | 企业自定义空间或存储空间。 |
| folderId | String | 文件夹ID。  **[!NOTE]**   - 自定义空间和存储空间可调用[添加文件夹](https://open.dingtalk.com/document/orgapp/add-folder)接口，实现在空间内添加文件夹。 - 该参数只支持Android和IOS端。 |
| space | JsonObject | types这个数组里有space参数需要构建这个数据。 |
| file | JsonObject | types这个数组里有file参数需要构建这个数据。 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| type | String | 支持上传附件的类型，目前有photo、camera、file、space。 |
| data | Array[Object] | 文件上传成功后的数据信息。 |
| spaceId | String | 目标空间id。 |
| fileId | String | 文件id。 |
| fileName | String | 文件名称。 |
| fileType | String | 文件类型。 |
| fileSize | Long | 文件大小。 |
