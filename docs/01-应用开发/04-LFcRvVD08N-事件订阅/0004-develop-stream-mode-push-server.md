---
title: "开发事件推送服务"
source_url: "https://open.dingtalk.com/document/development/develop-stream-mode-push-server"
namespace: "development"
slug: "develop-stream-mode-push-server"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "开发指南 > 开发事件推送服务"
doc_id: "AmJSGSHW1a"
updated_at: "2026-07-22 16:25:25"
---

> Source: https://open.dingtalk.com/document/development/develop-stream-mode-push-server
> Path: 应用开发 / 事件订阅 / 开发指南 > 开发事件推送服务
> Updated: 2026-07-22 16:25:25

# 开发事件推送服务

如果你需要开发事件订阅的推送服务，可以选择Stream模式推送、HTTP模式推送或SyncHTTP等三种推送模式中的一种，你可以参考本文档操作步骤完成开发操作。

## **开发 Stream 模式（推荐）**

### **Java**

#### **前提条件**

- 拥有访问公网的运行环境。
- JDK1.8及以上。

#### **安装 SDK**

添加依赖项到工程的pom.xml文件或下载对应的jar包，最新的 SDK 版本可以在[这里](https://central.sonatype.com/artifact/com.dingtalk.open/app-stream-client)查看和下载。

```
<dependency>
  <groupId>com.dingtalk.open</groupId>
  <artifactId>app-stream-client</artifactId>
  <version>{sdk-version}</version>
</dependency>
```

#### **服务端接入**

| **配置项** | **描述** |
| --- | --- |
| ${clientId} | 钉钉企业内部应用和钉钉第三方企业应用的唯一身份标识。详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client ID 对应旧版应用的AppKey/SuiteKey。 |
| ${clientSecret} | 钉钉企业内部应用和钉钉第三方企业应用的调用密钥，详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client Secret 对应旧版应用的AppSecret/SuiteSecret。 |

```
public static void main(String[] args) {
  OpenDingTalkStreamClientBuilder
    .custom()
    .credential(new AuthClientCredential("${clientId}", "${clientSecret}"))
    //注册事件监听
    .registerAllEventListener(new GenericEventListener() {
      public EventAckStatus onEvent(GenericOpenDingTalkEvent event) {
        try {
          //事件唯一Id
          String eventId = event.getEventId();
          //事件类型
          String eventType = event.getEventType();
          //事件产生时间
          Long bornTime = event.getEventBornTime();
          //获取事件体
          JSONObject bizData = event.getData();
          //处理事件
          process(bizData);
          //消费成功
          return EventAckStatus.SUCCESS;
        } catch (Exception e) {
          //消费失败
          return EventAckStatus.LATER;
        }
      }
    })
    .build().start();
}
```

#### **示例代码**

我们以机器人回调和互动卡片回调举例，开发者可参考下方示例代码：

- **机器人回调**

  ```
  public static void main(String[] args) throws Exception {
    OpenDingTalkStreamClientBuilder
      .custom()
      .credential(new AuthClientCredential("${clientId}", "${clientSecret}"))
      //注册机器人监听器
      .registerCallbackListener("${topic}", robotMessage -> {
        log.info("receive robotMessage, {}", robotMessage);
        //开发者根据自身业务需求，处理机器人回调
        return new JSONObject();

      })
      .build().start();
  }
  ```

  | **参数名** | **说明** |
  | --- | --- |
  | clientId | 钉钉企业内部应用和钉钉第三方企业应用的唯一身份标识。详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client ID 对应旧版应用的AppKey/SuiteKey。 |
  | clientSecret | 钉钉企业内部应用和钉钉第三方企业应用的调用密钥，详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client Secret 对应旧版应用的AppSecret/SuiteSecret。 |
  | topic | 机器人回调名称，固定值：`/v1.0/im/bot/messages/get`。 |
- **卡片回调**

  详情参见[互动卡片-事件回调](../../05-互动卡片/02-MhNX42mFB1-模板搭建卡片/0007-event-callback-card.md)。

  ```
  public static void main(String[] args) throws Exception {
          OpenDingTalkStreamClientBuilder
                  .custom()
                  .credential(new AuthClientCredential("${clientId}", "${clientSecret}"))
                  //注册卡片回传监听器
                  .registerCallbackListener("/v1.0/card/instances/callback", callbackData -> {
                      log.info("receive call back request, {}", callbackData);
                      //your code is here

                      //开发者根据自身业务需求，变更卡片内容，返回response
                      CardCallbackResponse resp = new CardCallbackResponse();
                      return resp;

                  })
                  .build().start();
  }
  ```

  | **参数名** | **说明** |
  | --- | --- |
  | clientId | 钉钉企业内部应用和钉钉第三方企业应用的唯一身份标识。详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client ID 对应旧版应用的AppKey/SuiteKey。 |
  | clientSecret | 钉钉企业内部应用和钉钉第三方企业应用的调用密钥，详情参见[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client Secret 对应旧版应用的AppSecret/SuiteSecret。 |
  | topic | 注册的卡片回调名称，固定值：`/v1.0/card/instances/callback`。 |

### **Golang**

#### **前提条件**

- 拥有访问公网的运行环境。
- 运行环境1.16及以上。

#### **安装 SDK**

```
go get github.com/open-dingtalk/dingtalk-stream-sdk-go/v0.0.5
```

#### **服务端接入**

| **配置项** | **描述** |
| --- | --- |
| ${clientId} | 钉钉企业内部应用和钉钉第三方企业应用的唯一身份标识。详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client ID 对应旧版应用的AppKey/SuiteKey。 |
| ${clientSecret} | 钉钉企业内部应用和钉钉第三方企业应用的调用密钥，详情参见 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。  Client Secret 对应旧版应用的AppSecret/SuiteSecret。 |

```
func main() {
  e := clientV2.
    NewBuilder().
    Credential(&clientV2.AuthClientCredential{ClientId: "${clientId}", ClientSecret: "${clientSecret}"}).
    //监听开放平台事件
    RegisterAllEventHandler(func(event *clientV2.GenericOpenDingTalkEvent) clientV2.EventStatus {
      println("receive event ", event.Data)
      //成功返回 clientV2.EventStatusSuccess,失败返回clientV2.EventStatusLater
      return clientV2.EventStatusSuccess
    }).
    Build().
    Start(context.Background())
	
  if e != nil {
    println("failed to start stream client", e.Error())
    return
  }

  select {}
}
```

#### **示例代码**

我们以机器人回调举例，开发者可参考下方示例代码：

```
func OnChatReceive(ctx context.Context, data *chatbot.BotCallbackDataModel) error {
  return nil
}

func StartRobot() {
  logger.SetLogger(logger.NewStdTestLogger())
  cli := client.NewStreamClient(
    client.WithAppCredential(client.NewAppCredentialConfig(${clientId}, ${clientSecret})),
    client.WithUserAgent(client.NewDingtalkGoSDKUserAgent()),
    client.WithSubscription(utils.SubscriptionTypeKCallback, ${topic}, chatbot.NewDefaultChatBotFrameHandler(OnChatReceive).OnEventReceived),
  )

  err := cli.Start(context.Background())
  if err != nil {
    panic(err)
  }

  defer cli.Close()

  select {}
}
```

| **参数名** | **说明** |
| --- | --- |
| clientId | 企业内部开发 AppKey/第三方企业应用 SuiteKey。 |
| clientSecret | 企业内部开发 AppSecret/第三方企业应用 SuiteSecret。 |
| topic | 机器人回调名称，固定值：`/v1.0/im/bot/messages/get`。 |

### **其他语言支持**

- [Java SDK接入示例工程](https://github.com/open-dingtalk/dingtalk-stream-sdk-java-quick-start)
- [Golang SDK及示例代码](https://github.com/open-dingtalk/dingtalk-stream-sdk-go)
- [Python SDK及示例代码](https://github.com/open-dingtalk/dingtalk-stream-sdk-python)
- [Node.js SDK及示例代码](https://github.com/open-dingtalk/dingtalk-stream-sdk-nodejs)

过程中有问题也可以通过[技术支持](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)提交反馈和问题交流。

### **错误码**

当接收事件显示

| 错误码（errCode） | 错误信息（errMsg） | **说明** | 解决方案 |
| --- | --- | --- | --- |
| 20001 | 受调用量超量影响，当前我的消息服务已经暂停。请联系你所在的组织管理员并予以处理  接收消息中，新增 **errMsg** 字段，用于展示错误信息。 | - 接收消息中无消息内容   无 text 和 content 字段内容   - 登录[开发者后台](https://open-dev.dingtalk.com/)即可查看调用量。  image | 需要升级钉钉专业版或购买增购包。 |

### **常见问题**

- **一个应用程序中，是否可以启动多个事件监听？**

  答：可以启动多个事件监听服务，你可以根据需要启动多个Stream客户端配置。

  > 1. 企业内部应用：一个企业仅需配置一个Stream客户端即可。

  > 2. 第三方企业应用：仅需监听该第三方企业应用，即可获取当前授权企业的事件订阅内容。

## **开发 HTTP 模式**

### **前提条件**

1. 了解[配置 HTTP 推送（不推荐）](0003-configure-stream-push.md#58bfd87c4fupu)流程。
2. 开发环境：

   - Maven 3
   - JDK ：1.8 及以上

### **操作步骤**

1. 接入事件消息加解密类：

   ```
   package com.dingtalk.open;

   import java.io.ByteArrayOutputStream;
   import java.nio.charset.Charset;
   import java.security.MessageDigest;
   import java.security.Permission;
   import java.security.PermissionCollection;
   import java.util.Arrays;
   import java.util.HashMap;
   import java.util.Map;
   import java.util.Random;
   import java.security.Security;
   import java.lang.reflect.Field;

   import javax.crypto.Cipher;
   import javax.crypto.spec.IvParameterSpec;
   import javax.crypto.spec.SecretKeySpec;

   import com.alibaba.fastjson.JSON;

   import org.apache.commons.codec.binary.Base64;

   public class DingCallbackCrypto {

       private static final Charset CHARSET = Charset.forName("utf-8");
       private static final Base64 base64 = new Base64();
       private byte[] aesKey;
       private String token;
       private String corpId;
       /**
        * ask getPaddingBytes key固定长度
        **/
       private static final Integer AES_ENCODE_KEY_LENGTH = 43;
       /**
        * 加密随机字符串字节长度
        **/
       private static final Integer RANDOM_LENGTH = 16;

       /**
        * 构造函数
        *
        * @param token          钉钉开放平台上，开发者设置的token
        * @param encodingAesKey 钉钉开放台上，开发者设置的EncodingAESKey
        * @param corpId         企业自建应用-事件订阅, 使用appKey
        *                       企业自建应用-注册回调地址, 使用corpId
        *                       第三方企业应用, 使用suiteKey
        *
        * @throws DingTalkEncryptException 执行失败，请查看该异常的错误码和具体的错误信息
        */
       public DingCallbackCrypto(String token, String encodingAesKey, String corpId) throws DingTalkEncryptException {
           if (null == encodingAesKey || encodingAesKey.length() != AES_ENCODE_KEY_LENGTH) {
               throw new DingTalkEncryptException(DingTalkEncryptException.AES_KEY_ILLEGAL);
           }
           this.token = token;
           this.corpId = corpId;
           aesKey = Base64.decodeBase64(encodingAesKey + "=");
       }

       public Map<String, String> getEncryptedMap(String plaintext) throws DingTalkEncryptException {
           return getEncryptedMap(plaintext, System.currentTimeMillis(), Utils.getRandomStr(16));
       }

       /**
        * 将和钉钉开放平台同步的消息体加密,返回加密Map
        *
        * @param plaintext 传递的消息体明文
        * @param timeStamp 时间戳
        * @param nonce     随机字符串
        * @return
        * @throws DingTalkEncryptException
        */
       public Map<String, String> getEncryptedMap(String plaintext, Long timeStamp, String nonce)
           throws DingTalkEncryptException {
           if (null == plaintext) {
               throw new DingTalkEncryptException(DingTalkEncryptException.ENCRYPTION_PLAINTEXT_ILLEGAL);
           }
           if (null == timeStamp) {
               throw new DingTalkEncryptException(DingTalkEncryptException.ENCRYPTION_TIMESTAMP_ILLEGAL);
           }
           if (null == nonce) {
               throw new DingTalkEncryptException(DingTalkEncryptException.ENCRYPTION_NONCE_ILLEGAL);
           }
           // 加密
           String encrypt = encrypt(Utils.getRandomStr(RANDOM_LENGTH), plaintext);
           String signature = getSignature(token, String.valueOf(timeStamp), nonce, encrypt);
           Map<String, String> resultMap = new HashMap<String, String>();
           resultMap.put("msg_signature", signature);
           resultMap.put("encrypt", encrypt);
           resultMap.put("timeStamp", String.valueOf(timeStamp));
           resultMap.put("nonce", nonce);
           return resultMap;
       }

       /**
        * 密文解密
        *
        * @param msgSignature 签名串
        * @param timeStamp    时间戳
        * @param nonce        随机串
        * @param encryptMsg   密文
        * @return 解密后的原文
        * @throws DingTalkEncryptException
        */
       public String getDecryptMsg(String msgSignature, String timeStamp, String nonce, String encryptMsg)
           throws DingTalkEncryptException {
           //校验签名
           String signature = getSignature(token, timeStamp, nonce, encryptMsg);
           if (!signature.equals(msgSignature)) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_SIGNATURE_ERROR);
           }
           // 解密
           String result = decrypt(encryptMsg);
           return result;
       }

       /*
        * 对明文加密.
        * @param text 需要加密的明文
        * @return 加密后base64编码的字符串
        */
       private String encrypt(String random, String plaintext) throws DingTalkEncryptException {
           try {
               byte[] randomBytes = random.getBytes(CHARSET);
               byte[] plainTextBytes = plaintext.getBytes(CHARSET);
               byte[] lengthByte = Utils.int2Bytes(plainTextBytes.length);
               byte[] corpidBytes = corpId.getBytes(CHARSET);
               ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
               byteStream.write(randomBytes);
               byteStream.write(lengthByte);
               byteStream.write(plainTextBytes);
               byteStream.write(corpidBytes);
               byte[] padBytes = PKCS7Padding.getPaddingBytes(byteStream.size());
               byteStream.write(padBytes);
               byte[] unencrypted = byteStream.toByteArray();
               byteStream.close();
               Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
               SecretKeySpec keySpec = new SecretKeySpec(aesKey, "AES");
               IvParameterSpec iv = new IvParameterSpec(aesKey, 0, 16);
               cipher.init(Cipher.ENCRYPT_MODE, keySpec, iv);
               byte[] encrypted = cipher.doFinal(unencrypted);
               String result = base64.encodeToString(encrypted);
               return result;
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_ENCRYPT_TEXT_ERROR);
           }
       }

       /*
        * 对密文进行解密.
        * @param text 需要解密的密文
        * @return 解密得到的明文
        */
       private String decrypt(String text) throws DingTalkEncryptException {
           byte[] originalArr;
           try {
               // 设置解密模式为AES的CBC模式
               Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
               SecretKeySpec keySpec = new SecretKeySpec(aesKey, "AES");
               IvParameterSpec iv = new IvParameterSpec(Arrays.copyOfRange(aesKey, 0, 16));
               cipher.init(Cipher.DECRYPT_MODE, keySpec, iv);
               // 使用BASE64对密文进行解码
               byte[] encrypted = Base64.decodeBase64(text);
               // 解密
               originalArr = cipher.doFinal(encrypted);
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_DECRYPT_TEXT_ERROR);
           }

           String plainText;
           String fromCorpid;
           try {
               // 去除补位字符
               byte[] bytes = PKCS7Padding.removePaddingBytes(originalArr);
               // 分离16位随机字符串,网络字节序和corpId
               byte[] networkOrder = Arrays.copyOfRange(bytes, 16, 20);
               int plainTextLegth = Utils.bytes2int(networkOrder);
               plainText = new String(Arrays.copyOfRange(bytes, 20, 20 + plainTextLegth), CHARSET);
               fromCorpid = new String(Arrays.copyOfRange(bytes, 20 + plainTextLegth, bytes.length), CHARSET);
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_DECRYPT_TEXT_LENGTH_ERROR);
           }

           // corpid不相同的情况
           if (!fromCorpid.equals(corpId)) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_DECRYPT_TEXT_CORPID_ERROR);
           }
           return plainText;
       }

       /**
        * 数字签名
        *
        * @param token     isv token
        * @param timestamp 时间戳
        * @param nonce     随机串
        * @param encrypt   加密文本
        * @return
        * @throws DingTalkEncryptException
        */
       public String getSignature(String token, String timestamp, String nonce, String encrypt)
           throws DingTalkEncryptException {
           try {
               String[] array = new String[] {token, timestamp, nonce, encrypt};
               Arrays.sort(array);
               System.out.println(JSON.toJSONString(array));
               StringBuffer sb = new StringBuffer();
               for (int i = 0; i < 4; i++) {
                   sb.append(array[i]);
               }
               String str = sb.toString();
               System.out.println(str);
               MessageDigest md = MessageDigest.getInstance("SHA-1");
               md.update(str.getBytes());
               byte[] digest = md.digest();

               StringBuffer hexstr = new StringBuffer();
               String shaHex = "";
               for (int i = 0; i < digest.length; i++) {
                   shaHex = Integer.toHexString(digest[i] & 0xFF);
                   if (shaHex.length() < 2) {
                       hexstr.append(0);
                   }
                   hexstr.append(shaHex);
               }
               return hexstr.toString();
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_SIGNATURE_ERROR);
           }
       }

       public static class Utils {
           public Utils() {
           }

           public static String getRandomStr(int count) {
               String base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
               Random random = new Random();
               StringBuffer sb = new StringBuffer();

               for (int i = 0; i < count; ++i) {
                   int number = random.nextInt(base.length());
                   sb.append(base.charAt(number));
               }

               return sb.toString();
           }

           public static byte[] int2Bytes(int count) {
               byte[] byteArr = new byte[] {(byte)(count >> 24 & 255), (byte)(count >> 16 & 255), (byte)(count >> 8 & 255),
                   (byte)(count & 255)};
               return byteArr;
           }

           public static int bytes2int(byte[] byteArr) {
               int count = 0;

               for (int i = 0; i < 4; ++i) {
                   count <<= 8;
                   count |= byteArr[i] & 255;
               }

               return count;
           }
       }

       public static class PKCS7Padding {
           private static final Charset CHARSET = Charset.forName("utf-8");
           private static final int BLOCK_SIZE = 32;

           public PKCS7Padding() {
           }

           public static byte[] getPaddingBytes(int count) {
               int amountToPad = 32 - count % 32;
               if (amountToPad == 0) {
                   amountToPad = 32;
               }

               char padChr = chr(amountToPad);
               String tmp = new String();

               for (int index = 0; index < amountToPad; ++index) {
                   tmp = tmp + padChr;
               }

               return tmp.getBytes(CHARSET);
           }

           public static byte[] removePaddingBytes(byte[] decrypted) {
               int pad = decrypted[decrypted.length - 1];
               if (pad < 1 || pad > 32) {
                   pad = 0;
               }

               return Arrays.copyOfRange(decrypted, 0, decrypted.length - pad);
           }

           private static char chr(int a) {
               byte target = (byte)(a & 255);
               return (char)target;
           }
       }

       public static class DingTalkEncryptException extends Exception {
           public static final int SUCCESS = 0;
           public static final int ENCRYPTION_PLAINTEXT_ILLEGAL = 900001;
           public static final int ENCRYPTION_TIMESTAMP_ILLEGAL = 900002;
           public static final int ENCRYPTION_NONCE_ILLEGAL = 900003;
           public static final int AES_KEY_ILLEGAL = 900004;
           public static final int SIGNATURE_NOT_MATCH = 900005;
           public static final int COMPUTE_SIGNATURE_ERROR = 900006;
           public static final int COMPUTE_ENCRYPT_TEXT_ERROR = 900007;
           public static final int COMPUTE_DECRYPT_TEXT_ERROR = 900008;
           public static final int COMPUTE_DECRYPT_TEXT_LENGTH_ERROR = 900009;
           public static final int COMPUTE_DECRYPT_TEXT_CORPID_ERROR = 900010;
           private static Map<Integer, String> msgMap = new HashMap();
           private Integer code;

           static {
               msgMap.put(0, "成功");
               msgMap.put(900001, "加密明文文本非法");
               msgMap.put(900002, "加密时间戳参数非法");
               msgMap.put(900003, "加密随机字符串参数非法");
               msgMap.put(900005, "签名不匹配");
               msgMap.put(900006, "签名计算失败");
               msgMap.put(900004, "不合法的aes key");
               msgMap.put(900007, "计算加密文字错误");
               msgMap.put(900008, "计算解密文字错误");
               msgMap.put(900009, "计算解密文字长度不匹配");
               msgMap.put(900010, "计算解密文字corpid不匹配");
           }

           public Integer getCode() {
               return this.code;
           }

           public DingTalkEncryptException(Integer exceptionCode) {
               super((String)msgMap.get(exceptionCode));
               this.code = exceptionCode;
           }
       }
       static {
                   try {
                           Security.setProperty("crypto.policy", "limited");
                           RemoveCryptographyRestrictions();
                   } catch (Exception var1) {
                   }

           }
           private static void RemoveCryptographyRestrictions() throws Exception {
                   Class<?> jceSecurity = getClazz("javax.crypto.JceSecurity");
                   Class<?> cryptoPermissions = getClazz("javax.crypto.CryptoPermissions");
                   Class<?> cryptoAllPermission = getClazz("javax.crypto.CryptoAllPermission");
                   if (jceSecurity != null) {
                           setFinalStaticValue(jceSecurity, "isRestricted", false);
                           PermissionCollection defaultPolicy = (PermissionCollection)getFieldValue(jceSecurity, "defaultPolicy", (Object)null, PermissionCollection.class);
                           if (cryptoPermissions != null) {
                                   Map<?, ?> map = (Map)getFieldValue(cryptoPermissions, "perms", defaultPolicy, Map.class);
                                   map.clear();
                           }

                           if (cryptoAllPermission != null) {
                                   Permission permission = (Permission)getFieldValue(cryptoAllPermission, "INSTANCE", (Object)null, Permission.class);
                                   defaultPolicy.add(permission);
                           }
                   }

           }
           private static Class<?> getClazz(String className) {
                   Class clazz = null;

                   try {
                           clazz = Class.forName(className);
                   } catch (Exception var3) {
                   }

                   return clazz;
           }
           private static void setFinalStaticValue(Class<?> srcClazz, String fieldName, Object newValue) throws Exception {
                   Field field = srcClazz.getDeclaredField(fieldName);
                   field.setAccessible(true);
                   Field modifiersField = Field.class.getDeclaredField("modifiers");
                   modifiersField.setAccessible(true);
                   modifiersField.setInt(field, field.getModifiers() & -17);
                   field.set((Object)null, newValue);
           }
           private static <T> T getFieldValue(Class<?> srcClazz, String fieldName, Object owner, Class<T> dstClazz) throws Exception {
                   Field field = srcClazz.getDeclaredField(fieldName);
                   field.setAccessible(true);
                   return dstClazz.cast(field.get(owner));
           }

   }
   ```

   更多语言请参考[dingtalk-callback-Crypto](https://github.com/open-dingtalk/dingtalk-callback-Crypto?spm=ding_open_doc.document.0.0.23455f66h4kWO2)。
2. 编写 HTTP 推送服务端代码：

   1. 接收事件消息：

      | **配置项** | **描述** |
      | --- | --- |
      | msg\_signature | 消息体签名。 |
      | timestamp | 时间戳。 |
      | nonce | 随机字符串 |
      | json | 加密事件数据体。 |

      ```
      import com.alibaba.fastjson.JSONObject;
      import org.springframework.web.bind.annotation.RequestBody;
      import org.springframework.web.bind.annotation.RequestMapping;
      import org.springframework.web.bind.annotation.RequestParam;
      import org.springframework.web.bind.annotation.RestController;
      import java.util.Map;

      @RestController
      public class CallbackController {
        
        @PostMapping("{你注册的HTTP地址的urlpath}")
        public Map<String, String> callBack(
                  @RequestParam(value = "msg_signature", required = false) String msg_signature,
                  @RequestParam(value = "timestamp", required = false) String timeStamp,
                  @RequestParam(value = "nonce", required = false) String nonce,
                  @RequestBody(required = false) JSONObject json) {
          
          } 
      }
      ```
   2. 响应事件消息：

      > **[!NOTE]**
      >
      > 当你收到开放平台的POST验证请求时，你需要做解密处理，并在 **2500 ms** 内响应并返回。

      ```
      import com.alibaba.fastjson.JSON;
      import com.alibaba.fastjson.JSONObject;
      import org.slf4j.Logger;
      import org.slf4j.LoggerFactory;
      import org.springframework.web.bind.annotation.RequestBody;
      import org.springframework.web.bind.annotation.RequestMapping;
      import org.springframework.web.bind.annotation.RequestParam;
      import org.springframework.web.bind.annotation.RestController;

      import java.util.Map;

      @RestController
      public class CallbackController {

          private final Logger bizLogger = LoggerFactory.getLogger(getClass());
          @PostMapping("{你注册的HTTP地址的urlpath}")
          public Map<String, String> callBack(
                  @RequestParam(value = "msg_signature", required = false) String msg_signature,
                  @RequestParam(value = "timestamp", required = false) String timeStamp,
                  @RequestParam(value = "nonce", required = false) String nonce,
                  @RequestBody(required = false) JSONObject json) {
              try {
                  // 1. 从http请求中获取加解密参数

                  // 2. 使用加解密类型
                  // 2、调用订阅事件接口订阅的事件为企业级事件推送，此时OWNER_KEY为：开发者后台应用的Client ID（原企业内部应用 appKey )
                  DingCallbackCrypto callbackCrypto = new DingCallbackCrypto("<开发者后台配置的签名 token >", "<开发者后台配置的加密 aes_key>", "<OWNER_KEY>");
                  String encryptMsg = json.getString("encrypt");
                  String decryptMsg = callbackCrypto.getDecryptMsg(msg_signature, timeStamp, nonce, encryptMsg);

                  // 3. 反序列化回调事件json数据
                  JSONObject eventJson = JSON.parseObject(decryptMsg);
                  String eventType = eventJson.getString("EventType");

                  // 4. 根据EventType分类处理
                  if ("check_url".equals(eventType)) {
                      // 测试回调url的正确性
                      bizLogger.info("测试回调url的正确性");
                  } else if ("user_add_org".equals(eventType)) {
                      // 处理通讯录用户增加事件
                      bizLogger.info("发生了：" + eventType + "事件");
                  } else {
                      // 添加其他已注册的
                      bizLogger.info("发生了：" + eventType + "事件");
                  }

                  // 5. 返回success的加密数据
                  Map<String, String> successMap = callbackCrypto.getEncryptedMap("success");
                  return successMap;

              } catch (Exception e) {
                  e.printStackTrace();
              }
              return null;
          }
      }
      ```

      此时，你的 HTTP 推送服务端就已经开发完成了。你可以按照[配置 HTTP 推送（不推荐）](0003-configure-stream-push.md#58bfd87c4fupu)流程校验是否接入正确。

## **开发 SyncHTTP  模式**

### **前提条件**

1. 了解[配置 SyncHTTP 推送（不推荐）](0003-configure-stream-push.md#421584309ds03)流程。
2. 开发环境：

   - Maven 3
   - JDK ：1.8 及以上

### **操作步骤**

1. 接入事件消息加解密类：

   ```
   package com.dingtalk.open;

   import java.io.ByteArrayOutputStream;
   import java.nio.charset.Charset;
   import java.security.MessageDigest;
   import java.security.Permission;
   import java.security.PermissionCollection;
   import java.util.Arrays;
   import java.util.HashMap;
   import java.util.Map;
   import java.util.Random;
   import java.security.Security;
   import java.lang.reflect.Field;

   import javax.crypto.Cipher;
   import javax.crypto.spec.IvParameterSpec;
   import javax.crypto.spec.SecretKeySpec;

   import com.alibaba.fastjson.JSON;

   import org.apache.commons.codec.binary.Base64;

   public class DingCallbackCrypto {

       private static final Charset CHARSET = Charset.forName("utf-8");
       private static final Base64 base64 = new Base64();
       private byte[] aesKey;
       private String token;
       private String corpId;
       /**
        * ask getPaddingBytes key固定长度
        **/
       private static final Integer AES_ENCODE_KEY_LENGTH = 43;
       /**
        * 加密随机字符串字节长度
        **/
       private static final Integer RANDOM_LENGTH = 16;

       /**
        * 构造函数
        *
        * @param token          钉钉开放平台上，开发者设置的token
        * @param encodingAesKey 钉钉开放台上，开发者设置的EncodingAESKey
        * @param corpId         企业自建应用-事件订阅, 使用appKey
        *                       企业自建应用-注册回调地址, 使用corpId
        *                       第三方企业应用, 使用suiteKey
        *
        * @throws DingTalkEncryptException 执行失败，请查看该异常的错误码和具体的错误信息
        */
       public DingCallbackCrypto(String token, String encodingAesKey, String corpId) throws DingTalkEncryptException {
           if (null == encodingAesKey || encodingAesKey.length() != AES_ENCODE_KEY_LENGTH) {
               throw new DingTalkEncryptException(DingTalkEncryptException.AES_KEY_ILLEGAL);
           }
           this.token = token;
           this.corpId = corpId;
           aesKey = Base64.decodeBase64(encodingAesKey + "=");
       }

       public Map<String, String> getEncryptedMap(String plaintext) throws DingTalkEncryptException {
           return getEncryptedMap(plaintext, System.currentTimeMillis(), Utils.getRandomStr(16));
       }

       /**
        * 将和钉钉开放平台同步的消息体加密,返回加密Map
        *
        * @param plaintext 传递的消息体明文
        * @param timeStamp 时间戳
        * @param nonce     随机字符串
        * @return
        * @throws DingTalkEncryptException
        */
       public Map<String, String> getEncryptedMap(String plaintext, Long timeStamp, String nonce)
           throws DingTalkEncryptException {
           if (null == plaintext) {
               throw new DingTalkEncryptException(DingTalkEncryptException.ENCRYPTION_PLAINTEXT_ILLEGAL);
           }
           if (null == timeStamp) {
               throw new DingTalkEncryptException(DingTalkEncryptException.ENCRYPTION_TIMESTAMP_ILLEGAL);
           }
           if (null == nonce) {
               throw new DingTalkEncryptException(DingTalkEncryptException.ENCRYPTION_NONCE_ILLEGAL);
           }
           // 加密
           String encrypt = encrypt(Utils.getRandomStr(RANDOM_LENGTH), plaintext);
           String signature = getSignature(token, String.valueOf(timeStamp), nonce, encrypt);
           Map<String, String> resultMap = new HashMap<String, String>();
           resultMap.put("msg_signature", signature);
           resultMap.put("encrypt", encrypt);
           resultMap.put("timeStamp", String.valueOf(timeStamp));
           resultMap.put("nonce", nonce);
           return resultMap;
       }

       /**
        * 密文解密
        *
        * @param msgSignature 签名串
        * @param timeStamp    时间戳
        * @param nonce        随机串
        * @param encryptMsg   密文
        * @return 解密后的原文
        * @throws DingTalkEncryptException
        */
       public String getDecryptMsg(String msgSignature, String timeStamp, String nonce, String encryptMsg)
           throws DingTalkEncryptException {
           //校验签名
           String signature = getSignature(token, timeStamp, nonce, encryptMsg);
           if (!signature.equals(msgSignature)) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_SIGNATURE_ERROR);
           }
           // 解密
           String result = decrypt(encryptMsg);
           return result;
       }

       /*
        * 对明文加密.
        * @param text 需要加密的明文
        * @return 加密后base64编码的字符串
        */
       private String encrypt(String random, String plaintext) throws DingTalkEncryptException {
           try {
               byte[] randomBytes = random.getBytes(CHARSET);
               byte[] plainTextBytes = plaintext.getBytes(CHARSET);
               byte[] lengthByte = Utils.int2Bytes(plainTextBytes.length);
               byte[] corpidBytes = corpId.getBytes(CHARSET);
               ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
               byteStream.write(randomBytes);
               byteStream.write(lengthByte);
               byteStream.write(plainTextBytes);
               byteStream.write(corpidBytes);
               byte[] padBytes = PKCS7Padding.getPaddingBytes(byteStream.size());
               byteStream.write(padBytes);
               byte[] unencrypted = byteStream.toByteArray();
               byteStream.close();
               Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
               SecretKeySpec keySpec = new SecretKeySpec(aesKey, "AES");
               IvParameterSpec iv = new IvParameterSpec(aesKey, 0, 16);
               cipher.init(Cipher.ENCRYPT_MODE, keySpec, iv);
               byte[] encrypted = cipher.doFinal(unencrypted);
               String result = base64.encodeToString(encrypted);
               return result;
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_ENCRYPT_TEXT_ERROR);
           }
       }

       /*
        * 对密文进行解密.
        * @param text 需要解密的密文
        * @return 解密得到的明文
        */
       private String decrypt(String text) throws DingTalkEncryptException {
           byte[] originalArr;
           try {
               // 设置解密模式为AES的CBC模式
               Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
               SecretKeySpec keySpec = new SecretKeySpec(aesKey, "AES");
               IvParameterSpec iv = new IvParameterSpec(Arrays.copyOfRange(aesKey, 0, 16));
               cipher.init(Cipher.DECRYPT_MODE, keySpec, iv);
               // 使用BASE64对密文进行解码
               byte[] encrypted = Base64.decodeBase64(text);
               // 解密
               originalArr = cipher.doFinal(encrypted);
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_DECRYPT_TEXT_ERROR);
           }

           String plainText;
           String fromCorpid;
           try {
               // 去除补位字符
               byte[] bytes = PKCS7Padding.removePaddingBytes(originalArr);
               // 分离16位随机字符串,网络字节序和corpId
               byte[] networkOrder = Arrays.copyOfRange(bytes, 16, 20);
               int plainTextLegth = Utils.bytes2int(networkOrder);
               plainText = new String(Arrays.copyOfRange(bytes, 20, 20 + plainTextLegth), CHARSET);
               fromCorpid = new String(Arrays.copyOfRange(bytes, 20 + plainTextLegth, bytes.length), CHARSET);
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_DECRYPT_TEXT_LENGTH_ERROR);
           }

           // corpid不相同的情况
           if (!fromCorpid.equals(corpId)) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_DECRYPT_TEXT_CORPID_ERROR);
           }
           return plainText;
       }

       /**
        * 数字签名
        *
        * @param token     isv token
        * @param timestamp 时间戳
        * @param nonce     随机串
        * @param encrypt   加密文本
        * @return
        * @throws DingTalkEncryptException
        */
       public String getSignature(String token, String timestamp, String nonce, String encrypt)
           throws DingTalkEncryptException {
           try {
               String[] array = new String[] {token, timestamp, nonce, encrypt};
               Arrays.sort(array);
               System.out.println(JSON.toJSONString(array));
               StringBuffer sb = new StringBuffer();
               for (int i = 0; i < 4; i++) {
                   sb.append(array[i]);
               }
               String str = sb.toString();
               System.out.println(str);
               MessageDigest md = MessageDigest.getInstance("SHA-1");
               md.update(str.getBytes());
               byte[] digest = md.digest();

               StringBuffer hexstr = new StringBuffer();
               String shaHex = "";
               for (int i = 0; i < digest.length; i++) {
                   shaHex = Integer.toHexString(digest[i] & 0xFF);
                   if (shaHex.length() < 2) {
                       hexstr.append(0);
                   }
                   hexstr.append(shaHex);
               }
               return hexstr.toString();
           } catch (Exception e) {
               throw new DingTalkEncryptException(DingTalkEncryptException.COMPUTE_SIGNATURE_ERROR);
           }
       }

       public static class Utils {
           public Utils() {
           }

           public static String getRandomStr(int count) {
               String base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
               Random random = new Random();
               StringBuffer sb = new StringBuffer();

               for (int i = 0; i < count; ++i) {
                   int number = random.nextInt(base.length());
                   sb.append(base.charAt(number));
               }

               return sb.toString();
           }

           public static byte[] int2Bytes(int count) {
               byte[] byteArr = new byte[] {(byte)(count >> 24 & 255), (byte)(count >> 16 & 255), (byte)(count >> 8 & 255),
                   (byte)(count & 255)};
               return byteArr;
           }

           public static int bytes2int(byte[] byteArr) {
               int count = 0;

               for (int i = 0; i < 4; ++i) {
                   count <<= 8;
                   count |= byteArr[i] & 255;
               }

               return count;
           }
       }

       public static class PKCS7Padding {
           private static final Charset CHARSET = Charset.forName("utf-8");
           private static final int BLOCK_SIZE = 32;

           public PKCS7Padding() {
           }

           public static byte[] getPaddingBytes(int count) {
               int amountToPad = 32 - count % 32;
               if (amountToPad == 0) {
                   amountToPad = 32;
               }

               char padChr = chr(amountToPad);
               String tmp = new String();

               for (int index = 0; index < amountToPad; ++index) {
                   tmp = tmp + padChr;
               }

               return tmp.getBytes(CHARSET);
           }

           public static byte[] removePaddingBytes(byte[] decrypted) {
               int pad = decrypted[decrypted.length - 1];
               if (pad < 1 || pad > 32) {
                   pad = 0;
               }

               return Arrays.copyOfRange(decrypted, 0, decrypted.length - pad);
           }

           private static char chr(int a) {
               byte target = (byte)(a & 255);
               return (char)target;
           }
       }

       public static class DingTalkEncryptException extends Exception {
           public static final int SUCCESS = 0;
           public static final int ENCRYPTION_PLAINTEXT_ILLEGAL = 900001;
           public static final int ENCRYPTION_TIMESTAMP_ILLEGAL = 900002;
           public static final int ENCRYPTION_NONCE_ILLEGAL = 900003;
           public static final int AES_KEY_ILLEGAL = 900004;
           public static final int SIGNATURE_NOT_MATCH = 900005;
           public static final int COMPUTE_SIGNATURE_ERROR = 900006;
           public static final int COMPUTE_ENCRYPT_TEXT_ERROR = 900007;
           public static final int COMPUTE_DECRYPT_TEXT_ERROR = 900008;
           public static final int COMPUTE_DECRYPT_TEXT_LENGTH_ERROR = 900009;
           public static final int COMPUTE_DECRYPT_TEXT_CORPID_ERROR = 900010;
           private static Map<Integer, String> msgMap = new HashMap();
           private Integer code;

           static {
               msgMap.put(0, "成功");
               msgMap.put(900001, "加密明文文本非法");
               msgMap.put(900002, "加密时间戳参数非法");
               msgMap.put(900003, "加密随机字符串参数非法");
               msgMap.put(900005, "签名不匹配");
               msgMap.put(900006, "签名计算失败");
               msgMap.put(900004, "不合法的aes key");
               msgMap.put(900007, "计算加密文字错误");
               msgMap.put(900008, "计算解密文字错误");
               msgMap.put(900009, "计算解密文字长度不匹配");
               msgMap.put(900010, "计算解密文字corpid不匹配");
           }

           public Integer getCode() {
               return this.code;
           }

           public DingTalkEncryptException(Integer exceptionCode) {
               super((String)msgMap.get(exceptionCode));
               this.code = exceptionCode;
           }
       }
       static {
                   try {
                           Security.setProperty("crypto.policy", "limited");
                           RemoveCryptographyRestrictions();
                   } catch (Exception var1) {
                   }

           }
           private static void RemoveCryptographyRestrictions() throws Exception {
                   Class<?> jceSecurity = getClazz("javax.crypto.JceSecurity");
                   Class<?> cryptoPermissions = getClazz("javax.crypto.CryptoPermissions");
                   Class<?> cryptoAllPermission = getClazz("javax.crypto.CryptoAllPermission");
                   if (jceSecurity != null) {
                           setFinalStaticValue(jceSecurity, "isRestricted", false);
                           PermissionCollection defaultPolicy = (PermissionCollection)getFieldValue(jceSecurity, "defaultPolicy", (Object)null, PermissionCollection.class);
                           if (cryptoPermissions != null) {
                                   Map<?, ?> map = (Map)getFieldValue(cryptoPermissions, "perms", defaultPolicy, Map.class);
                                   map.clear();
                           }

                           if (cryptoAllPermission != null) {
                                   Permission permission = (Permission)getFieldValue(cryptoAllPermission, "INSTANCE", (Object)null, Permission.class);
                                   defaultPolicy.add(permission);
                           }
                   }

           }
           private static Class<?> getClazz(String className) {
                   Class clazz = null;

                   try {
                           clazz = Class.forName(className);
                   } catch (Exception var3) {
                   }

                   return clazz;
           }
           private static void setFinalStaticValue(Class<?> srcClazz, String fieldName, Object newValue) throws Exception {
                   Field field = srcClazz.getDeclaredField(fieldName);
                   field.setAccessible(true);
                   Field modifiersField = Field.class.getDeclaredField("modifiers");
                   modifiersField.setAccessible(true);
                   modifiersField.setInt(field, field.getModifiers() & -17);
                   field.set((Object)null, newValue);
           }
           private static <T> T getFieldValue(Class<?> srcClazz, String fieldName, Object owner, Class<T> dstClazz) throws Exception {
                   Field field = srcClazz.getDeclaredField(fieldName);
                   field.setAccessible(true);
                   return dstClazz.cast(field.get(owner));
           }

   }
   ```

   更多语言请参考[dingtalk-callback-Crypto](https://github.com/open-dingtalk/dingtalk-callback-Crypto?spm=ding_open_doc.document.0.0.23455f66h4kWO2)。
2. 编写 SyncHTTP 推送服务端代码：

   1. 接收事件消息：

      | **配置项** | **描述** |
      | --- | --- |
      | msg\_signature | 消息体签名。 |
      | timestamp | 时间戳。 |
      | nonce | 随机字符串 |
      | json | 加密事件数据体。 |

      ```
      import com.alibaba.fastjson.JSONObject;
      import org.springframework.web.bind.annotation.RequestBody;
      import org.springframework.web.bind.annotation.RequestMapping;
      import org.springframework.web.bind.annotation.RequestParam;
      import org.springframework.web.bind.annotation.RestController;
      import java.util.Map;

      @RestController
      public class CallbackController {
        
        @PostMapping("{你注册的HTTP地址的urlpath}")
        public Map<String, String> callBack(
                  @RequestParam(value = "msg_signature", required = false) String msg_signature,
                  @RequestParam(value = "timestamp", required = false) String timeStamp,
                  @RequestParam(value = "nonce", required = false) String nonce,
                  @RequestBody(required = false) JSONObject json) {
          
          } 
      }
      ```
   2. 响应事件消息：

      > **[!NOTE]**
      >
      > 当你收到开放平台的POST验证请求时，你需要做解密处理，并在 **2500 ms** 内响应并返回。

      ```
      import com.alibaba.fastjson.JSON;
      import com.alibaba.fastjson.JSONObject;
      import org.slf4j.Logger;
      import org.slf4j.LoggerFactory;
      import org.springframework.web.bind.annotation.RequestBody;
      import org.springframework.web.bind.annotation.RequestMapping;
      import org.springframework.web.bind.annotation.RequestParam;
      import org.springframework.web.bind.annotation.RestController;

      import java.util.Map;

      @RestController
      public class CallbackController {

          private final Logger bizLogger = LoggerFactory.getLogger(getClass());
          @PostMapping("{你注册的HTTP地址的urlpath}")
          public Map<String, String> callBack(
                  @RequestParam(value = "msg_signature", required = false) String msg_signature,
                  @RequestParam(value = "timestamp", required = false) String timeStamp,
                  @RequestParam(value = "nonce", required = false) String nonce,
                  @RequestBody(required = false) JSONObject json) {
              try {
                  // 1. 从http请求中获取加解密参数

                  // 2. 使用加解密类型
                  // 2、调用订阅事件接口订阅的事件为企业级事件推送，此时OWNER_KEY为：开发者后台应用的Client ID（原企业内部应用 appKey )
                  DingCallbackCrypto callbackCrypto = new DingCallbackCrypto("<开发者后台配置的签名 token >", "<开发者后台配置的加密 aes_key>", "<OWNER_KEY>");
                  String encryptMsg = json.getString("encrypt");
                  String decryptMsg = callbackCrypto.getDecryptMsg(msg_signature, timeStamp, nonce, encryptMsg);

                  // 3. 反序列化回调事件json数据
                  JSONObject eventJson = JSON.parseObject(decryptMsg);
                  String eventType = eventJson.getString("EventType");

                  // 4. 根据EventType分类处理
                  if ("check_url".equals(eventType)) {
                      // 测试回调url的正确性
                      bizLogger.info("测试回调url的正确性");
                  } else if ("user_add_org".equals(eventType)) {
                      // 处理通讯录用户增加事件
                      bizLogger.info("发生了：" + eventType + "事件");
                  } else {
                      // 添加其他已注册的
                      bizLogger.info("发生了：" + eventType + "事件");
                  }

                  // 5. 返回success的加密数据
                  Map<String, String> successMap = callbackCrypto.getEncryptedMap("success");
                  return successMap;

              } catch (Exception e) {
                  e.printStackTrace();
              }
              return null;
          }
      }
      ```
