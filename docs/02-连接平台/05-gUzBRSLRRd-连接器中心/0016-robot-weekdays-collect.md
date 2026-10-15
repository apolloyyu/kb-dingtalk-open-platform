---
title: "工作日定时发送机器人消息收集日报"
source_url: "https://open.dingtalk.com/document/connection/robot-weekdays-collect"
namespace: "connection"
slug: "robot-weekdays-collect"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > 机器人 > 工作日定时发送机器人消息收集日报"
doc_id: "5KsQOQmRE7"
updated_at: "2026-05-19 19:46:08"
---

> Source: https://open.dingtalk.com/document/connection/robot-weekdays-collect
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > 机器人 > 工作日定时发送机器人消息收集日报
> Updated: 2026-05-19 19:46:08

# 工作日定时发送机器人消息收集日报

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 拥有所在钉钉组织**已发布**的钉钉[企业内部应用机器人](../../01-应用开发/01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)。
3. 拥有所在钉钉组织且已经完成了[添加机器人入群](../../01-应用开发/01-XOnnmGCTbn-开发指南/0079-add-robot-to-group.md)的操作。

## **预期效果**

![日报消息提醒.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0304913961/p711666.png)

## 步骤一：创建连接流

1. 登录[开发者后台](https://open-dev.dingtalk.com/fe/connector#/myFlow)。
2. 单击**开放能力 > 连接平台 > 我的连接流 > 创建连接流。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304913961/p711667.png)

## 步骤二：配置连接流

1. 配置触发事件：

   1. 选择**内置工具 > 定时触发**。

      ![定时触发（固定）.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304913961/p711668.png)
   2. 选择**触发事件 > 自定义时间触发。**

      ![自定义时间触发（固定）.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304913961/p711670.png)
   3. 配置参数：

      - 生效日期：2023-08-26至2024-08-26**。**
      - 触发周期：每周触发。
      - 每周的执行日期：周一、周二、周三、周四和周五。
      - 执行时间：18:00。
2. 配置执行动作：

   1. 选择**官方连接器 > 机器人。**

      ![连接器机器人.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304913961/p711695.png)
   2. 选择**执行动作 >** **发送markdown消息[自定义机器人]****。**

      ![markdown机器人自定义消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304913961/p711696.png)
   3. 配置参数：

      - **markdown格式正文**：选择**输入值**，本示例填写如下：

        ```
        [魔法棒]<font color = "FF6A00">**日报来喽！**</font>

        请同学们[<font color = "007FFF">**点这里**</font>](https://www.dingtalk.com)提交日报 

        填写完成后，请注意保存提交哦[撒花]

        > *提醒来自温柔、可爱、贴心的钉三多～*
        ```
      - **accessToken**：选择**输入值**，本示例填写：[机器人Webhook的access\_token值](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0791-faq-robot.md#cf081fe0c4jc1)。
      - **标题**：选择**输入值**，本示例填写：日报。

      此时，单击**测试并预览，**就可以查看日报消息了。
3. 发布连接流。

## 恭喜，你已完成全部配置！

发布完成后，即在周一至周五每天18:00可以接收到日报提醒，可在连接流页面单击**调试**体验。

![调试体验机器人日报.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0304913961/p711749.png)
