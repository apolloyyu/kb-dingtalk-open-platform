---
title: "开放接口创建卡片实例"
source_url: "https://open.dingtalk.com/document/development/open-the-interface-to-create-a-card-instance"
namespace: "development"
slug: "open-the-interface-to-create-a-card-instance"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片创建 > 开放接口创建卡片实例"
doc_id: "ZJUe1HO5et"
updated_at: "2026-08-04 09:07:22"
---

> Source: https://open.dingtalk.com/document/development/open-the-interface-to-create-a-card-instance
> Path: 互动卡片 / 开发指南 / 卡片创建 > 开放接口创建卡片实例
> Updated: 2026-08-04 09:07:22

# 开放接口创建卡片实例

本文介绍了通过开放接口创建卡片实例。

## **核心概念**

前文提到互动卡片是由**卡片模板**和**卡片数据**构成的， 创建卡片实例是将卡片模板和卡片数据关联起来进行**实例化**的过程。完成创建后即可针对卡片实例进行数据更新、投放等操作。

详情参见[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0780-interface-for-creating-a-card-instance.md)接口。

### **卡片数据**

卡片的数据分为公共数据和私有数据，公共数据是所有用户都可见的数据，私有数据是只有每个用户自己可见的数据。创建卡片的时候可以设置卡片实例的公共数据和私有数据。

创建卡片后，也可以通过[卡片更新](0009-card-update.md)来主动更新卡片的公共数据和私有数据。

### **动态数据源属性**

卡片的公共数据和私有数据都是存储在卡片服务端的，同时，卡片也允许用户将一些敏感、需要定时更新，或者需要针对不同人定制的数据，存放在用户处。这种数据叫动态数据，卡片服务端会根据用户在创建卡片时配置的规则，到用户处拉取数据。对于拉取到的数据，卡片服务端不会进行存储，而是直接渲染卡片。更多详情参见[动态数据源](0008-dynamic-data-source.md)。

### **多场域属性**

一张卡片可以同时存在于多个场域，例如一张在 IM 群聊里的卡片可以同时出现在群聊吊顶中。如果卡片需要投放到某个场域，那么需要在创建的时候就在卡片实例上添加该场域的属性。例如，如果卡片需要投放到 IM 群聊场域中，可以配置卡片在该场域下的通知内容、是否支持转发等。

下图展示了一张同时存在于 IM 群聊、吊顶中的卡片。

![投放效果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2170650471/p790886.png)

目前可用的场域、以及如何配置和添加场域信息参见：

- 通过服务端API-[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0780-interface-for-creating-a-card-instance.md)接口，实现场域的添加。
- 通过服务端API-[新增或者更新卡片的场域信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0787-add-field-interface.md)接口，实现对场域信息的添加和更新操作，详情参见[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)。

## **前置准备**

在创建卡片实例之前，确保你已经完成：

- 在卡片平台上完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)。

## **步骤一：创建卡片**

一张基本的卡片可以包含这几个基本信息：

- `userId`： 创建卡片的用户的 ID，非必填，不超过100个字符
- `userIdType`：卡片使用的用户 ID 的类型，1 为 userId 模式，2 为 unionId 模式，默认为 1
- `cardTemplateId`：卡片模板的 ID，在[卡片模板搭建及发布](../03-MhNX42mFB1-模板搭建器/0001-card-template-overview.md)后获取
- `outTrackId`：卡片 ID。这是开发者自定义的，后续对卡片的投放和互动操作，均是通过 outTrackId 来完成，不超过100个字符
- `cardData`：卡片的公共数据
- `privateData`：卡片的私有数据

