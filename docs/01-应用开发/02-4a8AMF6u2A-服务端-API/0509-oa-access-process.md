---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/oa-access-process"
namespace: "development"
slug: "oa-access-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 概述"
doc_id: "MOsft2J7pC"
updated_at: "2026-07-20 09:25:24"
---

> Source: https://open.dingtalk.com/document/development/oa-access-process
> Path: 应用开发 / 服务端 API / OA 审批 > 自有 OA 审批 > 概述
> Updated: 2026-07-20 09:25:24

# 概述

本文介绍了审批流程中心的背景、什么是审批流程中心、用户侧接入效果和开发者侧接入教程等内容。

## **审批流程中心背景**

中国企业数字化进入了新阶段，业务数字化、系统之间打通、产业链上下游数字化协同的需求增多，为了更好得满足客户的需求，钉钉选择PaaS化定位，这个定位也决定了钉钉必须越来越开放。

OA审批是钉钉产品中做适合承载PaaS化的能力之一，因此基于以上的定位，OA审批也进行了PaaS化改造。将表单能力和流程能力进行了开放，提供了流程中心接入开放方案，满足不同业务形态合作伙伴的开放需求。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3819325761/p554611.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3819325761/p554612.png)

## **什么是审批流程中心**

钉钉OA审批支持将外部系统（企业自研或采购的第三方系统）的审批任务推送到钉钉审批应用。审批任务可以实时多端（PC、手机、Pad）触达用户，并通过钉钉审批的嵌入式单据的侧边栏打开，用户在钉钉审批中即可统一查看和处理所有审批、享受一站式的审批体验，同时结合对话框消息推送、一键转发聊天、每日待办提醒、效率看板等功能，从审批发起、处理到统计全面提升审批效率。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3819325761/p554614.png)

### **适用场景**

中大型企业的审批往往分散在不同的业务系统中，审批人每天需要花费时间切换不同系统去处理审批，操作繁琐且浪费时间，而且审批人很容易忘记，导致业务不能及时得到处理，影响企业的管理效率，高层管理者面临的审批类型和数量更多，问题往往也更加严重。

**流程中心将分散在各个应用系统内的审批单据聚合，打造“一站式” OA 审批**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3819325761/p554615.png)

### **接入价值**

**为用户提供一站式 OA 审批，自建/三方审批任务也享受一方产品体验**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3819325761/p554616.png)

- 钉钉流程中心将分散在各处的审批单据聚合，减少多入口的不便利，打造“一站式”的审批管理中心。

  - 通过集成将原本分散在 **企业 OA、人力资源、财务** 等各系统中的单据集合到钉钉流程中心列表中，并提供**统一、便捷的审批数据的展示、通知（包括生成IM动态卡片、生成钉钉待办等）、操作、搜索、筛选、导出、打印、管理方式。**
  - 钉钉流程中心支持将三方或自建系统的审批数据嵌入到**钉钉审批的侧边抽屉的形式打开**，减少审批人页面跳转情况，带来连贯顺畅的审批体验。
  - 页面结构及设计简洁，同时适配 PC、手机、平板，**多端无缝切换，推广、上手门槛低**。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086677.png)
- 接入钉钉流程中心为业务提效赋能，助力更高效的审批流转效率。

  - 集成后的待办审批任务会通过**OA审批助手推送每周待办**，降低审批流转时间，减少审批任务长时间滞留情况。
  - 集成后审批流转情况将汇集到审批效率看板中，管理效率的提升直观可视化，每周将会给管理员推送**企业管理员推送企业审批效率报表**，关注异常耗时的审批人、审批部门、审批流程，**及时发现企业流程运转阻塞**，提高企业执行力。
  - 集成后可快捷将审批转发到聊天中，**打通审批与 IM 信息流**，审批人在沟通中即可完成审批
  - 通过 **一键拉群**，可一键将流程中的其他同学拉进沟通群中，保证信息传递效率及上下文清晰，支撑审批快速决策。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086678.png)
- 接入钉钉流程中心，可开放部分高级功能给管理员按需配置。

  - **Before**：钉钉审批为审批流程提供了许多高级功能，管理员可以对审批模板进行自定义设置，这些高级功能对外部系统/三方 OA 系统/套件发起的流程都是默认关闭的。
  - **After：**接入流程中心时，原生审批会开放部分高级功能给管理员按需配置。
  - **外部系统发起的流程可以在管理后台的表单管理里查看**：可以查看、编辑外部系统的表单模板；接口创建的表单模板默认在“表单管理-系统或其他应用表单”里。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086683.png)

## **用户侧接入效果**

### 员工视角效果

- 详情页

  - **OA审批官方详情页透出，三方审批表单数据同步展示，显示抄送以及审批节点**
  - **支持OA审批内完成同意、拒绝，一站式完成审批操作**
  - **透出开发商品牌标，加强生态伙伴的品牌渗透**
  - 支持三方跳转的转交、撤销
  - 支持导出/下载
  - 支持发起群聊
  - 支持分享
  - 支持跳转三方原始审批单
  - 支持评论

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515463.png)
- 支持审批消息卡片并透出生态伙伴品牌

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515465.png)
- 每天智能工作助理推送未完成的审批

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515467.png)
- 支持审批中心四大列表页透出、搜索

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515468.png)
- 抄送，发送抄送卡片

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515475.png)
- 支持钉钉统一待办通知：在一个地方处理所有工作待办

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515476.png)

### **管理员视角效果**

- 支持在管理后台查看、搜索流程中心模板

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515478.png)
- 支持在管理后台查看、搜索流程中心模板的审批实例数据
- 支持在管理后台删除/导出流程中心审批单

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856897661/p515479.png)

## **开发者侧接入教程**

详细接入流程步骤请参考：[OA审批流程中心操作流程](0476-oa-approval-process-center-access-example.md)

- 流程中心API相比原自有流程API的变化

  - 原自有流程开放接口统一迁移到流程中心新开放接口
  - 新增部分接口参数，已有参数兼容
- 新增查询OA审批待处理任务接口，开发者可通过该接口校验数据一致性

### **流程中心接入方案**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086687.png)

### **流程中心接入时序图**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086690.png)

### **具体接入方式**

企业内部应用/三方应用可以调用钉钉开放平台的自有OA审批下的流程中心相关接口，将审批数据同步到钉钉审批流程中心，为企业提供了统一的审批处理入口。详细接入流程步骤参考：[OA审批流程中心操作流程](0476-oa-approval-process-center-access-example.md)

1. 创建审批表单。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086691.png)
2. 同步数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5270154871/p1086692.png)
