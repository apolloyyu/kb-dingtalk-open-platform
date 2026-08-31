---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/holiday-management-describe"
namespace: "development"
slug: "holiday-management-describe"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 假期管理 > 概述"
doc_id: "f933Zw9pYu"
updated_at: "2025-09-10 19:29:31"
---

> Source: https://open.dingtalk.com/document/development/holiday-management-describe
> Path: 应用开发 / 服务端 API / 考勤 > 假期管理 > 概述
> Updated: 2025-09-10 19:29:31

# 概述

企业都有假期的发放规则，例如根据企业员工的职位发放不同的假期余额。目前钉钉假期规则不支持此类定制化逻辑。钉钉开放假期相关的接口，满足企业更多的定制化场景。

> **[!IMPORTANT]**
>
> 在调用假期接口前，确保已经在开发者后台申请了接口权限。

## 权限申请

在调用假期管理相关接口前，需要先申请接口权限：

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/appMgr/provider/eapp/53642/1)，然后单击目标应用。
2. 单击**权限管理**，然后单击**考勤**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7540958661/p517870.png)
3. 添加假期管理相关接口权限，然后单击**申请权限**或**批量申请**。

   > **[!NOTE]**
   >
   > 如果接口申请被拒绝，可在**申请栏**中找到**假期管理**的接口权限，然后将鼠标移至**已拒绝**上查看拒绝原因。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6540958661/p517881.png)

## 场景一：同步假期规则

企业可以根据使用提供的假期API，将企业已有的假期发放规则同步到钉钉假期管理系统（[钉钉管理后台](https://oa.dingtalk.com) **> 工作台 > 应用管理 > OA审批**）。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7540958661/p517891.png)

然后在请假表单设计中使用钉钉提供的审批出勤套件，自动进行假期余额计算，并同步到钉钉考勤应用。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7540958661/p517890.png)

## 场景二：企业内部假期余额同步到钉钉审批

企业有内部的假期发放规则，希望将内部假期余额同步到钉钉审批时，可通过以下接口实现（以企业内部应用为例）：

1. 调用[初始化假期余额](0236-initialize-holiday-balance.md)接口。
2. 管理员[钉钉管理后台](https://oa.dingtalk.com) **> 工作台 > 应用管理 > OA审批 > 假期管理 > 员工假期余额**，查看更新后的员工余额。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6540958661/p517894.png)
