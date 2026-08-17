---
title: "创建数据源"
source_url: "https://open.dingtalk.com/document/aipass/create-a-data-source"
namespace: "aipass"
slug: "create-a-data-source"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "数据工厂 > 创建数据源"
doc_id: "HzlEb891Qs"
updated_at: "2026-08-14 09:26:54"
---

> Source: https://open.dingtalk.com/document/aipass/create-a-data-source
> Path: 数据资产 / 宜数（智能问数） / 数据工厂 > 创建数据源
> Updated: 2026-08-14 09:26:54

# 创建数据源

> **[!NOTE]**
>
> 当前功能属于**高级版**。

## **概述**

在数据工厂里使用数据的前提是将自有数据库注册为数据工厂中的数据源，目前数据工厂支持Mysql 及Postgres 两大类生态的数据库。

| **名词** | **说明** |
| --- | --- |
| **数据源** | 指读取数据的来源。可以是Mysql、Hologres等数据库 |
| **数据集** | 指数据的集合，由字段组成。可以通过拖拽或JOIN数据库内的表字段，或者提前定义字段，再由连接器产出数据。 |
| **Hologres** | 指阿里一站式实时数据仓库引擎，支持海量数据实时写入、实时更新、实时分析，支持标准SQL（兼容PostgreSQL协议），支持PB级数据多维分析。 |
| **连接器** | 指[钉钉连接平台](https://open-dev.dingtalk.com/fe/connector#/myFlow)搭建的连接媒介，就是用简捷的方式实现应用与应用之间的连接。  平台上架了【[数据资产平台](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101A840E5E84213639B7000D?corpId=ding32fff839a3e0105d&gray=1)】的连接器，可以实现用户业务数据安全、快速的上架。 |

## **功能价值**

通过创建数据源，可以实现客户自有数据在钉钉场域内的注册，加工与消费，并可以与钉钉官方数据进行融合分析。

## **适用场景**

企业自有数据在钉钉场域内进行消费-创建数据源：

1. 单击“数据工厂”菜单，选择“数据源管理”，单击“新建数据源”按钮进入选择数据库类型界面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4180766871/p890620.png)
2. 根据自有数据库的类型，选择数据库，单击“下一步”，进行数据源信息录入界面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4180766871/p890621.png)

   目前支持的数据库类型：

   | **数据库** | **说明** |
   | --- | --- |
   | MySQL | 5.7、8.0版本 |
   | PostgreSQL | 8.2及以上版本 |
   | Alibaba AnalyticDB for PostgreSQL | 6.0、4.3版本 |
   | Alibaba Hologres | 数仓版 |
   | Alibaba PolarDB for PostgreSQL | 11.0、14.0版本 |
   | Alibaba PolarDB for MySQL | 5.7、8.0.1、8.0.2版本 |
   | Alibaba AnalyticDB for MySQL | 3.0版本 |
   | Huawei GaussDB | 8.1及以上版本 |
3. 填写数据库的连接信息，包括，名称，描述，连接地址，用户和密码，点击“测试连通性”进行连通性测试，连通性测试成功后，点击“确定”按钮进行保存数据源完成数据源的创建。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4180766871/p889002.png)
