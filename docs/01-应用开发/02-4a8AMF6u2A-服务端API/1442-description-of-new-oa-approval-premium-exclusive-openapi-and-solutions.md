---
title: "关于新增OA审批高级版专享OpenAPI和解决方案的说明"
source_url: "https://open.dingtalk.com/document/development/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions"
namespace: "development"
slug: "description-of-new-oa-approval-premium-exclusive-openapi-and-solutions"
group: "应用开发"
tab: "服务端API"
breadcrumb: "平台公告与计费 > 平台公告 > 关于新增OA审批高级版专享OpenAPI和解决方案的说明"
doc_id: "RdSbT6pygH"
updated_at: "2026-07-22 16:25:02"
---

> Source: https://open.dingtalk.com/document/development/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions
> Path: 应用开发 / 服务端API / 平台公告与计费 > 平台公告 > 关于新增OA审批高级版专享OpenAPI和解决方案的说明
> Updated: 2026-07-22 16:25:02

# 关于新增OA审批高级版专享OpenAPI和解决方案的说明

为满足广大开发者在个性化应用开发方面的需求，钉钉 OA 审批新增了一批面向[OA审批高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)客户的专享OpenAPI&解决方案。这些专享OpenAPI&解决方案将提供更丰富的能力，响应更个性化的业务需求，支持不同场景下的企业内部应用开发，建议开发者更合理、有效地使用 OpenAPI，打造更健康的钉钉开放生态。

## **一、新增的OA审批高级版的专享OpenAPI和解决方案列表**

### **说明**

钉钉可能会因法律法规、政策调整和监管指令所需，或者为维护钉钉服务安全性等，对以下接口的范围或具体功能进行增加、修改或删除。实际对客户开放的接口以钉钉开放平台届时公示的内容为准。

### **专享解决方案****列表**

