---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/faq-robot"
namespace: "development"
slug: "faq-robot"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 常见问题"
doc_id: "1dPbE5wApv"
updated_at: "2026-08-04 09:07:26"
---

> Source: https://open.dingtalk.com/document/development/faq-robot
> Path: 应用开发 / 服务端 API / 即时通信 > 常见问题
> Updated: 2026-08-04 09:07:26

# 常见问题

本文介绍了钉钉即时通信IM的常见问题。

## **会话管理**

- **群URL是否有有效期，失效后怎么办？**

  答：群URL有有效期，默认有效期365天，群主、群名称等变动会触发群URL有效期过期。
- **建群时的UUID有什么用？**

  答：UUID主要用于控制建群请求的幂等性，防止手抖、重试时错误地重复创建群聊会话。
- **如何获取群聊的人员或群聊名称信息?**

  答：若群聊为企业内部群，可通过[查询群信息](0740-obtain-a-group-session.md)接口获取。
- **人员离职，普通群若要移除对应人员有自动化方案吗？**

  答：普通群暂无方案，因普通群中人员存在并无其他关联关系。目前只有企业内部群可以满足离职时自动离开本企业下的内部群。

## **消息通知**

- **工作通知发送OA消息为什么提示接受者不能超过5个人？**

  答：发送OA消息，如果设置了消息状态栏，此时系统需要为以后更新消息状态栏做准备，系统处理时长较长，因此一次请求最多只能给5个人发。详情参见[消息通知类型-OA消息](0775-message-types-and-data-format.md)。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3098765761/p556415.png)
- **如何获取工作通知发送失败的原因？**

  答：可以使用工作通知查询接口，查询工作通知的发送结果，发送结果中会有为什么没有接收到的展示，比如userId无效，发送过于频繁等。详情参见[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3098765761/p556420.png)
- **查询工作通知发送结果和更新工作通知为什么偶尔会出现失败？**

  答：常见的失败原因主要由于工作通知的结果查询和更新时间超出了工作通知发送的时限（24小时）。建议检查查询和更新时间是否在发送的有效时限内。
- **怎样控制链接在钉钉内打开还是在浏览器中打开？**

  答：你可以通过pc\_slide的属性来控制是否使用钉钉内浏览器打开链接

  - 在浏览器打开：`dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.baidu.com&pc_slide=false&title=title`。
  - 在钉钉内打开：`dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.baidu.com&pc_slide=true&title=title`。
  > **[!NOTE]**
  >
  > - **url**：为需要访问的地址，需要进行urlEnCode编码
  > - **pc\_slide**：控制是否在浏览器打开还是在钉钉内打开
  > - **title**：代表在钉钉内打开时左上角的文字，默认为:详情
