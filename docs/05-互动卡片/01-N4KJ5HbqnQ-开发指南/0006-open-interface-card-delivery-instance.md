---
title: "开放接口投放卡片实例"
source_url: "https://open.dingtalk.com/document/development/open-interface-card-delivery-instance"
namespace: "development"
slug: "open-interface-card-delivery-instance"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片投放 > 开放接口投放卡片实例"
doc_id: "k98iVCLzyc"
updated_at: "2026-08-04 09:07:24"
---

> Source: https://open.dingtalk.com/document/development/open-interface-card-delivery-instance
> Path: 互动卡片 / 开发指南 / 卡片投放 > 开放接口投放卡片实例
> Updated: 2026-08-04 09:07:24

# 开放接口投放卡片实例

通过本文你将了解如何通过开放接口将一张卡片投放到不同的场域中。

## **核心概念**

使用卡片投放接口，可以通过一次调用将同一个卡片实例进行跨场域投放。目前已支持的场域包括：群聊、机器人单聊、人与人单聊、吊顶。

一次投放主要包含 4 个核心要素：

| **要素** | **说明** | **长度限制** |
| --- | --- | --- |
| 卡片实例 ID（outTrackId） | 唯一标识一张卡片，由开发者生成。 | ≤ 100 字符 |
| 统一投放 ID（openSpaceId） | 包含多个开放场域 ID，可以在多次投放中复用。 | ≤ 1000 字符 |
| 卡片场域属性（openSpaceModel） | 同一场域下的公共属性（如通知属性）。 | - |
| 卡片投放属性（openDeliverModel） | 每次投放时的差异化属性（如@人信息）。 | - |

### **卡片实例 ID**

唯一标识一张卡片，由开发者生成并作为入参。在投放卡片时，使用卡片实例id唯一标识一张卡片。

### **统一投放 ID**

在投放接口中，使用 `openSpaceId` 作为统一投放id，一个 `openSpaceId` 包含多个开放场域 id，并且可以在多次投放中复用。`openSpaceId`采用固定协议且支持版本升级，主要由**版本、场域code、场域id**三部分内容组成，其具体协议内容可参见服务端API-[投放卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0781-delivery-card-interface.md)接口。

目前支持的场域以及场域id的含义如下：

| **场域类型** | **场域code** | **场域id** | **场域id含义** |
| --- | --- | --- | --- |
| 人与人单聊 | IM\_SINGLE | openConversationId | 会话id |
| 群聊 | IM\_GROUP | openConversationId | 会话id |
| 机器人单聊 | IM\_ROBOT | 用户id(userId/unionId) | 员工id |
| 吊顶 | ONE\_BOX | openConversationId | 会话id |

> **[!NOTE]**
>
> - 调用创建群会话接口若未保存`OpenConversationId`，可使用`chatId`调用[获取群会话的OpenConversationId](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0745-obtain-group-openconversationid.md)接口获取。
> - `userIdType` 字段填写，请参考[卡片数据与参数配置-userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0790-faq-card.md#8607bdd785avq)。

### **卡片场域属性**

对于同一个卡片实例，在同一个场域下，有一些相同的属性（如IM群聊场域下的通知属性），在投放接口中将这些属性统一定义为卡片的场域属性，一个卡片实例在一个场域下拥有唯一的场域属性。

同时，卡片实例只有设置了某个场域属性，才能被投放至该场域。为卡片设置场域属性有两种方式：

- **创建时设置**：在创建卡片时设置场域属性；
- **调用接口设置**：开放接口提供为卡片设置场域属性的接口，调用[新增或者更新卡片的场域信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0787-add-field-interface.md)接口即可为已经创建的卡片设置某个场域的属性，使其可被投放至该场域中。

### **卡片投放属性**

- 定义每次投放时的差异化属性（如 IM 群聊场域下的@人信息）。
- 在投放接口中将这些属性定义为卡片投放属性。
- 每次投放时需传入对应场域的投放属性。

## **前置准备**

在投放卡片实例之前，确保已经完成如下的准备工作：

- 在卡片平台上完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)。
- 实现完成[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)流程。

