---
title: "onKeyboardHide"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-keyboard-hide"
namespace: "development"
slug: "jsapi-on-keyboard-hide"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 键盘输入 > onKeyboardHide"
doc_id: "nFMIQKVD8q"
updated_at: "2025-08-27 18:06:11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-keyboard-hide
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 键盘输入 > onKeyboardHide
> Updated: 2025-08-27 18:06:11

# onKeyboardHide

监听键盘收起。

> 需要在 page 中设置该回调。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11577) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
Page({
  onKeyboardHide() {
    dd.alert({
      content: 'keyboard hide',
    });
  },
});
```
