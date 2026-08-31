---
title: "实现网页方式登录应用（登录第三方网站）"
source_url: "https://open.dingtalk.com/document/development/tutorial-obtaining-user-personal-information"
namespace: "development"
slug: "tutorial-obtaining-user-personal-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 网页应用免登 > 实现网页方式登录应用（登录第三方网站）"
doc_id: "fhfqc76nqi"
updated_at: "2026-07-02 10:35:22"
---

> Source: https://open.dingtalk.com/document/development/tutorial-obtaining-user-personal-information
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 网页应用免登 > 实现网页方式登录应用（登录第三方网站）
> Updated: 2026-07-02 10:35:22

# 实现网页方式登录应用（登录第三方网站）

本文档指导你如何实现用户通过浏览器登录应用（扫码或账密方式）。在本场景中，企业内部应用可以通过浏览器网页方式获取用户授权的个人信息。

> **[!NOTE]**
>
> - 企业内部应用与三方企业应用实现流程类似，本文档以企业内部应用实现流程为例。
> - 因内部应用的安全考虑，企业内部应用**不支持跨组织**授权登录。即只有组织内的用户可以通过浏览器网页方式登录应用。

## **简介**

### **教学内容**

本教程介绍用户通过网页（浏览器）的方式登录钉钉应用，并在第三方网站获取用户授权信息。

### **教学目标**

将通过两种实现方式实现网页登录钉钉应用：

- 内嵌二维码方式实现用户登录授权
- 构造钉钉登录链接的方式实现用户登录授权

### **教学范围**

面向钉钉应用开发者

## **前提条件**

- 已经获取开发者权限。
- 已经申请了`Contact.User.mobile`和`Contact.User.Read`权限点，如何申请可参考[添加接口调用权限](0003-add-api-permission.md)。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **开发流程**

### **方式一：使用钉钉提供的页面登录授权**

构造钉钉应用授权登录访问地址

> **[!IMPORTANT]**
>
> - 为了方便阅读，以下参数示例做了换行处理。正常情况下无需进行参数换行。
> - redirect\_uri必须要做urlencode，以下示例已经进行urlencode。
> - 以下登录页面在初次校验登录状态时显示。

redirect\_uri必须要做urlencode

```
https://login.dingtalk.com/oauth2/auth?
redirect_uri=https%3A%2F%2Fwww.aaaaa.com%2Fauth
&response_type=code
&client_id=dingxxxxxxx   //应用的AppKey 
&scope=openid corpid  //此处的openId保持不变
&state=dddd
&prompt=consent
```

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| redirect\_uri | 是 | 授权通过/拒绝后回调地址。  **[!IMPORTANT]**  需要与开发者后台钉钉登录与分享的地址保持一致，redirect\_uri需要进行urlencode。 |
| response\_type | 是 | 固定值为code。  授权通过后返回authCode。 |
| client\_id | 是 | 步骤一中创建的应用详情中获取。   - 企业内部应用：client\_id为应用的 Client ID。 - 第三方企业应用：client\_id为应用的 Client ID。 |
| scope | 是 | 授权范围，授权页面显示的授权信息以应用注册时配置的为准。  当前只支持两种输入：   - **openid**：授权后可获得用户userid - **openid corpid**：授权后可获得用户id和登录过程中用户选择的组织id，空格分隔。注意url编码。 |
| prompt | 是 | 值为consent时，会进入授权确认页。 |
| state | 否 | 跟随authCode原样返回。 |
| org\_type | 否 | 控制输出特定类型的组织列表，org\_type=management 表示只输出有管理权限的组织。  **[!IMPORTANT]**  scope包含corpid时该参数存在意义。 |
| corpId | 否 | 用于指定用户需要选择的组织。  **[!IMPORTANT]**   - scope包含corpid时该参数存在意义。 - 传入的corpId需要是当前用户所在的组织。 |

### **方式二：内嵌二维码方式登录授权**

> **[!IMPORTANT]**
>
> 嵌入二维码的页面必须和redirect\_uri参数所指定的页面“同源”，否则扫码后会没有反应，“同源”指：协议相同、二级或三级域名相同、端口号相同等。详情请参考文档[浏览器的同源策略](https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy)。

1. 在页面中引入钉钉扫码登录 JS SDK。

   ```
   <script src="https://g.alicdn.com/dingding/h5-dingtalk-login/0.21.0/ddlogin.js"></script>
   ```
