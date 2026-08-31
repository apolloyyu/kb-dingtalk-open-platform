---
title: "第三方个人应用学习指南"
source_url: "https://open.dingtalk.com/document/dingstart/create-and-configure-an-application"
namespace: "dingstart"
slug: "create-and-configure-an-application"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 第三方个人应用学习指南"
doc_id: "kGas2HJ38X"
updated_at: "2026-07-22 16:55:13"
---

> Source: https://open.dingtalk.com/document/dingstart/create-and-configure-an-application
> Path: 应用开发 / 开发指南 / 开发指南 > 第三方个人应用学习指南
> Updated: 2026-07-22 16:55:13

# 第三方个人应用学习指南

## **准备工作**

在正式开发前，你可以先了解开发基本知识，方便快速开始。

- 已经了解了钉钉开放平台的基础概念，详细内容参见[基础概念](0001-basic-concepts-beta.md)。
- 已经了解了钉钉开放平台的应用类型，详细内容参见[应用类型与能力说明](0002-application-type-introduction.md)。
- 如果在开发过程中遇到问题，可参见[技术支持](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)提供工单。
- 在正式开始前，你需要[获取开发者权限](0006-get-developer-permissions.md)，成为钉钉开发者。

## 创建和配置应用

### **创建应用**

创建应用后，可以获取到应用的基础凭证信息，设置开发人员和接口权限等。

参考以下操作，创建一个第三方个人小程序应用

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。

   > **[!NOTE]**
   >
   > 只有管理员和子管理员可登录开发者后台。
2. 在**应用开发**页面，选择**第三方个人应用**，然后单击**创建应用**。

   ![创建应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121872871/p345313.png)
3. 填写应用的基本信息，然后单击**确定创建**。

   ![填写应用信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7170045361/p345314.png)
4. 单击**凭证与基础信息**获取应用的AppId和AppSecret。

   ![应用拼争](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121872871/p345315.png)

### **人员管理**

在**人员管理**页面添加开发和体验人员。

- 在创建小程序后，默认会将当前小程序的创建者添加为开发人员。如果应用有多个开发者，管理员可以通过手机号码添加该应用的开发者。添加开发人员后，该开发人员可使用开发者工具进行应用开发。
- 添加为体验人员，才可以使用小程序的体验版本。

  ![p165967](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121872871/p256809.png)

### **监控中心**

在**监控中心**页面开启监控并设置稳定性负责人配置。

![p186671](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121872871/p256810.png)

### **安全中心**

在**安全中心**页面添加HTTP安全域名和webview安全域名。

- HTTP安全域名：

  开发者开发的小程序，若前端与服务端需要进行网络通信，需要事先设置一个或多个服务端安全域名（或IP），且小程序前端只能通过已设置的安全域名（或IP）与服务端进行网络通信。

  当安全域名更新时，需要在小程序开发工具重新打包上传版本，设置的域名才会生效。

  本质上，小程序前端与后端的网络通信是同普通的H5前后端一样的。因此在您做快速体验时，可以填写小程序前端所在环境能访问的任何域名/IP地址，比如可以是您自己的办公电脑本机地址或者局域网地址。
- webview安全域名：

  小程序使用webview组件内嵌H5页面时，需要将H5页面地址域名添加到webview安全域名中。

  ![p186576 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121872871/p256771.png)

## **免登接入**

通过钉钉开放平台提供的能力，用户在使用应用时可无需输入账号密码，快速完成身份验证。

### **适用对象与限制条件**

本功能适用于以下场景：

- 应用类型：**第三方个人应用**
- 运行环境：仅支持**小程序**
- 认证方式：基于临时授权码（authCode）的授权机制

### **流程说明**

#### **前端发起授权并获取 authCode**

用户进入E 小程序后，前端通过钉钉客户端提供的 JSAPI 发起授权请求，获取[getAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0006-jsapi-get-auth-code.md)（authCode），随后将该code传递给应用后端。该操作通常使用`dd.getAuthCode` 接口完成。

> **关键术语说明**：`authCode` 是通过钉钉客户端 JSAPI（如 `dd.getAuthCode`）获取的临时授权码，有效期短暂且仅能使用一次，用于后端换取用户基本信息。

#### **服务端调用接口获取用户信息**

应用后端接收到`authCode`后，调用钉钉服务端接口 `sns/getuserinfo_bycode`[获取用户基本信息](../02-4a8AMF6u2A-服务端-API/0052-queries-basic-user-information.md)，完成登录流程。

