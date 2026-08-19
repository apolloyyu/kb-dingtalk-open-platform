---
title: "AppLink的结构"
source_url: "https://open.dingtalk.com/document/development/structure-of-applink"
namespace: "development"
slug: "structure-of-applink"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > AppLink的结构"
doc_id: "m9ept0VmSm"
updated_at: "2026-07-21 09:26:20"
---

> Source: https://open.dingtalk.com/document/development/structure-of-applink
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > AppLink的结构
> Updated: 2026-07-21 09:26:20

# **AppLink的结构**

本文档介绍 AppLink 协议的结构、能力、使用场景及版本支持情况，帮助开发者通过标准 URL 在不同环境中打开钉钉客户端或其内部功能。本协议适用于企业内部应用、第三方企业应用以及小程序等类型的应用。开发者可通过配置 AppLink 实现跨平台跳转至钉钉功能页面，提升用户操作效率。

## **AppLink能力**

AppLink 是一种基于 HTTPS 的标准化 URL 协议，用于在移动和桌面端安全地唤起钉钉客户端并跳转到指定功能页面。相比传统的 deep link 协议（如 `dingtalk://`），AppLink 具备更好的兼容性与降级机制。

目前可通过 AppLink 打开的钉钉功能，请参考[已支持的协议](1396-open-applet.md)文档。

典型使用场景包括：

- 营销页面中嵌入“一键加入工作群”按钮，点击后直接唤起钉钉创建群聊；
- 企业官网提供“打开审批应用”入口，外部用户点击后自动跳转至钉钉审批首页；
- H5 页面引导用户打开某项微应用或小程序，实现无缝业务衔接。

当用户在不同环境点击 AppLink 时，行为如下：

- **在钉钉客户端内打开 AppLink**：

  将直接解析并跳转至对应的钉钉功能页面，无需中间页，体验流畅。
- **在钉钉客户端外部（如浏览器）打开 AppLink**：

  会首先跳转至一个中间页，该页面用于判断设备是否安装钉钉客户端。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4724809671/p1047658.png)中间页将提示用户下载钉钉或单击打开钉钉对应的功能。

## **AppLink结构**

AppLink 的完整格式为： `https://applink.dingtalk.com/{path}?{query}`，如下图所示：

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AXNkOM115pZEOY74/img/175f446d-e2a5-4f60-92bb-2588cd6406ba.png)

其结构由以下字段组成：

| **字段** | **值** | **说明** |
| --- | --- | --- |
| **scheme** | https | 固定值。 |
| **host** | applink.dingtalk.com | 固定值。 |
| **path** | 对应不同的协议 | - 页面类，例如：    - **/page/yunpan**：打开钉钉云盘   - **/page/****h5\_app\_open**：打开H5微应用 - 行为类，例如：    - **/action/creategroup**：创建群聊   - **/action/open\_mini\_app**：打开小程序应用 |
| **query** | 协议参数，不同的协议有不同的定义 | 例如：key1=value1&key2=value2 。  **[!NOTE]**  所有参数key 和 value 都要进行encodeURIComponent。 |

## **以降级方式打开**

AppLink 是 `dingtalk://`（DeepLink 协议）的升级版本，具备更强的容错与降级能力。

当用户设备上的钉钉版本不支持当前 AppLink 时，系统会自动降级处理：

1. 先尝试打开 AppLink 中间页；
2. 再通过传统 DeepLink 方式继续执行：`dingtalk://dingtalkclient/${path}`；
3. 若仍失败，则停留在下载/升级提示页。

AppLink 与 DeepLink 的 path 大部分保持映射一致，开发者可参考已支持的[AppLink的结构](#)文档进行兼容性适配。

## **支持版本情况**

在钉钉客户端内使用AppLink时，如果当前钉钉版本低于要求的最小钉钉版本时，将打开Applink网页，提示版本过低，需要升级钉钉客户端版本后使用。

| **钉钉客户端** | **IOS** | **Android** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥6.5.50 | ≥6.5.50 |

## **典型示例**

以下是使用 AppLink 的典型示例，帮助开发者快速验证功能。

- **生成带参数的 AppLink URL**

  以打开 H5 微应用为例，原始 URL 为： `https://applink.dingtalk.com/page/h5_app_open?appId=1234&corpId=ding16b241fd****4f7c288&appType=2&path=/a/index`

  构造 AppLink 跳转链接时，需对参数进行编码处理：

  ```
  const h5Url = '/a/index';
  const encodedUrl = encodeURIComponent(h5Url);
  const appLink = 'https://applink.dingtalk.com/page/h5_app_open?appId=1234&corpId=ding16b241fd****4f7c288&appType=2&path=%2Fa%2Findex';
  ```
- **如何判断是否成功打开钉钉功能**

  - 成功标志：钉钉客户端启动并显示目标页面内容。
  - 失败可能表现：停留在中间页、提示“版本不支持”、跳转空白页等。
- **常见失败情况及排查方法**

  - **问题1：点击无反应或跳转失败**

    检查是否对参数进行了encodeURIComponent；避免特殊字符未转义。
  - **问题2：提示“请升级钉钉版本”**

    当前客户端版本低于最低要求，请参照下文版本支持表进行升级。
  - **问题3：打开的是空白页或非预期页面**

    检查 path 是否拼写错误，参数是否符合目标协议规范。
