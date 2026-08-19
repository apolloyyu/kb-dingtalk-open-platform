---
title: "打开审批详情"
source_url: "https://open.dingtalk.com/document/development/open-approval-details"
namespace: "development"
slug: "open-approval-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开审批详情"
doc_id: "ljZXkVdRWD"
updated_at: "2022-12-28"
---

> Source: https://open.dingtalk.com/document/development/open-approval-details
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开审批详情
> Updated: 2022-12-28

# 打开审批详情

本文档介绍如何通过指定协议跳转至钉钉OA审批实例详情页，适用于企业内部应用、第三方应用等场景。

## 使用场景

当用户在三方系统中处理完业务流程后，常需跳转至钉钉审批详情页查看当前审批进度或操作记录。通过构造特定URL协议，可实现从外部系统一键跳转至钉钉OA审批详情界面，提升用户体验和操作效率。

下图为跳转后的示意图：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3808165271/p846042.png)

## 协议

```
https://applink.dingtalk.com/approval/detail
```

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **Mac** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | 7.0.30 | 7.0.30 | 7.0.30 | 7.0.30 |

## **字段说明**

| **名称** | **类型** | **是否必填** | **示例值** | **描述** |
| --- | --- | --- | --- | --- |
| corpId | String | 是 | ding16b\*\*\*\*c288 | 企业corpId，可参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。 |
| instanceId | String | 是 | PROC-\*\*\*\*-\*\*\*\*- | 实例 ID，可根据 OpenAPI [发起审批实例](0497-create-an-approval-instance.md)获取/通过[审批事件订阅](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)获取。 |
| from | String | 是 | ding\*\*\*\*lxhgn | 请求来源，建议传开发者后台的应用key：   - 企业内部应用，填写应用的[Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（appKey）。 - 第三方企业应用，填写应用[Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（suiteKey）。 |

## **使用示例**

> **[!NOTE]**
>
> 使用前请确认填写参数是否正确。

```
https://applink.dingtalk.com/approval/detail?corpId=ding1*****8e4f7c288&instanceId=IHWzTQ****1745725553&from=ding*****xhgn
```
