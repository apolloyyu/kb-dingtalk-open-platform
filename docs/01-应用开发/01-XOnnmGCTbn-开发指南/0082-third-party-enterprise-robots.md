---
title: "第三方企业机器人"
source_url: "https://open.dingtalk.com/document/dingstart/third-party-enterprise-robots"
namespace: "dingstart"
slug: "third-party-enterprise-robots"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 企业机器人 > 第三方企业机器人"
doc_id: "KaUOROnlzP"
updated_at: "2026-06-30 09:01:02"
---

> Source: https://open.dingtalk.com/document/dingstart/third-party-enterprise-robots
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 企业机器人 > 第三方企业机器人
> Updated: 2026-06-30 09:01:02

# 第三方企业机器人

本文介绍了如何创建、发布第三方企业机器人。

## 使用说明

1. 确保组织已经完成[入驻成产品方案商](../07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)。
2. 确保组织下，有已完成上架的第三方企业应用。上架流程请参考[合作全流程指引](../07-TjCzIgfQs3-平台服务/0027-isv-cooperation-guide.md)。
3. 第三方企业机器人功能正在灰度，预计7月份全量后可接入使用，敬请期待。

## 步骤一：创建第三方企业机器人

1. 创建第三方企业应用，参见第三方企业应用的[应用创建与配置](0007-create-application.md)流程。
2. 第三方企业应用创建后，将自动创建第三方企业机器人。
3. 每个第三方企业应用仅可创建1个第三方企业机器人。

## 步骤二：设置机器人信息

1. 单击**应用功能** > **机器人与消息推送**。

   ![三方机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2621872871/p580482.png)
2. 可以查看机器人名称和图标，第三方企业机器人的名称和图标须与第三方企业应用的名称和图标保持一致。

   > **[!NOTE]**
   >
   > 1. 如需修改机器人名称和图标，请修改第三方企业应用的名称和图标并进行审核。
   > 2. 修改第三方企业机器人的名称和图标后，仅会对新安装该机器人的组织生效；已安装该机器人的组织可以在[**钉钉管理后台 > 工作台 > 应用管理**](https://oa.dingtalk.com/index.htm#/microApp/microAppListNew)通过修改第三方应用的名称和图标来进行修改。
3. 可以设置第三方企业机器人的信息：

- **机器人简介**：标题简述用于群内添加机器人时对钉钉用户展示机器人的功能。

  ![机器人简介](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2621872871/p580556.png)
- **机器人简介**：机器人简介用于在机器人的个人信息页中展示机器人的功能描述。

  ![机器人描述](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2621872871/p580560.png)
- **机器人预览图**：机器人预览图用于群内添加机器人时对钉钉用户展示机器人消息发送出来时的预览效果。

  ![消息预览图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2621872871/p580890.png)
- **消息接收地址**：消息接收地址用于你的业务系统接收来自机器人推送的消息。

> **[!IMPORTANT]**
>
> 原有**开放能力** > **机器人**页面中的数据不会改变，但该页面入口将在后期进行关停，关停前将提前通过开发者后台公告进行通知。

## 步骤三：发布机器人

确认机器人相关信息后，单击**发布**按钮，机器人功能将被发布。

## 步骤四：组织添加第三方企业机器人

组织若需要使用第三方企业机器人，需要将该机器人所属的第三方企业应用安装到组织中，机器人服务将自动生效。

## 步骤五：组织使用机器人

第三方企业机器人支持在企业单聊会话，企业群聊会话中使用。

### 在企业单聊会话中，使用机器人

企业内用户可以通过搜索机器人名称，在功能列表，找到机器人并进行单聊。

![机器人使用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2621872871/p580575.png)

### 在企业群聊会话中，使用机器人

![机器人展示](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6448929761/p581221.gif)

## 步骤六：组织管理第三方企业机器人的可见范围

组织若需要控制第三方企业机器人在组织内部的可见性，可在[**钉钉管理后台 > 工作台 > 应用管理**](https://oa.dingtalk.com/index.htm#/microApp/microAppListNew)中设置应用的可见范围。机器人的可见范围将跟随应用可见范围生效。

![设置可见范围](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2621872871/p581222.png)

## 步骤七：组织自行停用第三方企业机器人的功能

当前暂不支持第三方企业应用的开发者关闭机器人功能。

> **[!NOTE]**
>
> - 对于已停用的应用，机器人将在组织和已安装的群内停用。
> - 对于已从组织中卸载的应用，机器人将在组织和已安装的群内自动删除。
> - 应用停用和卸载后，第三方企业机器人在钉钉主搜功能中将在次日开始不可搜索，群内将立即生效。
