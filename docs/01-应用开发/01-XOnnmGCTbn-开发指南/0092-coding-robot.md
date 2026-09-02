---
title: "CODING机器人"
source_url: "https://open.dingtalk.com/document/dingstart/coding-robot"
namespace: "dingstart"
slug: "coding-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > CODING机器人"
doc_id: "VFsmURkrQO"
updated_at: "2025-09-25 21:05:04"
---

> Source: https://open.dingtalk.com/document/dingstart/coding-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > CODING机器人
> Updated: 2025-09-25 21:05:04

# CODING机器人

## 生成 CODING 机器人 Webhook

从 PC 端或者手机端的群机器人入口进入到机器人管理页面，选择「CODING 机器人」，按照设置流程生成 CODING 机器人，即可获取到相应群的 Webhook，其格式如下：

```
https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx
```

## 在 CODING 中设置项目的 Webhook

1. 进入你的 CODING 项目，依次点击左侧「设置」>「Webhook」> 「新建 Webhook」来添加 Webhook![resize,w_1500 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1924199951/p131243.png)
2. 填入 Webhook 地址，内容格式选择「钉钉」，内容类型选择「application/json」，勾选相应的监听事件，点击「新建 Webhook」按钮即可![resize,w_1500 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1924199951/p131244.png)

立即去配置：<https://coding.net>
