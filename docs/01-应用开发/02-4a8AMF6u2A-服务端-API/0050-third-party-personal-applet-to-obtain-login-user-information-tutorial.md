---
title: "第三方个人小程序获取登录用户信息"
source_url: "https://open.dingtalk.com/document/development/third-party-personal-applet-to-obtain-login-user-information-tutorial"
namespace: "development"
slug: "third-party-personal-applet-to-obtain-login-user-information-tutorial"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 使用教程 > 第三方个人小程序获取登录用户信息"
doc_id: "uYxi6nrUyo"
updated_at: "2026-09-15 09:36:10"
---

> Source: https://open.dingtalk.com/document/development/third-party-personal-applet-to-obtain-login-user-information-tutorial
> Path: 应用开发 / 服务端 API / 通讯录管理 > 使用教程 > 第三方个人小程序获取登录用户信息
> Updated: 2026-09-15 09:36:10

# 第三方个人小程序获取登录用户信息

## 概述

### 业务背景

独立开发者或小型团队在开发面向个人用户的小程序时，面临以下核心痛点：

- **用户注册门槛高**：传统应用需要用户手动注册账号，填写个人信息，降低用户使用意愿。
- **身份验证复杂**：需要独立实现用户认证模块，增加开发和维护成本。
- **用户体验割裂**：用户需要在钉钉和小程序之间切换，频繁登录影响使用流畅度。

### 核心价值

通过钉钉第三方个人应用免登方案，可以实现：

- **零注册体验**：用户无需额外注册，通过钉钉授权即可快速使用小程序。
- **身份自动获取**：基于OAuth 2.0协议自动获取用户身份信息。
- **降低开发成本**：复用钉钉身份体系，无需独立实现用户认证模块。

### 适用场景

本文档适用于**第三方个人开发者**，需要为钉钉上的个人用户提供小程序服务。典型场景包括：

- **个人工具类应用**：待办清单、笔记记录、日程管理等个人效率工具。
- **生活服务类应用**：记账、健身追踪、阅读打卡等生活辅助工具。
- **内容消费类应用**：资讯阅读、视频观看、音乐播放等内容型应用。

> **[!NOTE]**
>
> 第三方个人应用由产品方案商开发者开发，提供给钉钉上个人用户使用的小程序，通过免登机制让用户无需输入账号密码即可登录。

## 典型业务场景

### 场景一：个人工具类小程序

- **实施前**

  ![个人工具实施前流程_20260910_093501_20260910_093630](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0716349871/p1102036.png)
- **实施后**

  ![个人工具实施后流程_20260910_093558_20260910_093724](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0716349871/p1102037.png)
- **价值收益**

  - 用户注册时间从平均30秒降至0秒 。
  - 开发者运维成本降低80%（无需维护用户账号体系） 。
  - 用户留存率提升（免去注册步骤，降低使用门槛）。

### 场景二：跨平台个人应用

- **典型流程**

  ![跨平台个人应用流程_20260910_093655_20260910_093826](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0716349871/p1102038.png)
- **关键优势**

  - 一套代码服务所有个人用户，无需为每个用户单独配置。
  - 基于钉钉openId唯一标识用户，数据安全隔离。
  - 用户更换设备后仍可同步数据（openId不变）。

## **实施指南**

### **背景说明**

在开始开发前，请确保已理解钉钉开放平台的基本概念，包括：

- **第三方个人应用：**产品方案商开发者开发，提供给钉钉上个人用户使用的小程序。
- **免登机制：**用户无需输入账号密码，通过钉钉客户端授权即可登录应用。

### 前提条件