调用服务端API-[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0780-interface-for-creating-a-card-instance.md)接口实现卡片实例的创建。

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "example-user-id",
  "userIdType": 1,
  "cardTemplateId" : "example-template-id",
  "outTrackId" : "example-out-track-id",
  "cardData" : {
    "cardParamMap" : {
      "param1" : "example_value"				    // 模板上配置的卡片参数
    }
  },
  "privateData" : {
    "example_user_id" : {								    // 用户 ID
      "cardParamMap" : {
        "privateParam1" : "example_value"   // 模板上配置的卡片私有参数
      }
    }
  }
}
```

Java

```
package com.aliyun.sample;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.dingtalkcard_1_0.models.CreateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.tea.TeaConverter;
import com.aliyun.tea.TeaException;
import com.aliyun.tea.TeaPair;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.teautil.Common;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        List<String> args = Arrays.asList(args_);
        Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("example--user-id")
            .setUserIdType(1)
            .setOutTrackId("example-out-track-id")
            .setCardTemplateId("example-template-id")
            .setCardData(cardData)
            .setPrivateData(privateData);
        try {
            client.createCardWithOptions(createCardRequest, createCardHeaders,
                new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!Common.empty(err.code) && !Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }
        }
    }
}
```

> **[!NOTE]**
>
> - 卡片非 String 类型属性的填写请参考：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0789-instructions-for-filling-in-api-card-data.md)。
> - `userIdType` 字段的填写请参考：[卡片数据与参数配置-userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0790-faq-card.md#8607bdd785avq)。
> - 总大小控制在100KB以内

## **步骤二：设置卡片的高级属性**

如果想使用卡片的高级功能，比如多场域或者动态数据源，要在上述创建卡片步骤的基础上，设置卡片的多场域属性或者动态数据源属性。

### **添加多场域属性**

卡片在投放到某个场域之前，需要在卡片上配置该场域的属性。卡片的场域属性可以在创建的时候配置，也可以在创建后补加。下面介绍在创建卡片的时候配置场域属性，如何在创建好的卡片上添加场域属性以及将卡片投放到场域，详情参见[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)。

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "example_user_id",
  "userIdType": 1,
  "cardTemplateId" : "example_template_id",
  "outTrackId" : "example_out_track_id",
  "cardData" : {
    "cardParamMap" : {
      "param1" : "example_value"        // 模板上配置的卡片参数
    }
  },
  "privateData" : {
    "example_user_id" : {        // 用户 ID
      "cardParamMap" : {
        "privateParam1" : "example_value"   // 模板上配置的卡片私有参数
      }
    }
  },
  "imSingleOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
       "ZH_CN": "卡片", 
       "EN_US": "card"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了一个卡片消息",
      "isNotificationOff" : false
    }
  },
  "imGroupOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
       "ZH_CN": "卡片", 
       "EN_US": "card"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了一个卡片消息",
      "isNotificationOff" : false
    }
  },
  "imRobotOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
       "ZH_CN": "卡片", 
       "EN_US": "card"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了一个卡片消息",
      "isNotificationOff" : false
    }
  },
  "topOpenSpaceModel" : {
    "spaceType" : "ONE_BOX"
  }
}
```

Java

