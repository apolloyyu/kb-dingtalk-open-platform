---
title: "接入流程"
source_url: "https://open.dingtalk.com/document/dingstart/mini-app-procedures-for-authorized-logon-to-ios-applications"
namespace: "dingstart"
slug: "mini-app-procedures-for-authorized-logon-to-ios-applications"
group: "应用开发"
tab: "开发指南"
breadcrumb: "接入移动客户端 > 接入钉钉登录 > 接入流程"
doc_id: "lnoBJHORqu"
updated_at: "2026-07-02 10:31:49"
---

> Source: https://open.dingtalk.com/document/dingstart/mini-app-procedures-for-authorized-logon-to-ios-applications
> Path: 应用开发 / 开发指南 / 接入移动客户端 > 接入钉钉登录 > 接入流程
> Updated: 2026-07-02 10:31:49

# 接入流程

## **登录SDK下载**

### **iOS**

| **基本信息** | **说明** |
| --- | --- |
| SDK名称 | 钉钉登录SDK（iOS） |
| 开发者 | 钉钉科技有限公司 |
| 功能介绍 | 帮助用户使用钉钉账号快速登录 |
| 包名 | com.laiwang.ADTOpenAuthSDK |
| MD5值 | e2877e6792257c085cd7561bea4d2ed0 |
| 最新版本 | 0.0.1.16 |
| 下载地址 | [点击下载](https://files.alicdn.com/tpsservice/b1441c40818f069c0d10a3bbd36fdcd0.zip?spm=ding_open_doc.document.0.0.518e4a97BXQxUc&file=b1441c40818f069c0d10a3bbd36fdcd0.zip) | Demo参考[ADTOpenAuthDemo .zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250103/jbjajn/ADTOpenAuthDemo+.zip) |
| 使用说明 | - 安装客户端版本 7.1.16 及以上。 - ADTOpenAuthSDK 部署系统版本为 iOS 12.0 及以上。 - 下载并使用本SDK，即表示您已阅读并同意《[钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md)》、《[钉钉开放平台开发者服务协议](../07-TjCzIgfQs3-平台服务/0002-open-platform-developer-service-agreement.md)》。 |
| 更新日期 | 2023-12-22 |
| 个人信息处理规则 | 规则：   - [iOS登录SDK合规指南](0107-mini-app-ios-login-sdk-developer-compliance-guide.md) - [钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md) |

### **Android**

| **基本信息** | **说明** |
| --- | --- |
| SDK名称 | 钉钉登录SDK（Android） |
| 开发者 | 钉钉科技有限公司 |
| 功能介绍 | 帮助用户使用钉钉账号快速登录 |
| 包名 | com.android.dingtalk.openauth |
| MD5值 | 0a854f08a461f8a8ebec8aff6f8ddc00 |
| 最新版本 | 1.5.0.10 |
| 下载地址 | [点击下载](https://repo1.maven.org/maven2/com/alibaba/android/ddopenauth/1.5.0.10/ddopenauth-1.5.0.10.aar) | Demo参考 [钉钉OAuthSDKDemo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250408/wlsvef/%E9%92%89%E9%92%89OAuthSDKDemo.zip) |
| 使用说明 | 下载并使用本SDK，即表示您已阅读并同意《[钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md)》、《[钉钉开放平台开发者服务协议](../07-TjCzIgfQs3-平台服务/0002-open-platform-developer-service-agreement.md)》。 |
| 更新日期 | 2023-10-08 |
| 个人信息处理规则 | 规则：   - [Android登录SDK合规指南](0108-mini-app-android-login-sdk-compliance-guide.md) - [钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md) |

### HarmonyOS

| **基本信息** | **说明** |
| --- | --- |
| SDK名称 | 钉钉登录SDK（HarmonyOS） |
| 开发者 | 钉钉科技有限公司 |
| 功能介绍 | 帮助用户使用钉钉账号快速登录 |
| 包名 | com.harmony.dingtalk.openauth |
| MD5值 | 979828b6caaf2618815d1ed23e6e5b8e |
| 最新版本 | 1.1.0 |
| 下载地址 | [点击下载](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251124/lkaoit/openauth.har) | Demo参考 [OpenAuthDemo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250911/kvhldz/OpenAuthDemo.zip) |
| 使用说明 | - 安装钉钉客户端 8.0.6 及以上的版本。 - 下载并使用本SDK，即表示您已阅读并同意《[钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md)》、《[钉钉开放平台开发者服务协议](../07-TjCzIgfQs3-平台服务/0002-open-platform-developer-service-agreement.md)》。 |
| 更新日期 | 2025-10-24 |
| 个人信息处理规则 | 规则：   - [鸿蒙登录SDK合规指南](0109-hongmeng-sdk-compliance.md) - [钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md) |

## **登录接入流程图**

![p481496](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7865216371/p899369.png)

## **iOS接入登录**

### **步骤一：****创建并配置钉钉应用**

- 进入[开放平台-开发者后台](https://open-dev.dingtalk.com/)，单击**应用开发**，选择需要接入登录的应用。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p740485.png)
- 在**凭证与基础信息**中，记录应用的 **Client ID** 。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p740486.png)
- 在**分享设置-接入登录**中，填写自定义重定向 URL 。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p740487.png)

  > **[!NOTE]**
  >
  > 1、在授权登录过程中，钉钉会校验授权接口的参数redirectUri，与此处配置的域名是否一致。
  >
  > 2、回调地址中不要带#号，否则会导致钉钉无法回调。比如下面链接不建议填写：
  >
  > https://www.dingtalk.com/auth/#/
  >
  > 建议填写成
  >
  > https://www.dingtalk.com/auth
- 在**分享设置-接入分享**中，如果启用iOS分享，则需要填写iOS BundleId, 务必和正式版保持一致

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p745935.png)

