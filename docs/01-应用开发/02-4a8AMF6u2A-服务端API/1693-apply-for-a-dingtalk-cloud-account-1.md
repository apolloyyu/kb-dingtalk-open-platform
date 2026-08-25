---
title: "申请钉钉云账号"
source_url: "https://open.dingtalk.com/document/development/apply-for-a-dingtalk-cloud-account-1"
namespace: "development"
slug: "apply-for-a-dingtalk-cloud-account-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 申请钉钉云账号 > 申请钉钉云账号"
doc_id: "vTKCrin8cK"
updated_at: "2025-12-18 09:31:55"
---

> Source: https://open.dingtalk.com/document/development/apply-for-a-dingtalk-cloud-account-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 申请钉钉云账号 > 申请钉钉云账号
> Updated: 2025-12-18 09:31:55

# 申请钉钉云账号

本文档指导开发者完成钉钉云账号的申请流程，包括登录开发者后台、申请条件、购买解决方案以及关键的消息接收人设置。请按照以下步骤操作，确保顺利开通并稳定使用钉钉云服务。

## 步骤一：登录开发者后台

1. 使用企业管理员账号访问 [开发者后台](https://oa.dingtalk.com/?redirect=http%3A%2F%2Foa.dingtalk.com%2Fomp%2Fapi%2Fmicro_app%2Fadmin%2Flanding%3Fcorpid%3Dopen-dev.dingtalk.com%26redirect_url%3Dhttp%3A%2F%2Fopen-dev.dingtalk.com%2F#/login)。
2. 成功登录后，在首页找到并点击 **“钉钉云”** 模块，进入钉钉云服务页面，如下图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3575299951/p163326.png "image.png")

## **步骤二申请钉钉云账号**

**前提条件：企业必须已完成产品方案商入驻，方可申请钉钉云账号。**

- 若尚未入驻，请参考 [合作全流程指引](https://open.dingtalk.com/document/isvapp/isv-cooperation-guide) 完成相关认证与签约流程。
- 入驻成功后，系统将自动开通钉钉云账号申请权限，如下图所示：

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6238725671/p163327.png "image.png")

## 步骤三：登录钉钉云购买解决方案

- 进入钉钉云控制台。
- 在解决方案市场中选择所需的产品或服务套餐。
- 根据业务需求完成购买流程，激活对应资源。

> ⚠️ **注意**：未完成购买前，部分功能和服务可能无法正常使用。

## 步骤四：设置消息接收人

> **[!IMPORTANT]**
>
> **建议将公司负责人设置为消息接收人，免因未收到欠费等重要提醒，导致无法继续使用钉钉云。钉钉云资源的释放或停用将会导致应用不可用！**

### **操作步骤**

1. 进入到钉钉云控制台后，找到消息接收管理的入口，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3575299951/p163328.png "image")
2. 进入消息接收管理-基本接收管理，配置常规通知的接收规则，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3575299951/p163329.png "image")
3. 点击 **“新增消息接收人”**，输入接收人的姓名、手机号及邮箱地址，确保信息准确无误后保存，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4575299951/p163330.png "image")

   保存成功后，如下图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4575299951/p163331.png "image.png")
4. 验证联系方式可用性，系统将向填写的手机和邮箱发送测试消息，请确认接收方能正常收到短信和邮件，避免遗漏后续告警信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4575299951/p163332.png "image")

   正常接收消息，如下图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4575299951/p163333.png "image.png")
5. 为关键消息类型配置接收人，其他消息类型，推荐设置消息接收人，保证可以接收到消息。

   > **[!NOTE]**
   >
   > - 为以下高优先级消息类型设置接收人，推荐将公司负责人或运维主管设为接收对象。
   > - 除上述必选外，其他消息类型也应尽可能配置接收人，以保障全面监控与响应能力。

   | **类型** | **消息类型** |
   | --- | --- |
   | **基本消息管理** | 产品到期通知 |
   | ECS/RDS到期前15天通知 |
   | 产品的欠费、停服、即将释放相关信息通知 |
   | 产品新功能上线或下线的通知 |
   | 产品运维通知 |
   | ECS故障通知 |
   | 云数据库故障或运维通知 |
   | **语音接收管理** | 账户余额预警通知 |
   | 产品即将释放通知 |
   | DDoS黑洞通知 |
