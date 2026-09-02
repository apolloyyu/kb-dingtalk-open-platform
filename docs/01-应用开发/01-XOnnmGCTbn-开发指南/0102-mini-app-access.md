---
title: "接入流程"
source_url: "https://open.dingtalk.com/document/dingstart/mini-app-access"
namespace: "dingstart"
slug: "mini-app-access"
group: "应用开发"
tab: "开发指南"
breadcrumb: "接入移动客户端 > 接入钉钉分享 > 接入流程"
doc_id: "T1ayomqmbQ"
updated_at: "2026-07-02 10:31:47"
---

> Source: https://open.dingtalk.com/document/dingstart/mini-app-access
> Path: 应用开发 / 开发指南 / 接入移动客户端 > 接入钉钉分享 > 接入流程
> Updated: 2026-07-02 10:31:47

# 接入流程

本文介绍如何使用钉钉分享SDK接入钉钉分享。

## **分享SDK下载**

仅适用需要接入钉钉分享能力，帮助用户在钉钉 App 分享信息。

### **iOS**

| **基本信息** | **说明** |
| --- | --- |
| SDK名称 | 钉钉分享SDK（iOS） |
| 开发者 | 钉钉科技有限公司 |
| 功能介绍 | 帮助用户在钉钉 App 分享信息 |
| 包名 | com.laiwang.DTShareKit |
| MD5值 | 1585c506a5feaf540509919b03a4fac0 |
| 最新版本 | 3.1.0 |
| 下载地址 | [点击下载](https://files.alicdn.com/tpsservice/94a5e78286e0d71c935165a28da1514b.zip) |
| 使用说明 | - 安装钉钉客户端2.7.0及以上版本。 - iOS DTShareSDK部署系统版本为 iOS 12.0 及以上。 - 下载并使用本SDK，即表示您已阅读并同意《[钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md)》、《[钉钉开放平台开发者服务协议](../07-TjCzIgfQs3-平台服务/0002-open-platform-developer-service-agreement.md)》。 |
| 个人信息处理规则 | 规则：   - [iOS分享SDK合规指南](0103-mini-app-ios-sharing-sdk-compliance-guide.md) - [钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md) |
| 更新日期 | 2024-01-11 |

### **Android**

| **基本信息** | **说明** |
| --- | --- |
| SDK名称 | 钉钉分享SDK（Android） |
| 开发者 | 钉钉科技有限公司 |
| 功能介绍 | 帮助用户在钉钉 App 分享信息 |
| 包名 | com.android.dingtalk.share |
| MD5值 | 8ece42b7615a2fb86880737ccf60b91a |
| 最新版本 | 1.2.0.3 |
| 下载地址 | [点击下载](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260325/qrxlhj/Android%E5%88%86%E4%BA%AB%E5%B7%A5%E5%85%B7%E5%8C%85.zip)（文件包含Demo和Jar包） |
| 使用说明 | - 安装钉钉客户端2.7.0及以上版本。 - 下载并使用本SDK，即表示您已阅读并同意《[钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md)》、《[钉钉开放平台开发者服务协议](../07-TjCzIgfQs3-平台服务/0002-open-platform-developer-service-agreement.md)》。 |
| 更新日期 | 2024-03-04 |
| 个人信息处理规则 | 规则：   - [Android分享SDK合规指南](0104-mini-app-android-share-sdk-compliance-guide.md) - [钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md) |

> Android用户注册需要提供签名，具体步骤参考 SDK 下载压缩包里面“常见问题.docx”文件。

### **HarmonyOS**

| **基本信息** | **说明** |
| --- | --- |
| SDK名称 | 钉钉分享SDK（HarmonyOS） |
| 开发者 | 钉钉科技有限公司 |
| 功能介绍 | 帮助用户在钉钉 App 分享信息 |
| 包名 | @dingtalk/ddsharesdk |
| MD5值 | 534953fa4f8874a44faa27f0c568ee1a |
| 最新版本 | 1.1.5 |
| 下载地址 | [点击下载](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251031/zqfluo/ddsharesdk.har) |
| 使用说明 | - IDE 5.0.3.906 以上，API 12及以上。 - 安装钉钉客户端7.6.23及以上版本。 - iOS DTShareSDK部署系统版本为 iOS 12.0 及以上。 - 下载并使用本SDK，即表示您已阅读并同意《[钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md)》、《[钉钉开放平台开发者服务协议](../07-TjCzIgfQs3-平台服务/0002-open-platform-developer-service-agreement.md)》。 |
| 个人信息处理规则 | 规则：   - [鸿蒙分享SDK合规指南](0105-harmony-share-sdk-compliance-guide.md) - [钉钉开放平台隐私权政策](../07-TjCzIgfQs3-平台服务/0001-open-latform-privacy-policy.md) |
| 更新日期 | 2025.10.22 |

## **iOS接入分享**

### **步骤一：接入钉钉分享**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/shareMan)，打开应用列表页，单击应用进入应用详情页。

   ![企业内部应用-移动端-分享打开应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386713.png)
2. 在应用信息页面，获取应用的AppKey。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p740486.png)
3. 在应用详情页，单击**钉钉登录与分享**，进入登录与分享页面。

   ![移动应用接入-钉钉登录与分享](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386717.png)
