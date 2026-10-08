---
title: "应用内授权开通接入"
source_url: "https://open.dingtalk.com/document/development/in-app-authorization-to-open-access"
namespace: "development"
slug: "in-app-authorization-to-open-access"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "应用市场 > 接入内容 > 应用内授权开通接入"
doc_id: "u9oXrnxp6O"
updated_at: "2026-07-14 09:22:25"
---

> Source: https://open.dingtalk.com/document/development/in-app-authorization-to-open-access
> Path: 应用开发 / 服务端 API / 应用市场 > 接入内容 > 应用内授权开通接入
> Updated: 2026-07-14 09:22:25

# 应用内授权开通接入

## 什么是应用内授权

钉钉会根据一定的推荐逻辑推荐应用，用户首次进入的时候，默认拉起授权弹窗，用户点击取消，授权弹窗关闭，依然停留在示例页面中，点击示例页面再次拉起授权弹窗；点击开始试用，正式进入应用。

- **移动端授权界面**

  ![应用授权-概述-图2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5412993871/p374072.png)
- **PC端授权界面**

  ![应用内授权-PC端-产品交互图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5412993871/p372978.png)

## **移动端应用内授权**

### **授权流程**

用户应用内授权体验流程，如下图所示。

![应用内授权开通-图2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3555700461/p372155.png)

### **接入方式**

#### **H5微应用接入**

监听SDK返回的内容，如果action值是ok时，需要开发者将当前页面重定向到正式应用的地址。

> **[!IMPORTANT]**
>
> 开通了应用的组织的corpId可能和url带入的corpId不同。如果支持免费规格的应用，个人体验应用时，钉钉会用一个隐藏组织让个人体验，因此开通应用的组织可能是钉钉的一个隐藏组织，所以**开通应用的组织的corpId，以SDK返回的corpId为准**（不管是组织开通还是个人开通，如果action是ok的话，SDK都是会返回当前开通应用的组织的corpId）。

在H5微应用内，如果开通成功后，要实现内部页面跳转，请不要直接使用`window.location.href`进行跳转，建议使用如下方式。

```
import openLink from 'dingtalk-jsapi/api/biz/util/openLink';
import close from 'dingtalk-jsapi/api/biz/navigation/close';

openLink({ url: 'xxx' }).then(() => close({}));
```

> **[!IMPORTANT]**
>
> 由于安卓端存在一些问题，以下方式跳转会出错，请不要使用以下方式：
>
> ```
> window.location.href = "xxx";
> ```

**【已接入应用改动点】**

- 升级sdk版本，在action是ok的情况下，用sdk返回的corpId重定向到正式应用的地址，关闭H5示例页。action是cancel或unknown的情况下，停留在H5示例页面。
- 删除之前服务端的从钉钉获取可见范围的相关逻辑，并且在营销页面也不需要再和服务端进行交互

#### **小程序接入**

小程序需要准备一个展示应用首页内容的H5展示页面，在H5展示页上调用SDK调起开通弹窗。

> **[!NOTE]**
>
> 此H5展示页是一个能在线上访问到的非小程序技术栈开发的页面，不是指H5微应用，不需要在钉钉上单独创建H5微应用。

小程序应用，用户在SDK上点击开通后，SDK会自动打开小程序，因此不需要开发者处理重定向。开发者只需要监听SDK返回的action，如果是ok，表示用户已经进入过小程序使用了，并关闭了小程序回到了H5展示页，此时直接关闭H5展示页即可。

**【已接入应用改动点】**

升级sdk版本，并在action是ok的情况下，关闭H5示例页。

#### **接入代码示例**（H5和小程序都适用）

代码示例如下：

> **[!IMPORTANT]**
>
> **dingtalk-design-libs**需要依赖npm包**dingtalk-jsap**，因此需要确保应用已经引入了**dingtalk-jsapi**这个npm包。

```
// 用下面这句import，同时兼容PC和移动端
import { openTryoutSku } from 'dingtalk-design-libs@0.0.14-alpha.3';

// 自行判断调用这个方法的时机
openTryoutSku({
  // corpId可以从应用首页的url上获取到
  corpId: '',
  // 应用的appId
  appId: '',
  // 从应用首页的url上获取到，url上参数名为 purchaseToken。
  // purchaseToken如何配置参考下文 配置入口地址。
  token: '',
  miniAppId: '', // 如果是三方小程序应用，需要设置一下自身的miniAppId。H5微应用可以不设置这个参数
}).then((res) => {
  const {
    // action的值为：
    // 'ok'，用户执行了开通动作，或将自己加入了已开通的应用的可见范围内
    // 'cancel', 用户点击了取消按钮
    // 'unknown'，用户点击空白区域关闭了弹窗，此时可以跟cancel采取同样的处理逻辑
    action,
    // 开通了应用的组织的corpId。因为个人开通可能会用钉钉的隐藏组织，所以开通应用的组织的corpId以这里返回的为准。
    corpId,
  } = res;
  // action不是ok的情况下，可以不采取任何动作
}).catch(() => {
  // 钉钉侧出现了技术异常，比如打开弹窗失败等，出现概率非常低
});
```

