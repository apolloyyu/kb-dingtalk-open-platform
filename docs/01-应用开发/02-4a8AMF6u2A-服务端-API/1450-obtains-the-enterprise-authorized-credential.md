---
title: "获取定制应用的access_token"
source_url: "https://open.dingtalk.com/document/development/obtains-the-enterprise-authorized-credential"
namespace: "development"
slug: "obtains-the-enterprise-authorized-credential"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 获取定制应用的access_token"
doc_id: "zpla4g9gDQ"
updated_at: "2026-08-25 09:36:32"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-enterprise-authorized-credential
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 获取访问凭证 > 获取定制应用的access_token
> Updated: 2026-08-25 09:36:32

# 获取定制应用的access\_token

产品方案商可通过此接口获取授权企业的access\_token。调用服务端API获取应用资源时，需要通过access\_token来鉴权调用者身份进行授权。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版 [获取定制应用的accessToken](0038-obtain-the-access-token-of-the-third-party-application-authorization-enterprise.md)接口，已接入用户不受影响。

在使用access\_token时，请注意：

- access\_token的有效期为7200秒（2小时），有效期内重复获取会返回新的access\_token。
- 开发者需要缓存access\_token，用于后续接口的调用。因为每个应用的access\_token是彼此独立的，所以进行缓存时需要区分应用来进行存储。
- 不能频繁调用gettoken接口，否则会受到频率拦截。

推荐使用SDK调用本接口：

- HTTP调用方式必须设置**signature**参数，钉钉会对请求进行签名验证，以保证安全。签名计算方式，请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。
- SDK调用方式无需自行进行签名计算，钉钉SDK已自带签名功能。**推荐**使用钉钉提供的[服务端SDK](0002-download-the-server-side-sdk.md)进行调用。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是（委托产品方案商开发时使用） | 无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.service.get_corp_token) |
| 第三方企业应用 | 是 | 无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.service.get_corp_token) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/service/get_corp_token`

## 请求参数(SDK请求)

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| accessKey | String | 是 | suitep1f5lzyglm7fryun | 在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取：   - **定制应用**：输入定制应用的CustomKey。 - **第三方企业应用**：输入第三方企业应用的SuiteKey。 |
| accessSecret | String | 是 | \_FP5PpZF3irDKj3e | 在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取：   - **定制应用**：输入定制应用的CustomSecret。 - **第三方企业应用**：输入第三方企业应用的SuiteSecret。 |
| suiteTicket | String | 是 | test | 钉钉推送的suiteTicket。   - 定制应用可随意填写。 - 第三方企业应用使用钉钉开放平台向应用推送的suite\_ticket，请参考[数据格式biz\_type=2](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-dqx-ue5-0f8)。   **[!NOTE]**  suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。 |
| auth\_corpid | String | 是 | ding123456 | 授权企业的CorpId。   - 定制应用可以在[钉钉开发者后台定制应用页面](https://open-dev.dingtalk.com/#/list-custom)查看。 - 第三方企业应用使用钉钉开放平台向应用推送的授权企业的corpid，请参考[数据格式biz\_type=4](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-ca8-x7n-gdw)。 |

## 请求参数(HTTP请求)

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| accessKey | String | 是 | suitxxxxyun | 在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取：   - **定制应用**：输入定制应用的CustomKey。 - **第三方企业应用**：输入第三方企业应用的SuiteKey。 |
| timestamp | Number | 是 | 1527130370219 | 当前时间戳，单位是毫秒。 |
| suiteTicket | String | 是 | test | 钉钉推送的suiteTicket。   - 定制应用可随意填写。 - 第三方企业应用使用钉钉开放平台向应用推送的suite\_ticket，请参考[数据格式biz\_type=2](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-dqx-ue5-0f8)。   **[!NOTE]**  suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。 |
| signature | String | 是 |  | 签名，计算方式请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。 |
| auth\_corpid | String | 是 | ding123456 | 授权企业的CorpId。   - 定制应用可以在[钉钉开发者后台定制应用页面](https://open-dev.dingtalk.com/#/list-custom)查看。 - 授权开通第三方企业应用的授权企业corpid：    - **微应用**，在微应用首页地址后面拼接?corpId=$CORPID$，再在页面内js解析获取当前企业corpid（仅支持工作台进入应用时使用）。   - **小程序**：在小程序app.js的onLaunch方法内会自动获取当前企业corpId，只需要解析即可获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| expires\_in | Number | 7200 | 授权企业的access\_token超时时间，单位秒。 |
| access\_token | String | 1cc1bb3xxxx | 授权企业的access\_token。 |
| errmsg | String | ok | 返回码的描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（JAVA SDK）**

```
DefaultDingTalkClient client= new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_corp_token");
OapiServiceGetCorpTokenRequest req= new OapiServiceGetCorpTokenRequest();
req.setAuthCorpid("dingc365fcxxxx");
OapiServiceGetCorpTokenResponse execute= client.execute(req,"accessKey","accessSecret","suiteTicket");
```

**返回示例**

```
{
        "access_token":"1cc1bb3xxxx",
        "errcode":0,
        "errmsg":"ok",
        "expires_in":7200
}
```
