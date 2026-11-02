---
title: "通用数据结构"
source_url: "https://open.dingtalk.com/document/development/common-data-structure"
namespace: "development"
slug: "common-data-structure"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 通用数据结构"
doc_id: "nUsQkiT94z"
updated_at: "2025-09-12 17:20:04"
---

> Source: https://open.dingtalk.com/document/development/common-data-structure
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 通用数据结构
> Updated: 2025-09-12 17:20:04

# 通用数据结构

## DentryModel

知识库节点的数据结构。

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| contentType | String | alidoc | 内容类型。   - alidoc：钉钉文档 - link：快捷方式 - archive：压缩包 - document：文件 |
| createdTime | Long | 1663912334000 | 创建的时间戳，单位毫秒。 |
| updatedTime | Long | 1663912334000 | 更新的时间戳，单位毫秒。 |
| creator | Object |  | 创建者信息。 |
| unionId | String | chyxxxxx | 创建者的unionId。 |
| name | String | 小钉 | 创建者的名称。 |
| dentryId | String | 4BYmxxxxx | 节点ID。 |
| spaceId | String | 4BYmaKexxxxx | 知识库id。 |
| docKey | String | LAJdlxxxxx | 文档docKey，用于标识一篇钉钉文档的key。  **[!NOTE]**    只有内容类型为alidoc的才会有值。 |
| space | [SpaceModel](#SpaceModel) |  | 知识库信息。 |
| dentryUuid | String | m0Xwxxxxx | 节点全局唯一标识id。 |
| dentryType | String | file | 节点类型。   - file：文件 - folder：文件夹。 |
| extension | String | adoc | 文件后缀名。  **[!NOTE]**    只有文件返回该字段。 |
| name | String | 钉钉文档.adoc | 节点名称。 |
| url | String | https://xxx.yy | 节点访问url。 |
| path | String | 测试组织/测试知识库/abc | 节点的路径。 |
| hasChildren | Boolean | false | 是否有子节点。 |
| updater | Object |  | 更新人信息。 |
| unionId | String | abc | 更新人的unionId。 |
| name | String | abc | 更新人的名称。 |
| linkSourceInfo | [LinkSourceInfo](#LinkSourceInfo) |  | 快捷方式类型的节点，其指向的原始数据信息。 |
| visitorInfo | Object |  | 访问者对当前节点的权限等信息。 |
| spaceActions | Array of String | PUBLIC\_SHARE\_SPACE,GET\_SPACE | 空间的操作列表。   - PUBLIC\_SHARE\_SPACE：公开发布知识库 - HANDOVER\_WORKSPACE：移交空间 - UPDATE\_SPACE：更新空间基本信息 - GET\_SPACE：查询空间基本信息 - GET\_SPACE\_SECURITY：查询空间安全设置 - DELETE\_SPACE：彻底删除空间 - MANAGE\_SPACE\_SECURITY：管理空间安全设置 - GET\_SPACE\_MEMBER：查询空间成员 - MANAGE\_SPACE\_PIN：管理空间置顶 - USE\_SPACE\_TEMPLATE：使用空间模板创建 - RECYCLE\_SPACE：归档空间 - GET\_SPACE\_TEMPLATE：查询和预览空间模板 - RECOVER\_SPACE：恢复空间 - MANAGE\_SPACE\_TEMPLATE：管理空间模板 - MANAGE\_SPACE\_MEMBER：管理空间成员 - RENAME\_SPACE：重命名空间 |
| dentryActions | Array of String | COPY\_DENTRY, GET\_DENTRY\_MEMBER | 节点的操作列表。   - GET\_DENTRY：查询节点基本信息 - LIST\_CHILD：列子节点 - CREATE\_CHILD：创建子节点 - RENAME\_DENTRY：重命名节点 - MOVE\_DENTRY：移动节点 - COPY\_DENTRY：复制节点 - RECYCLE\_DENTRY：回收节点 - RECOVER\_DENTRY：恢复节点 - DELETE\_DENTRY：删除节点 - GET\_DENTRY\_MEMBER：获取节点成员列表 - MANAGE\_DENTRY\_MEMBER：管理节点成员 - PREVIEW：文档预览 - CONTENT\_COPY：内容复制 - DOWNLOAD\_ATTACHMENT：下载文档内附件/图片等资源 - EXPORT：导出为其他格式 - EXPORT\_IMAGE：导出为长图 - UPLOAD\_ATTACHMENT：上传文档内附件、图片等资源 - EDIT：文档编辑 - READ\_HISTORY：查看历史版本 - EDIT\_HISTORY：编辑历史版本 - SAVE\_AS：另存为 - SAVE\_AS\_TEMPLATE：另存为模板 - LINK\_SHARE：链接或卡片分享 - PUBLIC\_SHARE：公开分享 - CHANGE\_PERMISSION\_MODE：修改权限模式 - TEMPORARY\_SHARE\_NODE：临时共享节点 - DOWNLOAD：下载 - UPLOAD：上传 - SAVE\_AS\_QUICK\_LINK：保存为快捷方式 - SEND\_COPY\_FILE：发送副本 - CLOUD\_PRINT：云打印 - MANAGE\_SECURITY\_SETTING：管理安全设置 - UPLOAD\_FOLDER：上传文件夹 - IMPORT：导入 - IMPORT\_FOLDER：导入文件夹 |
| roleCode | String | 5 | 当前用户对这个空间的访问角色。   - 0：无权限 - 1：仅可查看 - 2：可查看/下载 - 3：可编辑 - 4：可管理 - 5：所有者 |

## DentryVO

知识库节点的数据结构。

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| contentType | String | alidoc | 内容类型。   - alidoc：钉钉文档 - link：快捷方式 - archive：压缩包 - document：文件 |
| createdTime | Long | 1663912334000 | 创建时间戳，单位毫秒。 |
| updatedTime | Long | 1663912334000 | 更新时间戳，单位毫秒。 |
| creator | Object |  | 创建者信息。 |
| unionId | String | chyxxxxx | 创建者的unionId。 |
| name | String | 小钉 | 创建者的名称。 |
| dentryId | String | 4BYmaNxxxxx | 节点ID。 |
| spaceId | String | 4BYxxxxx | 知识库ID。 |
| docKey | String | LAJdl6xxxxx | 文档docKey，用于标识一篇钉钉文档的key。  **[!NOTE]**    只有内容类型为alidoc的才会有值。 |
| space | [SpaceModel](#SpaceModel) |  | 知识库信息。 |
| dentryUuid | String | cdefg | 节点全局唯一标识ID。 |
| dentryType | String | file | 节点类型。   - file：文件 - folder：文件夹 |
| extension | String | adoc | 文件后缀名。 |
| name | String | 钉钉文档.adoc | 节点名称。 |
| url | String | https://xxx.yy | 节点访问url。 |
| path | String | 测试组织/测试知识库/abc | 节点的路径。 |
| hasChildren | Boolean | false | 是否有子节点。 |
| updater | Object |  | 更新人信息。 |
| unionId | String | xhyxxxxx | 更新人的unionId。 |
| name | String | 小钉 | 更新人的名称。 |
| linkSourceInfo | [LinkSourceInfo](#LinkSourceInfo) |  | 快捷方式类型的节点，其指向的原始数据信息。 |
| visitorInfo | Object |  | 访问者对当前节点的权限等信息。 |
| spaceActions | Array of String | PUBLIC\_SHARE\_SPACE,GET\_SPACE | 空间的操作列表。   - PUBLIC\_SHARE\_SPACE：公开发布知识库 - HANDOVER\_WORKSPACE：移交空间 - UPDATE\_SPACE：更新空间基本信息 - GET\_SPACE：查询空间基本信息 - GET\_SPACE\_SECURITY：查询空间安全设置 - DELETE\_SPACE：彻底删除空间 - MANAGE\_SPACE\_SECURITY：管理空间安全设置 - GET\_SPACE\_MEMBER：查询空间成员 - MANAGE\_SPACE\_PIN：管理空间置顶 - USE\_SPACE\_TEMPLATE：使用空间模板创建 - RECYCLE\_SPACE：归档空间 - GET\_SPACE\_TEMPLATE：查询和预览空间模板 - RECOVER\_SPACE：恢复空间 - MANAGE\_SPACE\_TEMPLATE：管理空间模板 - MANAGE\_SPACE\_MEMBER：管理空间成员 - RENAME\_SPACE：重命名空间 |
| dentryActions | Array of String | COPY\_DENTRY, GET\_DENTRY\_MEMBER | 节点的操作列表。   - GET\_DENTRY：查询节点基本信息 - LIST\_CHILD：列子节点 - CREATE\_CHILD：创建子节点 - RENAME\_DENTRY：重命名节点 - MOVE\_DENTRY：移动节点 - COPY\_DENTRY：复制节点 - RECYCLE\_DENTRY：回收节点 - RECOVER\_DENTRY：恢复节点 - DELETE\_DENTRY：删除节点 - GET\_DENTRY\_MEMBER：获取节点成员列表 - MANAGE\_DENTRY\_MEMBER：管理节点成员 - PREVIEW：文档预览 - CONTENT\_COPY：内容复制 - DOWNLOAD\_ATTACHMENT：下载文档内附件/图片等资源 - EXPORT：导出为其他格式 - EXPORT\_IMAGE：导出为长图 - UPLOAD\_ATTACHMENT：上传文档内附件、图片等资源 - EDIT：文档编辑 - READ\_HISTORY：查看历史版本 - EDIT\_HISTORY：编辑历史版本 - SAVE\_AS：另存为 - SAVE\_AS\_TEMPLATE：另存为模板 - LINK\_SHARE：链接或卡片分享 - PUBLIC\_SHARE：公开分享 - CHANGE\_PERMISSION\_MODE：修改权限模式 - TEMPORARY\_SHARE\_NODE：临时共享节点 - DOWNLOAD：下载 - UPLOAD：上传 - SAVE\_AS\_QUICK\_LINK：保存为快捷方式 - SEND\_COPY\_FILE：发送副本 - CLOUD\_PRINT：云打印 - MANAGE\_SECURITY\_SETTING：管理安全设置 - UPLOAD\_FOLDER：上传文件夹 - IMPORT：导入 - IMPORT\_FOLDER：导入文件夹 |
| roleCode | String | 5 | 当前用户对这个空间的访问角色。   - 0：无权限 - 1：仅可查看 - 2：可查看/下载 - 3：可编辑 - 4：可管理 - 5：所有者 |

## LinkSourceInfo

链接指向的原始数据信息。

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| id | String | abc | 快捷方式关联的源文件ID（空间内唯一）。 |
| spaceId | String | def | 快捷方式关联的源文件所属空间id。 |
| linkType | Long | 0 | 快捷方式类型。   - 0：通用快捷方式 - 1：闪会快捷方式 - 2：日志快捷方式 - 3：闪会2.0快捷方式 |
| extension | String | docx | 快捷方式关联的源文件后缀。 |
| iconUrl | Object |  | 非通用快捷方式的图标信息。 |
| small | String | def | 被选中时的加深图标。 |
| line | String | gh | 默认的目录树图标。 |

## OpenActionModel

操作信息的数据结构。

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| name | String | sky | 操作人名称。 |
| timestamp | Long | 273829092 | 操作时间戳。 |

## SpaceModel

知识库的数据结构。

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| id | String | n9XJxxxxx | 知识库id。 |
| name | String | 测试知识库 | 知识库名称。 |
| type | Integer | 1 | 知识库类型。 |
| url | String | https://alidocs.dingtalk.com/i/spaces/n9XJ\*\*\*\*\*\*\*Xy/overview | 知识库访问url。 |
| owner | Object |  | 知识库所有者。 |
| unionId | String | qXExxxxx | 用户unionId。 |
| name | String | 小钉 | 用户名称。 |
| visitorInfo | Object |  | 访问者对当前知识库的权限等信息。 |
| spaceActions | Array of String | GET\_SPACE | 空间的操作列表。   - PUBLIC\_SHARE\_SPACE：公开发布知识库 - HANDOVER\_WORKSPACE：移交空间 - UPDATE\_SPACE：更新空间基本信息 - GET\_SPACE：查询空间基本信息 - GET\_SPACE\_SECURITY：查询空间安全设置 - DELETE\_SPACE：彻底删除空间 - MANAGE\_SPACE\_SECURITY：管理空间安全设置 - GET\_SPACE\_MEMBER：查询空间成员 - MANAGE\_SPACE\_PIN：管理空间置顶 - USE\_SPACE\_TEMPLATE：使用空间模板创建 - RECYCLE\_SPACE：归档空间 - GET\_SPACE\_TEMPLATE：查询和预览空间模板 - RECOVER\_SPACE：恢复空间 - MANAGE\_SPACE\_TEMPLATE：管理空间模板 - MANAGE\_SPACE\_MEMBER：管理空间成员 - RENAME\_SPACE：重命名空间 |
| dentryActions | Array of String | GET\_DENTRY | 节点的操作列表。   - GET\_DENTRY：查询节点基本信息 - LIST\_CHILD：列子节点 - CREATE\_CHILD：创建子节点 - RENAME\_DENTRY：重命名节点 - MOVE\_DENTRY：移动节点 - COPY\_DENTRY：复制节点 - RECYCLE\_DENTRY：回收节点 - RECOVER\_DENTRY：恢复节点 - DELETE\_DENTRY：删除节点 - GET\_DENTRY\_MEMBER：获取节点成员列表 - MANAGE\_DENTRY\_MEMBER：管理节点成员 - PREVIEW：文档预览 - CONTENT\_COPY：内容复制 - DOWNLOAD\_ATTACHMENT：下载文档内附件/图片等资源 - EXPORT：导出为其他格式 - EXPORT\_IMAGE：导出为长图 - UPLOAD\_ATTACHMENT：上传文档内附件、图片等资源 - EDIT：文档编辑 - READ\_HISTORY：查看历史版本 - EDIT\_HISTORY：编辑历史版本 - SAVE\_AS：另存为 - SAVE\_AS\_TEMPLATE：另存为模板 - LINK\_SHARE：链接或卡片分享 - PUBLIC\_SHARE：公开分享 - CHANGE\_PERMISSION\_MODE：修改权限模式 - TEMPORARY\_SHARE\_NODE：临时共享节点 - DOWNLOAD：下载 - UPLOAD：上传 - SAVE\_AS\_QUICK\_LINK：保存为快捷方式 - SEND\_COPY\_FILE：发送副本 - CLOUD\_PRINT：云打印 - MANAGE\_SECURITY\_SETTING：管理安全设置 - UPLOAD\_FOLDER：上传文件夹 - IMPORT：导入 - IMPORT\_FOLDER：导入文件夹 |
| roleCode | String | 3 | 权限。   - 0：无权限 - 1：仅可查看 - 2：可查看/下载 - 3：可编辑 - 4：可管理 - 5：所有者 |
| recentList | Array of [DentryModel](#DentryModel) |  | 知识库中最近编辑的三篇文档。 |
| iconVO | Object |  | 知识库图标。 |
| type | String | url | 图标类型。 |
| icon | String | https://img.alicdn.com/imgextra/i1/O1xxxxx.png | 图标地址。 |
| cover | String | https://img.alicdn.com/imgextra/i1/O1xxxxx.png | 封面地址。 |
| description | String | 这是简介 | 知识库简介。 |

## SpaceVO

知识库的数据结构。

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| id | String | n9XJxxxxx | 知识库id。 |
| name | String | 测试知识库 | 知识库名称。 |
| type | Integer | 1 | 知识库类型。 |
| url | String | https://alidocs.dingtalk.com/i/spaces/n9XJ\*\*\*\*\*\*\*Xy/overview | 知识库访问url。 |
| owner | Object |  | 知识库所有者。 |
| unionId | String | qXExxxxx | 用户unionId。 |
| name | String | 小钉 | 用户名称。 |
| visitorInfo | Object |  | 访问者对当前知识库的权限等信息。 |
| spaceActions | Array of String | GET\_SPACE | 空间的操作列表。   - PUBLIC\_SHARE\_SPACE：公开发布知识库 - HANDOVER\_WORKSPACE：移交空间 - UPDATE\_SPACE：更新空间基本信息 - GET\_SPACE：查询空间基本信息 - GET\_SPACE\_SECURITY：查询空间安全设置 - DELETE\_SPACE：彻底删除空间 - MANAGE\_SPACE\_SECURITY：管理空间安全设置 - GET\_SPACE\_MEMBER：查询空间成员 - MANAGE\_SPACE\_PIN：管理空间置顶 - USE\_SPACE\_TEMPLATE：使用空间模板创建 - RECYCLE\_SPACE：归档空间 - GET\_SPACE\_TEMPLATE：查询和预览空间模板 - RECOVER\_SPACE：恢复空间 - MANAGE\_SPACE\_TEMPLATE：管理空间模板 - MANAGE\_SPACE\_MEMBER：管理空间成员 - RENAME\_SPACE：重命名空间 |
| dentryActions | Array of String | GET\_DENTRY | 节点的操作列表。   - GET\_DENTRY：查询节点基本信息 - LIST\_CHILD：列子节点 - CREATE\_CHILD：创建子节点 - RENAME\_DENTRY：重命名节点 - MOVE\_DENTRY：移动节点 - COPY\_DENTRY：复制节点 - RECYCLE\_DENTRY：回收节点 - RECOVER\_DENTRY：恢复节点 - DELETE\_DENTRY：删除节点 - GET\_DENTRY\_MEMBER：获取节点成员列表 - MANAGE\_DENTRY\_MEMBER：管理节点成员 - PREVIEW：文档预览 - CONTENT\_COPY：内容复制 - DOWNLOAD\_ATTACHMENT：下载文档内附件/图片等资源 - EXPORT：导出为其他格式 - EXPORT\_IMAGE：导出为长图 - UPLOAD\_ATTACHMENT：上传文档内附件、图片等资源 - EDIT：文档编辑 - READ\_HISTORY：查看历史版本 - EDIT\_HISTORY：编辑历史版本 - SAVE\_AS：另存为 - SAVE\_AS\_TEMPLATE：另存为模板 - LINK\_SHARE：链接或卡片分享 - PUBLIC\_SHARE：公开分享 - CHANGE\_PERMISSION\_MODE：修改权限模式 - TEMPORARY\_SHARE\_NODE：临时共享节点 - DOWNLOAD：下载 - UPLOAD：上传 - SAVE\_AS\_QUICK\_LINK：保存为快捷方式 - SEND\_COPY\_FILE：发送副本 - CLOUD\_PRINT：云打印 - MANAGE\_SECURITY\_SETTING：管理安全设置 - UPLOAD\_FOLDER：上传文件夹 - IMPORT：导入 - IMPORT\_FOLDER：导入文件夹 |
| roleCode | String | 1 | 权限。   - 0：无权限 - 1：仅可查看 - 2：可查看/下载 - 3：可编辑 - 4：可管理 - 5：所有者 |
| iconVO | Object |  | 知识库图标信息。 |
| type | String | 1 | 图标类型。 |
| icon | String | https://img.alicdn.com/imgextra/i1/xxxxx.png | 图标。 |
| cover | String | https://img.alicdn.com/imgextra/i1/xxxxx.png | 封面。 |
| description | String | 这是简介 | 知识库简介。 |
