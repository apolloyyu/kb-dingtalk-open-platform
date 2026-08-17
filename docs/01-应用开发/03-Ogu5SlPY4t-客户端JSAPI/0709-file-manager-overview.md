---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/file-manager-overview"
namespace: "development"
slug: "file-manager-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 文件管理器 > 概述"
doc_id: "bZ8jLTrfWU"
updated_at: "2025-09-17 21:00:55"
---

> Source: https://open.dingtalk.com/document/development/file-manager-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 文件管理器 > 概述
> Updated: 2025-09-17 21:00:55

# 概述

本文介绍了什么是文件管理器，文件管理器可用功能概览以及文件管理器相关概念。

## **什么是文件管理器**

钉钉小程序提供了一套小程序代码包文件和用户本地文件的文件存储管理接口，即FileSystemManager文件管理器，它可以通过dd.getFileSystemManager获取，再通过调用FileSystemManager管理所有文件系统。

## **文件管理器可用功能概览**

通过全局唯一的文件系统管理器（FileSystemManager），可以对所有文件系统进行管理操作。

| **名称** | **功能说明** |
| --- | --- |
| [创建本地用户目录](https://open.dingtalk.com/document/orgapp/creat-folder) | 调用**FileSystemManager.mkdir**，创建本地用户目录。 |
| [判断文件或目录是否存在](https://open.dingtalk.com/document/orgapp/determine-whether-a-file-or-directory-exists) | 调用**FileSystemManager.access**，判断文件或者目录是否存在。 |
| [保存文件](https://open.dingtalk.com/document/orgapp/save-file) | 调用**FileSystemManager.saveFile**，将本地临时文件保存为本地缓存文件或本地用户文件。 |
| [获取文件信息](https://open.dingtalk.com/document/orgapp/get-file-information) | 调用**FileSystemManager.getFileInfo**，获取本地临时文件、本地缓存文件和本地用户文件的信息。 |
| [获取本地用户文件和目录列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-local-user-files) | 调用**FileSystemManager.readdir**，获取本地用户文件列表。 |
| [获取文件或目录的status对象](https://open.dingtalk.com/document/orgapp/obtain-the-file-status-object) | 调用**FileSystemManager.stat**，获取文件或目录的status对象。 |
| [获取本地缓存文件列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-local-cached-files) | 调用**FileSystemManager.getSavedFileList**，获取本地缓存文件列表。 |
| [读取本地用户文件内容](https://open.dingtalk.com/document/orgapp/read-local-user-file) | 调用**FileSystemManager.readFile**，读取本地用户文件的内容。 |
| [删除本地用户文件目录](https://open.dingtalk.com/document/orgapp/delete-local-user-file-directory) | 调用**FileSystemManager.rmdir**，删除本地用户文件目录。 |
| [删除本地用户文件](https://open.dingtalk.com/document/orgapp/delete-objects-local) | 调用**FileSystemManager.unlink**，删除本地用户文件。 |
| [删除本地缓存文件](https://open.dingtalk.com/document/orgapp/delete-local-cache-files) | 调用**FileSystemManager.removeSavedFile**，删除本地缓存文件。 |
| [复制文件保存到本地用户目录内](https://open.dingtalk.com/document/orgapp/copy-the-file-to-the-local-user-directory) | 调用**FileSystemManager.copyFile**，复制文件保存到本地用户目录。 |
| [重命名并移动本地用户文件或目录](https://open.dingtalk.com/document/orgapp/rename-and-move-local-user-files-or-directories) | 调用**FileSystemManager.rename**，重命名本地用户文件或目录的名称并且可以移动到新目录下。 |
| [向本地用户目录写入文件](https://open.dingtalk.com/document/orgapp/write-file-to-local-user-directory) | 调用**FileSystemManager.writeFile**，向本地用户目录内写入文件。 |
| [向本地用户文件末尾添加内容](https://open.dingtalk.com/document/orgapp/append-content-to-the-end-of-the-local-user-file) | 调用**FileSystemManager.appendFile**，向本地用户文件末尾添加内容。 |
| [解压本地用户文件](https://open.dingtalk.com/document/orgapp/unzip-local-user-files) | 调用**FileSystemManager.unzip**，解压本地用户文件。 |

## **名词解释**

### **本地文件**

本地文件是指小程序被用户添加到手机后，以用户维度隔离，有一块独立的文件存储区域。即同一台手机，仅支持每个手机用户访问自己登录账号下的文件，不支持访问其它登录用户的文件，同一个用户不同小程序之间的文件也不能互相访问。
本地文件的文件路径格式为`{{协议名}}://文件路径`，其中协议名通常为https，但开发者无需关注此点，也不需在代码中体现完整文件路径。

> **[!NOTE]**
>
> 为了安全考虑，本地文件是钉钉分配给用户的沙盒文件，和用户文件系统隔离，小程序开发者可以通过文件管理器的接口来访问，但用户无法在手机文件系统中直接访问。

**本地文件可分为本地临时文件、本地缓存文件和本地用户文件。**

#### **本地临时文件**

- 本地临时文件只能通过特定接口产生，不能直接写入内容。本地临时文件通过文件虚拟协议`https://resource`操作。
- 本地临时文件产生后，仅在当前生命周期内保证有效，重启之后不一定可用。并且一旦小程序被完全关闭就被清理，即下次冷启动小程序时不可继续使用。
- 如果需要保证在下次启动是无需下载，可通过[保存文件](https://open.dingtalk.com/document/orgapp/save-file)接口将本地临时文件转换为本地缓存文件或本地用户文件。
- 在下载临时文件时，可先通过[判断文件或目录是否存在](https://open.dingtalk.com/document/orgapp/determine-whether-a-file-or-directory-exists)接口检查文件是否存在，减少重复文件下载，提升用户体验。
- 支持产生本地临时文件的API有：

- [选择图片](https://open.dingtalk.com/document/orgapp/dd-chooseimage)，获取本地图片的本地临时文件。
- [选择视频](https://open.dingtalk.com/document/orgapp/dd-choosevideo)，获取本地视频的本地临时文件。
- [下载文件](https://open.dingtalk.com/document/orgapp/mini-program-download-objects)，获取公网服务资源的本地临时文件。

#### **本地缓存文件**

- 本地缓存文件只能通过调用特定接口产生，不能直接写入内容，本地缓存文件通过文件虚拟协议`https://resource`操作。
- 本地缓存文件产生后，重启小程序之后仍可用。
- 本地缓存文件只能通过[保存文件](https://open.dingtalk.com/document/orgapp/save-file)（不指定filePath）接口将本地临时文件保存获取。
- 单个本地缓存文件最大限制是10MB。
- 本地缓存文件和本地用户文件共计最多可存储50MB文件，若超出该大小，可通过[删除本地缓存文件](https://open.dingtalk.com/document/orgapp/delete-local-cache-files)接口删除本地缓存文件。
- 支持产生本地缓存文件的API有：

- [保存文件](https://open.dingtalk.com/document/orgapp/save-file)（不传filePath），将本地临时文件保存为本地缓存文件。

#### **本地用户文件**

- 本地用户文件通过文件虚拟协议`https://usr`操作。
- 本地用户文件是指钉钉提供了一个用户文件目录给开发者，开发者对这个目录有完全自由的读写权限，通过`dd.env.USER_DATA_PATH`可以获取到这个目录的路径。
- 单个本地用户文件最大限制是10MB。
- 本地用户文件与本地缓存文件共计最多可存储50MB文件，若超过该大小，可通过[删除本地缓存文件](https://open.dingtalk.com/document/orgapp/delete-local-cache-files)接口删除本地缓存文件或[删除本地用户文件](https://open.dingtalk.com/document/orgapp/delete-objects-local)接口删除本地用户文件。
- 支持产生本地用户文件的API有：

- [保存文件](https://open.dingtalk.com/document/orgapp/save-file)（传filePath），将本地临时文件保存为本地用户文件。
- [复制文件保存到本地用户目录内](https://open.dingtalk.com/document/orgapp/copy-the-file-to-the-local-user-directory)，将本地临时文件、本地缓存文件和本地用户文件复制保存到本地用户目录内。
- [向本地用户目录写入文件](https://open.dingtalk.com/document/orgapp/write-file-to-local-user-directory)，向本地用户目录内写入文件。

#### **读写权限**

| **接口、组件** | **读权限** | **写权限** |
| --- | --- | --- |
| **本地临时文件** | 有 | 无 |
| **本地缓存文件** | 有 | 无 |
| **本地用户文件** | 有 | 有 |

### **清理策略**

小程序退出后，系统会检查该小程序的临时文件占用。如占用超过限制，临时文件会被优先删除，因此本地临时文件只能保证在小程序当前生命周期内可用，一旦小程序被关闭就可能被清理，下次冷启动不保证可用。
本地缓存文件和本地用户文件的清理时机，只有在代码包被清理的时候会被清理。如果本地缓存文件和本地用户文件占用达到限制，此时无法写入新文件，需要开发者手动清理。