## **投放流程**

以 IM 群聊 + 吊顶 双场域投放为例，完整流程如下：

![投放流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5465085871/p538024.png)

1. 调用服务端API-[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0780-interface-for-creating-a-card-instance.md)接口，实现创建卡片实例并获取`outTrackId`。
2. 若卡片未增加场域属性，则需要调用服务端API-[新增或者更新卡片的场域信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0787-add-field-interface.md)接口为卡片配置场域属性。

   HTTP

   ```
   PUT /v1.0/card/instances/spaces HTTP/1.1
   Host:api.dingtalk.com
   x-acs-dingtalk-access-token:String
   Content-Type:application/json

   {
     "outTrackId" : "example_out_track_id",
     "imGroupOpenSpaceModel" : { // 群聊场域属性
       "supportForward" : false, // 是否支持转发
       "lastMessageI18n" : { // 消息lastMessage
         "ZH_CN": "卡片",
         "EN_US": "card"
       },
       "searchSupport" : { // 搜索属性
         "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
         "searchTypeName" : "{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}",
         "searchDesc" : "搜索描述示例"
       },
       "notification" : { // 通知属性
         "alertContent" : "你收到了一个卡片消息",
         "notificationOff" : false
       }
     },
     "topOpenSpaceModel" : { // 吊顶场域
       "spaceType" : "ONE_BOX"
     }
   }
   ```

   Java

   ```
   package com.aliyun.sample;
   import java.util.ArrayList;
   import java.util.List;
   import java.util.Map;

   import com.aliyun.dingtalkcard_1_0.Client;
   import com.aliyun.dingtalkcard_1_0.models.*;
   import com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestCoFeedOpenSpaceModel;
   import com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestTopOpenSpaceModel;
   import com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModelNotification;
   import com.aliyun.teautil.Common.empty;
   import com.aliyun.teautil.models.RuntimeOptions;
   import com.aliyun.tea.*;

   public void appendSpacExample throws Exception {
     List<String> args = Arrays.asList(args_);
     Client client = Sample.createClient();
     AppendSpaceHeaders appendSpaceHeaders = new AppendSpaceHeaders();
     appendSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";

     // 吊顶场域属性
     AppendSpaceRequestTopOpenSpaceModel topOpenSpaceModel = new AppendSpaceRequestTopOpenSpaceModel()
       .setSpaceType("ONE_BOX");

     // 群聊场域属性
     // 通知属性
     AppendSpaceRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new AppendSpaceRequestImGroupOpenSpaceModelNotification()
       .setAlertContent("你收到了一个卡片消息")
       .setNotificationOff(false);
     // 搜索属性
     AppendSpaceRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new AppendSpaceRequestImGroupOpenSpaceModelSearchSupport()
       .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
       .setSearchTypeName("{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}")
       .setSearchDesc("搜索描述示例");
     // lastMessage属性
     Map<String, String> imGroupOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
       new TeaPair("ZH_CN", "卡片"),
       new TeaPair("EN_US", "card"}")
     );
     AppendSpaceRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new AppendSpaceRequestImGroupOpenSpaceModel()
       .setSupportForward(false)
       .setLastMessageI18n(imGroupOpenSpaceModelLastMessageI18n)
       .setSearchSupport(imGroupOpenSpaceModelSearchSupport)
       .setNotification(imGroupOpenSpaceModelNotification);

     String outTrackId = "example_out_track_id";
     AppendSpaceRequest appendSpaceRequest = new AppendSpaceRequest()
       .setOutTrackId("example_out_track_id")
       .setImGroupOpenSpaceModel(imGroupOpenSpaceModel)
       .setTopOpenSpaceModel(topOpenSpaceModel);
     
     try {
       client.appendSpaceWithOptions(appendSpaceRequest, appendSpaceHeaders, new RuntimeOptions());
     } catch (TeaException err) {
       if (!empty(err.code) && !empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!empty(err.code) && !empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```
