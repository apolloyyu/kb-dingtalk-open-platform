---
title: "接入流程"
source_url: "https://open.dingtalk.com/document/development/interactive-card-usage-example"
namespace: "development"
slug: "interactive-card-usage-example"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "搭建平台 > 高级版搭建平台 > 接入流程"
doc_id: "RMkJN3vKgN"
updated_at: "2026-08-07 14:53:32"
---

> Source: https://open.dingtalk.com/document/development/interactive-card-usage-example
> Path: 互动卡片 / 模板搭建卡片 / 搭建平台 > 高级版搭建平台 > 接入流程
> Updated: 2026-08-07 14:53:32

# 接入流程

为了让使用者更加直观地了解如何使用模板编辑器来搭建互动卡片，本文以审批卡片为例，完整展示从 0 到 1 的开发流程。通过本指南，开发者可快速掌握互动卡片的设计、数据绑定、发送与交互更新等核心能力。

## **术语说明**

| **术语** | **说明** |
| --- | --- |
| **互动卡片** | 支持动态数据渲染与用户交互的消息模板，可在群聊或单聊中使用。 |
| **sys\_full\_json\_obj** | 系统保留字段，用于传递复杂结构数据（JSON 对象需序列化为字符串）。 |
| **回传请求** | 用户点击按钮时，钉钉服务端向开发者服务器发起的 HTTP 回调请求。 |
| **outTrackId** | 业务唯一标识符（如审批单 ID），发送与更新卡片时必须保持一致。 |
| **corpId** | 企业的唯一标识。 |
| **cardPrivateData** | 卡片私有数据字段，包含按钮 ID（actionIds）和自定义回传参数（params）。 |

## **准备工作**

在开始开发前，请确保已完成以下准备工作：

- 已创建**企业内部应用**或**第三方企业应用**，并在钉钉开发者后台完成注册；
- 已获取应用的`AppKey`和`AppSecret`，用于调用 API 获取访问令牌；
- 已申请并正确配置机器人`robotCode`，用于消息发送。

## **接入流程简介**

本流程适用于企业内部自建应用或第三方企业应用的开发者，用于在钉钉群聊中实现可交互的消息卡片（如审批、任务处理等场景）。整体流程如下：

步骤一：分析卡片需求。

步骤二：分析布局以及搭建样式。

步骤三：定义字段以及绑定数据。

步骤四：调用钉钉开放平台提供的[发送钉钉互动卡片](https://open.dingtalk.com/document/group/send-interactive-dynamic-cards#topic-2043166)接口发送卡片。

步骤五：调用钉钉开放平台提供的[更新钉钉互动卡片](https://open.dingtalk.com/document/group/update-dingtalk-interactive-cards#doc-api-dingtalk-UpdateInteractiveCard)接口更新互动卡片。

## 步骤一：分析卡片需求

以审批卡片为例，需具备以下交互功能：

- 用户点击整个卡片可跳转至审批详情页面；
- 卡片底部提供"同意"、"拒绝"按钮，支持一键操作；
- 操作完成后，按钮状态变更为"已同意"或"已拒绝"，且不可再次点击；
- 卡片数据根据审批结果实时更新，保持状态同步。

**效果示意**：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389810.png)

操作后状态变化：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389811.png)

即使按钮已禁用，用户仍可通过点击卡片整体跳转至详情页。

## 步骤二：分析布局以及搭建样式

### 布局拆分

卡片整体分为三部分：

- **卡片头部**：使用"卡片头部"组件设置主标题区域
- **卡片内容区**：包含标题和列表项（每项由标签加粗 + 值普通字体组成）
- **卡片底部按钮区**：使用"横排按钮"组件添加"同意"、"拒绝"按钮

### **实现步骤**

1. 先实现三个简单部分：卡片头部、标题、按钮。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389812.png)
2. 由于列表标题是加粗字体，而列表内容是普通字体，无法用单个文本组件实现，需使用布局组件：

   1. 插入一个 1：1 布局组件，调整好间距。

      ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389813.png)
   2. 在左右两个布局上分别放置两个文本组件，调整间距并设置加粗样式。

      ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389814.png)
   3. 开启左边布局组件的 "自适应宽度" 属性。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p1093570.png)
   4. 同时给左边的文本组件也设置成 "**自适应宽度**"。

      ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389816.png)
   5. 修改文案内容，完成最终效果。

      ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389817.png)
3. 至此完成卡片的样式搭建。

## 步骤三：定义字段以及绑定数据

### 定义变量

根据卡片需求，列出需要动态变更的内容：

- 审批标题
- 审批内容项
- 审批的状态
- 审批的详情页链接

在卡片编辑器的**数据源面板**中，点击"**编辑普通变量**"，录入上述字段：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389818.png)

审批内容项通过**对象数组**方式表达（而非单独字段），提升灵活性。创建变量时可同步设置 Mock 数据，方便预览效果。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389819.png)

### 绑定变量到模板

1. **配置卡片点击跳转链接**：选中整个卡片组件，给卡片配置卡片的点击跳转链接。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389820.png)
2. **设置审批标题**

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389821.png)
3. **设置审批内容项**：由于是对象数组，需使用 "循环渲染容器" 组件。

   1. 在卡片上放置“循环渲染容器”，同时设置组件的对象数组为审批内容项：

      ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389822.png)
   2. 将前面搭建好的内容项组件放置到"循环渲染容器"里面，修改文本内容为变量。

      > **[!NOTE]**
      >
      > 读取对象数组每一项的内容时，变量需加 `"loop."` 前缀。

      ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389823.png)
