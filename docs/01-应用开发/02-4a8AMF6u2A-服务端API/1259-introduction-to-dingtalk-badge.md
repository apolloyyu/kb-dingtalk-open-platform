---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/introduction-to-dingtalk-badge"
namespace: "development"
slug: "introduction-to-dingtalk-badge"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 概述"
doc_id: "SIaNaJiIrE"
updated_at: "2026-05-19 20:32:08"
---

> Source: https://open.dingtalk.com/document/development/introduction-to-dingtalk-badge
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 概述
> Updated: 2026-05-19 20:32:08

# 概述

钉工牌作为组织内的数字身份码，一码连接班车、门禁、考勤、自助服务、工作餐，以及员工参展、差旅、外勤等各种场景，实现企业员工在组织外也一码畅行。本文介绍如何使用钉工牌。

## 什么是钉工牌

钉工牌是企业数字化的标志，是员工的数字化工作证。钉钉基于组织自身的通讯录，联合支付宝和阿里云的支付与安全能力，为企业组织提供一站式的工牌解决方案。

企业可开通钉工牌服务，员工出示钉工牌，不仅能实现物理工牌常有的门禁通行、食堂就餐支付等能力，还能有访客识别、企业协议价支付、员工收款等能力。钉钉聚焦实现用户端钉工牌的展码、解码、支付、安全等能力，在应用场景上与合作伙伴的系统开放共建。

### 操作界面

钉工牌包含组织、个人、管理三个页面，可在页面底部进行切换。

- **组织**

  ![组织](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1185950461/p377225.png)
- **个人**

  ![个人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1185950461/p377234.png)
- **管理**

  - 工牌管理

    ![企业管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1185950461/p377235.png)
  - 个人码管理

    ![个人码管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1185950461/p377236.png)

### **场景示例**

以下表格中介绍了钉工牌的几种常见的使用场景。

#### **场景一：刷码消费**

##### **示例一**

- 场景描述：某科技公司为方便企业内员工在食堂就餐，开发了一个企业内部应用，接入了钉工牌的能力，为企业内部员工分配电子码，然后采用虚拟账户充值机制，当员工在食堂消费时只从该虚拟账户扣款。
- 相关接口：

  - [解码钉工牌电子码](1264-stack-dingtalk-badge.md)
  - [通知支付结果](1265-sync-dingtalk-badge-code-payment-result.md)
  - [通知退款结果](1266-notification-dingtalk-badge-code-refund-result.md)

##### **示例二**

- 场景描述：某科技公司为方便企业内员工在食堂就餐，开发了一个企业内部应用，接入了钉工牌的能力，为企业内部员工分配电子码，然后采用虚拟账户充值机制，如果员工的虚拟户或者点券余额不足消费金额时，需要从员工的支付宝账号免密扣款。
- 相关接口：

  - [解码钉工牌电子码](1264-stack-dingtalk-badge.md)
  - [通知支付结果](1265-sync-dingtalk-badge-code-payment-result.md)
  - [通知退款结果](1266-notification-dingtalk-badge-code-refund-result.md)
  - [支付宝相关的收单接口](https://opendocs.alipay.com/open/01zuoj)

    > **[!NOTE]**
    >
    > 在使用钉工牌解码接口返回的**alipayCode**调用支付宝接口进行支付时，需要额外将requestId传入支付宝扩展参数**extend\_params**中，**extend\_params**参数格式如下：
    >
    > ```
    > {
    >     "extend_params": {
    >         "DYNAMIC_TOKEN_OUT_BIZ_NO": "这里传requestId"
    >     }
    > }
    > ```

#### **场景二：核验场景**

- 场景描述：某公司是一个门禁服务商，其上架的第三方企业应用中集成了钉工牌能力，实现为其客户公司员工定制的门禁系统。
- 相关接口：

  - [创建钉工牌电子码](1262-create-a-badge-user-instance.md)
  - [解码钉工牌电子码](1264-stack-dingtalk-badge.md)
  - [同步钉工牌码验证结果](1268-notification-dingtalk-badge-verification-result.md)

#### **场景三：临时场景**

- 场景描述：某公司是一个门禁服务商，其上架的第三方企业应用中集成了钉工牌能力，实现为其客户公司员工定制的门禁系统。
- 相关接口：

  - [解码钉工牌电子码](1271-decoding-dingtalk-payment-code.md)
  - [创建钉工牌电子码](1269-create-a-user-code-instance.md)
  - [更新钉工牌电子码](1270-update-user-code-instance.md)

## 如何使用钉工牌

### 工作原理

下图展示了钉工牌的工作原理。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4406984361/p342121.png)

### 用户使用流程

钉工牌用户使用流程如下：

