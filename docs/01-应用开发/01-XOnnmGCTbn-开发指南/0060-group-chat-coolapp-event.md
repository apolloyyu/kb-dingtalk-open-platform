---
title: "感知群变化（事件订阅）"
source_url: "https://open.dingtalk.com/document/dingstart/group-chat-coolapp-event"
namespace: "dingstart"
slug: "group-chat-coolapp-event"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 开发参考 > 感知群变化（事件订阅）"
doc_id: "IAmirVeF59"
updated_at: "2026-07-21 14:13:30"
---

> Source: https://open.dingtalk.com/document/dingstart/group-chat-coolapp-event
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 开发参考 > 感知群变化（事件订阅）
> Updated: 2026-07-21 14:13:30

# 感知群变化（事件订阅）

如果你想要通过事件订阅的方式感知整个群聊酷应用的变化，你可以依据本文档进行了解。

## **事件分类**

- 酷应用启用

  最先感知到的事件，建议开发者进行数据与群绑定等初始化操作，对用户推送欢迎语和操作指引。
- 群原生事件

  包括添加或删除群成员、群名称变更等，建议开发者在自己的功能中进行数据同步，权限、规则更新。
- 终止类事件

  最后感知到的事件，例如：群解散、酷应用停用，建议开发者进行合理的数据、权限更新。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5956817661/p508752.png)

事件订阅内容，详情参考 [开发 HTTP 模式](../04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md#6d7a5d60ddwgj)和 [开发 Stream 模式（推荐）](../04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md#7c157d52c89et)。
