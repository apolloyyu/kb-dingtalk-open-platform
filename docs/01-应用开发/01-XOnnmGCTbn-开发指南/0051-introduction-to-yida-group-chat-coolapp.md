---
title: "钉钉酷应用工厂介绍"
source_url: "https://open.dingtalk.com/document/dingstart/introduction-to-yida-group-chat-coolapp"
namespace: "dingstart"
slug: "introduction-to-yida-group-chat-coolapp"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 宜搭群聊酷应用（ISV应用） > 钉钉酷应用工厂介绍"
doc_id: "o6DQ1sGlGO"
updated_at: "2026-06-30 09:00:53"
---

> Source: https://open.dingtalk.com/document/dingstart/introduction-to-yida-group-chat-coolapp
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 宜搭群聊酷应用（ISV应用） > 钉钉酷应用工厂介绍
> Updated: 2026-06-30 09:00:53

# 钉钉酷应用工厂介绍

本文介绍了钉钉酷应用工厂（[宜搭通过低代码构建钉钉酷应用](https://xmtrf1.aliwork.com/yidaCoolApp)）内容。

## 概述

宜搭结合钉钉开放平台全面开放策略，全面开放核心场景，旨在进一步**加强钉钉生态融合、推动企业以钉钉为数字化底座的进程**，通过低代码方式共同打造酷应用，促进新流量，带来全新用户体验。

宜搭酷应用工厂助力传统企业现代化转型：

| **传统企业应用** | **宜搭酷应用** |
| --- | --- |
| - 应用繁杂冗余，造成数据孤岛，数据传递割裂感强。 - 以 SaaS 为主的传统应用升级成本高，耗时久。 - 传统系统技术结构、需求逻辑复杂，员工上手门槛高。 - 面向功能做设计，人去找应用，满足诉求。 | - 无需改变现有应用，获得新功能以及新体验。 - 通过宜搭集成自动化能力无缝集成各类应用/系统的数据，打破信息孤岛。 - 核心功能投放至钉钉群聊等高频场域，点击直达，即刻协同，工作效率 。 - 面向场景做设计，应用找人，沉浸体验。 |

## 什么是酷应用

**沉浸式融合体验，应用在钉钉端内一触即达**。**酷应用是一种基于“沉浸式、场景化、网络协同和数据普惠”理念的钉钉全新应用形态**。

- 传统应用数字化升级转型
- 改变OA和沟通的割裂现状
- 改善用户协同场景体验
- 解决沟通无沉淀、同步性差问题

更多酷应用介绍，请参考钉钉酷应用—应用新形态[酷应用开发手册](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20220824/ypdn/%E3%80%8A%E9%92%89%E9%92%89%E9%85%B7%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C%E3%80%8B.pdf)。

## 宜搭酷应用平台功能介绍

宜搭上几百万的企业自建应用都具备了半屏打开、自定义酷卡片发送、低代码逻辑编排的能力，酷能力赋能应用形态变得更简单。**宜搭上生产的低代码应用默认具备酷应用的能力！**使用入口更快捷、交互更轻量、协同更紧密、连接更轻松

宜搭酷应用的形态：**新入口、新形态、新体验、新连接**。

1. **企业自建应用或模板应用快速入群**：通过“群插件”，将巨型的企业应用解构变成敏捷的原子级功能，快速嵌入到各种高频的协同场景，让它们在应该出现的时候刚好出现。
2. **交互卡片**：通过“交互卡片”，将关键的交互动作，以卡片的方式推到群等各种协同沟通场所，在不同场景中快速完成多角色业务协同。结合"半屏卡片/表单", 让关键节点处理人能够沉浸式的实时响应。
3. **新体验：**酷应用投放到钉钉各个场域内（如钉钉群等），通过机器人发送卡片，进行业务即时响应、实时协同。表单全部默认变成半屏效果，沉浸式使用。
4. **集成自动化流融合卡片：**将复杂系统进行业务解构后，配合可视化的集成自动化能力，支持自定义卡片触发时机、数据渲染、动作设计等能力，实现企业内外部系统的互通互联，满足企业轻量级、全方位和高灵活度的复杂集成需求，降低全代码后端开发成本。

## 酷应用设计指南

钉钉酷应用整体的设计规范，详情参见[钉钉酷应用设计指南&通用设计规范](https://standard.dingtalk.com/#/cate/1/page/818)。

[](https://cloud.video.taobao.com/play/u/null/p/1/e/6/t/1/d/ud/375514552508.mp4)

宜搭搭建的应用通过酷插件默认酷应用化：

宜搭酷应用（插件）= k( 酷消息 + 酷吊顶+ 酷动态卡片 + 酷看板 )； 满足 3k ，即为酷应用

目前根据酷应用搭建的难易度和场景深度使用，将酷能力以用户视角进行了等级分层：

| L1 ：酷消息 | L2 ：酷吊顶 | L3：酷动态卡片 | L4：酷看板 |
| --- | --- | --- | --- |
| 典型场景：   - 链接分享自动转卡片 - 宜搭消息卡片化 | 典型场景：   - 项目指标进度播报 - 场景公告 | 典型场景：   - 工单预警类 - 项目进度管理类 - 数据收集型/客户服务型/单任务流转型/多任务流转型场景协同卡片范式 | 典型场景：   - 数据卡片 - 活的信息（数据）、无处不在、按需呈现 - 报表数据洞察与分析，定时播报与总结 |
| 0824酷消息 | 酷吊顶0824（1） 酷吊顶0824（2） | 0824酷动态卡片 酷动态卡片（2） | 酷看板 |
| 配置入口：   - 页面快捷消息 - 流程快捷审批卡片消息 | 配置入口：   - 页面快捷消息 - 流程设计器/集成自动化卡片节点 | 配置入口：   - 流程设计器/集成自动化卡片节点 | 配置入口：   - 数据工厂>数据服务 - 流程设计器/集成自动化卡片节点 |

## 宜搭酷应用开发说明

钉钉酷应用整体的设计规范，详情参见[钉钉酷应用设计指南&通用设计规范](https://standard.dingtalk.com/#/cate/1/page/818)。

| 01酷应用介绍 | 02酷应用设计规范与指南 | 03酷应用开发指南 | 04 酷应用模板快速酷化及上架指南 |
| --- | --- | --- | --- |
| - [酷应用介绍](https://open.dingtalk.com/coolapp) - [宜搭通过低代码构建钉钉酷应用官方介绍](https://xmtrf1.aliwork.com/yidaCoolApp)    - [钉钉酷应用工厂（通过低代码构建酷应用）全新发布](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Xzr6RBgD3LYJnMe6MxLKVZPnyElvd7e9?utm_medium=dingdoc_doc_plugin_url&utm_source=dingdoc_doc)   - [宜搭应用具备酷应用能力介绍](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/yZvMRzlLwOAWrkgXqYR9VnjY02pBqGox) - [《你好低代码-酷应用专题》直播介绍](https://h5.dingtalk.com/group-live-share/index.htm?type=2&liveFromType=6&liveUuid=5213a3b5-e054-48b9-b699-8b8dfb4547a7&bizType=kankan&dd_nav_bgcolor=FF2C2D2F#/union) | - [酷应用设计指南与通用规范](https://standard.dingtalk.com/#/cate/1/page/818) | - [低代码构建钉钉酷应用开发设计指南](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/7Y36k14mK9AV35vAPyg185NqapjblR2D)    - [酷卡片设计](0053-yida-cool-card-design.md)   - [酷流程设计](0054-yida-cool-process-design.md)   - [酷应用发布](0055-yida-cool-application-release.md)   - [酷应用启用](0056-yida-cool-application-enabled.md) - [酷应用常见高频FAQ指南](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/bxgzX5wq4YoJPe1lvQOp8Ry2OB79ALPD) | - [宜搭模板应用快速酷化&上架到钉钉酷应用市场SOP](https://xmtrf1.aliwork.com/o/cool_template_sop) |

登录[宜搭](https://www.aliwork.com/)，进行应用流程开发：

1. 集成自动化、流程设计器内新增发送、更新卡片节点，配置卡片内容，设置卡片属性、绑定卡片动作行为和渲染卡片数据。![0824渲染卡片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3521872871/p480873.png)
2. 进入卡片设计器，自定义卡片样式、数据源变量、按钮动作等。![0824设置按钮](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3521872871/p480874.png)
3. 企业自建酷应用上架到酷应用市场。![0824发布酷应用市场](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3521872871/p480875.png)
4. 钉钉群会话栏内**>**“更多”启用企业自建的酷应用，进行酷应用流程体验。![宜搭酷应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3521872871/p480357.png)
