---
title: "API 调用步骤详解"
source_url: "https://open.dingtalk.com/document/development/server-api-calling-guide"
namespace: "development"
slug: "server-api-calling-guide"
group: "应用开发"
tab: "服务端API"
breadcrumb: "API 调用指南 > API 调用步骤详解"
doc_id: "wSZghZdSMI"
updated_at: "2026-07-02 10:34:59"
---

> Source: https://open.dingtalk.com/document/development/server-api-calling-guide
> Path: 应用开发 / 服务端API / API 调用指南 > API 调用步骤详解
> Updated: 2026-07-02 10:34:59

# API 调用步骤详解

本指南旨在指导开发者从零开始，通过调用钉钉开放平台接口，完成从注册应用到接口调通的全流程操作。文档涵盖关键步骤、代码示例、注意事项及调试方法，确保开发者快速上手并成功调用API。

> **[!NOTE]**
>
> 本示例是以企业内部应用为基础，通过调用接口获取通讯录中用户的详细信息为例，若是其他应用类型的应用，也可参考此文档。

## **前置工作**

1. **基础概念**：已了解钉钉开放平台的基础概念及各产品块文档说明，详见[基础概念](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)文档说明。
2. **接口频率限制：**已了解API的调用频率限制，详见[调用频次与限流](1433-how-to-process-api-throttling-on-the-dingtalk-server.md)文档说明。
3. **开发者权限**：具有[开发者后台](https://open-dev.dingtalk.com/?spm=dd_developers.header.unLogin.openDevBtn&hash=%23%2F#/)子管理员和开发者权限，也可以登录钉钉开发者完成新用户的注册与激活。
4. **获取用户**`UserId`：登录[钉钉管理后台](http://oa.dingtalk.com/)并在**通讯录 > 成员管理**下查看`UserId`，详见[基础概念](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)说明。

## **步骤一：创建钉钉应用**

1. 访问[开发者后台](https://open-dev.dingtalk.com/?spm=dd_developers.header.unLogin.openDevBtn&hash=%23%2F#/)，单击**应用开发** > **钉钉应用** > **创建应用**。

   > **[!NOTE]**
   >
   > 本示例已企业内部应用为例，第三方企业应用和第三方个人应用创建路径一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7516308771/p1071962.png)
2. 填写应用信息，并单击**保存**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5967308771/p1071963.png)

   | **配置项** | **是否必选** | **配置说明** |
   | --- | --- | --- |
   | **应用名称** | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | **应用描述** | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
3. 进入应用详情页，在**基础信息** > **凭证与基础信息**，查看应用凭证与基础信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7516308771/p1071964.png)
4. 保存应用的**Client ID**和**Client Secret**，用于后续接口调用使用。

   > **[!NOTE]**
   >
   > **Client ID**和**Client Secret**获取可参考[基础概念](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)中说明，获取后请妥善保管，避免泄露。

## **步骤二：配置权限**

