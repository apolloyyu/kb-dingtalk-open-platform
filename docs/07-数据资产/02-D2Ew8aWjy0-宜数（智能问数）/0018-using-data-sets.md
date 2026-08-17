---
title: "使用数据集"
source_url: "https://open.dingtalk.com/document/aipass/using-data-sets"
namespace: "aipass"
slug: "using-data-sets"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "数据工厂 > 使用数据集"
doc_id: "GEfYKldBmd"
updated_at: "2026-08-14 09:26:58"
---

> Source: https://open.dingtalk.com/document/aipass/using-data-sets
> Path: 数据资产 / 宜数（智能问数） / 数据工厂 > 使用数据集
> Updated: 2026-08-14 09:26:58

# 使用数据集

> **[!NOTE]**
>
> 当前**高级版**可使用。

## **概述**

通过数据工厂创建出的数据集，可以在各个功能内（问数助理、互动大屏、自定义仪表盘、数据API）进行消费。

## **场景一：问数助理使用数据集**

### **使用效果**

![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7145754371/p889062.gif)

### **搭建流程**

1. 在数据工厂中，加工宜搭数据集，选择宜搭数据源中“设备维修工单” 表单，并与在其他数据源中的维表进行关联。

   ![1e5f8052-35cd-428c-be24-9ea1e1e82800](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890656.gif)
2. 进入钉钉工作台，选择宜数（智能问数）产品，单击“创建” 新的问数助理。

   ![创建问数助理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890016.png)
3. 在“数据管理”中，添加数据集，选择“数据资产平台”，然后选择数据工厂的宜搭数据集，配置维度，字段描述等相关信息后即可进行问数。

   ![f723e5d3-ae0e-41e5-9b1f-5b7ab9d14f57](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890657.gif)

## **场景二：互动大屏使用数据集**

### **使用效果**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890660.png)

### **搭建流程**

1. 登录[数据资产平台>数据看版>高级数据大屏](https://open-dev.dingtalk.com/fe/daas?hash=%23%2FdataScreen#/dataScreen)。
2. 新建数据大屏，创建组件（以柱状图为例）。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p889047.png)
3. 柱状图配置：

   - 数据源：单击添加，数据域选择自有数据，按用户配置的数据集选择业务场景和数据表。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890662.png)
   - 维度：即柱状图横轴。平台将业务日期自动生成日、周、月三个维度，其他字段不变。
   - 指标：即柱状图纵轴，选择数值类型的字段。
   - 数据时间范围：按数据集的业务日期字段计算，只统计所选时间范围的数据。
   - 其他：按需配置。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890663.png)
4. 单击确认，即可完成状态图的配置。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890665.png)

## **场景三：自定义看版使用数据集**

### **使用效果**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3870954371/p890666.png)

### **搭建流程**

1. 登录[数据资产平台>数据看板>自定义仪表盘](https://open-dev.dingtalk.com/fe/daas#/myDashboard)。
2. 新建仪表盘。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890668.png)
3. 创建组件（以柱状图为例）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890669.png)
4. 柱状图配置：

   - 数据源：单击添加，数据域选择自有数据，按用户配置的数据集选择业务场景和数据表。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890670.png)
   - 维度：即柱状图横轴。平台将业务日期自动生成日、周、月三个维度，其他字段不变。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890671.png)
   - 指标：即柱状图纵轴，选择数值类型的字段。
   - 数据时间范围：按数据集的业务日期字段计算，只统计所选时间范围的数据。
   - 其他：按需配置。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890672.png)
5. 保存&发布。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p890673.png)

## **场景四：数据API**使用数据集

1. 登录[数据资产平台](https://open-dev.dingtalk.com/fe/daas#/myDashboard)
2. 单击数据服务菜单，选择数据API ，单击自有数据，选择数据工厂中加工的数据集，勾选相应字段，即可完成数据API的创建。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8180766871/p889050.png)
