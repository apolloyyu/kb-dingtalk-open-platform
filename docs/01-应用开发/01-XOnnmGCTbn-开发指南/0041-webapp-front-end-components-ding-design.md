---
title: "前端组件 (Ding Design)"
source_url: "https://open.dingtalk.com/document/dingstart/webapp-front-end-components-ding-design"
namespace: "dingstart"
slug: "webapp-front-end-components-ding-design"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 开发参考 > 前端组件 (Ding Design)"
doc_id: "8IU24N0hFH"
updated_at: "2026-01-22 20:01:15"
---

> Source: https://open.dingtalk.com/document/dingstart/webapp-front-end-components-ding-design
> Path: 应用开发 / 开发指南 / 开发网页应用 > 开发参考 > 前端组件 (Ding Design)
> Updated: 2026-01-22 20:01:15

# 前端组件 (Ding Design)

本文介绍了什么是 Ding Design，Ding Design 特性、组件详情与使用指南等内容。

## **什么是 Ding Design**

[Ding Design](https://ding.design) 是面向企业级应用的前端 UI 组件库，支持多端统一设计与开发，覆盖小程序、React Mobile 与 React PC 三大场景。

基于 TypeScript 构建，Ding Design 提供完整的类型定义与无障碍访问支持，帮助开发者提升开发效率与代码健壮性。同时，组件库遵循钉钉设计语言体系，确保与钉钉整体体验高度融合。

## **Ding Design** **特性**

- **多端适配**

  一套组件库同时支持小程序、React 移动端与 React 桌面端，降低多平台维护成本。无论用户在移动端还是 PC 端使用，都能获得一致的操作体验。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5723809671/p1047111.png)
- **TypeScript 支持**

  所有组件均使用 TypeScript 开发，提供完整的类型声明文件（.d.ts），支持 IDE 自动补全、参数提示和编译期错误检查，显著提升开发体验与项目可维护性。
- **主题定制**

  支持浅色与暗色主题动态切换，可通过配置项或 CSS 变量灵活调整主题风格，满足不同品牌风格需求。
- **开箱即用**

  提供常用基础组件（如 Button、Modal、Form、Table 等）和复杂业务组件，并配备详细的文档与示例代码，减少重复开发工作。

## 快速开始

安装 Ding Design 组件库，并在项目中引入和使用相关组件，如何使用请参考官方文档[快速上手](https://ding.design/?spm=ding_open_doc.document.0.0.600b696bRxJxKm#/cate/227/page/738)。

### **移动端组件**

#### **安装**

```
$ npm install dingtalk-design-mobile --save
```

#### **使用**

```
import { Button } from 'dingtalk-design-mobile';
ReactDOM.render(<Button type="primary">按钮<Button>, mountNode);
```

## 桌面端组件

#### **安装**

```
$ npm install dingtalk-design-desktop --save
```

#### **使用**

```
import { Button } from 'dingtalk-design-desktop';
ReactDOM.render(<Button type="primary">按钮<Button>, mountNode);
```

## 小程序组件

小程序组件 `dingtalk-design-miniapp` 是一套遵循钉钉设计规范的组件库， 涵盖基础组件和业务组件，由钉钉官方为钉钉小程序量身设计，让用户的体验和感知统一。 目前同时支持钉钉小程序与支付宝小程序。

#### **安装**

```
$ npm install dingtalk-design-miniapp --save
```

#### **使用**

`dingtalk-design-miniapp` 的使用方式与自定义组件的使用方式相同，以 `button` 为例：

##### **1.引入组件**

安装组件库后，在页面 `json` 文件中引入组件，例如：

```
{
    "component": true,
    "usingComponents": {
         "button": "dingtalk-design-miniapp/es/button/index"
    }
}
```

##### **2.使用组件**

在页面 axml 中添加组件和支持属性

```
<button type="primary" onCatchTap="onBtnCatchTap" className="button-default">主要操作</button>
```

##### **3.事件绑定**

按钮点击事件，上文中绑定了onBtnCatchTap， js 中实现

```
Page({
  onBtnCatchTap(e){
    console.log(e);
  }
})
```

## **组件详情与使用指南**

请进入 [ding.design](https://ding.design/#/cate/64/page/475) 官方站点，获取组件详情与使用指南。