2. 在需要引入扫码登录的地方，调用如下方法。

   ```
   <!-- STEP1：在HTML中添加包裹容器元素 -->
   <div id="self_defined_element" class="self-defined-classname"></div>
   <style>
       /* STEP2：指定这个包裹容器元素的CSS样式，尤其注意宽高的设置 */
       .self-defined-classname {
           width: 300px;
           height: 300px;
       }
   </style>
   <script>
       // STEP3：在需要的时候，调用 window.DTFrameLogin 方法构造登录二维码，并处理登录成功或失败的回调。
       window.DTFrameLogin(
           {
               id: 'self_defined_element',
               width: 300,
               height: 300,
           },
           {
               redirect_uri: encodeURIComponent('http://www.aaaaa.com/a/b/'),
               client_id: 'dingxxxxxxxxxxxx',
               scope: 'openid',
               response_type: 'code',
               state: 'xxxxxxxxx',
               prompt: 'consent',
           },
           (loginResult) => {
               const {redirectUrl, authCode, state} = loginResult;
               // 这里可以直接进行重定向
               window.location.href = redirectUrl;
               // 也可以在不跳转页面的情况下，使用code进行授权
               console.log(authCode);
           },
           (errorMsg) => {
               // 这里一般需要展示登录失败的具体原因,可以使用toast等轻提示
               console.error(`errorMsg of errorCbk: ${errorMsg}`);
           },
       );
   </script>
   ```

   参数说明((TypeScript语言描述))：

   ```
   // ********************************************************************************
   // window.DTFrameLogin方法定义
   // ********************************************************************************
   window.DTFrameLogin: (
     frameParams: IDTLoginFrameParams, // DOM包裹容器相关参数
     loginParams: IDTLoginLoginParams, // 统一登录参数
     successCbk: (result: IDTLoginSuccess) => void, // 登录成功后的回调函数
     errorCbk?: (errorMsg: string) => void,         // 登录失败后的回调函数
   ) => void;

   // ********************************************************************************
   // DOM包裹容器相关参数
   // ********************************************************************************
   // 注意！width与height参数只用于设置二维码iframe元素的尺寸，并不会影响包裹容器尺寸。
   // 包裹容器的尺寸与样式需要接入方自己使用css设置
   interface IDTLoginFrameParams {
     id: string;      // 必传，包裹容器元素ID，不带'#'
     width?: number;  // 选传，二维码iframe元素宽度，最小280，默认300
     height?: number; // 选传，二维码iframe元素高度，最小280，默认300
   }

   // ********************************************************************************
   // 统一登录参数
   // ********************************************************************************
   // 参数意义与“拼接链接发起登录授权”的接入方式完全相同（缺少部分参数）
   // 增加了isPre参数来设定运行环境
   interface IDTLoginLoginParams {
     redirect_uri: string;     // 必传，注意url需要encode
     response_type: string;    // 必传，值固定为code
     client_id: string;        // 必传
     scope: string;            // 必传，如果值为openid+corpid，则下面的org_type和corpId参数必传，否则无法成功登录
     prompt: string;           // 必传，值为consent。
     state?: string;           // 选传
     org_type?: string;        // 选传，当scope值为openid+corpid时必传
     corpId?: string;          // 选传，当scope值为openid+corpid时必传
     exclusiveLogin?: string;  // 选传，如需生成专属组织专用二维码时，可指定为true，可以限制非组织账号的扫码
     exclusiveCorpId?: string; // 选传，当exclusiveLogin为true时必传，指定专属组织的corpId
   }

   // ********************************************************************************
   // 登录成功后返回的登录结果
   // ********************************************************************************
   interface IDTLoginSuccess {
     redirectUrl: string;   // 登录成功后的重定向地址，接入方可以直接使用该地址进行重定向
     authCode: string;      // 登录成功后获取到的authCode，接入方可直接进行认证，无需跳转页面
     state?: string;        // 登录成功后获取到的state
   }
   ```

1. 访问已经构造的钉钉应用授权登录访问地址（方式一）/通过扫描二维码的方式实现用户登录授权（方式二）。
2. 当用户同意授权后，此时会携带 authCode 到步骤五重定向 URL 的路径后，例如：`http://example.com?code=f85c6*****7b77&authCode=f85c6******e49e87b77`。

   > 此处，code 和 authCode 一致，取任一即可。
3. 根据 authCode，调用服务端[获取用户token](0032-obtain-user-token.md)接口，获取用户个人token。
4. 根据用户个人token，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口，获取授权用户个人信息。

   > **[!NOTE]**
   >
   > 调用获取用户通讯录个人信息接口，获取当前授权人的信息，unionId参数值传字符串me。

   至此，你就可以获取到用户的个人授权信息。

