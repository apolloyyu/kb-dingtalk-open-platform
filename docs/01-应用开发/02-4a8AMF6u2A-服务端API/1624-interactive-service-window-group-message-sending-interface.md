---
title: "消息群发"
source_url: "https://open.dingtalk.com/document/development/interactive-service-window-group-message-sending-interface"
namespace: "development"
slug: "interactive-service-window-group-message-sending-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 互动服务窗 > 消息群发"
doc_id: "1jn5JsEH0T"
updated_at: "2025-10-30 10:37:28"
---

> Source: https://open.dingtalk.com/document/development/interactive-service-window-group-message-sending-interface
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 互动服务窗 > 消息群发
> Updated: 2025-10-30 10:37:28

# 消息群发

调用本接口群发消息。

> **[!IMPORTANT]**
>
> - 为提升接口的使用体验，已经对该接口进行了升级：
>
>   - 如未使用本接口，推荐使用[消息群发](0826-api-sendmessage.md)新的接口；
>   - 如已经使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。
> - 使用dep\_id\_list或is\_to\_all方式做大规模人群推送时，选中人数上限为10万人。如果超过此上限，群发失败，群发任务不会执行。
> - 在多人推送的情况下，同一天只会收到一条相同的内容（消息去重机制）。单人定向推送（只填一个userid）时，没有此保护机制，注意避免重复推送。
> - 出于系统保护的考虑，我们对接口的调用做了频率限制，详情请参考[调用频率限制](0012-call-frequency-limit.md)。
> - 接口调用成功，不代表所有接收人立马收到消息，根据系统拥堵情况收到时间可能会有一定的延迟。

