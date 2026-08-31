---
title: "multiSelect"
source_url: "https://open.dingtalk.com/document/development/jsapi-multi-select"
namespace: "development"
slug: "jsapi-multi-select"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 选项选择器 > multiSelect"
doc_id: "K1vqWXdNbY"
updated_at: "2025-08-27 18:06:25"
---

> Source: https://open.dingtalk.com/document/development/jsapi-multi-select
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 选项选择器 > multiSelect
> Updated: 2025-08-27 18:06:25

# multiSelect

调用multiSelect，进行下拉框多选配置。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11617) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11617) |

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

- `options`（array，必填）：待选选项列表。
- `selectOption`（array）：已选选项列表。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（array）返回结果为数组，包含用户选中的index列表，从0开始。

## **示例****代码**

### 默认出入参

```
dd.multiSelect({
  options: ['选项1', '选项2', '选项3', '选项4'],
  selectOption: [`selectOption示例值1`, `selectOption示例值2`],
  success: (res) => {
    // res: [59, 95]
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
[49, 31]
```