### **步骤二：搭建开发环境**

- 将已下载的文件解压，在对应 target 的 Build Phases 中点加号把 xcframework 导入到工程中

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2159592871/p748680.png)

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7129843071/p748702.png)
- 修改 info.plist：

  - CFBundleURLType 下新增项：

    - URL identifier 填 dingtalk 。
    - URL scheme 新增项，值为开放平台对应应用的 **Client ID**，用于鉴权后跳回业务方 app
  - （可选）LSApplicationQueriesSchemes 下添加白名单 dingtalk、dingtalk-openauth、dingtalk-openauth2 ，用于检测钉钉安装状态。

    > **[!NOTE]**
    >
    > iOS系统限制 LSApplicationQueriesSchemes 最多只能有50个，超出部分有可能不生效。尤其是 Xcode 13 打包，iOS 15.0 及以上，超出部分不生效。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p745939.png)
- 相关方法实现

  - 在 app 启动阶段，调用`registerApp:identifier:`方法注册业务方基本信息。

    > **[!NOTE]**
    >
    > 其中 appId 为开放平台对应应用的 **Client ID**，identifier 为保证独一无二，填写 app 的 **bundleId。**

    ```
    @interface AppDelegate () <ADTOpenAuthAPIDelegate>

    @end

    @implementation AppDelegate

    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      
        [ADTOpenAuthAPI registerApp:kOpenAppId
                         identifier:kOpenBundleId];
      
        //...
        
        return YES;
    }
    ```

    如果使用SceneDelegate，使用下面回调方法

    ```
    @interface SceneDelegate () <ADTOpenAuthAPIDelegate>
    @end

    @implementation SceneDelegate

    - (void)scene:(UIScene *)scene willConnectToSession:(UISceneSession *)session options:(UISceneConnectionOptions *)connectionOptions {
        // 创建窗口和根视图控制器
        if ([scene isKindOfClass:[UIWindowScene class]]) {
            [ADTOpenAuthAPI registerApp:kOpenAppIdV2
                             identifier:kOpenBundleIdV2];
            //...
        }
    }
    ```
  - 在 openURL 入口调用 AuthAPI 的`handleOpenURL:delegate:`方法处理授权结果，并将 AppDelegate 设为代理。

    ```
    - (BOOL)application:(UIApplication *)app 
                openURL:(NSURL *)url
                options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
        
        if ([ADTOpenAuthAPI handleOpenURL:url
                                 delegate:self]) {
            return YES;
        }
        
        return NO;
    }
    ```

    如果使用SceneDelegate，使用下面回调方法

    ```
    - (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
        // 处理 URL 打开
        for (UIOpenURLContext *context in URLContexts) {
            NSURL *url = context.URL;
            // 处理 URL 逻辑
            if ([ADTOpenAuthAPI handleOpenURL:url
                                     delegate:self]) {
                NSLog(@"handle success url=%@", url);
            }
        }
    }
    ```
  - AppDelegate或SceneDelegate 实现代理协议方法，SDK 在拿到鉴权结果后会在`onResp:`方法中回调，如果成功会返回 authCode 授权码，用于业务方服务端做 SSO 鉴权。

    ```
    @interface AppDelegate () <ADTOpenAuthAPIDelegate>

    //...

    #pragma mark ADTOpenAuthAPIDelegate

    - (void)onResp:(ADTBaseResp *)resp {
        if ([resp isKindOfClass:[ADTOpenAuthResp class]]) {
            ADTOpenAuthResp *authResp = (ADTOpenAuthResp *)resp;
            
            NSString *authCode = authResp.authCode;

            // 将授权码 authCode 交给服务端做SSO鉴权
        }
    }
    ```

