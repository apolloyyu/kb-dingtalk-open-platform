---
title: "卡片更新"
source_url: "https://open.dingtalk.com/document/development/card-update"
namespace: "development"
slug: "card-update"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片互动 > 卡片更新"
doc_id: "Vi22O3EV8i"
updated_at: "2026-08-04 09:07:31"
---

> Source: https://open.dingtalk.com/document/development/card-update
> Path: 互动卡片 / 开发指南 / 卡片互动 > 卡片更新
> Updated: 2026-08-04 09:07:31

# 卡片更新

通过本文，你将会了解到如何更新一个互动卡片，如何对某个人的卡片内容做变更。

## **核心概念**

### 卡片更新

当卡片背后承载的业务发生变更的时候，系统希望对应的卡片内容也能及时反映出业务的变化。此时，我们就可以通过调用开放接口，来主动更新卡片的内容，及时给用户反馈当前业务发生的变动。

### 适用场景

> **[!NOTE]**
>
> 如果业务数据变动高频或者对数据刷新及时性不敏感，可使用[动态数据源](0008-dynamic-data-source.md)。

- **审批结果变更**：审批单通过/拒绝后，立即更新卡片状态反馈给所有相关人。
- **订单状态流转**：订单从"待支付"变为"已发货""已完成"等低频但需即时生效的状态变更。
- **任务进度同步**：项目任务完成、里程碑达成等需要主动推送给团队成员的节点性更新。

### 更新数据类型

| **数据类型** | **影响范围** | **适用场景** |
| --- | --- | --- |
| 公有数据更新 | 所有卡片接收者 | 全员可见的业务状态变更（如审批结果）。 |
| 私有数据更新 | 仅指定用户 | 个性化内容变更（如个人待办、权限相关展示）。 |

> **[!NOTE]**
>
> **同时更新**：支持在一次调用中同时更新公有数据和私有数据。

## **更新流程**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4540261761/p537538.png)

## 更新操作示例

### 示例 1：基础更新操作

#### 更新公有数据

调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)接口更新所有接收者可见的公有数据。

**关键参数**：

