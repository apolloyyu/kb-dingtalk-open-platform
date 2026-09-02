---
title: "基础概念"
source_url: "https://open.dingtalk.com/document/dingstart/basic-concepts-beta"
namespace: "dingstart"
slug: "basic-concepts-beta"
group: "应用开发"
tab: "开发指南"
breadcrumb: "平台简介 > 基础概念"
doc_id: "sCL2QMwMeu"
updated_at: "2026-07-22 16:55:12"
---

> Source: https://open.dingtalk.com/document/dingstart/basic-concepts-beta
> Path: 应用开发 / 开发指南 / 平台简介 > 基础概念
> Updated: 2026-07-22 16:55:12

# 基础概念

文档是钉钉开放平台的**开发基础概念**指南，主要面向初次接触钉钉开发的开发者，旨在帮助理解核心术语、身份标识及权限体系。

## **关键开发后台**

文档明确了三个主要的操作平台，开发者需根据角色区分使用：

### **开发者后台**

[钉钉开发者后台](https://open-dev.dingtalk.com/#/index)是管理应用开发的服务平台。开发者可以配置应用信息，查看应用运行情况等。

> **[!IMPORTANT]**
>
> 只有企业管理员和授予了**开发者权限**和**工作台管理**权限的子管理员可访问开发者后台。子管理员权限可以在[钉钉企业管理后台](https://oa.dingtalk.com/)配置。

### **企业管理后台**

[钉钉企业管理后台](https://oa.dingtalk.com/)是企业管理员用于管理组织架构、成员权限、工作台配置的核心平台。通过该后台，管理员可完成通讯录导入、审批流程设置、子管理员授权等操作。

### **合作伙伴平台**

[钉钉合作伙伴平台](https://partner.dingtalk.com/)是面向服务商的统一管理平台，提供技术对接、部署实施、服务等全链路服务。当前涵盖产品方案商、部署服务商和培训服务商三类角色。

## **核心身份标识（ID体系）**

在钉钉开发中，区分“谁”和“哪个应用”至关重要。文档中定义了以下关键ID：

### **CorpId**

代表钉钉中的一个企业组织的唯一标识。调用绝大多数企业级API时，必须配合此ID进行身份验证。

**查看路径**：登录[钉钉开发者后台](http://open-dev.dingtalk.com/)，在**首页**下查看企业的`CorpId`。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7014308771/p1071880.png)

### **UserId**

代表企业内的具体员工的唯一标识。用于发送消息、查询档案、审批等接口，不可更改。

**查看路径**：登录[钉钉管理后台](http://oa.dingtalk.com/)，在**通讯录 > 成员管理**页面，单击员工姓名可查看员工的`UserId`。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7014308771/p1071882.png)

### **UnionId**

用户跨应用统一标识，同一用户在同一个开放平台账号下的所有应用中拥有相同的UnionId，用于跨应用数据打通。

**查看路径**：通过用户的userId调用[查询用户详情](../02-4a8AMF6u2A-服务端-API/0056-query-user-details.md)接口获取`unionid`参数值。

### **Unified App ID**

钉钉为所有类型应用分配的全局唯一ID，旨在简化跨系统对接，逐步替代旧的AgentId/AppId体系。

**查看路径**：登录[钉钉开发者后台](http://open-dev.dingtalk.com/)，进入应用详情后，在**凭证与基础信息**中查看。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8009733371/p883502.png)

### **AgentId**

企业内部应用（如H5、小程序）的能力标识。主要用于工作台管理API（如设置首页）。

**查看路径**：

- 企业内部应用网页应用AgentId

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1997117961/p726226.png)
- 企业内部应用小程序AgentId

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1997117961/p726228.png)

### **MiniAppId**

钉钉小程序的唯一身份标识，用于发布、调试及权限配置。

**查看路径**：登录[钉钉开发者后台](http://open-dev.dingtalk.com/)，在**应用开发**页面，单击已创建的应用，然后单击**应用信息**查看MiniAppId。

- **企业内部应用/第三方企业应用**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1997117961/p726215.png)
- **第三方个人应用**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1997117961/p726219.png)

## **安全凭证与权限 (Auth体系)**

这部分是开发中最容易出错的地方，涉及API调用的鉴权和免登录逻辑。

### **Client ID/Client Secret**

- **定义**：应用的身份凭证对（类似用户名和密码）。
- **用途**：用于获取 `access_token`，企业内部应用和第三方应用均使用此机制。
- **注意**：`Client Secret` 属于私密密钥，必须妥善保管，不可泄露。
- **获取**：在[钉钉开发者后台](http://open-dev.dingtalk.com/)创建企业内部应用或第三方企业应用后，系统会自动生成一对 Client ID和 Client Secret。

  > **[!NOTE]**
  >
  > 如果企业内部应用授权给服务商开发，服务商需要根据**CustomKey**和**CustomSecret**获取授权。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1997117961/p726090.png)

### **access\_token**

- **定义**：调用 OpenAPI 的“门票”。
- **用途**：每次调用受保护接口时，必须携带此凭据以验证合法性。
- **注意**：有效期通常为 7200 秒（2小时），有效期内重复获取会自动续期。
- **获取：**

  - 企业内部应用，通过[获取企业内部应用的accessToken](../02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取access\_token。
  - 第三方企业应用，通过[获取第三方应用授权企业的accessToken](../02-4a8AMF6u2A-服务端-API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取access\_token。
- **差异：**

  - 企业内部应用的 `access_token` 具备该应用所申请的所有权限。
  - 第三方应用的 `access_token` 权限受限于企业授权范围。

### **authCode**

**定义**：用于用户身份认证的关键凭证。

**用途**：用于换取用户身份信息（如 `userid`）。

**注意**：有效期仅为 5 分钟，使用一次后即失效且不可重复使用。

**获取**：通过调用 [getAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0006-jsapi-get-auth-code.md)、[requestAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md)等接口获取，详细使用可参考[身份验证（免登）](../02-4a8AMF6u2A-服务端-API/0016-sso-overview.md)。

### jsapi\_ticket

**定义**：用于生成前端 JS API 的签名。

**用途**：H5微应用需要安全调用钉钉提供的各类 JSAPI 能力（如获取用户信息、发起聊天、调用原生组件等）。

**注意**：有效期设为 2 小时，过期或参数不一致，将导致"jsapi ticket 读取失败”或“签名校验失败”等错误。

**获取**：使用 `access_token` 调用[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口获取。

### **SSOSecret**

- **定义**：配合 `CorpId` 使用的密钥。
- **用途**：主要用于获取微应用后台免登所需的 `access_token`，实现管理员从钉钉后台单点登录到第三方管理系统，无需重复输入账号密码
- **场景**：常用于企业SaaS系统的后台集成，提升运维效率与安全性。
- **获取**：登录[**钉钉开发者后台**](https://open-dev.dingtalk.com/#/) **> 基本信息 > 开发信息（旧版）**，找到**企业自用账号信息** > **点击查看**SSOSecret。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7014308771/p507291.png)

## **快速上手**

以下伪代码展示如何使用 `userid` 和 `access_token` 发起一次最简单的 API 调用，验证环境配置是否正确：

```
GET https://oapi.dingtalk.com/topapi/v2/user/get?access_token=ACCESS_TOKEN&userid=USERID
```

**步骤说明**：

1. **获取凭证**：使用 `Client ID` 和 `Client Secret` 调用接口获取 `access_token`。
2. **准备参数**：在管理后台找到任意成员的 `userid`。
3. **替换参数**：构造上述请求，替换 `ACCESS_TOKEN` 和 `USERID`。
4. **发起测试**：若返回 `"errcode": 0, "errmsg": "ok"`，则表示配置成功，可继续后续开发。

> 提示：实际开发中请使用 HTTPS 并做好错误处理与重试机制。
