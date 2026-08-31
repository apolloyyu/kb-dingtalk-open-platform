---
title: "AI 卡片模板"
source_url: "https://open.dingtalk.com/document/development/ai-card-template"
namespace: "development"
slug: "ai-card-template"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片模板搭建 > AI 卡片模板"
doc_id: "1yzF1zcrW1"
updated_at: "2026-08-04 09:07:19"
---

> Source: https://open.dingtalk.com/document/development/ai-card-template
> Path: 互动卡片 / 开发指南 / 卡片模板搭建 > AI 卡片模板
> Updated: 2026-08-04 09:07:19

# AI 卡片模板

通过本文你将了解到如何创建与使用 AI 卡片模板

> **[!IMPORTANT]**
>
> - AI 卡片模板，可用于 AI 应用开发，详情参考[钉钉 AI PaaS 介绍](../../03-AI-PaaS/01-pm4vgiS9Br-平台介绍/0001-introduction-to-dingtalk-ai-paas-1.md)。
> - AI 卡片模板，可用于 IM 机器人当中，详情参考[打字机效果流式 AI 卡片](../02-ukxqoQhFaf-搭建平台/0002-typewriter-effect-streaming-ai-card.md)。

## **创建 AI 卡片模板**

目前可以在[卡片平台](https://open-dev.dingtalk.com/fe/card)创建 AI 类型的卡片模板，只需要在创建模板的过程中选择“消息卡片”，同时卡片模板场景选择“AI 卡片”即可。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9365085871/p715257.png)

**将现有卡片转换成AI卡片**：对于存量的**消息**和**标准**卡片，可以直接导入到新创建的 AI 卡片中，导入后原来卡片的内容会被移动到输入中以及完成状态下。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4778983961/p715252.png)

## **如何设置AI卡片状态**

为了降低业务的使用成本，我们针对 AI 卡片模板预设了几个状态，包含处理中、输入中、完成、失败等状态。业务可以通过调用 [AI卡片流式更新](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0785-api-streamingupdate.md)通过传递 isFinalize、isError 参数控制状态的变更。

| **状态名** | **补充说明** |
| --- | --- |
| 处理中 | 无需手动设置，AI 卡片投放后，流式更新开始前的状态。 |
| 输入中 | 无需手动设置，流式更新开始后的状态。 |
| 完成 | 需要手动设置，在流式更新接口传入 isFinalize = true 设置。 |
| 失败 | 需要手动设置，在流式更新接口传入 isError = true 设置。 |

可以在「AI卡片」组件里配置当前卡片支持的状态类型， 默认会启用处理中、输入中以及完成状态。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9365085871/p715276.png)

在开发过程中可以通过切换模拟器上方的卡片状态栏来切换卡片的状态，分别进行搭建和预览。

## AI卡片状态说明

### **处理中状态**

- 作用：在功能排队或者内容准备时使用。
- 自定义：处理中的样式由卡片内置， 是钉钉标准设计，目前不支持自定义。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9365085871/p790565.png)

### **输入中状态**

- 作用：在卡片进行数据流式更新时使用，卡片的边框会有渐变的动画效果。
- 自定义：输入中会在数据支持流式更新时生效，可添加文本、markdown 等组件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9365085871/p790567.png)

#### **完成状态**

- 作用：流式内容更新结束后的状态。用户可以在当前状态查看内容、执行操作以及完成反馈。
- 自定义：可添加所有类型的组件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9365085871/p790568.png)

#### 失败状态

- 作用：在遇到异常情况时使用此状态，可以用于展示错误信息或者提供重试能力。
- 自定义：卡片默认提供一份兜底文案， 如果文案不符合要求，业务可以自定义搭建所需样式。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9365085871/p790569.png)
