---
title: "应用开发与监控"
source_url: "https://open.dingtalk.com/document/dingstart/dingstart-development-application"
namespace: "dingstart"
slug: "dingstart-development-application"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 应用开发与监控"
doc_id: "9B3wrjX0dJ"
updated_at: "2026-05-12 08:53:46"
---

> Source: https://open.dingtalk.com/document/dingstart/dingstart-development-application
> Path: 应用开发 / 开发指南 / 开发指南 > 应用开发与监控
> Updated: 2026-05-12 08:53:46

# 应用开发与监控

## **开发应用**

平台目前提供了多种应用开发方式，其中包括小程序应用和微应用、酷应用等，你可根据实际开放环境，选择合适的开发场景进行开发：

- [开发AI应用](../../03-AI-PaaS/01-pm4vgiS9Br-平台介绍/0001-introduction-to-dingtalk-ai-paas-1.md)
- [开发小程序应用](0026-optional-develop-a-small-program-server.md)
- [配置网页应用](0032-configure-web-application.md)

  > **[!NOTE]**
  >
  > 网页应用的运行环境如果是鸿蒙系统，可参考[鸿蒙适配指南](0036-harmony-adaptation-guide.md)文档，在鸿蒙系统中接入钉钉JSAPI。
- [开发酷应用](0044-coolapp-overview.md)
- [开发机器人](0077-robot-application-overview.md)

## **监控应用**

数据由客户端自动采集，并通过加密通道上报至监控平台。经过系统处理后，结果在“监控大盘”中以可视化图表形式展示，便于团队进行问题排查与性能优化。例如，当发现页面加载缓慢时，可通过“性能分析”模块查看首屏渲染时间、资源加载瓶颈，结合“API分析”判断是否存在接口响应延迟，进而优化前端逻辑或协调后端调优。

[监控平台](../06-JDICnQyZLF-开发工具/0017-monitoring-platform-1.md)提供全面的应用性能与异常监控能力，帮助开发者实时掌握应用运行状态，快速定位并解决问题。核心功能模块包括：

- **性能分析**：采集页面加载时间、资源加载耗时等关键性能指标。
- **JS异常**：捕获前端JavaScript运行时错误，定位异常堆栈。
- **API分析**：监控接口请求成功率、响应时间及失败原因。

> **[!IMPORTANT]**
>
> 监控中心仅支持**小程序应用**和**网页应用**（即微应用）。其他类型的应用暂不支持此功能。

### **使用前提**

在开始配置前，请确认满足以下条件：

1. **适用应用类型**：

   - 已创建并配置完成的**小程序应用**
   - 或已部署的**网页应用**（微应用）
2. **操作权限要求**：

   - 需使用企业管理员或具备“应用开发权限”的账号登录[开发者后台](https://open-dev.dingtalk.com/#/)。

### **加入监控**

请按照以下步骤完成监控中心的接入配置：

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **监控中心。**
3. 配置监控接入方式：

   - **小程序**：直接单击“**加入监控**”，系统将自动注入监控脚本。
   - **网页应用**：需复制提供的代码块，并粘贴到网页应用前端页面的 `<header></header>` 标签中。

     > **[!NOTE]**
     >
     > - 可添加对应的应用负责人、运维负责人和开发负责人。
     > - 如果是小程序，则加入代码后需要保存并重新发版；如果是微应用则加入代码后需要重新部署并更新代码。
4. 完成配置后，单击“**加入监控**”以启用服务。
5. 加入监控后，单击**查看监控大盘**，即可查看应用能力运行情况。详情可参考[监控平台](../06-JDICnQyZLF-开发工具/0017-monitoring-platform-1.md)。
