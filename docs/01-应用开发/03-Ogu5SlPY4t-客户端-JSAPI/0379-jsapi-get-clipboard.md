---
title: "getClipboard"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-clipboard"
namespace: "development"
slug: "jsapi-get-clipboard"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 剪贴板 > getClipboard"
doc_id: "iuuB4PrqfC"
updated_at: "2025-08-27 18:07:43"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-clipboard
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 剪贴板 > getClipboard
> Updated: 2025-08-27 18:07:43

# getClipboard

调用getClipboard，获取系统剪贴板的内容。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10148) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `text`（string）：剪切板数据。

## **示例****代码**

### 默认出入参

```
dd.getClipboard({
  success: (res) => {
    const { text } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "text": "我是数据" }
```
