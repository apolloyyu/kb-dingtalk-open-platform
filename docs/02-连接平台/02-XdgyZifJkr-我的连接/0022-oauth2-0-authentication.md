---
title: "OAuth2.0鉴权"
source_url: "https://open.dingtalk.com/document/connection/oauth2-0-authentication"
namespace: "connection"
slug: "oauth2-0-authentication"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 鉴权设置 > OAuth2.0鉴权"
doc_id: "U3bq8boBW2"
updated_at: "2026-07-27 17:25:48"
---

> Source: https://open.dingtalk.com/document/connection/oauth2-0-authentication
> Path: 连接平台 / 我的连接 / 开发参考 > 鉴权设置 > OAuth2.0鉴权
> Updated: 2026-07-27 17:25:48

# OAuth2.0鉴权

OAuth2.0 是一种广泛使用的授权框架，允许用户通过第三方系统（如 Zoho CRM）进行身份验证，并获取访问受保护资源的权限。

## **基本介绍**

在钉钉连接平台中，OAuth2.0 鉴权适用于**第三方集成场景**，即当企业需要将外部 SaaS 系统与钉钉打通时，通过标准 OAuth2.0 流程完成用户授权和 token 获取。

该方式要求配置人员具备管理员权限或开发者权限，能够访问钉钉开放平台及目标第三方系统的开发者控制台。整个流程依赖于客户端凭证（Client ID/Secret）、回调地址、以及一系列 API 接口的正确配置。

核心流程如下：

- 用户触发授权请求；
- 跳转至第三方 OAuth 授权页面；
- 用户同意授权后，第三方系统重定向到指定回调地址并携带临时 code；
- 连接平台使用 code 向第三方 Token 接口请求 access\_token；
- 后续接口调用均携带该 token 完成身份认证。

> **说明**：本鉴权方式需确保网络可达性，且回调地址可被公网访问。同时，所有敏感信息（如 Client Secret）应妥善保管，避免泄露。

## 前置条件

为顺利完成 OAuth2.0 鉴权配置，请提前准备以下事项：

1. **在钉钉平台创建对应类型的应用**

   根据业务需求选择“企业内部应用”或“第三方企业应用”，并在【应用开发】>【基础信息 > 凭证与基础信息】中获取 AgentId 及 CorpSecret（如适用），并启用相关 API 权限。