4. 在**接入分享**栏，开启**iOS 分享**，然后输入**iOS Bundle ID**，最后单击保存。

   > **[!NOTE]**
   >
   > iOS Bundle ID应填写你的iOS应用对应的ID。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p745935.png)

### **步骤二：配置iOS应用**

1. 将已下载的iOS SDK的framework导入到工程中。

   ![1543219285868-c74da8e9-f2c5-405f-9ef4-bbdbb9724adc.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9923269951/p163310.png)
2. 配置工程。

   1. 在**Other Linker Flags**添加 `-all_load`选项。

      ![TB118c9KVXXXXcIaXXXXXXXXXXX-808-201.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9923269951/p163311.png)
   2. 在**Custom iOS Target Properties**的**LSApplicationQueriesSchemes**列表中添加dingtalk、dingtalk-open。

      > **[!NOTE]**
      >
      > iOS系统限制LSApplicationQueriesSchemes最多只能有50个，超出部分有可能不生效。尤其是Xcode13打包，iOS15.0及以上，超出部分不生效。
   3. 在**URL Types**中配置以下信息。

      | 内容 | 配置说明 |
      | --- | --- |
      | **Identifier** | dingtalk |
      | **URL Schemes** | 填写步骤一中获取的AppKey。  iShot2022-08-26 11 |

      ![移动应用接入-iOS分享配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1099842461/p386729.png)
   > **[!NOTE]**
   >
   > iOS9及以后的系统需要将钉钉和分享SDK的scheme配置在Info.plist。

### **步骤三：在代码中使用开发工具包**

1. 注册应用并添加必要的URLHandler。

   > **[!NOTE]**
   >
   > 代码中的 `[DTOpenAPl registerApp:@"appld"]` 中的 appId 为应用的 [Client ID](0001-basic-concepts-beta.md#section-pje-9wf-l7c)（原应用 AppKey）。

   如示例中，在AppDelegate.m文件中引用`AppDelegate.h`，在@implementation AppDelegate中增加如下代码：

   ![1529660134343-d20dbb6d-208c-4599-8d53-91cbe55d3b6d.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9923269951/p163313.png)
2. 分享数据到钉钉客户端。

   发送分享请求的过程主要分为两部分：

   1. 组装DTMediaMessage对象。

      不同类型的分享数据通过DTMediaMessage的mediaObject区分。

      | **类型** | **描述** |
      | --- | --- |
      | DTMediaTextObject | 纯文本数据。 |
      | DTMediaImageObject | 纯图片数据。 |
      | DTMediaWebObject | Web页面数据。 |
   2. 调用`+[DTOpenAPI sendReq:]`发送数据。

   下面是分享文本部分代码，其他类型请参考 SDK 相关方法注释：

   ```
   DTSendMessageToDingTalkReq *sendMessageReq = [[DTSendMessageToDingTalkReq alloc] init];
       
   DTMediaMessage *mediaMessage = [[DTMediaMessage alloc] init];
       
   DTMediaTextObject *textObject = [[DTMediaTextObject alloc] init];
   textObject.text = @"Hi DingTalk.";
       
   mediaMessage.mediaObject = textObject;
   sendMessageReq.message = mediaMessage;
   [DTOpenAPI sendReq:sendMessageReq completion:^(BOOL success) {
     if (success) {
          NSLog(@"[DTShareKitDemo] Text 发送成功.");
        }
     else {
          NSLog(@"[DTShareKitDemo] Text 发送失败.");
        }
    }];
   ```

   > **[!NOTE]**
   >
   > - 分享纯图片数据和Web页面缩略图时，可以使用图片URL和图片Data两种形式，钉钉内优先使用图片Data形式。
   > - 分享数据的数据量限制在SDK的头文件中均有描述，超过限制的数据不会发送到钉钉客户端。
3. 判断当前设备是否支持分享到钉钉。

   钉钉从2.7版本开始支持分享，SDK中提供了接口来判断当前设备是否能够支持分享到钉钉。

   ```
   /**
    检测设备是否安装了钉钉客户端.
    
    @return YES 设备安装了钉钉客户端. NO 设备没有安装钉钉客户端.
    */
   + (BOOL)isDingTalkInstalled;

   /**
    检测设备安装的钉钉是否支持钉钉OpenAPI.
    
    @return YES 设备安装的钉钉客户端支持钉钉OpenAPI. NO 设备安装的钉钉客户端不支持钉钉OpenAPI.
    */
   + (BOOL)isDingTalkSupportOpenAPI;

   /**
    检测设备安装的钉钉是否支持钉钉SSO授权.
    
    @return YES 设备安装的钉钉客户端支持钉钉SSO授权. NO 设备安装的钉钉客户端不支持钉钉SSO授权.
    */
   + (BOOL)isDingTalkSupportSSO;

   /**
    获取钉钉在AppStore的安装地址.
    
    @return 钉钉在AppStore的安装地址.
    */
   + (NSString *)appStoreURLOfDingTalk;
   ```

   > **[!NOTE]**
   >
   > 在iOS9上需要将钉钉SDK相关的Scheme注册到Info.plist的LSApplicationQueriesSchemes名单中，否则会导致检测方法总是返回NO。

## **Android接入分享**

### **步骤一：接入钉钉分享**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/shareMan)，打开应用列表页，点击应用进入应用详情页。

   ![企业内部应用-移动端-分享打开应用 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386713.png)
2. 在应用信息页面，获取应用的AppKey。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p740486.png)
3. 在应用详情页，单击**分享设置**，进入登录与分享页面。

   ![移动应用接入-钉钉登录与分享 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p386717.png)
