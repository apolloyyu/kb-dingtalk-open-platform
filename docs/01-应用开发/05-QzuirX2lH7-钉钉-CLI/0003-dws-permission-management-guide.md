---
title: "钉钉DWS权限管控指南"
source_url: "https://open.dingtalk.com/document/development/dws-permission-management-guide"
namespace: "development"
slug: "dws-permission-management-guide"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "新手入门 > 权限管理 > 钉钉DWS权限管控指南"
doc_id: "LM6PVPZroC"
updated_at: "2026-10-29 15:00:28"
---

> Source: https://open.dingtalk.com/document/development/dws-permission-management-guide
> Path: 应用开发 / 钉钉 CLI / 新手入门 > 权限管理 > 钉钉DWS权限管控指南
> Updated: 2026-10-29 15:00:28

# 钉钉DWS权限管控指南

本文介绍作为组织管理员如何管理组织的 CLI 权限。

## **说明**

DWS CLI（DingTalk WorkSpace CLI）将钉钉的群聊、通讯录、日历、文档、AI 表格、OA 审批等业务能力开放为命令行接口，供开发者与 AI Agent（如千问办公）调用。管理员可以通过开发者后台，从「组织级 → 渠道级 → 人员/权限项级」三个层面控制谁能用、能用到哪些能力。

## **权限管理产品界面**

- **管理入口**：[钉钉开发者后台](https://open-dev.dingtalk.com/fe/old?hash=%23%2FdeveloperSettings#/developerSettings) > 导航栏**更多** > **基本信息** > 左侧**CLI设置**。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109305.png)
- **功能介绍：**

  - **DWS CLI 管理**：组织总开关、操作日志入口。
  - **Agent 管理**：在组织权限基础上，针对不同Agent应用渠道下设置不同的DWS CLI权限。

    - **千问办公：**与钉钉深度集成，开箱即用，默认开启，仅在千问办公会话内处理，管理员可按需收紧权限。
    - **其他渠道：**默认关闭，其他渠道包含企业自建Agent和其他Agent产品，例如Codex；若组织需要在其他渠道中使用钉钉DWS，需要将其他渠道的开关打开。
  - **CLI 管控配置：**在组织下按业务域配置权限项。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109307.png)

## **组织CLI权限控制**

### **组织总开关**

控制组织成员是否可通过 DWS CLI 访问其在本组织内的个人数据（如文档、日程、消息等），是Agent可以使用钉钉DWS CLI的前提。

- **组织总开关位置**：CLI设置页 >「DWS CLI管理」卡片右上角开关。本开关**默认开启，**如需更改管理员可至开发者后台操作。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109309.png)

  当组织总开关关闭时，该组织成员没有CLI的使用权限，登录授权页面会提示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2695423971/p1109310.png)
- **组织操作日志**：可查看组织维度下的调用日志，包含成员、对应指令、是否成功等。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2695423971/p1109311.png)

  dws调用日志界面，如下图：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109312.png)

### **组织成员权限申请与审批**

组织管理员可以设置是否允许范围外成员可以向管理员发起 DWS CLI 使用申请，详见：[如何开通组织成员CLI权限申请](0004-cli-permissions-organizational-members.md)。

- **申请开关**：管理员可通过按钮控制是否允许组织成员主动发起 DWS CLI 使用申请，该开关**默认关闭**。开关关闭时，组织成员无法向管理员发起申请，用户申请时，会收到无法申请的提示：“当前组织不支持用户主动发起DWS CLI使用申请”，请联系管理员在开发者后台开通。xxxxx（独立文档）”

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109313.png)
- **当开关打开时**：不在可用范围内的人员可发起权限申请，管理员会收到相关审批，审批通过后开通该人员的DWS CLI的使用权限。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109314.png)

### **Agent渠道设置**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109315.png)

对每个已开启的 Agent 渠道，点击该行「设置」，可单独配置。如需修改生效范围，先点击“编辑”按钮，进行修改，然后保存，5分钟后生效：