1. 注册了钉钉管理员账号。如果没有注册，请[单击这里完成注册](https://www.dingtalk.com/)。
2. 安装小程序开发者工具IDE，详情参见[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)。
3. 安装了Java开发环境（JDK1.6及以上）以及Java项目构建工具Maven。
4. 参见[第三方个人应用学习指南](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md)介绍，完成第三方个人应用创建。

### **代码实现**

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击**应用开发 > 第三方个人应用**后，**创建应用**。

步骤二：单击**基础信息 > 应用信息**，获取应用`AppId`和`AppSecret`。

步骤三：[添加接口调用权限](0003-add-api-permission.md)。确定需申请的权限，申请对应的权限。

步骤四：使用授权套件获取authCode。

步骤五：获取个人用户身份访问凭证[获取用户token](0031-obtain-user-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤六：调用服务端API-[获取用户通讯录个人信息](0053-dingtalk-retrieve-user-information.md)接口。

## **实施步骤**

### **步骤一：获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **应用信息**。
4. 记录应用的`AppId`和`AppSecret`。

   ![iShot2022-08-23 20](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9547521661/p480322.png)

### **步骤二：申请接口权限**

1. **确认需要申请哪些权限**

   应用需要获取哪些信息，申请的权限不同。请参考权[个人权限scope列表](0007-function-description.md#50679ce2b8jpj)确认需要开通哪些权限。

   > **[!NOTE]**
   >
   > 如果需要获取用户个人手机号，则需要申请开通[获取用户通讯录个人信息](0053-dingtalk-retrieve-user-information.md)接口权限和字段权限。
2. **申请接口或字段权限**

   - 登录[开发者后台](https://open-dev.dingtalk.com/#/)，选择进入对应的应用。
   - 在应用的**权限管理**页面，输入对应权限关键字进行搜索，然后选择对应的权限单击**申请权限**。

     例如，需要获取用户个人手机号信息，搜索**个人信息**，选择**个人权限**，并单击**申请权限**。添加**通讯录个人信息读权限**和**个人手机号信息**权限。

     ![iShot2022-08-23 20](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9547521661/p480310.png)

### **步骤三：使用授权套件获取authCode**

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

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0716349871/p1102042.png)

   单击允许后，**page.onShow**方法内调用的**disposeAuthData**方法内可获取authCode值**。**

### **步骤四：调用服务端接口**

1. 调用[获取用户token](0031-obtain-user-token.md)接口，获取获取个人用户身份访问凭证。

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
2. 调用服务端API-[获取用户通讯录个人信息](0053-dingtalk-retrieve-user-information.md)接口，获取登录用户信息。

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

### **步骤五：验证与调试**

为确保免登流程稳定运行，建议开发者进行以下验证与调试操作：

#### **检查API调用状态**

查看关键接口的调用次数与成功率。

#### **错误码排查**

若调用失败，请查看全局错误码：

- `errcode=40001`：access\_token无效 → 检查`AppId`和`AppSecret`是否正确。
- `errcode=40029`：code无效 → 用户重新触发免登获取新code。
- `errcode=60020`：未授权接口权限 → 在开发者后台添加接口调用权限并提交审核。

#### **典型场景判断依据**

- ✅ **成功场景：**用户免登后能正确显示姓名、openId等信息。
- ❌ **失败场景：**提示"网络请求失败"、"安全域名未配置"等 → 检查服务日志、安全域名配置、后端服务连通性。

## 常见问题

- **Q1：无法关联小程序应用如何处理？**

  答：请确认当前登录账号是否已被添加为该应用的开发人员。登录开发者后台，进入应用详情页，在"人员管理"中检查并添加对应成员。
- **Q2：调用接口返回errcode错误如何处理？**

  答：请根据返回的errcode值查阅[钉钉开放平台全局错误码文档](0013-server-api-error-codes-1.md)。
- **Q3：前端无法获取用户信息可能是什么原因？**

  答：可能原因包括：

  - 安全域名未设置或配置错误 。
  - 后端服务未正常启动或接口不可达。
  - access\_token获取失败，检查`AppId`和`AppSecret`是否正确。
  - 小程序未上传新版本导致缓存未更新。
