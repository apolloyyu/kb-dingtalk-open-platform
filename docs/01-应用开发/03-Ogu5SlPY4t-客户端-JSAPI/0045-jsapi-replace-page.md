---
title: "replacePage"
source_url: "https://open.dingtalk.com/document/development/jsapi-replace-page"
namespace: "development"
slug: "jsapi-replace-page"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 导航栏 > replacePage"
doc_id: "I3064fdKpc"
updated_at: "2025-08-27 18:05:00"
---

> Source: https://open.dingtalk.com/document/development/jsapi-replace-page
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 导航栏 > replacePage
> Updated: 2025-08-27 18:05:00

# replacePage

调用 replacePage 替换页面，类似 web 端调用 location.replace 。

使用新的页面替换当前页面，当前页面会被立即销毁，展示新页面，无动画。

在 Android 端要实现 replace 效果，需要在目标 url 上拼上参数 `dd_enbale_replace=true` ，才能有 web 的 replace 行为。

例如原跳转地址：  
<https://open.dingtalk.com>  
Android 跳转地址需要修改为：  
<https://open.dingtalk.com?dd_enbale_replace=true>

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11612) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `url`（string，必填）：新的页面链接。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.replacePage({
  url: 'https://open.dingtalk.com',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
