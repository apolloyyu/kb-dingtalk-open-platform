---
title: "消息卡片发送及更新"
source_url: "https://open.dingtalk.com/document/development/message-card-sending-and-updating"
namespace: "development"
slug: "message-card-sending-and-updating"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "消息卡片发送及更新"
doc_id: "FvywjLsCVr"
updated_at: "2026-08-05 09:10:09"
---

> Source: https://open.dingtalk.com/document/development/message-card-sending-and-updating
> Path: 互动卡片 / 开发指南 / 消息卡片发送及更新
> Updated: 2026-08-05 09:10:09

# 消息卡片发送及更新

本文以审批卡片为例，展示从需求分析、模板搭建、字段绑定、创建投放到交互响应的完整端到端流程。

## **核心概念**

### 消息卡片发送及更新

以审批卡片为例，展示从需求分析 → 模板搭建 → 字段绑定 → 创建投放 → 交互响应的完整端到端流程。用户点击卡片可跳转详情页，点击底部按钮可快速完成"同意""拒绝"操作，卡片状态实时变更。

一个典型的审批卡片样式如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9022985871/p549542.png)

用户点击整个卡片可以跳转到审批的详情页面，点击卡片底部的按钮，则可以快速地完成"同意"、"拒绝"操作，同时卡片状态发生变更，按钮切换成"已同意"或"已拒绝"的样式：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9022985871/p549543.png)

此时按钮已不能再点击，但仍可以点击整个卡片进入到详情页面。

### 适用场景

- **审批流通知**：审批单提交后推送卡片，审批人直接在卡片上操作，结果实时更新。
- **任务协作**：任务分配、进度更新、完成确认等需要交互式反馈的业务通知。
- **业务告警与处置**：监控告警推送卡片，运维人员一键确认/忽略，卡片状态同步变更。

## 前置准备

在开始之前，请确保已完成以下准备工作：

- 了解[普通卡片模板](0001-card-template-building-and-publishing.md)搭建和发布流程。
- 了解[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)流程。
- 了解[卡片平台投放卡片实例](0005-card-delivery-instance-for-card-platform.md)流程。
- 已注册[卡片事件回调](0007-event-callback-card.md)（如需按钮交互）。

## **步骤一：分析需求并创建模板**

分析完上述审批卡片的交互需求后，即可在[钉钉卡片平台](https://open-dev.dingtalk.com/fe/card#/)上创建对应的卡片模板：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9022985871/p525141.png)

## **步骤二：搭建卡片模板布局**

从上面审批卡片的样式可以看出，卡片分为三个部分：

- 卡片头部区
- 卡片内容区
- 卡片操作区

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9022985871/p549544.png)

### **卡片头部区搭建**

卡片头部区的样式可以通过布局容器实现三栏布局。图片、文字以及标签分别放置在对应的布局中。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9022985871/p549545.png)

最左边的审批图标是固定尺寸的，因此对应的布局宽度可以设置成固定宽度：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524336.gif)

中间"审批"文字的宽度可能因不同客户端而有所差异，因此需要给文字及其对应布局设置为自适应宽度：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524347.gif)

最后的标签组件无需过多设置。配置完标签组件后，再整体调整各组件之间的间距及垂直居中即可：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524348.gif)

至此，卡片头部区搭建完成。

### **卡片内容区搭建**

内容区布局相对简单，上下两部分均由文本组件构成。区别在于：上方文本设置了加粗样式，下方文本使用小号字体并设置为灰色。中间部分由一个布局容器组成，内部放置两个文本布局。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9022985871/p549546.png)

设置中间文本内容时，只需注意将左侧布局和文本设置为自适应宽度，这样右侧文案就会紧贴左侧文案显示：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524414.gif)

### **卡片操作区搭建**

卡片操作区只有两个按钮，较为简单，直接使用「横排按钮」组件放置"同意""拒绝"两个按钮即可：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524989.gif)

至此，整个卡片模板的样式已全部搭建完成。

## **步骤三：定义模板字段并绑定数据**

上述步骤搭建的是一个静态卡片模板。为了让卡片能在业务系统中实际使用，需要将模板中的内容与真实业务数据关联起来，因此需要对卡片模板进行字段定义和数据绑定。

### 定义卡片模板变量字段

从该审批卡片的需求来看，卡片上存在动态变化的内容包括：

- 审批的二级模块
- 审批的标题
- 审批的内容项
- 审批的创建时间
- 审批的状态
- 审批的详情页链接