- **工作通知消息接口调用失败**

  当调用工作通知消息接口出错时，请参考以下信息进行排查：

  1. 首先确认，是否是由于工作消息接口调用触发限制导致的：

     - 同一个应用相同消息的内容同一个用户一天只能接收一次。
     - 同一个微应用给同一个用户发送消息，企业内部开发方式一天不得超过500次。
     - 通过设置to\_all\_user参数全员推送消息，一天最多3次。
     - 同一个微应用给同一个用户发送消息，第三方企业应用一天不得超过 100 次。
  2. 调用[获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口，确认该工作消息是已经成功发送完成。
  3. 调用[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口，如果接收者在forbidden\_user\_id\_list中，则说明超出了工作消息发送次数限制，如果在failed\_user\_id\_list中，则说明接收者接收失败，重新发送。
  4. “消息链接在PC端工作台打开”这种跳转方式，只有工作消息类型为OA消息时才支持移动端跳转到应用。
- **发送工作通知与机器人发送消息选择图片类型的格式标准分别是什么？**

  答：如下表所示。

  | **机器人发送图片消息(图片尺寸单位px)** | | **工作通知发送图片消息(图片尺寸单位px)** | |
  | --- | --- | --- | --- |
  | **宽度** | **高度** | **宽度** | **高度** |
  | 宽度 ≤ 358 | 高度 ≤ 350 | 宽度 ≤ 338 | 高度 ≤ 677 |
  |  | | **发送后展示的尺寸：**336 × 189 | |
- **发送工作通知无报错，但接收人员未收到工作通知**

  答：[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)出现人员未收到工作通知，其可能原因包括但不限于以下几点：

  - 企业内部应用发送消息单次最多只能给5000人发送
  - 给同一员工一天只能发送一条内容相同的消息通知。
  - 企业内部应用每天给每个员工最多可发送500条消息通知
  - 企业内部应用发送消息时，每分钟最多有5000人可以接收到消息。

  此外，出现上述问题可以通过[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)来查询发送结果。
- **发送工作通知有哪些注意事项？**

  答：发送工作通知需注意以下几点：

  - 同一个应用相同消息的内容同一个用户一天只能接收一次。
  - 同一个微应用给同一个用户发送消息，企业内部开发方式一天不得超过500次。
  - 通过设置to\_all\_user参数全员推送消息，一天最多3次。
  - 同一个微应用给同一个用户发送消息，第三方企业应用一天不得超过 100 次。
  - 调用获取工作通知消息的发送进度接口，确认该工作消息是已经成功发送完成。
  - 调用获取工作通知消息的发送结果接口，如果接收者在forbidden\_user\_id\_list中，则说明超出了工作消息发送次数限制，如果在failed\_user\_id\_list中，则说明接收者接收失败，重新发送。
  - “消息链接在PC端工作台打开”这种跳转方式，只有工作消息类型为OA消息时才支持移动端跳转到应用。
- **PC端消息链接如何在侧边栏打开？**

  答：在PC客户端点击消息中的URL链接时，希望在PC客户端打开而不是外跳到浏览器，可参考[消息链接说明](0776-message-link-description.md)。

  示例：`dingtalk://dingtalkclient/page/link?url=http%3A%2F%2Fwww.dingtalk.com&pc_slide=true`

  **参数说明：**传参URL必须urlEncode(编码处理)，pc\_slide如果为true表示在PC客户端侧边栏打开, false或者不传表示用浏览器打开。

## **机器人**

- **如何编辑或者删除群插件？**

  答：群插件目前暂不支持编辑和删除功能。
- **修改机器人名称如何生效？**

  答：修改机器人名称生效的方式如下：

  - 修改机器人名称之后，添加到正式群聊会话中的机器人名称生效。
  - 若是点击调试进入的测试群“xxxxxxxx-TEST”，修改机器人名称后，则需要重新点击调试，否则修改名称不生效。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4243897661/p513154.png)
- **机器人上传头像在Windows端显示不清晰**

  答：遇到上述PC端显示机器人头像不清晰可能原因如下:

  这是由于PC端设备屏幕的分辨率导致，屏幕分辨率不同会造成显示效果不同。
- **调用机器人发送markdown消息时，空格与换行如何实现？**

  答：空格与换行实现方式如下：

  - **空格格式**：&nbsp 或 &#160 或 &#xA0
  - **换行格式**： \n

    > **[!IMPORTANT]**
    >
    > \n前后两个空格。
- **如何获取企业内部应用机器人robotCode？**

  答：登录[开发者后台](https://open-dev.dingtalk.com)，机器人在保存发布完成后，即可查看机器人robotCode。

  ![机器人robotCode](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0644209761/p603450.gif)
- **如何添加企业内部应用机器人入群？**

  > **[!NOTE]**
  >
  > 1. 企业内部机器人已完成保存发布。详情参见[配置企业机器人](../01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)。
  > 2. 企业内部企应用已完成发布，否则企业内部其他成员无法查看到该机器人，详情参见[发布应用](../01-XOnnmGCTbn-开发指南/0019-publish-dingtalk-application.md)。

  答：添加机器人入群方法如下：

  ![机器人入群](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1995598761/p596115.gif)
- **如何获取企业内部应用机器人Webhook的access\_token？**

  > **[!NOTE]**
  >
  > 机器人添加入群之后，才能查看机器人Webhook的access\_token值。

  答：获取Webhook的access\_token值的方式如下：

  ![Webhook中Token值](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1995598761/p596131.png)
- **如何手动在钉钉客户端创建一个企业内部群？**

  在机器人所在的企业，创建一个企业内部群。如已有该企业的企业内部群，此步骤可跳过。

  > **[!NOTE]**
  >
  > 例如“机器人”所在企业为“测试组织演示”，创建企业内部群必须为“测试组织演示[内部群]”。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4118309761/p604999.png)
