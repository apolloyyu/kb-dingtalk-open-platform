---
title: "自定义机器人发送群聊消息"
source_url: "https://open.dingtalk.com/document/development/custom-bot-to-send-group-chat-messages"
namespace: "development"
slug: "custom-bot-to-send-group-chat-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 使用教程 > 自定义机器人发送群聊消息"
doc_id: "kYnuQHsRz9"
updated_at: "2026-07-14 09:21:53"
---

> Source: https://open.dingtalk.com/document/development/custom-bot-to-send-group-chat-messages
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 使用教程 > 自定义机器人发送群聊消息
> Updated: 2026-07-14 09:21:53

# 自定义机器人发送群聊消息

本文档介绍使用自定义机器人发送群聊消息的步骤。

## 明确需求

在正式开发之前，你可以提前了解，本文档将帮助你使用自定义机器人 Webhook 对应的 [自定义机器人发送群消息](0717-custom-robots-send-group-messages.md)接口发送群聊消息。它将以加签的方式来演示自定义机器人的使用。为了帮助你快速上手，您可以尝试运行“快速体验”提供的示例 demo。这将帮助你对自定义机器人的使用有一个直观的体验。

## 前提条件

1. 完成[创建自定义机器人](../01-XOnnmGCTbn-开发指南/0081-custom-bot-creation-and-installation.md)流程。

   > 自定义机器人的安全设置选择**加签**的方式，详情参考[自定义机器人安全设置](../01-XOnnmGCTbn-开发指南/0082-customize-robot-security-settings.md)。
2. 完成[获取自定义机器人 Webhook 地址](../01-XOnnmGCTbn-开发指南/0083-obtain-the-webhook-address-of-a-custom-robot.md)流程。
3. 开发环境准备：

   | **开发环境** | **说明** |
   | --- | --- |
   | Java | - 已安装 JDK 1.8 及以上 - 已安装 Maven 3 |
   | Python | - Python 3 |

## **快速体验**

1. 你可以下载示例 demo：

   | **示例** | **说明** |
   | --- | --- |
   | Java | [custom-robot-group-message-quick-start-java.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250519/cvzdoy/custom-robot-group-message-quick-start-java.zip) |
   | Python | [custom-robot-group-message-quick-start-python.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250519/qspdnf/custom-robot-group-message-quick-start-python.zip) |
2. 启动示例 demo：

   | **类型** | **说明** |
   | --- | --- |
   | Java | 1. 修改 customRobotGroupMessage.java 的 main 方法参数：     - CUSTOM\_ROBOT\_TOKEN：机器人应用的 access\_token 的值，详情参考[获取自定义机器人 Webhook 地址](../01-XOnnmGCTbn-开发指南/0083-obtain-the-webhook-address-of-a-custom-robot.md)。  **[!NOTE]**  仅需填写 Webhook 地址后access\_token的值。不是整个webhook地址。  image    - SECRET：安全设置，加签密钥。详情参考[自定义机器人安全设置](../01-XOnnmGCTbn-开发指南/0082-customize-robot-security-settings.md)。    - （可选）USER\_ID：用户的 userId 信息，详情参考[用户 UserId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-aa9-zk1-os6)。  内部群：可以填写用户的 UserId 实现 @ 能力。  外部群：机器人调用 OpenAPI 发送消息时，无法实现 @ 能力。 2. 启动 main 方法。 3. 此时，你可以在群内看到自定义机器人发送的消息了。 |
   | Python | 1. 在当前文件的目录下，输入启动命令：`python3 send_custom_robot_group_message.py --access_token="your custom robot token" --secret="your custom robot secret" --userid="you need @ group user's userid"`。  注意替换机器人 webhook 的 access\_token、机器人的加签 secret 和用户 userid，参数如何获取请参考 Java 中的说明。 2. 此时，你可以在群内看到自定义机器人发送的消息了。 |

## **操作步骤**

> 下方为 Java 示例，Python 示例请下载上方体验 demo。

