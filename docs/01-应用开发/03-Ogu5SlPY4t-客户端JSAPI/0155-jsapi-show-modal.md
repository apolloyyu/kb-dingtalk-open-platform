---
title: "showModal"
source_url: "https://open.dingtalk.com/document/development/jsapi-show-modal"
namespace: "development"
slug: "jsapi-show-modal"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 交互反馈 > showModal"
doc_id: "mFMBnsfhaV"
updated_at: "2025-08-27 18:06:06"
---

> Source: https://open.dingtalk.com/document/development/jsapi-show-modal
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 交互反馈 > showModal
> Updated: 2025-08-27 18:06:06

# showModal

增强版modal弹浮层

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11615) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11615) |

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

- `cells`（array）：浮层元素数组，每一个item为一个包含image、title、content内容的对象。
- `image`（string）：图片地址。
- `title`（string）：标题。
- `content`（string）：文本内容。
- `buttonLabels`（array，必填）：按钮列表，至少有一个按钮，最多两个按钮。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `buttonIndex`（string，必填）：被点击按钮的索引。  
    
  > 从0开始。

## **示例****代码**

### 默认出入参

```
dd.showModal({
  cells: [
    {
      image:
        'https://img.alicdn.com/tfs/TB1KzrwRFXXXXasXXXXXXXXXXXX-540-380.png',
      title: 'DEMO版本更新',
      content: '图片尺寸是540x380;',
    },
    {
      image:
        'https://img.alicdn.com/tfs/TB1KzrwRFXXXXasXXXXXXXXXXXX-540-380.png',
      title: 'DEMO版本更新',
      content: '图片尺寸是540x380;',
    },
  ],
  image: 'image示例值',
  title: 'title示例值',
  content: 'content示例值',
  buttonLabels: ['了解更多', '知道了'],
  success: (res) => {
    const { buttonIndex } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "buttonIndex": "1" }
```
