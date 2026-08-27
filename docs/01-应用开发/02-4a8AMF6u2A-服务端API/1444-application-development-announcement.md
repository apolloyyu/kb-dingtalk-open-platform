---
title: "【升级】应用开发平台权限管理升级公告"
source_url: "https://open.dingtalk.com/document/development/application-development-announcement"
namespace: "development"
slug: "application-development-announcement"
group: "应用开发"
tab: "服务端API"
breadcrumb: "平台公告与计费 > 平台公告 > 【升级】应用开发平台权限管理升级公告"
doc_id: "NTU9Rw29Q8"
updated_at: "2026-08-27 16:40:41"
---

> Source: https://open.dingtalk.com/document/development/application-development-announcement
> Path: 应用开发 / 服务端API / 平台公告与计费 > 平台公告 > 【升级】应用开发平台权限管理升级公告
> Updated: 2026-08-27 16:40:41

# 【升级】应用开发平台权限管理升级公告

为了提升开发者在应用开发与运营阶段中管理应用权限的使用体验，并便于开发者分析和查询应用已申请权限的使用情况，我们对开发者后台的权限管理功能进行了优化和升级。

## **升级详情**

### **查看权限调用**

#### **权限管理页面**

1. 进入应用详情页，单击**开发配置** > **权限管理，**在权限管理页面，新增应用权限调用情况提醒。
2. 单击**点击查看详情**跳转到**监控中心**查看权限使用情况。

> **[!NOTE]**
>
> **企业内部应用**暂无权限调用情况提醒，你可以直接访问**监控中心**查看调用情况。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0950917071/p766084.png)

#### **监控中心页面**

进入应用详情页，单击**开发配置** > **监控中心**，进入监控中心页面。

> **[!NOTE]**
>
> 权限监控的统计数据为T+1，当天开通产生调用记录的权限无法查询到，需第二天才能查询到记录。

##### **正在调用**

单击**正在调用**按钮，查看已开通权限点在近 180 天有调用记录的权限点信息和调用接口清单。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0950917071/p766085.png)

##### **未调用**

单击**未调用**按钮，查看已开通权限点近 180 天未产生调用记录的权限点信息。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1950917071/p766086.png)

### **移除权限**

进入应用详情页，单击**开发配置** > **权限管理。**可以在搜索框输入对应未调用权限点并单击**移除权限**进行权限回收。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0950917071/p766099.png)

#### **正在调用**

如果近 180 天该权限包**存在**调用记录，新增**禁止**移除权限提醒。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0950917071/p766104.png)

#### **未调用**

如果近 180 天该权限包**不存在**调用记录，新增**确认**移除权限提醒。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1950917071/p766103.png)

## **变更影响**

- 权限管理功能升级：预计于 2024 年 2 月 1 日正式上线。
- 权限管理功能升级：仅在[新版应用](https://open.dingtalk.com/document/orgapp/application-development-platform)管理生效。

## **常见问题**

- ### **权限管理升级后提供的新能力**

  **答：**升级后，新增了应用调用权限点和 OpenAPI 的统计数据，可以根据调用记录的统计，删除未调用的权限，避免了误删除的问题。
- ### **升级后权限管理功能上企业内部应用和第三方企业应用的差异**

  **答：**

  | **差异** | **企业内部应用** | **第三方企业应用** |
  | --- | --- | --- |
  | 入口 | 仅支持通过应用详情页中**开发配置** > **监控中心**中查看 | - 在应用详情页中**开发配置** > **权限管理**中单击**点击查看详情**查看 - 支持通过应用详情页中**开发配置** > **监控中心**中查看 |
  | 是否支持删除有调用记录的权限点 | 支持 | 不支持 |
- ### **应用权限调用统计时长**

  **答：**统计了应用近 180 天以内有调用记录的权限点及调用的 OpenAPI。
- ### **新申请的权限点且已经调用OpenAPI为什么显示“未调用”**

  **答：**统计数据是 T+1 而非实时的，即当天申请并调用的 OpenAPI，第二天才能统计到调用记录。
- ### **为什么在监控中心看不到“权限监控”模块**

  **答：**

  - 确认你的应用是否已经升级为新版应用
  - 确认你是否为应用的创建者或者管理员角色
