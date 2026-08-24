---
title: "创建并投放卡片"
source_url: "https://open.dingtalk.com/document/development/create-and-deliver-cards"
namespace: "development"
slug: "create-and-deliver-cards"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 互动卡片 > 创建并投放卡片"
doc_id: "O2gPy8KKZh"
updated_at: "2026-07-14 09:22:14"
---

> Source: https://open.dingtalk.com/document/development/create-and-deliver-cards
> Path: 应用开发 / 服务端API / 即时通信 > 互动卡片 > 创建并投放卡片
> Updated: 2026-07-14 09:22:14

# 创建并投放卡片

调用本接口，可以创建卡片实例，并将卡片投放至多个指定场域，创建卡片的时候，除了设置卡片的基本数据，还可以设置动态数据源等。

## **接口调用说明**

### **调用说明**

> **[!NOTE]**
>
> 目前支持将卡片投放至以下场域：IM群聊、IM单聊酷应用、IM机器人单聊、吊顶。

在将卡片投放到不同的场域时，使用`outTrackId`唯一标识一张卡片，通过`openSpaceId`标识需要被投放的场域及其场域Id，通过`openDeliverModels`传入不同的投放场域。

场域类型及其sapceId定义如下：

| 场域类型 | SpaceType | SpaceId | SpaceId含义 |
| --- | --- | --- | --- |
| IM群聊 | IM\_GROUP | openConversationId | 会话id |
| IM单聊酷应用 | IM\_SINGLE | openConversationId | 会话id |
| IM机器人单聊 | IM\_ROBOT | userId/unionId | 员工id |
| 吊顶 | ONE\_BOX | openConversationId | 会话id |

例如：IM 群聊的 `openSpaceId` 为：`dtv1.card//IM_GROUP.cidg2bR***JzmpFY=`。其中`dtv1.card//`为前缀固定值，`IM_GROUP`为群聊标识SpaceType，`cidg2bR***JzmpFY=`为群会话的openConversationId。

### 接口示例

