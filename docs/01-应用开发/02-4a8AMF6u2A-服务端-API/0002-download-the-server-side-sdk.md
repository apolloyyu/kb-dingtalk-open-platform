---
title: "服务端SDK下载"
source_url: "https://open.dingtalk.com/document/development/download-the-server-side-sdk"
namespace: "development"
slug: "download-the-server-side-sdk"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "API 调用指南 > 服务端SDK下载"
doc_id: "5sZqhSBh98"
updated_at: "2026-08-25 09:36:28"
---

> Source: https://open.dingtalk.com/document/development/download-the-server-side-sdk
> Path: 应用开发 / 服务端 API / API 调用指南 > 服务端SDK下载
> Updated: 2026-08-25 09:36:28

# 服务端SDK下载

钉钉官方提供了统一的SDK，使用SDK可以便捷地调用服务端API。

> **[!IMPORTANT]**
>
> 在使用钉钉接口前，请先确认接口版本（新版或旧版），然后下载对应版本的 SDK 或引入对应的 Maven 依赖进行调用：**注意：新旧两个版本的 SDK 不可混用。**
>
> - **旧版接口**：请参考本文「[旧版服务端SDK](#section-q8u-97x-mxu)」说明，使用[旧版工具包](#sectiondiv-d1x-qb4-rrq)，**Maven 版本固定为**`2.0.0`。
> - **新版接口**：请参考本文「[新版服务端SDK](#section-3uc-c2m-3no) 」说明，使用[新版工具包](#e2287636e4q62)，**Maven 最新版本为**`2.2.62`。

## 新版API VS 旧版API

为提升接口使用体验并提供更规范的开发标准，钉钉开放平台对服务端API进行了规范升级。目前平台同时支持旧版服务端API（基于旧版规范）和新版服务端API（基于新版RESTful风格规范）。建议新应用优先接入新版API以获得持续的能力更新和技术支持。

> **[!NOTE]**
>
> 旧版服务端API与新版服务端API所开放的产品能力不完全一致。请根据业务需求选择合适的API版本。已有应用可继续使用旧版API，但新增功能推荐使用新版API。

### **标识的差异**

- 旧版接口的访问域名为`https://oapi.dingtalk.com/`，如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1079592871/p1084445.png)
- 新版接口的访问域名为`https://api.dingtalk.com/`、`v1.0`表示当前接口版本，如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1079592871/p1084446.png)

### **如何选择SDK**

