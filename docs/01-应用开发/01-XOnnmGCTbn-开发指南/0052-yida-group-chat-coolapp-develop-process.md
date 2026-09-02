---
title: "酷应用开发流程"
source_url: "https://open.dingtalk.com/document/dingstart/yida-group-chat-coolapp-develop-process"
namespace: "dingstart"
slug: "yida-group-chat-coolapp-develop-process"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 宜搭群聊酷应用（ISV应用） > 酷应用开发流程"
doc_id: "ec0VXBmxn9"
updated_at: "2025-09-03 15:56:22"
---

> Source: https://open.dingtalk.com/document/dingstart/yida-group-chat-coolapp-develop-process
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 宜搭群聊酷应用（ISV应用） > 酷应用开发流程
> Updated: 2025-09-03 15:56:22

# 酷应用开发流程

本文介绍宜搭酷应用开发流程。

目前宜搭上几百万的企业自建应用都具备了半屏打开、自定义酷卡片发送、低代码逻辑编排的能力，酷能力赋能应用形态变得更简单。宜搭上生产的低代码应用默认具备酷应用的能力！

**目前支持企业自建酷应用，同时也支持一方和三方构建模板酷应用，上架至钉钉酷应用市场。**

## 宜搭酷应用开发指引帮助指引

钉钉酷应用整体的设计规范，详情参见[钉钉酷应用设计指南&通用设计规范](https://standard.dingtalk.com/#/cate/1/page/818)。

| 01酷应用介绍 | 02酷应用设计规范与指南 | 03酷应用开发指南 | 04 酷应用模板快速酷化及上架指南 |
| --- | --- | --- | --- |
| - [酷应用介绍](https://open.dingtalk.com/coolapp) - [宜搭酷应用工厂介绍](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/yZvMRzlLwOAWrkgXqYR9VnjY02pBqGox) - [《你好低代码-酷应用专题》直播介绍](https://h5.dingtalk.com/group-live-share/index.htm?type=2&liveFromType=6&liveUuid=5213a3b5-e054-48b9-b699-8b8dfb4547a7&bizType=kankan&dd_nav_bgcolor=FF2C2D2F#/union) | - [宜搭酷应用设计指南](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/7Y36k14mK9AV35vAPyg185NqapjblR2D) - [酷应用设计指南与通用规范](https://standard.dingtalk.com/#/cate/1/page/818) | - [酷应用开发手册](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/EGd6jK4Nvk3Jl9PMZZ0e8ZOP0LawMmQq) - [酷应用常见高频FAQ指南](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/bxgzX5wq4YoJPe1lvQOp8Ry2OB79ALPD) | - [宜搭模板应用快速酷化&上架到钉钉酷应用市场SOP](https://xmtrf1.aliwork.com/o/cool_template_sop) |

## 宜搭酷应用模板专区

目前宜搭酷应用已建立单独的分类专区，如果需要查看现有酷应用模板的相关配置，可直接启用后查看应用的配置链路，如需群内启用测试，可将应用上架到群自建酷应用中心，详见步骤五。![宜搭酷应用模板中心](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480363.png)

## 群订餐场景展示

### 场景一：餐品快速发布

食堂管理员经过简单的活动配置，将当天的新食品通过互动卡片或置顶卡片的形式发布到多个群内，不同群的员工在群内就能完成餐品预定。

### 场景二：餐品一键预定

企业可对互动卡片进行配置，设置“一键预定”按钮，新餐品发布同步到群内，群内员工单击“一键预定”按钮，填写预定信息后，可实现快速下单。订单信息以及库存在卡片上实时展示。

- 超时了不能提交、超份数了不能提交 -业务规则校验。
- 当订餐售罄时，按条件显示售罄按钮。

### 场景三：点餐数据通报

餐品售罄或到达预定时间后，系统会根据不同的定制要求自动统计订餐数据，并同步到群内，方便群内成员了解订餐情况。

- 订餐场景售罄情况下卡片发送到当前群。

### 场景四：导出订餐数据

订餐结束后，食堂管理员可以在应用后台数据管理页快速导出订餐数据，根据数据通知食堂准备订餐员工的餐品。![0824宜搭酷应用订餐](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7115331661/p480877.png)

## 群订餐接入流程

登录[宜搭](https://www.aliwork.com/)，进行应用流程开发

[](https://cloud.video.taobao.com/play/u/null/p/1/e/6/t/1/d/ud/373308520283.mp4)

## 步骤一：业务应用核心页面搭建

登录[宜搭](https://www.aliwork.com/)，进行应用流程开发：

- 表单设计器搭建发起活动表单![0824宜搭酷应用健康餐预定](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480379.png)
- 表单设计器搭建提交订餐表单![0824宜搭酷应用提交订餐表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480384.png)
- 自定义设计器搭建订餐列表页面![0824宜搭酷应用订餐列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480389.png)
- 报表设计器搭建订餐深度分析报表![0824宜搭酷应用报表展示](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480400.png)

## 步骤二：发送卡片节点配置

1. 单击**集成&自动化**。
2. 根据场景需求配置表单事件，当订餐活动表单创建成功时，推送订餐活动卡片。![0824宜搭酷应用集成自动化](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480403.png)
3. 单击触发事件“发起活动推送2个卡片”的**编辑**按钮，进入事件触发页面，在集成自动化流内选择卡片模板，选择**订餐列表**。![0824设置模板列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480410.png)
4. 选择**订餐列表**，集成自动化绑定卡片。![0824卡片配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480413.png)
5. 集成自动化配置卡片发送范围。![0824宜搭酷应用推送范围](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480418.png)

## 步骤三：卡片搭建

- 订餐列表卡片设计器![0824宜搭酷应用订单列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480435.png)
- 订餐看板卡片设计器![0824宜搭酷应用订餐看板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480436.png)

## 步骤四：更新卡片节点配置

单击**集成&自动化**，选择对应触发事件**编辑**按钮。![更新卡片节点配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480442.png)

## 步骤五：应用发布

选择**发布到企业自建应用中心**![0824宜搭酷应用发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480454.png)

### 发布到企业自建应用中心

![0824宜搭酷应用上架](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7537231661/p480462.png)

## 步骤六：应用使用

酷应用在钉群内启用使用链路效果如下。![0824宜搭酷应用使用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7115331661/p480880.png)
