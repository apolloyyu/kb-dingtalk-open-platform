---
title: "条件渲染"
source_url: "https://open.dingtalk.com/document/development/conditional-rendering-card"
namespace: "development"
slug: "conditional-rendering-card"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 绑定卡片变量 > 条件渲染"
doc_id: "e71H0TEQC6"
updated_at: "2026-08-05 09:10:18"
---

> Source: https://open.dingtalk.com/document/development/conditional-rendering-card
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 绑定卡片变量 > 条件渲染
> Updated: 2026-08-05 09:10:18

# 条件渲染

通过本文你将了解到什么是条件渲染以及它的使用场景。

## **内容介绍**

组件的条件渲染指组件仅在满足特定条件（如钉钉环境版本号、变量值判断等）时才显示。

### **适用场景**

需根据变量值展示不同效果时使用条件渲染，如审批卡片中对未处理、已接受、已拒绝三种状态的处理。

### **预期效果**

![compare](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8122985871/p534080.png)

实现简单告警卡片：

- 反馈数小于 10 时，展示橙色「**告警**」标签。
- 反馈数大于等于 10 时，展示红色「**危险**」标签。

## **步骤一：布局搭建**

布局较简单，从大纲树描述：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8122985871/p550569.png)

- 使用 1:1 布局容器分割内容。
- 左边容器填充**基础文本**组件展示反馈数。
- 右边容器填充两个标签分别展示**警告**和**危险**。
- 适当调整布局。

## **步骤二：创建与绑定变量**

1. 本例只需设置反馈数一个变量，创建 `count` 数字变量代表反馈数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8122985871/p550571.png)
2. 为左边容器的「基础文本」组件绑定反馈数变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8122985871/p550573.png)

## **步骤三：设置条件**

1. 为**警告**标签设置显示条件：当 `count` 小于 `10` 时展示。

   ![set_tag_show_1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p534091.gif)
2. 为**危险**标签设置显示条件：当 `count` 大于等于 `10` 时展示。

   ![set_tag_show_2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p534092.gif)
3. 进入预览模式后，即可感受反馈数不同时的不同效果。