![iShot2021-12-21 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3188891461/p372207.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 企业内部服务号消息权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.message.mass.send) |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/message/mass/send`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| media\_id | String | 否 | P16mHftLYX8iE | 消息卡片素材id。  **[!NOTE]**  当参数msg\_type为news\_card、image类型时，该参数为必填项。 |
| is\_to\_all | Boolean | 是 | false | 是否群发给组织下所有人：   - **true**：是 - **false**：否 |
| msg\_type | String | 是 | text | 消息类型：   - **text**：文本类型，文本内容填在text\_content字段中 - **news\_card**：消息卡片，可以通过[查询图文卡片列表](0824-query-message-card-list.md)接口获取media\_id - **image**：图片类型，可以通过[上传媒体文件](0646-upload-media-files.md)接口获media\_id - **markdown**：markdown消息，需要设置msg\_body中markdown对象的相关参数 - **action\_card**：action\_card卡片消息，需要设置msg\_body中action\_card对象的相关参数 - **single\_news\_card**：新样式的消息卡片，可通过[上传媒体文件](0646-upload-media-files.md)接口获取，只支持发送一个文章   **[!NOTE]**  当你使用 markdown 或 action\_card 类型时，推荐图片比例为 16:9。如果不使用该比例，则图片可能显示不完整。 |
| text\_content | String | 否 | hello | 文本内容，当msg\_type为text时有效。 |
| uuid | String | 是 | 48566508-3f35 | 调用时填写随机生成的UUID，防止消息重复发送。 |
| userid\_list | String | 否 | user1,user2 | 接收者的用户userid列表，列表最大长度1000。 |
| dep\_id\_list | String | 否 | 1958658,2324553 | 接收者的部门id列表，接收者是部门id下（包括子部门下）的所有用户，列表最大长度1000。 |
| roleIds | String | 否 | 1958658,2324553 | 接收者角色roleId列表，列表最大长度1000。 |
| allow\_comment | Boolean | 否 | true | 是否允许评论，仅在消息卡片(msg\_type=news\_card)、卡片消息(msg\_type=single\_news\_card)类型时生效。 |
| comment\_type | Number | 否 | 1 | 评论类型：   - **0**：普通评论 - **1**：精选评论，仅在允许评论时有效 |
| show\_homepage | Number | 否 | 0 | 消息是否在主页展示：   - **0**：不展示 - **1**：展示 |
| is\_preview | Boolean | 否 | true | 是否预览推送，预览推送只会发给单个用户，并且内容链接24小时后可能会失效。  **[!NOTE]**  取值为**true**时，**userid\_list**不能为空。 |
| msg\_body | MessageBody | 否 |  | 消息体。当msg\_type设置为markdown时，必须传入markdown对象的相关参数；当msg\_type设置为action\_card时，必须传入action\_card对象的相关参数。 |
| markdown | Markdown | 否 |  | markdown消息。 |
| text | String | 否 | markdown text | markdown格式的消息，建议5000字符以内。  **[!NOTE]**  当msg\_type设置为markdown时，该字段为必填项。 |
| title | String | 否 | title | 首屏会话透出的展示内容。  **[!NOTE]**  当msg\_type设置为markdown时，该字段为必填项。 |
| action\_card | ActionCard | 否 |  | action\_card卡片消息。 |
| btn\_orientation | String | 否 | 0 | 使用独立跳转ActionCard样式时的按钮排列方式：   - **0**：竖直排列 - **1**：横向排列   **[!NOTE]**  必须与button\_list同时设置。 |
| single\_title | String | 否 | single title | 使用整体跳转ActionCard样式时的标题，最长20个字符。  **[!NOTE]**  必须与single\_url同时设置。 |
| markdown | String | 否 | markdown text | 消息内容，支持markdown，语法请参考[markdown消息](0775-message-types-and-data-format.md#section-z2d-ytu-j5z)。建议1000个字符以内。 |
| button\_list | Button[] | 否 |  | 使用独立跳转ActionCard样式时的按钮列表。  **[!NOTE]**  必须与btn\_orientation同时设置。 |
| title | String | 否 | btn\_title1 | 使用独立跳转ActionCard样式时的按钮的标题，最长20个字符。 |
| action\_url | String | 否 | btn\_action\_url1 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| single\_url | String | 否 | https://dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| title | String | 否 | title | 透出到会话列表和通知的文案，最长64个字符。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| task\_id | String | 106689 | 推送任务id。 |
| request\_id | String | 15x4w8vuaw2a | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/message/mass/send?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "is_to_all": false, 
        "dep_id_list":"1958658,2324553",
        "unionid": "IlrIsTHaiSYXluZP61h0zxgiEiE", 
        "is_preview": true, 
        "text_content": "hello", 
        "msg_body": {
                "action_card": {
                        "single_url": "https://dingtalk.com", 
                        "button_list": {
                                "action_url": "btn_action_url1", 
                                "title": "btn_title1"
                        }, 
                        "btn_orientation": "0", 
                        "single_title": "single title", 
                        "markdown": "markdown text", 
                        "title": "title"
                }, 
                "markdown": {
                        "text": "markdown text", 
                        "title": "title"
                }
        }, 
        "media_id": "", 
        "msg_type": "action_card", 
        "uuid": "48566508-3fdsfsfdgdsd", 
        "userid_list": "10203029011219896,manager4220"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/mass/send");
OapiMessageMassSendRequest req = new OapiMessageMassSendRequest();
req.setUnionid("jYdrJoCmTo0iE");
req.setMediaId("P16mHftLYX8iE");
req.setIsToAll(false);
req.setMsgType("text");
req.setTextContent("hello");
req.setUuid("48566508-3f35");
req.setUseridList("user1,user2");
req.setDepIdList("1958658,2324553");
req.setIsPreview(true);
Markdown markdown = new Markdown();
markdown.setText("markdown text");
markdown.setTitle("title");
messageBody.setMarkdown(markdown);
ActionCard actionCard = new ActionCard();
actionCard.setBtnOrientation("0");
actionCard.setSingleTitle("single title");
actionCard.setMarkdown("markdown text");
List<Button> buttons = new ArrayList<Button>();
Button button = new Button();
buttons.add(button);
button.setTitle("btn_title1");
button.setActionUrl("btn_action_url1");
actionCard.setButtonList(buttons);
actionCard.setSingleUrl("https://dingtalk.com");
actionCard.setTitle("title");
messageBody.setActionCard(actionCard);
req.setMsgBody(messageBody);
OapiMessageMassSendResponse rsp = client.execute(req, access_token);
```

**返回示例**

```
{
        "errcode":0,
        "request_id":"15x4w8vuaw2a",
        "task_id":"msgP9aYVMkfTvWGmr+VabHsyQ=="
}
```

