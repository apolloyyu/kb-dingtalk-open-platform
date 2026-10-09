---
title: "交互方式"
source_url: "https://open.dingtalk.com/document/development/interactive-mode"
namespace: "development"
slug: "interactive-mode"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 添加卡片交互 > 交互方式"
doc_id: "lKxzW22lfd"
updated_at: "2026-08-05 09:37:53"
---

> Source: https://open.dingtalk.com/document/development/interactive-mode
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 添加卡片交互 > 交互方式
> Updated: 2026-08-05 09:37:53

# 交互方式

本文介绍钉钉互动卡片所具备的交互方式，以及具体的使用方法。

## **卡片添加交互**

钉钉互动卡片具备互动能力，可以通过给按钮等交互组件添加点击事件即可。以按钮为例，在按钮的设置项里面，通过配置“按钮点击事件类型”即可为按钮添加交互能力。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3783985871/p550668.png)

## **交互方式概览**

| **交互方式** | **作用** | **核心配置项** |
| --- | --- | --- |
| [链接跳转](#6db6d7c08c4u3) | 点击后打开链接 | 链接类型、链接值、是否dtmd链接 |
| [回传请求](#2a2a907c7eq68) | 点击后发起回调请求到回调地址 | 回传参数、Toast文案、成功判定条件 |
| [复制内容](#d6608cfaaad65) | 点击后复制指定文字 | 复制内容 |
| [确认框](#7bacef46e1k9e) | 点击后弹出二次确认弹窗 | 标题、内容、确认/取消按钮文案 |
| [动作面板](#529c27ca9awjl) | 点击后弹出Actionsheet | 样式类型、动作名称、动作描述、动作类型 |
| [弹窗提示](#e38f5eb329eb8) | 点击后弹出Toast提示 | 提示内容、提示类型 |

下面详细介绍每种交互方式的配置方法。

## **链接跳转**

点击后打开指定链接。

### **配置项**

- **链接类型**：指定是否需要区分不同客户端。若无需区分，使用"统一链接"即可。
- **链接值**：所要打开的链接地址，可固定或绑定变量。必填，值为空时点击无响应。
- **是否 dtmd 链接**：若链接以 `dtmd://` 开头，需开启此选项，否则协议不生效。

> **[!NOTE]**
>
> 若希望链接在钉钉客户端内以侧边栏/半浮层方式打开，参考[链接跳转规范](0040-link-jump-specification.md)。

## 回传请求

点击后向回调地址发起请求。

### 配置项

- **回传参数**：指定回调请求的上下文参数（如点赞请求中的 like 参数），可配置固定值或绑定变量。业务接收回调后可解析这些参数。
- **请求成功 Toast 文案**：请求成功后客户端弹出的提示文案。
- **请求失败 Toast 文案**：请求失败后客户端弹出的提示文案。
- **请求成功判定条件**：指定业务如何判断请求成功。只有配置此项，上述 Toast 文案才能正常显示。

### 请求内容示例

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "XXXXXX",
    "userId": "XXXXXX",
    "value": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]},\"params\":{\"like\":\"true\"}}"
}
```

其中 `value` 字段包含卡片请求上下文：

- `actionIds`：当前按钮的 id。
- `params`：请求的参数。

## 复制内容

点击后复制指定文字内容。

### 配置项

- **复制内容**：所要复制的文本，支持使用变量。

## 确认框

点击后弹出二次确认弹窗。

### 配置项

- 确认框标题：弹窗标题，支持变量和多语言配置。
- 确认框内容：弹窗内容，支持变量和多语言配置。
- 确认按钮文案：确认按钮文案，支持变量和多语言配置。
- 取消按钮文案：取消按钮文案，支持变量和多语言配置。

### 效果展示

- **PC 端效果**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2268750761/p523731.png)
- **移动端效果**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2268750761/p523733.png)

## 动作面板

点击后弹出动作面板（Actionsheet）。

### 配置项

- **样式类型**：动作选项的样式，有两种类型：

  - 默认样式
  - 警告样式（红色字展示）
- **动作名称**：动作选项的文案内容。
- **动作描述**：动作选项的描述内容（非必填）。
- **动作类型**：点击动作后触发的事件，可配置"打开链接"或"回传请求"。

### 效果展示

- **PC 端效果**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2268750761/p523748.png)
- **移动端效果**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2268750761/p523752.png)

## 弹窗提示

点击后弹出 Toast 提示。

### 配置项

- **提示内容**：所要显示的 Toast 文案。
- **提示类型**：Toast 的类型，有三种：

  - 默认
  - 成功
  - 失败

  三者区别在于 Toast 提示的 icon，**目前只在 PC 端生效**。
