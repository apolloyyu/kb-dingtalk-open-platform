---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/dingtalk-document-overview"
namespace: "development"
slug: "dingtalk-document-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 概述"
doc_id: "1wIYBdj3mq"
updated_at: "2026-11-11 17:26:31"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-document-overview
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 概述
> Updated: 2026-11-11 17:26:31

# 概述

钉钉文档 OpenAPI 提供了一套 RESTful 风格的接口，允许开发者通过程序化方式操作钉钉文档。你可以使用这些接口实现文档内容的自动化读写、块元素的增删改查、内容批量操作等功能，适用于文档自动生成、内容同步、智能写作等场景。

## **钉钉文档**

### **介绍**

钉钉文档是阿里巴巴集团钉钉自主研发的企业协同办公套件，其包含文档、表格、脑图等在线创作工具。在日常使用中，无需下载文档即可通过电脑、手机或平板直接编辑和查看文档内容，文档内容实时自动保存。

同时，钉钉文档与钉钉深度整合，可基于组织关系与同事高效协作。使用钉钉文档还可以用于信息收集、项目管理、会议、业务汇报和新人入职等日常工作场景。更多功能介绍，请参见[钉钉使用手册-钉钉文档](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/od245kZmnOeW4D4L73YEWYbzxL6R0wMQ)。

![钉钉文档](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3518304361/p338100.png)

### **开放概览**

#### **开放接口列表**

文档提供了丰富的接口开放能力，开发者通过API接口可以实现文档的基础操作。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [覆写文档（个人授权）](0579-api-docupdatecontent.md) | 以 Markdown 格式覆写整篇文档内容。  **[!NOTE]**  该方式需要用户授权后，才能调用该接口。 | 新版 |
| [覆写文档（应用授权）](0580-api-doc-updatecontent.md) | 以 Markdown 格式覆写整篇文档内容。  **[!NOTE]**  该方式通过应用凭证appKey、appSecret获取accessToken后即可调用。 | 新版 |
| [获取资源上传信息](0581-api-getresourceuploadinfo.md) | 查询文档指定资源的上传地址。 | 新版 |
| [插入内容](0582-api-insertcontent.md) | 在文档指定位置插入一段 Markdown 内容。 | 新版 |
| [查询块元素](0583-api-docblocksquery.md) | 查询文档根节点下的一级块元素列表。 | 新版 |
| [插入块元素](0584-api-docinsertblocks.md) | 在文档指定位置插入 1 个块元素。 | 新版 |
| [更新块元素](0585-api-docblocksmodify.md) | 更新文档中任意 1 个块元素的内容或属性。 | 新版 |
| [删除块元素](0586-api-docdeleteblock.md) | 删除文档中 1 个特定的块元素。 | 新版 |
| [在段落末尾追加文本](0587-api-docappendtext.md) | 向指定段落末尾追加一段文本。 | 新版 |
| [在段落末尾追加行内元素](0588-api-docappendparagraph.md) | 在指定段落末尾追加一个行内元素。 | 新版 |

#### **回调事件列表**

