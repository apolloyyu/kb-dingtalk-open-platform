---
title: "第三方企业应用事件与回调流程"
source_url: "https://open.dingtalk.com/document/development/third-party-enterprise-application-address-book-change-event-subscription-process"
namespace: "development"
slug: "third-party-enterprise-application-address-book-change-event-subscription-process"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 第三方企业应用事件与回调流程"
doc_id: "Z2iab40aya"
updated_at: "2025-10-16 15:06:24"
---

> Source: https://open.dingtalk.com/document/development/third-party-enterprise-application-address-book-change-event-subscription-process
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 第三方企业应用事件与回调流程
> Updated: 2025-10-16 15:06:24

# 第三方企业应用事件与回调流程

本文可以帮助你了解第三方企业应用事件与回调的流程，通过本文你将了解如何配置第三方企业应用的事件以及如何接收第三方企业应用的事件回调内容。

## 教程介绍

本教程以事件订阅中企业内部用户变更事件为例展示第三方企业应用事件与回调的流程，通过本教程您将学习到：

- 配置第三方企业应用事件订阅。
- 接收第三方企业应用的事件回调内容。

## 接入流程

步骤一：创建第三方企业应用。

步骤二：设置开发管理。

步骤三：配置事件与回调。

步骤四：设置体验组织授权开通（可选）。

步骤五：测试事件订阅与回调（可选）。

## 准备工作

在开始本文前，确保你已经完成了以下准备工作：