> **[!NOTE]**
>
> - 调用频率每分钟会有限制，请合理控制请求频次。
> - 建议对异常情况进行重试机制与日志记录。

### **示例代码**

#### **前端示例**

```
dd.getAuthCode({
  corpId: 'ding12345xxx',
  success: (res) => {
    const { authCode } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

#### **服务端示例**

接口调用成功后，返回用户信息包括 `nick`（昵称）、`openid`、`unionid` 等字段。

```
/**
 * Quick-Start示例代码
 * 实现了最简单的获取个人身份验证功能
 */
@RestController
public class IndexController {
    private static final Logger bizLogger = LoggerFactory.getLogger(IndexController.class);

    /**
     * 欢迎页面
     */
    @RequestMapping(value = "/welcome", method = RequestMethod.GET)
    public String welcome() {
        return "welcome";
    }

    /**
     * 钉钉用户登录，显示当前登录用户基本信息
     * @param authCode 由E应用前端JSAPI获取到的临时授权码
     */
    @RequestMapping(value = "/login", method = RequestMethod.POST)
    @ResponseBody
    public Object login(@RequestParam(value = "authCode") String authCode) {
        Long start = System.currentTimeMillis();
        ServiceResult serviceResult;
        try {
            DefaultDingTalkClient  client = new DefaultDingTalkClient(URL_GET_USERINFO_BY_CODE);
            OapiSnsGetuserinfoBycodeRequest req = new OapiSnsGetuserinfoBycodeRequest();
            req.setTmpAuthCode(authCode);
            OapiSnsGetuserinfoBycodeResponse response = client.execute(req,Constant.APP_ID,Constant.APP_SECRET);
            serviceResult = ServiceResult.success(response.getUserInfo());
            return serviceResult;
        } catch (Exception e) {
            bizLogger.error("loginFailed,authCode"+authCode,e);
            serviceResult = ServiceResult.failure("-1",e.getMessage());
            //返回结果
        }
        bizLogger.info("cost:"+(System.currentTimeMillis()-start));
        return serviceResult;
    }
}
```

### **缓存策略建议**

为提升用户体验并减少重复请求，建议对用户登录状态进行本地缓存管理：

- 使用 `dd.setStorage` 在客户端存储用户信息及时间戳。
- 下次进入页面时优先读取缓存。
- 推荐缓存有效期设置为 2 小时，避免长时间无效登录状态。

### **常见问题**

- **Q: authCode 获取失败有哪些常见原因？**

  A: 可能原因包括：未正确引入 dd-sdk-js、网络异常、未在钉钉客户端内打开等。
- **Q: 用户信息接口返回 errcode=40001？**

  A: 表示凭证无效，请检查填写的参数 是否正确，并确认authCode是否已过期。
- Q: **是否支持 PC 端免登？**

  A: 当前方案主要适用于移动端 小程序；PC 端建议结合扫码登录或其他认证方式。

## **发送消息**

开发者可通过消息高效触达用户，通知用户当前行为的结果及状态等。消息支持配置应用内跳转页面地址，当用户查看消息并点击“进入应用查看”时，将跳转至开发者指定的应用内页面。具体实现方式请参考本文档的开发流程。

在开始开发前，你需要：

- 在应用**基础信息 > 应用信息**中获取 **AppId** 和 **AppSecret**，用于后续接口调用鉴权。
- 确保客户端小程序已上线，并可在真机环境中运行表单提交操作。

### **限制说明**

- **适用应用类型**：第三方个人应用
- **formId 有效期**：formId 为临时授权码，有效期为7天，过期后不可用于发送消息。
- **推送次数规则**：每提交1次表单，在7天内您仅可以向用户推送1条消息，多次提交可以推送多条。

### **开发流程**

1. 开发者在用户提交的form表单上声明属性`report-submit="true"`。

   > **[!NOTE]**
   >
   > 该属性需要在真机环境下生效。

   ```
   <form onSubmit="formSubmit"  report-submit="true">
     <view class="section section_gap">
       <view class="section__title">表单类型</view>
       <input name="text" maxlength="10" placeholder="最大输入长度10" />
     </view>
     <view class="btn-area">
       <button formType="submit">推送消息</button>
     </view>
   </form>
   ```
2. 在 `onSubmit`事件中通过`e.detail.formId`获取推送消息所需的临时授权码（code），并将该 code 发送到开发者服务器进行存储。

   ```
   formSubmit(e){
     // 通过e.detail.formId可以获取到推送消息的临时授权码code
     dd.httpRequest({
       url: 'http://表单提交的服务端地址?code='+e.detail.formId,
       method: 'POST',
       headers:{"Content-Type":"application/json"},
       data: { 
       },
       dataType: 'json',
       success: function(res) {
         if(res.data.success){
           dd.alert({content:'form表单提交处理成功'});
         }else{
           dd.alert({title:"form表单提交处理失败",
                     content:JSON.stringify(res)});
         }                            
       },
       fail: function(res) {
         dd.alert({content: 'form表单提交处理'});
       }
     });
   }
   ```
3. 当业务需要向用户推送消息时，服务端调用钉钉提供的消息推送接口，使用之前获取的 code 向用户发送消息。

   ```
   public static String sendMsg() throws RuntimeException {
       try {
           DefaultDingTalkClient  client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/send_msg");
           OapiSnsSendMsgRequest req = new OapiSnsSendMsgRequest();
           req.setCode(code);
           OapiSnsSendMsgRequest.Eapp eapp = new OapiSnsSendMsgRequest.Eapp();
           eapp.setImg("@lALPBxxxxAs4");
           eapp.setContent("非常感谢您的反馈，非常感谢您的反馈。 \n\n"+System.currentTimeMillis());
           eapp.setTitle("工单已回复");
           eapp.setLink("eapp://page/index?param=aaa");
           OapiSnsSendMsgRequest.Msg msg = new OapiSnsSendMsgRequest.Msg();
           msg.setMsgtype("eapp");
           msg.setEapp(eapp);
           req.setMsg(msg);
           OapiSnsSendMsgResponse response = client.execute(req,Constant.APP_ID,Constant.APP_SECRET)
       } catch (ApiException e) {
           bizLogger.error("sendMsg failed", e);
           throw new RuntimeException();
       }

   }
   ```

## **发布应用**

应用开发完成后，可以定向邀请体验用户进行应用测试，完成应用体验测试后，可以提交应用审核，审核通过后即可发布应用。

### **体验版本**

为了方便开发者对已经开发的版本进行体验和测试，在开发者后台，无需产品上线审核，就可以将开发版本设置为体验版。设置成功后，体验人员即可扫码使用该版本。步骤如下：

1. 在人员设置中添加体验成员。
2. 在版本管理中，选择一个开发版本设置为体验版。

   ![p190670 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2059592871/p256779.png)
3. 让体验者扫体验二维码开始体验。

### **提交审核**

在产品正式上线前，需提交产品审核。应用首次发布上线，钉钉团队将会对产品进行审核。审核通过后，钉钉用户将可以在钉钉内打开并使用该应用。

提交审核前，建议先阅读[第三方个人应用发布规范](../07-TjCzIgfQs3-平台服务/0014-personalapp-commercial-release.md)，将会大大提升通过审核的概率。

![p190704 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2059592871/p256782.png)

### **灰度测试**

审核通过后，开发者可点击“灰度”进行版本灰度。新版本进入灰度测试阶段后，开发者可以提高灰度比例，灰度比例只能提高不能降低。如果在灰度阶段版本出现缺陷，开发者可以选择不发布该版本的应用。

### **版本发布**

灰度测试后，开发者点击**发布**，应用发布到线上，用户可以通过扫码或分享进入应用，且所有的钉钉用户均可使用该版本的应用。

> **[!NOTE]**
>
> 第三方个人应用产品发布前，应用归属的钉钉组织需满足以下条件：
>
> - 钉钉组织需完成高级认证。
> - 钉钉组织需完成产品方案商入驻。

1. 点击要发布的应用，点击**版本管理**，选择需要提交审核的版本。

   ![p190704 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2059592871/p256782.png)
2. 点击**提交审核**。

   > **[!NOTE]**
   >
   > 如果没有进行钉钉组织认证和服务商认证，会提示先进行认证。您可以按照开发者后台提示流程进行认证，也可以参考[合作全流程指引](../07-TjCzIgfQs3-平台服务/0027-isv-cooperation-guide.md)。
3. 在产品审核页面，依次进行安全扫描、产品审核等。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8842462061/p165987.png "image.png")

   1. 单击安全扫描下的**点击进入**，对提交应用进行安全扫描，并将展示安全扫描报告。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8842462061/p165988.png "image.png")
   2. 查看产品审核标准，可以查看第三方个人应用的产品设计规范，见[产品设计规范](../07-TjCzIgfQs3-平台服务/0015-product-design-specification.md)。
   3. 单击提交审核下的**点此进入**，提交审核。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8842462061/p165989.png "image.png")