[文档导出任务完成事件](../04-LFcRvVD08N-事件订阅/0013-events-doc-export-completed.md#undefined)

### **名词解释**

在使用钉钉文档 OpenAPI 之前，需要了解以下核心概念：

- **dentryUuid**

  文档的唯一标识。以`https://alidocs.dingtalk.com/i/nodes/Z90D4da-id`为例，`dentryUuid`就是`Z90D4da-id`。
- **blockId**

  块元素的唯一标识，可通过「查询块元素」接口获取。
- **operatorId**

  操作人的`unionId`，用于标识执行操作的用户身份和权限校验。
- **BlockElement**

  块元素，是文档内容的基本组成单位，如段落、标题、高亮块、表格等。
- **InlineElement**

  行内元素，嵌套在块元素内部，如贴纸、图片、链接、插槽等。

## **表格**

### **开放概览**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| **工作表** | | |
| [创建工作表](0591-create-a-worksheet.md) | 在表格文档中创建一个新的工作表。 | 新版 |
| [删除工作表](0593-delete-classic-workbooks.md) | 删除表格内的某个工作表。 | 新版 |
| [获取工作表](0594-obtain-worksheet-properties.md) | 获取某个工作表属性。 | 新版 |
| [更新工作表](0592-update-worksheet.md) | 修改钉钉表格中指定工作表的元属性。 | 新版 |
| [获取所有工作表](0595-obtain-all-worksheets.md) | 获取指定表格中所有的工作表信息。 | 新版 |
| **行列** | | |
| [删除行](0596-delete-row.md) | 删除指定的行。 | 新版 |
| [删除列](0597-delete-column.md) | 删除指定的列。 | 新版 |
| [设置自动行高](0598-set-row-height-automatically.md) | 可根据指定的字体大小自动调整钉钉表格中指定行的行高，使内容完整显示。 | 新版 |
| [批量设置列宽](0599-api-setcolumnswidth.md) | 一次性设置钉钉表格中从指定列开始的连续多列的宽度。 | 新版 |
| [批量设置行高](0600-api-setrowsheight.md) | 一次性设置钉钉表格中从指定行开始的连续多行的高度。 | 新版 |
| [工作表中追加行](0601-append-line.md) | 在工作表的已有数据末尾追加若干行数据。 | 新版 |
| [设置行隐藏或显示](0602-set-row-visibility.md) | 设置行隐藏或者正常显示。 | 新版 |
| [设置列隐藏或显示](0603-set-column-visibility.md) | 设置列隐藏或者正常显示。 | 新版 |
| [指定行上方插入若干行](0604-insert-rows-before-rows.md) | 在指定的行上方插入若干行。 | 新版 |
| [指定列左侧插入若干列](0605-insert-column-before-column.md) | 在指定列左侧插入若干列。 | 新版 |
| **单元格区域** | | |
| [合并单元格](0606-merge-cells.md) | 将钉钉表格中指定区域内的多个单元格合并为一个整体。 | 新版 |
| [插入下拉列表](0607-insert-drop-down-list.md) | 为钉钉表格中指定单元格区域设置下拉列表选项。 | 新版 |
| [删除下拉列表](0608-delete-drop-down-list.md) | 移除钉钉表格中指定单元格区域上已设置的下拉列表配置。 | 新版 |
| [获取单元格区域](0609-get-cell-properties.md) | 获取单元格属性。 | 新版 |
| [更新单元格区域](0610-update-cell-properties.md) | 更新单元格信息。 | 新版 |
| [查找工作表中的单元格](0611-find-the-next-eligible-cell.md) | 根据指定的条件查找匹配给定字符串的下一个单元格。 | 新版 |
| [查找所有符合条件的单元格](0612-find-all-matching-cells.md) | 在指定工作表中搜索包含目标文本的单元格，并返回匹配单元格的位置列表。 | 新版 |
| [清除单元格区域内数据](0613-clear-cell-data.md) | 清除单元格区域内数据，不包括格式。 | 新版 |
| [清除单元格区域内所有内容](0614-clear-all.md) | 清除单元格区域内所有内容，包括格式。 | 新版 |
| **条件格式** | | |
| [创建条件格式规则](0615-create-conditional-formatting-rules.md) | 在钉钉表格的指定工作表中创建条件格式规则。 | 新版 |
| **筛选** | | |
| [创建筛选](0616-api-createfilter.md) | 在钉钉表格的指定工作表上创建全局筛选，并指定筛选范围。 | 新版 |
| [更新筛选](0617-api-updatefilter.md) | 一次性批量更新全局筛选中多列的筛选条件。 | 新版 |
| [删除筛选](0618-api-deletefilter.md) | 删除指定工作表上的全局筛选，使所有因筛选条件被隐藏的行恢复显示。 | 新版 |
| [获取筛选](0619-api-getfilter.md) | 查询指定工作表上当前生效的全局筛选信息。 | 新版 |
| [筛选排序](0620-api-sortfilter.md) | 对全局筛选范围内的数据按指定列进行升序或降序排序。 | 新版 |
| [设置筛选条件](0621-api-setfiltercriteria.md) | 为全局筛选中的指定列设置或更新筛选条件。 | 新版 |
| [删除筛选条件](0622-api-clearfiltercriteria.md) | 清除全局筛选中指定列的筛选条件，使该列不再参与筛选计算。 | 新版 |
| **筛选试图** | | |
| [创建筛选视图](0623-api-createfilterview.md) | 在钉钉表格的指定工作表上创建筛选视图，并指定视图名称和筛选范围。 | 新版 |
| [更新筛选视图](0624-api-updatefilterview.md) | 更新指定筛选视图的名称、范围或筛选条件。 | 新版 |
| [删除筛选视图](0625-api-deletefilterview.md) | 删除指定工作表上的某个筛选视图及其所有筛选条件。 | 新版 |
| [获取筛选视图列表](0626-api-getfilterviews.md) | 获取指定工作表上所有筛选视图的列表。 | 新版 |
| [设置筛选视图条件](0627-api-setfilterviewcriteria.md) | 为指定筛选视图中的某一列设置或更新筛选条件。 | 新版 |
| [删除筛选视图条件](0628-api-clearfilterviewcriteria.md) | 清除指定筛选视图中某一列的筛选条件，使该列不再参与筛选计算。 | 新版 |
| **浮动图片** | | |
| [创建浮动图片](0629-api-createfloatimage.md) | 获取钉钉表格指定工作表中所有浮动图片的列表信息。 | 新版 |
| [更新浮动图片](0630-api-updatefloatimage.md) | 更新钉钉表格中已有浮动图片的属性。 | 新版 |
| [删除浮动图片](0631-api-deletefloatimage.md) | 删除钉钉表格指定工作表中的一张浮动图片。 | 新版 |

### **名词解释**

- **workbookId**

  表格文件的唯一标识。即知识库 API 返回的`nodeId`（`dentryUuid`），也可以从表格 URL 中获取。获取方式如下：

  - **方式一**：从表格 URL 中获取。

    ![从URL获取workbookId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2944684771/p1063487.png)
  - **方式二**：从文档信息中获取。

    ![从文档信息获取workbookId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2944684771/p1063490.png)
  - **方式三**：通过知识库 API 获取。

    调用[获取节点](0570-get-knowledge-base-acquisition-node.md)或[创建知识库文档](0567-create-team-space-document.md)接口，返回的`nodeId`（`dentryUuid`）即为`workbookId`。
- **sheetId**

  工作表的 ID 或名称。可通过[获取所有工作表](0595-obtain-all-worksheets.md)接口获取，也可以直接传工作表标题。
- **rangeAddress**

  单元格范围地址，使用 A1 表示法。
- **operatorId**

  操作人的`unionId`，用于标识执行操作的用户身份和权限校验。

## **云盘**

### **介绍**

> **[!IMPORTANT]**
>
> 为便于开发者接入，钉盘产品名称将于2022年2月14日更新为**云盘**，与钉钉产品名称保持一致。

钉钉云盘是基于阿里云的企业盘，提供智能安全的企业数据管理方案。云盘是集文件存储、管理与多人协作于一体的文件管理平台。它支持在任何设备上随时随地一键存储、编辑、分享工作学习资料，文档协作更高效。

钉钉云盘由私人盘和企业盘组成，其中企业盘由三个文件夹组成：

1. 我的文件、团队文件。
2. 群文件。
3. 其他微应用存储，可在OA后台“云盘-容量管理-微应用”查看。

私人盘初始容量为2GB，企业盘初始容量为100GB。更多功能介绍，请参见[钉钉使用手册-云盘](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/6wPdlBDrQk4JYrl0vX2Y8XKx72oEGeL5)。

![bff674672d794be79571b911d1d502c80521](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9574484561/p448009.jpeg)

### **开放概览**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新建空间](0634-new-space.md) | 新建企业共享空间。 | 新版 |
| [删除空间](0635-delete-a-space.md) | 删除企业共享空间。 | 新版 |
| [获取空间列表](0636-queries-a-space-list.md) | 获取空间详情信息。 | 新版 |
| [根据spaceId获取指定空间信息](0637-retrieves-the-space-list-on-the-management-side.md) | 根据spaceId获取指定空间的信息。 | 新版 |

### **名词解释**

- **spaceId**

  钉盘以space作为文件存储容器，可类比电脑上的C盘、E盘等。例如在钉钉内，每一个群文件对应一个space，企业钉盘中的公共区、共享文件夹、我的文件等也分别对应一个space。
- **fileId**

  文件在钉盘内的唯一性标识。
- **自定义空间**

  针对企业或ISV的个性化需求，钉盘在企业下开辟了自定义空间来供企业或ISV使用。每个企业可以自定义若干存储空间，每个微应用可以使用一个自定义存储空间，该空间在钉钉客户端不可见，在电脑管理后台可以查看其占用企业空间的情况。
- **钉盘权限**

  区别于普通文件存储，钉盘提供完善的权限管理服务，文件的上传、下载、查看等操作需要在权限允许的条件下执行。
- **存储服务器 & 钉盘服务器**

  存储服务器提供文件的存储服务，存储服务器上以mediaId唯一标识文件。钉盘服务器提供文件的目录关系、权限管理等服务。钉盘系统以fileId唯一标识文件，存储服务器内文件可添加到钉盘文件系统。
- **企业空间容量**

  钉盘存储空间属于有限资源，超出部分需付费购买。钉盘为企业免费提供100G空间，微应用使用的自定义空间将占用企业空间。

## **知识库**

### **介绍**

知识库是钉钉内专业高效的企业知识管理平台，可用于搭建企业知识管理库和企业内部的文档协同。操作简单便捷，管理员添加成员后即可多人共享，实时同步，知识库成员可以在其中记录内部协作产出的所有内容。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/dozoMnmmZf2xrzAW/5ea509f6d8f04819ad72ab2dac3614c80521.gif)

