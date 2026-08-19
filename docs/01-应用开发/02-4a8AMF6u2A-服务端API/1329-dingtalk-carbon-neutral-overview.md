---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/dingtalk-carbon-neutral-overview"
namespace: "development"
slug: "dingtalk-carbon-neutral-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉钉碳中和 > 概述"
doc_id: "1mQuUGQ4E5"
updated_at: "2026-07-20 10:40:39"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-carbon-neutral-overview
> Path: 应用开发 / 服务端API / 更多开放 > 钉钉碳中和 > 概述
> Updated: 2026-07-20 10:40:39

# 概述

本文介绍钉钉碳减排的产品理念、核心功能、数据可信性依据，以及如何查看减碳成果和接入其数据能力。通过本指南，开发者与企业管理者可全面了解钉钉在推动企业绿色办公与数字化减碳方面的实践路径。

## **简介**

### **产品定义与定位**

“钉钉碳减排”是钉钉基于集团ESG战略推出的碳普惠公益产品，旨在通过**利用数字技术**助力企业在日常办公中的低碳行为，让每个企业组织都能够更便捷、更低门槛的加入减碳行列，为企业组织提供数字化服务平台，让其通过日常的低碳办公行为，**结合最新数字化技术，**减少自然资源的消耗，帮助更多企业组织实现「碳中和」**。**

![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7707134861/p672149.png)

该产品由钉钉联合北京绿色交易所共同推出，对平台上的低碳办公场景进行权威方法学认证，实现减碳行为的可视化、可量化和可持续运营。用户积累的“低碳能量”可用于公益捐赠或福利兑换，进一步增强组织内部的环保参与感。

### **核心价值**

- **科学可信**：所有减碳场景均基于经认证的方法学报告与专业测算模型。
- **便捷接入**：无需额外硬件或复杂系统改造，企业开通后即可自动记录减碳数据。
- **生态扩展**：未来将接入更多数字化减碳应用，构建开放的低碳办公生态。

## **使用场景**

钉钉碳减排所提供的碳数据具备高度的专业性与公信力，适用于企业社会责任报告、绿色办公评估及潜在的碳交易准备。以下是其核心优势的具体说明：

### **覆盖广泛的低碳办公场景**

其产品形态核心围绕**TO B**维度引入开发，组织在钉钉上的**11个核心**低碳办公场景已完成减碳测算，并引入阿里云能耗宝提供的3个减碳好习惯，未来将接入更多低碳数字化生态应用，全面呈现组织在数字化办公上的减碳成果。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8707134861/p672152.png)

### **方法学与测算依据**

钉钉碳减排提供的减碳数字化场景，具备可追溯的方法学报告及一套科学专业的测算公式，提升组织ESG报告的信披能力，并为组织“践行节能减排，助力绿色发展”提供数据支撑。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7707134861/p672151.png)

目前“视频视频会议和无纸化办公”的减碳场景正在递交申请深圳碳普惠场景的备案准备，未来有望进行碳交易或碳抵消。随着各地政策落实，我们会联合集团ESG部门，积极推进地方政府认可相关的方法学。

## **查看减碳成果**

创建组织后，会默认预置钉钉碳减排服务，你可以通过手机端打开 **钉钉**，以下任意方式查看组织/个人减碳成果。

- **我的** > **钱包** > **碳减排**。

  ![我的碳减排..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9325154871/p672687.png)
- 直接**搜索**“碳减排”或“绿色办公”。

  ![查询减排..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9325154871/p672686.png)
- 用钉钉扫码进入。

  ![扫码碳减排..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9325154871/p672674.png)

## **开放概览**

钉钉碳减排提供了丰富的能力，开发者可以实现节能增效、绿色降碳等场景的数据支撑，与企业业务系统打通。

> **[!IMPORTANT]**
>
> 更多碳减排数据开放及消费能力请移至[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)，该平台是为企业提供的统一数据管理平台，基于钉钉构建安全、可扩展、易维护和管理的数据服务，助力业务决策！

![碳减排说明..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9325154871/p672673.png)

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [写入每日用户碳数据明细信息](1330-write-in-the-detailed-information-of-daily-user-carbon-data.md) | 通过此接口可写入用户的每日碳减排行为明细数据，包括减碳方式、减碳量、行为时间等详细信息。 | 新版 |
| [写入每日组织碳数据明细信息](1331-third-party-applications-write-daily-organizational-carbon-data-details-1.md) | 通过此接口可上报组织每日的碳减排明细数据，包括减碳行为类型、减碳量、发生时间等信息。 | 新版 |
