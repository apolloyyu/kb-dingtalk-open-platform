---
title: "审批表单数据同步至宜搭"
source_url: "https://open.dingtalk.com/document/connection/approval-form-appropriate"
namespace: "connection"
slug: "approval-form-appropriate"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > 宜搭 > 审批表单数据同步至宜搭"
doc_id: "IJYOD0QCfR"
updated_at: "2026-07-30 09:19:00"
---

> Source: https://open.dingtalk.com/document/connection/approval-form-appropriate
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > 宜搭 > 审批表单数据同步至宜搭
> Updated: 2026-07-30 09:19:00

# 审批表单数据同步至宜搭

本文介绍了OA审批表单数据同步至宜搭。

## **简介**

OA数据表单同步到宜搭可以为很多行业带来重大意义，特别是那些需要频繁交换数据的行业。提高了工作效率、数据质量和安全性，优化行业的数据管理和协作。这项能力的运用促进企业的数字化转型和创新发展。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)（OA审批中使用连接器必备）。
3. 拥有一个所在组织的[宜搭应用](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0368-yida-faq.md#7b1f6070ebwcc)。

## **预期效果**

OA审批数据表单提交后，同步至宜搭数据表单。

![同步至宜搭数据表单.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697458.png)

## **步骤一：创建宜搭数据表单**

- 如果无宜搭数据表单，详情参见[如何创建流程表单？](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0368-yida-faq.md#fc88b0c0ebdtm)。

  > **[!NOTE]**
  >
  > 本示例使用**单行文本**和**数值**两个组件。
- 如果已有宜搭数据表单，可直接使用。

## **步骤二：创建连接流**

1. [创建连接流](../02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)，并完善连接流基本信息。
2. 配置触发事件：

   1. 单击**设置入参**，在**编码模式**下粘贴下方JSON示例。

      ```
      {
        "title": "OAPI业务参数",
        "type": "object",
        "properties": {
          "number": {
            "type": "number",
            "title": "宜搭表单数字输入框",
            "description": "宜搭表单数字输入框"
          },
          "text": {
            "type": "string",
            "title": "宜搭表单文本输入框",
            "description": "宜搭表单文本输入框"
          },
          "userId": {
            "title": "用户的userid",
            "type": "string",
            "description": "用户的userid"
          }
        },
        "required": [
          "userId",
          "text",
          "number"
        ]
      }
      ```

      ![设置入参- 同步OA审批数据表单同步至宜搭.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697479.png)
   2. 完成配置。
3. 配置执行动作：

   1. 选择官方连接器。

      ![官方连接器-选择宜搭.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697532.png)
   2. 选择执行动作 > **保存表单数据。**

      ![保存表单数据.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697534.png)
   3. 配置参数。
   4. 测试并预览：

      1. 输入测试值。

         ![配置参数-宜搭.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697541.png)
      2. 完成测试。

         ![完成测试-宜搭.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697545.png)

         此时，测试数据已经同步至宜搭数据表单。
   5. 设置出参。

      1. 单击**设置出参**，在**编码模式**下粘贴下方JSON示例。

         ```
         {
           "title": "OneConsole返回结果",
           "type": "object",
           "properties": {
             "success": {
               "title": "是否成功",
               "type": "boolean"
             },
             "errorMsg": {
               "title": "错误详情",
               "type": "string"
             }
           }
         }
         ```
      2. 单击**点击进行配置，**设置参数出参信息。
      3. 测试、预览并完成**保存**。

         ![保存出参配置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697548.png)
   6. 发布连接流。

      ![发布宜搭.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697549.png)

## **步骤三：配置OA数据表单**

1. 登录钉钉客户端，单击**工作台** > **审批**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p696429.png)
2. 单击管理后台。进入后台管理页面。

   > **[!IMPORTANT]**
   >
   > 进入OA审批管理后台，必须拥有OA审批应用管理权限，否则该按钮图标不显示。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697488.png)
3. 创建新表单，选择**数据表单**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697489.png)
4. 表单设计。

   1. 选择表单组件，选择**单行输入框**和**数字输入框**。

      ![宜搭-选择组件.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697583.png)
   2. 配置连接器。

      1. 添加连接器。

         ![配置连接流.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697587.png)
      2. 设置触发条件。

         ![表单提交（触发事件）.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697601.png)
      3. 选择连接器。

         ![选择连接器-宜搭.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697606.png)
      4. 配置执行动作并保存。

         ![保存连接器设置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697613.png)
      5. 发布流程表单。

         ![OA数据表单发布.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4156925871/p697617.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 进入钉钉客户端**工作台** > **审批**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p696480.png)
2. 选择上述发布的表单，填写信息并提交表单。

   ![提交数据表单.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3156925871/p697626.png)