4. 在**接入分享**栏，开启**Android 分享**，然后依次填写**Android包名称**和**Android签名**，最后单击保存。

   > **[!NOTE]**
   >
   > 签名获取方式请参考[签名方法](https://open.dingtalk.com/document/orgapp/share-sdk-download)。

   ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p676009.png)

### **步骤二：搭建开发环境**

使用以下任意一种方式搭建开发环境。

- 方式一：Gradle依赖

  在模块的`build.gradle`的`dependencies`中添加`compile 'com.alibaba.android:ddsharesdk:1.1.0'`
- 方式二：jar包直接引入

  1. 新建一个名为DDShareDemo的Android工程，在工程中创建一个libs工程，将下载的jar包复制到该目录中，如下图所示：

     ![jar包](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1496077161/p260452.png)
  2. 将libs目录下的JAR包文件添加到工程依赖中。

### **步骤三：在代码中使用开发工具包**

如果您的程序需要接收钉钉发送的请求，或者接收发送到钉钉的请求的响应结果，需要执行以下操作：

1. 在您的包名相应目录下新建一个`ddshare`。

   ![DDShareActivity](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1496077161/p260647.png)

   然后在`AndroidManifest`文件中添加**exported**属性，设置为**true。**

   ![添加属性](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1216368061/p204486.png)
2. 实现**IDDAPIEventHandler**接口，钉钉的响应结果将回调到onResp方法中。

   onResp方法示例代码如下：

   ```
   public void onResp(BaseResp baseResp) {
       int errCode = baseResp.mErrCode;
       Log.d("lzc" , "errorCode==========>"+errCode);
       String errMsg = baseResp.mErrStr;
       Log.d("lzc" , "errMsg==========>"+errMsg);
       if(baseResp.getType() == ShareConstant.COMMAND_SENDAUTH_V2 && (baseResp instanceof SendAuth.Resp)){
           SendAuth.Resp authResp = (SendAuth.Resp) baseResp;
           switch (errCode){
               case BaseResp.ErrCode.ERR_OK:
                   Toast.makeText(this, "授权成功，授权码为:"+authResp.code, Toast.LENGTH_SHORT).show();
                   break;
               case BaseResp.ErrCode.ERR_USER_CANCEL:
                   Toast.makeText(this, "授权取消", Toast.LENGTH_SHORT).show();
                   break;
               default:
                   Toast.makeText(this, "授权异常"+baseResp.mErrStr, Toast.LENGTH_SHORT).show();
                   break;
           }
       }else{
           switch (errCode){
               case BaseResp.ErrCode.ERR_OK:
                   Toast.makeText(this, "分享成功", Toast.LENGTH_SHORT).show();
                   break;
               case BaseResp.ErrCode.ERR_USER_CANCEL:
                   Toast.makeText(this, "分享取消", Toast.LENGTH_SHORT).show();
                   break;
               default:
                   Toast.makeText(this, "分享失败"+baseResp.mErrStr, Toast.LENGTH_SHORT).show();
                   break;
           }
       }
       finish();
   }
   ```
