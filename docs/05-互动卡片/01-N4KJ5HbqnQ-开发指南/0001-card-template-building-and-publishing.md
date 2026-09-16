---
title: "普通卡片模板"
source_url: "https://open.dingtalk.com/document/development/card-template-building-and-publishing"
namespace: "development"
slug: "card-template-building-and-publishing"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片模板搭建 > 普通卡片模板"
doc_id: "oV5zN4vacY"
updated_at: "2026-08-04 09:07:18"
---

> Source: https://open.dingtalk.com/document/development/card-template-building-and-publishing
> Path: 互动卡片 / 开发指南 / 卡片模板搭建 > 普通卡片模板
> Updated: 2026-08-04 09:07:18

# 普通卡片模板

通过本文你将了解到如何创建互动卡片的模板以及如何进行模板的搭建。

> **[!NOTE]**
>
> 在搭建卡片模板之前，确保你已经完成了以下的准备工作：
>
> - 成为钉钉开发者，详情参见[成为钉钉开发者](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。

互动卡片是由**卡片模板**和**卡片数据**构成的，卡片模板决定了卡片的结构，卡片数据则决定了卡片展示的具体内容，在使用互动卡片之前需要先准备一个卡片模板，具体需要经过以下步骤。

## **步骤一：创建卡片模板**

1. 前往[开发者后台 > 卡片平台](https://open-dev.dingtalk.com/fe/card)。
2. 进入**新建模板**页面，并填写**模板名称**、[卡片类型](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0777-overview-card.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365085871/p512421.png)
3. 关联[钉钉应用列表](https://open-dev.dingtalk.com/fe/app#/corp/app)中的应用（可选）。

   ![iShot_2022-11-04_15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365085871/p512674.png)

   关联应用后在**应用详情页** > **酷应用** > **扩展到群会话** > **功能设计**中对应类型的卡片模板列表可见，如图

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365085871/p512439.png)
4. 点击「创建」按钮即可创建模板，创建模板后即可查看该卡片模板的模板 ID。

   > **[!NOTE]**
   >
   > 后续发送卡片消息流程中接口将会使用模板ID。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365085871/p513011.png)

## **步骤二：搭建卡片模板**

1. 进入**模板列表**页面，即可看到创建的卡片模板。单击卡片模板上的「编辑**」**按钮，即可进入卡片模板搭建器进行编辑。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365085871/p513012.png)
2. 在卡片模板搭建器（如下图）中，可以通过拖拉拽的方式对卡片模板进行搭建，详情参见[卡片模板搭建器](../03-MhNX42mFB1-模板搭建器/0001-card-template-overview.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365085871/p512504.png)

## **步骤三：卡片模板发布**

当卡片模板搭建完成时，即可点击「发布」按钮对模板进行发布操作，发布完成后即可进行后续卡片实例的创建以及投放等流程，真正将卡片发送出来。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0582293761/p547784.png)

> **[!IMPORTANT]**
>
> 卡片模板发布成功后将无法再次修改，请谨慎操作。
