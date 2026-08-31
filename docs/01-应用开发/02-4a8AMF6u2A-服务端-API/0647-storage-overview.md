---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/storage-overview"
namespace: "development"
slug: "storage-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 概述"
doc_id: "4oIFepqCbm"
updated_at: "2026-05-15 18:19:58"
---

> Source: https://open.dingtalk.com/document/development/storage-overview
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 概述
> Updated: 2026-05-15 18:19:58

# 概述

本文介绍了什么是存储，存储接口能力以及资源等内容。

## 什么是存储

存储API提供智能安全的企业数据管理方案，可以满足围绕文件存储的办公场景协作所需，主要能力包括但并不限于文件的上传、下载、管理、流转，主流文件在线预览和编辑能力，权限管理等。可以使用存储API实现从简单的应用附件到复杂的云盘类产品的功能需要。

当你的应用使用存储API后，可以实现：

- 可以和钉钉其他应用中的文件高效流转。
- 可以满足企业管理员的文件管控需要，详情请参见[钉钉管理后台](https://oa.dingtalk.com/dingtalk-enterprise-storage.htm#/)。

## 开放概览

存储提供了丰富的接口开放能力，开发者通过API接口可以实现存储和企业业务系统打通。

### **企业管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取企业信息](0650-obtain-enterprise-storage-related-information.md) | 获取企业存储的相关信息。 | 新版 |

### **应用**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [获取群存储空间信息](0640-obtain-group-storage-space-information.md) | 获取群存储空间信息。 | 新版 |
| [以应用身份发送文件给指定用户](0641-sends-a-storage-file-to-a-specified-user.md) | 以应用身份发送文件给指定用户。 | 新版 |
| [发送文件到指定会话](0642-send-file-to-specified-session.md) | 发送文件到指定会话。 | 新版 |
| [发送文件链接到指定会话](0643-send-a-file-link-to-the-specified-session.md) | 发送文件链接到指定会话。 | 新版 |
| [获取应用信息](0651-obtains-the-information-about-the-current-application.md) | 获取应用信息。 | 新版 |

### **空间管理**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [添加空间](0652-add-space.md) | 在企业存储内添加新空间。 | 新版 |
| [获取空间信息](0653-get-space-information.md) | 获取存储空间的信息。 | 新版 |

### **文件管理**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [添加文件夹](0654-add-folder.md) | 在存储空间内添加文件夹。 | 新版 |
| [复制文件或文件夹](0655-copy-an-object.md) | 复制文件或文件夹。 | 新版 |
| [批量复制文件或文件夹](0656-copy-files-or-folders-in-bulk.md) | 批量复制文件或文件夹。 | 新版 |
| [移动文件或文件夹](0657-move-a-file-or-folder.md) | 移动文件或文件夹的位置。 | 新版 |
| [批量移动文件或文件夹](0658-bulk-move-files-or-folders.md) | 批量移动文件或文件夹。 | 新版 |
| [重命名文件或文件夹](0659-rename-a-file-or-folder.md) | 重命名文件或文件夹。 | 新版 |
| [删除文件或文件夹](0660-delete-a-file-or-folder.md) | 删除文件或文件夹。 | 新版 |
| [批量删除文件或文件夹](0661-delete-files-or-folders-in-bulk.md) | 批量删除文件或文件夹。 | 新版 |
| [恢复文件历史版本](0662-restore-previous-versions-of-files.md) | 恢复文件历史版本。 | 新版 |
| [获取文件版本列表](0663-obtains-a-list-of-file-versions.md) | 获取文件版本列表。 | 新版 |
| [获取文件或文件夹信息](0664-obtain-file-or-folder-information.md) | 获取文件或文件夹信息。 | 新版 |
| [批量获取文件或文件夹信息](0665-get-file-or-folder-information-in-bulk.md) | 批量获取文件或文件夹信息。 | 新版 |
| [获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md) | 获取空间内的文件或文件夹列表。 | 新版 |
| [获取空间下所有文件或文件夹列表](0667-get-a-list-of-all-files-or-folders-under-a.md) | 平铺获取空间下所有文件或文件夹列表。 | 新版 |
| [获取文件预览或编辑信息](0670-obtains-the-object-preview-or-editing-information.md) | 获取文件预览或编辑的链接。 | 新版 |
| [更新文件或文件夹的应用属性](0668-update-file-application-properties.md) | 更新文件或文件夹的应用属性。 | 新版 |
| [删除文件或文件夹的应用属性](0669-delete-file-app-attribute.md) | 删除文件或文件夹的应用属性。 | 新版 |
| [批量获取文件缩略图](0671-get-file-thumbnails-in-bulk.md) | 批量获取文件的缩略图信息。 | 新版 |

### **文件传输**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [获取文件上传信息](0674-obtain-file-upload-informations.md) | 获取文件上传信息。 | 新版 |
| [提交文件](0675-submittal-file.md) | 提交文件完成文件上传。 | 新版 |
| [初始化文件分片上传](0676-initialize-a-multipart-upload-object.md) | 初始化文件分片上传。 | 新版 |
| [获取文件分片上传信息](0677-obtains-the-information-about-multipart-uploads-of-an-object.md) | 获取文件分片后每片文件的上传信息。 | 新版 |
| [获取文件下载信息](0678-obtains-the-download-information-about-a-file.md) | 获取存储空间内文件的下载信息。 | 新版 |

### **权限管理**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [添加权限](0681-add-permissions-file.md) | 添加存储空间的权限。 | 新版 |
| [删除权限](0682-delete-permissions-file.md) | 删除存储空间的权限。 | 新版 |
| [修改权限](0683-modify-permissions-file.md) | 修改存储空间的权限。 | 新版 |
| [获取权限列表](0684-get-permission-list.md) | 获取存储空间的权限列表。 | 新版 |
| [设置权限继承模式](0685-set-permission-inheritance-mode.md) | 根据文件uuid、操作者unonId和权限继承模式inheritance，设置权限的继承模式。 | 新版 |
| [获取权限继承模式](0686-get-permission-inheritance-mode.md) | 根据文件uuid和操作者unionId，获取权限继承模式信息。 | 新版 |

### **回收站管理**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [获取回收站信息](0687-obtain-information-about-the-recycle-bin.md) | 获取回收站信息。 | 新版 |
| [获取回收项列表](0688-gets-the-list-of-recycle-items.md) | 获取回收站内的回收项信息列表。 | 新版 |
| [获取回收项信息](0689-obtain-recycling-item-information.md) | 获取回收项信息。 | 新版 |
| [还原回收项](0690-restore-recycle-items.md) | 还原回收项。 | 新版 |
| [批量还原回收项](0691-batch-restore-recycled-items.md) | 批量还原回收项。 | 新版 |
| [删除回收项](0692-delete-recycle-item.md) | 删除回收站内的某个回收项。 | 新版 |
| [批量删除回收项](0693-batch-delete-recycle-items.md) | 批量删除回收站内的回收项。 | 新版 |
| [清空回收站](0694-empty-the-recycle-bin.md) | 根据回收站Id清空回收站。 | 新版 |

### **任务管理**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [获取存储中异步任务信息](0695-get-the-asynchronous-task-information-in-storage.md) | 获取存储中异步任务信息。 | 新版 |

### **事件订阅**

| **API版本** | **API版本** | **API版本** |
| --- | --- | --- |
| [订阅文件变更事件](0696-subscribe-to-file-change-events.md) | 订阅存储文件变更事件。 | 新版 |
| [取消订阅文件变更事件](0697-unsubscribe-from-file-change-events.md) | 取消订阅存储文件变更事件。 | 新版 |

## **使用教程**

钉钉提供了存储接口接入流程示例。

| **教程名称** | **功能介绍** | **教学范围** | **Demo 下载** |
| --- | --- | --- | --- |
| [钉盘文件的上传、预览和下载](0648-dingpan-document.md) | 钉盘文件的上传、下载、预览 | 所有钉钉开发者 | [file-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250807/zkuhco/file-demo.zip?spm=ding_open_doc.document.0.0.244b769bqOAIbj&file=file-demo.zip) |
| [上传本地文件到钉钉文档（我的文档）](0649-upload-files-dingtalk-documents-documents.md) | 将本地文件上传到钉钉文档（我的文档）目录下 | 所有钉钉开发者 | [doc-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250704/bpihcw/doc-demo.zip?spm=ding_open_doc.document.0.0.244b769bqOAIbj&file=doc-demo.zip) |

## 资源说明

- **空间**资源主要包含以下属性：

  | 属性 | 类型 | 说明 |
  | --- | --- | --- |
  | spaceId | string | 空间Id。 |
  | spaceName | string | 空间名称。 |
  | spaceType | string | 空间类型。  - **USER**：用户空间 - **APP**：应用空间 |
  | quota | int64 | 空间总容量。  **[!NOTE]**  -1表示该空间额度无限制，如果有企业属性，不能超过企业空间额度。 |
  | usedQuota | int64 | 空间已使用容量。 |
  | createTime | string (iso8601) | 创建时间。 |
  | modifyTime | string (iso8601) | 修改时间。 |
- **文件和文件夹**资源主要包含以下属性：

  | 属性 | 类型 | 类型 |
  | --- | --- | --- |
  | id | string | 文件或文件夹的id。 |
  | spaceId | string | 空间Id。 |
  | path | string | 文件或文件夹在空间内的路径。 |
  | status | string | 状态。  - **NORMAL**：正常 - **DELETED**：已删除 - **EXPIRED**：已过期 |
  | partitionType | string | 存储分区。  - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属MiniOSS存储分区 |
  | parentId | string | 文件目录Id。 |
  | fileType | string | 文件类型。  - **FILE**：文件 - **FOLDER**：文件夹 |
  | extension | string | 文件后缀名。 |
- **权限**主要包含以下属性：

  | 属性 | 类型 | 说明 |
  | --- | --- | --- |
  | id | string | 权限成员id。  - 如果type参数值为**ORG**，该参数值传企业**corpId**。 - 如果type参数值为**DEPT**，该参数值传部门**deptId**，调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 - 如果type参数值为**TAG**，该参数值传**tag名称**。 - 如果type参数值为**CONVERSATION**，该参数值传会话**openConversationId**，通过[创建群会话](1483-session-management-creates-groups.md)接口或[创建场景群](1486-create-a-scene-group-v2.md)接口获取。 - 如果type参数值为**USER**，该参数传用户**unionId**，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
  | roleId | string | 权限角色Id。  - **OWNER**：拥有者 - **MANAGER**：管理者 - **EDITOR**：编辑者 - **DOWNLOADER**：下载者 - **READER**：查看者 |
  | type | string | 权限成员类型：  - **ORG**：企业 - **DEPT**：部门 - **TAG**：自定义tag - **CONVERSATION**：会话 - **USER**：用户 |
  | duration | string | 授权有效时长，单位秒，默认值为-1，表示永久有效。  - 被添加权限的空间类型是APP时，授权有效时长生效。 - 被添加权限的空间类型是USER时，授权有效时长无效，默认为永久有效。 |
