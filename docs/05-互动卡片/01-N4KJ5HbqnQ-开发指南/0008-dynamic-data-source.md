---
title: "动态数据源"
source_url: "https://open.dingtalk.com/document/development/dynamic-data-source"
namespace: "development"
slug: "dynamic-data-source"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片互动 > 动态数据源"
doc_id: "qx7bw2uLgN"
updated_at: "2026-08-04 09:07:29"
---

> Source: https://open.dingtalk.com/document/development/dynamic-data-source
> Path: 互动卡片 / 开发指南 / 卡片互动 > 动态数据源
> Updated: 2026-08-04 09:07:29

# 动态数据源

通过本文你可以了解到卡片动态数据源的使用和常见问题

## **核心概念**

### **动态数据源**

用户看到一张互动卡片的时候，卡片中的数据来源可以分为如下几类:

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9465085871/p1092605.png)

| **数据类型** | **获取时机** | **更新方式** | **适用场景** |
| --- | --- | --- | --- |
| 卡片公有数据 | 卡片实例创建时 | 调用更新接口变更 | 所有接收人可见的静态信息 |
| 卡片私有数据 | 卡片实例创建时 | 调用更新接口变更 | 特定接收人可见的个性化信息 |
| 动态数据源数据 | 卡片在客户端渲染时 | 回调动态数据源提供方拉取时变更 | 敏感数据、千人千面、定时更新 |

### **主要适用场景**

动态数据源主要在以下场景中使用:

- **敏感数据保护**：发票金额、抬头等不能托管到卡片服务端的数据。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9465085871/p549417.png)
- **千人千面展示**：根据用户权限动态显示/隐藏内容（如查看员工 OKR 时按权限过滤）。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9465085871/p549534.png)
- **定时数据更新**：每日销售额、业务趋势图等需要定期刷新的报表数据。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9465085871/p549535.png)

### **数据源交互流程**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9465085871/p537800.png)

## **前置准备**

在使用动态数据源之前，建议您已经完成了以下的准备工作:

- 了解[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)过程。
- 了解[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)流程和[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)流程。
- 了解[卡片平台投放卡片实例](0005-card-delivery-instance-for-card-platform.md)流程和[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)流程。
- **确保客户端的版本高于 6.5.40**

## **接入方式**

动态数据源的接入方式有两种，一种可以通过卡片搭建平台，在后台创建卡片实例时绑定数据源，一种可以通过开放接口接入的方式完成。

| **接入方式** | **适用场景** | **配置入口** |
| --- | --- | --- |
| 卡片搭建平台接入 | 通过[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md) | 在[卡片平台创建卡片实例 > 步骤二：创建卡片实例 > 完成数据配置](0001-card-template-building-and-publishing.md)实现动态数据源接入。 |
| 开放接口接入 | 通过 API 创建卡片实例 | 调用创建卡片接口时配置 `openDynamicDataConfig` 参数。 |

## **开放接口接入流程**

我们以一张最简单的发票金额动态拉取为例，通过接口接入需要如下几个步骤:

### **注册回调地址**

调用[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)接口，注册动态数据源的回调地址。

回调模式选择：

- **HTTP 模式**：需提供公网可访问域名，钉钉通过 HTTP 请求推送回调
- **Stream 模式**：零公网 IP、零域名、零证书、零网关、零内网穿透，通过 TCP 持久连接接收回调（推荐）

### **配置动态数据源**

调用[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0780-interface-for-creating-a-card-instance.md)接口，在`openDynamicDataConfig`参数中配置动态数据源。在[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)中，动态数据源相关配置参数`openDynamicDataConfig`，通过简单实例，针对`openDynamicDataConfig`参数的解释说明：

#### **核心参数说明**