### **步骤三：授权登录**

- 发起登录鉴权

  - 在需要登录的业务场景调用`sendReq:onViewController:`方法发起登录鉴权，如果在 LSApplicationQueriesSchemes 条目中添加了钉钉跳转白名单，会优先尝试跳转钉钉进行鉴权，否则吊起应用内 H5 页面进行鉴权。请求中的参数 redirectUrl需要与开放平台配置的重定向 URL 保持一致。

    ```
    - (void)tryAuthLogin {
        ADTOpenAuthReq *req = [ADTOpenAuthReq new];
        // 必选参数
        req.redirectUrl = @"https://www.dingtalk.com/auth";
        req.responseType = @"code";
        req.scope = @"openid corpid";
        req.prompt = @"consent";
        // 建议添加一个随机数，作用见下面文档
        //req.state = @"defaultState";
        
        //当H5授权时，会使用此viewController做present一个网页；如果传nil，会导致无法打开授权H5网页.
        BOOL result = [ADTOpenAuthAPI sendReq:req onViewController:self];
        if (result) {
            NSLog(@"授权登录 发送成功.");
        }
        else {
            NSLog(@"授权登录 发送失败.");
        }
    }
    ```

    **参数说明：**

    | 参数 | 是否必填 | 备注 |
    | --- | --- | --- |
    | appId | 是 | 钉钉开放平台应用标识，即第一步中获取的AppKey。 |
    | redirectUri | 是 | 创建应用时填写的回调域名，仅用于校验域名是否一致，不会跳转。  **[!NOTE]**  需要与创建应用时填写的回调域名保持一致。 |
    | responseType | 是 | 当前只支持固定值code，授权通过后返回authCode。 |
    | scope | 是 | 应用授权作用域。授权页面显示的授权信息以应用注册时配置的为准  当前只支持两种输入：  - "openid"：授权后可获得用户openid。 - "openid corpid"：授权后可获得用户openid和登录过程中用户选择的组织corpId。 |
    | nonce | 否 | 字段值任意填写，授权登录后原样返回。 |
    | state | 否 | 用于保持请求和回调的状态，授权请求后原样带回给第三方。  **[!NOTE]**  该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数加session进行校验。 |
    | prompt | 否 | 固定值为consent，会进入授权确认页。 |
