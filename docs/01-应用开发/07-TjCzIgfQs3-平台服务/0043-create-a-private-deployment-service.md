---
title: "创建私有部署服务"
source_url: "https://open.dingtalk.com/document/services/create-a-private-deployment-service"
namespace: "services"
slug: "create-a-private-deployment-service"
group: "应用开发"
tab: "平台服务"
breadcrumb: "合作指南 > 产品方案商 > 应用市场的合作指引 > 基础概念 > 创建私有部署服务"
doc_id: "21VgdgMe8n"
updated_at: "2026-08-25 09:45:15"
---

> Source: https://open.dingtalk.com/document/services/create-a-private-deployment-service
> Path: 应用开发 / 平台服务 / 合作指南 > 产品方案商 > 应用市场的合作指引 > 基础概念 > 创建私有部署服务
> Updated: 2026-08-25 09:45:15

# 创建私有部署服务

计算巢服务为服务商提供了一个简便的服务创建、发布和管理的平台。每个计算巢服务的管理动作包含创建服务、测试服务、发布服务等，从而形成了服务的完整生命周期。本文介绍服务商如何通过计算巢控制台创建私有部署服务。

## 准备工作

服务商需要已加入阿里云生态合作伙伴、计算巢ISV计划，并开通了计算巢服务**权限。具体内容，请参见《服务商快速入门》**的[服务商快速入门](https://open.dingtalk.com/document/hide/quick-start-for-service-providers#section-sso-x2h-618)。

## 操作步骤

1. 登录[计算巢控制台](https://computenest.console.aliyun.com/#/vendor/cn-hangzhou/services)。

   请使用已开通计算巢服务权限的阿里云账号登录，登录后控制台默认为服务商控制台，如下图所示。

   ![iShot2022-07-29 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5132267871/p473031.png)
2. 在左侧导航栏中，单击**我的服务**。
3. 在**已发布服务**或**未发布服务**页面左上角，单击**创建新服务**。
4. 在**创建新服务**页面，配置服务信息。

   | 配置项 | | 配置说明 |
   | --- | --- | --- |
   | 服务类型 | | 计算巢服务包含多种服务类型，选择私有部署服务。私有部署服务包含服务商提供的软件和阿里云资源，且均部署在客户账号下。 |
   | 服务信息 | | 选择服务为**简体中文版**或者**英文版**，并配置以下服务信息  - 服务图标：支持JPG、PNG格式。建议您上传的图片分辨率为192x192像素，以便保证展示效果。 - 服务名称：由中文、数字、英文及下划线（\_）组成，长度在3~200个字符之间，一个中文字等于2个字符。 - 服务简介：简介长度在10~500个字符之间，一个中文字等于2个字符。 - 版本描述：版本描述长度在1~200个字符之间，一个中文字等于2个字符。建议包含具体的软件版本，同一服务下各个版本的描述不能相同。 |
   | 录入模板 | 录入方式 | 包含**手动录入模板**和**选择场景模板**两种方式。  - 手动录入模板：需要选择**部署方式**、**填写模板名称**和**模板内容**。其中模板内容可以上传已写好的模板文件，模板支持ROS JSON、ROS YAML、Terraform格式。  当**部署方式**选择**ROS**或者**Terraform**时，**模板内容**填写的详细信息，请参见[资源编排](https://open.dingtalk.com/document/publishing-services/create-and-verify-a-template#task-2223544)。若因业务场景需要，在同一服务中需要创建不同类型的模板，可填写多个模板。单击模板1后的“+”图标，添加模板。例如，在同一个服务中需要区分单可用区和多可用区时，可分别添加单可用区模板和多可用区模板来进行。  **[!NOTE]**      - 支持试用的模板，不允许新建VPC和VSwitch。若您的模板支持试用服务时，请在模板中将VPC和VSwitch参数设置为模板参数。   - 试用模板中试用的安全组必须新建，不能选择已有的安全组。 - 选择模板场景：在**选择场景**下拉菜单中选择模板场景，**模板内容**框中会自动填充内容，您无需修改。 |
   | 部署地域 | 选择允许部署的地域（可多选），如不选默认部署全部地域。 |
   | 支持说明 | 选择是否支持用户免费试用服务。试用服务的详细信息，请参见[配置免费试用](https://open.dingtalk.com/document/management-services/create-a-service-that-supports-free-trial#task-2232385)。  **[!NOTE]**  若您设置了套餐，可选择其中的一个或多个套餐为试用套餐；若未设置套餐，可指定一个或多个模板为试用模板。 |
   | 套餐设置 | 根据模板内容，选择需要设置的套餐参数并设置参数的值。 若您需要用户在创建服务实例时，可以自定义套餐内的任意参数，则可选中**是否支持自定义参数**。反之则不选。  套餐设置的详细信息，请参见[套餐设置](https://open.dingtalk.com/document/publishing-services/create-package-settings-for-a-service#topic-2128212)。  **[!NOTE]**  若您已选择**支持试用**时，创建的套餐中必须有一个套餐设置为支持试用。否则在保存文档时会报错。 |
   | 镜像分发设置 | 关联分发镜像 | 单击**关联分发镜像**，选择部署物中已分发的镜像替换模板中的镜像。  若您未创建部署物，需要先创建部署物并完成镜像分发。创建部署物的详细操作，请参见[创建部署物](https://open.dingtalk.com/document/publishing-services/create-a-deployment-object#task-2218069)。 |
   | 应用分组 | 应用分组设置 | 将模板中的资源进行分组，方便用户查看并操作资源。  用户在查看服务实例时，可以根据选择对整个服务实例或其中一个分组的资源进行查看资源、查看监控、运维管理和查看日志信息等操作。  **[!NOTE]**  每个资源只能属于一个分组。 |
   | 运维通知 | 运维通知设置 | 在**运维通知**区域**，配置报警配置模板**信息：  - 设置云监控模板：选择云监控报警模板。 - 设置分组云监控模板：选择应用分组的云监控报警模板。  **[!NOTE]**  若要选择分组云监控模板，则必须先设置应用分组。  若您还未创建云监控报警模板，则需要先创建云监控报警模板后，再选择您创建的报警模板。创建报警模板和查看报警通知的详细操作，请参见[运维通知说明](https://open.dingtalk.com/document/publishing-services/configure-notifications-for-operations-and-maintenance#task-2226699)。 |
   | 授权配置 | 用户授权 | - 如需开启代运维功能，则选中**需要用户授权**，并选择需要用户授予的权限。 - 如不需开启，则不选中**需要用户授权**。 私有部署代运维的详细操作，请参见[私有部署服务代运维设置](https://open.dingtalk.com/document/management-services/configure-the-hosted-operations-and-maintenance-feature-for-a-private-service#topic-2187549)。 |
   | 部署配置 | 预计部署时间 | 设置之后，该数据会在用户进行服务实例部署时显示，告知其平均部署时间。 |
   | 部署超时时间 | 设置了该服务实例部署超过多长时间则为异常。用户侧部署时，如果部署时间超过了超时时间，则会显示部署失败。仅当服务类型为私有部署服务时，需要配置该参数。 |
   | 部署链接权限 | 可根据您的规划进行设置。  - 公开的：所有用户在获取到部署链接后，都可以通过部署链接创建服务实例。 - 受限的：只有添加了部署链接权限白名单的用户才可以通过部署链接访问或者创建服务实例。添加用户部署链接权限白名单的具体操作，请参见  [修改服务部署权限](https://open.dingtalk.com/document/management-services/modify-the-permissions-on-service-deployment#task-2179400)。 **[!NOTE]**  在您保存或者发布服务之后，如果想要修改部署链接权限配置，可以直接在服务详情页面修改，不需要创建新版本。 |
   | 试用中心配置 | 最长试用时间 | 设置试用服务实例的最长试用时间，该参数在**支持试用**设置为开启状态时可设置。  该参数只对试用服务实例生效，对正式服务实例无效。试用服务的最长试用时间不能超过30天。  **[!NOTE]**  试用服务实例产生的资源费用由阿里云支付，但会消耗服务商的试用额度。因此，请仔细规划试用套餐或试用模板的配置和试用时长，达到用户试用体验和试用人数间取得平衡。 |
   | 标签配置 | 标签选择 | 在**标签选择**区域，选择或填写完整的标签键和标签值，为服务资源绑定标签。每个资源最多可绑定20条标签。  若无可选的标签键和标签值，可创建自定义标签。创建自定义标签的详细操作，请参见[创建并绑定自定义标签](https://open.dingtalk.com/document/resource-management/add-a-custom-tag#task-2537588)。 |
5. 单击**保存服务**，完成服务创建。

## 执行结果

创建服务完成后，您可以在**未发布服务**页面查看服务。

![iShot2022-07-29 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8320909561/p473034.png)

## 后续步骤

1. 服务保存后，您需要对创建的服务进行测试，确保其正常可用。更多信息，请参见[测试服务功能](https://open.dingtalk.com/document/service-provider-guide-refactoring/test-service-features#task-2097338)。
2. 服务测试通过后，再提交审核，审核通过后即可发布上线。更多信息，请参见[上线服务](https://open.dingtalk.com/document/publishing-services/publish-services#task-2097339)。
