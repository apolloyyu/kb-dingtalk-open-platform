---
title: "关于钉钉OpenAPI付费计量模式优化的通知"
source_url: "https://open.dingtalk.com/document/development/notice-optimization--payment-metering"
namespace: "development"
slug: "notice-optimization--payment-metering"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "平台公告与计费 > 平台公告 > 关于钉钉OpenAPI付费计量模式优化的通知"
doc_id: "jzaAzUXhu4"
updated_at: "2026-01-22 20:28:02"
---

> Source: https://open.dingtalk.com/document/development/notice-optimization--payment-metering
> Path: 应用开发 / 服务端 API / 平台公告与计费 > 平台公告 > 关于钉钉OpenAPI付费计量模式优化的通知
> Updated: 2026-01-22 20:28:02

# 关于钉钉OpenAPI付费计量模式优化的通知

## **尊敬的钉钉开发者**

### **一、 调整内容与生效时间**

从 2025 年 9 月 1 日起，**钉钉 AI 表格（多维表）**、**Agoal**、**组织大脑**、**OA 审批-高级版**、**宜搭**的服务端 OpenAPI 将纳入钉钉企业自建应用的 OpenAPI 付费体系，与 OA 审批、TB、钉盘、文档、考勤、人事等 API 接口一样也纳入计费计量。

### **二、 计费计量规则说明**

纳入统一管理后，您的 API 调用额度将遵循钉钉标准化的 OpenAPI 规则：

1. 免费调用额度：钉钉标准版组织，每月享有固定的免费 API 调用额度，可覆盖大部分中小型企业的日常开发与使用需求。
2. 额度用尽保护期：为防止因未及时扩容而影响业务运转，当每月额度用尽后，系统将自动提供一个**最长为 5 天 的缓冲保护期**，在此期间您的应用仍可正常调用 API。

### **三、 如何评估与准备？**

为确保您的业务在策略调整后平稳运行，我们强烈建议您提前进行评估和规划，请您登录【钉钉开发者后台】，查看您应用在过去一段时间的 API 调用情况，预估未来的使用量。

我们深知此次调整可能需要您投入时间进行适配，并在此期间提供不间断服务和预警支持。若预估用量将超出免费额度，您可以通过以下方式获取更高额度：

**方案一：**如需更高调用次数，可独立购买【[企业应用开发增购包](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)】，更多信息可查看[计费模型](1431-dingtalk-application-development-platform-billing-model.md)

**方案二：**升级至【钉钉专业版】或【钉钉专属版】，可在套餐内获得更高的免费调用额度及更多增值权益。

我们的目标是与您共同成长，打造一个更健康、高效的开发环境。如有任何疑问，请随时通过[**开发者后台**](https://open-dev.dingtalk.com/?spm=ding_open_doc.document.0.0.18684a70r5VDh3&hash=%23%2F#/)**或联系您的客户经理**进行咨询。

本公告自2025 年 7 月 22日起正式生效，特此公告。感谢您的支持与理解！

钉钉开放平台能力中心

2025 年 7 月 22 日
