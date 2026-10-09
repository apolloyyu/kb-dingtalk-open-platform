---
title: "绑定变量"
source_url: "https://open.dingtalk.com/document/development/binding-variables"
namespace: "development"
slug: "binding-variables"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 绑定卡片变量 > 绑定变量"
doc_id: "nNCQDkzXi1"
updated_at: "2026-08-05 09:10:15"
---

> Source: https://open.dingtalk.com/document/development/binding-variables
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 绑定卡片变量 > 绑定变量
> Updated: 2026-08-05 09:10:15

# 绑定变量

本文将介绍什么是绑定变量以及如何绑定变量。

## 绑定变量

将数据源面板中定义的变量展示在卡片上，需要在[组件属性设置面板](0024-outline-tree-panel.md#41817b64b84wa)中将组件属性与对应变量绑定。

## **绑定变量的作用**

绑定变量后，卡片渲染时会使用变量的值进行展示。此外，还可结合变量值控制组件显隐（[条件渲染](0028-conditional-rendering-card.md)），或结合数组变量和「循环渲染容器」循环渲染数组项（[循环渲染](0029-loop-rendering.md)）。

## **如何绑定变量**

组件属性设置面板支持两种绑定方式：

- 使用下拉框绑定变量：看到具有「绑定变量」字样的设置器时，选中后即可快速绑定变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5122985871/p550045.png)

  不同属性可绑定的变量类型可能不同。例如「图片圆角」只能绑定数字类型变量。若变量列表中找不到目标变量，很可能是类型不匹配。下图是「单张图片」组件的属性设置面板，图片高度、宽度和圆角三个属性均支持绑定变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5122985871/p550050.png)
- **使用**`${}`**语法绑定变量**：部分设置器（如带帮助图标的文本输入框）支持通过输入 `${}` 来绑定变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5122985871/p550082.png)

  这种方式以字符串输入为基础，可自由拼接字符串和变量。输入 `$` 时，搭建器会自动弹出可用变量列表，选中后自动补充 `{variable}`。也可手动输入 `${变量名}` 绑定。

  > **[!IMPORTANT]**
  >
  > 需要注意的是，如果要使用的变量是对象变量的属性，那么需要通过`${object.property}`的方式来引用；如果在循环渲染容器里面要引用循环项的字段时，需要使用 `${loop.变量名}` 的格式来引用。
