---
title: "配置SyncHTTP推送（推荐）"
source_url: "https://open.dingtalk.com/document/development/configure-synchttp-push"
namespace: "development"
slug: "configure-synchttp-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 配置数据推送 > 配置SyncHTTP推送（推荐）"
doc_id: "KLzHcAwbZz"
updated_at: "2026-01-22 20:17:43"
---

> Source: https://open.dingtalk.com/document/development/configure-synchttp-push
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 配置数据推送 > 配置SyncHTTP推送（推荐）
> Updated: 2026-01-22 20:17:43

# 配置SyncHTTP推送（推荐）

SyncHTTP推送方式适用于本地部署的情况。与HTTP推送方式比，SyncHTTP推送的是业务数据的最终状态，开发者可以直接使用推送的数据。

## **准备工作**

在开始配置 SyncHTTP 推送之前，请确保已完成以下前置条件：

1. **注册钉钉开发者账号**：访问 [钉钉开放平台](https://open.dingtalk.com/) 注册并登录开发者账户。
2. **创建第三方企业应用**：

   - 进入[开发者后台](https://open-dev.dingtalk.com/)，创建一个“第三方企业应用”。
   - 记录下生成的 `SuiteKey` 和 `SuiteSecret`，后续将用于调用接口和消息加解密。
3. **获取必要的凭证信息**：在应用详情页的「基础信息 > 凭证与基础信息」中查看或生成 `SuiteKey` 和 `SuiteSecret`。

## 回调说明

钉钉会向第三方企业应用推送其订阅的事件，包括但不限于：应用开通、授权变更、组织架构更新等。通过订阅这些事件，开发者可以更好地与钉钉集成。

> **[!IMPORTANT]**
>
> 第三方企业应用开发**必须**要注册回调，接收企业授权开通应用事件，用于通知三方应用哪个组织开通了本应用，第三方应用后台收到此事件后，需要初始化企业信息。

目前钉钉支持的事件推送方式包括

- RDS推送
- HTTP推送
- SyncHTTP推送

其中，**SyncHTTP 推送**以 HTTP 回调的形式，按照 RDS 推送的数据字段和格式，将数据推送到 ISV 的服务端。服务商可将HTTP接收的数据，按照RDS推送方式和类型保存到自建数据库或RDS中。

> **[!NOTE]**
>
> 使用 SyncHTTP 方式接收回调时，应立即完成数据落库操作并返回成功响应；如有其他复杂业务逻辑，建议采用异步任务处理，避免超时。

SyncHTTP不需要开发者手动调用激活应用接口，接到推送ticket后可用其直接调用服务端接口。

> **[!NOTE]**
>
> SyncHTTP推送和HTTP推送的出口IP为：
>
> - 203.119.0.0/16
> - 203.119.128.0/17
> - 140.205.0.0/16
> - 106.11.0.0/16
> - 198.11.0.0/16
> - 59.82.0.0/16

## 注册回调事件流程

首先，开发者需要在钉钉开放平台配置HTTP请求接收地址用于接收推送的订阅事件，然后设置要订阅的事件。在配置完请求地址后，钉钉开放平台会向该地址发送POST请求，只有在规定时间内正确返回了包含"**success**"的加密字符串才完成事件订阅。

回调事件订阅的流程，如下图所示：

![配置流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2578078061/p204984.png)

## 配置请求地址和订阅回调事件

通过SyncHTTP回调方式接收钉钉推送的回调事件，首先需要配置HTTP回调URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求。

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。找到已创建的应用，进入应用详情页。
2. 单击**开发管理**，然后单击**修改**，推送类型选择**SyncHTTP推送**。
3. 配置用于接收请求的HTTP地址。

   - **token**：钉钉每次向你的地址推送事件数据时都会携带`token`，用于生成签名、校验回调请求的合法性。必须为英文或数字，长度为3~32个字符。
   - **数据加密密钥**：单击**自动生成**生成AES密钥。回调消息内容的加解密参数，是AES密钥的Base64编码，具体使用参见本文档下方的[消息加解密](#section-vhz-t5l-4kf)。
   - **回调URL**：用于接收订阅事件请求的URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求。

     > **[!NOTE]**
     >
     > 每个应用只能配置一个回调URL，该应用订阅的所有事件通知都会发送到该请求网址。

     ![p256064](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9877607161/p256070.png)
4. 配置完成后，单击**验证有效性**按钮时，开放平台会向你配置的网址推送一个application/json格式的 POST请求, 用于验证你配置的网址的合法性。如下所示：

   ```
   {
       "encrypt":"HJ+q6tp1qhl9L1+++j74xxxx"   //加密字符串，参考下文的加解密说明
   }
   ```

   当你收到开放平台的POST验证请求时，你需要做解密处理，并在**1200ms**内返回包含**success**的加密字符串给钉钉，长时间未及时响应会被限流。
5. 成功配置请求地址后，在**回调事件**列表区域，勾选要订阅的回调事件，然后单击右上角**保存**。

   > **[!NOTE]**
   >
   > 如果某个回调事件无法勾选，在开发者后台的**权限管理**页面申请对应的接口权限。

   ![p204978](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9877607161/p256066.png)

## 推送数据说明

配置完回调URL后，单击**验证有效性**按钮时，开放平台会向你配置的网址推送一个application/json格式的 POST请求, 用于验证你配置的网址的合法性。

如下所示：

```
{
    "encrypt":"HJ+q6tp1qhl9L1+++j74xxxx"   //加密字符串，参考下文的加解密说明
}
```

你需要对收到的消息内容进行解密，详情请参考本文档下方的[消息加解密](#section-vhz-t5l-4kf)。解密后的事件类型如下：

- check\_url：测试回调事件。

  解密后数据：

  ```
  {
      "EventType" : "check_url"
  }
  ```
- check\_create\_suite\_url：验证回调事件。

  解密后数据：

  ```
  {
    "EventType":"check_create_suite_url",
    "Random":"brdkKLMW"
  }
  ```
- check\_update\_suite\_url：回调地址更新事件。

  解密后数据：

  ```
  {
    "EventType":"check_update_suite_url",
    "Random":"xxxxxx",
    "TestSuiteKey":"suited6db0pze8yao1b1y"
  }
  ```
- SYNC\_HTTP\_PUSH\_HIGH：高优先级数据，激活应用等。

  ```
  {
   "EventType": "SYNC_HTTP_PUSH_HIGH",
   "bizData": [{
    "gmt_create": 1608639648000,
    "biz_type": 4,
    "open_cursor": 0,
    "subscribe_id": "14999999001_0",
    "id": 7001,
    "gmt_modified": 1608639648000,
    "biz_id": "1489999001",
    "biz_data": "{\"auth_user_info\":{\"userId\":\"manager4xxx\"},\"auth_corp_info\":{\"corp_type\":0,\"corpid\":\"dingffea2a0dcc37d0xxxxxxx25e91351\",\"auth_level\":0,\"auth_channel\":\"\",\"industry\":\"\",\"full_corp_name\":\"xx测试组织\",\"corp_name\":\"xx测试组织\",\"invite_url\":\"https://pre-wx.dingtalk.com/xxxxx/index.html?bizSource=____source____&corpId=dingffea2a0dcc3xxxxx25e91351&inviterUid=71E7E5B48C2DDB2xxxxxxF52346D\",\"auth_channel_type\":\"\",\"invite_code\":\"\",\"is_authenticated\":false,\"license_code\":\"\",\"corp_logo_url\":\"\"},\"syncAction\":\"org_suite_auth\",\"auth_scope\":{\"errcode\":0,\"condition_field\":[],\"auth_user_field\":[\"jobnumber\",\"isLeader\",\"name\",\"position\",\"isAdmin\",\"avatar\",\"department\",\"userid\",\"deviceId\",\"isHide\"],\"auth_org_scopes\":{\"authed_user\":[],\"authed_dept\":[1]},\"errmsg\":\"ok\"},\"auth_info\":{\"agent\":[{\"agentid\":1038226450,\"agent_name\":\"土壕推送测试1217\",\"logo_url\":\"https://static-legacy.dingtalk.com/media/lADPDfmVQafoVxxxxxx0_200.jpg\",\"appid\":62282,\"admin_list\":[\"manager492\"]}]},\"permanent_code\":\"MFcbac-7zg0Mhcl-_dGmY2_f4NZPzLUf813xxxxxrjyEoGmKjqZwfi-5mh\"}",
    "corp_id": "dingffea2axxxxxx0dcb25e91351",
    "status": 0
   }]
  }
  ```
- SYNC\_HTTP\_PUSH\_MEDIUM：普通优先级数据，例如通讯录变更 。

  ```
  {
   "EventType": "SYNC_HTTP_PUSH_MEDIUM",
   "bizData": [{
    "gmt_create": 1608639751000,
    "biz_type": 14,
    "open_cursor": 0,
    "subscribe_id": "14778001_0",
    "id": 68,
    "gmt_modified": 1608639751000,
    "biz_id": "433877002",
    "biz_data": "{\"errcode\":0,\"userPermits\":\"\",\"userPerimits\":\"\",\"syncAction\":\"org_dept_create\",\"outerDept\":false,\"errmsg\":\"ok\",\"deptManagerUseridList\":\"\",\"parentid\":1,\"groupContainSubDept\":false,\"outerPermitUsers\":\"\",\"outerPermitDepts\":\"\",\"deptPerimits\":\"\",\"createDeptGroup\":true,\"name\":\"f'f'f\",\"id\":433885002,\"autoAddUser\":true,\"deptHiding\":false,\"deptPermits\":\"\",\"order\":43388775002}",
    "corp_id": "ding7629a25dxxxxxxxxf7214b6d69",
    "status": 0
   }]
  }
  ```

SYNC\_HTTP\_PUSH\_HIGH和SYNC\_HTTP\_PUSH\_MEDIUM类型的bizData数据就是RDS推送中的open\_sync\_biz\_data和open\_sync\_biz\_data\_medium表中的数据，具体格式请参[数据格式](https://open.dingtalk.com/document/isvapp/data-formats)。

## 接收并响应回调事件

启动一个HTTP服务（如下所示），在服务响应逻辑中解密后存储回调（推送）数据。

完整代码示例：<https://github.com/opendingtalk/eapp-isv-quick-start-java/blob/master/src/main/java/com/controller/CallbackController.java>

```
package com.controller;
import com.dingtalk.oapi.lib.aes.DingTalkEncryptor;
import org.springframework.web.bind.annotation.*;

/**
 * ISV 小程序回调信息处理
 */
@RestController
@RequestMapping("/")
public class CallbackController {

    private final Logger log = LoggerFactory.getLogger(getClass());

    @PostMapping(value = "dingCallback")
    public Object dingCallback(
            @RequestParam(value = "signature") String signature,
            @RequestParam(value = "timestamp") Long timestamp,
            @RequestParam(value = "nonce") String nonce,
            @RequestBody(required = false) JSONObject body
    ) {
        String[] config = CommonUtil.readConfig();
        String params = "signature:" + signature + " timestamp:" + timestamp + " nonce:" + nonce + " body:" + body;
        DingTalkEncryptor dingTalkEncryptor = new DingTalkEncryptor(config[CommonUtil.TOKEN], config[CommonUtil.ENCODING_AES_KEY], config[CommonUtil.SUITE_KEY]);

        // 从post请求的body中获取回调信息的加密数据进行解密处理，消息加解密参见下文
        String encrypt = body.getString("encrypt");
        String plainText = dingTalkEncryptor.getDecryptMsg(signature, timestamp.toString(), nonce, encrypt);
        JSONObject callBackContent = JSON.parseObject(plainText);

        // 根据回调事件类型做不同的业务处理
        String eventType = callBackContent.getString("EventType");
        //TODO 将数据持久化
        return plainText;
    }
}
```

## 消息加解密

为了保证数据传输的安全，钉钉在向回调URL推送订阅的回调事件时，会携带配置的token用来验证事件来源。同时使用该密钥对消息内容做对称加密。

单击[这里](https://github.com/open-dingtalk/dingtalk-callback-Crypto)获取回调加解密类库和对应demo。

### **加密流程说明**

钉钉服务器将明文消息 `msg` 进行如下加密处理：

`encrypt = Base64_Encode(AES_Encrypt[random(16B) + msg_len(4B) + msg + $key])`

其中：

- `random`：16 字节随机字符串；
- `msg_len`：4 字节的消息长度（网络字节序）；
- `msg`：原始消息明文；
- `$key`：应用的`suiteKey`。

### **解密流程**

1. 从 JSON 请求体中取出 `encrypt` 字段；
2. 对其进行 Base64 解码：`aes_msg = Base64_Decode(encrypt)`；
3. 使用 AES 密钥进行解密：`rand_msg = AES_Decrypt(aes_msg)`；
4. 去除前 16 字节随机串和 4 字节长度字段，得到原始 `msg` 明文。

### **示例代码**

完整示例请参见[钉钉第三方企业应用-小程序-快速开始Java版](https://github.com/opendingtalk/eapp-isv-quick-start-java/blob/master/src/main/java/com/controller/CallbackController.java)

### **工具类依赖说明**

上述加解密过程依赖于官方提供的`DingTalkEncryptor`工具类。你可以从以下仓库获取完整的加解密库和示例代码：参见[dingtalk-callback-Crypto](https://github.com/open-dingtalk/dingtalk-callback-Crypto)。

示例代码片段如下：

```
public Map<String, String> callBack(HttpServletRequest request,
                                    @RequestParam(value = "msg_signature", required = false) String msg_signature,
                                    @RequestParam(value = "timestamp", required = false) String timeStamp,
                                    @RequestParam(value = "nonce", required = false) String nonce,
                                    @RequestBody(required = false) JSONObject json) {
    try {
        // 1. 从http请求中获取加解密参数

        // 2. 使用加解密类型
        // Constant.OWNER_KEY 说明：
        // 1、开发者后台配置的订阅事件为应用级事件推送，
        //      此时OWNER_KEY为应用的APP_KEY（企业内部应用）或SUITE_KEY（三方应用）。
        // 2、调用订阅事件接口订阅的事件为企业级事件推送，
        //      此时OWNER_KEY为：企业的CORP_ID（企业内部应用）或SUITE_KEY（三方应用）
        DingCallbackCrypto callbackCrypto = new DingCallbackCrypto(Constant.AES_TOKEN, Constant.AES_KEY, Constant.OWNER_KEY);
        String encryptMsg = json.getString("encrypt");
        String decryptMsg = callbackCrypto.getDecryptMsg(msg_signature, timeStamp, nonce, encryptMsg);

        // 3. 反序列化回调事件json数据
        JSONObject eventJson = JSON.parseObject(decryptMsg);
        String eventType = eventJson.getString("EventType");

        // 4. 根据EventType分类处理
        bizLogger.info("发生了：" + eventType + "事件");

        // 5. 返回success的加密数据
        Map<String, String> successMap = callbackCrypto.getEncryptedMap("success");
        return successMap;

    } catch (DingTalkEncryptException e) {
        e.printStackTrace();
    }
    return null;
}
```
