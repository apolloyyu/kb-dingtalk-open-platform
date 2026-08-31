---
title: "获取并补全员工的民族信息"
source_url: "https://open.dingtalk.com/document/development/realize-automatic-push-of-employee-birthday-wishes-information"
namespace: "development"
slug: "realize-automatic-push-of-employee-birthday-wishes-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 使用教程 > 获取并补全员工的民族信息"
doc_id: "jLES1yAEEK"
updated_at: "2026-07-14 09:22:29"
---

> Source: https://open.dingtalk.com/document/development/realize-automatic-push-of-employee-birthday-wishes-information
> Path: 应用开发 / 服务端 API / 智能人事 > 使用教程 > 获取并补全员工的民族信息
> Updated: 2026-07-14 09:22:29

# 获取并补全员工的民族信息

本文档介绍了如何调用智能人事相关接口实现获取员工的民族信息，如果民族信息为空，通过接口实现更新。首先创建一个企业内部应用，再使用智能人事提供的API，实现获取员工民族信息、更新员工民族、获取员工花名册元数据字段信息期流程。

## 流程简介

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请智能人事相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)，通过accessToken鉴权调用者身份。

步骤四：调用服务端智能人事和工作通知相关API：

1. 调用服务端API-[获取员工花名册字段信息](0939-api-getemployeerosterbyfield.md)接口，获取员工的民族。
2. 如果获取员工民族的字段为空，说明该员工的民族字段没有填写，调用服务端API-[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口，获取员工花名册字段元数据值。
3. 调用服务端API-[更新员工花名册信息](0940-intelligent-personnel-update-employee-file-information.md)接口，更新员工的民族信息。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`qyapi_hrm_read_user`和`qyapi_hrm_manager`，并申请权限。

## **步骤三：**获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)，以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。

```
public void getAccessToken() throws ApiException {
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
  OapiGettokenRequest req = new OapiGettokenRequest();
  req.setAppkey("dingxxxxxxxxxhgn");
  req.setAppsecret("9G_xxxxxxxxxxxxxxx1JDf0Qq3nexxxxxxxxGIO");
  req.setHttpMethod("GET");
  OapiGettokenResponse rsp = client.execute(req);
  System.out.println(rsp.getBody());
}
```

## 步骤四：调用服务端智能人事和工作通知相关API

1. 调用服务端API-[获取员工花名册字段信息](0939-api-getemployeerosterbyfield.md)接口，获取员工的年龄。

   例如，获取员工张三的年龄信息如下

   ```
   {"field_code":"sys02-nationType","field_name":"民族","field_value_list":[{"item_index":0,"label":"阿昌族","value":"40"}],"group_id":"sys02"}
   ```

   解析label值，可以拿到员工的民族信息。
2. 如果未获取到民族字段信息，调用服务端API-[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口，获取的民族字段元数据信息如下

   ```
   {
     "field_code":"sys02-nationType",
       "field_name":"民族",
       "field_type":"DDSelectField",
       "option_text":"[{\"label\":\"汉族\",\"value\":\"1\"},{\"label\":\"阿昌族\",\"value\":\"40\"},{\"label\":\"白族\",\"value\":\"15\"},{\"label\":\"保安族\",\"value\":\"49\"},{\"label\":\"布朗族\",\"value\":\"36\"},{\"label\":\"布依族\",\"value\":\"11\"},{\"label\":\"朝鲜族\",\"value\":\"14\"},{\"label\":\"穿青人\",\"value\":\"57\"},{\"label\":\"傣族\",\"value\":\"19\"},{\"label\":\"达斡尔族\",\"value\":\"33\"},{\"label\":\"德昂族\",\"value\":\"45\"},{\"label\":\"侗族\",\"value\":\"12\"},{\"label\":\"东乡族\",\"value\":\"24\"},{\"label\":\"独龙族\",\"value\":\"52\"},{\"label\":\"鄂伦春族\",\"value\":\"51\"},{\"label\":\"俄罗斯族\",\"value\":\"47\"},{\"label\":\"鄂温克族\",\"value\":\"42\"},{\"label\":\"高山族\",\"value\":\"56\"},{\"label\":\"亻革家人\",\"value\":\"58\"},{\"label\":\"仡佬族\",\"value\":\"22\"},{\"label\":\"哈尼族\",\"value\":\"16\"},{\"label\":\"哈萨克族\",\"value\":\"18\"},{\"label\":\"赫哲族\",\"value\":\"54\"},{\"label\":\"回族\",\"value\":\"4\"},{\"label\":\"景颇族\",\"value\":\"34\"},{\"label\":\"京族\",\"value\":\"43\"},{\"label\":\"基诺族\",\"value\":\"44\"},{\"label\":\"柯尔克孜族\",\"value\":\"32\"},{\"label\":\"拉祜族\",\"value\":\"23\"},{\"label\":\"黎族\",\"value\":\"17\"},{\"label\":\"傈僳族\",\"value\":\"21\"},{\"label\":\"珞巴族\",\"value\":\"55\"},{\"label\":\"满族\",\"value\":\"3\"},{\"label\":\"毛南族\",\"value\":\"37\"},{\"label\":\"蒙古族\",\"value\":\"9\"},{\"label\":\"门巴族\",\"value\":\"50\"},{\"label\":\"苗族\",\"value\":\"5\"},{\"label\":\"仫佬族\",\"value\":\"31\"},{\"label\":\"纳西族\",\"value\":\"27\"},{\"label\":\"怒族\",\"value\":\"41\"},{\"label\":\"普米族\",\"value\":\"39\"},{\"label\":\"羌族\",\"value\":\"28\"},{\"label\":\"撒拉族\",\"value\":\"35\"},{\"label\":\"畲族\",\"value\":\"20\"},{\"label\":\"水族\",\"value\":\"26\"},{\"label\":\"塔吉克族\",\"value\":\"38\"},{\"label\":\"塔塔尔族\",\"value\":\"53\"},{\"label\":\"土家族\",\"value\":\"8\"},{\"label\":\"土族\",\"value\":\"29\"},{\"label\":\"佤族\",\"value\":\"25\"},{\"label\":\"维吾尔族\",\"value\":\"6\"},{\"label\":\"乌孜别克族\",\"value\":\"46\"},{\"label\":\"锡伯族\",\"value\":\"30\"},{\"label\":\"瑶族\",\"value\":\"13\"},{\"label\":\"彝族\",\"value\":\"7\"},{\"label\":\"裕固族\",\"value\":\"48\"},{\"label\":\"藏族\",\"value\":\"10\"},{\"label\":\"壮族\",\"value\":\"2\"}]"
   }
   ```
3. 根据民族字段元数据信息的value值，调用服务端API-[更新员工花名册信息](0940-intelligent-personnel-update-employee-file-information.md)接口，更新员工的民族信息。

   > **[!NOTE]**
   >
   > [更新员工花名册信息](0940-intelligent-personnel-update-employee-file-information.md)接口，指定value值，员工的民族组队值会更新为对应的label值，例如更新张三的民族信息时，指定value值为1，张三的民族信息会显示为对应的汉族。
