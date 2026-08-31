---
title: "（可选）测试应用"
source_url: "https://open.dingtalk.com/document/dingstart/test-dingtalk-app"
namespace: "dingstart"
slug: "test-dingtalk-app"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 应用测试与发布 > （可选）测试应用"
doc_id: "L81J9Ycel2"
updated_at: "2026-07-22 16:55:15"
---

> Source: https://open.dingtalk.com/document/dingstart/test-dingtalk-app
> Path: 应用开发 / 开发指南 / 开发指南 > 应用测试与发布 > （可选）测试应用
> Updated: 2026-07-22 16:55:15

# （可选）测试应用

如果你需要测试应用功能，可以按照本文档的操作步骤进行验证。本文适用于已完成应用开发的企业内部应用或第三方企业应用开发者，部分操作需具备管理员权限。

## **前提条件**

1. 已完成[应用创建与配置](0007-create-application.md)流程。
2. 已完成事件订阅接入配置。

   - **事件订阅服务**用于接收钉钉平台推送的用户行为事件（如消息发送、应用安装等），可在【开发者后台】>【开发配置】> 【事件订阅】中查看是否已启用。
   - 钉钉支持三种回调事件接收方式：RDS推送、SyncHTTP推送和Stream推送。详情请参考[事件订阅](../02-4a8AMF6u2A-服务端-API/0014-event-subscription-overview.md)。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**应用发布** > **体验组织与人员**。
3. 单击授权体验组织，完成授权操作

   > **[!NOTE]**
   >
   > - 如果没有体验组织，需要单击右上角**添加测试组织**并完成**设置体验成员**。
   > - 授权前请确认**事件订阅服务**已开启，否则可能导致授权失败。
4. 授权完成后，可在该体验组织内测试应用功能。

## **更多信息**

授权体验组织后，可根据应用类型通过以下方式使用或添加应用。

### **AI 助理**

已发布的 AI 助理会自动加入对应组织的组织架构中。你可以参考以下内容使用 AI 助理：

在钉钉主搜索框中输入 AI 助理名称，即可查找并使用。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4980774071/p755929.png)

### **小程序/网页应用**

发布完成后，可在钉钉客户端工作台中查找对应应用进行使用。

![使用小程序:网页应用.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p722548.png)

### **机器人**

1. 打开**钉钉客户端** > 指定群聊会话。

   ![1.打开指定群会话.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p722551.png)
2. 单击**群设置**，打开群设置页。

   ![2.单击群设置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p722553.png)
3. 单击**群管理** > **机器人** ，打开机器人管理页。

   ![3.机器人管理页面.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p722556.png)
4. 单击添加机器人，选择对应的机器人完成添加。

   ![4.完成机器人添加.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p722561.png)

机器人添加完成后，获取企业应用机器人的 Webhook 地址，具体操作详见[企业机器人 Webhook 地址](../02-4a8AMF6u2A-服务端-API/0791-faq-robot.md)。

### **酷应用**

#### **群聊酷应用**

酷应用被安装到群内后，群内成员可以在沟通的过程中高效的查看和使用酷应用提供的数据和功能，来完成业务协作。

以下是安装步骤：

1. 在钉钉移动端，打开需要配置的企业内部群，在**酷应用栏**，单击**更多**图标，进入酷应用中心。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4221872871/p723785.png)
2. 在酷应用页面左上角区域，连续点击6次蓝色图标后进入测试安装页面。通过输入酷应用编码，在群内安装这个群应用。

#### **单聊酷应用**

基于主应用扩展快捷入口、会话机器人和互动卡片的能力。使应用不仅可以在单聊会话实现任务协同、目标共创、商机共享、战报通告等沉浸体验，从技术能力上还实现在单聊会话中集成酷应用。

以下是安装步骤：

1. 在钉钉移动端，打开需要配置的人员会话，在**应用栏**，单击**更多**图标，进入酷应用中心。

   ![单聊酷应用安装.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4221872871/p723813.png)
2. 在酷应用页面左上角区域，连续点击6次蓝色图标后进入测试安装页面。通过输入酷应用编码，单聊会话内安装单聊酷应用。

#### **消息菜单酷应用**

在钉钉上可以通过长按消息唤起菜单，并通过菜单的功能选项对消息进行操作，如消息转发、消息转日程、消息转任务等。

![消息菜单体验.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p724525.png)

#### **链接增强酷应用**

链接增强实现了钉钉聊天中的链接转换能力，接入后可以实现链接自动识别并转换成卡片。用户可以直观的查看卡片的内容信息，并且可以借助卡片的交互能力直接在卡片上实现业务操作。

#### **成员资料页酷应用**

成员资料页扩展实现了成员资料页的扩展能力，在成员资料页扩展一些信息，比如员工上下班情况、销售业绩展示等。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3221872871/p517300.png)

#### **文档酷应用**

文档酷应用能够实现将这些工作转变成自动化任务，接入后可以帮助用户及时感知一些指定操作、快速进行文档内容读写及校验。

![文档酷应用展示.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7731072871/p722585.png)

## **后续步骤**

测试应用完成后，请进行上架前的[应用自检与分发](0019-selfcheck-dingtalk-app.md)，确保功能完整性和合规性。
