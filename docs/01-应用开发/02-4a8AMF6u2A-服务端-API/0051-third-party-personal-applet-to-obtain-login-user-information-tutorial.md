---
title: "第三方个人小程序获取登录用户信息"
source_url: "https://open.dingtalk.com/document/development/third-party-personal-applet-to-obtain-login-user-information-tutorial"
namespace: "development"
slug: "third-party-personal-applet-to-obtain-login-user-information-tutorial"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 使用教程 > 第三方个人小程序获取登录用户信息"
doc_id: "uYxi6nrUyo"
updated_at: "2026-07-02 10:35:51"
---

> Source: https://open.dingtalk.com/document/development/third-party-personal-applet-to-obtain-login-user-information-tutorial
> Path: 应用开发 / 服务端 API / 通讯录管理 > 使用教程 > 第三方个人小程序获取登录用户信息
> Updated: 2026-07-02 10:35:51

# 第三方个人小程序获取登录用户信息

本文档介绍第三方个人小程序获取登录用户信息的流程。

## **接入流程简介**

本文档展示了，创建一个第三方个人应用，使用通讯录提供的API，实现获取当前登录用户个人信息操作流程：

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击**应用开发 > 第三方个人应用**后，**创建应用**。

步骤二：单击**基础信息 > 应用信息**，获取应用AppKey和AppSecret。

步骤三：[添加接口调用权限](0003-add-api-permission.md)。确定需申请的权限，申请对应的权限。

步骤四：使用授权套件获取authCode。

步骤五：获取个人用户身份访问凭证[获取用户token](0032-obtain-user-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤六：调用服务端API-[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口。

## **步骤一：创建应用**

> **[!NOTE]**
>
> 如果已有第三方个人应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发 > 第三方个人应用**后，点击**创建应用**。

   ![iShot2022-08-23 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6394521661/p480243.png)
3. 填写创建第三方个人应用信息。

   - **应用类型**：默认只有小程序。
   - **应用名称**：填写应用名称。
   - **应用描述**：填写应用描述。
   - **应用图标**：上传应用图标，也可以使用钉钉默认图标。![iShot2022-08-23 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7394521661/p480252.png)

## **步骤二：获取AppId和AppSecret**

获取第三方个人应用的AppId和AppSecret信息。![iShot2022-08-23 20](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9547521661/p480322.png)

## **步骤三：添加接口或字段权限**

1. **确认需要申请哪些权限**

   应用需要获取哪些信息，申请的权限不同。请参考权[个人权限scope列表](0007-function-description.md#50679ce2b8jpj)确认需要开通哪些权限。

   > **[!NOTE]**
   >
   > 如果需要获取用户个人手机号，则需要申请开通[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口权限和字段权限。
2. **申请接口或字段权限**

   - 登录[开发者后台](https://open-dev.dingtalk.com/#/)，选择进入对应的应用。
   - 在应用的**权限管理**页面，输入对应权限关键字进行搜索，然后选择对应的权限单击**申请权限**。

     例如，需要获取用户个人手机号信息，搜索**个人信息**，选择**个人权限**，并单击**申请权限**。添加**通讯录个人信息读权限**和**个人手机号信息**权限。![iShot2022-08-23 20](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9547521661/p480310.png)

## **步骤四：使用授权套件获取authCode**

钉钉统一授权套件SDK要求，钉钉版本需要在**6.0.10及以上**。低版本需提示用户升级客户端，你可以通过以下方式判断钉钉版本。

```
import { getENV, } from 'dingtalk-jsapi/lib/env';
import { compareVersion, } from 'dingtalk-jsapi/lib/sdk/sdkLib';

const { platform, version, appType, } = getENV();
/**
 * 判断当前app版本是否支持使用SDK
 * @return {boolean}
 */
function isAuthSDKSupport() {
  return compareVersion(version, '6.0.5');
}
```

1. 安装授权套件SDK。

   执行以下命令，下载安装SDK。

   ```
   npm install dingtalk-design-libs --save
   ```
2. 在`app.onShow`方法添加**onAuthAppBack**调用。

   ```
   onShow(options) {
       onAuthAppBack(options, (data) => {
           // 这里可以对返回数据做二次处理，之后需要把数据返回到page.onShow
           dd.alert({
               title: 'app is onAppShow have data ：' + JSON.stringify(data),
           });
           return data;
       });
   },
   ```
3. 在小程序需要授权的页面，使用授权SDK。

   例如`page/index/index.js`，通过**openAuthMiniApp**唤起授权套件。

   ```
   import { openAuthMiniApp, disposeAuthData} from 'dingtalk-design-libs/biz/openAuthMiniApp';
   ```

   ```
   onTap() {
       return openAuthMiniApp({
           path: 'pages/home/home',  //不要改,这里是小程序dingwlanwvdmrtjjwdmd下的一个页面地址
           panelHeight: 'percent50',
           extraData:{
               clientId:'dingwlanwxxx', // 应用ID，即第一步中第三方个人应用的AppId。
               rpcScope:'Contact.User.Read',
               fieldScope:'Contact.User.mobile',
               type:0,
               ext: JSON.stringify({}),
               from:''
           }
       });
   },
   ```
4. 使用**page.onShow**方法调用**disposeAuthData**处理授权后的结果。

   ```
   onShow(e) {
       disposeAuthData((options)=>{
           dd.alert({
               title:'disposeAuthData',
               content:JSON.stringify(options) //这里获取authCode。
           })
       })
   },
   ```
5. 调用效果。

   ![iShot2022-08-23 20](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9547521661/p480311.png)

   单击允许后，**page.onShow**方法内调用的**disposeAuthData**方法内可获取authCode值**。**

## **步骤五：获取个人用户身份访问凭证**

参考[获取用户token](0032-obtain-user-token.md)接口文档。

```
public void getToken() throws Exception {
        com.aliyun.dingtalkoauth2_1_0.Client client = AuthTest.createClient1();
        GetUserTokenRequest getUserTokenRequest = new GetUserTokenRequest()
                .setClientId("dingzxxxx")  //第一步获取的三方个人小程序的AppId。
                .setClientSecret("XyJONrxxxxx") //第一步获取的三方个人小程序的AppSecret。
                .setCode("18ec1db4xxxxx") //第三步获取的authCode。
                .setGrantType("authorization_code");
        try {
            GetUserTokenResponse userToken = client.getUserToken(getUserTokenRequest);
            System.out.println(JSON.toJSONString(userToken));
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
                System.out.println(JSON.toJSONString(err));
            }
        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
                System.out.println(JSON.toJSONString(err));
            }
        }
    }
```

## **步骤六：**调用服务端相关API

调用服务端API-[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口。

> **[!NOTE]**
>
> unionId参数固定传`me`。

```
public void getUserInfo() throws Exception {
        com.aliyun.dingtalkcontact_1_0.Client client = AuthTest.createClient();
        GetUserHeaders getUserHeaders = new GetUserHeaders();
        getUserHeaders.xAcsDingtalkAccessToken = "17e756xxxxx"; //第四步获取的个人用户身份访问凭证。
        try {
            GetUserResponse me = client.getUserWithOptions("me", getUserHeaders, new RuntimeOptions());
            System.out.println(JSON.toJSON(me));
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
                System.out.println(JSON.toJSONString(err));
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
                System.out.println(JSON.toJSONString(err));

            }

        }

    }
```
