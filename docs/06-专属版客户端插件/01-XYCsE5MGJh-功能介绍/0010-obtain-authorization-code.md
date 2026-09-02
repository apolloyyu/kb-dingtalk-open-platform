---
title: "获取插件免登授权码"
source_url: "https://open.dingtalk.com/document/development/obtain-authorization-code"
namespace: "development"
slug: "obtain-authorization-code"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取插件免登授权码"
doc_id: "9mIhCz1uuC"
updated_at: "2026-08-12 09:20:52"
---

> Source: https://open.dingtalk.com/document/development/obtain-authorization-code
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取插件免登授权码
> Updated: 2026-08-12 09:20:52

# 获取插件免登授权码

## **基础信息**

当专属插件有获取免登授权码做安全身份校验时，可通过借用 H5 微应用身份获取。参考JSAPI [requestAuthCode](../../01-应用开发/03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md)。

| API名称 | 调用方式 | 说明 |
| --- | --- | --- |
| dd. getAuthCode | 异步 | 获取免登授权码，授权码同微应用的 requestAuthCode，授权码使用方式可参考：[requestAuthCode](../../01-应用开发/03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md) |

> **[!NOTE]**
>
> - 本方案仅使用与钉钉登录成功后使用，对于登录前或者登录过程中的场景无法使用。
> - 插件的 BundleID 请不要包含特殊字符，包含特殊字符可能会出现不适配问题。

## **参数说明**

**入参**

| 入参 | 类型 | 说明 |
| --- | --- | --- |
| corpid | String | 可选，如果未指定，默认使用用户所在的专属组织对应的 CorpId。 |
| clientId | String | 必填，开放平台创建的应用的 ClientID，具体获取方式请参考后续描述。 |

**返回结果**

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | String | 授权码。 |

## **示例代码**

Android-Java

```
ApiRequest req = new ApiRequest();
req.api = "dd.getAuthCode";
req.params.put("clientId", "xxxxx")
req.params.put("corpid", "yyyyyy")
MainBundle.getBundleContext().invokeApi(req, new ApiCallback<ApiResponse>() {
  @Override
  public void onSuccess(ApiResponse response) {
    String authCode = response.getString("code");
  }

  @Override
  public void onException(String s, String s1) {
  
  }
});
```

arkts

```
const param = new Map<string, APIDataType>()
param.set("clientId", clientId)
param.set("corpid", corpId)
myBundle.invokeApi({api: "dd.getAuthCode", params: param})
  .then((data) => { 
    myBundle.toast(`authCode: ${data.getString('code')}`)
  })
  .catch((e: Error) => {
    myBundle.toast(`用例失败：${e.message}`)
  })
```

## **配置插件**

为了能够使得客户端专属插件获取到免登授权码，需要在钉钉开放平台创建对应的微应用，并配置权限。

> **[!NOTE]**
>
> 企业管理员（具有钉钉 OA 管理后台操作权限的人员）需要提前配置开放平台应用，专属插件才能正确获取到登录授权码。如果接口获取异常时，请先联系企业管理员确认是否正常按照下面的操作完成配置。

1. 请先登录钉钉开放平台，并登录到应用关联的企业组织下，并进入“我的后台” - “应用开发” 。链接：[钉钉开放平台后台](https://open-dev.dingtalk.com/fe/app#/corp/app)
2. 创建应用

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1916230671/p1010163.png)

   单击“创建应用”，并填写应用信息。参考示例：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1916230671/p1010164.png)
3. 在创建好的应用详情界面，选择“应用能力” - “添加应用能力” - “网页应用”，单击后进入网页应用的配置页面，同时右侧 tab 区也会增加一项“网页应用”。添加后配置应用首页地址，然后点击保存。格式如下：

   https://exclusiveplugin.<专属插件的 bundleId>.com

   > **[!IMPORTANT]**
   >
   > 如果 bundleID 包含特殊字符，比如下划线，请将所有特殊字符（包括下划线）替换成中划线“-”。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1916230671/p1010165.png)
4. 在应用详情界面，单击 “开发配置” - “权限管理”，进一步配置插件可访问的数据权限。

   > **[!NOTE]**
   >
   > 假如专属插件期望获取用户的手机号等信息，需要管理员赋予相关权限。
   >
   > **注意：请谨慎赋予专属插件更多权限，避免企业隐私信息泄露，务必遵循“非必要不开通”的原则**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1916230671/p1010167.png)
5. 在应用详情界面，单击 “应用发布” - “版本管理与发布” - “创建新版本”，执行应用发布。

   > **[!NOTE]**
   >
   > 只有发布后应用才能正式生效。注意：由于应用是一个非真实存在的网页应用，因此请务必不要发布到全员，范围选择“仅我可见”即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1916230671/p1010169.png)
6. 在应用详情界面，单击 “基础信息” - “凭证与基础信息”，然后拷贝应用的凭证（ClientID）并填写到请求接口中。

## **常见问题**

当请求返回异常时，常见的几个问题：

（1）请确认开放平台配置的插件是否发布，如果未发布，请参考上面的文档发布一个空版本，另外也请确认 ClientID 是否填写正确。

（2）填写的域名不正确，由于域名中不能包含特殊字符，假如你的 bundleId 中包含特殊字符，请务必记得将特殊字符替换成中划线"-"。

（3）登录的账号不在配置的企业中，因此导致没有权限访问对应 ClientID 的权限。
