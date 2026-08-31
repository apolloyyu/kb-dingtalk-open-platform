---
title: "服务端API统计工具"
source_url: "https://open.dingtalk.com/document/download/api-development-tools"
namespace: "download"
slug: "api-development-tools"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > 服务端API开发工具 > 服务端API统计工具"
doc_id: "z07RQ1rHnf"
updated_at: "2026-01-22 19:53:10"
---

> Source: https://open.dingtalk.com/document/download/api-development-tools
> Path: 应用开发 / 开发工具 / 开发者工具 > 服务端API开发工具 > 服务端API统计工具
> Updated: 2026-01-22 19:53:10

# 服务端API统计工具

服务端API统计工具提供统计近7天的钉钉OpenAPI运行情况，包含调用次数、错误率、错误分布等信息。

## **简介**

本功能适用于企业内部自建应用及第三方企业应用，用于监控和分析近7天内调用钉钉服务端OpenAPI的运行情况。通过该工具，开发者可以查看调用次数、错误率、错误分布等关键指标，帮助定位接口调用异常、优化集成逻辑并提升系统稳定性。

**适用对象说明**： 应用创建者或应用管理员可以展示自己所管理的应用列表。

## **使用场景**

- **接口异常排查**：当业务系统出现调用失败时，通过错误分布快速定位高频错误码（如 `40001` access\_token无效）。
- **调用量监控**：评估API调用频率是否接近配额限制，提前扩容或优化调用策略。
- **多环境对比**：比较测试环境与生产环境的调用成功率差异，识别部署问题。

## 前置条件

- **用户角色要求**：您必须是目标应用的**应用创建者**或具有管理权限的**管理员**。
- **应用状态要求**：应用已成功创建并通过基础配置，处于可运行状态。
- **权限配置要求**：应用已在“权限管理”中申请并审批通过所需的API调用权限（如涉及特定接口）。
- **数据延迟说明**：页面展示的数据为离线统计结果，默认展示前一日数据，即支持查询最近8天至昨日范围内的调用记录。

## 操作步骤

你可以通过以下步骤进入API统计工具。

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 在开发者后台首页单击开发工具，然后单击**API统计**区域的**查看详情**。

   ![位置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9278284461/p401425.png)
3. 在统计区域即可查看应用的API调用**总览数据**。

   > **[!NOTE]**
   >
   > 此页面展示数据为调用钉钉服务端OpenAPI的统计数据。默认展示数据为前一天调用的离线数据，即仅支持近8天至昨日的时间筛选。
   > 应用创建者或应用管理员可以展示自己所管理的应用列表。

   ![数据总览](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0378284461/p401432.png)
4. 选择对应应用，单击操作栏**查看调用详情**即可进入API调用详情页。

   此页面可以查看查看某个应用调用的所有API，以及API一天内的调用数和出错率。

   ![调用详情页](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0378284461/p401438.png)
5. 单击**查看错误分布**即可进入错误分布图页面。

   此页面可查看各错误类型占比、错误码，以及可以直接单击**去诊断**然后查看对应错误的**错误原因**和**解决方案**。

   ![错误分布图页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0378284461/p401456.png)

## 常见问题（FAQ）

**Q1：为什么看不到某些应用的统计数据？**

A：请确认您是否为该应用的创建者或管理员，且应用未被停用或删除。

**Q2：数据为何不是实时更新？**

A：统计基于离线计算，默认延迟一天，最新仅能查看到昨日数据。

**Q3：错误码含义在哪里查询？**

A：可参考文档：

- [新版接口错误码](https://open.dingtalk.com/document/development/error-code)
- [旧版接口错误码](../02-4a8AMF6u2A-服务端-API/0013-server-api-error-codes-1.md)