1. 添加依赖项到工程的`pom.xml`文件。

   ```
    <dependencies>
           <dependency>
               <groupId>com.aliyun</groupId>
               <artifactId>alibaba-dingtalk-service-sdk</artifactId>
               <version>2.0.0</version>
           </dependency>

           <dependency>
               <groupId>commons-codec</groupId>
               <artifactId>commons-codec</artifactId>
               <version>1.11</version>
           </dependency>
       </dependencies>
   ```
2. 创建 main 方法，并启动。

   ```
   import com.dingtalk.api.DefaultDingTalkClient;
   import com.dingtalk.api.DingTalkClient;
   import com.dingtalk.api.request.OapiRobotSendRequest;
   import com.dingtalk.api.response.OapiRobotSendResponse;
   import com.taobao.api.ApiException;
   import org.apache.commons.codec.binary.Base64;

   import javax.crypto.Mac;
   import javax.crypto.spec.SecretKeySpec;
   import java.io.UnsupportedEncodingException;
   import java.net.URLEncoder;
   import java.security.InvalidKeyException;
   import java.security.NoSuchAlgorithmException;
   import java.util.Arrays;

   public class customRobotGroupMessage {

       public static final String CUSTOM_ROBOT_TOKEN = "<your custom robot token>";

       public static final String USER_ID= "<you need @ group user's userId>";

       public static final String SECRET = "<your custom robot SECRET>";

       public static void main(String[] args) {
           try {
               Long timestamp = System.currentTimeMillis();
               System.out.println(timestamp);
               String secret = SECRET;
               String stringToSign = timestamp + "\n" + secret;
               Mac mac = Mac.getInstance("HmacSHA256");
               mac.init(new SecretKeySpec(secret.getBytes("UTF-8"), "HmacSHA256"));
               byte[] signData = mac.doFinal(stringToSign.getBytes("UTF-8"));
               String sign = URLEncoder.encode(new String(Base64.encodeBase64(signData)),"UTF-8");
               System.out.println(sign);

               //sign字段和timestamp字段必须拼接到请求URL上，否则会出现 310000 的错误信息
               DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/robot/send?sign="+sign+"&timestamp="+timestamp);
               OapiRobotSendRequest req = new OapiRobotSendRequest();
               /**
                * 发送文本消息
                */
               //定义文本内容
               OapiRobotSendRequest.Text text = new OapiRobotSendRequest.Text();
               text.setContent("钉钉，让进步发生");
               //定义 @ 对象
               OapiRobotSendRequest.At at = new OapiRobotSendRequest.At();
               at.setAtUserIds(Arrays.asList(USER_ID));
               //设置消息类型
               req.setMsgtype("text");
               req.setText(text);
               req.setAt(at);
               OapiRobotSendResponse rsp = client.execute(req, CUSTOM_ROBOT_TOKEN);
               System.out.println(rsp.getBody());
           } catch (ApiException e) {
               e.printStackTrace();
           } catch (UnsupportedEncodingException e) {
               throw new RuntimeException(e);
           } catch (NoSuchAlgorithmException e) {
               throw new RuntimeException(e);
           } catch (InvalidKeyException e) {
               throw new RuntimeException(e);
           }
       }
   }
   ```

   此时，你可以在群内看到自定义机器人发送的消息了。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3112993871/p768588.png)

## **常见问题**

### **调用频率限制**

由于消息发送太频繁会严重影响群的使用体验，因此自定义机器人发送消息的频率限制如下：

**每个机器人每分钟最多发送20条消息到群里，如果超过20条，会限流10分钟。**

> 如果你有大量发消息的场景（譬如系统监控报警）可以将这些信息进行整合，通过markdown消息以摘要的形式发送到群里。

## **相关文档**

- [自定义机器人安全设置](../01-XOnnmGCTbn-开发指南/0082-customize-robot-security-settings.md)
- [消息发送与接收类型](0699-robot-message-type.md)
- [自定义机器人发送群消息](0717-custom-robots-send-group-messages.md)
