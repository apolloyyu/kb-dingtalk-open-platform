---
title: "扩展点概述"
source_url: "https://open.dingtalk.com/document/development/harmonyos-extension-points-overview"
namespace: "development"
slug: "harmonyos-extension-points-overview"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "使用扩展点 > 扩展点概述"
doc_id: "QRhtTrcMfA"
updated_at: "2026-08-14 17:50:58"
---

> Source: https://open.dingtalk.com/document/development/harmonyos-extension-points-overview
> Path: 专属版客户端插件 / HarmonyOS 插件 / 使用扩展点 > 扩展点概述
> Updated: 2026-08-14 17:50:58

# 扩展点概述

## **什么是扩展点**

钉钉客户端平台通过扩展点的方式，允许开发者在钉钉基础上自定义功能和行为，以此完成定制需求的开发。

扩展点本质上是一个接口类，开发者可以实现相关接口完成扩展实现类的开发。钉钉框架会将扩展实现类注册到钉钉平台中并在特定时机回调。基于扩展点，开发者可以实现扩展菜单项（比如首页加号）、设置项、新增登录流程节点等。通过多个扩展点的组合使用，可以实现比如VPN、安全沙箱等场景的专属插件。

![开放文档画图-流程图.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0252489961/p715759.png)

## **常见使用场景**

- 如果开发的插件期望在打开钉钉后，能够自动连接企业内网，建议你关注**首页生命周期扩展点**。
- 如果开发的插件期望在登录前能够连接企业内网，建议关注**登录流程扩展点**。
- 如果开发的插件期望对用户登录增加额外认证流程（比如短信验证），建议关注**登录认证扩展点**。
