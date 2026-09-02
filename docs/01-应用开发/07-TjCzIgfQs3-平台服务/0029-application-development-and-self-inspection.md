---
title: "步骤二：完成应用开发和自检"
source_url: "https://open.dingtalk.com/document/services/application-development-and-self-inspection"
namespace: "services"
slug: "application-development-and-self-inspection"
group: "应用开发"
tab: "平台服务"
breadcrumb: "合作指南 > 产品方案商 > 应用市场的合作指引 > 步骤二：完成应用开发和自检"
doc_id: "gkxMCj7Yo0"
updated_at: "2026-08-25 09:45:07"
---

> Source: https://open.dingtalk.com/document/services/application-development-and-self-inspection
> Path: 应用开发 / 平台服务 / 合作指南 > 产品方案商 > 应用市场的合作指引 > 步骤二：完成应用开发和自检
> Updated: 2026-08-25 09:45:07

# 步骤二：完成应用开发和自检

本阶段将指导您完成应用的开发、配置、部署及自检全过程。本文档涵盖关键开发环节的操作要点，帮助开发者系统化推进项目落地。

## 开发流程

1. **创建应用并初始化配置**

   在开发者平台填写应用基本信息（如名称、图标、回调地址），完成基础创建。详细步骤请参考[第三方企业应用学习指南](../01-XOnnmGCTbn-开发指南/0004-isv-learning-map.md)。

   > **[!NOTE]**
   >
   > 为避免后续审核不通过，请仔细阅读[钉钉开放设计规范](https://open.dingtalk.com/document/design)。
2. **接入监控中心**

   配置日志上报路径与监控指标，启用性能追踪和异常告警功能。建议设置关键业务埋点，便于后续问题定位。详细步骤请参考[监控应用](../01-XOnnmGCTbn-开发指南/0008-dingstart-development-application.md#5bebc838f3d4q)。
3. **配置安全域名**

   在管理后台添加可信域名列表，确保前端请求来源合法。详细步骤请参考[钉钉安全域名](../01-XOnnmGCTbn-开发指南/0017-config-domain-name.md)。
4. **部署应用服务**

   将应用代码部署至稳定运行环境，推荐使用容器化方案提升部署效率与一致性。详细步骤请参考[部署方式介绍](../01-XOnnmGCTbn-开发指南/0009-introduction-to-deployment-methods.md)。
5. **执行上线前自检**

   检查接口连通性、权限配置、安全策略是否生效，并验证监控数据是否正常回传。详细步骤请参考[应用自检与分发](../01-XOnnmGCTbn-开发指南/0021-selfcheck-dingtalk-app.md)。

## 技术答疑

如果在开发过程中遇到问题，可以在**开发者后台**提交工单咨询。

具体详见：[技术支持](0044-ngliko.md)。