- 获取 accessToken，accessToken 是登录用户的访问凭证。

  - 根据 authCode 调用接口获取 accessToken，由业务方服务端接入，可参考[接入文档](../02-4a8AMF6u2A-服务端-API/0032-obtain-user-token.md)。
  - 客户端本地可以通过[接口调试工具](https://open-dev.dingtalk.com/apiExplorer?spm=ding_open_doc.document.0.0.2bd4492dQuxTUk#/?devType=isv&api=oauth2_1.0%23GetUserToken)进行调试，
- 获取用户通讯录相关信息

  - 根据 accessToken 调用接口获取用户通讯录相关信息，由业务方服务端接入，可参考[接入文档](../02-4a8AMF6u2A-服务端-API/0054-dingtalk-retrieve-user-information.md)。
  - 客户端本地可以通过[接口调试工具](https://open-dev.dingtalk.com/apiExplorer?spm=ding_open_doc.document.0.0.2e901f874Ka2xN#/?devType=isv&api=contact_1.0%23GetUser)进行调试

## **Android接入登录**

### **步骤一：创建钉钉应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/shareMan)，打开应用列表页，点击应用进入应用详情页。

   ![企业内部应用-移动端-分享打开应用 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386713.png)
2. 在应用信息页面，获取应用的AppKey和AppSecret。![iShot2022-08-26 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p481671.png)
3. 在应用详情页，单击**分享设置**，进入登录与分享页面。

   ![移动应用接入-钉钉登录与分享 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386717.png)
4. 在**接入登录**栏，添加回调域名。

   > **[!NOTE]**
   >
   > 在授权登录过程中，钉钉会校验授权接口的参数redirectUri，与此处配置的域名是否一致。

   ![iShot2022-08-25 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p481462.png)
5. 在**接入分享**栏，打开Android分享，填入包名及签名。

   ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p676009.png)

### **步骤二：搭建开发环境**

Android Studio 环境下：

1. 在build.gradle文件中，指定仓库并添加如下依赖：

   - 指定仓库：

     ```
     repositories {
        mavenCentral()
     }
     ```
   - 添加依赖：

     ```
     dependencies {
      implementation 'com.alibaba.android:ddopenauth:1.5.0.10'
     }
     ```
2. 在工程AndroidManifest.xml中添加声明：

   ```
   <uses-permission android:name="android.permission.INTERNET" />
   <!--如果你的App targetSdkVersion>=30，请添加权限声明-->
   <uses-permission android:name="android.permission.QUERY_ALL_PACKAGES" />
   ```

   如需混淆，建议混淆文件中增加：

   ```
   -keep class com.android.dingtalk.openauth.**{*;}
   ```

### **步骤三：发送请求到钉钉**

```
AuthLoginParam.AuthLoginParamBuilder builder = AuthLoginParam.AuthLoginParamBuilder.newBuilder();
builder.appId(yourAppId);
builder.redirectUri(yourRedirectUri);
builder.responseType(responseType);
builder.scope(scope);
builder.nonce(nonce);
builder.state(state);
builder.prompt(prompt);
IDDAuthApi authApi = DDAuthApiFactory.createDDAuthApi(context, builder.build());
authApi.authLogin()
```

**参数说明：**

| 参数 | 是否必填 | 备注 |
| --- | --- | --- |
| appId | 是 | 钉钉开放平台应用标识，即第一步中获取的AppKey。 |
| redirectUri | 是 | 创建应用时填写的回调域名，仅用于校验域名是否一致，不会跳转。  **[!NOTE]**  需要与创建应用时填写的回调域名保持一致。 |
| responseType | 是 | 当前只支持固定值code，授权通过后返回authCode。 |
| scope | 是 | 应用授权作用域。授权页面显示的授权信息以应用注册时配置的为准  当前只支持两种输入：   - openid：授权后可获得用户oepnid。 - openid%20corpid：授权后可获得用户openid和登录过程中用户选择的组织corpId。 |
| nonce | 否 | 字段值任意填写，授权登录后原样返回。 |
| state | 否 | 用于保持请求和回调的状态，授权请求后原样带回给第三方。  **[!NOTE]**  该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数加session进行校验。 |
| prompt | 是 | 固定值为consent，会进入授权确认页。 |

#### **当前用户已安装钉钉，则跳转钉钉APP拉起授权登录页**

> **[!NOTE]**
>
> 第三步截图只在首次授权登录时出现。

![iShot2022-08-25 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2159592871/p481471.png)

#### **当前用户未安装钉钉时，通过H5登录并授权**

> **[!NOTE]**
>
> 第三步截图只在首次授权登录时出现。

![iShot2022-08-25 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2159592871/p481475.png)

### **步骤四：接收授权结果**

1. 在包名相应目录下新建ddauth，并新增DDAuthActivity：![iShot2022-08-25 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p481481.png)
2. 在工程AndroidManifest.xml中添加声明：

   ```
   <!-- 钉钉统一登录 sdk 回调 Activity -->
   <activity
    android:name=".ddauth.DDAuthActivity"
    android:exported="true" />
   <!-- 钉钉统一登录 sdk 回调 Activity -->
   ```
3. 在DDAuthActivity中接收回调：

   ```
   public class DDAuthActivity extends AppCompatActivity {

      @Override
      protected void onCreate(@Nullable Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);

       Intent intent = getIntent();
       String authCode = intent.getStringExtra(DDAuthConstant.CALLBACK_EXTRA_AUTH_CODE);
       String state = intent.getStringExtra(DDAuthConstant.CALLBACK_EXTRA_STATE);
       String error = intent.getStringExtra(DDAuthConstant.CALLBACK_EXTRA_ERROR);

       if(!TextUtils.isEmpty(authCode)) {
       // 授权成功
       } else {
       // 授权失败
       }
       finish();
      }
   }
   ```

   **返回值说明**：

   | 返回值 | 说明 |
   | --- | --- |
   | error | 取值：  - ERR\_OK = 0（用户同意） - ERR\_AUTH\_DENIED = -4（用户角色授权） - ERR\_USER\_CANCEL = -2（用户取消） |
   | authCode | 授权码，可换取个人用户accessToken的凭证。  **[!NOTE]**  authCode只能使用一次。 |
   | state | 调用方标识其请求的唯一性的标志，state字符串长度不能超过1K。 |

### **步骤五：获取用户个人access\_token**

使用步骤四返回的authCode，调用[获取用户token](../02-4a8AMF6u2A-服务端-API/0032-obtain-user-token.md)接口，换取用户个人access\_token。

```
public class Test {
    public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoauth2_1_0.Client(config);
    }
    public void getUserToken() throws Exception {
        com.aliyun.dingtalkoauth2_1_0.Client client = Test.createClient();
        GetUserTokenRequest getUserTokenRequest = new GetUserTokenRequest()
                .setClientId("dingzxxxx") //第一步创建应用时获取的AppKey。
                .setClientSecret("XyJONrxxxxx") //第一步创建应用时获取的AppSecret。
                .setCode("18ec1db4xxxxx") //第四步获取的authCode。
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
}
```

### **步骤六：获取用户个人信息**

使用步骤五获取的用户个人access\_token，调用[获取用户通讯录个人信息](../02-4a8AMF6u2A-服务端-API/0054-dingtalk-retrieve-user-information.md)接口，获取用户个人手机号、用户的钉钉昵称、头像URL、用户的个人邮箱等信息。

```
public class Test {
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public void getUserInfo() throws Exception {
        com.aliyun.dingtalkcontact_1_0.Client client = Test.createClient();
        GetUserHeaders getUserHeaders = new GetUserHeaders();
        getUserHeaders.xAcsDingtalkAccessToken = "17e756exxxx";//第五步获取的个人用户Token。
        try {
            GetUserResponse response = client.getUserWithOptions("me", getUserHeaders, new RuntimeOptions());
            System.out.println(JSON.toJSON(response));
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
}
```

## **鸿蒙接入登录**

### **步骤一：接入钉钉分享**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/shareMan)，找到自己的创建的应用，单击应用进入应用详情页。

   ![企业内部应用-移动端-分享打开应用 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386713.png)
2. 在应用信息页面，获取应用的 **Client ID**。

   ![iShot2022-08-26 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p481671.png)
3. 在应用详情页，单击**分享设置**，进入登录与分享页面。

   ![移动应用接入-钉钉登录与分享 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386717.png)
4. 在**接入登录**栏，添加回调域名。

   > **[!NOTE]**
   >
   > 在授权登录过程中，钉钉会校验授权接口的参数redirectUri，与此处配置的域名是否一致。

   ![iShot2022-08-25 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p481462.png)
5. 在**接入分享**栏，开启 鸿蒙**分享**，然后依次填写鸿蒙应用 **Bundle Name**和 **Identifier**，最后单击保存。

   > **[!NOTE]**
   >
   > **Identifier** 为 鸿蒙应用唯一标识 **appIdentifier**而不是 appId，详情见官方文档：[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V14/js-apis-bundlemanager-bundleinfo-V14)

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005961.png)