- 入驻成为产品方案商，详情请参考文档[入驻成为产品方案商](https://open.dingtalk.com/document/isvapp/become-an-application-service-provider)。
- 需要成为钉钉开发者，详情请参考[成为钉钉开发者](https://open.dingtalk.com/document/isvapp/become-a-dingtalk-developer)。

## 步骤一：创建第三方企业应用

在本部分，你需要在开发者后台创建一个第三方企业应用-H5微应用。

> **[!NOTE]**
>
> 如果已有第三方企业应用，可跳过此步骤。

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/index)。
2. 在**开发者后台**页面，选择**第三方企业应用**，然后单击**创建应用**。![第三方企业应用事件与回调创建](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p439989.png)
3. 在弹出的创建应用页面中填写基本信息，单击确定创建。

   - 应用类型：选择H5微应用。![填写基本信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p379419.png)
4. 应用创建完成后，在**基础信息**-**应用信息**页面，可以查看应用的**SuiteKey**和**SuiteSecret**。![第三方企业应用事件与回调](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p439986.png)

## 步骤二：设置开发管理

1. 单击**基础信息 > 开发管理**进入开发管理页面，单击**修改**，并根据以下内容配置开发信息。

   - **服务器出口IP：**输入调用钉钉服务端API时使用的IP即企业服务器的公网IP，多个IP请以英文逗号","隔开，支持带一个\*号通配符的IP格式。
   - **应用首页地址：**请输入http或https开头的网址链接，如`https://open.dingtalk.com/document/`。
2. 添加完成后，单击**保存**。

![第三方企业应用事件与回调开发管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p439992.png)

## 步骤三：配置事件与回调

单击**应用功能 > 事件与回调**进入事件回调页面。

1. 选择对应的推送方式，本文选择SyncHttp推送。![第三方企业应用事件与回调推送方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p439997.png)
2. 设置对应信息。

   - 生成加密Aes\_key，回调消息内容的加解密参数，是AES密钥的Base64编码。
   - 生成签名Token，钉钉每次向你的地址推送事件数据时都会携带`token`，用于生成签名、校验回调请求的合法性。必须为英文或数字，长度为3~32个字符。
   - 设置回调请求地址，用于接收事件订阅请求的URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求。![第三方企业应用事件与回调设置回调参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440017.png)
3. 校验回调有效性。

   > **[!NOTE]**
   >
   > 接收事件回调的 URL，必须是公网可以访问的url地址，需保证URL地址所在服务可以正常访问。
   >
   > 测试阶段，可使用frp内网穿透测试工具，详情请参考[frp内网穿透工具](https://open.dingtalk.com/document/resourcedownload/alibaba-cloud-frp-intranet-penetration-tool)。

   ![第三方企业应用事件与回调验证有效性](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440008.png)**校验有效性流程：**

   1. 引入pom依赖文件。

      ```
          <parent>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-parent</artifactId>
              <version>2.1.4.RELEASE</version>
          </parent>
          <properties>
              <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
              <maven.compiler.source>8</maven.compiler.source>
              <maven.compiler.target>8</maven.compiler.target>
          </properties>
          <dependencies>
              <dependency>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-starter</artifactId>
              </dependency>

              <dependency>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-devtools</artifactId>
                  <optional>true</optional>
              </dependency>

              <dependency>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-starter-web</artifactId>
              </dependency>

              <dependency>
                  <groupId>javax.servlet</groupId>
                  <artifactId>javax.servlet-api</artifactId>
                  <scope>provided</scope>
              </dependency>

              <dependency>
                  <groupId>com.alibaba</groupId>
                  <artifactId>fastjson</artifactId>
                  <version>1.2.72</version>
              </dependency>

              <dependency>
                  <groupId>commons-io</groupId>
                  <artifactId>commons-io</artifactId>
                  <version>2.4</version>
              </dependency>
           </dependencies>
      ```
   2. 引入消息加解密类，详情请参考[dingtalk-callback-Crypto](https://github.com/open-dingtalk/dingtalk-callback-Crypto)。
   3. 接收并响应回调事件。

      ```
      @RestController
      @RequestMapping("/")
      public class CallbackController {

          private final Logger log = LoggerFactory.getLogger(getClass());

      //*
      //     * 创建应用，验证回调URL创建有效事件（第一次保存回调URL之前）

          private static final String EVENT_CHECK_CREATE_SUITE_URL = "check_create_suite_url";

      //*
      //     * 创建应用，验证回调URL变更有效事件（第一次保存回调URL之后）

          private static final String EVENT_CHECK_UPADTE_SUITE_URL = "check_update_suite_url";

      //*
      //     * suite_ticket推送事件

          private static final String SYNC_HTTP_PUSH_HIGH = "SYNC_HTTP_PUSH_HIGH";

      //*
      //     * 企业授权开通应用事件

          private static final String EVENT_TMP_AUTH_CODE = "tmp_auth_code";

          @PostMapping(value = "dingCallback")
          public Object dingCallback(
                  @RequestParam(value = "signature") String signature,
                  @RequestParam(value = "timestamp") Long timestamp,
                  @RequestParam(value = "nonce") String nonce,
                  @RequestBody(required = false) JSONObject body
          ) {
              String params = "signature:" + signature + " timestamp:" + timestamp + " nonce:" + nonce + " body:" + body;
              try {
                  log.info("begin callback:" + params);
                  //参数分别填写Token、Aes_key和第三方企业应用的suiteKey
                  DingCallbackCrypto dingTalkEncryptor = new DingCallbackCrypto("fOAKxh71yYPEzCF3Uydxfb3eupK4Bdo**********", "W2tf5v5NWgPwcZCMz1f3faSUk9B6u*********", "suitew9h1bvc3t2rmqaym");
                  // 从post请求的body中获取回调信息的加密数据进行解密处理
                  String encrypt = body.getString("encrypt");
                  String plainText = dingTalkEncryptor.getDecryptMsg(signature, timestamp.toString(), nonce, encrypt);
                  JSONObject callBackContent = JSON.parseObject(plainText);
                  // 根据回调事件类型做不同的业务处理
                  //建议开发者在回调接口中只对接收到的事件进行落库处理，不进行业务逻辑处理，保证接口不会超时
                  String eventType = callBackContent.getString("EventType");
                  if (EVENT_CHECK_CREATE_SUITE_URL.equals(eventType)) {
                      log.info("验证新创建的回调URL有效性: " + plainText);
                      System.out.println("验证新创建的回调URL有效性：" + callBackContent);
                  } else if (EVENT_CHECK_UPADTE_SUITE_URL.equals(eventType)) {
                      log.info("验证更新回调URL有效性: " + plainText);
                      System.out.println("验证更新回调URL有效性：" + callBackContent);
                  } else if (SYNC_HTTP_PUSH_HIGH.equals(eventType)) {
                      // suite_ticket用于用签名形式生成accessToken(访问钉钉服务端的凭证)，需要保存到应用的db。
                      // 钉钉会定期向本callback url推送suite_ticket新值用以提升安全性。
                      // 应用在获取到新的时值时，保存db成功后，返回给钉钉success加密串（如本demo的return）
                      log.info("应用suite_ticket数据推送: " + plainText);
                  } else if (EVENT_TMP_AUTH_CODE.equals(eventType)) {
                      // 本事件应用应该异步进行授权开通企业的初始化，目的是尽最大努力快速返回给钉钉服务端。用以提升企业管理员开通应用体验
                      // 即使本接口没有收到数据或者收到事件后处理初始化失败都可以后续再用户试用应用时从前端获取到corpId并拉取授权企业信息，进而初始化开通及企业。
                      log.info("企业授权开通应用事件: " + plainText);
                  } else {
                      System.out.println("其他事件:" + callBackContent);
                  }
                  // 返回success的加密信息表示回调处理成功
                  System.out.println(dingTalkEncryptor.getEncryptedMap("success", timestamp, nonce));
                  return dingTalkEncryptor.getEncryptedMap("success", timestamp, nonce);
              } catch (Exception e) {
                  //失败的情况，应用的开发者应该通过告警感知，并干预修复
                  log.error("process callback fail." + params, e);
                  return "fail";
              }
          }
      }
      ```
4. 点击**保存**，查看回调URL所在服务，保存推送的suiteTicket参数，调用服务端接口时需要使用。

   > **[!NOTE]**
   >
   > 以下数据为解密biz\_type=2的suiteTicket最新状态，5个小时重新推送一次，详情请参看[数据格式](https://open.dingtalk.com/document/isvapp/data-formats)。

   ```
   {
     "EventType": "SYNC_HTTP_PUSH_HIGH",
     "bizData": [
       {
         "gmt_create": 1652841516000,
         "biz_type": 2,
         "open_cursor": 0,
         "subscribe_id": "253***1_0",
         "id": 230**,
         "gmt_modified": 1652841516000,
         "biz_id": "253****1",
         "biz_data": "{\"syncAction\":\"suite_ticket\",\"suiteTicket\":\"3Je*************ZtZa4sdl9do4dWC********ykDelR5AdPZt02lhkOY3p7yLKkdN9nVktPIkmlIjn2A\",\"syncSeq\":\"1ABA5C5215CB8BDEE8CA8D33A9\"}",
         "corp_id": "ding9f50b1*********",
         "status": 0
       }
     ]
   }
   ```

## 步骤四：设置体验组织授权开通（可选）

单击**部署与发布 > 版本管理与发布**进入页面。

1. 授权体验组织，若无体验组织需创建体验组织。

   > **[!NOTE]**
   >
   > 点击授权时务必保证回调URL所在的服务开启，否则无法授权成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9195473661/p490962.png)
2. 授权成功后，查看已授权体验组织。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9195473661/p493574.png)

## 步骤五：测试事件订阅与回调（可选）

> **[!NOTE]**
>
> 测试事件订阅与回调时务必保证回调URL所在的服务开启。

1. 申请相应的事件订阅的接口权限。本文以**通讯录> 企业内部用户变更**事件为例。![第三方企业应用事件与回调测试事件订阅](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440034.png)
2. 开启事件订阅。![第三方企业应用事件与回调开启事件订阅](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440070.png)
3. 事件订阅成功后，展示相应事件订阅。![第三方企业应用事件与回调订阅成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440071.png)
4. 测试事件订阅。

   1. 登录体验组织[钉钉管理后台](https://oa.dingtalk.com/#/welcome)。
   2. 修改企业内员工信息。![第三方企业应用事件与回调测试体验组织通讯录](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440078.png)![第三方企业应用事件与回调修改员工信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440084.png)
   3. 修改完成后，查看对应员工信息。![第三方企业应用事件与回调修改成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2019733561/p440088.png)
   4. 查看对应的事件订阅回调信息。

      > **[!NOTE]**
      >
      > 以下数据为解密biz\_type=13的企业员工的最新状态，详情请参看[数据格式](https://open.dingtalk.com/document/isvapp/data-formats)。

      ```
      {
        "EventType": "SYNC_HTTP_PUSH_MEDIUM",
        "bizData": [
          {
            "gmt_create": 1652846332000,
            "biz_type": 13,
            "open_cursor": 0,
            "subscribe_id": "2530****_0",
            "id": 5872,
            "gmt_modified": 1652846332000,
            "biz_id": "085*********",
            "biz_data": "{\"errcode\":0,\"unionEmpExt\":{},\"exclusiveAccount\":false,\"unionid\":\"iiqo**********gpw0wiEiE\",\"syncAction\":\"user_modify_org\",\"roles\":[{\"id\":20768*****,\"name\":\"子管理员\",\"groupName\":\"默认\",\"type\":102},{\"id\":20768*****,\"name\":\"行政\",\"groupName\":\"职务\",\"type\":0}],\"userid\":\"085*********\",\"managerUserid\":\"manager****\",\"isLeaderInDepts\":\"{499175958:false,505937693:false}\",\"isBoss\":false,\"isSenior\":false,\"department\":[499175958,505937693],\"orderInDepts\":\"{499175958:176292748870660512,505937693:176290579128509512}\",\"errmsg\":\"ok\",\"active\":true,\"avatar\":\"https://static-legacy.dingtalk.com/media/lADOrB***********_750_560.jpg\",\"isAdmin\":true,\"tags\":{\"teacher\":[\"506****\"]},\"isHide\":false,\"jobnumber\":\"002\",\"name\":\"小钉\",\"position\":\"总监\",\"realAuthed\":false,\"syncSeq\":\"342A1036CFC0257DD540210FAB\"}",
            "corp_id": "ding077ede7c***************",
            "status": 0
          }
        ]
      }
      ```
