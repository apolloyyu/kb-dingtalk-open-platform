---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/knowledge-base-overview"
namespace: "development"
slug: "knowledge-base-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 概述"
doc_id: "YDeCgTaTTZ"
updated_at: "2026-05-15 18:17:43"
---

> Source: https://open.dingtalk.com/document/development/knowledge-base-overview
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 概述
> Updated: 2026-05-15 18:17:43

# 概述

本文档介绍了知识库产品，什么是知识库，知识库开放了哪些接口能力。

## **什么是知识库**

知识库是钉钉内专业高效的企业知识管理平台，可用于搭建企业知识管理库和企业内部的文档协同。操作简单便捷，管理员添加成员后即可多人共享，实时同步，知识库成员可以在其中记录内部协作产出的所有内容。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/dozoMnmmZf2xrzAW/5ea509f6d8f04819ad72ab2dac3614c80521.gif)

## **功能介绍**

### **文档管理**

知识库中, 可以使用文件夹对文档做归类。每个知识库都可以在一个目录树中呈现所有的文档。也可以在目录树上新增文档或者文件夹。![知识库](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7026493761/p551634.png)

也可以通过脑图视图的形式结构化呈现知识库下的所有文档内容，在知识库首页就可以直接在脑图上拖拽，快速高效完成文档结构的调整。

![](https://alidocs.oss-accelerate.aliyuncs.com/a/RlVejGnjwcVJ75YA/de44552457c64966b3ce904036dd21970521.gif?preview-key=132)

### **权限管理**

知识库支持多级权限设置, 包含知识库级别、文件夹级别和单文档级别。

权限类型有: 可管理、可编辑、可查看/下载、仅可查看。

用户可以通过添加、修改、移除权限来实现对人、部门、群、组织等的权限控制。

![权限](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6026493761/p551640.png)

## **开放概览**

### **开放接口列表**

知识库提供了丰富的接口开放能力，开发者通过API接口可以实现钉使用知识库功能。

#### **知识库管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新建知识库](0557-new-knowledge-base.md) | 创建组织下的知识库。 | 新版 |
| [获取知识库](0558-obtain-the-knowledge-base.md) | 查询知识库信息。 | 新版 |
| [置顶知识库](0559-api-pinspace.md) | 根据知识库 ID 和 操作者 UnionID，将对应知识库置顶。 | 新版 |
| [获取知识库列表](0560-get-knowledge-base-list.md) | 根据操作人unionId，获取知识库列表信息。 | 新版 |
| [批量获取知识库](0561-batch-acquisition-of-knowledge-base.md) | 根据操作人unionId和知识库ID，查询知识库信息。 | 新版 |
| [知识库转交所有者](0562-api-handoveryworkspace.md) | 将知识库所有者转交给他人。 | 新版 |
| [获取我的文档知识库信息](0563-get-my-documents.md) | 根据操作人unionId，获取操作人的文档信息。 | 新版 |

#### **目录树管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [复制文档](0564-api-copydoc.md) | 将节点复制到其他节点下。 | 新版 |
| [创建快捷方式](0565-api-createshortcut.md) | 创建知识库或文件的快捷方式。。 | 新版 |
| [获取任务状态](0566-api-gettaskinfo.md) | 通过Task查询任务状态，可与复制文档结合使用。 | 新版 |
| [创建知识库文档](0567-create-team-space-document.md) | 在知识库内创建文档或者文件夹。 | 新版 |
| [删除知识库文档](0568-delete-team-space-documents.md) | 删除团队空间文档或者文件夹。 | 新版 |
| [知识库下载文件](0569-knowledge-base-download-file.md) | 获取知识库中文件的下载信息。 | 新版 |
| [获取节点](0570-get-knowledge-base-acquisition-node.md) | 根据操作者unionId和节点id，获取单个节点信息。 | 新版 |
| [获取节点列表](0571-get-node-list.md) | 根据父节点ID，查询父节点下的节点列表。 | 新版 |
| [通过链接获取节点](0572-get-node-by-link.md) | 根据操作者unionId和文档链接，获取节点信息。 | 新版 |
| [批量获取节点](0573-obtain-nodes-in-batch.md) | 根据节点id和操作人unionId信息，批量查询节点信息。 | 新版 |

### **回调事件列表**

知识库支持创建小组、小组变更、小组成员变更等多种回调事件：

- [文档知识库中创建小组](../04-LFcRvVD08N-事件订阅/0010-event-doc-spaces-create-team.md)
- [文档知识库中小组变更](../04-LFcRvVD08N-事件订阅/0011-event-doc-spaces-team-change.md)
- [文档知识库中小组成员变更](../04-LFcRvVD08N-事件订阅/0012-event-doc-spaces-team-member-change.md)

## **使用教程**

钉钉提供了知识库接口接入流程示例。

- [知识库上传文件](0554-upload-files-to-the-knowledge-base.md)
- [知识库成员管理](0556-knowledge-base-member-management.md)
- [知识库权限变更](0555-change-of-knowledge-base-access-rights.md)

## **名词解释**

### **目录树**

指的是知识库目录结构形成的一棵树。

### **节点**

指的是知识库目录树上的节点, 包含文件夹和文件两种。

### **权限**

- 可以利用权限来安全管理团队组织内部文档。
- 默认继承上一级文档/文件夹权限, 提升赋权效率。
- 支持权限+/-, 提升团队信息安全管理。
