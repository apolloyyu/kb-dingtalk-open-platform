---
title: "介绍"
source_url: "https://open.dingtalk.com/document/dingstart/introduction-to-dingtalk-sharing"
namespace: "dingstart"
slug: "introduction-to-dingtalk-sharing"
group: "应用开发"
tab: "开发指南"
breadcrumb: "接入移动客户端 > 接入钉钉分享 > 介绍"
doc_id: "PwqwfjBkrD"
updated_at: "2026-07-22 16:55:34"
---

> Source: https://open.dingtalk.com/document/dingstart/introduction-to-dingtalk-sharing
> Path: 应用开发 / 开发指南 / 接入移动客户端 > 接入钉钉分享 > 介绍
> Updated: 2026-07-22 16:55:34

# 介绍

## 使用场景

某员工在社交媒体软件上看到一篇非常赞的文章，并希望将这篇文章分享给到企业钉钉群中。在这个场景中就会使用到分享SDK的功能。为了便于大家理解，我们通过交互示例来说明：

下图是支付宝“生活号”中的一篇文章，分享给钉钉好友场景，钉钉好友可以在钉钉内打开被分享的内容。其中从支付宝分享到钉钉的过程中就使用到分享的SDK。

![iShot2022-09-20 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4350174871/p492516.png)

## 版本要求

如果分享人的钉钉版本低于2.7，则会引导分享人升级钉钉，升级后便可正常分享。

如果分享人手机上没有安装钉钉，那么分享人点击分享到钉钉时，会引导分享人下载钉钉。

- iOS：引导跳转至AppStore。
- Android： 引导至http://www.dingtalk.com/index.html。

## 使用说明

> **[!NOTE]**
>
> 钉钉分享只支持企业内部应用接入，不支持第三方企业应用接入。

当您的应用需要使用钉钉分享时，需要先在[开发者后台](https://open-dev.dingtalk.com/#/shareMan)创建应用，配置相关内容才可以使用钉钉分享，具体使用流程请参考[分享接入流程](0102-mini-app-access.md)。
