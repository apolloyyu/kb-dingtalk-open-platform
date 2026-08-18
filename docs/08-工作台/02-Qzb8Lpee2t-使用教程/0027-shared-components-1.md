---
title: "共享组件"
source_url: "https://open.dingtalk.com/document/dingstart/shared-components-1"
namespace: "dingstart"
slug: "shared-components-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "合作伙伴教程 > 共享组件"
doc_id: "PtVuXsNe9A"
updated_at: "2025-10-21 14:09:16"
---

> Source: https://open.dingtalk.com/document/dingstart/shared-components-1
> Path: 工作台 / 使用教程 / 合作伙伴教程 > 共享组件
> Updated: 2025-10-21 14:09:16

# 共享组件

本文档介绍共享组件的相关信息。

## 什么是共享组件

共享组件是指钉钉合作伙伴采用工作台[全代码组件](0008-dashboard-overview-workbench.md)或[低代码模式](0006-add-self-built-interactive-cards-to-the-workbench.md)的开发模式，开发独立组件，并且将组件提交上架，最终成为钉钉的官方共享组件，这类组件面向钉钉所有组织开放。

共享组件核心由两部分组成：

- **代码和配置 ：**组件上架时会上传代码和配置到钉钉的代码库，上架后代码和配置归属于钉钉。合作伙伴可以持续对代码和配置进行优化，验收完成后生效到用户。
- **服务端数据：**共享组件的服务端数据必须是**钉钉官方**提供的数据，比如钉钉开发平台提供的各类api接口。不允许使用合作伙伴自己的服务接口。

## **如何开发共享组件**

共享组件采用[全代码组件](0008-dashboard-overview-workbench.md)或[低代码组件](0006-add-self-built-interactive-cards-to-the-workbench.md)的开发形式，唯一的区别是数据源（服务端数据接口）必须采用钉钉开放平台API的方式。

数据传输架构图如下：

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/0QvjnAMjjbB3nXo5/img/d322e407-6ae7-4971-9906-cea12bd25032.png)

### **前端SDK**

组件调用开放平台API的SDK示例如下：

```
const data = await getSdk().request({
  // 示例
  type: 'OPEN_API', // type类型固定为OPEN_API
  method: 'GET', // GET或POST
  path: '/v1.0/calendar/users/Y9za3KXqU2siE/calendars/primary/events',
 	host: 'oapi.dingtalk.com',
	headParams: '{}',    // json 字符串格式，生效到http协议的头部, 没有可以为空
 	params: '{}',    // json 字符串格式，生效到http协议请求的url参数, 没有可以为空
 	body: '{"language":"zh_CN", "userid":"0828416124358791"}' // json 字符串格式，生效到http协议请求的body, 没有可以为空
});
```

> **[!IMPORTANT]**
>
> 调用钉钉开放平台API时，尽量采用新版本API。

## 共享组件的规范

共享组件是钉钉合作伙伴贡献自己的产品和开发能力给钉钉，帮助钉钉丰富工作台组件生态。

**合作伙伴的责任&义务**：如果共享组件出现功能性问题或者用户投诉反馈，合作伙伴有责任和义务在收到钉钉优化意见后第一时间进行问题定位和修复，并且在问题修复后重新上架生效。

**合作伙伴的收益**：所有共享组件在工作台设计器中都会透出服务商信息，以便导流给合作伙伴，促成商机。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/0QvjnAMjjbB3nXo5/img/d3c098fc-7a02-4d9c-a5dc-13be369e543d.png)

## **共享组件验收上架**

共享组件以官方组件的形式提供给所有钉钉工作台用户使用，因此组件在验收环节会相对严格，必须满足以下基础要求。

1. 安全稳定，在各种情况下组件不奔溃。
2. 样式整洁美观。
3. 功能定位清晰，交互方便简洁 。

验收由钉钉工作台侧的产品和设计同学共同把关，验收一旦通过，开发者即可提交发布，线上生效。

> **[!NOTE]**
>
> - 共享组件目前还在共创阶段，如有关于共创组件的开发和上架需求，可以扫描下方钉钉群二维码，加入群内反馈。
> - 基于验收要求，建议开发者提前准备好产品设计稿，扫码加入共创群，提供给钉钉侧的产品和设计同学。
> - 共享组件在共创期间，合作伙伴只需要开发好自己的组件，并保证体验和稳定性，钉钉侧会负责帮助合作伙伴的组件上架，让所有钉钉组织用户可以使用和体验组件。

![iShot_2023-03-08_09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0799328761/p579080.png)

## **共享组件实践案例**

本案例为日程组件为例，日程组件通过调用钉钉API获取用户实时日程数据。该组件功能定位清晰，交互方便简单，样式简洁美观。标准工作台用户可以在组件中心添加日程组件，定制工作台用户可在设计器添加日程组件，进行体验。

![workbench-pic1..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8903842861/p638108.png)