### **步骤二：搭建开发环境**

DevEco Studio 环境下：

1. 在oh-package.json5文件中，添加@dingtalk/openauth依赖：

   ```
   {
     "name": "entry",
     "version": "1.0.0",
     "description": "",
     "main": "",
     "author": "",
     "license": "",
     "dependencies": {
       "@dingtalk/openauth": "1.1.0"
     }
   }
   ```
2. 在module.json5中添加querySchemes及requestPermissions权限配置。

   ```
   {
     "module": {
       "querySchemes": [
         "dingtalk"
       ],
       "requestPermissions": [
         {
           "name" : "ohos.permission.INTERNET"
         }
       ]
     }
   }
   ```

### **步骤三：发送请求到钉钉**

执行下方代码：

```
import { DDAuthApiFactory, AuthLoginParam } from '@dingtalk/openauth';

let param:AuthLoginParam = {
  // 钉钉开放平台应用标识
  appId: "Your AppId",
  // 创建应用时填写的回调域名，仅用于校验域名是否一致，不会跳转
  redirectUri: "Your redirectUri",
  // 返回时拉起的Ability页面
  callBackAbilityName: "EntryAbility",
  // 固定值code，授权通过后返回authCode
  responseType: "code",
  // 应用授权作用域 openid：授权后可获得用户openid, openid%20corpid：授权后可获得用户openid和登录过程中用户选择的组织corpId
  scope: "openid",
  // 固定值为consent，首次会进入授权确认页
  prompt: "consent",
  // 用于保持请求和回调的状态，授权请求后原样带回给第三方
  state: "state"
}
DDAuthApiFactory.createDDAuthApi(param).authLogin(component)
```