### **功能介绍**

- **文档管理**

  知识库中, 可以使用文件夹对文档做归类。每个知识库都可以在一个目录树中呈现所有的文档。也可以在目录树上新增文档或者文件夹。![知识库](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7026493761/p551634.png)

  也可以通过脑图视图的形式结构化呈现知识库下的所有文档内容，在知识库首页就可以直接在脑图上拖拽，快速高效完成文档结构的调整。

  ![](https://alidocs.oss-accelerate.aliyuncs.com/a/RlVejGnjwcVJ75YA/de44552457c64966b3ce904036dd21970521.gif?preview-key=132)
- **权限管理**

  知识库支持多级权限设置, 包含知识库级别、文件夹级别和单文档级别。

  权限类型有: 可管理、可编辑、可查看/下载、仅可查看。

  用户可以通过添加、修改、移除权限来实现对人、部门、群、组织等的权限控制。

  ![权限](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6026493761/p551640.png)

### **开放概览**

#### **开放接口列表**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新建知识库](0557-new-knowledge-base.md) | 创建组织下的知识库。 | 新版 |
| [获取知识库](0558-obtain-the-knowledge-base.md) | 查询知识库信息。 | 新版 |
| [置顶知识库](0559-api-pinspace.md) | 根据知识库 ID 和 操作者 UnionID，将对应知识库置顶。 | 新版 |
| [获取知识库列表](0560-get-knowledge-base-list.md) | 根据操作人unionId，获取知识库列表信息。 | 新版 |
| [批量获取知识库](0561-batch-acquisition-of-knowledge-base.md) | 根据操作人unionId和知识库ID，查询知识库信息。 | 新版 |
| [知识库转交所有者](0562-api-handoveryworkspace.md) | 将知识库所有者转交给他人。 | 新版 |
| [获取我的文档知识库信息](0563-get-my-documents.md) | 根据操作人unionId，获取操作人的文档信息。 | 新版 |
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

#### **回调事件列表**

知识库支持创建小组、小组变更、小组成员变更等多种回调事件：

- [文档知识库中创建小组](../04-LFcRvVD08N-事件订阅/0010-event-doc-spaces-create-team.md)
- [文档知识库中小组变更](../04-LFcRvVD08N-事件订阅/0011-event-doc-spaces-team-change.md)
- [文档知识库中小组成员变更](../04-LFcRvVD08N-事件订阅/0012-event-doc-spaces-team-member-change.md)

### **使用教程**

钉钉提供了知识库接口接入流程示例。

- [知识库上传文件](0554-upload-files-to-the-knowledge-base.md)
- [知识库成员管理](0556-knowledge-base-member-management.md)
- [知识库权限变更](0555-change-of-knowledge-base-access-rights.md)

### **集成方案**

企业若需要集成更多知识库相关能力，可参考下方内容进行接入：

- [项目文档管理：知识库文档沉淀与需求流程线上化](https://open.dingtalk.com/document/development/knowledge-document-requirement-process)

### **名词解释**

- **目录树**

  指的是知识库目录结构形成的一棵树。
- **节点**

  指的是知识库目录树上的节点, 包含文件夹和文件两种。
- **权限**

  - 可以利用权限来安全管理团队组织内部文档。
  - 默认继承上一级文档/文件夹权限, 提升赋权效率。
  - 支持权限+/-, 提升团队信息安全管理。

## **存储文件**

### **介绍**

存储API提供智能安全的企业数据管理方案，可以满足围绕文件存储的办公场景协作所需，主要能力包括但并不限于文件的上传、下载、管理、流转，主流文件在线预览和编辑能力，权限管理等。可以使用存储API实现从简单的应用附件到复杂的云盘类产品的功能需要。

当你的应用使用存储API后，可以实现：

- 可以和钉钉其他应用中的文件高效流转。
- 可以满足企业管理员的文件管控需要，详情请参见[钉钉管理后台](https://oa.dingtalk.com/dingtalk-enterprise-storage.htm#/)。

### **开放概览**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| **企业管理** | | |
| [获取企业信息](0650-obtain-enterprise-storage-related-information.md) | 获取企业存储的相关信息。 | 新版 |
| **应用** | | |
| [获取群存储空间信息](0640-obtain-group-storage-space-information.md) | 获取群存储空间信息。 | 新版 |
| [以应用身份发送文件给指定用户](0641-sends-a-storage-file-to-a-specified-user.md) | 以应用身份发送文件给指定用户。 | 新版 |
| [发送文件到指定会话](0642-send-file-to-specified-session.md) | 发送文件到指定会话。 | 新版 |
| [发送文件链接到指定会话](0643-send-a-file-link-to-the-specified-session.md) | 发送文件链接到指定会话。 | 新版 |
| [获取应用信息](0651-obtains-the-information-about-the-current-application.md) | 获取应用信息。 | 新版 |
| **空间管理** | | |
| [添加空间](0652-add-space.md) | 在企业存储内添加新空间。 | 新版 |
| [获取空间信息](0653-get-space-information.md) | 获取存储空间的信息。 | 新版 |
| **文件管理** | | |
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
| [获取 dentryUuid 信息](0672-api-getuuidbydentryid.md) | 根据文件的 spaceId 和 dentryId 获取文件的 dentryUuid 信息。 | 新版 |
| [根据 dentryUuid 获取 spaceId](0673-api-getdentryidbyuuid.md) | 根据文件 dentryUuid 获取当前文件的 spaceId 和 dentryId。 | 新版 |
| [根据文档id或URL获取文件DentryUuid](0674-api-getuuidbyidorurl.md) | 通过文档标识或URL查询节点dentryUuid。 | 新版 |
| **文件传输** | | |
| [获取文件上传信息](0675-obtain-file-upload-informations.md) | 获取文件上传信息。 | 新版 |
| [提交文件](0676-submittal-file.md) | 提交文件完成文件上传。 | 新版 |
| [初始化文件分片上传](0677-initialize-a-multipart-upload-object.md) | 初始化文件分片上传。 | 新版 |
| [获取文件分片上传信息](0678-obtains-the-information-about-multipart-uploads-of-an-object.md) | 获取文件分片后每片文件的上传信息。 | 新版 |
| [获取文件下载信息](0679-obtains-the-download-information-about-a-file.md) | 获取存储空间内文件的下载信息。 | 新版 |
| **权限管理** | | |
| [添加权限](0682-add-permissions-file.md) | 添加存储空间的权限。 | 新版 |
| [删除权限](0683-delete-permissions-file.md) | 删除存储空间的权限。 | 新版 |
| [修改权限](0684-modify-permissions-file.md) | 修改存储空间的权限。 | 新版 |
| [获取权限列表](0685-get-permission-list.md) | 获取存储空间的权限列表。 | 新版 |
| [设置权限继承模式](0686-set-permission-inheritance-mode.md) | 根据文件uuid、操作者unonId和权限继承模式inheritance，设置权限的继承模式。 | 新版 |
| [获取权限继承模式](0687-get-permission-inheritance-mode.md) | 根据文件uuid和操作者unionId，获取权限继承模式信息。 | 新版 |
| **回收站管理** | | |
| [获取回收站信息](0688-obtain-information-about-the-recycle-bin.md) | 获取回收站信息。 | 新版 |
| [获取回收项列表](0689-gets-the-list-of-recycle-items.md) | 获取回收站内的回收项信息列表。 | 新版 |
| [获取回收项信息](0690-obtain-recycling-item-information.md) | 获取回收项信息。 | 新版 |
| [还原回收项](0691-restore-recycle-items.md) | 还原回收项。 | 新版 |
| [批量还原回收项](0692-batch-restore-recycled-items.md) | 批量还原回收项。 | 新版 |
| [删除回收项](0693-delete-recycle-item.md) | 删除回收站内的某个回收项。 | 新版 |
| [批量删除回收项](0694-batch-delete-recycle-items.md) | 批量删除回收站内的回收项。 | 新版 |
| [清空回收站](0695-empty-the-recycle-bin.md) | 根据回收站Id清空回收站。 | 新版 |
| **任务管理** | | |
| [获取存储中异步任务信息](0696-get-the-asynchronous-task-information-in-storage.md) | 获取存储中异步任务信息。 | 新版 |
| **事件订阅** | | |
| [订阅文件变更事件](0697-subscribe-to-file-change-events.md) | 订阅存储文件变更事件。 | 新版 |
| [取消订阅文件变更事件](0698-unsubscribe-from-file-change-events.md) | 取消订阅存储文件变更事件。 | 新版 |

### **使用教程**

钉钉提供了存储接口接入流程示例。

- [钉盘文件的上传、预览和下载](0648-dingpan-document.md)：点击[file-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250807/zkuhco/file-demo.zip?spm=ding_open_doc.document.0.0.244b769bqOAIbj&file=file-demo.zip)下载Demo。
- [上传本地文件到钉钉文档（我的文档）](0649-upload-files-dingtalk-documents-documents.md)：点击[doc-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250704/bpihcw/doc-demo.zip?spm=ding_open_doc.document.0.0.244b769bqOAIbj&file=doc-demo.zip)下载Demo。

### **资源说明**

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
  | id | string | 权限成员id。  - 如果type参数值为**ORG**，该参数值传企业**corpId**。 - 如果type参数值为**DEPT**，该参数值传部门**deptId**，调用[获取部门列表](0081-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 - 如果type参数值为**TAG**，该参数值传**tag名称**。 - 如果type参数值为**CONVERSATION**，该参数值传会话**openConversationId**，通过[创建群会话](1482-session-management-creates-groups.md)接口或[创建场景群](1485-create-a-scene-group-v2.md)接口获取。 - 如果type参数值为**USER**，该参数传用户**unionId**，可调用[查询用户详情](0055-query-user-details.md)接口获取unionid参数值。 |
  | roleId | string | 权限角色Id。  - **OWNER**：拥有者 - **MANAGER**：管理者 - **EDITOR**：编辑者 - **DOWNLOADER**：下载者 - **READER**：查看者 |
  | type | string | 权限成员类型：  - **ORG**：企业 - **DEPT**：部门 - **TAG**：自定义tag - **CONVERSATION**：会话 - **USER**：用户 |
  | duration | string | 授权有效时长，单位秒，默认值为-1，表示永久有效。  - 被添加权限的空间类型是APP时，授权有效时长生效。 - 被添加权限的空间类型是USER时，授权有效时长无效，默认为永久有效。 |

## **媒体文件**

### **介绍**

媒体文件是钉钉提供的开放能力之一，可以在企业内部应用和第三方企业应用内的文件储存场景使用。

- **媒体文件位置说明**

  本功能媒体文件使用的空间是钉钉提供给组织的特定存储空间，不属于组织的钉盘空间，调用本功能接口上传文件，不占用钉钉组织的钉盘空间**。**
- **存储有效期说明**

  本功能文件的存储有效期无限制，通常钉钉组织没有解散，上传文件返回的media\_id可以一直使用。

### **开放概览**

| **API** | **说明** | **API版本** |
| --- | --- | --- |
| [上传媒体文件](0646-upload-media-files.md) | 上传图片、语音媒体资源文件以及普通文件。 | 旧版 |

### **使用教程**

钉钉提供了媒体文件接口接入流程示例。

- [上传媒体文件后发送工作通知](0645-procedure-for-using-media-files.md)：点击[file-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250729/qrbdtr/file-demo.zip?spm=ding_open_doc.document.0.0.18684a70zYmQDC&file=file-demo.zip)下载Demo。