| **参数** | **说明** | **示例值** |
| --- | --- | --- |
| `dynamicDataSourceConfigs` | 动态数据源配置列表（支持多个） | - |
| `dynamicDataSourceId` | 数据源 ID，需与回调响应一一对应 | `"example_ds_1"` |
| `pullConfig.pullStrategy` | 拉取策略 | - `ONCE`：可查看下方[HTTP 请求示例（ONCE）](#3cea93d3286mt)示例。 - `INTERVAL`：可查看下方[HTTP 请求示例（INTERVAL - 每 30 秒拉取）](#13843aef97qkq)示例。 - `RENDER`：可查看下方[HTTP 请求示例（RENDER - 每次渲染时拉取）](#12e20530e774n)示例。 |
| `pullConfig.timeUnit` | 间隔单位（仅 INTERVAL 策略） | `SECONDS` / `MINUTES` / `HOURS` / `DAYS` |
| `pullConfig.interval` | 间隔时间（仅 INTERVAL 策略，最小 6 秒） | `30` |

#### 三种拉取策略对比

| **策略** | **触发时机** | **适用场景** | **配置示例** |
| --- | --- | --- | --- |
| ONCE | 仅首次查看时拉取一次 | 一次性数据（如审批状态） | `"pullStrategy": "ONCE"` |
| INTERVAL | 按固定间隔定时拉取 | 实时报表、监控数据 | `"pullStrategy": "INTERVAL", "timeUnit": "SECONDS", "interval": 30` |
| RENDER | 每次卡片上屏时拉取 | 高频变化数据、个性化内容 | `"pullStrategy": "RENDER"` |

#### HTTP 请求示例（ONCE）

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "user123",
  "userIdType": 1,
  "cardTemplateId" : "abcd-1234",
  "outTrackId" : "my-out-trarck-id",
  "cardData" : {
    "cardParamMap" : {
    "title": "张三提交的报销单",
    "type": "差旅费",
    "reason": "出差费用",
    "status": "未审批",
    "amount": "" 	//需要通过动态数据源获取的数据的字段，可以为空
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

import java.util.ArrayList;
import java.util.List;

import com.aliyun.dingtalkcard_1_0.models.*;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfig;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig;
import com.aliyun.tea.*;

public class Sample {

    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();

        //组装动态数据源配置
        CreateCardRequestOpenDynamicDataConfig openDynamicDataConfig = new CreateCardRequestOpenDynamicDataConfig();

        //数据源配置列表
        List<CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs> configs = new ArrayList<>();
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs configs1 = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs();
        //数据源id
        configs1.dynamicDataSourceId = "example_ds_1";

        //数据源拉取策略
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig pullConfig = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig();
        pullConfig.pullStrategy = "ONCE";
        configs1.setPullConfig(pullConfig);
      
        configs.add(configs1);
        openDynamicDataConfig.dynamicDataSourceConfigs = configs;

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("my-user-id")
            .setUserIdType(1)
            .setOutTrackId("out-track-id")
            .setCardTemplateId("card-template-id")
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

#### HTTP 请求示例（INTERVAL - 每 30 秒拉取）

> **[!NOTE]**
>
> - **timeUnit**：拉取间隔时间的单位，支持 **SECONDS**、**MINUTES**、**HOURS**、**DAYS**。
> - **interval**：拉取间隔，如果 `timeUnit` 为 **SECONDS** 时，`interval` 最小值为 6，即拉取间隔最小为 6 秒。

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "user123",
  "userIdType": 1,
  "cardTemplateId" : "abcd-1234",
  "outTrackId" : "my-out-trarck-id",
  "cardData" : {
    "cardParamMap" : {
    "title": "张三提交的报销单",
    "type": "差旅费",
    "reason": "出差费用",
    "status": "未审批",
    "amount": "" 	//需要通过动态数据源获取的数据的字段，可以为空
    }
  },
	"openDynamicDataConfig":{
  	"dynamicDataSourceConfigs":[
    	{
      	"dynamicDataSourceId":"example_ds_1",   // 动态数据源 ID
        "pullConfig": {		
        	"pullStrategy": "INTERVAL",	// 间隔拉取
        	"timeUnit": "SECONDS",		// 拉取间隔时间的单位
        	"interval": "30"	  // 拉取间隔时间
      	}
      }
    ]
  }
}
```

Java

```
package com.aliyun.sample;

import java.util.ArrayList;
import java.util.List;

import com.aliyun.dingtalkcard_1_0.models.*;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfig;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig;
import com.aliyun.tea.*;

public class Sample {

    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();

        //组装动态数据源配置
        CreateCardRequestOpenDynamicDataConfig openDynamicDataConfig = new CreateCardRequestOpenDynamicDataConfig();
        //字段映射类型默认填写REPLACE_WITHOUT_MAPPING
        openDynamicDataConfig.dynamicDataMappingMethod = "REPLACE_WITHOUT_MAPPING";

        //数据源配置列表
        List<CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs> configs = new ArrayList<>();
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs configs1 = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs();
        //数据源id
        configs1.dynamicDataSourceId = "example_ds_1";

        //数据源拉取策略
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig pullConfig = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig();
        pullConfig.pullStrategy = "INTERVAL";
      	pullConfig.interval=30;
        pullConfig.timeUnit="SECONDS";
        configs1.setPullConfig(pullConfig);

        configs.add(configs1);

        openDynamicDataConfig.dynamicDataSourceConfigs = configs;

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("my-user-id")
            .setUserIdType(1)
            .setOutTrackId("out-track-id")
            .setCardTemplateId("card-template-id")
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

#### HTTP 请求示例（RENDER - 每次渲染时拉取）

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
    "userId": "user123",
    "userIdType": 1,
    "cardTemplateId": "abcd-1234",
    "outTrackId": "my-out-trarck-id",
    "cardData": {
        "cardParamMap": {
            "title": "张三提交的报销单",
            "type": "差旅费",
            "reason": "出差费用",
            "status": "未审批",
            "amount": ""       //需要通过动态数据源获取的数据的字段，可以为空
        }
    },
    "openDynamicDataConfig": {
        "dynamicDataSourceConfigs": [
            {
                "dynamicDataSourceId": "example_ds_1",     // 动态数据源 ID
                "pullConfig": {
                    "pullStrategy": "RENDER"    // 拉取策略
                }
            }
        ]
    }
}
```

Java

```
package com.aliyun.sample;

import java.util.ArrayList;
import java.util.List;

import com.aliyun.dingtalkcard_1_0.models.*;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfig;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig;
import com.aliyun.tea.*;

public class Sample {

    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();

        //组装动态数据源配置
        CreateCardRequestOpenDynamicDataConfig openDynamicDataConfig = new CreateCardRequestOpenDynamicDataConfig();
        //字段映射类型默认填写REPLACE_WITHOUT_MAPPING
        openDynamicDataConfig.dynamicDataMappingMethod = "REPLACE_WITHOUT_MAPPING";

        //数据源配置列表
        List<CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs> configs = new ArrayList<>();
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs configs1 = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs();
        //数据源id
        configs1.dynamicDataSourceId = "example_ds_1";

        //数据源拉取策略
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig pullConfig = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig();
        pullConfig.pullStrategy = "RENDER";
        configs1.setPullConfig(pullConfig);

        configs.add(configs1);

        openDynamicDataConfig.dynamicDataSourceConfigs = configs;

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("my-user-id")
            .setUserIdType(1)
            .setOutTrackId("out-track-id")
            .setCardTemplateId("card-template-id")
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

### 实现回调接口

#### **回调请求格式**

钉钉向注册的 URL 发送 POST 请求：

```
{
  "type": "dynamicDataCallback",						// 标识回调类型为动态数据源
  "corpId": "corp1234",											// 触发人的企业 ID
  "userId": "user0",												// 触发人的 userId
  "outTrackId": "testOutTrackId",					  // 卡片 ID
  "content": "{\"dynamicDataSourceQueryRequests\": [{\"dynamicDataSourceId\": \"example_ds_1\"}}"
}
```

content：这是JSONString格式，解析后为如下样式：

```
"content": {
    "dynamicDataSourceQueryRequests": [
        {
            "dynamicDataSourceId": "example_ds_1" // 请求动态数据源 ID
        }
    ]
}
```

#### 回调响应格式

处理完请求后，返回以下格式更新卡片数据：

```
{
  "dataSourceQueryResponses": [
    {
      "data": "{\"amount\":\"1000元\"}", // 返回的动态数据，端上直接覆盖并渲染
      "dynamicDataSourceId": "example_ds_1", // 动态数据源 ID
      "dynamicDataValueType": "OBJECT"	// 动态数据的类型，支持 STRING、ARRAY、OBJECT 等
    }
  ]
}
```

| **字段** | **说明** | **可选值** |
| --- | --- | --- |
| `data` | 返回的动态数据（JSON String），端上直接覆盖渲染 | - |
| `dynamicDataSourceId` | 对应的数据源 ID | 与请求一致。 |
| `dynamicDataValueType` | 数据类型 | `STRING` / `ARRAY` / `OBJECT` |

#### HTTP 模式安全校验

如[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)时提供了"卡片数据回调 apiSecret"，钉钉会在请求 Header 中包含签名：

• `x-ddpaas-signature-timestamp`：签名时间戳

• `x-ddpaas-signature`：签名串 = calcSignature(apiSecret, <签名时间戳>)

Java 签名验证示例：

```
public static String calcSignature(String apiSecret, long ts) {
  try {
    Mac mac = Mac.getInstance("HmacSHA256");
    SecretKeySpec key = new SecretKeySpec(apiSecret.getBytes(), "HmacSHA256");
    mac.init(key);
    return Base64.getEncoder()
      .encodeToString(mac.doFinal(Long.toString(ts).getBytes()));
  } catch (NoSuchAlgorithmException | InvalidKeyException e) {
    throw new GatewayException(ErrorCodeConstant.SYSTEM_ERROR,
                               "sign api secret failed", e);
  }
}
```

### **效果展示**

| **动态数据拉取前** | **动态数据拉取后** |
| --- | --- |
| image | image |

## **注意事项**

- 动态数据源回调有超时（TIMEOUT）限制，请在 2 秒内完成业务处理并响应。
- 如果有比较耗时的业务逻辑处理（比如调用大模型），考虑异步调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)的方式来更新卡片。
- 请勿在回调过程中调用更新接口。
