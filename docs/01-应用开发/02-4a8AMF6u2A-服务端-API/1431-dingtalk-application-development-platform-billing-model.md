---
title: "计费模型说明"
source_url: "https://open.dingtalk.com/document/development/dingtalk-application-development-platform-billing-model"
namespace: "development"
slug: "dingtalk-application-development-platform-billing-model"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "平台公告与计费 > 资源与计费 > 计费模型说明"
doc_id: "mFtejspXaW"
updated_at: "2026-05-09 11:47:10"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-application-development-platform-billing-model
> Path: 应用开发 / 服务端 API / 平台公告与计费 > 资源与计费 > 计费模型说明
> Updated: 2026-05-09 11:47:10

# 计费模型说明

本文介绍应用开发平台的计费模型

应用开发平台为企业开发者提供多种应用类型和丰富的应用能力，帮助企业进行数字化建设。其中，企业内部应用开发消耗的开放接口用量会被计量、事件订阅和自定义机器人使用webhook&stream消息收发会被计费。

## **应用开发平台的计费模型**

针对不同的钉钉版本，应用开发平台都配送了不同额度的 API 接口调用，Webhook&Stream 调用和 API 调用并发 QPS 的月上限权益，详细如下图：

| **能力服务** | | **标准版钉钉**  **2025 年 11 月 19 日之前** | **标准版钉钉**  **2025 年 11 月 19 日（含当日）之后** |
| --- | --- | --- | --- |
| **API接口调用量** | | 10000次/自然月 | **5000 次/自然月** |
| **Webhook&Stream调用量** | | 5000次/自然月 | **3000次/自然月** |
| **连接流节点执行量** | | 1000 次/自然月 | **500 次/自然月** |
| **QPS频次限制** | | 20qps | **20qps** |

为满足企业级客户对应用开发资源的需求，现对现有资源进行了提升，具体方案可通过以下两种模式实现弹性扩展。

**方式一**：当客户每购入**1套专业版（9800元/年）**，您可在以下权益中**任选5项组合扩容**，根据企业需求灵活定制，实现资源精准配置：

| **权益项** | | **若5项资源都需要**  示例配置A | **若需要应用开发、连接流**  示例配置B |
| --- | --- | --- | --- |
| 企业存储 | | 1TB | 不选 |
| 音视频 | 会议资源 | 3 个60分钟标清会议室  + 2 个24小时高清会议室  （同时开5个会议） | 不选 |
| 直播资源 | 1 个60分钟标清直播间  + 1个24小时高清直播间  （同时进行2场直播） | 不选 |
| 应用开发 | 付费 API 调用量  Webhook & Stream用量 | 20 万次/自然月  5 万次/自然月 | 80 万次/自然月  20 万次/自然月  （选4个权益） |
| 连接流节点执行量 | 1 万次/自然月 | 1 万次/自然月  （选1个权益） |

- 已购买钉钉专业版/钉钉专属版且合同处于有效期内的客户，仍享有原合同权益，不受本次调整影响。
- 附：[钉钉专业版（新）权益说明](https://alidocs.dingtalk.com/i/p/WVJqzqJw73dDXYEKJqzqJxEjkKyJqXYE?dontjump=true)

**方式二：**支持购买[企业开发增购包](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)，开发者可登录[开发者后台-资源管理](https://open-dev.dingtalk.com/?hash=%23%2F#/)查看企业所有的用量权益。如您已经收到用量预警，或调用额度无法满足使用，您可以购买[应用开发增购包（独立购）](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)提升当月调用总额度。

|  | **企业应用开发增购包** | **价格** |
| --- | --- | --- |
| **API接口调用量** | **500万次/自然月（可叠加）** | **19800元/年** |
| **Webhook&Stream调用量** | **50万次/自然月（可叠加）** |
| **QPS频次限制** | **60qps（****上限60QPS****）** |
| **连接流节点执行量** | **10万次/自然月（可叠加）** |

## **计量规则**

- 因为单应用调用QPS限流、API全局QPS限流、网络不可达等原因导致的失败调用，不会被统计到调用次数中。
- 基础开放接口不纳入计费，具体请查看[不纳入调用量限制的接口清单](1432-basic-interfaces-such-as-log-off-and-address-book.md)
- 基础事件订阅不纳入计费，具体请查看[不纳入使用量限制的事件清单](1434-appendix-a-list-of-events-not-included-in-webhook.md)

## **使用建议**

关于如何更有效合理的调用钉钉API接口，建议重点关注以下几点：

1. **优化接口调用逻辑**：例如，接口的功能是读取钉钉数据，应避免循环定时（轮询方式）调用接口，如有需要可接入钉钉的回调通知 ，有效减少调用次数，且更能保障数据实时性。
2. **判断接口错误码**：例如，调用接口遇到报错，根据错误码判断错误原因，请勿无限重试，控制重试次数。
3. 针对API的应用QPS限流，请查看[调用频次与限流](1433-how-to-process-api-throttling-on-the-dingtalk-server.md)。

关于如何更有效合理的调用钉钉 Webhook&Stream 消息通道，建议重点关注：

1. **事件订阅优化方案，遵循以下几个原则**：仅订阅必要事件、事件业务去重、快速响应返回，具体可参考[资源合理使用建议](1435-appendix-b-proposals-for-rational-use-of-resources.md)。
