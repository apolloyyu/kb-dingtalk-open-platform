---
title: "链接跳转规范"
source_url: "https://open.dingtalk.com/document/development/link-jump-specification"
namespace: "development"
slug: "link-jump-specification"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "卡片规范设计 > 卡片规范 > 链接跳转规范"
doc_id: "RrUgnBam9l"
updated_at: "2025-09-23 19:18:47"
---

> Source: https://open.dingtalk.com/document/development/link-jump-specification
> Path: 互动卡片 / 模板搭建卡片 / 卡片规范设计 > 卡片规范 > 链接跳转规范
> Updated: 2025-09-23 19:18:47

# 链接跳转规范

本文介绍了卡片中打开链接的几种方式以及对应的协议和示例效果。

## **概述**

互动卡片支持链接的跳转。默认情况下，如果给卡片配置的是一个普通的 HTTP 协议的链接，如 https://dingtalk.com ，那么它会以新窗口的方式打开（在 PC 端以系统默认浏览器打开，移动端以普通 H5 页面打开）。

但钉钉除了常规的新窗口打开之外，还支持其他多种打开方式，如侧边栏打开、半浮层打开等。通过合理使用钉钉的统一跳转协议，即可实现这些跳转效果。

## **桌面端打开 URL**

### **以弹窗方式打开**

```
dingtalk://dingtalkclient/page/link?popup_wnd=true&url=${url}&title=${title}&width=${width}&height=${height}
```

| 参数 | 描述 | 目标值 | 示例值 |
| --- | --- | --- | --- |
| url | 弹窗打开的链接  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | https://www.dingtalk.com | https%3A%2F%2Fwww.dingtalk.com |
| title | 弹窗的标题  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | 钉钉官网 | %E9%92%89%E9%92%89%E5%AE%98%E7%BD%91 |
| width | 弹窗的宽度 | 700 | 700 |
| height | 弹窗的高度 | 800 | 800 |

#### **示例效果**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1765819661/p523426.png)

### **以侧边栏方式打开**

```
dingtalk://dingtalkclient/page/link?pc_slide=true&url=${url}
```

| 参数 | 描述 | 目标值 | 示例值 |
| --- | --- | --- | --- |
| url | 侧边栏打开的链接  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | https://www.dingtalk.com | https%3A%2F%2Fwww.dingtalk.com |

#### **示例效果**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0765819661/p523428.png)

## **移动端打开 URL**

### **以全屏方式打开**

```
dingtalk://dingtalkclient/page/link?url=${url}
```

| 参数 | 描述 | 目标值 | 示例值 |
| --- | --- | --- | --- |
| url | 全屏打开的链接  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | https://www.dingtalk.com | https%3A%2F%2Fwww.dingtalk.com |

#### **示例效果**

![mob_fullscreen](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0765819661/p523431.png)

### **以半浮层方式打开**

```
dingtalk://dingtalkclient/action/im_open_hybrid_panel?panelHeight=percent${percent}&hybridType=online&pageUrl=${pageUrl}
```

| 参数 | 描述 | 目标值 | 示例值 |
| --- | --- | --- | --- |
| pageUrl | 半浮层打开的链接  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | https://www.dingtalk.com | https%3A%2F%2Fwww.dingtalk.com |
| percent | 半浮层占手机屏幕高度的百分比（数字） | 83 | 83 |

#### **示例效果**

![mob_float](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7077480761/p534097.png)

## **多端通用 URL**

以上链接的打开方式都只是针对某个端才生效，如果想要实现在 PC 端以某种方式打开链接，在移动端又是通过另外一种方式进行打开，那么可以使用以下这个跳转协议：

```
dingtalk://dingtalkclient/action/open_platform_link?pcLink=${pcLink}&mobileLink=${mobileLink}
```

| 参数 | 描述 | 目标值 | 示例值 |
| --- | --- | --- | --- |
| pcLink | 桌面端的 dingtalk 协议链接，包含了打开方式等信息，详见上述**桌面端打开 URL**  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.dingtalk.com&pc\_slide=true | dingtalk%3A%2F%2Fdingtalkclient%2Fpage%2Flink%3Furl%3Dhttps%253A%252F%252Fwww.dingtalk.com%26pc\_slide%3Dtrue |
| mobileLink | 移动端的 dingtalk 协议链接，包含了打开方式等信息，详见上述**移动端打开 URL**  **[!IMPORTANT]**  需要进行 URI encode 转换处理 | dingtalk://dingtalkclient/action/im\_open\_hybrid\_panel?panelHeight=percent83&hybridType=online&pageUrl=https%3A%2F%2Fwww.dingtalk.com | dingtalk%3A%2F%2Fdingtalkclient%2Faction%2Fim\_open\_hybrid\_panel%3FpanelHeight%3Dpercent83%26hybridType%3Donline%26pageUrl%3Dhttps%253A%252F%252Fwww.dingtalk.com |

### **示例效果**

结合上述`pcLink`和`mobileLink`的示例值，最终的链接如下：

```
dingtalk://dingtalkclient/action/open_platform_link?pcLink=dingtalk%3A%2F%2Fdingtalkclient%2Fpage%2Flink%3Furl%3Dhttps%253A%252F%252Fwww.dingtalk.com%26pc_slide%3Dtrue&mobileLink=dingtalk%3A%2F%2Fdingtalkclient%2Faction%2Fim_open_hybrid_panel%3FpanelHeight%3Dpercent83%26hybridType%3Donline%26pageUrl%3Dhttps%253A%252F%252Fwww.dingtalk.com
```

展示效果如下：在桌面端打开了侧边栏，而在移动端则是以半浮层的形式打开链接。

![slide_and_float](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7077480761/p534098.png)