| API版本 | 旧版服务端API | 新版服务端API |
| --- | --- | --- |
| SDK | 使用[旧版服务端SDK](#section-q8u-97x-mxu)，旧版支持版本：Java、PHP、Python、.NET、.NET Core。 | 使用[新版服务端SDK](#section-3uc-c2m-3no)，新版支持版本：Java（支持通过Maven安装）、Node.js、PHP、Go、C#、Python。 |
| 开放的产品能力 | - 现状：旧版服务端API和新版服务端API开放的产品能力不同，即新版服务端API未包含全部的服务端API的产品能力，请根据实际需求，选择需要的API接入。 - 计划：后续将逐步把旧版API迁移至新版规范，最终实现功能全覆盖。 | |
| 是否开放新能力 | 不再开放新能力。 | 持续开放新能力。 |
| 是否推荐 | 已接入的应用可继续使用，接口不会下线。 | 若新版本存在对应接口，推荐接入新版服务端API。 |

## 新版服务端SDK

新版SDK基于阿里云OpenAPI规范构建，推荐新项目优先使用。支持多语言接入，可通过包管理工具快速集成。

### **请求示例**

新版SDK与旧版SDK有所差别，以下是关于新版接口的使用示例，以创建日程为例：

```
  /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcalendar_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcalendar_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcalendar_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventHeaders createEventHeaders = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventHeaders();
        createEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRichTextDescription richTextDescription = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRichTextDescription()
                .setText("<div class=\"__aliyun_email_body_block\"><div  style=\"clear:both;\"><span  style=\"text-decoration:line-through;\">测试测试</span></div><div  style=\"clear:both;\"><span  style=\"color:#ff0000;\">热热热</span></div><div  style=\"clear:both;\"><span  style=\"text-decoration:underline;\">单独的</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;\">啊啊啊</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;font-style:italic;\">事实上</span></div></div>");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestUiConfigs uiConfigs0 = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestUiConfigs()
                .setUiName("updateEventButton")
                .setUiStatus("hide");
       java.util.Map<String, String> extra = TeaConverter.buildMap(
                new TeaPair("noChatNotification", "true"),
                new TeaPair("noPushNotification","true")
        );
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestOnlineMeetingInfo onlineMeetingInfo = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestOnlineMeetingInfo()
                .setType("dingtalk");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestReminders reminders0 = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestReminders()
                .setMethod("dingtalk")
                .setMinutes(15);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestLocation location = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestLocation()
                .setDisplayName("dingtalk");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestAttendees attendees0 = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestAttendees()
                .setId("iiiP35sJxxx")
                .setIsOptional(false);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrenceRange recurrenceRange = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrenceRange()
                .setType("endDate")
                .setEndDate("2021-12-31T10:15:30+08:00")
                .setNumberOfOccurrences(5);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrencePattern recurrencePattern = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrencePattern()
                .setType("daily")
                .setDayOfMonth(1)
                .setDaysOfWeek("monday")
                .setIndex("last")
                .setInterval(1)
                .setFirstDayOfWeek("monday");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrence recurrence = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrence()
                .setPattern(recurrencePattern)
                .setRange(recurrenceRange);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestEnd end = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestEnd()
                .setDate("2020-09-21")
                .setDateTime("2021-09-20T10:15:30+08:00")
                .setTimeZone("Asia/Shanghai");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestStart start = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestStart()
                .setDate("2021-09-20")
                .setDateTime("2021-09-20T10:15:30+08:00")
                .setTimeZone("Asia/Shanghai");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest createEventRequest = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest()
                .setSummary("test event")
                .setDescription("something about this event")
                .setStart(start)
                .setEnd(end)
                .setIsAllDay(false)
                .setRecurrence(recurrence)
                .setAttendees(java.util.Arrays.asList(
                    attendees0
                ))
                .setLocation(location)
                .setReminders(java.util.Arrays.asList(
                    reminders0
                ))
                .setOnlineMeetingInfo(onlineMeetingInfo)
                .setExtra(extra)
                .setUiConfigs(java.util.Arrays.asList(
                    uiConfigs0
                ))
                .setRichTextDescription(richTextDescription);
        try {
            client.createEventWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "primary", createEventRequest, createEventHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
```

其他语言示例代码，可参考具体接口文档中的**示例**模块，我们提供了HTTP、Java、Python、PHP、Go、Node.js、C#等多种方式调用。

### **SDK下载与依赖**

- **Java**

  **方式一**：通过Maven安装DingTalk OpenAPI Java SDK

  添加依赖项到`pom.xml`的文件中，建议始终使用最新版本以获得功能更新与安全修复。

  ```
  <dependency>
   <groupId>com.aliyun</groupId>
   <artifactId>dingtalk</artifactId>
   <version>2.2.62</version>
  </dependency>
  ```

  **方式二**：通过下载[**SDK安装包**](https://open-dev.dingtalk.com/sdk/download/java)进行安装。
- **Go**

  在命令行中，执行以下命令安装DingTalk OpenAPI Go SDK。

  ```
  go get -u github.com/alibabacloud-go/dingtalk/
  ```
- **C#**

  **方式一：**使用`dotnet`来安装C# SDK，最新的SDK版本可以在[这里](https://www.nuget.org/packages/AlibabaCloud.SDK.Dingtalk)查看。

  ```
  dotnet add package AlibabaCloud.SDK.Dingtalk
  ```

  **方式二**：通过下载[**SDK安装包**](https://open-dev.dingtalk.com/sdk/download/csharp)进行安装。
- **PHP**

  **方式一：**使用composer工具进行安装。

  ```
  composer require alibabacloud/dingtalk
  ```

  **方式二**：通过下载[**SDK安装包**](https://open-dev.dingtalk.com/sdk/download/composer)进行安装。
- **Node.js**

  **方式一：**执行以下命令，使用npm安装依赖。

  ```
  npm install @alicloud/dingtalk --save
  ```

  **方式二**：通过下载[**SDK安装包**](https://open-dev.dingtalk.com/sdk/download/nodejs)进行安装。
- **Python**

  **方式一：**执行以下命令，使用pip安装包依赖。

  ```
  pip install alibabacloud_dingtalk
  ```

  **方式二**：通过下载[**SDK安装包**](https://open-dev.dingtalk.com/sdk/download/python)进行安装，Python SDK适用于Python 3.0及以上版本。

## 旧版服务端SDK

旧版SDK基于早期架构设计，仅用于兼容历史接口（URL包含 `/topapi/`）。新项目建议使用新版SDK。

### 请求示例

下面是使用SDK调用API的请求示例：

- Java

  ```
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/get");
  OapiUserGetRequest req = new OapiUserGetRequest();
  req.setUserid("userid1");
  req.setHttpMethod("GET");
  OapiUserGetResponse rsp = client.execute(req, accessToken);
  ```
- PHP

  ```
  include "TopSdk.php";
  // DingTalkConstant::$METHOD_GET 要与下面调用接口url要求的保持一致
  $c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_GET , DingTalkConstant::$FORMAT_JSON);
  $req = new OapiUserGetRequest();
  $req->setUserid("userid1");
  $resp=$c->execute($req, $accessToken,"https://oapi.dingtalk.com/user/get");
  var_dump($resp)
  ```
- Python

  ```
  import dingtalk.api
  request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/user/get")
  request.userid="userid1"
  response = request.getResponse()
  print(response)
  ```
- Node

  ```
  let { Config, OapiProcessinstanceGetParams, OapiProcessinstanceGetRequest } = require('./client.js');
  let Client = require('./client.js').default
  // import Client,{ Config, GetOapiProcessinstanceParams, GetOapiProcessinstanceRequest } from "./client.js";
  async function test() {
    const config = new Config()
    config.serverUrl = 'https://oapi.dingtalk.com/topapi/processinstance/get'
    config.session = 'access_token'
    const params = new OapiProcessinstanceGetParams();
    params.processInstanceId = '23aa6xxxxc1b56c'

    const request = new OapiProcessinstanceGetRequest()
    request.params = params
    const client = new Client(config)
    try {
      const res = await client.oapiProcessinstanceGet(request)
      console.log(res.body)
    } catch (err) {
      console.log(err)
    }
  }
  test()
  ```
- .NET

  ```
  IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/get");
  OapiUserGetRequest req = new OapiUserGetRequest();
  req.Userid = "userid1";
  req.SetHttpMethod("GET");
  // accessToken 参数是需要通过https://open.dingtalk.com/document/development/obtain-orgapp-token接口获取
  OapiUserGetResponse rsp = client.Execute(req, access_token)
  ```

**请求示例说明**：

1. **初始化Client对象**：设置目标接口的完整URI。通常无需手动拼接 `access_token` 等参数；但部分POST接口可能需在URL中附加非token类参数。
2. **构造Request对象**：命名规则一般为 `Oapi + 接口路径驼峰形式 + Request`。例如 `/user/get` 对应 `OapiUserGetRequest`。
3. **设置请求参数**：调用对应setter方法赋值。注意默认HTTP方法为POST，若接口为GET，需显式调用 `setHttpMethod("GET")`。
4. **执行请求**：调用 `client.execute(req, access_token)` 发起调用。对于获取token类接口（如 `/gettoken`、`/sns/gettoken`、`/service/get_suite_token`），调用时无需传入token。
5. **处理响应**：返回结果为与Request对应的Response对象，可从中提取业务数据或错误信息。

### SDK下载与依赖

#### **环境依赖**

- Java SDK 需要依赖 Java SE/EE 1.5及以上
- .NET SDK 需要依赖 .NET Framework 2.0及以上 （不支持Windows Phone平台）

#### 下载地址

- Java版本：

  - JAR包下载：[点击下载](https://open-dev.dingtalk.com/download/openSDK/java)
  - 添加maven依赖：

    ```
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>alibaba-dingtalk-service-sdk</artifactId>
        <version>2.0.0</version>
    </dependency>
    ```
- PHP版本：[点击下载](https://open-dev.dingtalk.com/download/openSDK/php)
- Python版本：[点击下载](https://open-dev.dingtalk.com/download/openSDK/python)
- Python3版本：[点击下载](https://open-dev.dingtalk.com/download/openSDK/python3)
- .NET版本：[点击下载](https://open-dev.dingtalk.com/download/openSDK/cshap)
- .NET Core版本：[点击下载](https://open-dev.dingtalk.com/download/openSDK/netCore)
- Node版本：[点击下载](https://icms-document.oss-cn-beijing.aliyuncs.com/nodeSDK/dingtalk-sdk-nodejs.zip?versionId=CAEQGBiBgMD5xfDg7RciIDQ2MDYxNTc0NDMyODRkY2FhYjI2OGE3MDBhNmYyMTgz)
