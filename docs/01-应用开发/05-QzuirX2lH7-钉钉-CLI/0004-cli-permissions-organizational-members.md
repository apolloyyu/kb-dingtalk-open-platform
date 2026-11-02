---
title: "如何开通组织成员CLI权限申请"
source_url: "https://open.dingtalk.com/document/development/cli-permissions-organizational-members"
namespace: "development"
slug: "cli-permissions-organizational-members"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "新手入门 > 权限管理 > 如何开通组织成员CLI权限申请"
doc_id: "Pfts2dx6c6"
updated_at: "2026-10-29 15:00:29"
---

> Source: https://open.dingtalk.com/document/development/cli-permissions-organizational-members
> Path: 应用开发 / 钉钉 CLI / 新手入门 > 权限管理 > 如何开通组织成员CLI权限申请
> Updated: 2026-10-29 15:00:29

# 如何开通组织成员CLI权限申请

本文介绍组织管理员如何开通和关闭「组织成员 CLI 权限申请」能力，以及在成员发起申请后如何完成审批开通。

## **说明**

DWS CLI 的可用人员范围支持全员可用，或按部门、角色圈选指定人员。当采用指定人员范围时，**范围外成员可以向管理员主动发起 DWS CLI 使用申请**，由管理员审批后单独开通该人员的权限，无需管理员逐个手动添加人员。

- **申请开关位置**：CLI 设置页 -Agent渠道-设置-组织成员权限申请开关；本开关默认关闭，组织成员不能向管理员发起权限申请。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8595423971/p1109328.png)
- **默认状态**：**默认关闭**。开关关闭时，组织成员无法向管理员发起申请。成员发起申请会收到提示：「当前组织不支持用户主动发起 DWS CLI 使用申请」，需联系管理员在开发者后台开通。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9227523971/p1109367.png)

## **开通成员权限申请**

1. 访问[钉钉开发者后台](https://open-dev.dingtalk.com/fe/old?hash=%23%2FdeveloperSettings#/developerSettings)。
2. 依次选择**导航栏 更多 >「基本信息」**> **左侧 CLI 设置** > **Agent渠道**。
3. 打开需要设置的渠道权限开关，点击“**设置**”，进入编辑页面打开使用申请按钮。

   > **[!NOTE]**
   >
   > 千问办公渠道和其他渠道需要分别设置，每个渠道均可控制是否支持可用范围外的组织成员发起权限申请。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8595423971/p1109328.png)
4. 打开申请开关后，管理员将收到来自成员的申请，可通过OA审批同意或拒绝。

   ![5eecdaf48460cde5d2da805c3df178f6f7fea2d3cf2e1bb475b8339e1c4c24834322b4c2cdd63b4d6b58639871ed7e1ba156a98577f418d56a6f2fefd32762c3b69eb27e70ca2cf1a8b62b2f78068a3090046f3f0687177a2c63649481a0dc90](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8595423971/p1109329.png)

## **常见问题（FAQ）**

- **Q1：成员反馈无法发起权限申请？**

  检查组织成员权限申请开关是否已开启。该开关默认关闭，关闭时组织成员无法向管理员发起申请。
- **Q2：审批通过后成员仍然无法使用某项能力？**

  说明对应权限项的可用范围不包含该成员，或该权限项已被收紧。到 CLI 管控配置中找到该业务域下的权限项，调整可用范围。
- **Q3：成员反馈完全无法使用 CLI？**

  按顺序检查四处：① 组织总开关（DWS CLI 管理）→ ② 该成员所在渠道的开关与人员范围（Agent 管理）→ ③ 对应权限项的可用范围（CLI 管控配置）→ ④ 该成员是否已通过权限申请审批。
- **Q4：修改生效范围后多久生效？**

  生效范围修改保存后约 5 分钟生效。