```
package com.aliyun.sample;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.dingtalkcard_1_0.models.CreateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.tea.TeaConverter;
import com.aliyun.tea.TeaException;
import com.aliyun.tea.TeaPair;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.teautil.Common;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        List<String> args = Arrays.asList(args_);
        Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();
      
        // 吊顶场域属性
        CreateCardRequest.CreateCardRequestTopOpenSpaceModel topOpenSpaceModel = new CreateCardRequest.CreateCardRequestTopOpenSpaceModel()
            .setSpaceType("ONE_BOX");
      
        // 人与人单聊场域属性
        // 通知属性
        CreateCardRequest.CreateCardRequestImSingleOpenSpaceModelNotification imSingleOpenSpaceModelNotification = new CreateCardRequest.CreateCardRequestImSingleOpenSpaceModelNotification()
            .setAlertContent("你收到了一个卡片消息")
            .setNotificationOff(false);
        // 搜索属性
        CreateCardRequest.CreateCardRequestImSingleOpenSpaceModelSearchSupport imSingleOpenSpaceModelSearchSupport = new CreateCardRequest.CreateCardRequestImSingleOpenSpaceModelSearchSupport()
            .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
            .setSearchTypeName("{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}")
            .setSearchDesc("卡片的具体描述");
        // lastMessage属性
        Map<String, String> imSingleOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("ZH_CN", "卡片"),
            new TeaPair("EN_US", "card"}")
        );
        CreateCardRequest.CreateCardRequestImSingleOpenSpaceModel imSingleOpenSpaceModel = new CreateCardRequest.CreateCardRequestImSingleOpenSpaceModel()
            .setSupportForward(false)
            .setLastMessageI18n(imSingleOpenSpaceModelLastMessageI18n)
            .setSearchSupport(imSingleOpenSpaceModelSearchSupport)
            .setNotification(imSingleOpenSpaceModelNotification);

        // 群聊场域属性
        // 通知属性
        CreateCardRequest.CreateCardRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new CreateCardRequest.CreateCardRequestImGroupOpenSpaceModelNotification()
            .setAlertContent("你收到了一个卡片消息")
            .setNotificationOff(false);
        // 搜索属性
        CreateCardRequest.CreateCardRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new CreateCardRequest.CreateCardRequestImGroupOpenSpaceModelSearchSupport()
            .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
            .setSearchTypeName("{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}")
            .setSearchDesc("卡片的具体描述");
        // lastMessage属性
        Map<String, String> imGroupOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("ZH_CN", "卡片"),
            new TeaPair("EN_US", "card"}")
        );
        CreateCardRequest.CreateCardRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new CreateCardRequest.CreateCardRequestImGroupOpenSpaceModel()
            .setSupportForward(false)
            .setLastMessageI18n(imGroupOpenSpaceModelLastMessageI18n)
            .setSearchSupport(imGroupOpenSpaceModelSearchSupport)
            .setNotification(imGroupOpenSpaceModelNotification);

        // 人与机器人单聊场域属性
        // 通知属性
        CreateCardRequest.CreateCardRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new CreateCardRequest.CreateCardRequestImRobotOpenSpaceModelNotification()
            .setAlertContent("你收到了一个卡片消息")
            .setNotificationOff(false);
        // 搜索属性
        CreateCardRequest.CreateCardRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new CreateCardRequest.CreateCardRequestImRobotOpenSpaceModelSearchSupport()
            .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
            .setSearchTypeName("{\"zh_CN\":\"示例\",\"zh_TW\":\"示例\",\"en_US\":\"Example\"}")
            .setSearchDesc("卡片的具体描述");
        // lastMessage属性
        Map<String, String> imRobotOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("ZH_CN", "卡片"),
            new TeaPair("EN_US", "card"}")
        );
        CreateCardRequest.CreateCardRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new CreateCardRequest.CreateCardRequestImRobotOpenSpaceModel()
            .setSupportForward(false)
            .setLastMessageI18n(imRobotOpenSpaceModelLastMessageI18n)
            .setSearchSupport(imRobotOpenSpaceModelSearchSupport)
            .setNotification(imRobotOpenSpaceModelNotification);

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("example-user-id")
            .setUserIdType(1)
            .setOutTrackId("example-out-track-id")
            .setCardTemplateId("example-template-id")
            .setCardData(cardData)
            .setPrivateData(privateData)
            .setImSingleOpenSpaceModel(imSingleOpenSpaceModel)
            .setImGroupOpenSpaceModel(imGroupOpenSpaceModel)
            .setImRobotOpenSpaceModel(imRobotOpenSpaceModel)
            .setTopOpenSpaceModel(topOpenSpaceModel);
        try {
            client.createCardWithOptions(createCardRequest, createCardHeaders,
                new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!Common.empty(err.code) && !Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }
        }
    }
}
```

### **添加动态数据源属性**

在创建卡片的时候，可以配置卡片的动态数据源属性。下例创建了一个简单的具有动态数据源属性的卡片，动态数据源相关配置的参数为`openDynamicDataConfig`，详情参见[动态数据源](0008-dynamic-data-source.md)。

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "example_user_id",
  "userIdType": 1,
  "cardTemplateId" : "example_template_id",
  "outTrackId" : "example_out_track_id",
  "cardData" : {
    "cardParamMap" : {
    "title": "张三提交的报销单",
    "type": "差旅费",
    "reason": "出差费用",
    "status": "未审批",
    "amount": "" 			  //需要通过动态数据源获取的数据的字段，可以为空
    }
  },
	"openDynamicDataConfig":{
  	"dynamicDataSourceConfigs":[
    	{
      	"dynamicDataSourceId":"example_ds_1", //数据源id
        "pullConfig": {													
        	"pullStrategy": "ONCE"   //只需要获取一次											
      	}
      }
    ]
  }
}
```

Java

```
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = GetTokenTest.createClient();
        com.aliyun.dingtalkcard_1_0.models.CreateCardHeaders createCardHeaders
            = new com.aliyun.dingtalkcard_1_0.models.CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        com.aliyun.dingtalkcard_1_0.models.PrivateDataValue privateDataValueKey
            = new com.aliyun.dingtalkcard_1_0.models.PrivateDataValue();
        java.util.Map<String, com.aliyun.dingtalkcard_1_0.models.PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestCardData cardData
            = new com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestCardData();
        com.aliyun.dingtalkcard_1_0.models.CreateCardRequest createCardRequest
            = new com.aliyun.dingtalkcard_1_0.models.CreateCardRequest()
            .setUserId("example-user-id")
            .setUserIdType(1)
            .setOutTrackId("example-out-track-id")
            .setCardTemplateId("example-template-id")
            .setCardData(cardData)
            .setPrivateData(privateData);
        try {
            client.createCardWithOptions(createCardRequest, createCardHeaders,
                new com.aliyun.teautil.models.RuntimeOptions());
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