- **启用开关**：控制该渠道 CLI 能力是否可用；
- **生效范围**：支持全员可用，或按部门、角色圈选；
- **权限范围管控**：支持按业务分类限定该渠道能用到哪些权限项。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109317.png)

当组织需要对某一企业自建Agent做单独的管控，可通过**“添加”**来配置企业自建应用。以钉钉应用凭证实现自建Agent的渠道单独管控，详情见：[如何单独管理企业自建Agent的权限](0005-manage-permissions-enterprise.md)。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109319.png)

## **用户权限管理**

### **CLI 管控配置**

按业务域全局配置人员可使用的 CLI 权限范围，该权限生效范围为组织维度，各渠道的设置可以基于此再精细管控。业务域包括：会话与群聊、通讯录、AI 表格、文档、邮箱、OA 审批、日历、待办、AI 听记、日志、考勤、钉盘、DING 消息、AI 应用、工作台、直播等。

每个业务域下包含若干权限项，列表展示三项信息：

- **权限名称**：一项具体的 CLI 能力，如"搜索会话列表""拉取会话消息内容""以个人身份发消息"；
- **风险等级**：低风险 / 中风险 / 高风险，用于分级收紧；
- **可用范围**：全员可用或指定人员；
- **设置：**可设置该权限是否启用与生效范围。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2695423971/p1109320.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1695423971/p1109321.png)

## **常见问题（FAQ）**

- **Q1：成员反馈无法使用钉钉连接器 / CLI？**

  按顺序检查四处：① 组织总开关（DWS CLI管理）→ ② 该成员所在渠道的开关与人员范围（Agent管理）→ ③ 对应权限项的可用范围（CLI管控配置）。
- **Q2：调用某能力时提示权限不足？**

  说明对应权限项的可用范围不包含该成员，或该权限项已被收紧。到 CLI 管控配置中找到该业务域下的权限项，调整可用范围。
- **Q3：组织自建的 Agent 能不能直接用 CLI？**

  需要打开组织总开关和其他渠道开关。如果想要对企业自建Agent做单一渠道的精细化管控，需点击「添加」走接入流程。
- **Q4：关闭组织总开关后，成员已登录的 CLI 还能用吗？**

  不能。关闭后组织内所有 CLI 调用被阻断，已登录的 CLI 会话立即失效。重新开启后成员需重新登录授权。
- **Q5：怎么查一段时间内谁在用 CLI、调用了什么？**

  使用「DWS CLI管理」卡片右上角的**操作日志**，支持按部门级、员工级查看调用记录；失败操作可查看具体错误信息，用于问题定位。
- **Q6：在千问办公中使用需要单独开通吗？**

  不需要。千问办公与钉钉深度集成，因此渠道默认开启、全员可用；管理员如需收紧，可单独调整该渠道的人员范围与可用权限。
- **Q7：目前组织自建的Agent接入了开源版本的钉钉DWS CLI，我应该如何控制权限？**

  可以通过在“其他渠道”中设置生效范围和权限范围，来控制权限。如果想实现自建Agent1和自建Agent2的权限不一致，需要分别进行“添加”，添加完成后针对不同的应用进行不同的设置。
- **Q8：我使用的是Codex类Agent产品，我的权限如何管理？**

  Codex类产品属于其他渠道，可通过在“其他渠道”进行设置管理。
- **Q9：我如果想实现仅千问办公中可使用钉钉CLI，应该如何设置。**

  打开组织开关和千问办公开关，并关闭“其他渠道”开关，即可实现仅在千问办公中使用钉钉CLI的功能。
- **Q10：我如果想实现“其他渠道”中仅企业信息管理部的人可使用应该怎么办？**

  在“其他渠道”的设置中，生效范围选择部分成员可用，在部分成员中可用范围选择企业信息管理部门。
- **Q11：之前可以使用CLI，现在没有权限了，应该怎么办？**

  为了让企业使用钉钉CLI更安全，本次更新命令权限控制新增指令级。如对您原有权限有影响，需管理员在开发者后台重新配置一下CLI权限。