**参数说明：**

| 参数 | 是否必填 | 备注 |
| --- | --- | --- |
| appId | 是 | 钉钉开放平台应用标识，即第一步中获取的ClientId。 |
| redirectUri | 是 | 创建应用时填写的回调域名，仅用于校验域名是否一致，不会跳转。  **[!NOTE]**  需要与创建应用时填写的回调域名保持一致。 |
| responseType | 是 | 当前只支持固定值code，授权通过后返回authCode。 |
| scope | 是 | 应用授权作用域。授权页面显示的授权信息以应用注册时配置的为准  当前只支持两种输入：   - openid：授权后可获得用户oepnid。 - openid%20corpid：授权后可获得用户openid和登录过程中用户选择的组织corpId。 |
| prompt | 是 | 固定值为consent，会进入授权确认页。 |
| callBackAbilityName | 是 | 授权成功后显式Want唤起指定的Ability。  **[!NOTE]**  Ability需要在module.json5中配置"exported": true |
| nonce | 否 | 字段值任意填写，授权登录后原样返回。 |
| state | 否 | 用于保持请求和回调的状态，授权请求后原样带回给第三方。  **[!NOTE]**  该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数加session进行校验。 |
| targetBundleName | 否 | 指定的钉钉BundleName, 用于指定跳转钉钉专属版，不填时默认跳转钉钉标准版 |
| webForceLogin | 否 | true时钉钉未安装时不保留登录状态，每次授权都要求重新登录，默认为false |

#### **当前用户已安装钉钉，则跳转钉钉APP拉起授权登录页**

> **[!NOTE]**
>
> 第三步截图只在首次授权登录时出现。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005971.png) ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005969.png) ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005970.png)

#### **当前用户未安装钉钉时，通过H5登录并授权**

> **[!NOTE]**
>
> 第三步截图只在首次授权登录时出现。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005972.png) ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005974.png) ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1159592871/p1005973.png)

### **步骤四：接收授权结果**

在步骤三内填写的callBackAbilityName对应的Ability内接收授权结果：

```
export default class EntryAbility extends UIAbility {

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    if (want?.parameters?.action === "hmos.dingtalk.oauth2") {
      const authCode = want?.parameters?.authCode as string
      const state = want?.parameters?.state as string
      const error = want?.parameters?.error as string
      if (authCode) {
        promptAction.showToast({
          message: `授权成功 ${authCode}`
        });
      } else {
        promptAction.showToast({
          message: `授权失败 ${error}`
        });
      }
    }
  }
}
```

**返回值说明**：

| 返回值 | 说明 |
| --- | --- |
| error | 取值：   - **ERR\_OK = 0**：用户同意 - **ERR\_AUTH\_DENIED = -4**：用户角色授权 - **ERR\_USER\_CANCEL = -2**：用户取消 |
| authCode | 授权码，可换取个人用户accessToken的凭证。  **[!NOTE]**  authCode只能使用一次。 |
| state | 调用方标识其请求的唯一性的标志，state字符串长度不能超过1K。 |
