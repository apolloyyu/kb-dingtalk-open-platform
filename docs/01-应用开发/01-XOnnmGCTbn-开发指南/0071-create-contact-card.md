---
title: "创建通讯录卡片"
source_url: "https://open.dingtalk.com/document/dingstart/create-contact-card"
namespace: "dingstart"
slug: "create-contact-card"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发成员资料页酷应用 > 创建通讯录卡片"
doc_id: "JjbY2ieL2K"
updated_at: "2026-06-30 09:01:03"
---

> Source: https://open.dingtalk.com/document/dingstart/create-contact-card
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发成员资料页酷应用 > 创建通讯录卡片
> Updated: 2026-06-30 09:01:03

# 创建通讯录卡片

本文档指导开发者如何在钉钉开放平台创建通讯录卡片

## **操作步骤**

1. 登录[卡片平台](https://open-dev.dingtalk.com/fe/card)，进入卡片模板管理页面。

   > **[!NOTE]**
   >
   > 该平台用于搭建和预览自定义卡片样式，支持可视化编辑与代码模式
2. 单击**新建卡片模板**，进入新模板创建向导界面

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3621872871/p517289.png)
3. 设置卡片模板信息，完成创建。

   - 输入模板名称与描述
   - 在类型选择中，**必须选择“通讯录卡片”**
   - 关联应用选择已经创建好的应用

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3621872871/p517291.png)

   创建完成后，即可自定义设计通讯录卡片。
4. 设计卡片内容布局：

   - 使用拖拽组件或 JSON 编辑器构建 UI 结构
   - 所有容器组件需设置明确的高度值（例如 height: "200px"），卡片高度**必须定高**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3621872871/p517295.png)
5. 完成设计后保存模板，并发布上线。
6. 在钉钉客户端验证效果，查看目标成员详情页是否正确渲染卡片。
