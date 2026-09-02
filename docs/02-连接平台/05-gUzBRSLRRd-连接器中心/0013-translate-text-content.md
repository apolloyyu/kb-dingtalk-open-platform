---
title: "翻译文本内容"
source_url: "https://open.dingtalk.com/document/connection/translate-text-content"
namespace: "connection"
slug: "translate-text-content"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > AI能力 > 翻译文本内容"
doc_id: "VynGBGZ6x7"
updated_at: "2026-05-19 19:46:10"
---

> Source: https://open.dingtalk.com/document/connection/translate-text-content
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > AI能力 > 翻译文本内容
> Updated: 2026-05-19 19:46:10

# 翻译文本内容

本文介绍了通过AI能力，实现文本内容翻译功能。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 拥有所在钉钉组织**已发布**的钉钉[企业内部应用机器人](../../01-应用开发/01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)。
3. 拥有所在钉钉组织且已经完成了[添加机器人入群](../../01-应用开发/01-XOnnmGCTbn-开发指南/0079-add-robot-to-group.md)的操作。

## **预期效果**

实现文本内容中译英。

![翻译文本内容.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714501.png)

## **步骤一：创建连接器**

- 如果无连接器，详情参见[创建连接器](../02-XdgyZifJkr-我的连接/0010-create-connector.md)。
- 如果已有连接器，可直接使用已有连接器。

## **步骤二：配置触发事件**

1. 选择创建的连接器进入详情页面，然后依次选择**触发事件 > 创建触发事件**。

   ![连接器-创建触发事件..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7984055861/p674345.png)
2. 填写触发事件的基础信息。
3. 在模型配置界面下，配置**触发事件入参**参数，然后单击**下一步**。

   ![设置文本消息字段.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689603.png)
4. 在调试界面下，填写**触发事件入参**参数，然后单击**立即调试**。

   ![立即调试-工作通知文本内容.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689610.png)
5. 调试完成之后，选择**发布**。

   ![发布文本消息text.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689613.png)

## **步骤三：创建连接流**

1. 单击**我的连接流 > 创建连接流**。

   ![创建连接流（新版）.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714384.png)

   此时，你已经进入连接流配置页面。
2. 配置触发事件：

   1. **选择自建连接器**，单击**触发事件 > 自建连接器 > 测试**（步骤二中创建的连接器）。

      ![选择自建连接器.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714392.png)
   2. 选择触发事件，单击**测试**（步骤二中创建的触发事件）。

      ![选择触发事件（新版）.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714398.png)
3. 配置执行动作：

   1. 添加AI执行动作：

      1. 选择**官方连接器**，单击**执行动作 > 官方连接器 > AI能力**。

         ![官方连接器（新版）.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714425.png)
      2. 选择执行动作，单击**文本翻译**。

         ![选择AI执行动作.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714430.png)
      3. 配置参数：

         - 翻译源文字符串：**选择引用值 > 触发事件 > 入参.文本内容**。
         - 翻译源语言类型：选择**输入值，填写 zh。**
         - 翻译目标语言类型：选择**输入值，填写 en。**

           ![AI参数配置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714433.png)

           配置完成后，可单击下方**测试并预览**进行测试，即可查看翻译内容。
   2. 添加机器人执行动作：

      1. 添加执行动作，单击**“⊕” > 请选择连接器和执行动作。**

         ![添加执行动作.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714479.png)
      2. 选择**官方连接器**，单击**执行动作 > 官方连接器 > 机器人**。

         ![机器人执行动作.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714486.png)
      3. 选择执行动作，单击**发送文本消息[自定义机器人]**。

         ![文本消息选择.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714489.png)
      4. 配置参数：

         - accessToken：选择**输入值**，本示例填写：[机器人Webhook的access\_token值](https://open.dingtalk.com/document/orgapp/faq-robot#ba79fa80c4c0g)。
         - 文本消息：选择**引入值 > 执行动作 >** **出参.OneConsole返回结果.翻译结果字符串**。

           ![AI中机器人设置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714495.png)

           配置完成后，可单击下方**测试并预览**进行测试，即可在群内查看机器人发送的翻译内容。
4. 发布连接流。

   ![发布AI连接流.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714496.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 获取触发事件[方式一（推荐）：通过Webhook地址触发事件](../02-XdgyZifJkr-我的连接/0013-using-connectors-1.md#636e0c4a67u8r)地址。
2. 根据Webhook地址，体验翻译文本内容。

![AI文本翻译.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1728550071/p714500.png)
