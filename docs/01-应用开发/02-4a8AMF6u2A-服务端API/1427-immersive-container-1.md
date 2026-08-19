---
title: "沉浸式容器"
source_url: "https://open.dingtalk.com/document/development/immersive-container-1"
namespace: "development"
slug: "immersive-container-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 沉浸式容器"
doc_id: "LsDojACk2P"
updated_at: "2026-07-21 09:26:29"
---

> Source: https://open.dingtalk.com/document/development/immersive-container-1
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 沉浸式容器
> Updated: 2026-07-21 09:26:29

# 沉浸式容器

本文介绍什么是沉浸式容器和沉浸式容器的优点。

## **什么是沉浸式容器**

沉浸式容器让酷应用在钉钉内显示更轻量，移动端半屏显示，桌面端侧边栏显示，可协同操作。

容器由标题区与内容区组成。

- **移动端**

  - 半屏容器高度为手机屏幕的83%，可配置为50%。
  - 导航高度固定56px。
- **桌面端**

  - 侧边栏宽度为480px。
  - 导航高度固定48px。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QoJGq7Y05j4rlAKe/img/e78023c4-0324-4706-83cc-5a11f29e8d8f.png)

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QoJGq7Y05j4rlAKe/img/2d5f9973-4c95-458a-8dd7-767be19362a6.png)

更多产品设计，请参见[沉浸式容器设计规范](https://ding.design/#/cate/1/page/823)。

## **沉浸式容器的优点**

以下将由浅入深介绍沉浸式容器的优点，以前和现在模式的对比。

1. **跳转协议**：页面容器可以被打开。
2. **页面布局**：基础的页面布局，自适应移动和桌面端。
3. **页面组件**：常用的页面组件，自适应移动和桌面端。
4. **页面模板**：以上的最佳实践和可复用的场景化模板。

   | **模块** | **以前** | **现在** |
   | --- | --- | --- |
   | **跳转协议** | [跳转协议](1395-structure-of-applink.md)众多，不够聚焦酷应用场景。 | 提供多种AppLink协议跳转，请参考[AppLink协议](1396-open-applet.md)。 |
   | **页面布局** | 无标准规范，开发自己实现，处理不同跳转协议的页面Header实现。 | - 页面容器标准设计规范，请参考[半屏容器&侧边栏设计规范](https://ding.design/#/cate/1/page/823)。 - 页面容器官方组件实现，请参考[页面容器PageContainer](https://ding.design/#/cate/64/page/826)。 image |
   | **页面组件** | - 缺少设计规范及配套实现 - 不支持桌面端  image - 一端代码直接跑在另一端，不符合交互习惯  image | Ding Design 官方设计语言 + 官方实现，自动支持移动和桌面端，请参考[Ding Design](https://ding.design/#/cate/227/page/740)。 |
   | **页面模板** | 无 | 覆盖表单、数据展示、数据统计等常用场景话模板，请参考[页面模板库](https://www.npmjs.com/package/dd-cool-templates)。 |

## 配套工具

- 基础组件 Ding Design，请参考[Ding Design](https://ding.design/#/)。
- 页面模板库，请参考[页面模板库](https://www.npmjs.com/package/dd-cool-templates)。
