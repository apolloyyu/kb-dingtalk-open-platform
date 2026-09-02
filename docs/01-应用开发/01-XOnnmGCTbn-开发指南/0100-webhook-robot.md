---
title: "Webhook 机器人"
source_url: "https://open.dingtalk.com/document/dingstart/webhook-robot"
namespace: "dingstart"
slug: "webhook-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > Webhook 机器人"
doc_id: "teOxfuRavP"
updated_at: "2025-09-03 15:56:51"
---

> Source: https://open.dingtalk.com/document/dingstart/webhook-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > Webhook 机器人
> Updated: 2025-09-03 15:56:51

# Webhook 机器人

如果你仅需要发送消息的能力，并仅限于从 GitLab、GitHub、JIRA、阿里云 Codeup 和 Travis 推送消息到钉钉群内。你可以依据本文档操作步骤完成接入。

## **操作步骤**

1. 打开钉钉客户端，进入指定群，单击群设置。
2. 单击**群管理** > **机器人** > 添加机器人。
3. 选择合适的机器人进行添加：

   - **阿里云 Codeup 机器人**：阿里云持续交付平台提供的代码托管服务。
   - **GitHub 机器人**：基于Git的代码托管服务。
   - **极狐 GitLab 机器人**：基于ROR的开源代码托管软件。
   - **JIRA 机器人**：出色的项目与事务跟踪工具。
   - **Travis 机器人**：出色的项目与事务跟踪工具。
4. 获取机器人 Webhook 地址。
5. 复制 Webhook 地址到对应产品空间：

   - 阿里云 Codeup 机器人，详情参考 [Webhook 配置说明](https://help.aliyun.com/document_detail/324267.html)。
   - GitHub 机器人，详情参考[创建 Webhook](https://docs.github.com/zh/webhooks/using-webhooks/creating-webhooks#creating-a-repository-webhook)。
   - 极狐 GitLab 机器人，详情参考 [在 GitLab 中配置 Webhook](https://docs.gitlab.cn/jh/user/project/integrations/webhooks.html#%E5%9C%A8%E6%9E%81%E7%8B%90gitlab-%E4%B8%AD%E9%85%8D%E7%BD%AE-webhook)。
   - JIRA 机器人，详情参考 [Managing webhooks](https://confluence.atlassian.com/adminjiraserver/managing-webhooks-938846912.html)。
   - Travis 机器人，详情参考 [Configuring webhook notification](https://docs.travis-ci.com/user/notifications#configuring-webhook-notifications)。
