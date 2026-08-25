---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-of-event-subscription"
namespace: "development"
slug: "overview-of-event-subscription"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "概述"
doc_id: "RMrRiwGarI"
updated_at: "2026-08-25 09:36:39"
---

> Source: https://open.dingtalk.com/document/development/overview-of-event-subscription
> Path: 应用开发 / 事件订阅 / 概述
> Updated: 2026-08-25 09:36:39

# 概述

## 什么是事件订阅

钉钉事件订阅功能，是钉钉开放平台推出的一项服务。这项服务允许开发者在自己开发的应用程序中，实时接收到钉钉平台产生的各类重要通知。通过设置事件订阅，你的应用能够监听到钉钉中发生的诸如部门架构调整、员工签到、打卡等事件，并据此在你的应用中进行及时响应和处理。利用这一功能，你的企业应用将能够更深度地与钉钉平台集成，实现信息共享和业务协同。

## **应用场景**

### 通讯录事件场景

在新员工入职或者离职时，应用需要第一时间变更用户数据，此时就可以订阅通讯录相关事件，就不需要定时去拉取通讯录对比，而是实时地获取到变化的通讯录信息，进行同步。

### 群事件场景

如果需要及时响应群内用户的操作，可以订阅事件。例如：某用户加入某群聊时，应用可以订阅即时通讯IM-会话管理下的相关事件，在用户进入群聊的时候，向用户发送欢迎等信息。

## **订阅流程**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3179592871/p741471.png)

## **订阅方式**

### **Stream 模式推送**

Stream 模式是钉钉开放平台提供的一种集成方式，它可以监听事件订阅回调使用 Stream 模式接入，钉钉开放平台将通过 Websocket 连接与应用程序通讯，Stream 模式将极大降低接入门槛和资源依赖，不需要公网服务器、IP、域名等资源，只需集成钉钉开放平台 SDK 即可。

- **适用应用：**企业内部应用、第三方企业应用
- **配置方式**：参考[配置 Stream 推送（推荐）](0003-configure-stream-push.md#151be9e66238j)
- **安全性**：不需要暴露公网ip，免受攻击，传输层使用TLS加密，每条连接的建立都有完整鉴权。
- **加解密**：无需加解密，接收到的为事件详细数据。

### **HTTP 推送**

HTTP推送方式适用于本地部署的情况，以HTTP POST请求方式以加密的方式推送给业务方。

- **适用应用：**企业内部应用
- **配置方式**：参考[配置 HTTP 推送（不推荐）](0003-configure-stream-push.md#58bfd87c4fupu)
- **安全性**：数据通道是公网通道，需要流量花费，安全等级低，效率低。
- **加解密**：推送的数据是密文数据，需要开发者自行验签、加解密，实现不同开发语言的验签、加解密逻辑。

## **订阅规则**

事件订阅的匹配规则采用Glob语法进行模式匹配。Glob是一种类似于正则表达式的匹配方式，但语法更为直观简单。在Glob规则中，可以使用包括`*`、`?`、`{}`、`[]`等特殊字符进行模式定义。在钉钉事件的自定义过滤中，我们仅使用`*`和`{}`两种字符来实现对事件的精确筛选。

> **[!NOTE]**
>
> 如果没有进行规则配置或者删除了所有已配置的规则，将会推送该类型的所有事件。

- **一个星号**`*`

  匹配任意个数的字符，包括空。不包括路径边界`/`或 `\`。例如： `/path/*/abc`可以匹配`/path/a/abc`和`/path/b/abc`等。
- **两个星号**`**`

  和一个星号类似，区别是可以跨路径边界，一般用来匹配多级目录。例如：`/path/**/abc`可以用来匹配`/eventkey/a/abc`、`/eventkey/b/abc`、`/eventkey/a/b/abc`、`/eventkey/a/b/c/abc`等。
- **大括号**`{}`

  大括号用来指定一个子模式匹配集合，例如：`{sun,moon,stars}`可以匹配 `sun`、`moon``starts`，`{temp*, tmp*}`可以匹配任何以 `temp`和`tmp`开头的字符串。

如果你需要按需订阅审批事件，参考如下**审批事件**示例：

| **事件类型** | **描述** | **规则说明** | **示例值** |
| --- | --- | --- | --- |
| **审批任务开始/结束/取消** | 针对某个业务分类下特定审批模板的任务开始、结束或取消事件。 | `/v1.0/event/bpms_task_change/bizCategoryId/{bizCategoryId}/processCode/{processCode}/type/{type}` | `/v1.0/event/bpms_task_change/bizCategoryId/{bizCategoryId}/processCode/PROC-EA*****F-885E-47AA-AEB9-8F59CB10E309/type/start` |
| 某个审批模板下的任务开始、结束或取消事件，直接使用审批模板代码`processCode`进行事件匹配。 | `/v1.0/event/bpms_task_change/processCode/{processCode}/type/{type}` | `/v1.0/event/bpms_task_change/processCode/PROC-EA*****F-885E-47AA-AEB9-8F59CB10E309/type/start` |
| **审批实例开始/结束/终止** | 针对某个业务分类下特定审批模板的实例开始/结束/终止事件。 | `/v1.0/event/bpms_instance_change/bizCategoryId/{bizCategoryId}/processCode/{processCode}/type/{type}` | `/v1.0/event/bpms_instance_change/bizCategoryId/{bizCategoryId}/processCode/PROC-EA*****F-885E-47AA-AEB9-8F59CB10E309/type/start` |
| 某个审批模板下的实例开始、结束或终止事件，直接使用审批模板代码`processCode`进行事件匹配。 | `/v1.0/event/bpms_instance_change/processCode/{processCode}/type/{type}` | `/v1.0/event/bpms_instance_change/processCode/PROC-EA*****F-885E-47AA-AEB9-8F59CB10E309/type/start` |

相关参数信息，请参考[审批实例开始、结束、终止、删除](0039-event-bpms-instance-change.md)。