> **[!NOTE]**
>
> 本地测试时purchaseToken可以不传。

### **自测**

可以通过钉钉开放平台提供的[内网穿透工具](https://open.dingtalk.com/document/resourcedownload/http-intranet-penetration)，将内部正在开发的地址映射为线上能被访问到的地址，然后将该地址在钉钉聊天窗里发送给自己，就能在手机钉钉上测试本地地址了。

- **H5微应用**

  自行拼接链接进入应用内页面测试流程。链接格式如下：

  ```
  https://xxxx?
  corpId=xxx
  &appId=xxx
  &appEntityType=APP
  &purchaseToken=$PURCHASE_TOKEN$
  &xxx=xxx
  ```

  其中corpId和appId的大小写方式自行决定，只需在调用的前端接口中带上对应参数值即可。自测不用带purchaseToken=$PURCHASE\_TOKEN。

  > **[!NOTE]**
  >
  > 用户授权后，会看到的工作台地址和商品详情页上的应用地址，将会被替换成真正的三方小程序地址。授权的用户不会再进入H5展示页。
- **小程序**

  小程序自测直接用H5展示页进行测试即可。

  **测试流程为：**

  1. 在H5展示页用SDK调起试用弹窗。
  2. 点击取消后回到H5展示页，H5展示页接收到**resume事件**后关闭。
  3. 点击授权后，SDK会自动进入三方小程序，关闭三方小程序后回到H5展示页，H5展示页接收到**resume事件**后关闭。
  > **[!NOTE]**
  >
  > 用户授权后，他看到的工作台地址和商品详情页上的应用地址，将会被替换成真正的三方小程序地址。授权的用户不会再进入H5展示页。

  特别注意：完成授权之后，从应用内返回，用户看不到示例页面或示例页面自动关闭，不要停留在示例页面。

### **常见问题**

在接入过程中可能会遇到如下问题。

- **Q：如果SDK弹窗没有出现怎么办？**

  A：此问题可通过以下两种方式解决：

  - 一、如果发现SDK弹窗没有出现，可以检查一下是否在代码中没有引入以下文件。

    > **[!NOTE]**
    >
    > - npm方式引入jsapi需要引入以下文件，否则一些基础的jsapi，如openLink会失效。
    > - 此文件为jsapi的初始化文件，在项目中引入依次即可。

    ```
    import 'dingtalk-jsapi/entry/union';
    ```
  - 二、如果发现引入文件后，依然没有SDK弹窗，并且`openTryoutSku(...).catch`抛出的错误信息是`openLink failed`。那么尝试删除node\_modules，重新install一下，再构建一次。
- **Q：没有进入then链路**

  A：如果发现SDK能打开弹窗，但点击弹窗中的”取消“按钮后，没有进入openTryoutSku(...).then的链路里的话，请在 dd.ready 里调用SDK，因为SDK依赖页面的resume事件，而resume事件要注册成功必须在dd.ready后，没有进入then可能是resume事件没有注册成功。

## **PC端应用内授权**

### **接入代码示例**

> **[!NOTE]**
>
> - **dingtalk-design-libs**需要依赖**npm**包**dingtalk-jsapi**。因此需要确保应用是引入了**dingtalk-jsapi**这个**npm**包。
> - 本地测试时purchaseToken可以不传。

```
// 同时兼容PC和移动端的情况
import { openTryoutSku } from 'dingtalk-design-libs';

// 开发者自行判断调用这个方法的时机
openTryoutSku({
  // corpId可以从应用首页的url上获取到
  corpId: '',
  // 应用的appId
  appId: '',
 // 从应用首页的url上获取到，url上参数名为 purchaseToken。
  // purchaseToken如何配置参照下文”配置入口地址“章节。
 token: '',
 miniAppId: '', // 如果是三方小程序应用，需要设置一下自身的miniAppId。H5微应用可以不设置这个参数
}).then((res) => {
  const {
    // action的值为：
  // 'ok'，用户执行了开通动作，或将自己加入了已开通的应用的可见范围内
    // 'cancel', 用户点击了取消按钮
    // 'unknown'，用户点击空白区域关闭了弹窗，此时可以跟cancel采取同样的处理逻辑
    action,
  // 开通了应用的组织的corpId。因为个人开通可能会用钉钉的隐藏组织，所以开通应用的组织的corpId以这里返回的为准。
  corpId,
  } = res;
 // action不是ok的情况下，可以不采取任何动作
}).catch(() => {
  // 钉钉侧出现了技术异常，比如打开弹窗失败等，出现概率非常低
});
```

### **接入方式**

- 监听SDK返回的内容，如果action值是ok时，需要开发者将当前页面重定向到正式应用的地址。

  > **[!IMPORTANT]**
  >
  > 开通了应用的组织的corpId可能和url带入的corpId不同。如果支持免费规格的应用，个人体验应用时，钉钉会用一个隐藏组织让个人体验，因此开通应用的组织可能是钉钉的一个隐藏组织，所以**开通应用的组织的corpId，以SDK返回的corpId为准**（不管是组织开通还是个人开通，如果action是ok的话，SDK都是会返回当前开通应用的组织的corpId）。

### **自测**

pc如何在工作台打开测试页面：

使用url：

```
dingtalk://dingtalkclient/page/link?url=${encodeURIComponent(测试页面地址+ddtab=true参数)}
```

例如：

```
dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fabc.com%2Ftest.html%3FcorpId%3Ddingf0f110ce4fd10fb7ee0f45d8e4f7c288%26ddtab%
```

## **配置入口页面地址**

参考以下步骤配置应用内未授权背景页面地址。

1. 登录开发者后台，进入"应用运营"-"商品上架管理"-体验授权-应用内授权设置。
2. 选择移动端/PC端的设置授权背景页面，点击后进行配置。

   ![应用内授权-配置页面入口1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7373700461/p372219.png)![应用内授权-PC端-图3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7373700461/p372221.png)

   > **[!IMPORTANT]**
   >
   > - 地址中两个参数一定加上：purchaseToken=$PURCHASE\_TOKEN$；corpId=$CORPID$；$CORPID$，$PURCHASE\_TOKEN$占位符会在正式上线后，在钉钉容器内自动替换为真正的值。
   > - 不要修改应用真正的首页地址。

## **验收**

### **验收前设置自测组织**

参考以下步骤：

1. 登录开发者后台，进入"应用运营"-"商品上架管理"-其他设置-应用内授权设置。
2. 选择移动端/PC端的设置自测组织，点击后进行配置。

   ![应用内授权-验收1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2763700461/p372228.png)

> **[!NOTE]**
>
> - 测试组织的名称需要以“测试”字样结尾。
> - 每次报备1个组织，如果该测试组织使用完无法再测试，可在提交审核前再保存一个，同时之前报备的将失效。

### **提交验收审核**

参考以下步骤：

1. 登录[开发者后台](http://open-dev.dingtalk.com/)，进入"应用运营"-"商品上架管理"-其他设置-应用内授权设置。
2. 如果没有设置测试组织和设置授权背景页面请先设置，设置完成的状态为“待送审”状态。
3. 点击选择移动端/PC端中的提交审核，上传自测视频。

   > **[!NOTE]**
   >
   > 可上传多个文件，视频文件建议不要太大。
4. 提交审核后，状态会变为“审核中”，等待审核人员审核。

   - 如果审核拒绝，状态会展示变为“审核拒绝”并会给出拒绝原因，修复完成之后可再次提交验收审核。
   - 如果审核通过，功能会自动全量上线，正式发布到到线上。可以在广场详情页和工作台推荐查看。

     ![应用内授权-验收-图4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2763700461/p372234.png)

### **验收视频材料用例**

1. 确保配置入口页面地址已经完成配置。
2. 在授权弹窗中，点击取消之后，再次点击应用的页面可再次唤起授权页面。
3. 点击开始试用后，可直接打开应用（不需要用户再次点击），从应用返回或关闭应用，示例页面会自动消失，不用用户手动关闭，这一条一定注意，出现后将拒绝通过。
4. 在工作台-XX分组（试用时安装的分组），可看到刚才试用的应用，点击应用，直接打开应用，不用再授权。

### **验收注意问题**

- **在示例页面前不用启动页面，应该直接进入到示例页面。**

  如下图所示，不需要启动页面，应该直接进入到示例页面。

  ![示例页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5862709161/p267150.png)
- **在示例页面中，不要出现两个底部栏。**

  ![不要有2个底部栏](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5862709161/p267156.png)
- 用户授权之后要直接进入到应用内，从应用中返回时，示例页面要自动关闭，不需要用户手动再关闭。
- 出现以下情况是没有接入个人版，先按照个人版的接入方案接入，接入完成后就不会出现这种情况。

  ![应用内授权-验收-图6](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2763700461/p372596.png)
