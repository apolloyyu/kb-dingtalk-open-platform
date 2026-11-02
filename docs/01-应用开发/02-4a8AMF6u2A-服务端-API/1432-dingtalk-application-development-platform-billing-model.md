---
title: "计费模型说明"
source_url: "https://open.dingtalk.com/document/development/dingtalk-application-development-platform-billing-model"
namespace: "development"
slug: "dingtalk-application-development-platform-billing-model"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "平台公告与计费 > 资源与计费 > 计费模型说明"
doc_id: "mFtejspXaW"
updated_at: "2026-10-28 15:14:13"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-application-development-platform-billing-model
> Path: 应用开发 / 服务端 API / 平台公告与计费 > 资源与计费 > 计费模型说明
> Updated: 2026-10-28 15:14:13

# 计费模型说明

本文介绍应用开发平台的计费模型。

应用开发平台为企业开发者提供多种应用类型和丰富的应用能力，帮助企业进行数字化建设。

## **应用开发平台的计费模型**

为促进企业在AI时代更多的业务创造与落地，钉钉各版本对应享有以下PaaS权益额度：

| **权益项** | | **标准版**  **未年检认证** | **标准版**  **已年检认证** | **AI基础版** | **AI高级版** | **AI尊享版** | **AI旗舰版** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **应用开发** | **付费 API 调用量** | **10000 次/自然月** | **10000 次/自然月** | **无上限** | **无上限** | **无上限** | **无上限** |
| **QPS频次限制** | **20** | **20** | **60** | **60** | **60** | **60** |
| **连接流节点执行量** | **700 次/自然月** | **700 次/自然月** | **/** | **50万次/自然月** | **100万次/自然月** | **250万次/自然月起** |

***备注说明****：付费API调用量无上限，指的是「不设置自然月度调用总量上限，但仍受 QPS频次限制等平台合理使用规则约束」*

为满足企业级客户对应用开发资源的需求，支持客户通过以下两种模式实行弹性拓展：

- **方式一**：支持客户自主选择[AI钉钉商业版本](https://n.dingtalk.com/dingding/dd-official-store/home.html?spm=a213l2.13146415.0.0.7f151ef7CTp82y&channel=aggregation_guanwang)升级，根据企业需求灵活定制，具体可咨询您的客户经理，[点此预约咨询](https://page.dingtalk.com/wow/dingtalk/default/dingtalk/9f1c40a074094777beaa928b2c4fbc1d)；
- **方式二**：支持AI钉钉商业版本客户独立购买连接流节点执行量增购包。开发者可登录[开发者后台-资源管理](https://open-dev.dingtalk.com/?hash=%23%2F#/)查看企业的用量权益与详情。如您已经收到用量预警，或调用额度无法满足使用，您可以购买连接流节点执行量增购包提升连接流节点执行量的调用总额度。

## **计量规则**

- 因单应用调用QPS限流、API全局QPS限流、网络不可达等场景导致的失败调用，不会被统计到调用次数中。
- 基础开放接口不纳入计费，具体请查看[不纳入调用量限制的接口清单](1433-basic-interfaces-such-as-log-off-and-address-book.md)。

## **使用建议**

关于如何更有效、合理调用钉钉API接口，建议重点关注以下几点：

- **优化接口调用逻辑**：例如，接口的功能是读取钉钉数据，应避免循环定时（轮询方式）调用接口，如有需要可接入钉钉的回调通知 ，有效减少调用次数，且更能保障数据实时性。
- **判断接口错误码**：例如，调用接口遇到报错，根据错误码判断错误原因，请勿无限重试，控制重试次数。
- 针对API的应用QPS限流，请查看[调用频次与限流](1434-how-to-process-api-throttling-on-the-dingtalk-server.md)。
