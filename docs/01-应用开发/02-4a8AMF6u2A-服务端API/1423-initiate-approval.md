---
title: "发起审批"
source_url: "https://open.dingtalk.com/document/development/initiate-approval"
namespace: "development"
slug: "initiate-approval"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 发起审批"
doc_id: "QR4Lx8ue6s"
updated_at: "2022-12-28"
---

> Source: https://open.dingtalk.com/document/development/initiate-approval
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 发起审批
> Updated: 2022-12-28

# 发起审批

通过本功能，开发者可引导用户从三方系统跳转至钉钉OA审批模板页面，实现审批流程的快速发起。适用于企业内部系统与钉钉集成、自动化办公流程触发等场景。

## 使用场景

- 企业HR系统提交请假申请时，自动跳转至钉钉审批界面
- 财务系统报销流程中，动态生成审批链接并跳转
- 第三方CRM系统创建客户合同后，触发合同审批流程

下图展示了从三方业务系统构造URL并携带参数跳转至钉钉OA审批模板的标准流程。关键步骤包括：获取企业corpId、配置对应processCode、设置来源标识from，并按规范拼接URL。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3808165271/p846041.png)

## 功能流程说明

1. 开发者在钉钉开发者后台获取当前企业的 `corpId`（企业唯一标识）。
2. 在OA审批模板详情页获取目标流程的 `processCode`（模板code）。
3. 确定跳转来源标识 `from`，用于前端展示上下文提示。
4. 按照协议格式拼接完整URL：`https://applink.dingtalk.com/approval/create?corpId=xxx&processCode=xxxx&from=xxxx`
5. 在浏览器或移动端加载该链接，打开钉钉审批表单页面

## 协议

```
https://applink.dingtalk.com/approval/create
```

## 版本支持

| 钉钉客户端 | Android | iOS | Mac | Windows |
| --- | --- | --- | --- | --- |
| 版本 | 7.0.30 | 7.0.30 | 7.0.30 | 7.0.30 |

## **字段说明**

| **名称** | **类型** | **是否必填** | **示例值** | **描述** |
| --- | --- | --- | --- | --- |
| corpId | String | 是 | ding16b\*\*\*\*c288 | 企业唯一标识corpId，由钉钉分配，区分大小写，可参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。 |
| processCode | String | 是 | PROC-\*\*\*\*-\*\*\*\*- | OA审批模板的code，可参考[基础概念-processCode](0473-workflow-overview.md)。 |
| from | String | 是 | ding\*\*\*\*lxhgn | 请求来源，建议传开发者后台的应用key：   - 企业内部应用，填写应用的[ClientID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（appKey）。 - 第三方企业应用，填写应用[ClientID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（suiteKey）。 |

## **使用示例**

假设已知以下信息：

- 企业corpId：`ding95cxxxx90abcd`
- 审批流程processCode：`PROC-OFFER-APPROVAL`
- 来源系统from：`ding****lxhgn`

> **[!NOTE]**
>
> 使用前请确认填写参数是否正确。

```
https://applink.dingtalk.com/approval/create?corpId=ding95cxxxx90abcd&processCode=PROC-OFFER-APPROVAL&from=ding****lxhgn
```