调用示例可参考文档[API 调用示例](0778-example-of-calling-the-card-api-interface.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/instances/createAndDeliver |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Instance.Write-互动卡片实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 卡片创建者的userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| cardTemplateId | String | 是 | 卡片内容模板ID，可通过登录[开发者后台 > 卡片平台](https://open-dev.dingtalk.com/fe/card)获取。  image |
| outTrackId | String | 是 | 外部卡片实例Id。     - 开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到 outTrackId 的场景，帮助开发者对TrackId进行记录 - 一个 outTrackId 唯一标识一张卡片，如果需要使用新的 cardTemplateId 或 cardData 等参数创建一张新的卡片，需要设置全新的 outTrackId，否则更改不会生效。 |
| callbackType | String | 否 | 卡片回调的类型：   - **STREAM**：stream模式 - **HTTP**：http模式     注意参数均为大写。  详情参见[卡片互动-事件回调](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0007-event-callback-card.md)文档。 |
| callbackRouteKey | String | 否 | 卡片回调HTTP模式时的路由 Key，用于查询注册的 callbackUrl。可通过调用服务端API-[注册卡片回调地址](0786-register-card-callback-address.md)接口，根据填写的`callbackRouteKey`入参字段获取。 |
| cardData | Object | 是 | 卡片数据，示例：   ``` "cardData": {     "cardParamMap": {       "intParam": "1",				   // 整数类型属性       "floatParam": "1.2.3",	                   // 浮点类型属性       "trueParam": "true",		           // 布尔类型属性，对应 TRUE       "falseParam": "false"			   // 布尔类型属性，对应 FALSE     } } ``` |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - key：参数名（最长不超过100B） - value: 参数值（最长不超过1KB）      - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[API 卡片数据的填写说明](0789-instructions-for-filling-in-api-card-data.md)。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| privateData | Map<String, Object> | 否 | 用户的私有数据：   - key：用户userId信息（最长不超过100B） - value：用户私有数据（最长不超过1KB）   示例：   ``` "privateData": {     "manager1234": {         "cardParamMap": {             "attendee": "小明、小王",             "image1": "mediaIdXXXXX1"         }     } } ``` |
|  | Object | 否 | 私有用户userId。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - key：参数名 - value: 参数值        - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[API 卡片数据的填写说明](0789-instructions-for-filling-in-api-card-data.md)。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| openDynamicDataConfig | Object | 否 | 动态数据源配置。 |
| dynamicDataSourceConfigs | Array | 否 | 动态数据源配置列表。 |
| dynamicDataSourceId | String | 否 | 数据源的唯一 ID, 调用方指定。      使用动态数据源功能时该参数字段必填。 |
| constParams | Map<String, String> | 否 | 回调数据源时回传的固定参数。 示例：   ``` {     "attendee": "小明、小王",     "creatorId": "id123456" } ``` |
| pullConfig | Object | 否 | 数据源拉取配置。      使用动态数据源功能时该参数字段必填。 |
| pullStrategy | String | 否 | 拉取策略，可选值：   - **NONE**：不拉取，无动态数据 - **INTERVAL**：间隔拉取 - **ONCE**：只拉取一次       使用动态数据源功能时该参数字段必填。 |
| interval | Integer | 否 | 拉取的间隔时间。       - 只在将`pullStrategy`设置为**INTERVAL**的时候生效。 - 最小拉取间隔时间3s。 |
| timeUnit | String | 否 | 拉取的间隔时间的单位， 可选值：   - **SECONDS**：秒 - **MINUTES**：分钟 - **HOURS**：小时 - **DAYS**：天       只在将`pullStrategy`设置为**INTERVAL**的时候生效。 |
| imSingleOpenSpaceModel | Object | 否 | IM单聊酷应用场域信息，具体表现如下：  image      单聊酷应用详情参考[接入单聊酷应用](../01-XOnnmGCTbn-开发指南/0061-configuration-private-chat-quick-entry.md)。 |
| supportForward | Boolean | 否 | 是否支持转发, 默认false。 |
| lastMessageI18n | Map<String, String> | 否 | 支持国际化的LastMessage，目前支持的语言枚举值：   - **ZH\_CN**：简体中文 - **ZH\_TW**：繁体中文: - **EN\_US**：英文 - **JA\_JP**：日语 - **VI\_VN**：越南语 - **TH\_TH**: 泰语       key为语言枚举值，value为lastMessage内容。    示例：   ``` {"ZH_CN":"卡片", "EN_US" : "card"} ``` |
| searchSupport | Object | 否 | 支持卡片消息可被搜索字段。 |
| searchIcon | String | 否 | 类型的icon，供搜索展示使用。 |
| searchTypeName | String | 否 | 卡片类型名。 |
| searchDesc | String | 否 | 供消息展示与搜索的字段。       - 最大限制200个字符，超过存储截断200。 |
| notification | Object | 否 | 通知信息。 |
| alertContent | String | 否 | 通知内容。      若不填写则使用默认文案：如你收到1条新消息。 |
| notificationOff | Boolean | 否 | 是否关闭推送通知：   - **true**：关闭 - **false**：不关闭       默认为 false |
| imGroupOpenSpaceModel | Object | 否 | IM群聊场域信息。 |
| supportForward | Boolean | 否 | 是否支持转发：   - **true**：支持 - **false**：不支持       若使用`imGroupOpenSpaceModel`对象，则该字段必填。 |
| lastMessageI18n | Map<String, String> | 否 | 支持国际化的LastMessage，目前支持的语言枚举值：   - **ZH\_CN**：简体中文 - **ZH\_TW**：繁体中文: - **EN\_US**：英文 - **JA\_JP**：日语 - **VI\_VN**：越南语 - **TH\_TH**: 泰语       key为语言枚举值，value为lastMessage内容。    示例：   ``` {"ZH_CN":"卡片", "EN_US" : "card"} ``` |
| searchSupport | Object | 否 | 支持卡片消息可被搜索字段。 |
| searchIcon | String | 否 | 类型的icon，供搜索展示使用。 |
| searchTypeName | String | 否 | 卡片类型名。 |
| searchDesc | String | 否 | 供消息展示与搜索的字段。       - 最大限制200个字符，超过存储截断200。 |
| notification | Object | 否 | 通知信息。 |
| alertContent | String | 否 | 通知内容。      若不填写则使用默认文案：如你收到1条新消息。 |
| notificationOff | Boolean | 否 | 是否关闭推送通知：   - **true**：关闭 - **false**：不关闭       默认为 false |
| imRobotOpenSpaceModel | Object | 否 | IM机器人单聊场域信息。 |
| supportForward | Boolean | 否 | 是否支持转发：   - **true**：转发 - **false**：不转发       若使用`imRobotOpenSpaceModel`对象，则该字段必填。 |
| lastMessageI18n | Map<String, String> | 否 | 支持国际化的LastMessage，目前支持的语言枚举值：   - **ZH\_CN**：简体中文 - **ZH\_TW**：繁体中文: - **EN\_US**：英文 - **JA\_JP**：日语 - **VI\_VN**：越南语 - **TH\_TH**: 泰语       key为语言枚举值，value为lastMessage内容。    示例：   ``` {"ZH_CN":"卡片", "EN_US" : "card"} ``` |
| searchSupport | Object | 否 | 支持卡片消息可被搜索字段。 |
| searchIcon | String | 否 | 类型的icon，供搜索展示使用。 |
| searchTypeName | String | 否 | 卡片类型名。 |
| searchDesc | String | 否 | 供消息展示与搜索的字段。       - 最大限制200个字符，超过存储截断200。 |
| notification | Object | 否 | 通知信息。 |
| alertContent | String | 否 | 供消息展示与搜索的字段。       - 最大限制200个字符，超过存储截断200。 |
| notificationOff | Boolean | 否 | 是否关闭推送通知：   - **true**：关闭 - **false**：不关闭       默认为 false |
| coFeedOpenSpaceModel | Object | 否 | 协作场域信息（废弃）。 |
| title | String | 否 | 卡片标题（废弃）。      若使用`coFeedOpenSpaceModel`对象，则该字段必填。 |
| coolAppCode | String | 否 | 酷应用编码（废弃）。 |
| topOpenSpaceModel | Object | 否 | 吊顶场域信息。 |
| spaceType | String | 否 | 吊顶场域属性，通过增加spaeType使卡片支持吊顶场域。       - 吊顶对应spaceType为**ONE\_BOX**。 - 若使用`topOpenSpaceModel`对象，则该字段必填。 |
| openSpaceId | String | 是 | 表示场域及其场域id，其格式为`dtv1.card//spaceType1.spaceId1;spaceType2.spaceId2_1;spaceType2.spaceId2_2;spaceType3.spaceId3`。 |
| imSingleOpenDeliverModel | Object | 否 | 单聊酷应用场域投放参数。 |
| atUserIds | Map<String, String> | 否 | 消息@人。格式：{"key":"value"}。   - key：用户的userId - value：用户名。       如果key、value都为"@ALL"则判断@所有人。    示例：   ``` "atUserIds" : {     "123456" : "小明" } ``` |
| extension | Map<String, String> | 否 | 扩展字段，示例如下：   ``` {"key":"value"} ``` |
| imGroupOpenDeliverModel | Object | 否 | 群聊投放参数。 |
| robotCode | String | 否 | 用于发送卡片的机器人编码。   - 场景群机器人发送群聊使用群机器人robotCode - 非场景群的企业内部开发的机器人发送群聊，使用机器人的AppKey - 第三方企业机器人，使用机器人的robotCode       若使用`imGroupOpenDeliverModel`对象，则该字段必填。 |
| atUserIds | Map<String, String> | 否 | 消息@人。格式：{"key":"value"}。   - key：用户的userId - value：用户名。       如果key、value都为"@ALL"则判断@所有人。    示例：   ``` "atUserIds" : {     "123456" : "小明" } ``` |
| recipients | Array of String | 否 | 指定接收人的userId。 |
| extension | Map<String, String> | 否 | 扩展字段，示例如下：   ``` {"key":"value"} ``` |
| imRobotOpenDeliverModel | Object | 否 | IM机器人单聊投放参数。 |
| spaceType | String | 否 | IM机器人单聊若未设置其他投放属性，需设置spaeType为`IM_ROBOT`。 |
| robotCode | String | 否 | 机器人编码。 |
| extension | Map<String, String> | 否 | 扩展字段，示例如下：   ``` {"key":"value"} ``` |
| topOpenDeliverModel | Object | 否 | 吊顶投放参数。 |
| expiredTimeMillis | Long | 否 | 过期时间戳。      若使用`topOpenDeliverModel`对象，则该字段必填。 |
| userIds | Array of String | 否 | 可以查看该吊顶卡片的userId。 |
| platforms | Array of String | 否 | 可以查看该吊顶卡片的设备：`android｜ios｜win｜mac`。 |
| coFeedOpenDeliverModel | Object | 否 | 协作投放参数（废弃）。 |
| bizTag | String | 否 | 业务标识（废弃）。       - 若使用`coFeedOpenDeliverModel`对象，则该字段必填。 - 需要先申请在协作中投放该bizTag，申请通过后才能使用。 |
| gmtTimeLine | Long | 否 | 协作场域下的排序时间（废弃）。      若使用`coFeedOpenDeliverModel`对象，则该字段必填。 |
| docOpenDeliverModel | Object | 否 | 文档投放参数（废弃）。 |
| userId | String | 否 | 员工userId信息（废弃）。      若使用`docOpenDeliverModel`对象，则该字段必填。 |
| userIdType | Integer | 否 | 用户userId类型：   - **1**（默认）：userId模式 - **2**：unionId模式       `userIdType` 字段的填写请参考：[userIdType 字段的填写说明](0790-faq-card.md#8cad7f90a8mzg)。 |
| cardAtUserIds | Array of String | 否 | 被@人的userId列表:         - 设置此字段，可以实现在卡片中@人的效果； - 同时需要在卡片的 markdown 内容中添加：`<a atId=example_user_id> 用户昵称<a>` ；     示例：比如卡片模板中的一个 markdown 变量名为 markdown\_content，则卡片变量需要设置为：   ``` {     "cardParamMap": {         "markdown_content": "这是一段测@人高亮文字: <a atId=example_user_id_1>小明 </a> <a atId=example_user_id_2>小红 </a>"     } } ``` |

### 请求示例

HTTP

```
POST /v1.0/card/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:example_token
Content-Type:application/json

{
  "userId" : "example_user_id",
  "cardTemplateId" : "b4fdsu2119f-9945-4e13-9989-747da19e3bc7",
  "outTrackId" : "example_out_track_id",
  "callbackType" : "STREAM",
  "callbackRouteKey" : "example_route_key",
  "cardData" : {
    "cardParamMap" : {
      "key" : "example_public_value"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "example_private_value"
      }
    }
  },
  "openDynamicDataConfig" : {
    "dynamicDataSourceConfigs" : [ {
      "dynamicDataSourceId" : "example_ds_01",
      "constParams" : {
        "key" : "example_const_param_value"
      },
      "pullConfig" : {
        "pullStrategy" : "INTERVAL",
        "interval" : 600,
        "timeUnit" : "SECONDS"
      }
    } ]
  },
  "imSingleOpenSpaceModel" : {
    "supportForward" : true,
    "lastMessageI18n" : {
      "key" : "互动卡片消息"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了1条卡片消息",
      "notificationOff" : false
    }
  },
  "imGroupOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
      "key" : "互动卡片消息"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了1条卡片消息",
      "notificationOff" : false
    }
  },
  "imRobotOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
      "key" : "互动卡片消息"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了1条卡片消息",
      "notificationOff" : false
    }
  },
  "coFeedOpenSpaceModel" : {
    "title" : "xxxx卡片",
    "coolAppCode" : "coolAppCode123"
  },
  "topOpenSpaceModel" : {
    "spaceType" : "ONE_BOX"
  },
  "openSpaceId" : "dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==",
  "imSingleOpenDeliverModel" : {
    "atUserIds" : {
      "key" : "example_user_name"
    },
    "extension" : {
      "key" : "example_ext_value"
    }
  },
  "imGroupOpenDeliverModel" : {
    "robotCode" : "example_robot_code",
    "atUserIds" : {
      "key" : "example_user_name"
    },
    "recipients" : [ "example_user_id" ],
    "extension" : {
      "key" : "example_ext_value"
    }
  },
  "imRobotOpenDeliverModel" : {
    "spaceType" : "IM_ROBOT",
    "robotCode" : "example_robot_code",
    "extension" : {
      "key" : "example_ext_value"
    }
  },
  "topOpenDeliverModel" : {
    "expiredTimeMillis" : 1665473229000,
    "userIds" : [ "example_user_id" ],
    "platforms" : [ "android" ]
  },
  "coFeedOpenDeliverModel" : {
    "bizTag" : "example_biz_tag",
    "gmtTimeLine" : 1665473229000
  },
  "docOpenDeliverModel" : {
    "userId" : "example_user_id"
  },
  "userIdType" : 1,
  "cardAtUserIds" : [ "example_user_id" ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverHeaders createAndDeliverHeaders = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverHeaders();
        createAndDeliverHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestDocOpenDeliverModel docOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestDocOpenDeliverModel()
                .setUserId("example_user_id");
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenDeliverModel coFeedOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenDeliverModel()
                .setBizTag("example_biz_tag")
                .setGmtTimeLine(1665473229000L);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenDeliverModel topOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenDeliverModel()
                .setExpiredTimeMillis(1665473229000L)
                .setUserIds(java.util.Arrays.asList(
                    "example_user_id"
                ))
                .setPlatforms(java.util.Arrays.asList(
                    "android"
                ));
        java.util.Map<String, String> imRobotOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "example_ext_value")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenDeliverModel imRobotOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenDeliverModel()
                .setSpaceType("IM_ROBOT")
                .setRobotCode("example_robot_code")
                .setExtension(imRobotOpenDeliverModelExtension);
        java.util.Map<String, String> imGroupOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "example_ext_value")
        );
        java.util.Map<String, String> imGroupOpenDeliverModelAtUserIds = TeaConverter.buildMap(
            new TeaPair("key", "example_user_name")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenDeliverModel()
                .setRobotCode("example_robot_code")
                .setAtUserIds(imGroupOpenDeliverModelAtUserIds)
                .setRecipients(java.util.Arrays.asList(
                    "example_user_id"
                ))
                .setExtension(imGroupOpenDeliverModelExtension);
        java.util.Map<String, String> imSingleOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "example_ext_value")
        );
        java.util.Map<String, String> imSingleOpenDeliverModelAtUserIds = TeaConverter.buildMap(
            new TeaPair("key", "example_user_name")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenDeliverModel imSingleOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenDeliverModel()
                .setAtUserIds(imSingleOpenDeliverModelAtUserIds)
                .setExtension(imSingleOpenDeliverModelExtension);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenSpaceModel topOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenSpaceModel()
                .setSpaceType("ONE_BOX");
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenSpaceModel coFeedOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenSpaceModel()
                .setTitle("xxxx卡片")
                .setCoolAppCode("coolAppCode123");
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModelNotification()
                .setAlertContent("你收到了1条卡片消息")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport()
                .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
                .setSearchTypeName("{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}")
                .setSearchDesc("卡片的具体描述");
        java.util.Map<String, String> imRobotOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "互动卡片消息")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel()
                .setSupportForward(false)
                .setLastMessageI18n(imRobotOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imRobotOpenSpaceModelSearchSupport)
                .setNotification(imRobotOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModelNotification()
                .setAlertContent("你收到了1条卡片消息")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport()
                .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
                .setSearchTypeName("{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}")
                .setSearchDesc("卡片的具体描述");
        java.util.Map<String, String> imGroupOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "互动卡片消息")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel()
                .setSupportForward(false)
                .setLastMessageI18n(imGroupOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imGroupOpenSpaceModelSearchSupport)
                .setNotification(imGroupOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModelNotification imSingleOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModelNotification()
                .setAlertContent("你收到了1条卡片消息")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport imSingleOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport()
                .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
                .setSearchTypeName("{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}")
                .setSearchDesc("卡片的具体描述");
        java.util.Map<String, String> imSingleOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "互动卡片消息")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel imSingleOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel()
                .setSupportForward(true)
                .setLastMessageI18n(imSingleOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imSingleOpenSpaceModelSearchSupport)
                .setNotification(imSingleOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig openDynamicDataConfigDynamicDataSourceConfigs0PullConfig = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig()
                .setPullStrategy("INTERVAL")
                .setInterval(600)
                .setTimeUnit("SECONDS");
        java.util.Map<String, String> openDynamicDataConfigDynamicDataSourceConfigs0ConstParams = TeaConverter.buildMap(
            new TeaPair("key", "example_const_param_value")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs openDynamicDataConfigDynamicDataSourceConfigs0 = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs()
                .setDynamicDataSourceId("example_ds_01")
                .setConstParams(openDynamicDataConfigDynamicDataSourceConfigs0ConstParams)
                .setPullConfig(openDynamicDataConfigDynamicDataSourceConfigs0PullConfig);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig openDynamicDataConfig = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig()
                .setDynamicDataSourceConfigs(java.util.Arrays.asList(
                    openDynamicDataConfigDynamicDataSourceConfigs0
                ));
        java.util.Map<String, String> privateDataValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "example_private_value")
        );
        com.aliyun.dingtalkcard_1_0.models.PrivateDataValue privateDataValueKey = new com.aliyun.dingtalkcard_1_0.models.PrivateDataValue()
                .setCardParamMap(privateDataValueKeyCardParamMap);
        java.util.Map<String, com.aliyun.dingtalkcard_1_0.models.PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "example_public_value")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestCardData cardData = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest.CreateAndDeliverRequestCardData()
                .setCardParamMap(cardDataCardParamMap);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest createAndDeliverRequest = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest()
                .setUserId("example_user_id")
                .setCardTemplateId("b4fdsu2119f-9945-4e13-9989-747da19e3bc7")
                .setOutTrackId("example_out_track_id")
                .setCallbackType("STREAM")
                .setCallbackRouteKey("example_route_key")
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setOpenDynamicDataConfig(openDynamicDataConfig)
                .setImSingleOpenSpaceModel(imSingleOpenSpaceModel)
                .setImGroupOpenSpaceModel(imGroupOpenSpaceModel)
                .setImRobotOpenSpaceModel(imRobotOpenSpaceModel)
                .setCoFeedOpenSpaceModel(coFeedOpenSpaceModel)
                .setTopOpenSpaceModel(topOpenSpaceModel)
                .setOpenSpaceId("dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==")
                .setImSingleOpenDeliverModel(imSingleOpenDeliverModel)
                .setImGroupOpenDeliverModel(imGroupOpenDeliverModel)
                .setImRobotOpenDeliverModel(imRobotOpenDeliverModel)
                .setTopOpenDeliverModel(topOpenDeliverModel)
                .setCoFeedOpenDeliverModel(coFeedOpenDeliverModel)
                .setDocOpenDeliverModel(docOpenDeliverModel)
                .setUserIdType(1)
                .setCardAtUserIds(java.util.Arrays.asList(
                    "example_user_id"
                ));
        try {
            client.createAndDeliverWithOptions(createAndDeliverRequest, createAndDeliverHeaders, new com.aliyun.teautil.models.RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

Python

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_and_deliver_headers = dingtalkcard__1__0_models.CreateAndDeliverHeaders()
        create_and_deliver_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestDocOpenDeliverModel(
            user_id='example_user_id'
        )
        co_feed_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestCoFeedOpenDeliverModel(
            biz_tag='example_biz_tag',
            gmt_time_line=1665473229000
        )
        top_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestTopOpenDeliverModel(
            expired_time_millis=1665473229000,
            user_ids=[
                'example_user_id'
            ],
            platforms=[
                'android'
            ]
        )
        im_robot_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_robot_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenDeliverModel(
            space_type='IM_ROBOT',
            robot_code='example_robot_code',
            extension=im_robot_open_deliver_model_extension
        )
        im_group_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_group_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_group_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenDeliverModel(
            robot_code='example_robot_code',
            at_user_ids=im_group_open_deliver_model_at_user_ids,
            recipients=[
                'example_user_id'
            ],
            extension=im_group_open_deliver_model_extension
        )
        im_single_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_single_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_single_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenDeliverModel(
            at_user_ids=im_single_open_deliver_model_at_user_ids,
            extension=im_single_open_deliver_model_extension
        )
        top_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestTopOpenSpaceModel(
            space_type='ONE_BOX'
        )
        co_feed_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestCoFeedOpenSpaceModel(
            title='xxxx卡片',
            cool_app_code='coolAppCode123'
        )
        im_robot_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenSpaceModelNotification(
            alert_content='你收到了1条卡片消息',
            notification_off=False
        )
        im_robot_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_robot_open_space_model_last_message_i18n = {
            'key': '互动卡片消息'
        }
        im_robot_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_robot_open_space_model_last_message_i18n,
            search_support=im_robot_open_space_model_search_support,
            notification=im_robot_open_space_model_notification
        )
        im_group_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenSpaceModelNotification(
            alert_content='你收到了1条卡片消息',
            notification_off=False
        )
        im_group_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_group_open_space_model_last_message_i18n = {
            'key': '互动卡片消息'
        }
        im_group_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_group_open_space_model_last_message_i18n,
            search_support=im_group_open_space_model_search_support,
            notification=im_group_open_space_model_notification
        )
        im_single_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenSpaceModelNotification(
            alert_content='你收到了1条卡片消息',
            notification_off=False
        )
        im_single_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_single_open_space_model_last_message_i18n = {
            'key': '互动卡片消息'
        }
        im_single_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenSpaceModel(
            support_forward=True,
            last_message_i18n=im_single_open_space_model_last_message_i18n,
            search_support=im_single_open_space_model_search_support,
            notification=im_single_open_space_model_notification
        )
        open_dynamic_data_config_dynamic_data_source_configs_0pull_config = dingtalkcard__1__0_models.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig(
            pull_strategy='INTERVAL',
            interval=600,
            time_unit='SECONDS'
        )
        open_dynamic_data_config_dynamic_data_source_configs_0const_params = {
            'key': 'example_const_param_value'
        }
        open_dynamic_data_config_dynamic_data_source_configs_0 = dingtalkcard__1__0_models.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs(
            dynamic_data_source_id='example_ds_01',
            const_params=open_dynamic_data_config_dynamic_data_source_configs_0const_params,
            pull_config=open_dynamic_data_config_dynamic_data_source_configs_0pull_config
        )
        open_dynamic_data_config = dingtalkcard__1__0_models.CreateAndDeliverRequestOpenDynamicDataConfig(
            dynamic_data_source_configs=[
                open_dynamic_data_config_dynamic_data_source_configs_0
            ]
        )
        private_data_value_key_card_param_map = {
            'key': 'example_private_value'
        }
        private_data_value_key = dingtalkcard__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_param_map = {
            'key': 'example_public_value'
        }
        card_data = dingtalkcard__1__0_models.CreateAndDeliverRequestCardData(
            card_param_map=card_data_card_param_map
        )
        create_and_deliver_request = dingtalkcard__1__0_models.CreateAndDeliverRequest(
            user_id='example_user_id',
            card_template_id='b4fdsu2119f-9945-4e13-9989-747da19e3bc7',
            out_track_id='example_out_track_id',
            callback_type='STREAM',
            callback_route_key='example_route_key',
            card_data=card_data,
            private_data=private_data,
            open_dynamic_data_config=open_dynamic_data_config,
            im_single_open_space_model=im_single_open_space_model,
            im_group_open_space_model=im_group_open_space_model,
            im_robot_open_space_model=im_robot_open_space_model,
            co_feed_open_space_model=co_feed_open_space_model,
            top_open_space_model=top_open_space_model,
            open_space_id='dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==',
            im_single_open_deliver_model=im_single_open_deliver_model,
            im_group_open_deliver_model=im_group_open_deliver_model,
            im_robot_open_deliver_model=im_robot_open_deliver_model,
            top_open_deliver_model=top_open_deliver_model,
            co_feed_open_deliver_model=co_feed_open_deliver_model,
            doc_open_deliver_model=doc_open_deliver_model,
            user_id_type=1,
            card_at_user_ids=[
                'example_user_id'
            ]
        )
        try:
            client.create_and_deliver_with_options(create_and_deliver_request, create_and_deliver_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_and_deliver_headers = dingtalkcard__1__0_models.CreateAndDeliverHeaders()
        create_and_deliver_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestDocOpenDeliverModel(
            user_id='example_user_id'
        )
        co_feed_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestCoFeedOpenDeliverModel(
            biz_tag='example_biz_tag',
            gmt_time_line=1665473229000
        )
        top_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestTopOpenDeliverModel(
            expired_time_millis=1665473229000,
            user_ids=[
                'example_user_id'
            ],
            platforms=[
                'android'
            ]
        )
        im_robot_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_robot_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenDeliverModel(
            space_type='IM_ROBOT',
            robot_code='example_robot_code',
            extension=im_robot_open_deliver_model_extension
        )
        im_group_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_group_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_group_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenDeliverModel(
            robot_code='example_robot_code',
            at_user_ids=im_group_open_deliver_model_at_user_ids,
            recipients=[
                'example_user_id'
            ],
            extension=im_group_open_deliver_model_extension
        )
        im_single_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_single_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_single_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenDeliverModel(
            at_user_ids=im_single_open_deliver_model_at_user_ids,
            extension=im_single_open_deliver_model_extension
        )
        top_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestTopOpenSpaceModel(
            space_type='ONE_BOX'
        )
        co_feed_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestCoFeedOpenSpaceModel(
            title='xxxx卡片',
            cool_app_code='coolAppCode123'
        )
        im_robot_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenSpaceModelNotification(
            alert_content='你收到了1条卡片消息',
            notification_off=False
        )
        im_robot_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_robot_open_space_model_last_message_i18n = {
            'key': '互动卡片消息'
        }
        im_robot_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImRobotOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_robot_open_space_model_last_message_i18n,
            search_support=im_robot_open_space_model_search_support,
            notification=im_robot_open_space_model_notification
        )
        im_group_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenSpaceModelNotification(
            alert_content='你收到了1条卡片消息',
            notification_off=False
        )
        im_group_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_group_open_space_model_last_message_i18n = {
            'key': '互动卡片消息'
        }
        im_group_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImGroupOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_group_open_space_model_last_message_i18n,
            search_support=im_group_open_space_model_search_support,
            notification=im_group_open_space_model_notification
        )
        im_single_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenSpaceModelNotification(
            alert_content='你收到了1条卡片消息',
            notification_off=False
        )
        im_single_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_single_open_space_model_last_message_i18n = {
            'key': '互动卡片消息'
        }
        im_single_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverRequestImSingleOpenSpaceModel(
            support_forward=True,
            last_message_i18n=im_single_open_space_model_last_message_i18n,
            search_support=im_single_open_space_model_search_support,
            notification=im_single_open_space_model_notification
        )
        open_dynamic_data_config_dynamic_data_source_configs_0pull_config = dingtalkcard__1__0_models.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig(
            pull_strategy='INTERVAL',
            interval=600,
            time_unit='SECONDS'
        )
        open_dynamic_data_config_dynamic_data_source_configs_0const_params = {
            'key': 'example_const_param_value'
        }
        open_dynamic_data_config_dynamic_data_source_configs_0 = dingtalkcard__1__0_models.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs(
            dynamic_data_source_id='example_ds_01',
            const_params=open_dynamic_data_config_dynamic_data_source_configs_0const_params,
            pull_config=open_dynamic_data_config_dynamic_data_source_configs_0pull_config
        )
        open_dynamic_data_config = dingtalkcard__1__0_models.CreateAndDeliverRequestOpenDynamicDataConfig(
            dynamic_data_source_configs=[
                open_dynamic_data_config_dynamic_data_source_configs_0
            ]
        )
        private_data_value_key_card_param_map = {
            'key': 'example_private_value'
        }
        private_data_value_key = dingtalkcard__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_param_map = {
            'key': 'example_public_value'
        }
        card_data = dingtalkcard__1__0_models.CreateAndDeliverRequestCardData(
            card_param_map=card_data_card_param_map
        )
        create_and_deliver_request = dingtalkcard__1__0_models.CreateAndDeliverRequest(
            user_id='example_user_id',
            card_template_id='b4fdsu2119f-9945-4e13-9989-747da19e3bc7',
            out_track_id='example_out_track_id',
            callback_type='STREAM',
            callback_route_key='example_route_key',
            card_data=card_data,
            private_data=private_data,
            open_dynamic_data_config=open_dynamic_data_config,
            im_single_open_space_model=im_single_open_space_model,
            im_group_open_space_model=im_group_open_space_model,
            im_robot_open_space_model=im_robot_open_space_model,
            co_feed_open_space_model=co_feed_open_space_model,
            top_open_space_model=top_open_space_model,
            open_space_id='dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==',
            im_single_open_deliver_model=im_single_open_deliver_model,
            im_group_open_deliver_model=im_group_open_deliver_model,
            im_robot_open_deliver_model=im_robot_open_deliver_model,
            top_open_deliver_model=top_open_deliver_model,
            co_feed_open_deliver_model=co_feed_open_deliver_model,
            doc_open_deliver_model=doc_open_deliver_model,
            user_id_type=1,
            card_at_user_ids=[
                'example_user_id'
            ]
        )
        try:
            await client.create_and_deliver_with_options_async(create_and_deliver_request, create_and_deliver_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

PHP

```
<?php

// This file is auto-generated, don't edit it. Thanks.
namespace AlibabaCloud\SDK\Sample;

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\docOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\coFeedOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\topOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imRobotOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imGroupOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imSingleOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\topOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\coFeedOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imRobotOpenSpaceModel\notification;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imRobotOpenSpaceModel\searchSupport;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imRobotOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imGroupOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imSingleOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\openDynamicDataConfig\dynamicDataSourceConfigs\pullConfig;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\openDynamicDataConfig\dynamicDataSourceConfigs;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\openDynamicDataConfig;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\PrivateDataValue;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest;
use AlibabaCloud\Tea\Utils\Utils\RuntimeOptions;

class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Dingtalk Client
     */
    public static function createClient(){
        $config = new Config([]);
        $config->protocol = "https";
        $config->regionId = "central";
        return new Dingtalk($config);
    }

    /**
     * @param string[] $args
     * @return void
     */
    public static function main($args){
        $client = self::createClient();
        $createAndDeliverHeaders = new CreateAndDeliverHeaders([]);
        $createAndDeliverHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $docOpenDeliverModel = new docOpenDeliverModel([
            "userId" => "example_user_id"
        ]);
        $coFeedOpenDeliverModel = new coFeedOpenDeliverModel([
            "bizTag" => "example_biz_tag",
            "gmtTimeLine" => 1665473229000
        ]);
        $topOpenDeliverModel = new topOpenDeliverModel([
            "expiredTimeMillis" => 1665473229000,
            "userIds" => [
                "example_user_id"
            ],
            "platforms" => [
                "android"
            ]
        ]);
        $imRobotOpenDeliverModelExtension = [
            "key" => "example_ext_value"
        ];
        $imRobotOpenDeliverModel = new imRobotOpenDeliverModel([
            "spaceType" => "IM_ROBOT",
            "robotCode" => "example_robot_code",
            "extension" => $imRobotOpenDeliverModelExtension
        ]);
        $imGroupOpenDeliverModelExtension = [
            "key" => "example_ext_value"
        ];
        $imGroupOpenDeliverModelAtUserIds = [
            "key" => "example_user_name"
        ];
        $imGroupOpenDeliverModel = new imGroupOpenDeliverModel([
            "robotCode" => "example_robot_code",
            "atUserIds" => $imGroupOpenDeliverModelAtUserIds,
            "recipients" => [
                "example_user_id"
            ],
            "extension" => $imGroupOpenDeliverModelExtension
        ]);
        $imSingleOpenDeliverModelExtension = [
            "key" => "example_ext_value"
        ];
        $imSingleOpenDeliverModelAtUserIds = [
            "key" => "example_user_name"
        ];
        $imSingleOpenDeliverModel = new imSingleOpenDeliverModel([
            "atUserIds" => $imSingleOpenDeliverModelAtUserIds,
            "extension" => $imSingleOpenDeliverModelExtension
        ]);
        $topOpenSpaceModel = new topOpenSpaceModel([
            "spaceType" => "ONE_BOX"
        ]);
        $coFeedOpenSpaceModel = new coFeedOpenSpaceModel([
            "title" => "xxxx卡片",
            "coolAppCode" => "coolAppCode123"
        ]);
        $imRobotOpenSpaceModelNotification = new notification([
            "alertContent" => "你收到了1条卡片消息",
            "notificationOff" => false
        ]);
        $imRobotOpenSpaceModelSearchSupport = new searchSupport([
            "searchIcon" => "@lALPDgQ9q8hFhlHNAXzNAqI",
            "searchTypeName" => "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
            "searchDesc" => "卡片的具体描述"
        ]);
        $imRobotOpenSpaceModelLastMessageI18n = [
            "key" => "互动卡片消息"
        ];
        $imRobotOpenSpaceModel = new imRobotOpenSpaceModel([
            "supportForward" => false,
            "lastMessageI18n" => $imRobotOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imRobotOpenSpaceModelSearchSupport,
            "notification" => $imRobotOpenSpaceModelNotification
        ]);
        $imGroupOpenSpaceModelNotification = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imGroupOpenSpaceModel\notification([
            "alertContent" => "你收到了1条卡片消息",
            "notificationOff" => false
        ]);
        $imGroupOpenSpaceModelSearchSupport = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imGroupOpenSpaceModel\searchSupport([
            "searchIcon" => "@lALPDgQ9q8hFhlHNAXzNAqI",
            "searchTypeName" => "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
            "searchDesc" => "卡片的具体描述"
        ]);
        $imGroupOpenSpaceModelLastMessageI18n = [
            "key" => "互动卡片消息"
        ];
        $imGroupOpenSpaceModel = new imGroupOpenSpaceModel([
            "supportForward" => false,
            "lastMessageI18n" => $imGroupOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imGroupOpenSpaceModelSearchSupport,
            "notification" => $imGroupOpenSpaceModelNotification
        ]);
        $imSingleOpenSpaceModelNotification = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imSingleOpenSpaceModel\notification([
            "alertContent" => "你收到了1条卡片消息",
            "notificationOff" => false
        ]);
        $imSingleOpenSpaceModelSearchSupport = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverRequest\imSingleOpenSpaceModel\searchSupport([
            "searchIcon" => "@lALPDgQ9q8hFhlHNAXzNAqI",
            "searchTypeName" => "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
            "searchDesc" => "卡片的具体描述"
        ]);
        $imSingleOpenSpaceModelLastMessageI18n = [
            "key" => "互动卡片消息"
        ];
        $imSingleOpenSpaceModel = new imSingleOpenSpaceModel([
            "supportForward" => true,
            "lastMessageI18n" => $imSingleOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imSingleOpenSpaceModelSearchSupport,
            "notification" => $imSingleOpenSpaceModelNotification
        ]);
        $openDynamicDataConfigDynamicDataSourceConfigs0PullConfig = new pullConfig([
            "pullStrategy" => "INTERVAL",
            "interval" => 600,
            "timeUnit" => "SECONDS"
        ]);
        $openDynamicDataConfigDynamicDataSourceConfigs0ConstParams = [
            "key" => "example_const_param_value"
        ];
        $openDynamicDataConfigDynamicDataSourceConfigs0 = new dynamicDataSourceConfigs([
            "dynamicDataSourceId" => "example_ds_01",
            "constParams" => $openDynamicDataConfigDynamicDataSourceConfigs0ConstParams,
            "pullConfig" => $openDynamicDataConfigDynamicDataSourceConfigs0PullConfig
        ]);
        $openDynamicDataConfig = new openDynamicDataConfig([
            "dynamicDataSourceConfigs" => [
                $openDynamicDataConfigDynamicDataSourceConfigs0
            ]
        ]);
        $privateDataValueKeyCardParamMap = [
            "key" => "example_private_value"
        ];
        $privateDataValueKey = new PrivateDataValue([
            "cardParamMap" => $privateDataValueKeyCardParamMap
        ]);
        $privateData = [
            "privateDataValueKey" => $privateDataValueKey
        ];
        $cardDataCardParamMap = [
            "key" => "example_public_value"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap
        ]);
        $createAndDeliverRequest = new CreateAndDeliverRequest([
            "userId" => "example_user_id",
            "cardTemplateId" => "b4fdsu2119f-9945-4e13-9989-747da19e3bc7",
            "outTrackId" => "example_out_track_id",
            "callbackType" => "STREAM",
            "callbackRouteKey" => "example_route_key",
            "cardData" => $cardData,
            "privateData" => $privateData,
            "openDynamicDataConfig" => $openDynamicDataConfig,
            "imSingleOpenSpaceModel" => $imSingleOpenSpaceModel,
            "imGroupOpenSpaceModel" => $imGroupOpenSpaceModel,
            "imRobotOpenSpaceModel" => $imRobotOpenSpaceModel,
            "coFeedOpenSpaceModel" => $coFeedOpenSpaceModel,
            "topOpenSpaceModel" => $topOpenSpaceModel,
            "openSpaceId" => "dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==",
            "imSingleOpenDeliverModel" => $imSingleOpenDeliverModel,
            "imGroupOpenDeliverModel" => $imGroupOpenDeliverModel,
            "imRobotOpenDeliverModel" => $imRobotOpenDeliverModel,
            "topOpenDeliverModel" => $topOpenDeliverModel,
            "coFeedOpenDeliverModel" => $coFeedOpenDeliverModel,
            "docOpenDeliverModel" => $docOpenDeliverModel,
            "userIdType" => 1,
            "cardAtUserIds" => [
                "example_user_id"
            ]
        ]);
        try {
            $client->createAndDeliverWithOptions($createAndDeliverRequest, $createAndDeliverHeaders, new RuntimeOptions([]));
        }
        catch (Exception $err) {
            if (!($err instanceof TeaError)) {
                $err = new TeaError([], $err->getMessage(), $err->getCode(), $err);
            }
            if (!Utils::empty_($err->code) && !Utils::empty_($err->message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }
        }
    }
}
$path = __DIR__ . \DIRECTORY_SEPARATOR . '..' . \DIRECTORY_SEPARATOR . 'vendor' . \DIRECTORY_SEPARATOR . 'autoload.php';
if (file_exists($path)) {
    require_once $path;
}
Sample::main(array_slice($argv, 1));
```

Go

```
// This file is auto-generated, don't edit it. Thanks.
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createAndDeliverHeaders := &dingtalkcard_1_0.CreateAndDeliverHeaders{}
  createAndDeliverHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  docOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverRequestDocOpenDeliverModel{
    UserId: tea.String("example_user_id"),
  }
  coFeedOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverRequestCoFeedOpenDeliverModel{
    BizTag: tea.String("example_biz_tag"),
    GmtTimeLine: tea.Int64(1665473229000),
  }
  topOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverRequestTopOpenDeliverModel{
    ExpiredTimeMillis: tea.Int64(1665473229000),
    UserIds: []*string{tea.String("example_user_id")},
    Platforms: []*string{tea.String("android")},
  }
  imRobotOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("example_ext_value"),
  }
  imRobotOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenDeliverModel{
    SpaceType: tea.String("IM_ROBOT"),
    RobotCode: tea.String("example_robot_code"),
    Extension: imRobotOpenDeliverModelExtension,
  }
  imGroupOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("example_ext_value"),
  }
  imGroupOpenDeliverModelAtUserIds := map[string]*string{
    "key": tea.String("example_user_name"),
  }
  imGroupOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenDeliverModel{
    RobotCode: tea.String("example_robot_code"),
    AtUserIds: imGroupOpenDeliverModelAtUserIds,
    Recipients: []*string{tea.String("example_user_id")},
    Extension: imGroupOpenDeliverModelExtension,
  }
  imSingleOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("example_ext_value"),
  }
  imSingleOpenDeliverModelAtUserIds := map[string]*string{
    "key": tea.String("example_user_name"),
  }
  imSingleOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenDeliverModel{
    AtUserIds: imSingleOpenDeliverModelAtUserIds,
    Extension: imSingleOpenDeliverModelExtension,
  }
  topOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverRequestTopOpenSpaceModel{
    SpaceType: tea.String("ONE_BOX"),
  }
  coFeedOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverRequestCoFeedOpenSpaceModel{
    Title: tea.String("xxxx卡片"),
    CoolAppCode: tea.String("coolAppCode123"),
  }
  imRobotOpenSpaceModelNotification := &dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenSpaceModelNotification{
    AlertContent: tea.String("你收到了1条卡片消息"),
    NotificationOff: tea.Bool(false),
  }
  imRobotOpenSpaceModelSearchSupport := &dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("@lALPDgQ9q8hFhlHNAXzNAqI"),
    SearchTypeName: tea.String("{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}"),
    SearchDesc: tea.String("卡片的具体描述"),
  }
  imRobotOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("互动卡片消息"),
  }
  imRobotOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenSpaceModel{
    SupportForward: tea.Bool(false),
    LastMessageI18n: imRobotOpenSpaceModelLastMessageI18n,
    SearchSupport: imRobotOpenSpaceModelSearchSupport,
    Notification: imRobotOpenSpaceModelNotification,
  }
  imGroupOpenSpaceModelNotification := &dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenSpaceModelNotification{
    AlertContent: tea.String("你收到了1条卡片消息"),
    NotificationOff: tea.Bool(false),
  }
  imGroupOpenSpaceModelSearchSupport := &dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("@lALPDgQ9q8hFhlHNAXzNAqI"),
    SearchTypeName: tea.String("{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}"),
    SearchDesc: tea.String("卡片的具体描述"),
  }
  imGroupOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("互动卡片消息"),
  }
  imGroupOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenSpaceModel{
    SupportForward: tea.Bool(false),
    LastMessageI18n: imGroupOpenSpaceModelLastMessageI18n,
    SearchSupport: imGroupOpenSpaceModelSearchSupport,
    Notification: imGroupOpenSpaceModelNotification,
  }
  imSingleOpenSpaceModelNotification := &dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenSpaceModelNotification{
    AlertContent: tea.String("你收到了1条卡片消息"),
    NotificationOff: tea.Bool(false),
  }
  imSingleOpenSpaceModelSearchSupport := &dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("@lALPDgQ9q8hFhlHNAXzNAqI"),
    SearchTypeName: tea.String("{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}"),
    SearchDesc: tea.String("卡片的具体描述"),
  }
  imSingleOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("互动卡片消息"),
  }
  imSingleOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenSpaceModel{
    SupportForward: tea.Bool(true),
    LastMessageI18n: imSingleOpenSpaceModelLastMessageI18n,
    SearchSupport: imSingleOpenSpaceModelSearchSupport,
    Notification: imSingleOpenSpaceModelNotification,
  }
  openDynamicDataConfigDynamicDataSourceConfigs0PullConfig := &dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig{
    PullStrategy: tea.String("INTERVAL"),
    Interval: tea.Int32(600),
    TimeUnit: tea.String("SECONDS"),
  }
  openDynamicDataConfigDynamicDataSourceConfigs0ConstParams := map[string]*string{
    "key": tea.String("example_const_param_value"),
  }
  openDynamicDataConfigDynamicDataSourceConfigs0 := &dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs{
    DynamicDataSourceId: tea.String("example_ds_01"),
    ConstParams: openDynamicDataConfigDynamicDataSourceConfigs0ConstParams,
    PullConfig: openDynamicDataConfigDynamicDataSourceConfigs0PullConfig,
  }
  openDynamicDataConfig := &dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfig{
    DynamicDataSourceConfigs: []*dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs{openDynamicDataConfigDynamicDataSourceConfigs0},
  }
  privateDataValueKeyCardParamMap := map[string]*string{
    "key": tea.String("example_private_value"),
  }
  privateDataValueKey := &dingtalkcard_1_0.PrivateDataValue{
    CardParamMap: privateDataValueKeyCardParamMap,
  }
  privateData := map[string]*dingtalkcard_1_0.PrivateDataValue{
    "privateDataValueKey": privateDataValueKey,
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("example_public_value"),
  }
  cardData := &dingtalkcard_1_0.CreateAndDeliverRequestCardData{
    CardParamMap: cardDataCardParamMap,
  }
  createAndDeliverRequest := &dingtalkcard_1_0.CreateAndDeliverRequest{
    UserId: tea.String("example_user_id"),
    CardTemplateId: tea.String("b4fdsu2119f-9945-4e13-9989-747da19e3bc7"),
    OutTrackId: tea.String("example_out_track_id"),
    CallbackType: tea.String("STREAM"),
    CallbackRouteKey: tea.String("example_route_key"),
    CardData: cardData,
    PrivateData: privateData,
    OpenDynamicDataConfig: openDynamicDataConfig,
    ImSingleOpenSpaceModel: imSingleOpenSpaceModel,
    ImGroupOpenSpaceModel: imGroupOpenSpaceModel,
    ImRobotOpenSpaceModel: imRobotOpenSpaceModel,
    CoFeedOpenSpaceModel: coFeedOpenSpaceModel,
    TopOpenSpaceModel: topOpenSpaceModel,
    OpenSpaceId: tea.String("dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ=="),
    ImSingleOpenDeliverModel: imSingleOpenDeliverModel,
    ImGroupOpenDeliverModel: imGroupOpenDeliverModel,
    ImRobotOpenDeliverModel: imRobotOpenDeliverModel,
    TopOpenDeliverModel: topOpenDeliverModel,
    CoFeedOpenDeliverModel: coFeedOpenDeliverModel,
    DocOpenDeliverModel: docOpenDeliverModel,
    UserIdType: tea.Int32(1),
    CardAtUserIds: []*string{tea.String("example_user_id")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateAndDeliverWithOptions(createAndDeliverRequest, createAndDeliverHeaders, &util.RuntimeOptions{})
    if _err != nil {
      return _err
    }

    return nil
  }()

  if tryErr != nil {
    var err = &tea.SDKError{}
    if _t, ok := tryErr.(*tea.SDKError); ok {
      err = _t
    } else {
      err.Message = tea.String(tryErr.Error())
    }
    if !tea.BoolValue(util.Empty(err.Code)) && !tea.BoolValue(util.Empty(err.Message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }

  }
  return _err
}

func main() {
  err := _main(tea.StringSlice(os.Args[1:]))
  if err != nil {
    panic(err)
  }
}
```

Node.js

```
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkcard_1_0 = require('@alicloud/dingtalk/card_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkcard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createAndDeliverHeaders = new dingtalkcard_1_0.CreateAndDeliverHeaders({ });
    createAndDeliverHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let docOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverRequestDocOpenDeliverModel({
      userId: 'example_user_id',
    });
    let coFeedOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverRequestCoFeedOpenDeliverModel({
      bizTag: 'example_biz_tag',
      gmtTimeLine: 1665473229000,
    });
    let topOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverRequestTopOpenDeliverModel({
      expiredTimeMillis: 1665473229000,
      userIds: [
        'example_user_id'
      ],
      platforms: [
        'android'
      ],
    });
    let imRobotOpenDeliverModelExtension = {
      key: 'example_ext_value',
    };
    let imRobotOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenDeliverModel({
      spaceType: 'IM_ROBOT',
      robotCode: 'example_robot_code',
      extension: imRobotOpenDeliverModelExtension,
    });
    let imGroupOpenDeliverModelExtension = {
      key: 'example_ext_value',
    };
    let imGroupOpenDeliverModelAtUserIds = {
      key: 'example_user_name',
    };
    let imGroupOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenDeliverModel({
      robotCode: 'example_robot_code',
      atUserIds: imGroupOpenDeliverModelAtUserIds,
      recipients: [
        'example_user_id'
      ],
      extension: imGroupOpenDeliverModelExtension,
    });
    let imSingleOpenDeliverModelExtension = {
      key: 'example_ext_value',
    };
    let imSingleOpenDeliverModelAtUserIds = {
      key: 'example_user_name',
    };
    let imSingleOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenDeliverModel({
      atUserIds: imSingleOpenDeliverModelAtUserIds,
      extension: imSingleOpenDeliverModelExtension,
    });
    let topOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverRequestTopOpenSpaceModel({
      spaceType: 'ONE_BOX',
    });
    let coFeedOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverRequestCoFeedOpenSpaceModel({
      title: 'xxxx卡片',
      coolAppCode: 'coolAppCode123',
    });
    let imRobotOpenSpaceModelNotification = new dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenSpaceModelNotification({
      alertContent: '你收到了1条卡片消息',
      notificationOff: false,
    });
    let imRobotOpenSpaceModelSearchSupport = new dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport({
      searchIcon: '@lALPDgQ9q8hFhlHNAXzNAqI',
      searchTypeName: '{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
      searchDesc: '卡片的具体描述',
    });
    let imRobotOpenSpaceModelLastMessageI18n = {
      key: '互动卡片消息',
    };
    let imRobotOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverRequestImRobotOpenSpaceModel({
      supportForward: false,
      lastMessageI18n: imRobotOpenSpaceModelLastMessageI18n,
      searchSupport: imRobotOpenSpaceModelSearchSupport,
      notification: imRobotOpenSpaceModelNotification,
    });
    let imGroupOpenSpaceModelNotification = new dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenSpaceModelNotification({
      alertContent: '你收到了1条卡片消息',
      notificationOff: false,
    });
    let imGroupOpenSpaceModelSearchSupport = new dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport({
      searchIcon: '@lALPDgQ9q8hFhlHNAXzNAqI',
      searchTypeName: '{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
      searchDesc: '卡片的具体描述',
    });
    let imGroupOpenSpaceModelLastMessageI18n = {
      key: '互动卡片消息',
    };
    let imGroupOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverRequestImGroupOpenSpaceModel({
      supportForward: false,
      lastMessageI18n: imGroupOpenSpaceModelLastMessageI18n,
      searchSupport: imGroupOpenSpaceModelSearchSupport,
      notification: imGroupOpenSpaceModelNotification,
    });
    let imSingleOpenSpaceModelNotification = new dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenSpaceModelNotification({
      alertContent: '你收到了1条卡片消息',
      notificationOff: false,
    });
    let imSingleOpenSpaceModelSearchSupport = new dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport({
      searchIcon: '@lALPDgQ9q8hFhlHNAXzNAqI',
      searchTypeName: '{"ZH_CN":"待办","ZH_TW":"待辦","EN_US":"ToDo"}',
      searchDesc: '卡片的具体描述',
    });
    let imSingleOpenSpaceModelLastMessageI18n = {
      key: '互动卡片消息',
    };
    let imSingleOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverRequestImSingleOpenSpaceModel({
      supportForward: true,
      lastMessageI18n: imSingleOpenSpaceModelLastMessageI18n,
      searchSupport: imSingleOpenSpaceModelSearchSupport,
      notification: imSingleOpenSpaceModelNotification,
    });
    let openDynamicDataConfigDynamicDataSourceConfigs0PullConfig = new dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig({
      pullStrategy: 'INTERVAL',
      interval: 600,
      timeUnit: 'SECONDS',
    });
    let openDynamicDataConfigDynamicDataSourceConfigs0ConstParams = {
      key: 'example_const_param_value',
    };
    let openDynamicDataConfigDynamicDataSourceConfigs0 = new dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs({
      dynamicDataSourceId: 'example_ds_01',
      constParams: openDynamicDataConfigDynamicDataSourceConfigs0ConstParams,
      pullConfig: openDynamicDataConfigDynamicDataSourceConfigs0PullConfig,
    });
    let openDynamicDataConfig = new dingtalkcard_1_0.CreateAndDeliverRequestOpenDynamicDataConfig({
      dynamicDataSourceConfigs: [
        openDynamicDataConfigDynamicDataSourceConfigs0
      ],
    });
    let privateDataValueKeyCardParamMap = {
      key: 'example_private_value',
    };
    let privateDataValueKey = new dingtalkcard_1_0.PrivateDataValue({
      cardParamMap: privateDataValueKeyCardParamMap,
    });
    let privateData = {
      privateDataValueKey: privateDataValueKey,
    };
    let cardDataCardParamMap = {
      key: 'example_public_value',
    };
    let cardData = new dingtalkcard_1_0.CreateAndDeliverRequestCardData({
      cardParamMap: cardDataCardParamMap,
    });
    let createAndDeliverRequest = new dingtalkcard_1_0.CreateAndDeliverRequest({
      userId: 'example_user_id',
      cardTemplateId: 'b4fdsu2119f-9945-4e13-9989-747da19e3bc7',
      outTrackId: 'example_out_track_id',
      callbackType: 'STREAM',
      callbackRouteKey: 'example_route_key',
      cardData: cardData,
      privateData: privateData,
      openDynamicDataConfig: openDynamicDataConfig,
      imSingleOpenSpaceModel: imSingleOpenSpaceModel,
      imGroupOpenSpaceModel: imGroupOpenSpaceModel,
      imRobotOpenSpaceModel: imRobotOpenSpaceModel,
      coFeedOpenSpaceModel: coFeedOpenSpaceModel,
      topOpenSpaceModel: topOpenSpaceModel,
      openSpaceId: 'dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==',
      imSingleOpenDeliverModel: imSingleOpenDeliverModel,
      imGroupOpenDeliverModel: imGroupOpenDeliverModel,
      imRobotOpenDeliverModel: imRobotOpenDeliverModel,
      topOpenDeliverModel: topOpenDeliverModel,
      coFeedOpenDeliverModel: coFeedOpenDeliverModel,
      docOpenDeliverModel: docOpenDeliverModel,
      userIdType: 1,
      cardAtUserIds: [
        'example_user_id'
      ],
    });
    try {
      await client.createAndDeliverWithOptions(createAndDeliverRequest, createAndDeliverHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
Client.main(process.argv.slice(2));
```

C#

```
// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

using Tea;
using Tea.Utils;

namespace AlibabaCloud.SDK.Sample
{
    public class Sample 
    {

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverHeaders createAndDeliverHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverHeaders();
            createAndDeliverHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestDocOpenDeliverModel docOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestDocOpenDeliverModel
            {
                UserId = "example_user_id",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenDeliverModel coFeedOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenDeliverModel
            {
                BizTag = "example_biz_tag",
                GmtTimeLine = 1665473229000,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenDeliverModel topOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenDeliverModel
            {
                ExpiredTimeMillis = 1665473229000,
                UserIds = new List<string>
                {
                    "example_user_id"
                },
                Platforms = new List<string>
                {
                    "android"
                },
            };
            Dictionary<string, string> imRobotOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "example_ext_value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenDeliverModel imRobotOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenDeliverModel
            {
                SpaceType = "IM_ROBOT",
                RobotCode = "example_robot_code",
                Extension = imRobotOpenDeliverModelExtension,
            };
            Dictionary<string, string> imGroupOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "example_ext_value"},
            };
            Dictionary<string, string> imGroupOpenDeliverModelAtUserIds = new Dictionary<string, string>
            {
                {"key", "example_user_name"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenDeliverModel
            {
                RobotCode = "example_robot_code",
                AtUserIds = imGroupOpenDeliverModelAtUserIds,
                Recipients = new List<string>
                {
                    "example_user_id"
                },
                Extension = imGroupOpenDeliverModelExtension,
            };
            Dictionary<string, string> imSingleOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "example_ext_value"},
            };
            Dictionary<string, string> imSingleOpenDeliverModelAtUserIds = new Dictionary<string, string>
            {
                {"key", "example_user_name"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenDeliverModel imSingleOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenDeliverModel
            {
                AtUserIds = imSingleOpenDeliverModelAtUserIds,
                Extension = imSingleOpenDeliverModelExtension,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenSpaceModel topOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestTopOpenSpaceModel
            {
                SpaceType = "ONE_BOX",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenSpaceModel coFeedOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestCoFeedOpenSpaceModel
            {
                Title = "xxxx卡片",
                CoolAppCode = "coolAppCode123",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel.CreateAndDeliverRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel.CreateAndDeliverRequestImRobotOpenSpaceModelNotification
            {
                AlertContent = "你收到了1条卡片消息",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel.CreateAndDeliverRequestImRobotOpenSpaceModelSearchSupport
            {
                SearchIcon = "@lALPDgQ9q8hFhlHNAXzNAqI",
                SearchTypeName = "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
                SearchDesc = "卡片的具体描述",
            };
            Dictionary<string, string> imRobotOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "互动卡片消息"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImRobotOpenSpaceModel
            {
                SupportForward = false,
                LastMessageI18n = imRobotOpenSpaceModelLastMessageI18n,
                SearchSupport = imRobotOpenSpaceModelSearchSupport,
                Notification = imRobotOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel.CreateAndDeliverRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel.CreateAndDeliverRequestImGroupOpenSpaceModelNotification
            {
                AlertContent = "你收到了1条卡片消息",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel.CreateAndDeliverRequestImGroupOpenSpaceModelSearchSupport
            {
                SearchIcon = "@lALPDgQ9q8hFhlHNAXzNAqI",
                SearchTypeName = "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
                SearchDesc = "卡片的具体描述",
            };
            Dictionary<string, string> imGroupOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "互动卡片消息"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel
            {
                SupportForward = false,
                LastMessageI18n = imGroupOpenSpaceModelLastMessageI18n,
                SearchSupport = imGroupOpenSpaceModelSearchSupport,
                Notification = imGroupOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel.CreateAndDeliverRequestImSingleOpenSpaceModelNotification imSingleOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel.CreateAndDeliverRequestImSingleOpenSpaceModelNotification
            {
                AlertContent = "你收到了1条卡片消息",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport imSingleOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel.CreateAndDeliverRequestImSingleOpenSpaceModelSearchSupport
            {
                SearchIcon = "@lALPDgQ9q8hFhlHNAXzNAqI",
                SearchTypeName = "{\"ZH_CN\":\"待办\",\"ZH_TW\":\"待辦\",\"EN_US\":\"ToDo\"}",
                SearchDesc = "卡片的具体描述",
            };
            Dictionary<string, string> imSingleOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "互动卡片消息"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel imSingleOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestImSingleOpenSpaceModel
            {
                SupportForward = true,
                LastMessageI18n = imSingleOpenSpaceModelLastMessageI18n,
                SearchSupport = imSingleOpenSpaceModelSearchSupport,
                Notification = imSingleOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig openDynamicDataConfigDynamicDataSourceConfigs0PullConfig = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig
            {
                PullStrategy = "INTERVAL",
                Interval = 600,
                TimeUnit = "SECONDS",
            };
            Dictionary<string, string> openDynamicDataConfigDynamicDataSourceConfigs0ConstParams = new Dictionary<string, string>
            {
                {"key", "example_const_param_value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs openDynamicDataConfigDynamicDataSourceConfigs0 = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs
            {
                DynamicDataSourceId = "example_ds_01",
                ConstParams = openDynamicDataConfigDynamicDataSourceConfigs0ConstParams,
                PullConfig = openDynamicDataConfigDynamicDataSourceConfigs0PullConfig,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig openDynamicDataConfig = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig
            {
                DynamicDataSourceConfigs = new List<AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestOpenDynamicDataConfig.CreateAndDeliverRequestOpenDynamicDataConfigDynamicDataSourceConfigs>
                {
                    openDynamicDataConfigDynamicDataSourceConfigs0
                },
            };
            Dictionary<string, string> privateDataValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "example_private_value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue privateDataValueKey = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue
            {
                CardParamMap = privateDataValueKeyCardParamMap,
            };
            Dictionary<string, AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue> privateData = new Dictionary<string, AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue>
            {
                {"privateDataValueKey", privateDataValueKey},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "example_public_value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest.CreateAndDeliverRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest createAndDeliverRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverRequest
            {
                UserId = "example_user_id",
                CardTemplateId = "b4fdsu2119f-9945-4e13-9989-747da19e3bc7",
                OutTrackId = "example_out_track_id",
                CallbackType = "STREAM",
                CallbackRouteKey = "example_route_key",
                CardData = cardData,
                PrivateData = privateData,
                OpenDynamicDataConfig = openDynamicDataConfig,
                ImSingleOpenSpaceModel = imSingleOpenSpaceModel,
                ImGroupOpenSpaceModel = imGroupOpenSpaceModel,
                ImRobotOpenSpaceModel = imRobotOpenSpaceModel,
                CoFeedOpenSpaceModel = coFeedOpenSpaceModel,
                TopOpenSpaceModel = topOpenSpaceModel,
                OpenSpaceId = "dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==",
                ImSingleOpenDeliverModel = imSingleOpenDeliverModel,
                ImGroupOpenDeliverModel = imGroupOpenDeliverModel,
                ImRobotOpenDeliverModel = imRobotOpenDeliverModel,
                TopOpenDeliverModel = topOpenDeliverModel,
                CoFeedOpenDeliverModel = coFeedOpenDeliverModel,
                DocOpenDeliverModel = docOpenDeliverModel,
                UserIdType = 1,
                CardAtUserIds = new List<string>
                {
                    "example_user_id"
                },
            };
            try
            {
                client.CreateAndDeliverWithOptions(createAndDeliverRequest, createAndDeliverHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
            }
            catch (TeaException err)
            {
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
            catch (Exception _err)
            {
                TeaException err = new TeaException(new Dictionary<string, object>
                {
                    { "message", _err.Message }
                });
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
        }

    }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 调用结果。 |
| result | Object | 创建实例结果。 |
| outTrackId | String | 外部卡片实例Id。 |
| deliverResults | Array | 投放结果。 |
| spaceType | String | 场域类型 ：   - **IM**：IM - **IM\_GROUP**：IM群聊 - **IM\_ROBOT**：IM机器人单聊 - **ONE\_BOX**：群吊顶 |
| spaceId | String | 场域Id。 |
| success | Boolean | 投放成功。 |
| carrierId | String | 投放结果id。      IM场域返回`processQueryKey`，用于业务后续查看消息已读列表，其他场域暂不返回。 |
| errorMsg | String | 错误信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "outTrackId" : "example_out_track_id",
    "deliverResults" : [ {
      "spaceType" : "IM_GROUP",
      "spaceId" : "cidp4Gh*******VCQ==",
      "success" : true,
      "carrierId" : "4v+AzUEDuC0dKuO*********J0w8=",
      "errorMsg" : "SYSTEM_ERROR"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | param.empty | 入参为空 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识outTrackId为空 |
| 400 | param.openSpaceIdEmpty | param.openSpaceIdEmpty | 投放openSpaceId为空 |
| 400 | param.openDeliverModelEmpty | param.openDeliverModelEmpty | 场域投放模型为空 |
| 400 | param.openDeliverModelError | param.openDeliverModelError | 场域投放模型格式错误 |
| 400 | param.openSpaceIdInvalid | param.openSpaceIdInvalid | openSpaceId不符合规范 |
| 400 | param.cardTemplateIdEmpty | param.cardTemplateIdEmpty | 卡片模板Id为空 |
| 400 | param.userIdEmpty | param.userIdEmpty | 用户userId为空 |
| 400 | param.cardPublicDataEmpty | param.cardPublicDataEmpty | 卡片公共数据为空 |
| 400 | param.userIdNotExist | param.userIdNotExist | 用户user不存在 |
| 400 | param.dynamicDataMappingEmpty | param.dynamicDataMappingEmpty | 动态数据源数据映射为空 |
| 400 | param.dynamicSourceIdEmpty | param.dynamicSourceIdEmpty | 动态数据源配置ID为空 |
| 400 | param.dynamicDataPullConfigEmpty | param.dynamicDataPullConfigEmpty | 动态数据源拉取配置为空 |
| 400 | param.dynamicDataPullIntervalInvalid | param.dynamicDataPullIntervalInvalid | 动态数据源拉取间隔时间为空或非法 |
| 400 | param.dynamicDataPullIntervalTimeUnitInvalid | param.dynamicDataPullIntervalTimeUnitInvalid | 动态数据源拉取间隔时间单位为空或非法 |
| 400 | param.dynamicDataSourcePullStrategyEmpty | param.dynamicDataSourcePullStrategyEmpty | 动态数据源拉取策略为空 |
| 400 | param.dynamicDataMappingPathEmpty | param.dynamicDataMappingPathEmpty | 动态数据源数据映射路径为空 |
| 400 | param.dynamicDataValueTypeEmpty | param.dynamicDataValueTypeEmpty | 动态数据源数据类型为空 |
| 400 | param.contentUnsafe | param.contentUnsafe | 卡片数据不能通过安全审查 |
| 400 | param.openSpaceModelInvalid | param.openSpaceModellnvalid | 错误的场域属性模型 |
| 400 | param.cardNotExist | param.cardNotExist | 卡片不存在 |
| 400 | param.cardAlreadyExist | param.cardAlreadyExist | 卡片已经存在 |
| 400 | param.templateNotExist | param.templateNotExist | 模板不存在 |
| 400 | param.templateUnpublished | param.templateUnpublished | 模板未发布 |
| 400 | param.invalid | param.invalid | 存在非法参数 |
| 500 | system.busy | system.busy | 系统繁忙 |