钉钉 OA 审批提供四种企业流程接入方案，满足企业各类业务管理和对接诉求。具体参考：[OA审批流程中心开放方案](https://open.dingtalk.com/document/orgapp/dingtalk-oa-approval-process-center-opening-scheme)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8531807271/p851962.png)

### **专享OpenAPI****列表**

| **OpenAPI名称** | **OpenAPI详情** | **效果示例** | **适用场景** |
| --- | --- | --- | --- |
| [查询审批中心用户待处理任务列表](0535-api-premiumgettodotasks.md) | 查询企业内指定用户待处理的审批任务列表（包含官方OA审批任务和三方业务系统同步到钉钉的审批任务）。 | 企业自建审批中心效果示例：  PC端效果示例：  批量审批-pc.gif  移动端效果示例：  批量审批-移动.gif | 企业自建审批中心：  客户多套业务系统（企业自研或采购的第三方系统）中的审批任务已接入钉钉审批中心，希望借助钉钉OA审批开放能力帮助企业自建审批中心，来实现分来源筛选、批量审批等功能。 |
| [查询审批中心用户已处理任务列表](0536-api-premiumgetdonetasks.md) | 查询企业内指定用户已处理的审批任务列表（包含官方OA审批任务和三方业务系统同步到钉钉的审批任务）。 |
| [查询审批中心用户已发起实例列表](0527-api-premiumgetsubmittedinstances.md) | 查询企业内指定用户已发起的实例列表（包含官方OA审批实例和三方业务系统同步到钉钉的外部集成审批实例）。 |
| [查询审批中心用户已收到的实例列表](0528-api-premiumgetnoticedinstances.md) | 查询企业内指定用户已收到的实例列表（包含官方OA审批实例和三方业务系统同步到钉钉的外部集成审批实例） |
| [批量同意或拒绝审批任务](0537-api-premiumbatchexecuteprocessinstances.md) | 使用指定的userId和任务result及评论remark，对一批具有不同审批实例ID、任务节点ID的审批任务，进行批量处理。 |
| [根据processCode分页获取审批流程数据](0530-api-premiumgetprocessinstances.md) | 根据表单的processCode，分页获取表单审批流程数据。包括表单提交时间、表单实例ID、提交人姓名、表单实例详情数据等信息。 | 效果示例：  例如，依次单击**工作台**> **OA审批**> **首页**> **点击进入表单模板**> **查看数据**，查看对应模板数据，如下图所示。  image | 企业自建应用集成模式：使用专享OpenAPI能力，深度集成钉钉OA审批。  通过钉钉OA审批高级版专享开放接口和前端页面AppLink协议等，满足更高级的开发需求，响应更个性化的业务需求。 |
| [获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md) | 获取权限范围内的相关审批实例ID列表。**针对已开通OA高级版的客户，支持最大查询5年内的实例数据。** |
| [更新流程表单审批实例](0525-api-premiumupdateprocessinstancevariables.md) | 更新流程表单审批实例，支持对流程中和已完成的实例数据进行更新。 | - OA审批详情页查看审批实例修改记录，如下图所示：  image.jpeg - 钉钉管理后台—安全与权限—审计日志查看审批实例修改记录，如下图所示：  image.jpeg |
| [获取审批表单控件字段内容修改记录](0529-api-premiumgetfieldmodifiedhistory.md) | 根据审批实例ID、控件字段ID，获取获取审批表单控件字段内容修改的历史记录，可用于在三方系统中展示。包括被修改的表单控件字段ID、修改记录详情、修改时间、操作人的userId、操作人名称等内容。 | 效果示例：  image  image |
| [管理员查询指定员工的待处理任务列表](0538-api-premiumquerytodotasksbymanager.md) | 通过管理员(managerUserId) 查询当前审批人UserId的所有待处理的OA审批任务信息，支持在职员工和离职员工的待处理任务查询。 | 流程交接效果示例：  image  image | 流程交接解决方案：  客户希望借助钉钉OA审批开放能力，在企业业务系统内实现钉钉官方OA审批流程交接功能，实现管理员批量将审批任务转交给组织内其他人员。 |
| [管理员批量转交指定员工的待处理任务](0539-api-premiumredirecttasksbymanager.md) | 通过待转交审批任务查询接口，由管理员将任务批量转交给组织内其他在职人员，转交人支持在职人员和离职人员，被转交人必须为组织内的在职人员。 |
| [创建或更新业务分组](0540-api-premiuminsertorupdatedir.md) | 将三方系统内的业务分组信息同步到钉钉OA审批，并生成对应的钉钉待办任务OA审批分类下的二级业务来源分组。 | 自定义业务分组效果示例：支持在待办中心自定义业务分类，查阅三方业务系统来源待办更清晰  image | 流程中心集成解决方案（自定义业务分组）：  客户希望把多个三方系统的审批任务都集中在钉钉审批中心，做一站式沉浸审批。同时希望在钉钉待办中心支持自定义业务分类、列表页一键审批，为用户、特别是审批事项繁多的管理层带来超级体验。 |
| [删除业务分组](0541-api-premiumdeldir.md) | 将三方系统同步到钉钉OA审批的分组信息进行删除，并同时删除对应的钉钉待办里OA审批分类下的二级分类，对应分类下的钉钉待办数据将移动至OA审批分类下的【其他】分组。 |
| [保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md) | 将三方业务系统中的自有审批模板数据同步到钉钉OA审批，同时支持在模板维度进行审批页面托管、自定义业务分组、自定义快捷审批等多个高级功能模块自定义集成配置。 | 审批托管效果示例：   - 支持三方自有OA审批使用官方详情页样式  image - 支持三方业务自定义配置/渲染审批操作区按钮（同意、拒绝等），且可透出三方业务执行异常报错文案详情。  **红框部分为审批详情页中的主要操作区，通俗的说就是审批的主要操作按钮，在审批单托管模式中此部分区域可由三方业务实现自定义灵活配置。**  image | 流程中心集成解决方案（审批页面托管模式）：  客户业务系统自有流程引擎，希望以自有OA审批模式集成，但没有h5详情页面，希望能复用钉钉官方OA审批详情页，并可自定义审批操作区。   - 灵活对接，将不同业务系统的审批单结构、样式统一，为用户提供多端（移动端/PC/平板）一致体验 - 审批操作区按钮可自定义，同意、拒绝、转交、打印等 |
| [保存流程中心外部集成审批实例](0543-api-premiumexternalintegrationprocessinstance.md) | 将三方业务系统中的自有审批实例数据同步到钉钉OA审批，同时支持在实例维度进行审批页面托管、自定义业务分组、自定义快捷审批等多个高级功能模块自定义集成配置。 |
| [保存流程中心外部集成审批任务](0544-api-premiumsaveintegratedtask.md) | 三方系统可以配置审批任务的回调接口，这样审批人可以在钉钉待办中心、OA审批卡片消息中直接进行审批操作，待办中心、OA审批卡片会回调三方系统，三方系统收到回调后更新任务信息，并将新的任务信息同步回审批中心，形成闭环。 | 自定义快捷审批效果示例：支持在待办中心列表页、OA审批消息卡片快捷审批来源于三方业务系统的待处理任务。  image  image | 流程中心集成解决方案（自定义快捷审批）：  客户希望把多个三方系统的审批任务都集中在钉钉审批中心，做一站式沉浸审批。同时希望在钉钉待办中心、OA审批卡片消息中支持一键审批，为用户、特别是审批事项繁多的管理层带来超级体验。 |
| [创建或更新数据表单模板](0545-api-premiumsaveform.md) | 创建或更新数据表单模板。 | 接口调用效果如下图所示：  image.jpeg | 数据表单集成解决方案场景：  客户希望通过OA审批数据表单做客户信息档案的存档，并且希望通过API接口能发起数据表单及获取数据表单内已有的数据，通过API接口进行数据集成，同步到自己的业务系统中。 |
| [获取数据表单schema](0546-api-premiumgetformschema.md) | 通过数据表单code，获取对应表单的schema信息。 |
| [创建数据表单实例](0547-api-createdatapremiumsaveforminstance.md) | 创建数据表单实例。 | 效果类似于**钉钉工作台 > OA审批 > 全部审批单 > 搜索对应审批单名称 > 发起提交**，接口调用效果如下图所示。  image.jpeg |
| [更新数据表单实例](0548-api-premiumupdateforminstance.md) | 更新数据表单实例内容。 | 效果类似于**钉钉工作台 > OA审批 > 全部审批单 > 搜索对应审批单名称 > 查询数据 > 修改实例**，接口调用效果如下图所示。  image.jpeg |
| [删除数据表单实例](0549-api-premiumdeleteforminstance.md) | 删除数据表单实例，仅限以管理员身份调用。 | 效果类似于**钉钉工作台 > OA审批 > 全部审批单 > 搜索对应审批单名称 > 数据查看 > 删除实例**，接口调用效果如下图所示。  image.jpeg |
| [获取单个数据表单实例详情](0551-obtain-details-of-a-single-data-form-instance.md) | 根据实例ID获取单个数据表单实例详情，包括表单提交时间、表单实例ID、提交人姓名、表单实例详情数据等信息。 | 效果类似于**工作台**> **OA审批**> **首页**> **点击进入表单模板**> **查看数据**> **查看详情**，如下图所示。image.png |
| [获取数据表单实例列表](0550-api-premiumgetforminstances.md) | 根据表单模板code分页获取数据表单实例列表，包括表单提交时间、表单实例ID、提交人姓名、表单实例详情数据等信息。 | 效果类似于**工作台**> **OA审批**> **首页**> **点击进入表单模板**> **查看数据**，查看对应模板数据，如下图所示。image.png |
| [获取审批钉盘空间信息](0531-api-premiumgetattachmentspace.md) | 获取审批钉盘空间的ID并授予当前用户上传附件的权限。**该接口支持离职人员获取，以满足企业离职审计等场景需求。** | 支持下载企业已离职人员的审批附件组件和审批评论中的文件，效果示例如下：  image.png | 离职审计解决方案场景：  客户希望对企业已离职的某些员工中离职审计，需对该离职人员所有涉及的审批单（包含已发起、审批、抄送等）中的所有附件（包含附件组件、评论中的附件）做审计。本批接口可结合【**企业自建审批中心**】相关审批列表接口配套使用，支持查询离职人员的实例列表和附件数据，以满足企业离职审计等业务场景需求。 |
| [授权预览审批附件](0532-api-premiumgetspacewithdownloadauth.md) | 授权预览审批附件。**该接口支持对评论中的附件下载授权预览，且支持离职人员，以满足企业离职审计等场景需求。** |
| [授权下载审批钉盘文件](0533-api-premiumaddapprovedentryauth.md) | 根据钉盘空间spaceId和文件fileId对钉盘文件进行授权审批钉盘空间下载权限。**该接口支持对离职人员授权下载，以满足企业离职审计等场景需求。** |
| [下载审批附件](0534-api-premiumgrantprocessinstancefordownloadfile.md) | 获取审批文件下载授权，并且生成下载链接。**支持评论中的附件下载，且支持离职人员下载，以满足企业离职审计等场景需求。** |

## **二、专享OpenAPI&解决方案上线时间**

2024 年 9 月 30 日起将陆续上线。

## **三、专享OpenAPI&解决方案的使用条件**

上述专享OpenAPI&解决方案，标准版客户需要[升级OA审批高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)后才可申请使用；部分客户在 9 月 30 日上线前已经参与公测，获得了这些 OpenAPI的调用权限，请按以下规则调用：

| **客户类型** | **是否参与公测** | **是否受影响** |
| --- | --- | --- |
| OA审批高级版客户 | 已参与公测 | 不受影响，继续正常调用 |
| 未参与公测 | 申请接口使用权限后，可调用 |
| 标准版客户 | 已参与公测 | 不可调用，需升级至OA审批高级版后，申请接口调用权限后才能恢复调用；权限申请步骤请参考本文档第四部分的说明 |
| 未参与公测 | 不可调用，需升级至OA审批高级版后，申请接口调用权限后才能调用；权限申请步骤请参考本文档第四部分的说明 |

## **四、专享OpenAPI&解决方案权限申请步骤**

申请入口：「[**开发者后台**](https://open-dev.dingtalk.com/) **> 应用开发 > 钉钉应用 > 新建应用或已有应用 > 点击应用 > 权限管理 > OA审批」**

- OA审批高级版客户，在「权限申请」处，搜索**「****OA审批工作流读写权限（OA高级版专享）****」**即可申请对应接口权限。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8531807271/p851980.png)
- 标准版客户，在「权限申请」处搜索**「****OA审批工作流读写权限（OA高级版专享）****」**，点击申请权限将跳转OA审批高级版的购买页面，[升级OA审批高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)后再申请接口权限。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8531807271/p851981.png)

## **五、常见问题**

1. 专享 OpenAPI 的计费规则是什么？

   答：标准版钉钉客户无法使用 OA 审批高级版的专享OpenAPI&解决方案，需要先[升级OA审批高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)后才能调用这些接口，专享 OpenAPI 使用时消耗 OA 审批高级版的 OpenAPI 额度。
2. 标准版客户能看到这些专享 OpenAPI 吗？

   答：2024 年 9月 30 日起，开发者可在开放平台开发者文档「**OA审批> 高级版专享接口」**及[开发者后台](https://open-dev.dingtalk.com/)中看到本次上线的专享 OpenAPI。
