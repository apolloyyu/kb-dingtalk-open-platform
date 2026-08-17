---
title: "open-avatar 头像组件"
source_url: "https://open.dingtalk.com/document/development/mini-app-open-avatar"
namespace: "development"
slug: "mini-app-open-avatar"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > open-avatar 头像组件"
doc_id: "LBIJ6qHiMH"
updated_at: "2025-09-17 20:58:35"
---

> Source: https://open.dingtalk.com/document/development/mini-app-open-avatar
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > open-avatar 头像组件
> Updated: 2025-09-17 20:58:35

# open-avatar 头像组件

本文介绍头像组件的使用。

open-avatar 头像组件用于在小程序中渲染一个钉钉用户头像，使用时只需要填写用户的 ID 信息。

> **[!IMPORTANT]**
>
> 支持此组件的钉钉版本最低为4.6.6**。**开发者可以使用 canIUse('open-avatar') 判断兼容性。

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| userId | String | 用户的userid，**默认值**：空。   - 企业内部应用   小程序使用userid。   - 第三方企业应用   小程序使用userid。 |
| openId | String | 第三方个人应用，小程序使用 openId，获取方法请参考免登接入。  **默认值**：空。 |
| nickName | String | 用户昵称。  **默认值**：空。 |
| avatar | String | 用户头像图片地址。  **默认值**：空。 |
| size | String | - **tiny**: 24px - **small**: 32px - **normal**: 36px - **big**: 40px - **large**: 48px - **huge**: 56px   **默认值**：normal。 |
| shape | String | 头像UI风格。   - **circle**：圆形 - **square**：带圆角方形   **[!IMPORTANT]**  此参数仅支持基础库为**1.24.29及****以上**版本。 |

**头像显示规则**

- 如果传了 nickName 和 avatar ，将优先以 nickName 和 avatar 来展示头像。
- 如果没有传 nickName 和avatar，而是传了userId / openId ，该组件会用 userId / openId 去钉钉服务端获取用户信息（获取用户信息是自动的，不需要小程序开发者干预）。

## 示例代码

第三方企业小程序渲染用户头像示例：

```
<open-avatar
    userId="12345"
    size="normal"></open-avatar>
```
