---
title: "接入链接增强"
source_url: "https://open.dingtalk.com/document/dingstart/access-link-enhancements-coolapp"
namespace: "dingstart"
slug: "access-link-enhancements-coolapp"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发链接增强酷应用 > 接入链接增强"
doc_id: "0X83fPopqa"
updated_at: "2026-08-07 14:52:48"
---

> Source: https://open.dingtalk.com/document/dingstart/access-link-enhancements-coolapp
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发链接增强酷应用 > 接入链接增强
> Updated: 2026-08-07 14:52:48

# 接入链接增强

本功能适用于已创建酷应用的企业内部应用或第三方企业应用的开发者。通过链接增强，可将普通链接消息升级为互动卡片，提升用户在群聊和单聊中的协作体验。

## 适用对象与权限说明

- **适用应用类型**：企业内部应用、第三方企业应用（需已开通酷应用能力）。
- **网络要求**：回调服务必须部署在公网可访问地址，支持 HTTPS 协议（推荐）。

## 链接增强调用流程

当用户在钉钉中发送一条链接消息时，系统将按以下流程处理：

1. 钉钉识别该链接，并查找开发者预先配置的链接增强规则。
2. 根据规则中的域名与路径匹配策略，确定是否触发链接增强。
3. 钉钉侧调用开发者注册的回调接口，开发者自行解析url后调用钉钉接口创建卡片实例，并返回卡片outTrackId。
4. 钉钉侧将卡片信息返回给客户端。
5. 客户端展示卡片数据。

## **前提条件**

- 已完成[创建酷应用](0007-create-application.md)流程。
- 应用类型为企业内部应用或第三方企业应用。

## **操作步骤**

1. 选择**链接增强**。
2. 在**酷应用列表** > **链接增强**，填写链接增强配置信息。

   | **配置项** | **说明** |
   | --- | --- |
   | 域名 | - **填写说明：**需要识别增强链接的域名。 - **填写示例：**`www.dingtalk.com`。 |
   | Path | - **填写说明：**请输入域名后面的完整路径（请勿携带参数）。 - **填写示例：**如链接是：https://www.dingtalk.com/test?id=123，则Path填写：`/test`，目前支持**完全匹配**和**正则匹配**两种。 |
   | 选择卡片 | - **填写说明**：请输入链接转换后展示使用的卡片模板id。可以在[互动卡片高级版](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0001-platform-building-overview.md#8ea07cac63f7j)定义。 - **填写示例**：如`07d54d61-xxxx-xxxx-a3a0-a6071ba8a60a`。 |
   | 卡片数据回调服务 | - **服务说明**：卡片数据回调服务用于在链接增强时请求开发者获取到需转换的链接对应的卡片模板和卡片数据，获取到的数据将用于卡片的渲染。 - **填写说明**：请输入获取卡片数据的业务回调服务地址，用于在链接转换时获取卡片的数据，HTTP接口必须支持POST请求方式，填写时请勿携带任何参数，请填写公网可访问的地址。 - **填写示例**: `https://dingtalk.com/unfurling/callback`。 |
   | 卡片数据回调Secret | - **填写说明**：请输入16位固定长度的自定义的字符长串，用于钉钉调用卡片数据业务回调的请求签名验证。 - **填写示例**：`asfghhesfsfghxxh`。 |
3. 单击保存，完成链接增强配置信息。
4. 开发链接增强回调HTTP接口：

   开发者需自主实现回调http接口服务。在链接增强成卡片时，钉钉会调用开发者注册的回调服务获取卡片outTrackId。

   1. 钉钉回调业务方数据结构（入参）：

      ```
      {
        "extension": "{\"url\":\"https://www.dingtalk.com/unf****ing/test?id=1\",\"openConversationId\":\"cidb9121bafe1=\",\"singleChatAnotherUserId\":\"12312tr14fas\"}",
        "corpId": "corp1",
        "userId": "user1"
      }
      ```

      | 名称 | 类型 | 是否必填 | 描述 |
      | --- | --- | --- | --- |
      | extension | String | 是 | 回调业务拓展信息，携带原始url字段。 |
      | >url | String | 是 | 发送人发送的原始链接。 |
      | >openConversationId | String | 是 | 发送人发送的会话openConversationId。 |
      | >singleChatAnotherUserId | String | 否 | - 如果会话是单聊，表示单聊对方在企业内的员工userId； - 如果会话是群聊，此字段为空。 |
      | corpId | String | 是 | 发送人或群所在的企业CorpId。 |
      | userId | String | 是 | 发送人在企业内的员工userId。 |
   2. 业务方解析url等参数，并自行调用[创建卡片](../02-4a8AMF6u2A-服务端-API/0780-interface-for-creating-a-card-instance.md)接口创建卡片实例（注意卡片创建者的userId在此场景需要必填，否则发送者自己可能看不到卡片）。
   3. 业务方响应钉钉侧数据结构（出参）：

      ```
      {
        "outTrackId": "业务自定义的卡片的唯一标识，也可以根据此id更新卡片数据",
        "cardOptions": {
          "supportForward": true, //是否支持转发，true表示卡片支持转发
          "lastMessage": "这里是卡片在会话列表中展示的文案"
        }
      }
      ```

      | 名称 | 类型 | 是否必填 | 描述 |
      | --- | --- | --- | --- |
      | outTrackId | String | 是 | 对应的是卡片唯一标识，开发者需确保唯一性。 |
      | cardOptions | Object | 否 | 卡片配置。 |
      | >supportForward | Boolean | 否 | 卡片是否支持转发：  - **true**：支持，默认值 - **false**：不支持 |
      | >lastMessage | String | 否 | 卡片发出后，在会话列表展示的内容，默认为url。 |

      **签名验证**：

      为了提升回调接口的安全性，从钉钉侧发起的HTTP回调请求，支持开发者进行来源校验。

      如配置链接增强时提供了“卡片数据回调Secret”，则收到的HTTP请求Header中包含签名相关Header:

      • x-ddpaas-signature-timestamp：签名时间戳

      • x-ddpaas-signature：签名串

      其中 <签名串> = calcSignature(apiSecret, <签名时间戳>)，apiSecret是配置时指定的“卡片数据回调Secret”

      接口提供方应使用如下方法计算签名并验证签名串是否正确以防未授权的调用：

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
5. 开发完成后，调试应用：

   1. 在**链接增强**页面，单击**添加测试人员**，选择**修改**，添加链接增强的测试人员。
   2. 添加测试人员后，对应的测试人员在企业内部群中可发送符合条件的测试链接，查看效果。
6. 调试完成后，单击**发布**。

## **后续步骤**

链接增强酷应用完成发布后，需要完成[发布应用](0019-publish-dingtalk-application.md)。

## **常见问题**

1. 链接增强发布后的生效范围有哪些？

   答：发布后会在企业内部群、以及双方共同组织包含开发者所在企业的单聊中生效
2. 如何实现千人千面，同一个卡片针对不同的人返回不同的数据?

   答：可以接入卡片的[动态数据源](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0008-dynamic-data-source.md)能力。
3. 回调接口的超时时间是多少？

   答：回调接口的超时时间为3秒。