3. 在**DDShareActivity**类中，将接收到的intent和实现了**IDDAPIEventHandler**接口的对象传递给**IDDShareApi**接口的handleIntent方法。然后应用请求钉钉的响应结果，钉钉将会通过调用onResp方法的形式返回。

   ```
   private IDDShareApi mIDDShareApi;

   @Override
   protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       Log.d("lzc" ,"onCreate==========>");
       try {
           //activity的export为true，try起来，防止第三方拒绝服务攻击。APP_ID指通过步骤一获取的应用的AppKey
           mIDDShareApi = DDShareApiFactory.createDDShareApi(this, Constant.APP_ID, false);
           mIDDShareApi.handleIntent(getIntent(), this);
       } catch (Exception e) {
           e.printStackTrace();
           Log.d("lzc" , "e===========>"+e.toString());
       }
   }
   ```
4. 判断当前设备是否支持分享。

   - 判断当前设备是否已经安装钉钉。

     ```
     findViewById(R.id.ding_install_check).setOnClickListener(new View.OnClickListener() {
         @Override
         public void onClick(View view) {
             boolean isInstalled = iddShareApi.isDDAppInstalled();
             Toast.makeText(MainActivity.this, "是否安装===》" + isInstalled, Toast.LENGTH_SHORT).show();
         }
     });
     ```
   - 判断当前设备是否支持分享到钉钉（已经安装钉钉并且钉钉版本支持分享）。

     ```
     findViewById(R.id.share_support_check).setOnClickListener(new View.OnClickListener() {
         @Override
         public void onClick(View view) {
             boolean isSupport = iddShareApi.isDDSupportAPI();
             Toast.makeText(MainActivity.this ,"是否支持分享到好友===》"+isSupport ,Toast.LENGTH_SHORT ).show();
         }
     });
     ```
5. 支持的分享类型。

   支持文本、图片、链接以及特殊的支付宝红包类型。具体使用请参考已下载的**Android SDK**示例。

## **鸿蒙接入分享**

### **步骤一：接入钉钉分享**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/shareMan)，找到自己的创建的应用，单击应用进入应用详情页。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p878409.png)
2. 在应用信息页面，获取应用的 **Client ID**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p878410.png)
3. 在应用详情页，单击**分享设置**，进入登录与分享页面。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p878411.png)
4. 在**接入分享**栏，单击右侧**编辑**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p878412.png)
5. 单击开启 鸿蒙 **分享**，然后依次填写鸿蒙应用 **Bundle Name**和 **Identifier**，最后单击保存。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5128872871/p878414.png)

   注意：**Identifier** 为 鸿蒙应用唯一标识 **appIdentifier** 而不是 appId，详情见官方文档：[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V14/js-apis-bundlemanager-bundleinfo-V14)

### **步骤二：搭建开发环境**

使用以下任意一种方式搭建开发环境。

方式一：使用demo中的har包直接安装

参考：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ide-ohpm-install-V5>。

方式二：通过三方库引入

上架三方工具库，通过ohpm -i安装。目前鸿蒙SDK暂未上架三方工具库，敬请期待。

### **步骤三：在代码中使用开发工具包**

如果您的程序需要接收钉钉发送的请求，或者接收发送到钉钉的请求的响应结果，需要执行以下操作：

1. 获取分享API

```
import { BaseResp, IDDAPIEventHandler, BaseReq, SendMessageToDD, ErrCode, DDShareApi } from "@dingtalk/ddsharesdk"
import { promptAction } from '@kit.ArkUI';

export class DDApiEventHandlerImpl implements IDDAPIEventHandler {

  onReq(req: BaseReq): void {
    console.log("DDTag 来自钉钉的请求");
  }

  onResp(resp: BaseResp): void {
    let errCode = resp.mErrCode;
    if (resp instanceof SendMessageToDD.Resp) {
      switch (errCode) {
        case ErrCode.ERR_OK:
          promptAction.showToast({
            message: "分享成功",
            duration: 2000
          })
        break;
        case ErrCode.ERR_USER_CANCEL:
          promptAction.showToast({
            message: "分享取消",
            duration: 2000
          })
          break;
        default :
          promptAction.showToast({
            message: "分享失败",
            duration: 2000
          })
          break;
      }
    }
  }
}

/**
 * 在钉钉开放平台申请的应用Client ID
 * 替换为自己的
 */
export const APP_ID: string = "123456"; // 为前面申请的Client ID
export const DDApi = DDShareApi.getInstance(APP_ID);
export const DDEventHandle = new DDApiEventHandlerImpl();
```