1. **查找所需权限**：根据接口文档，调用用户详情需`成员信息读权限`权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9969592871/p1084442.png)
2. **添加权限**：访问[开发者后台](https://open-dev.dingtalk.com/?spm=dd_developers.header.unLogin.openDevBtn&hash=%23%2F#/)，找到已经创建的应用并进入应用详情，在**权限管理**中搜索`成员信息读权限`，点击**立即申请**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7516308771/p1071951.png)

## **步骤三：获取Access Token**

> **[!IMPORTANT]**
>
> 在获取**Access Token**前，需要确定接口需要申请的是[普通权限](0003-add-api-permission.md)还是[敏感权限](0004-use-sensitive-permissions.md)，两种方式的获取方式不一样。

### **普通权限API**

#### **调用接口获取Token**

1. 访问[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口，通过右侧的**API调试**按钮打开[服务端调试工具](../06-JDICnQyZLF-开发工具/0005-api-explorer.md)。
2. 在调试工具中，替换`appkey（参数值替换为提前获取的Client ID）`和`appSecret（参数值替换为提前获取的Client Secret）`的值，并点击**发起调试**按钮。

   > **[!IMPORTANT]**
   >
   > 需要在登录状态下才能使用服务端调试台，且必须要绑定对应的应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9969592871/p1071954.png)

   也可直接复制下方代码，使用 cURL 命令，替换`appkey（参数值替换为提前获取的Client ID）`和`appSecret（参数值替换为提前获取的Client Secret）`的值后，直接发起调用，示例如下：

   ```
   curl -X POST 'https://api.dingtalk.com/v1.0/oauth2/accessToken' \
     -H 'Content-Type: application/json' \
     -d '{
       "appKey": "替换为提前获取的Client ID",
       "appSecret": "替换为提前获取的Client Secret"
     }'
   ```

#### **解析响应**

接口调用成功后，会生成accessToken值，如下：

```
{
  "accessToken" : "fw8ef8we8f76e6f7s8dxxxx", # 核心凭证
  "expireIn" : 7200 # 有效期（2小时）
}
```

#### **缓存与刷新**

- 建议将`access_token`缓存至数据库或内存，并设置定时刷新（过期前10分钟）。
- 避免频繁调用获取Token接口，否则可能触发限流。

### **敏感权限API**

第三方应用为了实现跨组织的数据互通与功能调用，必须经过严格的权限授权流程，需通过组织授权和个人授权两种机制获取目标企业的使用许可和用户数据访问权限。

#### **申请接口权限**

通过[应用使用敏感权限](0004-use-sensitive-permissions.md)文档内容，申请接口调用权限。

#### **接入授权套件**

申请敏感权限后，需要接入[授权套件](0007-function-description.md)，用户在授权弹窗中同意授权时，返回`authCode`，然后调用[获取用户token](0032-obtain-user-token.md)接口，换取用户级`access_token`。

## **步骤四：调用用户详情API**

### **普通权限API**

获取用户详情需要通过调用[查询用户详情](0056-query-user-details.md)接口，获取方式可直接使用钉钉SDK或通过HTTP方式直接获取，可根据实际需求进行选择。

#### **方式一：使用钉钉SDK（推荐）**

> **[!NOTE]**
>
> 若使用钉钉SDK进行调用，需要提前了解服务端 API 的差异，然后下载对应版本的SDK，详见[服务端SDK下载](0002-download-the-server-side-sdk.md)文档介绍。

1. 安装SDK（以Python为例）

   ```
   pip install dingtalk-sdk
   ```
2. 调用示例

   ```
   # -*- coding: utf-8 -*-
   import dingtalk.api

   req=dingtalk.api.OapiV2UserGetRequest("https://oapi.dingtalk.com/topapi/v2/user/get")

   req.userid="zhangsan"  # 替换为实际用户ID
   req.language="zh_CN"
   try:
   	resp= req.getResponse(access_token)
   	print(resp)
   except Exception,e:
   	print(e)
   ```

#### **方式二：直接发起HTTP请求**

```
curl -i 'https://oapi.dingtalk.com/topapi/v2/user/get' \
  -X 'POST' \
  -H 'Content-Type: application/json' \
  -d '{"userid":"替换为实际用户ID","language":"zh_CN"}'
```

#### **成功响应**

若接口返回值中`"errcode":"0"`且`"errmsg":"ok"`，则代表接口调用成功。

```
{
        "errcode":"0",
        "result":{
                "extension":"{\"爱好\":\"旅游\",\"年龄\":\"24\"}",
                "unionid":"z21HjQliSzpw0YWxxxxx",
                "boss":"true",
                "role_list":{
                        "group_name":"职务",
                        "name":"总监",
                        "id":"100"
                },
                "exclusive_account":false,
                "manager_userid":"manager240",
                "admin":"true",
                "remark":"备注备注",
                "title":"技术总监",
                "hired_date":"1597573616828",
                "userid":"zhangsan",
                "work_place":"未来park",
                "dept_order_list":{
                        "dept_id":"2",
                        "order":"1"
                },
                "real_authed":"true",
                "dept_id_list":"[2,3,4]",
                "job_number":"4",
                "email":"test@xxx.com",
                "leader_in_dept":{
                        "leader":"true",
                        "dept_id":"2"
                },
                "mobile":"18513027676",
                "active":"true",
                "org_email":"test@xxx.com",
                "telephone":"010-86123456-2345",
                "avatar":"xxx",
                "hide_mobile":"false",
                "senior":"true",
                "name":"张三",
                "union_emp_ext":{
                        "union_emp_map_list":{
                                "userid":"5000",
                                "corp_id":"dingxxx"
                        },
                        "userid":"500",
                        "corp_id":"dingxxx"
                },
                "state_code":"86"
        },
        "errmsg":"ok"
}
```

#### **错误处理**

- **权限不足**：检查`成员信息读权限`权限是否已申请。
- **用户不存在**：确认`userid`是否有效且无拼写错误。
- **Token过期**：刷新`access_token`后重试，并确认`access_token`有效且无拼写错误。

### **敏感权限API**

通过`authCode`换取用户级`access_token`后，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)获取用户的昵称、unionId 等信息。

若接口返回200，则代表接口执行成功，返回结果如下：

```
{
  "nick" : "zhangsan",
  "avatarUrl" : "https://xxx",
  "mobile" : "150xxxx9144",
  "openId" : "123",
  "unionId" : "z21HjQliSzpw0Yxxxx",
  "email" : "zhangsan@alibaba-inc.com",
  "stateCode" : "86"
}
```

## **支持与帮助**

如果你在开发过程中遇到了任何问题，可通过扫描下方二维码加入“钉钉开发者社区（互助群）”寻求帮助：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7516308771/p1071955.png)