因此可以定义出该卡片的所有字段：

| **字段** | **变量类型** | **描述** |
| --- | --- | --- |
| brand | 字符串 | 审批二级模块的名称。 |
| title | 字符串 | 审批标题。 |
| contents | 对象数组 | 审批内容项。是一个对象数组，对象的结构在下方描述。 |
| contents[\*].label | 字符串 | 审批内容项的标题。 |
| contents[\*].text | 字符串 | 审批内容项的内容。 |
| date | 字符串 | 审批单的创建时间。 |
| status | 字符串 | 审批状态。 |
| detailUrl | 字符串 | 审批详情页的URL。 |

其中，为了让审批内容足够灵活，审批内容项使用对象数组来表达，而非使用单独的字段，这样便于后续进行内容扩展。

定义好字段后，将其录入到卡片模板搭建器的变量面板中：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525031.png)

录入完模板变量后，为了方便搭建时预览效果，可以在此时配置对应的变量 mock 数据：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525049.png)

### 绑定卡片模板变量

- **文本变量绑定**

  对于文本变量绑定，只需在文本组件中使用 `${变量}` 格式即可完成绑定：

  ![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5826269661/p525038.gif)

  审批内容项需要进行特殊处理。由于上一环节将内容项设置为对象数组结构，因此在模板搭建时需要相应调整：将搭建好的内容放入循环渲染容器中，同时为循环渲染容器绑定对应的对象数组，并为内容项绑定对应的循环字段：

  ![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525062.gif)

  在循环渲染容器中绑定文本内容时，绑定的变量格式为 `${loop.变量}`，该语法表示当前数据是从对象数组中取每一项的对应字段。

  此外，在编辑卡片模板时，循环渲染容器内的元素默认只显示一条内容。如需查看完整效果，可切换到预览模式。
- **按钮变量绑定**

  在当前审批卡片中，我们希望用户点击"同意"或"拒绝"后，卡片能切换到"已同意"或"已拒绝"状态，且按钮不再可点击。为实现该效果，需要新增两个按钮——"已同意"和"已拒绝"，并将它们分别设置为禁用状态：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525066.png)

  此时卡片会显示四个按钮。为了让按钮根据审批状态正确显示，需要对四个按钮分别配置"是否显示"属性，通过审批状态字段来控制按钮的显隐：

  - 当 `status` 字段值为 `pending` 时，表示尚未操作，显示"拒绝"和"同意"两个按钮。
  - 当 `status` 字段值为 `accept` 时，表示审批已通过，仅显示"已通过"按钮，其他按钮隐藏。
  - 当 `status` 字段值为 `reject` 时，表示审批已拒绝，仅显示"已拒绝"按钮，其他按钮隐藏。

    ![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525086.gif)
- **按钮点击事件绑定**

  对于卡片上的"同意"和"拒绝"按钮，我们希望用户点击后能直接在卡片上发起回调请求到业务系统，执行对应操作。因此需要对这两个按钮配置点击事件：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525091.png)

  除了将按钮的"点击事件类型"设置为"回传请求"外，还需定义回传参数。当按钮被点击时，回传给业务系统的参数中会携带这些额外参数（如上图所示的参数为 `{"action": "reject"}`），用于让业务系统区分当前执行的是什么操作。
- **卡片链接跳转绑定**

  最后需要对整个卡片配置跳转链接。我们希望用户点击除按钮以外的任意区域都能直接跳转到当前审批的详情页面。在搭建器中，只需选中卡片组件，在"事件"面板中设置"链接跳转"事件，并绑定对应的变量即可：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525088.png)

至此，卡片模板的搭建和配置已全部完成。

## **步骤四：**卡片创建及投放

卡片模板搭建完成并保存后，可调用[创建并投放卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)接口实现卡片投放 。以本次审批卡片为例，具体调用 API 的请求如下：

**HTTP请求示例：**

```
POST /v1.0/card/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fake_token
Content-Type:application/json

{
  "userId": "fake_user_id",
  "cardTemplateId": "fake_card_template_id",
  "outTrackId": "custom_biz_id",
  "openSpaceId": "fake_open_conversation_id",
  "cardData" : {
  	"cardParamMap": {
      "brand": "智能财务",
      "title": "朱小志提交的财务报销",
      "contents": [
        {
          "label": "报销类型",
          "text": "差旅费"
        },
        {
          "label": "报销金额",
          "text": "1000"
        },
        {
          "label": "报销理由",
          "text": "出差费用"
        }
      ],
      "date": "2022-05-22 21:20",
      "status": "pending",
      "detailUrl": "https://dingtalk.com"
    }
  },
  "imGroupOpenSpaceModel" : {
    "supportForward" : true,
    "lastMessageI18n" : {
      "zh_CN" : "朱小志提交的财务报销"
    }
  },
  "imGroupOpenDeliverModel" : {
    "robotCode": "fake_robot_code"
  }
}
```