// 在EntryAbility 或应用自身的Ability 中响应来自钉钉的回调：

```
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.handleDingTalkCallIfNeed(want);
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.handleDingTalkCallIfNeed(want);
  }

  private  handleDingTalkCallIfNeed(want: Want) {
    DDApi.handleWant(want, DDEventHandle);
  }
}
```

2. 支持图片/文字/链接 等，具体使用请参考已下载的**Harmony dingtalk\_share\_demo**示例：

   [dingtalk\_share\_demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251031/grvroo/dingtalk_share_demo.zip)

### **鸿蒙应用开发手册**

- 在代码中接入SDK后，可调用接口实现钉钉分享功能
- 当前支持图片/文字/链接等分享到钉钉会话

#### **DDMediaMessage（钉钉媒体消息）**

| 字段 | 类型 | 含义 | 备注 |
| --- | --- | --- | --- |
| mMediaMessageObject | IMediaObject | 消息对象 | 描述媒体对象 |
| mTitle | string | 消息标题 |  |
| mThumbData | Uint8Array | 缩略图数据 | // 暂不支持解析 |
| mThumbUrl | string | 缩略图链接 |  |
| mUrl | string | 消息链接 |  |
| mContent | string | 消息内容 |  |

#### **SendMessageToDD.Req（发送请求）**

| 字段 | 类型 | 含义 | 备注 |
| --- | --- | --- | --- |
| mMediaMessage | DDMediaMessage | 媒体对象 |  |
| mScene | number | 场景 |  |

#### **示例**

一、文本分享类型

| 字段 | 类型 | 含义 | 备注 |
| --- | --- | --- | --- |
| mText | string | 文本数据 | 不允许超过6k |

文本类型分享demo

```
  let req: SendMessageToDD.Req | undefined = undefined;

  if (this.shareText) {
  let text: string = this.textContent;
  /** 构造text消息*/
  let textMessage: DDTextMessage = new DDTextMessage();
  textMessage.mText = text;

  let mediaMessage = new DDMediaMessage();
  mediaMessage.mMediaMessageObject = textMessage;

  req = new SendMessageToDD.Req();
  req.mMediaMessage = mediaMessage;

   // 返回需要打开的 Ability，不传的时候默认为 EntryAbility
   if (req) {
     req.callbackAbility = "";
   }
  if(this.mDDShareAPI != null) {
    this.mDDShareAPI.sendReq(req);
  }
```

二、图片类型分享示例

| 字段 | 类型 | 含义 | 备注 |
| --- | --- | --- | --- |
| mImageUri | string | 本地图片链接Uri |  |

图片类型分享demo

```
    let req: SendMessageToDD.Req | undefined = undefined;
    /**
     * 构造Image消息
     * 注意：目前仅支持Uri
     */
    let imageMessage = new DDImageMessage();
    imageMessage.mImageUri = fileUri.getUriFromPath(Utils.getImageCacheFile(getContext()) + "/aaa.png");

    let mediaMessage = new DDMediaMessage();
    mediaMessage.mMediaMessageObject = imageMessage;

    req = new SendMessageToDD.Req();
    req.mMediaMessage = mediaMessage;

    // 返回需要打开的 Ability，不传的时候默认为 EntryAbility
    if (req) {
      req.callbackAbility = "";
    }
    if(this.mDDShareAPI != null) {
      this.mDDShareAPI.sendReq(req);
    }
```

三、链接类型分享示例

| 字段 | 类型 | 含义 | 备注 |
| --- | --- | --- | --- |
| mUrl | string | web链接 |  |

Web链接类型分享demo

```
    let req: SendMessageToDD.Req | undefined = undefined;
    let webpMessageObject = new DDWebPageMessage();
    webpMessageObject.mUrl = "http://www.baidu.com";

    let webpMessage = new DDMediaMessage();
    webpMessage.mMediaMessageObject = webpMessageObject;
    webpMessage.mTitle = "TestTitle";
    webpMessage.mThumbUrl = "http://static.dingtalk.com/media/lAHPBY0V4shLSVDMlszw_240_150.gif";

    req = new SendMessageToDD.Req();
    req.mMediaMessage = webpMessage;

    // 返回需要打开的 Ability，不传的时候默认为 EntryAbility
    if (req) {
      req.callbackAbility = "";
    }
    if(this.mDDShareAPI != null) {
      this.mDDShareAPI.sendReq(req);
    }
```

支持拉起专属钉：

```
// 需要拉起目标的bundleName，默认为标准钉
req.targetAppBundleName = "**";
```