## **步骤一：创建并配置应用**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**应用开发** > **企业内部应用** > **钉钉应用** > **创建应用**。
3. 填写应用信息。

   | **配置项** | **是否必选** | **配置说明** |
   | --- | --- | --- |
   | **应用名称** | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | **应用描述** | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
4. 单击**保存**，进入应用详情页，单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 和 Client Secret。

   > 注意：请保存 Client ID 和 Client Secret，后续会使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026341.png)
5. 在应用详情页，单击**开发配置** > **安全设置**，进入安全配置页面。
6. 在重定向URL（回调域名）一栏中，输入`http://localhost:5173`，用于后续前端页面重定向使用。

   > 本示例使用`http://localhost:5173`作为重定向域名，你可以根据实际环境定义。
7. 配置完成后，单击保存。

## **步骤二：发布应用**

1. 在应用详情页，单击**应用发布** > **版本管理与发布**，进入版本发布页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026340.png)
2. 单击创建新版本，进入版本详情页面。
3. 配置版本信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用版本号 | 使用默认版本即可。 |
   | 版本信息 | 填写版本信息内容，根据自身业务情况填写。 |
   | 应用可见范围 | 选择任意范围即可。 |

   配置完成后。单击下方保存。
4. 在保存成功的弹框页面，单击直接发布。

   > 如果你不是企业管理员，发布应用时需要企业管理员审批，发布仅我可见则无需管理员审批。

## **步骤三：构建服务**

### **方式一：使用钉钉提供的页面登录授权**

1. 确保已经完成上方步骤，获取运行下方demo示例的参数和基本配置。
2. 下载[web-login-application-demo-java-construct-link.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251210/qagtgn/web-login-application-demo-java-construct-link.zip)示例 Demo。
3. 打开 IDE，并导入已下载的 Demo。

   > *示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。*

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026347.png)
4. 打开后端代码目录，在 resources 目录中修改`application.properties`文件，填写`clientId（应用Client ID）`和`clientSecret（应用Client Secret）`参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026349.png)
5. 点击启动后端服务。

   > **[!NOTE]**
   >
   > - 在启动后端服务前，请确保已经正确安装Maven 和 JDK，并配置了相关环境；如果是初次安装 IDE，需要在 IDE 中修改相关配置文件。
   > - 确保 5173 和 8080 端口没有被占用。
6. 点击前端项目文件，鼠标右键并选择**终端**打开。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026353.png)
7. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`

      > *注意：windows 在启动时候，请使用*`npm run dev:raw`
8. 至此，前端和后端服务已经启动成功。

### **方式二：内嵌二维码方式登录授权**

1. 确保已经完成上方步骤，获取运行下方demo示例的参数和基本配置。
2. 下载[web-login-application-demo-java-scan-code.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251113/tpcjjr/web-login-application-demo-java-scan-code.zip)示例 Demo。
3. 打开 IDE，并导入已下载的 Demo。

   > *示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。*

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026434.png)
4. 打开后端代码目录，在 resources 目录中修改`application.properties`文件，填写`clientId（应用Client ID）`和`clientSecret（应用Client Secret）`参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026435.png)
5. 打开前端代码目录，在src目录下修改 `main.js`，并填写正确的`corpId`和`clientId（应用Client ID）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026440.png)
6. 点击启动后端服务。

   > **[!NOTE]**
   >
   > - 在启动后端服务前，请确保已经正确安装Maven 和 JDK，并配置了相关环境；如果是初次安装 IDE，需要在 IDE 中修改相关配置文件。
   > - 确保 5173 和 8080 端口没有被占用。
7. 点击前端项目文件，鼠标右键并选择**终端**打开。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2987113671/p1026441.png)
8. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`

      > *注意：windows 在启动时候，请使用*`npm run dev:raw`
9. 至此，前端和后端服务已经启动成功。

## **步骤四：测试应用**

1. 在浏览器访问`http://localhost:5173`，展示界面如下：

   | **展示** | **说明** |
   | --- | --- |
   | 使用钉钉提供的页面登录授权 | image |
   | 内嵌二维码方式登录授权 | image |
2. 扫描二维码/打开钉钉登录授权页，用户授权后，即可查看用户个人信息。

   > 第三方企业应用无法获取用户完整手机号，为保障用户数据安全，已对手机号信息进行脱敏处理，第三方企业应用获取手机号示例：`155****3240`。

   | **展示** | **说明** |
   | --- | --- |
   | 使用钉钉提供的页面登录授权 | image |
   | 内嵌二维码方式登录授权 | image |
