---
title: "应用自检与分发"
source_url: "https://open.dingtalk.com/document/dingstart/selfcheck-dingtalk-app"
namespace: "dingstart"
slug: "selfcheck-dingtalk-app"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 应用自检与分发"
doc_id: "XeuRTK8YSb"
updated_at: "2026-06-30 09:00:26"
---

> Source: https://open.dingtalk.com/document/dingstart/selfcheck-dingtalk-app
> Path: 应用开发 / 开发指南 / 开发指南 > 应用自检与分发
> Updated: 2026-06-30 09:00:26

# 应用自检与分发

发布应用完成后，您需要完成上架前的应用自检与分发。本指南适用于第三方ISV应用的开发者，在提交上架前进行功能与稳定性检查。

## 准备工作

在开始自检前，请确认已完成以下配置和准备工作：

- 已登录[开发者后台](https://open-dev.dingtalk.com/)并拥有目标应用的管理或开发权限。
- 应用类型为“第三方企业应用”，且已完成开发与内部测试。
- 已在应用的 **开发配置 > 安全中心** 中配置正确的服务器出口公网IP。
- 应用首页及管理后台地址已启用HTTPS协议。
- 推送类型已设置为SyncHTTP或Stream，并完成回调URL的安全域名配置，参考[配置并更新安全域名](0013-configure-update-secure-domain-name.md)。
- 已接入监控中心，并持续运行至少24小时，确保有完整的API调用与异常监控数据。
- 服务端推荐部署于阿里云环境。

完成上述准备后，方可进入正式的自检流程。

## **自检应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，单击目标应用，进入应用详情页。
2. 在应用详情页，单击**应用发布 > 应用自检**。
3. 单击 **开始检测**，系统将自动完成功能项检查。

   该页面主要验证应用的基础配置是否合规，各检查项说明如下：

   | 检查项 | 说明 |
   | --- | --- |
   | 是否设置服务器出口ip | 需要在应用的开发配置 > 安全中心中设置服务器出口 IP。 |
   | 应用首页或管理后台地址是否https协议 | 应用首页或管理后台地址需要使用https协议。 |
   | 是否已设置有效推送类型 | 需要在应用的开发信息中完成推送设置。若使用SyncHTTP推送，回调URL地址需要使用[配置并更新安全域名](0013-configure-update-secure-domain-name.md)。 |
   | 是否已完成监控中心接入 | 需要在监控中心中完成接入，并且产生监控数据。 |
   | 服务端是否已部署在阿里云 | 选择正确的部署方式。 |
4. 功能自检完成后，单击**下一步**进入安全审核环节。请参考[安全准入评估](../07-TjCzIgfQs3-平台服务/0030-submit-your-product-to-the-shelves.md#undefined)，完成所需材料填写并提交审核。
5. 提交后进入稳定性监控阶段，如下图所示，具体要求参考[稳定性认证标准](../07-TjCzIgfQs3-平台服务/0030-submit-your-product-to-the-shelves.md#undefined)。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1198221961/p700376.png)

   | **数据指标** | **说明** | **指标要求** |
   | --- | --- | --- |
   | 监控中心的API成功率 | 可以在监控中心的**监控指标** > **API请求** > **成功率**处查看。 | ≥98.99% |
   | 监控中心的API平均耗时 | 可以在监控中心的**监控指标** > **API请求** > **请求耗时**处查看。 | <300 |
   | 监控中心的js报错率 | 可以在监控中心的**监控指标** > **JS异常** > **异常次数PV比**处查看。 | <1.99% |
   | 监控中心的白屏率 | 可以在监控中心的**监控指标** > **白屏异常** > **白屏率**处查看。 | <1.99% |
   | dd.config成功率 | 调用 d**d.config** SAPI的日平均成功率。 | ≥98.99% |
   | Http推送成功率 | 如果推送类型是Stream或SyncHttp时，成功率是统计日期内钉钉给回调地址推送的成功率（**耗时超过1500ms的推送算超时失败**）。 | ≥98.99% |
6. 稳定性监控完成后，单击**自检完成，**并**提交上架。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1198221961/p700389.png)
7. 应用提交上架后，需继续完善商品信息。请参考[步骤三：提交应用商品上架](../07-TjCzIgfQs3-平台服务/0030-submit-your-product-to-the-shelves.md)，完成应用名称、图标、描述、分类等信息的填写，以便进入审核队列。

   > **[!NOTE]**
   >
   > 如自检失败或指标不达标，请根据错误提示修复问题后重新运行检测。

## 定向应用分发

产品方案商可以自主拓展客户，基于明确的目标组织和固定的组织数量，使用**定向应用分发**功能进行第三方企业应用批量安装。

> **[!NOTE]**
>
> 如有定向定量应用分发需求，请优先加入“钉钉ISV沟通组”组织（[ISV沟通组申请地址](https://wx.dingtalk.com/invite-page/index.html?bizSource=____source____&corpId=dinga22b5311e4211323&inviterUid=B5B939A3299331EF99372A3FA1525DE6&encodeDeptId=0054DC2B53AFE745)）。

![应用定向分发](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5612469361/p260433.png)

1. 登录[开发者后台](https://open-dev.dingtalk.com/?)。
2. 单击**应用开发**，选择**第三方企业应用**。
3. 单击目标应用进入应用详情页，然后单击**定向应用分发**。
4. 单击**创建分发申请**。

   ![p244890](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7900117161/p258789.png)
5. 在**创建应用分发申请**页面填写以下信息。

   - **项目名称**：填写申请单名称。
   - **相关钉钉小二联系方式**：填写钉钉小二的手机号。
   - **应用安装方式**：

     - 授权安装：即通过客户企业管理员授权安装，需要企业管理员同意授权。
     - 静默安装：需要提交分发主组织和被分发组织之间的**书面授权安装应用的函件**，并加盖法律有效印章。

       > **[!NOTE]**
       >
       > 上传的授权函文件最大不得超过10M，支持PDF、JPG、PNG等格式的文件。
   - **导入清单**：请参考模板文件内容格式进行上传。

     清单包含以下内容：

     - 客户企业的corpId：例如，ding0ed2fxx。
     - 客户企业名称：例如，开放平台应用审核组。
     - 客户企业管理员手机号：例如，138xxxx3120。
6. 填写完成后单击**提交**，提交审核。

   ![p244965](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7900117161/p258800.png)
7. 审核通过后，选择状态为**审批通过**的项目，单击详情，进入分发页面。

   ![详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5351617161/p259164.png)
8. 在分发页面，你可以通过以下方式进行分发部署。

   - 单击**应用分发**进行部署。

     1. 单击**开始分发**，对**分发信息**下的组织进行统一部署，部署成功后，不同组织会显示不同的部署状态。

        ![开始分发](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5351617161/p259186.png)

        部署成功后，如下图所示：

        ![分发成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5351617161/p259185.png)
   - 使用部署二维码进行线下部署。

     1. 单击**部署二维码**，通过手机钉钉扫描生成的部署二维码。

        ![二维码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5351617161/p259190.png)
     2. 选择定向应用分发基本信息，并勾选**《钉钉工作台应用安装授权》**，最后单击**立即安装**。

        ![IMG_0412](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5351617161/p259209.jpg)

        安装成功后，如下图所示：

        ![IMG_0413](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5351617161/p259212.jpg)