- `updateCardDataByKey`：设为`true`为增量更新，设为`false`，为全量覆盖（默认）。
- 非 String 类型属性填写参考：：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0789-instructions-for-filling-in-api-card-data.md)。
- `userIdType` 字段填写参考：[卡片数据与参数配置-userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0790-faq-card.md#8607bdd785avq)。

**代码实例**：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "my-out-trarck-id",
  "userIdType" : 1,
  "cardData" : {
    "cardParamMap" : {
      "param1" : "val_changed"
    }
  },
  "cardUpdateOptions" : {
    "updateCardDataByKey" : true
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true);
        UpdateCardRequestCardData cardData = new UpdateCardRequestCardData();
        Map<String,String> cardDataMap = new HashMap<>();
        cardDataMap.put("param1", "val_changed");
        cardData.setCardParamMap(cardDataMap);
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setCardData(cardData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
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

#### 更新私有数据

调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)接口，更新指定用户的私有数据。

**关键参数**：

- `updatePrivateDataByKey`：设为 `true` 为增量更新，`false` 为全量覆盖（默认）
- 非 String 类型属性填写参考：：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0789-instructions-for-filling-in-api-card-data.md)。
- `userIdType` 字段填写参考：[卡片数据与参数配置-userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0790-faq-card.md#8607bdd785avq)。

**代码实例**：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "my-out-trarck-id",
  "userIdType" : 1,
  "privateData" : {
    "user123" : {
      "cardParamMap" : {
        "privateParam1" : "val_changed"
      }
    }
  },
  "cardUpdateOptions" : {
    "updatePrivateDataByKey" : true
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdatePrivateDataByKey(true);
        PrivateDataValue privateDataValueKey = new PrivateDataValue();
        Map<String,String> privateDataMap = new HashMap<>();
        privateDataMap.put("privateParam1", "val_changed");
        privateDataValueKey.setCardParamMap(privateDataMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("user123", privateDataValueKey)
        );
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
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

#### 同时更新公有/私有数据

调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)接口，在一次请求中同时更新公有数据和私有数据。

**关键参数**：

- `updateCardDataByKey`：控制公有数据更新方式。
- `updatePrivateDataByKey`：控制私有数据更新方式。
- 非 String 类型属性填写参考：：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0789-instructions-for-filling-in-api-card-data.md)。
- `userIdType` 字段填写参考：[卡片数据与参数配置-userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0790-faq-card.md#8607bdd785avq)。

**代码实例**：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "my-out-trarck-id",
  "userIdType" : 1,
  "cardData" : {
    "cardParamMap" : {
      "param1" : "val_changed"
    }
  },
  "privateData" : {
    "user123" : {
      "cardParamMap" : {
        "privateParam1" : "val_changed"
      }
    }
  },
  "cardUpdateOptions" : {
    "updatePrivateDataByKey" : true,
    "updateCardDataByKey" : true
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true)
                .setUpdatePrivateDataByKey(true);
        PrivateDataValue privateDataValueKey = new PrivateDataValue();
      	Map<String,String> privateDataMap = new HashMap<>();
        privateDataMap.put("privateParam1", "val_changed");
        privateDataValueKey.setCardParamMap(privateDataMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("userId123", privateDataValueKey)
        );
      
        UpdateCardRequestCardData cardData = new UpdateCardRequestCardData();
        Map<String,String> cardDataMap = new HashMap<>();
        cardDataMap.put("param1", "val_changed");
        cardData.setCardParamMap(cardDataMap);
      
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
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

### 示例 2：审批流完整业务更新

#### 前置说明

首先我们搭建了一个模板如下及模板对应的变量如下所示：

| image | image |
| --- | --- |

其中审批处理按钮只对审批人显示，审批过程中展示正常的审批按钮，审批结束后，展示禁用的审批按钮。

创建卡片时数据如下：

```
{
  "cardData": {
    "cardParamMap": {
      "title": "**的差旅报销",
      "type": "差旅费",
      "reason": "出差费用",
      "amount": "100",
      "status": "未审批"
    }
  },
  "privateData": {
    "userId1": {
      "cardParamMap": {
        "isApprover": "0"
      }
    },
    "userId2": {
      "cardParamMap": {
        "isApprover": "1",
        "isFinished": "0"
      }
    }
  }
}
```

创建后各用户看到的卡片状态：

| **用户视角** | **卡片展示** |
| --- | --- |
| userId1（提交人） | 查看审批单详情，无审批按钮。  image |
| userId2（审批人） | 查看审批单详情，显示"同意""拒绝"按钮。  image |

#### **审批完成后（调用更新接口）**

审批人 userId2 点击"同意"后，审批系统调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)接口，同时更新公有数据（审批状态）和私有数据（禁用按钮）。

**HTTP 请求示例**：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
    "outTrackId":"my-out-trarck-id",
    "userIdType":1,
    "cardData":{
        "cardParamMap":{
            "status":"审批完成"
        }
    },
    "privateData": {
             "userId2": {
                "cardParamMap": {
                		"isFinished": "1"
                }
            }
        }
    "cardUpdateOptions":{
        "updateCardDataByKey":true
        "updatePrivateDataByKey":true
    }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true)
                .setUpdatePrivateDataByKey(true);
        PrivateDataValue privateDataValueKey = new PrivateDataValue();
        Map<String,String> privateDataMap = new HashMap<>();
      	privateDataMap.put("isFinished", "1");
        privateDataValueKey.setCardParamMap(privateDataMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("userId123", privateDataValueKey)
        );
      
        UpdateCardRequestCardData cardData = new UpdateCardRequestCardData();
        Map<String,String> cardDataMap = new HashMap<>();
        cardDataMap.put("status", "审批完成");
        cardData.setCardParamMap(cardDataMap);
      
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
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

**更新后各用户看到的卡片状态**：

| **用户视角** | **更新后展示** |
| --- | --- |
| userId1（提交人） | 审批状态变为"审批完成"。  image |
| userId2（审批人） | 审批状态变为"审批已完成"，审批按钮禁用。  image |

## 视觉效果展示

### **提交审批阶段**

| **审批人视角** | **提交人视角** |
| --- | --- |
| image | image |

### 审批完成阶段

| **审批人视角** | **提交人视角** |
| --- | --- |
| image | image |
