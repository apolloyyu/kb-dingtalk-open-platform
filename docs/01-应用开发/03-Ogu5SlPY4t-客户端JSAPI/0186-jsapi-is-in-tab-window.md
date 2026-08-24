---
title: "isInTabWindow"
source_url: "https://open.dingtalk.com/document/development/jsapi-is-in-tab-window"
namespace: "development"
slug: "jsapi-is-in-tab-window"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 跳转 > isInTabWindow"
doc_id: "uZBKbGiotR"
updated_at: "2025-08-27 18:06:26"
---

> Source: https://open.dingtalk.com/document/development/jsapi-is-in-tab-window
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 跳转 > isInTabWindow
> Updated: 2025-08-27 18:06:26

# isInTabWindow

调用isInTabWindow，判断当前页面是否为弹窗页面。

- 打开的页面不是弹窗页面：调用本jsapi方法，判断页面是否为弹窗窗口，判断结果为false。例如，在钉钉PC端工作台打开应用内页面，如下图所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4441893561/p444735.png)
- 打开的页面是弹窗页面：在打开的页面内调用本jsapi方法，判断页面是否为弹窗窗口，判断结果为true。
  ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4877793561/p444666.png)

> 目前只有使用PC端打开新弹窗页面方法才可以打开弹窗页面。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 6.5.10 | 6.5.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11659) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `result`（boolean，必填）：是否为弹窗。

## **示例****代码**

### 默认出入参

```
dd.isInTabWindow({
  success: (res) => {
    const { result } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "result": true }
```
