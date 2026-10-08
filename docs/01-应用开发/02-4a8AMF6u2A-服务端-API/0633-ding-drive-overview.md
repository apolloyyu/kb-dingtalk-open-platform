---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/ding-drive-overview"
namespace: "development"
slug: "ding-drive-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 云盘（原钉盘） > 概述"
doc_id: "fJ0ZjU0BPu"
updated_at: "2026-05-15 18:19:18"
---

> Source: https://open.dingtalk.com/document/development/ding-drive-overview
> Path: 应用开发 / 服务端 API / 文档/文件 > 云盘（原钉盘） > 概述
> Updated: 2026-05-15 18:19:18

# 概述

本文档主要介绍什么是云盘，云盘接口能力，以及如何接入云盘接口能力等。

> **[!IMPORTANT]**
>
> 为便于开发者接入，钉盘产品名称将于2022年2月14日更新为**云盘**，与钉钉产品名称保持一致。

## 什么是云盘

钉钉云盘是基于阿里云的企业盘，提供智能安全的企业数据管理方案。云盘是集文件存储、管理与多人协作于一体的文件管理平台。它支持在任何设备上随时随地一键存储、编辑、分享工作学习资料，文档协作更高效。

钉钉云盘由私人盘和企业盘组成，其中企业盘由三个文件夹组成：

1. 我的文件、团队文件。
2. 群文件。
3. 其他微应用存储，可在OA后台“云盘-容量管理-微应用”查看。

私人盘初始容量为2GB，企业盘初始容量为100GB。更多功能介绍，请参见[钉钉使用手册-云盘](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/6wPdlBDrQk4JYrl0vX2Y8XKx72oEGeL5)。

![bff674672d794be79571b911d1d502c80521](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9574484561/p448009.jpeg)

## 开放概览

云盘提供了丰富的接口开放能力，开发者通过API接口可以实现云盘和企业业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新建空间](0634-new-space.md) | 新建企业共享空间。 | 新版 |
| [删除空间](0635-delete-a-space.md) | 删除企业共享空间。 | 新版 |
| [获取空间列表](0636-queries-a-space-list.md) | 获取空间详情信息。 | 新版 |
| [根据spaceId获取指定空间信息](0637-retrieves-the-space-list-on-the-management-side.md) | 根据spaceId获取指定空间的信息。 | 新版 |

## 名词解释

### **spaceId**

钉盘以space作为文件存储容器，可类比电脑上的C盘、E盘等。例如在钉钉内，每一个群文件对应一个space，企业钉盘中的公共区、共享文件夹、我的文件等也分别对应一个space。

### **fileId**

文件在钉盘内的唯一性标识。

### **自定义空间**

针对企业或ISV的个性化需求，钉盘在企业下开辟了自定义空间来供企业或ISV使用。每个企业可以自定义若干存储空间，每个微应用可以使用一个自定义存储空间，该空间在钉钉客户端不可见，在电脑管理后台可以查看其占用企业空间的情况。

### **钉盘权限**

区别于普通文件存储，钉盘提供完善的权限管理服务，文件的上传、下载、查看等操作需要在权限允许的条件下执行。

### **存储服务器 & 钉盘服务器**

存储服务器提供文件的存储服务，存储服务器上以mediaId唯一标识文件。钉盘服务器提供文件的目录关系、权限管理等服务。钉盘系统以fileId唯一标识文件，存储服务器内文件可添加到钉盘文件系统。

### **企业空间容量**

钉盘存储空间属于有限资源，超出部分需付费购买。钉盘为企业免费提供100G空间，微应用使用的自定义空间将占用企业空间。