4. **预览效果**：点击右上角"**预览模式**"查看最终效果。

   > **[!NOTE]**
   >
   > 未开启预览模式时，循环渲染容器最多只显示第一条内容，开启后才使用真正的列表内容展示。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389824.png)
5. 至此完成卡片变量的定义以及模板变量的绑定。

## 步骤四：发送互动卡片高级版内容

完成模板搭建后，调用钉钉开放平台提供的[发送钉钉互动卡片](https://open.dingtalk.com/document/group/send-interactive-dynamic-cards#topic-2043166)接口发送卡片。

**示例代码**：

```
POST /v1.0/im/interactiveCards/send HTTP/1.1
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "templateid",
  "openConversationId" : "opencid",
  "outTrackId" : "uniqueid",
  "robotCode" : "robotcode",
  "conversationType" : 1,
  "cardData" : {
    "cardParamMap" : {
      "title": "朱小志提交的财务报销",
      "detailUrl": "https://dingtalk.com",
      "status": "pending",
      "sys_full_json_obj": "{\\"contents\\":[{\\"label\\":\\"报销类型\\",\\"text\\":\\"差旅费\\"},{\\"label\\":\\"报销金额\\",\\"text\\":\\"1000元\\"},{\\"label\\":\\"报销理由\\",\\"text\\":\\"出差费用\\"}]}"
    }
  }
}
```

**参数说明**：

| 参数 | 是否必填 | 描述 |
| --- | --- | --- |
| cardTemplateId | 是 | 卡片模板 ID，可在卡片编辑器中获取。 |
| openConversationId | 是 | 接收方会话 ID及群ID。 |
| outTrackId | 是 | 业务唯一标识，在审批的场景下，建议使用审批单 ID。 |
| robotCode | 是 | 应用对应的机器人 ID 。 |
| conversationType | 是 | 会话类型：   - **1**：表示群聊 - **0**：表示单聊 |
| cardData.cardParamMap | 是 | 卡片数据映射表。 |
| sys\_full\_json\_obj | 否 | 复杂对象需序列化为 JSON 字符串后填入此字段。 |

调用接口成功后即可在群内看到发送的卡片。

## 步骤五：更新互动卡片高级版状态

为了实现用户点击按钮后的状态更新，需完成以下流程：

### 注册回调地址

在钉钉的开放平台上注册卡片的回调地址，点击卡片上“同意”或“拒绝”操作后，会通知到审批系统。

### 调整卡片模板

在原来的按钮基础上新增两个按钮："已同意"、"已拒绝"：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389825.png)

### 配置按钮显示逻辑

我们希望在未审批时显示“同意”和“拒绝”按钮，审批通过后显示“已通过”，审批拒绝显示“已拒绝”。

所以我们需要定义 `status` 字段表示审批状态，取值如下：

- `pending` - 未审批
- `accept` - 审批通过
- `reject` - 审批不通过

为四个按钮分别配置 "**是否显示**" 属性，通过条件计算控制按钮显示与否：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389826.png)

打开"预览模式"，动态修改 Mock 数据观察不同 `status` 值的表现：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389827.png)

### 配置按钮点击事件

当按钮的动态显示配置完之后，我们还需要配置按钮的点击事件，让审批系统知道当前按钮是要执行什么操作。

- "**已同意**"、"**已拒绝**"按钮：设置 "按钮状态" 为 "禁用"，使其不可点击。
- "**同意**"、"**拒绝**"按钮：配置 "按钮点击事件类型" 为 "回传请求"，用户点击后向回调地址发送请求。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2165806871/p389828.png)

### **处理回传请求**

以"同意"按钮为例，用户点击后审批系统接收到的 HTTP 请求，请求内容为：

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "XXXXXX",
    "userId": "XXXXXX",
    "content": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]},\"params\":{\"action\":\"accept\"}}"
}
```

**参数说明**：

| 字段 | 说明 |
| --- | --- |
| corpId | 点击该按钮的用户的组织。 |
| outTrackId | 卡片的唯一 ID（与发送时的 outTrackId 一致）。 |
| userId | 点击该按钮的用户 ID。 |
| content | 按钮详细信息（JSON 字符串），包含 `cardPrivateData` 字段。 |

其中 `cardPrivateData.actionIds` 代表当前点击的按钮 ID（如"同意"按钮 ID 为 1，则值为 `["1"]`）。若配置了回传参数，会在 `cardPrivateData.params` 中出现。

### 返回更新数据

审批系统识别出要执行"同意"操作后，处理完内部业务逻辑，需在回调请求中返回最新卡片数据：

```
{
  "cardTemplateId": "templateid",
  "outTrackId": "uqniueid",
  "cardOptions": {
    "updateCardDataByKey": true
  },
  "cardData": {
    "cardParamMap": {
      "status": "accept"
    }
  }
}
```

`updateCardDataByKey` 代表此次更新卡片的数据，只需更新指定字段，其他字段保持原有值。返回新数据后，钉钉互动卡片会及时刷新为最新状态。

至此就完成了卡片的状态更新的流程，详情参见[更新钉钉互动卡片](https://open.dingtalk.com/document/group/update-dingtalk-interactive-cards#doc-api-dingtalk-UpdateInteractiveCard)。
