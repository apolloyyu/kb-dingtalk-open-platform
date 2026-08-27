---
title: "根据sns临时授权码获取用户信息"
source_url: "https://open.dingtalk.com/document/development/obtain-the-user-information-based-on-the-sns-temporary-authorization"
namespace: "development"
slug: "obtain-the-user-information-based-on-the-sns-temporary-authorization"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 身份验证（免登） > 根据sns临时授权码获取用户信息"
doc_id: "VJWxtc35fw"
updated_at: "2026-08-25 09:36:36"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-user-information-based-on-the-sns-temporary-authorization
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 身份验证（免登） > 根据sns临时授权码获取用户信息
> Updated: 2026-08-25 09:36:36

# 根据sns临时授权码获取用户信息

调用本接口根据sns临时授权码获取用户信息。

> **[!NOTE]**
>
> 该接口获取的用户信息仅用于扫码登录第三方网站、钉钉内免登第三方网站和使用钉钉账号登录第三方网站的场景。

推荐使用SDK方式调用本接口：

- 在使用HTTP调用时，必须设置**signature**参数，钉钉会对请求进行签名验证，以保证安全。签名计算方式可参考[个人免登场景的签名计算方法](1428-signature-personal-registration.md)。
- **在使用SDK调用本接口时，无需自行进行签名计算，钉钉SDK已自带签名功能。**建议使用钉钉提供的SDK进行调用，SDK下载地址参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 是 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/sns/getuserinfo_bycode`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| accessKey | String | 是 | 3a2ca6aa3231b7xxxx | 应用的AppKey，在[钉钉开发者后台](https://open-dev.dingtalk.com/#/corpAuthInfo)应用详情页查看。 |
| timestamp | String | 是 | 1546084445901 | 当前时间戳，单位毫秒。  **[!NOTE]**  使用SDK调用时，这个值不需要填写，SDK内部已做处理。 |
| signature | String | 是 | ddsdssfsdfxxxx | 通过appSecret计算出来的签名值，计算方式请参考[个人免登场景的签名计算方法](1428-signature-personal-registration.md)。  **[!NOTE]**  使用SDK调用时，这个值不需要填写，SDK内部已做处理。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| tmp\_auth\_code | String | 否 | 4a2c5695b78738d495f47bxxxxxx | 用户授权的临时授权码，只能使用一次。获取方法请参考：[实现网页方式登录应用（登录第三方网站）](0019-tutorial-obtaining-user-personal-information.md) |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| user\_info | UserInfo |  | 用户信息。 |
| nick | String | 名字 | 用户在钉钉上面的昵称。 |
| unionid | String | dingdkjjojoixxxx | 用户在当前开放应用所属企业的唯一标识。 |
| openid | String | dingsdsqwlklklxxxx | 用户在当前开放应用内的唯一标识。 |
| main\_org\_auth\_high\_level | Boolean | true | 用户主企业是否达到高级认证级别。 |
| errmsg | String | ok | 返回描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/sns/getuserinfo_bycode?accessKey=ACCESS_KEY&timestamp=TIMESTAMP&signature=SIGNATURE
```

请求正文

```
{
        "tmp_auth_code":"4a2c5695b78738d495f47bxxxxxx"
}
```

**请求示例（JAVA SDK）**

```
 DefaultDingTalkClient  client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/getuserinfo_bycode");
 OapiSnsGetuserinfoBycodeRequest req = new OapiSnsGetuserinfoBycodeRequest();
 req.setTmpAuthCode("4a2c5695b78738d495f47bxxxxxx");
 OapiSnsGetuserinfoBycodeResponse response = client.execute(req,"yourAppId","yourAppSecret");
```

**请求示例（PHP SDK）**

```
include "TopSdk.php";
$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiSnsGetuserinfoBycodeRequest;
$req->setTmpAuthCode("4a2c5695b78738d495f47bxxxxxx");
$resp=$c->executeWithAccessKey($req, "https://oapi.dingtalk.com/sns/getuserinfo_bycode","yourAppId","yourAppSecret");
var_dump($resp)
```

**返回示例**

```
{
        "errcode":0,
        "user_info":{
                "nick":"名字",
                "unionid":"dingdkjjojoixxxx",
                "openid":"dingsdsqwlklklxxxx",
                "main_org_auth_high_level":true
        },
        "errmsg":"ok"
}
```
