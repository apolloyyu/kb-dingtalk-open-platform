---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-of-manufacturing-open-api"
namespace: "development"
slug: "overview-of-manufacturing-open-api"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 制造业 > 概述"
doc_id: "wlKgjaGvvA"
updated_at: "2026-05-19 20:34:21"
---

> Source: https://open.dingtalk.com/document/development/overview-of-manufacturing-open-api
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 制造业 > 概述
> Updated: 2026-05-19 20:34:21

# 概述

本文介绍了智能如何调用制造业计件日结系列接口和接口的功能描述。

## 什么是计件日结

计件日结是一款**钉钉小程序**，只要用来帮助生产企业解决计件报工等业务的快捷应用，是钉钉的共创伙伴和服务商。其功能包括工单、计件、报工、工资核算和可视化统计查询等。

让老板与生产管理人员清楚掌握用工成本、人员做工情况，真正避免了财务与员工、员工与员工之间因计件工资引起的不和谐情绪。

下图为计件日结主流程：

![计件日结主流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476380461/p378259.png)

## 开放概览

为更好解决**计件日结**应用和客户已有mes系统的对接，提升制造业企业的使用体验，实现mes和计件日结的互通，解决客户因上线钉钉**计件日结**后造成的系统割裂问题，开放以下接口。

| API | API说明 | API版本 |
| --- | --- | --- |
| [日清月结-计件报工接口](1108-riqing-monthly-settlement-piece-rate-reporting-interface.md) | 连接已有的MES应用，上报计件数据到钉钉。 | 新版 |
| [日清月结-查询计件报工数据](1109-riqing-monthly-settlement-query-interface-for-piece-rate-reporting.md) | 连接已有的MES应用，查询计件报工的数据。 | 新版 |

## **使用教程**

钉钉提供了制造业接口接入流程示例。

- [计件报工基本使用流程](1107-basic-use-process-of-a-piece-report-worker.md)
