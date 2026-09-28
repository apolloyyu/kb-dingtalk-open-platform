---
title: "变量与卡片的关系"
source_url: "https://open.dingtalk.com/document/development/relationship-between-variables-and-cards"
namespace: "development"
slug: "relationship-between-variables-and-cards"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 绑定卡片变量 > 变量与卡片的关系"
doc_id: "WkYNgUkQBv"
updated_at: "2026-08-05 09:10:14"
---

> Source: https://open.dingtalk.com/document/development/relationship-between-variables-and-cards
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 绑定卡片变量 > 变量与卡片的关系
> Updated: 2026-08-05 09:10:14

# 变量与卡片的关系

在绑定卡片变量之前，了解变量与卡片的关系，能帮助你更正确地绑定变量。

## **什么是变量**

变量是指不固定的、可复用的值，为卡片提供了动态的数据。如果没有变量，那么卡片将是静态的，即发送的所有卡片都会呈现一样的内容。

变量拥有不同的数据类型，如数字、字符串、布尔值等；同时，每个变量都具备唯一的变量名称，在绑定变量时通过绑定变量的名称来获取对应的数据。

在[数据源面板](0024-outline-tree-panel.md#aa650d08c1k6k)中，我们可以查看当前卡片中所配置的变量信息。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4122985871/p532265.png)

> **[!NOTE]**
>
> 关于变量的创建、编辑等操作请参考[数据源面板](0024-outline-tree-panel.md#aa650d08c1k6k)。

## **变量的作用**

通过[绑定变量](0026-binding-variables.md)，我们能做到：

- **展示变量内容**：绑定变量后，卡片就能使用变量的值来进行展示
- [条件渲染](0028-conditional-rendering-card.md)：结合变量的值来控制组件的显示与隐藏
- [循环渲染](0029-loop-rendering.md)：结合数组变量和「循环渲染容器」组件来循环渲染数组项

## **变量与卡片的关系**

一张互动卡片，是由**一个卡片模板**和**一组卡片数据**结合而成的。所谓卡片模板，就是我们在卡片搭建编辑器中搭建的卡片内容，而卡片的数据就是我们所定义的变量及其对应的值。卡片模板为某些内容提供了数据坑位，卡片会使用卡片数据填充这些坑位得到最终的卡片

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4122985871/p526806.png)

> **[!NOTE]**
>
> 这些坑位如何定义以及填充什么数据，是在搭建卡片模板时自由定义的。上图中模板中的`title`、`type`等就是定义的变量。