1. 打开钉钉移动端，在钉钉首页，单击右上角**+**号，然后单击**钉工牌**。

   ![入口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3154135361/p344865.png)
2. 打开钉工牌之后，会自动加载组织内已开通的钉工牌功能。

   ![丁工牌](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3154135361/p344873.png)
3. 在需要核验的场景下，出示对应的码即可。
4. 在扫码完成后，会展示核验结果。

   以下分别为公司门禁、访客验证和支付场景的验证结果。

   ![场景](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8359135361/p344934.png)

## 开放概览

### **开放接口列表**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建钉工牌电子码](1262-create-a-badge-user-instance.md) | 调用本接口为用户创建钉工牌电子码实例，主要用于访客、会展等临时证场景。 | 新版 |
| [更新钉工牌电子码](1263-update-dingtalk-user-instance.md) | 调用本接口更新用户钉工牌码的相关信息。 | 新版 |
| [解码钉工牌电子码](1264-stack-dingtalk-badge.md) | 用本接口解码钉工牌码，获取关联的企业、用户userid等信息。 | 新版 |
| [通知支付结果](1265-sync-dingtalk-badge-code-payment-result.md) | 用户使用钉工牌码扫码支付完成后，可调用本接口同步支付结果，并通知用户完成消费，同时为用户记录账单。 | 新版 |
| [通知退款结果](1266-notification-dingtalk-badge-code-refund-result.md) | 用户使用钉工牌码支付后，如果发生退款，退款完成后，调用本接口同步退款结果，生成对应账单。 | 新版 |
| [同步钉工牌码验证结果](1268-notification-dingtalk-badge-verification-result.md) | 用户使用钉工牌码进行身份验证后，可调用本接口通知身份验证结果。 | 新版 |
| [配置企业钉工牌](1261-save-dingtalk-enterprise-instance.md) | 调用本接口为企业企业开通钉工牌电子码。 | 新版 |
| [钉工牌通知消息](1267-dingtalk-badge-notification-message.md) | 调用本接口，可用于在企业钉工牌页面，发送企业针对员工的通知消息。 | 新版 |
| [创建钉工牌电子码](1269-create-a-user-code-instance.md) | 调用本接口为用户创建钉工牌电子码实例，主要用于访客、会展等临时证场景。 | 新版 |
| [更新钉工牌电子码](1270-update-user-code-instance.md) | 调用本接口更新用户钉工牌码的相关信息。 | 新版 |
| [解码钉工牌电子码](1271-decoding-dingtalk-payment-code.md) | 用本接口解码钉工牌码，获取关联的企业、用户userid等信息。 | 新版 |
| [通知支付结果](1272-notify-dingtalk-payment-code-payment-result.md) | 户使用钉工牌码扫码支付完成后，可调用本接口同步支付结果，并通知用户完成消费，同时为用户记录账单。 | 新版 |
| [通知退款结果](1273-dingtalk-payment-code-refund-information-synchronization-operation.md) | 用户使用钉工牌码支付后，如果发生退款，退款完成后，调用本接口同步退款结果，生成对应账单。 | 新版 |
| [同步钉工牌码验证结果](1274-sync-pin-badge-code-verification-result.md) | 用户使用钉工牌码进行身份验证后，可调用本接口通知身份验证结果。 | 新版 |
| [配置企业钉工牌](1275-set-up-enterprise-payment-code-configuration-interface.md) | 调用本接口为企业企业开通钉工牌电子码。 | 新版 |

### **回调事件列表**

钉工牌支持钉工牌核验、批量支付消息通知和用户代扣签解约事件。

- [钉工牌核验事件](../04-LFcRvVD08N-事件订阅/0030-event-ding-badge-verify.md)
- [批量支付消息通知](../04-LFcRvVD08N-事件订阅/0031-event-open-batch-trade-callback.md)
- [企业金融用户协议回调事件](../04-LFcRvVD08N-事件订阅/0032-event-open-user-agreement-callback.md)

## **使用教程**

钉钉提供了钉工牌接口接入流程示例。

- [钉工牌实现用户访客码创建](1260-nail-badge-for-identity-verification.md)

## 名词解释

### **电子码**

钉工牌的核心，是一个基于组织id、员工id生成的动态、安全的二维码，接入方可以根据自身需求，覆盖门禁、就餐、访客等等企业场景。

### **离线能力**

钉工牌电子码支持在用户无网、弱网情况下展示与核销。

### **支付码**

电子码除了包含身份信息之外，接入方还可以通过该码值调用支付宝，从钉钉用户绑定的支付宝账号扣款。

### **身份码**

相对支付码，仅代表用户身份，不具备扣款能力。
