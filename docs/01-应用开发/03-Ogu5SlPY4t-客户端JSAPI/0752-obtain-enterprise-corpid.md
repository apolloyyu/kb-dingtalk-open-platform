---
title: "获取企业CorpId"
source_url: "https://open.dingtalk.com/document/development/obtain-enterprise-corpid"
namespace: "development"
slug: "obtain-enterprise-corpid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > 获取企业CorpId"
doc_id: "hNp3Y3jmT7"
updated_at: "2025-09-17 20:57:39"
---

> Source: https://open.dingtalk.com/document/development/obtain-enterprise-corpid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > 获取企业CorpId
> Updated: 2025-09-17 20:57:39

# 获取企业CorpId

本文介绍了H5微应用获取企业CorpId的流程。

## H5微应用

在应用首页地址和PC端首页地址中使用$CORPID$做为参数占位符，当用户在工作台打开应用时，钉钉容器会将$CORPID$替换为当前访问用户的企业CorpId。

> **[!IMPORTANT]**
>
> 只有在钉钉工作台打开应用，才能将$CORPID$动态解析为企业CorpId。

### 示例

如下图所示，登录**开发者后台** > **找到对应应用** > **基础信息** > **开发管理**页面，将应用首页地址和PC端首页地址设置为`https://mm.vaiwan.cn/view/*******?corpId=$CORPID$`。![第三方企业首页地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7822622561/p434182.png)

用户在工作台打开应用时，会将CorpId替换。例如，企业CorpId是CorpId12345，替换后的地址为`https://mm.vaiwan.cn/view/*******?corpId=ding9f***********`。

在PC端和移动端打开效果相同。以移动端为例，打开效果如下图所示：![移动端获取CorpId2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7822622561/p434190.png)