3. 获取要被投放的场域id，构造`openSpaceId`。

   ```
   // openSpaceId由三部分组成：协议版本、场域类型、场域id，当前版本的格式为：
   dtv1.card://spaceType1.spaceId1;spaceType2.spaceId2

   // 场域类型及场域id见开放场域 id 章节，格式为：
   dtv1.card//im_group.example_open_conversation_id;one_box.example_open_conversation_id;

   // 具体openSpaceId示例：
   dtv1.card//im_group.cidp4Gh*******VCQ==;one_box.cidp4Gh*******VCQ==;
   ```
4. 构造目标场域的投放模型，并统一调用服务端API-[投放卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0781-delivery-card-interface.md)接口，实现卡片投放。

   HTTP

   ```
   POST /v1.0/card/instances/deliver HTTP/1.1
   Host:api.dingtalk.com
   Content-Type:application/json

   {
     "outTrackId" : "example_out_track_id",
     "openSpaceId" : "dtv1.card//im_group.example_conversation;one_box.example_conversation",
     "userIdType" : 1,
     "imGroupOpenDeliverModel" : { // 群聊投放属性
       "robotCode" : "example_robot_code", // 机器人code
       "recipients" : ["example_user_id_1", "example_user_id_2"] // 消息接收者
     },
     "topOpenDeliverModel" : { // 吊顶投放属性
       "expiredTimeMills" : 1665473229000, // 吊顶过期时间,毫秒
       "userIds" : ["example_user_id_3", "example_user_id_4"], // 可以看到吊顶的用户
       "platforms" : ["android", "ios", "win", "mac"] // 可以看到吊顶的设备
     }
   }
   ```

   Java

   ```
   package com.aliyun.sample;

   import java.util.ArrayList;
   import java.util.List;

   import com.aliyun.dingtalkcard_1_0.models.*;
   import com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImGroupOpenDeliverModel;
   import com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestCoFeedOpenDeliverModel;
   import com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestTopOpenDeliverModel;
   import com.aliyun.teautil.Common.empty;
   import com.aliyun.teautil.models.RuntimeOptions;
   import com.aliyun.tea.*;

   public void buildOpenDeliverModelAndDeliverCard() {
       // 群聊投放属性
       DeliverCardRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new DeliverCardRequestImGroupOpenDeliverModel()
           .setRobotCode("example_robot_code") // 机器人code
           .setRecipients(Arrays.asList("example_user_id_1", "example_user_id_2")) // 消息接收者
           .setSupportForward(true); // 是否支持转发
       // 吊顶投放属性
       DeliverCardRequestTopOpenDeliverModel topOpenDeliverModel = new DeliverCardRequestTopOpenDeliverModel()
           .setExpiredTimeMills(1665473229000L) // 吊顶过期时间
           .setUserIds(Arrays.asList("example_user_id_3", "example_user_id_4")) // 可以看到吊顶的用户
           .setPlatforms(Arrays.asList("android", "ios", "win", "mac")); // 可以看到吊顶的设备
       
       String outTrackId = "example_out_track_id";
       String openSpaceId = "dtv1.card//im_group.example_open_conversation_id;one_box.example_open_conversation_id";
       
       // 构造投放Request
       DeliverCardRequest deliverCardRequest = new DeliverCardRequest()
           .setOutTrackId(outTrackId)
           .setUserIdType(1)
           .setOpenSpaceId(openSpaceId)
           .setImGroupOpenDeliverModel(imGroupOpenDeliverModel)
           .setTopOpenDeliverModel(topOpenDeliverModel);
       
       try {
           client.deliverCardWithOptions(deliverCardRequest, deliverCardHeaders, new RuntimeOptions());
       } catch (TeaException err) {
           if (!empty(err.code) && !empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       } catch (Exception _err) {
           TeaException err = new TeaException(_err.getMessage(), _err);
           if (!empty(err.code) && !empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       }
   }
   ```

## **投放效果展示**

如图展示了上述示例中，将同一张卡片投放到IM群聊、吊顶中的效果。

![投放效果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2170650471/p790886.png)
