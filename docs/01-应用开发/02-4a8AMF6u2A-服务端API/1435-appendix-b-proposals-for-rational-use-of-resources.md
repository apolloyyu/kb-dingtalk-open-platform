---
title: "资源合理使用建议"
source_url: "https://open.dingtalk.com/document/development/appendix-b-proposals-for-rational-use-of-resources"
namespace: "development"
slug: "appendix-b-proposals-for-rational-use-of-resources"
group: "应用开发"
tab: "服务端API"
breadcrumb: "平台公告与计费 > 资源与计费 > 事件推送配额 > 资源合理使用建议"
doc_id: "FKJRIomtK8"
updated_at: "2026-04-29 13:08:42"
---

> Source: https://open.dingtalk.com/document/development/appendix-b-proposals-for-rational-use-of-resources
> Path: 应用开发 / 服务端API / 平台公告与计费 > 资源与计费 > 事件推送配额 > 资源合理使用建议
> Updated: 2026-04-29 13:08:42

# **资源合理使用建议**

钉钉开放平台提供了丰富的 Open API 、Webhook&Stream 消息通道等能力，本文提供了一些实践和建议，帮助开发者优化资源使用。

## 资源合理使用建议

一些业务场景中，应用功能可以通过调用 Open API 或者监听事件推送的方式来实现，比如获取群会话人员添加的变更信息，可以采取 Open API 轮询，也可以监听事件推送，只在需要时触发相应的操作。你可以根据以下因素做出更合适的选择。

- **实时性需求**——如果应用需要实时获取数据或处理事件，选择事件订阅方式可能更合适。
- **数据更新频率**——如果数据更新频率较高，资源消耗更多，使用事件订阅方式可能更合适。如果只需要定时或者偶尔获取数据，调用 Open API 可能更合适。
- **集成复杂度** —— 如果开发的功能较为复杂，需要调用多个 Open API, 开发成本增加，可以判断是否通过接入事件推送来降低开发难度。
- **数据获取量**——如果一次性获取的数据较大，选择事件推送方式可能更合适。调用 OpenAPI 会占用网络带宽和服务器资源。如果应用需要频繁调用 OpenAPI，可能会对系统性能和资源消耗产生影响。而事件推送可以减少对资源的消耗。

## **事件推送资源优化实践**

钉钉开放平台提供了事件推送方式，允许开发者在特定事件发生时接收实时通知。但是订阅过多的事件或处理过多的消息通知，可能会导致应用性能下降并增加资源消耗。

- **订阅必要事件**——确定应用所需的必要事件，避免订阅不相关的事件类型，减少订阅事件的数量。
- **事件业务去重**——在某些情况下，业务事件回调可能接收到重复事件，开发者需要对回调的相同 eventId 的事件做幂等处理。
- **快速响应返回——** 钉钉开放平台推送给用户的超时时间为 2.5s（http 模式）/ 3s（stream 模式）。建议消息收到后及时处理，实时正确返回响应，避免超时返回给钉钉开放平台，减少消息超时重试频率。

## **群内机器人Webhook用量管控**

当前支持管控两种群内Webhook机器人场景:

| 群自定义机器人  image.png  image.png | 搜索并添加【企业内部应用】机器人，并使用Webhook推送  image.png  image.png |
| --- | --- |

### **操作步骤**

1. 进入开发者后台>[资源管理](https://open-dev.dingtalk.com/?spm=dd_developers.header.unLogin.openDevBtn&hash=%23%2F#/)」，划动到「Webhook&Stream用量」卡片，点击「用量管控」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6457414671/p1029774.png)
2. 支持在用量管控弹窗中进行群机器人Webhook限制。

   > **[!NOTE]**
   >
   > 设置用量管控时，根据实际情况选择**全局限制**和**定向限制**，两种限制说明请参考下方说明介绍。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6457414671/p1029775.png)

### **说明**

- **【全局限制】**设置后，所有「群内的企业内部机器人Webhook」「群自定义机器人Webhook」都会被统一限制，按照单个机器人维度限制用量。

  - 场景：经常有企业成员，自己在群内创建群Webhook机器人，消耗了企业的Webhook额度，期望管控。
  - 解决办法：设置全局限制，所有群内创建的Webhook机器人，最多每月使用100次调用的额度，从而解决无法管控的问题。
- **【定向限制】**支持为指定机器人设置专属限制规则，设置后将覆盖全局限制配置

  - 场景：全局管控限制了其他成员的机器人后，有一些需要超出用量使用的IT自己做的群机器人，希望能突破限制。
  - 解决办法：设置定向限制。选择IT做的群内的自定义Webhook机器人，设置不限制。（或者设置比较大的额度）。