2. **在第三方系统注册开发者账号并创建应用**

   以 Zoho CRM 为例，在 [ZOHO API Console](https://api-console.zoho.com.cn/add#web) 注册开发者账户，创建 Web 应用，获取 Client ID 和 Client Secret，并配置允许的重定向 URI（即连接平台生成的回调地址）。
3. **网络与回调地址要求**

   - 回调地址必须为 HTTPS 协议；
   - 第三方系统需支持 CORS 或服务端可正常接收来自连接平台的 HTTP 请求；
   - 若部署在内网环境，需通过反向代理暴露公网地址用于调试。
4. **了解事件订阅机制（可选）**

   如需监听用户登录、token 刷新等事件，建议参考钉钉开放平台文档《[什么是事件订阅](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0014-event-subscription-overview.md)》进行配置。

## **鉴权示例**

1. 在连接平台新建连接器时，选择鉴权方式为 **OAuth2.0 鉴权**。

   ![选择OAuth2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626171.png)
2. **设置鉴权字段（可选）**，若第三方系统根据区域、实例等维度提供不同的认证域名或参数，则可通过自定义鉴权字段实现动态配置。

   > **[!NOTE]**
   >
   > 此项为可选设置项。若无特殊需求，可跳过此步骤直接进入下一步。支持字段类型包括文本、密码和下拉选项。

   1. 添加一个下拉类型的鉴权字段 `country`，用于选择服务器所在地区。

      ![设置鉴权字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626201.png)
   2. 单击 **编辑** 按钮，配置选项值：

      - 中国：`https://accounts.zoho.com.cn`。
      - 欧洲：`https://accounts.zoho.eu`。

        ![地区鉴权设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626226.png)
   3. 查看预览效果后，单击 **下一步** 完成设置。

      ![预览并下一步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626269.png)
3. **设置 OAuth 授权参数**

   1. 查看连接平台自动生成的授权回调地址。

      ![查看回调地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626281.png)
   2. 将该回调地址复制到第三方应用中，例如粘贴至  [ZOHO API Console](https://api-console.zoho.com.cn/add#web)的“重定向 URI”配置项。

      ![复制到第三方应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626306.png)
   3. 在连接平台填写由 ZOHO API Console 生成的凭证信息：

      - **Client ID**：填入从控制台复制的 Client ID；
      - **Client Secret**：填入对应的 Client Secret。

        ![设置OAuth授权参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626336.png)
4. 设置 OAuth 接口参数，详情参见 [ZOHO 发出授权请求](https://www.zoho.com.cn/crm/help/developer/api/auth-request.html)接口文档。

   > **[!NOTE]**
   >
   > 在连接平台中，`$.Query`、`$.Body`、`$.Header` 是用于从响应数据中提取关键参数的标准表达式语法，遵循 JSONPath 类似规则，支持多层嵌套访问。
   >
   > - **$.Query：**获取授权重定向后链接上的参数。
   > - **$.Body：**获取 Token 接口返回的 Body 参数。
   > - **$.Header**：获取 Token 接口返回的 Header 参数。

   - **请求方式：**`GET`。
   - **请求路径：**`{country}/oauth/v2/auth`。

     > **[!NOTE]**
     >
     > `{country}`为上一步中设置的下拉字段变量，运行时会自动替换为实际选择的域名（如`https://accounts.zoho.com.cn`）。

     ![设置OAuth授权接口路径](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626354.png)
   - **URL路径参数：**可以设置为 {country} 获取鉴权字段中，选择的区域所使用域名进行访问，也可以不使用鉴权字段，直接设置授权接口为：`https://accounts.zoho.com.cn/oauth/v2/auth` 。

     ![设置OAuth授权参数位置路径](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626356.png)
   - **URL查询参数：**必填参数包括：

     - `client_id`：填写 Client ID；
     - `response_type`：固定为`code`；
     - `redirect_uri`：填写连接平台提供的回调地址；
     - `scope`：根据目标接口权限范围设置，例如`ZohoCRM.modules.ALL`；
     - `access_type`：可选`offline`以获取 refresh\_token。

     ![设置OAuth授权参数查询参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626361.png)
5. **设置 OAuth 获取 Token**，详情参见[ZOHO 生成令牌](https://www.zoho.com.cn/crm/help/developer/api/access-refresh.html)接口文档。

   - **请求方式：**`POST`。
   - **请求路径：**`{accounts-server}/oauth/v2/token`。

     > **[!NOTE]**
     >
     > 此处 `{accounts-server}` 实际来源于授权回调中的 `accounts-server`参数，可在回调 URL 中观察到。

     ![设置OAuth获取Token接口路径](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626773.png)
   - **URL路径参数**

     绑定 `accounts-server` 动态变量，运行时解析为实际域名。使用表达式：`$.Query.accounts-server` 表示从前一步授权回调的查询参数中提取该值。

     ![设置OAuth获取Token参数位置路径](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626776.png)
   - **URL查询参数**

     ![设置OAuth获取Token参数位置查询](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626786.png)

     关键参数如下：

     - `code`：使用 `$.Query.code` 提取授权回调返回的临时 code；
     - `grant_type`：固定为 `authorization_code`；
     - `client_id` 和 `client_secret`：分别填入已配置的凭证信息；
     - `redirect_uri`：必须与授权请求一致。

     根据 zoho 文档可知，URL查询参数中 `code` 为上一步访问授权接口后以 Query 参数携带返回的令牌，连接平台中获取上一步中 Query 参数 `code` 使用：`$.Query.code`。
6. **设置 OAuth 刷新 Token。**

   - **请求方式：**`POST`。
   - **请求路径：**`{accounts-server}/oauth/v2/token`。

     ![设置OAuth刷新Token接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626844.png)
   - **URL路径参数：**同样使用`$.Query.accounts-server`提取域名。

     ![路径参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626853.png)
   - **URL查询参数**

     ![设置OAuth刷新Token参数位置查询](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626837.png)

     - 关键参数如下：

       - `grant_type`：固定为`refresh_token`；
       - `refresh_token`：使用`$.Body.refresh_token`从上一次获取 Token 的响应体中提取；
       - `client_id`和`client_secret`：同上。
     > 成功刷新后，新 access\_token 将自动更新并用于后续请求。
7. **Token 失效判断，**为实现自动刷新机制，需配置失效判定条件。当使用过期 token 请求接口时，Zoho CRM 返回响应体中`code`字段值为`INVALID_TOKEN`。

   > 原文中的`INVALI_TOKEN`已修正为正确的`INVALID_TOKEN`。

   因此，在连接平台中设置如下判断逻辑：

   - 判断路径：`$.Body.code`
   - 判断值：`INVALID_TOKEN`

   一旦命中该条件，系统将自动触发刷新 Token 流程。

   ![token失效](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p626808.png)
8. **设置鉴权请求参数**

   通常情况下，第三方系统要求在 HTTP 请求头中携带`Authorization`字段传递 token。

   1. 在“设置鉴权请求参数”中选择添加请求头。

      ![请求头设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p627424.png)
   2. 设置 Header 名称为`Authorization`，值采用表达式构造：

      ```
      Bearer $.Body.access_token
      ```

      ![自定义设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p627421.png)

      其中 `$.Body.access_token` 自动提取上一步获取 Token 接口返回的 access\_token。
9. 完成设置后，单击**保存配置并调试**。

   ![保存并调试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p627429.png)
10. 完成上述配置后，需进行调试以验证鉴权流程是否成功。

    1. **设置鉴权验证接口和参数**：填写鉴权验证接口的请求方式和请求验证的接口。

       例如访问 [ZOHO CRM 模块 API](https://www.zoho.com.cn/crm/help/developer/api/modules-api.html) 验证鉴权是否配置成功。在 **OAuth 授权接口以及参数**中配置模块 API 的 `scope` 为 `ZohoCRM.settings.all` 。
    2. **设置鉴权验证参数**（可选）：选择请求方式，填写接口所需参数。

       ![设置验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p627433.png)
    3. 进行**鉴权调试**：选择账户/添加账户进行鉴权调试。单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

       ![调试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8434415871/p627444.png)

       - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

         ![成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678111861/p627448.png)
       - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确：

         ![错误](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678111861/p627472.png)

         - 请求地址 **url** 中接口地址和需要携带 **URL查询参数** 是否正确。
         - 请求方式 **method** 是否设置正确。
         - 请求头 **headers** 中自动生成的 **Authorization** 是否加密正确。