## 消息类型与数据格式

- **text类型**

  ```
  {
          "is_to_all": false, 
         "dep_id_list":[1958658,2324553],
          "unionid": "IlrIsTHaiSYXluZP61h0zxgiEiE", 
          "is_preview": true, 
          "text_content": "hello", 
          "msg_type": "text", 
          "uuid": "48566508-3f35", 
          "userid_list": "user1,user2"
  }
  ```
- **news\_card类型**

  ```
  {
          "is_to_all": false, 
          "dep_id_list":[1958658,2324553],
          "unionid": "IlrIsTHaiSYXluZP61h0zxgiEiE", 
          "is_preview": true, 
          "media_id": "cardDHndhMAowusiE", 
          "msg_type": "news_card", 
          "uuid": "48566508-3f35", 
          "userid_list": "user1,user2"
  }
  ```
- **image类型**

  ```
  {
          "is_to_all": false, 
          "dep_id_list":[1958658,2324553],
          "unionid": "IlrIsTHaiSYXluZP61h0zxgiEiE", 
          "is_preview": true, 
          "media_id": "cardDHndhMAowusiE", 
          "msg_type": "image", 
          "uuid": "48566508-3f35", 
          "userid_list": "user1,user2"
  }
  ```
- **markdown类型**

  ```
  {
          "is_to_all": false, 
          "dep_id_list":[1958658,2324553],
          "unionid": "IlrIsTHaiSYXluZP61h0zxgiEiE", 
          "is_preview": true, 
          "text_content": "hello", 
          "msg_body": {
                   "markdown": {
                          "text": "markdown text", 
                          "title": "title"
                  }
          }, 
          "msg_type": "markdown", 
          "uuid": "48566508-3f35", 
          "userid_list": "user1,user2"
  }
  ```
- **action\_card类型**

  ```
  {
          "is_to_all": false, 
          "dep_id_list": [
                  1958658, 
                  2324553
          ], 
          "unionid": "IlrIsTHaiSYXluZP61h0zxgiEiE", 
          "is_preview": true, 
          "text_content": "hello", 
          "msg_body": {
                  "action_card": {
                          "single_url": "https://dingtalk.com", 
                          "button_list": {
                                  "action_url": "btn_action_url1", 
                                  "title": "btn_title1"
                          }, 
                          "btn_orientation": "0", 
                          "single_title": "single title", 
                          "markdown": "markdown text", 
                          "title": "title"
                  }
          }, 
          "media_id": "cardDHndhMAowusiE", 
          "msg_type": "action_card", 
          "uuid": "48566508-3f35", 
          "userid_list": "user1,user2"
  }
  ```

## 错误码

| **错误码** | **说明** | **排查方法** |
| --- | --- | --- |
| 800003 | unionid不合法 | 传入有效的服务号unionid。 |
| 800013 | 群发消息太过频繁，请稍后再试 | 调整发送频次，稍后重试。 |
| 800014 | 群发消息次数超过今日限制 | 当天群发次数额度用完了，明天再来。 |
| 800017 | 向该用户发送单聊次数超过今日限制 | 单人定向推送时，单日限制100次。 |
| 800019 | 接收人列表为空 | 检查是否漏传了userid\_list和dep\_id\_list。 |
| 800020 | 消息参数错误 | 检查消息内容msg\_type、media\_id、text\_content、msg\_body等字段的格式是否正确。 |
| 800022 | userId列表不合法 | 检查传入的userid\_list是否有效。 |
| 800035 | uuid重复 | 检测到重复请求，该uuid已经用过了。 |
| 800038 | uuid不能为空 | 必填字段不能为空。 |
| 800039 | 用户列表长度超过限制 | 单次不能超过1000个。 |
| 800040 | 部门列表长度超过限制 | 单次不能超过1000个。 |
| 800055 | 服务号发消息qps超过限制 | 接口调用太快，稍后重试，注意重试时更换uuid。 |
| 800056 | 服务号发消息qpm超过限制 | 接口调用太快，稍后重试，注意重试时更换uuid。 |
| 800057 | 服务号今日发消息总人次超过限制：组织人数 \* 50 | 当天群发人次额度用完了，明天再来。 |
