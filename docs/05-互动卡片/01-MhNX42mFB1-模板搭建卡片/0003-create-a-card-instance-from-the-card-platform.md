---
title: "卡片平台创建卡片实例"
source_url: "https://open.dingtalk.com/document/development/create-a-card-instance-from-the-card-platform"
namespace: "development"
slug: "create-a-card-instance-from-the-card-platform"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "快速入门 > 卡片创建 > 卡片平台创建卡片实例"
doc_id: "LNVaBX7DGY"
updated_at: "2026-08-04 09:07:20"
---

> Source: https://open.dingtalk.com/document/development/create-a-card-instance-from-the-card-platform
> Path: 互动卡片 / 模板搭建卡片 / 快速入门 > 卡片创建 > 卡片平台创建卡片实例
> Updated: 2026-08-04 09:07:20

# 卡片平台创建卡片实例

通过本文你将了解到如何创建一个包含静态数据和动态数据的卡片实例。

## **核心概念**

互动卡片是由**卡片模板**和**卡片数据**构成的， 创建卡片实例是将卡片模板和卡片数据关联起来进行**实例化**的过程，完成创建后即可针对卡片实例进行更多的操作（如：投放）。

## **前置准备**

在创建卡片实例之前，确保你已经完成：

- 在卡片平台上完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)。

## **步骤一：进入卡片实例管理页面**

1. 登录[开发者后台 > 卡片平台](https://open-dev.dingtalk.com/fe/card)。
2. 选择卡片， 单击「查看」进入卡片模板搭建页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p539888.png)

   > **[!NOTE]**
   >
   > 本示例使用的是消息卡片，你可以在新建模板中选择卡片类型为消息卡片。
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p547943.png)
   >
   > 在编辑页面左边的预设模板中选择使用「小程序卡片」。
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p548001.png)
   >
   > 本文在介绍如何使用动态数据源时会使用到图表变量。你可以在组件库中将图表组件拖动到模拟器中，然后点击右侧图表数据创建一个名为「chart」的图表变量。
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p548006.png)
   >
   > 至此你就完成了示例卡片的搭建，接下来即可发布模板并进入下一步骤
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p548009.png)
3. 单击右上角的「卡片实例管理」**，**进入卡片实例管理页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p521498.png)

> **[!IMPORTANT]**
>
> 需要先完成卡片模板的发布才能进入卡片实例管理页面。
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p521497.png)

## **步骤二：创建卡片实例**

进入卡片实例管理页面，单击页面左上角的「创建卡片实例**」**按钮，进入表单填写界面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p521510.png)

在此步骤中，你需要进行以下操作：

- **完成数据配置**：为卡片的变量配置数据来源
- **填写场域信息**：配置卡片所要投放的场域

### **完成数据配置**

卡片的数据分为静态和动态两种类型的数据。 这两种类型的数据主要有数据的获取时机和更新机制两方面的不同。

|  | **获取时机** | **更新方式** |
| --- | --- | --- |
| **静态数据** | 卡片实例化 | 通过服务端接口 |
| **动态数据** | 卡片渲染时获取，在实例化时只保存配置信息 | 由数据拉取配置决定 |

下面将介绍如何对静态数据和动态数据进行绑定。

#### **绑定静态数据**

对于卡片的每一个变量都可以绑定静态数据。 以变量 **content** 为例，选择数据类型为**静态数据**即可在数据一览中输入变量的实际内容。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p521613.png)

更新完静态数据后，右侧的模拟器会根据绑定的数据实时地展示预览效果，可以参考预览效果来检查和调整卡片的数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p523527.png)

#### **绑定动态数据**

在绑定动态数据之前需要先创建动态数据源， 目前卡片平台支持以下两种动态数据源：

- 数据资产平台数据源
- 开放平台连接器数据源

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p533034.png)

以数据资产平台数据源为例，选中后会出现如下图所示的数据源配置表单。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3962293761/p533041.png)

表单中各字段的含义如下表所示：

|  | **字段说明** | | **示例值** |
| --- | --- | --- | --- |
| **数据服务** | 数据资产平台提供的数据服务 | | 折线测试服务 |
| **数据拉取策略** | 轮询拉取 | 卡片在钉钉上运行时每隔一定时间会重新获取一次数据 | 轮询拉取 |
| 一次性拉取 | 卡片首次在钉钉上运行时会获取一次数据 |
| **轮询时间** | 卡片重新获取数据的时间间隔 | | 6 |
| **轮询时间单位** | 卡片重新获取数据的时间间隔单位（秒、分钟、小时） | | 秒 |

完成表单项的填写并点击「新增」即可创建一个动态数据源配置项。

如下图所示，新增的动态数据源配置，可以从上面了解到**数据源的名称**、**ID** 以及**数据类型**等基本信息。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p533064.png)

接着可以进行数据源的绑定。 因为我们创建的是`chart` 类型的数据源， 所以我们需要选择一个图表类型的变量来绑定这个动态数据源。如下图所示，找到图表变量 **chart** ，为其配置数据类型为**动态数据源**，在数据项选择创建的**折线测试服务**。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3962293761/p533085.png)

绑定完成后即可在右侧看到如下图所示的预览效果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p533092.png)

### **2. 填写场域信息**

除了卡片本身的数据之外， 还需要填写场域所需要的数据才能让卡片在对应场域中流通。 目前卡片支持 IM 、工作台等场域。 特定类型的卡片只能在对应场域中使用，而标准卡片可以在所有场域中使用。

本文示例使用的卡片是**消息卡片**，所以我们需要创建 IM 场域（群聊/单聊）的配置。单击「场域配置」一栏中的「新增场域」按钮选择场域并填写场域配置信息：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p523544.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p523617.png)

下表所示为 IM 场域投放的参数说明

|  | **说明** | **示例值** |
| --- | --- | --- |
| **是否需要鉴权** | 卡片是否要开启酷应用的鉴权 | 否 |
| **LastMessage** | 卡片发送到 IM 里时，会话列表展示的缩略信息image | 测试卡片 |
| **是否支持转发** | 卡片在 IM 中能否被转发 | 否 |

填写完**IM 场域**的配置信息后就可点击「创建实例按钮完成一个卡片实例的创建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p523633.png)

## **步骤三：查看卡片实例列表**

可以在**实例列表**一栏中查看历史创建的卡片实例列表。通过实例列表你可以了解到卡片的 bizId、创建时间、修改时间和场域信息，并可以点击右侧的**投放**按钮完成卡片的投放。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p523638.png)