其中各参数说明如下：

| **参数** | **说明** |
| --- | --- |
| userId | 创建该卡片的用户 ID。 |
| cardTemplateId | 卡片模板 ID，可在卡片编辑器创建模板时获取。 |
| outTrackId | 卡片的唯一 ID，需由业务侧维护。  在审批场景下可对应审批单 ID；后续如需更新卡片，也通过该 ID 进行操作。 |
| openSpaceId | 要投放的场域 ID。  在本例中需投放到群聊，因此对应群的 `openConversationId`。 |
| cardData | 当前卡片的数据，对应卡片模板上的变量字段。 |
| imGroupOpenSpaceModel | 群聊/单聊场域的场域配置信息，可设置卡片消息是否支持转发（`supportForward`）以及消息的 `lastMessage`。 |
| imGroupOpenDeliverModel | 群聊场域的投放配置信息，需设置当前卡片由哪个机器人发出（`robotCode`）。 |

调用接口成功后，即可在群聊中看到发送的卡片。

## **步骤五：响应用户点击操作**

### **回调请求格式**

完成上述步骤后，卡片即可正常发送到群聊中。但此时卡片上的按钮尚不具备交互能力，点击按钮不会有任何反应。

从前面的章节可以看到，我们为"同意"和"拒绝"按钮设置了"回传请求"事件。"回传请求"功能会在用户点击按钮时，主动调用卡片发送方提供的回调地址，并携带相关参数。但在使用该功能前，需先注册卡片的回调地址，详细注册方法请参考[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)文档。

当卡片有配置回调地址之后，此时用户点击“同意”按钮，钉钉卡片系统会向回调地址发送一个 HTTP 请求，同时带上以下参数：

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "custom_biz_id",
    "userId": "XXXXXX",
    "value": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]},\"params\":{\"action\":\"agree\"}}"
}
```

| **参数** | **说明** |
| --- | --- |
| corpId | 点击该按钮的用户所属组织 ID。 |
| outTrackId | 卡片的唯一 ID，与发送卡片时的 `outTrackId` 值一致。 |
| userId | 点击该按钮的用户 ID。 |
| value | 按钮的详细信息，是一个 JSON 字符串，包含`cardPrivateData`字段。 |

`value` 解析后的结构示例：

```
{
  "cardPrivateData": {
    "actionIds": ["1"],
    "params": {
      "action": "accept"
    }
  }
}
```

其中：

- `cardPrivateData.actionIds` 代表当前点击的按钮 ID。例如在本例中，"同意"按钮的 ID 为 1，因此 `actionIds` 的值为 `["1"]`。
- 如果在卡片模板上为按钮配置了回传参数，这些参数会出现在 `cardPrivateData.params` 中。
- 一般来说，业务系统可根据 `actionIds` 和 `params` 来判断用户点击的是哪个按钮，从而确定需要执行的操作。

### **回调响应格式**

为了让审批卡片显示"已同意"界面，需要在回调请求中返回新的卡片数据，使卡片界面得到更新：

```
{
  "cardUpdateOptions": {
    "updateCardDataByKey": true
  },
  "cardData": {
    "cardParamMap": {
      "status": "accept"
    }
  }
}
```

其中 `cardUpdateOptions.updateCardDataByKey` 表示此次更新卡片数据时，只更新指定的字段，其他未更新的字段保持原有值不变。返回新数据后，钉钉互动卡片会及时刷新为最新状态，至此完成了卡片状态更新的完整流程。

> **[!NOTE]**
>
> 需要注意的是，目前在卡片回传请求中更新 cardData 只会将公有数据下发给触发回传请求事件的用户，不会扩散给所有人。如果有需要协同更新所有卡片的需求，可以另外调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)接口进行公有数据的更新。更多事件回调相关请参考文档：[事件回调](0007-event-callback-card.md)。

## **效果展示**

| 待审批状态 | 已审批状态 |
| --- | --- |
| image | image |

## **相关内容**

如需了解更多互动卡片示例，请参考[互动卡片示例中心](https://github.com/open-dingtalk/dingtalk-card-examples)
