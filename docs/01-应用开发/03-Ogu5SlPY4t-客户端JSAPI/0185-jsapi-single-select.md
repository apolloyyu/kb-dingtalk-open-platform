---
title: "singleSelect"
source_url: "https://open.dingtalk.com/document/development/jsapi-single-select"
namespace: "development"
slug: "jsapi-single-select"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 选项选择器 > singleSelect"
doc_id: "EvvjcLchNm"
updated_at: "2025-08-27 18:06:25"
---

> Source: https://open.dingtalk.com/document/development/jsapi-single-select
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 选项选择器 > singleSelect
> Updated: 2025-08-27 18:06:25

# singleSelect

调用singleSelect，进行下拉框单选配置。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1605834061/p177833.png)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11616) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11616) |

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

- `source`（array，必填）：下拉控件的内容。
- `source[].key`（string，必填）：显示文本。
- `source[].value`（string，必填）：文本对应的值。
- `selectedKey`（string）：默认选中的key值。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `key`（string，必填）
- `value`（string，必填）

## **示例****代码**

### 默认出入参

```
dd.singleSelect({
  source: [
    {
      key: '选项1', //显示文本
      value: '123', //值，
    },
    {
      key: '选项2',
      value: '234',
    },
  ],
  selectedKey: '选项1',
  success: (res) => {
    const { key, value } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "key": `key示例值`, "value": `value示例值` }
```
