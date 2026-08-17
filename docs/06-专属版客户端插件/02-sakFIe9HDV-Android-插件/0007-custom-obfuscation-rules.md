---
title: "配置混淆规则"
source_url: "https://open.dingtalk.com/document/development/custom-obfuscation-rules"
namespace: "development"
slug: "custom-obfuscation-rules"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 配置混淆规则"
doc_id: "hHrlX31iI7"
updated_at: "2025-10-15 17:02:00"
---

> Source: https://open.dingtalk.com/document/development/custom-obfuscation-rules
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 配置混淆规则
> Updated: 2025-10-15 17:02:00

# 配置混淆规则

专属钉钉Release打包时会统一执行混淆加固，假如你的代码里使用反射、gson等，需要补充混淆规则，否则可能会出现**调试环境功能正常但Release集成版本功能异常**的现象。

## **配置混淆规则**

钉钉 Bundle 工程默认创建了 consumer-rules.pro 文件，可使用 Dingtalk DevKit 工具打开该 proguard 文件，然后补充必要的混淆规则。如下图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2207553661/p488943.png)

钉钉在构建时，会合并 consumer-rules.pro 文件中的 Keep 规则，然后集成打包。

> **[!WARNING]**
>
> 请务必不要添加通用规则，钉钉平台已经定义基础混淆规则，仅补充自研代码相关混淆规则即可。同时为了避免出现异常，钉钉插件构建脚本会扫描当前工程以及所依赖的aar，可能会提示proguard规则冲突导致的打deb失败，请根据提示移除非必要的混淆规则。
>
> 编译异常示例：
>
> Execution failed for task ':lib-bundle:publishBundle'.
>
> > Proguard rules below are not allowed in dingtalk platform, please remove the following rules!!
>
> lib-bundle-release.aar:
>
> -keep class com.alibaba.\*\*
>
> -dontusemixedcaseclassnames
