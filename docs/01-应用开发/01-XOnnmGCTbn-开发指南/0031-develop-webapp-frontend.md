---
title: "开发网页应用前端"
source_url: "https://open.dingtalk.com/document/dingstart/develop-webapp-frontend"
namespace: "dingstart"
slug: "develop-webapp-frontend"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 开发网页应用前端"
doc_id: "kyXiSlVr23"
updated_at: "2026-07-22 16:55:18"
---

> Source: https://open.dingtalk.com/document/dingstart/develop-webapp-frontend
> Path: 应用开发 / 开发指南 / 开发网页应用 > 开发网页应用前端
> Updated: 2026-07-22 16:55:18

# 开发网页应用前端

如果你需要使用钉钉客户端 API 和钉钉客户端组件开发网页应用，你可以依据本文档操作步骤完成网页应用前端的开发。

## **企业内部应用（可选）**

### **前提条件**

1. 成为[钉钉开发者](0006-get-developer-permissions.md)。
2. 创建[应用创建与配置](0007-create-application.md)，获取应用凭证信息 Client ID、Client Secret和应用 Agent ID。

### **钉钉客户端 JSAPI 鉴权**

1. 调用[获取企业内部应用的accessToken](../02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)接口，获取应用凭证 AccessToken。
2. 根据应用凭证 AccessToken，调用[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口，获取返回参数 jsapiTicket 字段值。

   > **[!NOTE]**
   >
   > 获取 jsapiTicket 后，如果 jsapiTicket 尚未过期，再次调用[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口时，返回的 jsapiTicket 值与之前的相同，只是续期了 2 小时。需要注意的是，从 jsapiTicket 生成起，最大过期时间为 24 小时，即使续期后，最大过期时间仍从 jsapiTicket 生成起计算。
   >
   > > 例如：当你早上 9 点，生成一个 jsapiTicket 时，即使一直续期，第二天早上9点，jsapiTicket 也会过期，需要重新生成一个新的 jsapiTicket。
3. 根据 jsapiTicket，计算签名 signature 字段，计算签名的各项参数如下：

   | **参数** | **说明** | ISV开发第三方企业应用 |
   | --- | --- | --- |
   | **url** | 当前网页的URL，不包含#及其后面部分。  **[!NOTE]**  必须是当前页面的location.href 的原内容，请勿提前进行encode/urlencode处理，否则会引起编码不一致最终导致**签名校验失败**。 | — |
   | **nonceStr** | 自定义固定字符串。 | — |
   | **agentId** | 应用的标识 | 可以从授权信息中获取到。 |
   | **timeStamp** | 时间戳 | 当前时间，但是前端和服务端进行校验时候的值要一致。 |
   | **corpId** | 企业ID | 通过在页面地址上追加`?corpId=$CORPID$`进行获取。  image  必须从工作台访问应用，才会正确解析当前访问用户的组织corpId。 |

   Java

   ```
   import java.net.URL;
   import java.net.URLDecoder;
   import java.security.MessageDigest;
   import java.util.Formatter;
   import java.util.Random;

   /**
    * 计算dd.config的签名参数 signature 
    **/
   public class DdConfigSign {

       /**
        * 计算dd.config的签名参数
        *
        * @param jsticket  通过微应用appKey获取的jsticket
        * @param nonceStr  自定义固定字符串
        * @param timeStamp 当前时间戳
        * @param url       调用dd.config的当前页面URL
        * @return
        * @throws Exception
        */
       public static String sign(String jsticket, String nonceStr, long timeStamp, String url) throws Exception {
           String plain = "jsapi_ticket=" + jsticket + "&noncestr=" + nonceStr + "&timestamp=" + String.valueOf(timeStamp)
               + "&url=" + decodeUrl(url);
           try {
               MessageDigest sha1 = MessageDigest.getInstance("SHA-256");
               sha1.reset();
               sha1.update(plain.getBytes("UTF-8"));
               return byteToHex(sha1.digest());
           } catch (Exception e) {
               throw new Exception(e.getMessage());
           }
       }

       // 字节数组转化成十六进制字符串
       private static String byteToHex(final byte[] hash) {
           Formatter formatter = new Formatter();
           for (byte b : hash) {
               formatter.format("%02x", b);
           }
           String result = formatter.toString();
           formatter.close();
           return result;
       }

       /**
        * 因为ios端上传递的url是encode过的，android是原始的url。开发者使用的也是原始url,
        * 所以需要把参数进行一般urlDecode
        *
        * @param url
        * @return
        * @throws Exception
        */
       private static String decodeUrl(String url) throws Exception {
           URL urler = new URL(url);
           StringBuilder urlBuffer = new StringBuilder();
           urlBuffer.append(urler.getProtocol());
           urlBuffer.append(":");
           if (urler.getAuthority() != null && urler.getAuthority().length() > 0) {
               urlBuffer.append("//");
               urlBuffer.append(urler.getAuthority());
           }
           if (urler.getPath() != null) {
               urlBuffer.append(urler.getPath());
           }
           if (urler.getQuery() != null) {
               urlBuffer.append('?');
               urlBuffer.append(URLDecoder.decode(urler.getQuery(), "utf-8"));
           }
           return urlBuffer.toString();
       }

       public static String getRandomStr(int count) {
           String base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
           Random random = new Random();
           StringBuffer sb = new StringBuffer();
           for (int i = 0; i < count; i++) {
               int number = random.nextInt(base.length());
               sb.append(base.charAt(number));
           }
           return sb.toString();
       }
   }
   ```

   Node.js

   ```
   const crypto = require('crypto');

   /**
    * 计算dd.config的签名参数 signature
    *
    * @param {string} jsticket 通过微应用appKey获取的jsticket
    * @param {string} nonceStr 自定义固定字符串
    * @param {number} timeStamp 当前时间戳
    * @param {string} url 调用dd.config的当前页面URL
    * @returns {string} 签名
    */
   function sign(jsticket, nonceStr, timeStamp, url) {
     try {
       const plain = `jsapi_ticket=${jsticket}&noncestr=${nonceStr}&timestamp=${timeStamp}&url=${decodeUrl(url)}`;
       const sha1 = crypto.createHash('sha256');
       sha1.update(plain, 'utf8');
       return byteToHex(sha1.digest());
     } catch (error) {
       console.error('Error in sign function:', error);
       throw error;
     }
   }

   // 字节数组转化成十六进制字符串
   function byteToHex(buffer) {
     return buffer.toString('hex');
   }

   /**
    * 因为ios端上传递的url是encode过的，android是原始的url。开发者使用的也是原始url,
    * 所以需要把参数进行一般urlDecode
    *
    * @param {string} urlString
    * @returns {string} 解码后的URL
    */
   function decodeUrl(urlString) {
     try {
       const parsedUrl = new URL(urlString);
       let urlBuffer = `${parsedUrl.protocol}:`;
       if (parsedUrl.host) {
         urlBuffer += `//${parsedUrl.host}`;
       }
       if (parsedUrl.pathname) {
         urlBuffer += parsedUrl.pathname;
       }
       if (parsedUrl.search) {
         urlBuffer += `?${decodeURIComponent(parsedUrl.search.substring(1))}`;
       }
       return urlBuffer;
     } catch (error) {
       console.error('Error in decodeUrl function:', error);
       throw error;
     }
   }

   module.exports = { sign };
   ```
4. 签名计算完成后，你需要返回给前端鉴权组件 dd. config 所需参数，包括：

   - 应用agentId
   - 企业corpId
   - 当前时间戳timeStamp
   - 自定义字符串nonceStr
   - 计算的签名信息signature
   - 应用类型type和授权组件列表 jsApiList
5. 前端 引入 JS SDK，详情参考[客户端SDK介绍](0029-webapp-read-before-development.md)。

   > 钉钉客户端使用一段式，例如：chooseChat， dingtalk-jsapi SDK 版本至少为3.0.27。

   ```
   npm install dingtalk-jsapi --save
   ```
6. 引入鉴权组件并配置参数：

   > **[!NOTE]**
   >
   > - 如果前端页面存在父子页面关系，那么必须对父页面进行鉴权，因为计算签名的方法不支持路由页面地址。当需要鉴权的子页面被加载时，需要刷新父页面，以完成鉴权流程，然后该子页面就可以调用需要鉴权的客户端 API。
   > - dd.config 下的参数值，必须从服务端中获取，否则无法鉴权成功。

   | **企业内部应用** | **第三方企业应用** |
   | --- | --- |
   | ``` dd.config({     agentId: '', // 企业内部应用，该值为企业内部应用的agentId。     corpId: '',//必填，企业ID     timeStamp: '', // 必填，生成签名的时间戳     nonceStr: '', // 必填，自定义固定字符串。     signature: '', // 必填，签名     type:0/1,   //选填。0表示微应用的jsapi,1表示服务窗的jsapi；不填默认为0。该参数从dingtalk.js的0.8.3版本开始支持     jsApiList : [         'biz.contact.choose',         'chooseChat'     ] // 必填，需要使用的jsapi列表，注意：不要带dd。 });  dd.error(function (err) {     alert('dd error: ' + JSON.stringify(err)); })//该方法必须带上，用来捕获鉴权出现的异常信息，否则不方便排查出现的问题 ``` | ``` dd.config({     appId: '', // 第三方企业应用，该参数值为授权企业开通后应用的agentId。不是第三方企业应用的appId。     corpId: '',//必填，企业ID     timeStamp: '', // 必填，生成签名的时间戳     nonceStr: '', // 必填，自定义固定字符串。     signature: '', // 必填，签名     type:0/1,   //选填。0表示微应用的jsapi,1表示服务窗的jsapi；不填默认为0。该参数从dingtalk.js的0.8.3版本开始支持     jsApiList : [         'biz.contact.choose',         'chooseChat'     ] // 必填，需要使用的jsapi列表，注意：不要带dd。 });  dd.error(function (err) {     alert('dd error: ' + JSON.stringify(err)); })//该方法必须带上，用来捕获鉴权出现的异常信息，否则不方便排查出现的问题 ``` |
7. 配置完成后，即可调用客户端 API，例如 chooseChat：

   ```
   dd.chooseChat({
     corpId: `corpId示例值`,
     isAllowCreateGroup: true,
     filterNotOwnerGroup: true,
     success: (res) => {
       const { title, chatId, openConversationId } = res;
     },
     fail: () => {},
     complete: () => {},
   });
   ```

### **体验示例Demo**

#### **开发准备**

| **开发环境** | **说明** |
| --- | --- |
| Java | - 已安装 JDK 17 及以上 - 已安装 Maven 3   本示例使用 JDK 17。 |
| Node.js | - 已安装 Node.js。 |

#### 应用准备

| **应用配置** | **说明** |
| --- | --- |
| 获取应用的凭证信息 | 获取应用 Client ID 、Client Secret 和 Agent ID。  image |
| 应用首页地址 | 设置为：`http://localhost:5173?corpid=$CORPID$`，用于后续测试使用。  image |
| PC端首页地址 |

> **[!NOTE]**
>
> 配置完成后，确保应用完成发布，否则工作台不可见，无法使用应用。

#### **操作步骤**

1. 确保完成上述准备工作，准备好下方示例 Demo的运行条件。
2. 你可以下载 [web-app-jsapi-auth.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250610/sixpfd/web-app-jsapi-auth.zip) Demo。
3. 你需要分别启动前端项目和后端项目：

   > *注意：确保 5173 和 8080 端口没有被占用。*

   | **启动项** | **说明** |
   | --- | --- |
   | 前端服务 | 在解压后的 web-app-jsapi-auth 的目录下：  1. `cd frontend/`  2. `npm install`  3. `npm run dev` |
   | 后端服务 | 在解压后的 web-app-jsapi-auth 的目录下：  1. `cd backend/`  2. `./mvnw spring-boot:run -Dspring-boot.run.arguments="--dingtalk.clientId=your app clientId --dingtalk.clientSecret=your app clientSecret --dingtalk.agentId=your app agentId"`  **[!NOTE]**  你需要替换 clientId 和 clientSecret：  - Client ID，详情参考[Client ID](0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 - Client Secret，详情参考 [Client Secret](0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 - Agent ID，详情参考[基础概念](0001-basic-concepts-beta.md#884d363067bnq)。 |
4. 项目启动后，即可在钉钉工作台打开应用。本示例分别鉴权：

   - [biz.contact.choose](../03-Ogu5SlPY4t-客户端-JSAPI/0740-on-the-pc-select-the-person-in-the-enterprise.md)：PC 端选择企业内部的人
   - [chooseChat](../03-Ogu5SlPY4t-客户端-JSAPI/0318-jsapi-choose-chat.md)：PC 端选择会话

     > 钉钉客户端使用一段式，例如：chooseChat， dingtalk-jsapi SDK 版本至少为3.0.27。

     | **客户端JSAPI** | **说明** |
     | --- | --- |
     | biz.contact.choose | **访问：**  image |
     | **结果：**  image |
     | chooseChat | **访问：**  image |
     | **结果：**  image |

## **第三方企业应用**

## 开发流程

确保服务端开发者已完成以下操作：

1. 调用[获取第三方应用授权企业的accessToken](../02-4a8AMF6u2A-服务端-API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口，获取应用凭证 AccessToken。

   > **[!NOTE]**
   >
   > 必须使用当前网页应用的参数获取access\_token。
2. 根据应用凭证 AccessToken，调用[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口，获取返回参数`jsapiTicket`字段值。

   > **[!NOTE]**
   >
   > 获取 jsapiTicket 后，如果 jsapiTicket 尚未过期，再次调用[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口时，返回的 jsapiTicket 值与之前的相同，只是续期了 2 小时。需要注意的是，从 jsapiTicket 生成起，最大过期时间为 24 小时，即使续期后，最大过期时间仍从 jsapiTicket 生成起计算。
   >
   > > 例如：当你早上 9 点，生成一个 jsapiTicket 时，即使一直续期，第二天早上9点，jsapiTicket 也会过期，需要重新生成一个新的 jsapiTicket。
3. 根据 jsapiTicket，计算签名 signature 字段，计算签名的各项参数如下：

   | **参数** | **说明** | ISV开发第三方企业应用 |
   | --- | --- | --- |
   | **url** | 当前网页的URL，不包含#及其后面部分。    **[!NOTE]**  必须是当前页面的location.href 的原内容，请勿提前进行encode/urlencode处理，否则会引起编码不一致最终导致**签名校验失败**。 | — |
   | **nonceStr** | 自定义固定字符串。 | — |
   | **agentId** | 应用的标识 | 可以从授权信息中获取到。 |
   | **timeStamp** | 时间戳 | 当前时间，但是前端和服务端进行校验时候的值要一致。 |
   | **corpId** | 企业ID | 通过在页面地址上追加?`corpId=$CORPID$`进行获取。  image |

   Java

   ```
   import java.net.URL;
   import java.net.URLDecoder;
   import java.security.MessageDigest;
   import java.util.Formatter;
   import java.util.Random;

   /**
    * 计算dd.config的签名参数 signature 
    **/
   public class DdConfigSign {

       /**
        * 计算dd.config的签名参数
        *
        * @param jsticket  通过微应用appKey获取的jsticket
        * @param nonceStr  自定义固定字符串
        * @param timeStamp 当前时间戳
        * @param url       调用dd.config的当前页面URL
        * @return
        * @throws Exception
        */
       public static String sign(String jsticket, String nonceStr, long timeStamp, String url) throws Exception {
           String plain = "jsapi_ticket=" + jsticket + "&noncestr=" + nonceStr + "&timestamp=" + String.valueOf(timeStamp)
               + "&url=" + decodeUrl(url);
           try {
               MessageDigest sha1 = MessageDigest.getInstance("SHA-256");
               sha1.reset();
               sha1.update(plain.getBytes("UTF-8"));
               return byteToHex(sha1.digest());
           } catch (Exception e) {
               throw new Exception(e.getMessage());
           }
       }

       // 字节数组转化成十六进制字符串
       private static String byteToHex(final byte[] hash) {
           Formatter formatter = new Formatter();
           for (byte b : hash) {
               formatter.format("%02x", b);
           }
           String result = formatter.toString();
           formatter.close();
           return result;
       }

       /**
        * 因为ios端上传递的url是encode过的，android是原始的url。开发者使用的也是原始url,
        * 所以需要把参数进行一般urlDecode
        *
        * @param url
        * @return
        * @throws Exception
        */
       private static String decodeUrl(String url) throws Exception {
           URL urler = new URL(url);
           StringBuilder urlBuffer = new StringBuilder();
           urlBuffer.append(urler.getProtocol());
           urlBuffer.append(":");
           if (urler.getAuthority() != null && urler.getAuthority().length() > 0) {
               urlBuffer.append("//");
               urlBuffer.append(urler.getAuthority());
           }
           if (urler.getPath() != null) {
               urlBuffer.append(urler.getPath());
           }
           if (urler.getQuery() != null) {
               urlBuffer.append('?');
               urlBuffer.append(URLDecoder.decode(urler.getQuery(), "utf-8"));
           }
           return urlBuffer.toString();
       }

       public static String getRandomStr(int count) {
           String base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
           Random random = new Random();
           StringBuffer sb = new StringBuffer();
           for (int i = 0; i < count; i++) {
               int number = random.nextInt(base.length());
               sb.append(base.charAt(number));
           }
           return sb.toString();
       }
   }
   ```

   Node.js

   ```
   const crypto = require('crypto');

   /**
    * 计算dd.config的签名参数 signature
    *
    * @param {string} jsticket 通过微应用appKey获取的jsticket
    * @param {string} nonceStr 自定义固定字符串
    * @param {number} timeStamp 当前时间戳
    * @param {string} url 调用dd.config的当前页面URL
    * @returns {string} 签名
    */
   function sign(jsticket, nonceStr, timeStamp, url) {
     try {
       const plain = `jsapi_ticket=${jsticket}&noncestr=${nonceStr}&timestamp=${timeStamp}&url=${decodeUrl(url)}`;
       const sha1 = crypto.createHash('sha256');
       sha1.update(plain, 'utf8');
       return byteToHex(sha1.digest());
     } catch (error) {
       console.error('Error in sign function:', error);
       throw error;
     }
   }

   // 字节数组转化成十六进制字符串
   function byteToHex(buffer) {
     return buffer.toString('hex');
   }

   /**
    * 因为ios端上传递的url是encode过的，android是原始的url。开发者使用的也是原始url,
    * 所以需要把参数进行一般urlDecode
    *
    * @param {string} urlString
    * @returns {string} 解码后的URL
    */
   function decodeUrl(urlString) {
     try {
       const parsedUrl = new URL(urlString);
       let urlBuffer = `${parsedUrl.protocol}:`;
       if (parsedUrl.host) {
         urlBuffer += `//${parsedUrl.host}`;
       }
       if (parsedUrl.pathname) {
         urlBuffer += parsedUrl.pathname;
       }
       if (parsedUrl.search) {
         urlBuffer += `?${decodeURIComponent(parsedUrl.search.substring(1))}`;
       }
       return urlBuffer;
     } catch (error) {
       console.error('Error in decodeUrl function:', error);
       throw error;
     }
   }

   module.exports = { sign };
   ```
4. 签名计算完成后，你需要返回给前端，用于 dd.config 所需参数包括：

   - 应用agentId
   - 企业corpId
   - 当前时间戳timeStamp
   - 自定义字符串nonceStr
   - 计算的签名信息signature
   - 应用类型type和授权组件列表 jsApiList
5. 前端 引入 JS SDK，详情参考[客户端SDK介绍](0029-webapp-read-before-development.md)。

   > 钉钉客户端使用一段式，例如：chooseChat， dingtalk-jsapi SDK 版本至少为3.0.27。

   ```
   npm install dingtalk-jsapi --save
   ```
6. 引入鉴权组件并配置参数：

   > **[!NOTE]**
   >
   > - 如果前端页面存在父子页面关系，那么必须对父页面进行鉴权，因为计算签名的方法不支持路由页面地址。当需要鉴权的子页面被加载时，需要刷新父页面，以完成鉴权流程，然后该子页面就可以调用需要鉴权的客户端 API。
   > - dd.config 下的参数值，必须从服务端中获取，否则无法鉴权成功。

   | **企业内部应用** | **第三方企业应用** |
   | --- | --- |
   | ``` dd.config({     agentId: '', // 企业内部应用，该值为企业内部应用的agentId。     corpId: '',//必填，企业ID     timeStamp: '', // 必填，生成签名的时间戳     nonceStr: '', // 必填，自定义固定字符串。     signature: '', // 必填，签名     type:0/1,   //选填。0表示微应用的jsapi,1表示服务窗的jsapi；不填默认为0。该参数从dingtalk.js的0.8.3版本开始支持     jsApiList : [         'biz.contact.choose',         'chooseChat'     ] // 必填，需要使用的jsapi列表，注意：不要带dd。 });  dd.error(function (err) {     alert('dd error: ' + JSON.stringify(err)); })//该方法必须带上，用来捕获鉴权出现的异常信息，否则不方便排查出现的问题 ``` | ``` dd.config({     appId: '', // 第三方企业应用，该参数值为授权企业开通后应用的agentId。不是第三方企业应用的appId。     corpId: '',//必填，企业ID     timeStamp: '', // 必填，生成签名的时间戳     nonceStr: '', // 必填，自定义固定字符串。     signature: '', // 必填，签名     type:0/1,   //选填。0表示微应用的jsapi,1表示服务窗的jsapi；不填默认为0。该参数从dingtalk.js的0.8.3版本开始支持     jsApiList : [         'biz.contact.choose',         'chooseChat'     ] // 必填，需要使用的jsapi列表，注意：不要带dd。 });  dd.error(function (err) {     alert('dd error: ' + JSON.stringify(err)); })//该方法必须带上，用来捕获鉴权出现的异常信息，否则不方便排查出现的问题 ``` |
7. 配置完成后，即可调用客户端 API，例如 chooseChat：

   ```
   dd.chooseChat({
     corpId: `corpId示例值`,
     isAllowCreateGroup: true,
     filterNotOwnerGroup: true,
     success: (res) => {
       const { title, chatId, openConversationId } = res;
     },
     fail: () => {},
     complete: () => {},
   });
   ```

## **后续步骤**

开发完成后，你需要完成以下步骤：

- 企业内部应用：[发布应用](0017-publish-dingtalk-application.md)，如果你需要实现免登、接入事件订阅和使用钉钉服务端 API，需要[开发网页应用服务端](0032-develop-webapp-backend.md)。
- 第三发企业应用：[配置网页应用](0030-configure-web-application.md)
