---
title: "概述"
source_url: "https://open.dingtalk.com/document/dingstart/dashboard-overview-workbench"
namespace: "dingstart"
slug: "dashboard-overview-workbench"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 概述"
doc_id: "cVk5d3rQPe"
updated_at: "2025-10-20 17:23:24"
---

> Source: https://open.dingtalk.com/document/dingstart/dashboard-overview-workbench
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 概述
> Updated: 2025-10-20 17:23:24

# 概述

一个组件有一个完整的业务功能，包含视图和逻辑，作为定制工作台的一部分，可以被定制工作台设计者拖入到工作台中使用。定制服务可根据需要开发工作台组件。

## 工作台插件

插件是定制工作台组件的载体，一个插件里可以包含多个定制工作台组件（建议10个以内），具体哪些组件归属于一个插件可以按项目情况由开发者自行决定。

钉钉工作台插件是一组小程序组件的集合，用于嵌入到钉钉工作台中使用。每个组件可以在工作台设计器中独立使用，也可以通过工作台小程序提供的SDK事件通道进行联动。当为多个客户设计钉钉工作台时，可使用同一套插件提供的组件，无需重复开发。

下图展示了自建组件开发的全流程。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5594440071/p739251.png)

## **数据源**

> **[!IMPORTANT]**
>
> 数据源归属于服务商企业，工作台和模板上的组件配置的数据源直接指向服务商企业数据源。因此数据源的任何变更会实时影响到所有组件的调用，需要谨慎修改。

在模板生成工作台和定制工作台时，系统会将模板或定制工作台里用到的服务商企业的数据源，自动授权给客户企业访问。

> **[!NOTE]**
>
> - 新增或变更数据源将会在 10 分钟之内生效。
> - 如果新增的数据源是提供给官方的资讯组件使用，返回的数据结构必须符合规范。详情请参考[官方组件数据格式](0014-qbmg52.md)。
> - 数据源指向的接口需要确保响应时间在 3s 内，否则会被当作响应超时。

![数据源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3751522161/p132873.png)

注册后的数据源，可以在服务商视角的设计器的数据源选择器中选择使用。也可以在 config.json 中的 dataSources 字段中使用。

![数据源选择 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3751522161/p132880.png)
