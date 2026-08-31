---
title: "发送群助手消息"
source_url: "https://open.dingtalk.com/document/development/group-template-robot-message"
namespace: "development"
slug: "group-template-robot-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群助手 > 发送群助手消息"
doc_id: "zmELpYZKVk"
updated_at: "2026-07-14 09:22:07"
---

> Source: https://open.dingtalk.com/document/development/group-template-robot-message
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 场景群 > 群助手 > 发送群助手消息
> Updated: 2026-07-14 09:22:07

# 发送群助手消息

调用本接口，通过群模板定义的机器人向群内发送消息。

## **接口调用说明**

支持场景：基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send\_v2 |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| target\_open\_conversation\_id | String | 是 | cid9FTRQSLo+sK\*\*\*\*\*== | 群ID，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |
| msg\_template\_id | String | 是 | offical\_template\_test\_action\_card | 消息模板ID，详情参见下文场景群通用消息模板。 |
| msg\_param\_map | String | 否 | {\"text1\":\"hello\",\"text2\":\"world\"} | 消息模板内容替换参数，普通文本类型。  **[!NOTE]**  取值为Json格式的字符串。 |
| msg\_media\_id\_param\_map | String | 否 | {\"pic1\":\"@123\",\"pic2\":\"@456\"} | 消息模板内容替换参数，多媒体类型。  **[!NOTE]**  取值为Json格式的字符串。 |
| receiver\_user\_ids | String[] | 否 | "072\*\*\*\*\*,manager422\*\*\*\*\*" | 消息接收人userId列表，调用[查询群成员](0751-query-group-members.md)接口获取`member_user_ids`参数值。  **[!NOTE]**  不设置任何接收人则消息对群内所有成员可见。 |
| receiver\_union\_ids | String | 否 | "jHs\*\*\*\*\*,atc\*\*\*\*\*" | 消息接收人unionId列表，调用[查询用户详情](0056-query-user-details.md)接口获取`unionid`参数值。  **[!NOTE]**  不设置任何接收人则消息对群内所有成员可见。 |
| receiver\_mobiles | String | 否 | "137\*\*\*\*\*000,158\*\*\*\*\*000" | 消息接收人手机号列表，调用[查询用户详情](0056-query-user-details.md)接口获取`mobile`参数值。  **[!NOTE]**  不设置任何接收人则消息对群内所有成员可见。 |
| at\_mobiles | String | 否 | "137\*\*\*\*\*000" | @人的手机号列表，调用[查询用户详情](0056-query-user-details.md)接口获取`mobile`参数值。  **[!NOTE]**  一次调用最多支持50人。 |
| at\_users | String | 否 | "072\*\*\*\*\*" | @人的userid列表，调用[查询群成员](0751-query-group-members.md)接口获取`member_user_ids`参数值。  **[!NOTE]**  一次调用最多支持50人。 |
| is\_at\_all | Boolean | 否 | true | 是否@所有人：   - **true**：是 - **false**：否 |
| robot\_code | String | 是 | fTv5O\*\*\*\*\* | 机器人编码，登录[开发者后台 > 开放能力 > 场景群 > 机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)查看id。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=aca06xxxx0ccad06e' \
-d 'target_open_conversation_id=cid9FTRQSLo+sK*****==' \
-d 'msg_template_id=offical_template_test_action_card' \
-d 'robot_code=fTv5O*****' \
-d 'msg_param_map={\"title\":\"测试标题\",\"markdown\":\"# 测试内容\"}' \
-d 'receiver_user_ids=[\"072*****\",\"manager422*****\"]'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2");
OapiImChatScencegroupMessageSendV2Request req = new OapiImChatScencegroupMessageSendV2Request();
req.setMsgTemplateId("inner_app_template_markdown");
req.setIsAtAll(false);
req.setMsgParamMap("{\"title\":\"测试\",\"markdown_content\":\"# 测试内容 \n @180xxxx3120\"}");
req.setMsgMediaIdParamMap("{\"pic1\":\"@123\",\"pic2\":\"@456\"}");
req.setTargetOpenConversationId("cid9FTRQSLo+sK*****==");
req.setAtMobiles("137*****000");
req.setAtUsers("072*****");
req.setReceiverUserIds("072*****,manager422*****");
req.setReceiverUnionIds("jHs*****,atc*****");
req.setRobotCode("fTv5O*****");
OapiImChatScencegroupMessageSendV2Response rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiImChatScencegroupMessageSendV2Request("https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2")

req.target_open_conversation_id="123"
req.msg_template_id="123"
req.receiver_user_ids="123,456"
req.receiver_union_ids="789,100"
req.receiver_mobiles="13700000000,15800000000"
req.at_mobiles="1370000001,15800000001"
req.is_at_all=true
req.robot_code="123"
req.at_users="user1,user2"
req.at_union_ids="unionId1,unionId1"
try:
	resp= req.getResponse(access_token)
	print(resp)
except Exception,e:
	print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiImChatScencegroupMessageSendV2Request;
$req->setTargetOpenConversationId("123");
$req->setMsgTemplateId("123");
$req->setReceiverUserIds("123,456");
$req->setReceiverUnionIds("789,100");
$req->setReceiverMobiles("13700000000,15800000000");
$req->setAtMobiles("1370000001,15800000001");
$req->setIsAtAll("true");
$req->setRobotCode("123");
$req->setAtUsers("user1,user2");
$req->setAtUnionIds("unionId1,unionId1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2");
OapiImChatScencegroupMessageSendV2Request req = new OapiImChatScencegroupMessageSendV2Request();
req.TargetOpenConversationId = "cid9FTRQSLo+sK*****==";
req.MsgTemplateId = "offical_template_test_action_card";
req.RobotCode = "fTv5O*****";
req.MsgParamMap = "{\"title\":\"测试标题\",\"markdown\":\"# 测试内容\"}";
req.ReceiverUserIds = new List<string> { "072*****", "manager422*****" };

OapiImChatScencegroupMessageSendV2Response rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| open\_msg\_id | String | 36\*\*\*\*\* | processQueryKey，可用此key调用[查询企业机器人群聊消息用户已读状态](0722-chatbot-queries-the-read-status-of-a-message.md)接口获取消息已读状态。 |
| request\_id | String | 3mwsbk909ffe | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "open_msg_id": "36*****",
  "request_id": "3mwsbk909ffe"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40036 | 入参为空 | 根据接口要求，传入必要参数。 |
| 660001 | 群编码为空 | 请传入正确的群ID，可通过[创建群](https://open.dingtalk.com/document/orgapp/create-a-scene-group-v2)接口获取。 |
| 660002 | 机器人编码为空 | 请传入正确的机器人code。 |
| 660012 | 不允许往该群发送卡片 | 请检查该群是否正确启用了群模板，可通过[启用群模板](https://open.dingtalk.com/document/orgapp/enable-a-group-template)接口启用群模板。 |
| 660014 | 查无此机器人 | 请检查传入的群机器人编码是否正确。 |
| 660015 | 查无此场景群 | 请检查传入的openConversationId是否正确，可通过[创建群](https://open.dingtalk.com/document/orgapp/create-a-scene-group-v2)接口获取。 |
| 660016 | 机器人不可用 | 对应机器人已不可用（可能已被群管理员删除），请重新绑定群助手机器人。 |
| 660018 | 查询图片文件地址失败 | 请检查指定的图片mediaId是否正确，可通过[上传媒体文件](https://open.dingtalk.com/document/orgapp/upload-media-files)接口获取。 |
| 660020 | 重复的占位符KEY | 文本和多媒体占位符不能包含同名占位符，请修改消息内容中的占位符。 |
| 660022 | 接收人识别失败 | 请检查接收人参数是否错误，可通过[查询群成员](https://open.dingtalk.com/document/orgapp/query-group-members)接口获取。 |
| 660023 | 群编码解码失败 | 请检查群编码是否填写正确。 |
| 660024 | 查无此消息模板 | 请检查消息模板是否正确。 |
| 660025 | 消息模板渲染失败 | 请检查消息模板动参的入参是否合法。 |
| 660026 | 机器人发送消息失败 | 请重试。 |
| 660027 | 消息模板ID为空 | 请传入消息模板。 |
| -1 | 系统异常 | 重试后如果还是出现此错误，请在开发者后台提交工单。= |

## 通用消息模板

场景群发消息接口目前已支持官方通用测试模板，方便开发者接入体验。

### 企业内部应用

如果你的应用是企业内部应用，可以直接使用企业内部应用公共模板，可用的模板如下：

> 如果以下消息模板无法满足你的需求，可以使用[互动卡片](https://open.dingtalk.com/document/orgapp/overview-card)。

- 文本消息模板：**msg\_template\_id**取值为`inner_app_template_text`。

  传参示例如下：

  ```
  {
      "robot_code": "iuEkXlixxx1002",
      "target_open_conversation_id": "3mwsbxxxfe==",
      "msg_param_map": {
          "content": "测试消息~"
      },
      "msg_template_id": "inner_app_template_text"
  }
  ```
- 图片消息模板：**msg\_template\_id**取值为`inner_app_template_photo`。

  传参示例如下：

  ```
  {
      "robot_code": "iuEkXlixxx1002",
      "target_open_conversation_id": "3mwsbxxxfe==",
      "msg_media_id_param_map": {
          "img_media_id": "@lAjPDxxx"
      },
      "msg_template_id": "inner_app_template_photo"
  }
  ```
- markdown模板：**msg\_template\_id**取值为`inner_app_template_markdown`。

  传参示例如下：

  ```
  {
      "robot_code": "iuEkXlixxx1002",
      "target_open_conversation_id": "3mwsbxxxfe==",
      "msg_param_map": {
          "title": "标题",
          "markdown_content": "# 测试内容"
      },
      "msg_template_id": "inner_app_template_markdown"
  }
  ```
- actionCard模板：**msg\_template\_id**取值为`inner_app_template_action_card`。

  传参示例如下：

  ```
  {
      "robot_code": "iuEkXlixxx1002",
      "target_open_conversation_id": "3mwsbxxxfe==",
      "msg_param_map": {
          "title": "标题",
          "markdown": "# 测试内容",
          "btn_orientation": "1",
          "btn_title_1": "btn_title_1",
          "action_url_1": "dingtalk.com",
          "btn_title_2": "btn_title_1",
          "action_url_2": "dingtalk.com",
          "btn_title_3": "btn_title_1",
          "action_url_3": "dingtalk.com",
          "btn_title_4": "btn_title_1",
          "action_url_4": "dingtalk.com"
      },
      "msg_template_id": "inner_app_template_action_card"
  }
  ```

### 第三方企业应用

如果你的应用是三方企业应用，官方消息模板**：msg\_template\_id**取值为`offical_template_test_action_card`。

传参示例如下：

```
{
    "robot_code": "iuEkXlixxx1002",
    "target_open_conversation_id": "3mwsbxxxfe==",
    "msg_param_map": {
        "title": "会话列表显示",
        "markdown": "# 测试内容",
        "btn_orientation": "1",
        "btn_title_1": "btn_title_1",
        "action_url_1": "dingtalk.com",
        "btn_title_2": "btn_title_2",
        "action_url_2": "dingtalk.com",
        "btn_title_3": "btn_title_3",
        "action_url_3": "dingtalk.com",
        "btn_title_4": "btn_title_4",
        "action_url_4": "dingtalk.com"
    },
    "msg_template_id": "offical_template_test_action_card"
}
```

模板占位符Key值如下。

| 参数 | 说明 |
| --- | --- |
| title | 会话列表显示标题。 |
| markdown | 消息内容，支持markdown语法。 |
| btn\_orientation | 按钮排列方向，仅2个按钮时有效，传值为2时水平排列。 |
| btn\_title\_1 ~ btn\_title\_4 | 按钮文案，支持最多4个按钮，传空或不传则按钮不显示。 |
| action\_url\_1 ~ action\_url\_4 | 按钮跳转地址，支持最多4个按钮，传空或不传则按钮不显示。 |

以下为**官方通用测试模板**原文，后续可参考下附原文的格式提供定制需求，包括**自定义模板内容**和**占位符key**。

```
{
    "msgtype": "actionCard",
    "actionCard": {
        "title": "${title}",
        "text": "${markdown}     # 该消息仅用于场景群开发者测试",
        "btnOrientation": "${btn_orientation}",
        "btns": [
            {
                "title": "${btn_title_1}",
                "actionURL": "${action_url_1}"
            },
            {
                "title": "${btn_title_2}",
                "actionURL": "${action_url_2}"
            },
            {
                "title": "${btn_title_3}",
                "actionURL": "${action_url_3}"
            },
            {
                "title": "${btn_title_4}",
                "actionURL": "${action_url_4}"
            }
        ]
    }
}
```

消息效果如下图。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2448635161/p247693.png)
