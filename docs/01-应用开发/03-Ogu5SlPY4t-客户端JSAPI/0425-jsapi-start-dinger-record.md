---
title: "startDingerRecord"
source_url: "https://open.dingtalk.com/document/development/jsapi-start-dinger-record"
namespace: "development"
slug: "jsapi-start-dinger-record"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "DingTalk A1 > startDingerRecord"
doc_id: "6IuPN8RFH8"
updated_at: "2026-02-25 10:59:52"
---

> Source: https://open.dingtalk.com/document/development/jsapi-start-dinger-record
> Path: 应用开发 / 客户端JSAPI / DingTalk A1 > startDingerRecord
> Updated: 2026-02-25 10:59:52

# startDingerRecord

DingTalk A1 发起录音

DingTalk A1 发起录音

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 8.2.10 | 8.2.10 | 8.0.27 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11937) |
| 小程序 | 8.2.10 | 8.2.10 | 8.0.27 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11937) |

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

- `templateId`（string）：纪要模板 ID
- `businessOrder`（string）：业务自定义 ID

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### fid

（number）录音记录ID 示例：`12345`

## **示例****代码**

### 默认Demo标题

```
dd.startDingerRecord({
  templateId: 'xxx',
  businessOrder: 'xxx',
  success: (res) => {
    // res: 12345
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
12345
```
