---
title: "酷应用群扩展沉浸式容器"
source_url: "https://open.dingtalk.com/document/dingstart/group-chat-coolapp-expands-immersive-container"
namespace: "dingstart"
slug: "group-chat-coolapp-expands-immersive-container"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 开发参考 > 酷应用群扩展沉浸式容器"
doc_id: "asI6zZUEq5"
updated_at: "2026-07-21 14:19:52"
---

> Source: https://open.dingtalk.com/document/dingstart/group-chat-coolapp-expands-immersive-container
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 开发参考 > 酷应用群扩展沉浸式容器
> Updated: 2026-07-21 14:19:52

# 酷应用群扩展沉浸式容器

本文介绍什么是沉浸式容器、沉浸式容器的优点以及酷应用群扩展中使用沉浸式容器的操作步骤。

## **什么是沉浸式容器**

沉浸式容器让酷应用在钉钉内显示更轻量，移动端半屏显示，桌面端侧边栏显示，可协同操作。

容器由标题区与内容区组成。

- **移动端**

  - 半屏容器高度为手机屏幕的83%，可配置为50%。
  - 导航高度固定56px。
- **桌面端**

  - 侧边栏宽度为480px。
  - 导航高度固定48px。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2974164871/p1084372.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2974164871/p1084373.png)

更多产品设计，请参见[沉浸式容器设计规范](https://ding.design/#/cate/1/page/823)。

## **沉浸式容器的优点**

以下将由浅入深介绍沉浸式容器的优点，以前和现在模式的对比。

1. **跳转协议**：页面容器可以被打开。
2. **页面布局**：基础的页面布局，自适应移动和桌面端。
3. **页面组件**：常用的页面组件，自适应移动和桌面端。
4. **页面模板**：以上的最佳实践和可复用的场景化模板。

   | **模块** | **以前** | **现在** |
   | --- | --- | --- |
   | **跳转协议** | [AppLink协议](../02-4a8AMF6u2A-服务端API/1395-structure-of-applink.md)多，不够聚焦酷应用场景。 | 提供多种AppLink协议跳转，请参考[AppLink协议](../02-4a8AMF6u2A-服务端API/1395-structure-of-applink.md)。 |
   | **页面布局** | 无标准规范，开发自己实现，处理不同跳转协议的页面Header实现。 | - 页面容器标准设计规范，请参考[半屏容器&侧边栏设计规范](https://ding.design/#/cate/1/page/823)。 - 页面容器官方组件实现，请参考[页面容器PageContainer](https://ding.design/#/cate/64/page/826)。 |
   | **页面组件** | - 缺少设计规范及配套实现 - 不支持桌面端 - 一端代码直接跑在另一端，不符合交互习惯 | Ding Design 官方设计语言 + 官方实现，自动支持移动和桌面端，请参考[Ding Design](https://ding.design/#/cate/227/page/740)。 |
   | **页面模板** | 无 | 覆盖表单、数据展示、数据统计等常用场景话模板，请参考[页面模板库](https://www.npmjs.com/package/dd-cool-templates)。 |

## **酷应用群扩展中使用沉浸式容器的操作步骤**

**步骤一**：提供多种AppLink协议跳转，请参考[AppLink协议](../02-4a8AMF6u2A-服务端API/1395-structure-of-applink.md)。

**步骤二**：配置酷应用的访问链接。![iShot2023-01-03 18](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2974164871/p547865.png)

**步骤三**：酷应用配置完成后，企业内部群开启该酷应用。![iShot2022-09-26 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8521872871/p495455.png)

**步骤四**：手机端钉钉客户端和PC端钉钉客户端访问该酷应用效果。

- **手机端：**

  ![iShot2023-01-03 18](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8521872871/p547867.png)
- **PC端：**

  ![iShot2022-09-26 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8521872871/p495463.png)

**步骤五**：打开的目标页面导航栏设置可参考[半屏容器&侧边栏设计规范](https://ding.design/#/cate/1/page/823)和[页面容器PageContainer](https://ding.design/#/cate/64/page/826)。

## 配套工具

- 基础组件 Ding Design，请参考[Ding Design](https://ding.design/#/)。
- 页面模板库，请参考[页面模板库](https://www.npmjs.com/package/dd-cool-templates)。
