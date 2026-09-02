---
title: "接入成员资料页"
source_url: "https://open.dingtalk.com/document/dingstart/access-member-profile-coolapp"
namespace: "dingstart"
slug: "access-member-profile-coolapp"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发成员资料页酷应用 > 接入成员资料页"
doc_id: "MfD3uL8Mph"
updated_at: "2026-07-21 14:49:33"
---

> Source: https://open.dingtalk.com/document/dingstart/access-member-profile-coolapp
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发成员资料页酷应用 > 接入成员资料页
> Updated: 2026-07-21 14:49:33

# 接入成员资料页

如果你需要接入成员资料页，你可以依据本文档操作步骤进行接入。

## 适用对象

本文档适用于以下类型的应用：

- 企业内部应用（由企业自主开发并用于内部管理）
- 第三方企业应用（为多个企业提供服务的ISV应用）

## **使用场景**

- 展示员工OKR目标进度、绩效数据、项目参与情况等动态信息。
- 在单聊或群聊中快速查看对方相关业务系统数据（如CRM客户状态、HR入职进度）。
- 实现跨系统信息聚合，减少切换成本，提高沟通协作效率。

## **前提条件**

在开始操作前，请确认满足以下要求：

- 企业已完成认证。
- 已完成[创建酷应用](https://open.dingtalk.com/document/dingstart/create-coolapp)流程。
- 在开发者后台已开启“成员资料页扩展”相关能力。
- 应用类型为企业内部应用或已上架的第三方企业应用。

## **操作步骤**

1. 选择**扩展到成员资料页**。
2. 在**基础信息**页面，配置**成员资料页**基础信息。

   | **配置项** | **必填** | **说明** |
   | --- | --- | --- |
   | 图标 | 是 | 酷应用图标，尺寸：240\*240px，格式：PNG。默认使用主应用图标。 |
   | 名称 | 是 | 酷应用名称信息。 |
   | 描述 | 是 | 简要描述酷应用功能。 |
3. 单击**功能设计**，配置互动互动卡片模板,可以使用默认卡片模板快速体验。

   > **[!NOTE]**
   >
   > 新建模板卡片，参见更多信息**创建通讯录卡片**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3756164871/p516971.png)

   | **配置项** | **说明** |
   | --- | --- |
   | 卡片模板 | - 填写说明：可以选择**酷应用通讯录卡片示例**。 **[!NOTE]**  若选择新建模板卡片，请参考[创建通讯录卡片](0071-create-contact-card.md)。 |
   | 卡片数据回调服务 | - 服务说明：卡片数据回调服务用于在成员资料页扩展时请求开发者获取到需卡片模板和卡片数据，获取到的数据将用于卡片的渲染。 - 填写说明：请输入获取卡片数据的业务回调服务地址，用于获取卡片的数据。 - 填写示例：`https://dingtalk.com/profile/card/callback`。 |

   确认配置无误后，单击右上角**保存**按钮。
4. 开发卡片数据回调，更多信息参考**功能开发** > **获取脚手架与示例**：

   1. 钉钉回调业务方数据结构（入参）：

      ```
      {
          "content": "{\"dynamicDataSourceQueryRequests\":[{\"dynamicDataSourceId\":\"ds.profile\",\"dynamicParams\":{\"profile\":\"{\\\"corpId\\\":\\\"ding82cdb244a6246deca13*****1351\\\",\\\"userId\\\":\\\"015353405866731012128\\\"}\"}}]}",
          "corpId": "ding82cdb244a6246deca13*****1351",
          "outTrackId": "COOLAPP-10-101F10E26908213F1****.V47",
          "type": "dynamicDataCallback",
          "userId": "13330623764729"
      }
      ```

      | 名称 | 类型 | 是否必填 | 描述 |
      | --- | --- | --- | --- |
      | userId | String | 是 | 查看人在某企业下userId信息。 |
      | corpId | String | 是 | 所属企业ID，从不同的入口进入成员资料页，企业ID不同。  - 内部群&外部群查看成员资料页：返回该内部群&外部群所属的企业ID。  image - 单聊&普通群查看成员资料页：返回被查看人的**主企业ID**。  image **[!NOTE]**  个人主企业可以从何以下路径查看 **移动端 > 左上角个人头像 > 点击个人头像 >企业/团队。** |
      | outTrackId | String | 是 | 卡片实例唯一标识。 |
      | type | String | 是 | 回调类型，目前是固定值`dynamicDataCallback`。 |
      | content | String | 是 | 回调业务拓展信息。  **[!NOTE]**  包含被查看人的企业ID和在企业I下的用户ID。 |
   2. 业务方响应钉钉侧数据结构（出参）：

      ```
      {
          "dataSourceQueryResponses": [
              {
                  "data": "{\"profileUrl\":\"www.dingtalk.com\",\"profilePcUrl\":\"www.dingtalk.com\",\"isProfileOwner\":false,\"okrs\":[{\"name\":\"这是小钉新的目标，(进度会刷新)\",\"progress\":40}]}",
                  "dynamicDataSourceId": "ds.profile",
                  "dynamicDataValueType": "OBJECT"
              }
          ]
      }
      ```

      | 名称 | 类型 | 描述 |
      | --- | --- | --- |
      | data | Object | 渲染卡片的私有数据对象，适合于设置每个人看到的不一样的卡片内容。 |
      | dynamicDataSourceId | String | 数据源类型，目前钉钉平台要求必须返回固定值 `ds.profile`。 |
      | dynamicDataValueType | String | 数据源data返回数据格式，目前钉钉平台要求必须返回固定值 `OBJECT`。 |

      签名验证：

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
               throw new RuntimeException("sign api secret failed", e);
          }
      }
      ```

      > **[!NOTE]**
      >
      > 卡片数据响应，请参考[成员资料页扩展互动卡片能力](0072-member-information-page-expands-interactive-card-capability-beta.md)。
5. 单击**预览发布** > **发布，**显示可见性设置。
6. 单击**去设置**，完成可见性设置。

   > **[!NOTE]**
   >
   > 登录钉钉管理后台，需要**企业子管理员权限。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3756164871/p517107.png)

   通讯录成员资料页可见性配置规则需要设置：展示范围和可见范围，支持按照部门、人、角色维度设置。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3756164871/p517131.png)

   > **[!NOTE]**
   >
   > 自己看自己需要勾选 **展示此信息的成员自己也可见**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3756164871/p516593.png)
7. 扫码查看成员资料页扩展，使用移动端扫码快速体验。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3756164871/p517220.png)

   扫码预览，展示信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3221872871/p517300.png)

## **后续步骤**

消息菜单酷应用完成发布后，需要完成[发布应用](0019-publish-dingtalk-application.md)。
