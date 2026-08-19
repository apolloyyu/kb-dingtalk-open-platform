---
title: "打开审批筛选页"
source_url: "https://open.dingtalk.com/document/development/open-approval-filter-page"
namespace: "development"
slug: "open-approval-filter-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开审批筛选页"
doc_id: "xTDcGV4bQK"
updated_at: "2022-12-28"
---

> Source: https://open.dingtalk.com/document/development/open-approval-filter-page
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开审批筛选页
> Updated: 2022-12-28

# 打开审批筛选页

## 使用场景

支持从三方业务系统直接跳转打开钉钉官方OA审批中心列表页，可支持待处理、已处理、已发起、我收到的审批列表数据查询，并可根据模板类型、审批状态、审批单发起人、时间范围等筛选。

![](https://img.alicdn.com/imgextra/i2/O1CN01BzcXPi1ihP8M5Rx6B_!!6000000004444-0-tps-1670-1216.jpg)

## 协议

```
https://applink.dingtalk.com/approval/list
```

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **Mac** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | 7.0.30 | 7.0.30 | 7.0.30 | 7.0.30 |

## **字段说明**

| **名称** | **类型** | **是否必填** | **示例值** | **描述** |
| --- | --- | --- | --- | --- |
| corpId | String | 是 | ding16b\*\*\*\*c288 | 企业corpId，可参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。 |
| type | String | 是 | upcoming | 列表类型：   - upcoming：待处理 - upcomed：已处理 - applied：已发起 - carboncopy：我收到的 |
| processStatus | String | 否 | TERMINATED | 审批状态筛选，仅支持已处理、已发起列表：   - RUNNING：审批中 - COMPLETED：审批完成 - TERMINATED：已撤销 |
| processCode | String | 否 | PROC-\*\*\*\*-\*\*\*\*- | 模板code，可参考[基础概念-processCode](0473-workflow-overview.md)。 |
| from | String | 是 | ding\*\*\*\*lxhgn | 请求来源，建议传开发者后台的应用key：   - 企业内部应用，填写应用的 [Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（appKey）。 - 第三方企业应用，填写应用 [Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（suiteKey）。 |

## **使用示例**

> **[!NOTE]**
>
> 使用前请确认填写参数是否正确。

```
https://applink.dingtalk.com/approval/list?corpId=ding1*******7c288&type=carboncopy&from=din*****hgn
```
