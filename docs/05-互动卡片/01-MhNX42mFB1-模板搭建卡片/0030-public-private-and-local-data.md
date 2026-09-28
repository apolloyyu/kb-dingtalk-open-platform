---
title: "公有、私有和本地数据"
source_url: "https://open.dingtalk.com/document/development/public-private-and-local-data"
namespace: "development"
slug: "public-private-and-local-data"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 绑定卡片变量 > 公有、私有和本地数据"
doc_id: "66rxeYtyEY"
updated_at: "2026-08-05 09:10:20"
---

> Source: https://open.dingtalk.com/document/development/public-private-and-local-data
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 绑定卡片变量 > 公有、私有和本地数据
> Updated: 2026-08-05 09:10:20

# 公有、私有和本地数据

通过本文你可以了解到公有数据、私有数据、本地数据三种模拟数据类型以及它们的区别。

> **[!NOTE]**
>
> 在阅读本文档之前，确保你已经完成了以下的准备工作：
>
> - 了解数据源面板中的 Mock 数据面板的相关操作，参见[数据源面板](0024-outline-tree-panel.md#aa650d08c1k6k)。

## **背景介绍**

在卡片模板搭建器中无真实服务端下发的卡片数据时，需通过变量数据模拟和变量绑定来[展示动态化内容](0026-binding-variables.md)。

> **[!NOTE]**
>
> Mock 数据面板支持三种数据类型的模拟：公有数据、私有数据和本地数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550495.png)

## **数据对比**

| **数据类型** | **可见范围** | **对应变量类型** | **优先级** | **在搭建器中模拟** | **通过 API 传入** |
| --- | --- | --- | --- | --- | --- |
| 公有数据 | 所有人可见 | 普通变量（公有） | 低 | ✓ | [卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md) |
| 私有数据 | 仅自己可见 | 普通变量（私有） | 高 | ✓ | [卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md) |
| 本地数据 | 仅自己可见 | 本地变量 | 不适用（临时数据） | ✓ | ✗ |

- **公有数据**：所有用户共享的数据，适用于大多数无"千人千面"诉求的场景。
- **私有数据**：针对用户自身定制的数据，优先级高于公有数据。若私有数据中获取不到值，会从公有数据中获取。
- **本地数据**：仅保存在当前客户端会话中的临时数据，卡片下发时为空，切换会话后重置，不支持通过 API 传入。

下面分别介绍三种数据的创建和使用方法。

## **公有数据**

公有数据是所有用户共享的数据，服务于普通公有变量。

创建公有变量及模拟数据步骤：

1. 未开启「私有化」开关创建的变量即为公有变量，适用于大多数无"千人千面"诉求的场景。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550503.png)
2. 在 Mock 数据面板中编写该变量的公有数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550514.png)
3. 使用组件绑定该变量，即可在模拟器中看到实时预览效果。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550517.png)

## **私有数据**

私有数据是针对用户自身定制的数据，仅用户本人可见。其优先级高于公有数据，渲染时若私有数据中获取不到对应值，会尝试从公有数据中获取。

将 `str` 转为私有变量并模拟私有数据：

1. 将`str`变量进行私有化。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550518.png)
2. 私有化后，在 Mock 数据面板中为该变量编写私有数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550522.png)
3. 模拟器中的 `public string` 已转变为 `private string`。虽然同时编写了 `str` 的公有数据和私有数据，但最终按私有数据显示，说明私有数据优先级高于公有数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550526.png)

## **本地数据**

与公有数据和私有数据不同，公有数据和私有数据服务普通变量，本地数据则服务本地变量。本地变量仅保存在当前客户端会话中，卡片下发时为空，切换会话后会重置，无法通过服务端下发默认值。

以简单例子展示本地变量和本地数据的运作：

1. 创建本地变量`local` 。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550557.png)
2. 编写该变量的本地数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550558.png)
3. 使用**选择框**组件绑定该本地变量。

   > **[!NOTE]**
   >
   > 目前能操作本地变量的组件只有**选择框**组件

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550561.png)
4. 修改**选择框**组件的点击事件为更新本地变量`local` 。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p550565.png)
5. 进入预览模式，单击**选择框**即可更新本地数据（布尔值取反）。如下图，选择框的选中状态随点击切换。

   ![local_var](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0222985871/p517529.png)
