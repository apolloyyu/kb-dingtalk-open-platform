---
title: "开发小程序（HTTP回调）"
source_url: "https://open.dingtalk.com/document/development/develop-mini-programs-http-callback"
namespace: "development"
slug: "develop-mini-programs-http-callback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 开发小程序（HTTP回调）"
doc_id: "WYoBIQ5bWc"
updated_at: "2025-10-16 14:31:49"
---

> Source: https://open.dingtalk.com/document/development/develop-mini-programs-http-callback
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 开发小程序（HTTP回调）
> Updated: 2025-10-16 14:31:49

# 开发小程序（HTTP回调）

通过本教程你将学会使用HTTP回调推送方式开发一个第三方企业小程序。

## 教程介绍

本教程以给登录用户发送一条消息的小程序为例演示小程序开发的完整流程。通过本教程您将学习到：

- 上架市场应用开发、发布的完整流程。
- HTTP推送。
- 应用开通授权。

![发送消息demo](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6038884061/p169831.png)

## 准备工作

- 注册了钉钉管理员账号。若未注册，单击[这里](https://oa.dingtalk.com/register_new.htm?source=1008_OA&lwfrom=2018122711522903000&succJump=oa#/)完成注册。
- 安装小程序开发者工具IDE，单击[这里](https://open.dingtalk.com/document/resourcedownload/miniapp-tool#topic-2625633)下载安装。
- 本教程中的示例Demo使用Java开发，确保您已经安装了Java开发环境（安装JDK）以及Java项目构建工具Maven。
- 安装HTTP穿透工具。

  > **[!IMPORTANT]**
  >
  > 鉴于很多开发者在临时体验开发时往往没有公网域名或者公网IP，本工具提供了一个公网代理服务，目的是方便开发测试。
  >
  > 本工具当前不保证多个开发者随意设置相同的子域名导致的冲突以及通道稳定性，因此正式应用、正式环境必须是真实的公网IP或者域名，正式应用上线绝对不能使用本工具。

  参考以下操作，安装HTTP内网穿透：

  1. 执行以下命令，下载该工具。

     ```
     git clone https://github.com/open-dingtalk/pierced.git
     ```
  2. 在对应的操作系统目录，执行`./ding -config=./ding.cfg -subdomain=域名前缀 端口`命令，启动该工具。

     其中：

     - 域名前缀：您需要使用的域名前缀，该前缀将会匹配到“vaiwan.com”前面，例如你的subdomain是example，启动工具后会将example.vaiwan.com映射到本地。
     - 端口：您需要代理的本地服务http-server端口，例如你本地端口为8080等。

     以Mac为例，执行以下代码启动内网测试工具：

     ```
     cd 下载目录/pierced/mac_64
     ./ding -config=./ding.cfg -subdomain=example 8080
     ```

     启动成功后的页面如下图所示：

     ![http穿透](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8955600061/p166074.png)

## 步骤一：创建应用

参考以下操作，创建应用：

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**应用开发**，选择**第三方企业应用**，然后单击**创建应用**。

   ![p141770 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9353360261/p256635.png)
3. 在弹出的页面，应用类型选择**小程序**，并填写基本信息，然后单击**确定创建**。

   ![create ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3401117161/p259097.png)

## 步骤二：服务端开发

为了帮助开发者快速体验上架应用的开发流程，我们提供了服务端和前端代码示例。

参考以下操作，完成服务端配置：

1. 执行以下代码，下载服务端代码。

   ```
   git clone https://github.com/opendingtalk/eapp-isv-quick-start-java.git
   ```
2. 在[开发者后台](https://open-dev.dingtalk.com/)，单击已创建的第三方小程序应用，完成以下配置：

   1. 单击**开发管理**，然后单击**修改**并完成以下配置：

      | 配置 | 说明 |
      | --- | --- |
      | **服务器出口IP** | 调用钉钉服务端API的公网IP，多个IP用逗号分隔。  本示例使用了内网穿透工具用来测试，输入**127.0.0.1**。 |
      | **推送类型** | 选择**使用HTTP推送**。  钉钉应用广场中上架的第三方企业应用，企业管理员可以授权开通。开通后，钉钉后台会推送授权信息到第三方应用后台。 |
      | **Token** | 自定义固定字符串，必须为英文或数字，长度为3~32个字符。  用于生成签名、校验回调请求的合法性。本应用下相关应用产生的回调消息都使用该值来解密。  本示例中输入**test**。 |
      | **数据加密密钥** | 回调消息加解密参数，是AES密钥的Base64编码，用于解密回调消息内容对应的密文。  本应用下相关应用产生的回调消息都使用该值来解密。  单击**自动生成**生成加密密钥。 |
      | **回调URL** | 开发者服务器接收推送信息的地址，用于接收钉钉服务器推送的消息。  打开已下载的服务端示例代码，在`eapp-isv-quick-start-java/src/main/java/com/controller/IndexController.java`码中查看回调URL。  本示例输入`http://example.vaiwan.com/dingCallback`。`example.vaiwan.com`是内网穿透工具启动的URL，请根据实际情况进行替换。 |
   2. 打开已下载的代码示例的`eapp-isv-quick-start-java/src/main/java/com/config/Constant.java`文件，提供以下配置：

      ![constant配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8955600061/p166114.png)

      1. 提供应用凭证**SUITE\_KEY**和**SUITE\_SECRET**，应用凭证信息可在开发者后台的**凭证与基础信息**页面获取。

         ![p166109](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4401117161/p256319.png)
      2. 提供应用签名的**TOKEN**和数据加解密密钥**ENCODING\_AES\_KEY**。在开发者后台的**开发管理**页面获取。

         ![p166111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4401117161/p256401.png)
   3. 启动后端服务：

      1. 进入下载的服务端代码项目路径，执行以下命令完成编译。

         ```
         mvn clean compile -U
         ```
      2. 执行以下代码，生成jar文件。

         ```
         mvn clean package -Dmaven.test.skip=true
         ```
      3. 执行以下代码，启动后端服务。

         ```
         java -jar target/eapp-isv-quick-start-1.0.0.jar
         ```
   4. 后端服务启动成功后，回到开发者后台的**开发管理**配置页面。单击回调URL的**验证有效性**，检测回调配置，验证通过后单击**保存**。

      ![回调URL](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9955600061/p166128.png)
3. 在开发者后台，单击**版本管理与发布**，单击**设置体验组织**添加体验人员，并开通应用。

   > **[!NOTE]**
   >
   > - 添加体验组织是创建一个全新的测试类型的组织，而不是关联已有的组织变为体验组织。
   > - 最多可创建10个体验组织。 体验组织默认可获取通讯录信息，包括：部门列表、部门详情、部门成员、管理员列表等。

   ![开通应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9955600061/p166150.png)

   开发者服务器正常启动状态下，点击体验组织后面的**开通应用**按钮，回调地址会接收到推送的授权开通事件信息。具体信息在点击**开通应用**之后，返回服务器接收推送信息的地址中。

   > **[!IMPORTANT]**
   >
   > 点击**开通应用**之后，服务端返回的数据，请保存返回参数AuthCode的值，用于获取永久授权码。

   **推送数据数据解密后示例：**

   ```
    { 
      "TimeStamp":1553709079062,
      "AuthCode": "80dc451ddc173da686f7e1492axxxx", 
      "AuthCorpId":"ding2f5d5f95e46aa503ffe9347xxxx",
      "EventType":"tmp_auth_code",
      "SuiteKey":"suitefcurkdvkc1ncxxxx"
    }
   ```
4. 接收到授权开通事件后，需要依次调用以下三个接口完成应用激活，激活完成后才算授权成功：

   1. 调用[获取第三方企业应用的suite\_access\_token](https://open.dingtalk.com/document/isvapp/obtain-application-suite-ticket)接口获取第三方应用凭证（suite\_access\_token）。

      **请求方式：**POST(HTTPS)

      **请求地址：**`https://oapi.dingtalk.com/service/get_suite_token`

      **POST请求包结构****体:**

      ```
      {
          "suite_key":"xxx",
          "suite_secret": "xxx",
          "suite_ticket": "xxx"
      }
      ```

      | **参数** | **类型** | **必须** | **说明** |
      | --- | --- | --- | --- |
      | suite\_key | String | 是 | 三方企业应用suitekey，开发者后台创建应用后获取。 |
      | suite\_secret | String | 是 | 三方企业应用suiteSecret，开发者后台创建应用后获取。 |
      | suiteTicket | String | 是 | 钉钉开放平台会向应用的回调URL推送的suite\_ticket，详细内容请参考[推送suite\_ticket事件](https://open.dingtalk.com/document/orgapp/push-suite_ticket-events-1)。 |
   2. 调用[获取授权企业的永久授权码](https://open.dingtalk.com/document/isvapp/obtain-a-permanent-authorization-code)接口获取永久授权码。

      **请求方式：**POST(HTTPS)

      **请求地址：**`https://oapi.dingtalk.com/service/get_permanent_code?suite_access_token=SUITE_ACCESS_TOKEN`

      **POST请求包结构****体:**

      ```
      {"tmp_auth_code": "xxx"}
      ```

      | 参数 | 类型 | 必须 | 说明 |
      | --- | --- | --- | --- |
      | suite\_access\_token | String | 是 | 应用套件suite\_access\_token，调用  [获取第三方企业应用的suite\_access\_token](https://open.dingtalk.com/document/isvapp/obtain-application-suite-ticket)接口返回。 |
      | tmp\_auth\_code | String | 是 | 临时授权码，来自授权开通事件中的AuthCode。  **[!IMPORTANT]**  临时授权码只能使用一次。 |
   3. 调用[激活应用](https://open.dingtalk.com/document/isvapp/activate-suite)接口激活企业授权的应用。

      **请求方式：**POST(HTTPS)

      **请求地址：**`https://oapi.dingtalk.com/service/activate_suite?suite_access_token=SUITE_ACCESS_TOKEN`

      **POST请求包结构****体:**

      ```
      {
        "suite_key":"xxxxxx",
        "auth_corpid":"xxxxxx",
        "permanent_code":"xxxxxx"
      }
      ```

      | 参数 | 类型 | 必须 | 说明 |
      | --- | --- | --- | --- |
      | suite\_access\_token | String | 是 | 应用套件suite\_access\_token。 |
      | suite\_key | String | 是 | 三方企业应用suitekey，开发者后台创建应用后获取。 |
      | auth\_corpid | String | 是 | 授权企业corpid。 |
      | permanent\_code | String | 是 | 企业的永久授权码。 |
5. 在开发者后台，单击**安全中心**，然后单击**添加**输入和钉钉小程序用于通讯的域名。

   本示例中输入内网穿透工具中配置的域名。

   ![p179116 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4401117161/p256216.png)

## 步骤三：发布小程序

为方便开发者快速体验钉钉小程序的开发流程，我们提供了小程序的服务端和前端代码示例。

1. 执行以下命令，下载前端小程序项目文件。

   ```
   git clone https://github.com/opendingtalk/eapp-isv-project-fe.git
   ```
2. 在小程序IDE中打开已下载的小程序项目，项目类型选择钉钉**第三方企业应用**。

   ![p142938](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8824718061/p201825.png)
3. 使用钉钉账号登录IDE，选择已设置的体验组织，然后打开`index.js`文件修后端服务URL。本示例输入内网穿透工具中设置的域名。
4. 单击**测试发消息**，如果能收到如下图的消息通知则代表成功。

   ![p143074](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8824718061/p201826.png)
5. 在小程序IDE中单击**上传**，上传开发版本。

   ![上传开发版本 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5475299951/p143419.png)
6. 登录[开发者后台](https://open-dev.dingtalk.com/#/appMgr/provider/eapp/54716/6)，选择**应用开发 > 第三方企业应用 > 小程序**。单击已创建的小程序，然后单击**版本管理与发布**，再单击**设为体验版**。

   体验组织内的成员就可以在钉钉工作台中体验小程序了。

   > **[!NOTE]**
   >
   > 只有先设置为体验版，才可以进行小程序发布。

   ![p180068 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4401117161/p256315.png)
