---
title: "stopDingerRecord"
source_url: "https://open.dingtalk.com/document/development/jsapi-stop-dinger-record"
namespace: "development"
slug: "jsapi-stop-dinger-record"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "DingTalk A1 > stopDingerRecord"
doc_id: "1mcVtht3gZ"
updated_at: "2026-02-05 20:56:37"
---

> Source: https://open.dingtalk.com/document/development/jsapi-stop-dinger-record
> Path: 应用开发 / 客户端 JSAPI / DingTalk A1 > stopDingerRecord
> Updated: 2026-02-05 20:56:37

# stopDingerRecord

DingTalk A1 停止录音

DingTalk A1 停止录音

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 8.2.10 | 8.2.10 | 8.0.25 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11938) |
| 小程序 | 8.2.10 | 8.2.10 | 8.0.25 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11938) |

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

### fid

（number）录音记录ID 示例：`12345`

## **示例****代码**

### 默认Demo标题

```
dd.stopDingerRecord({
  success: (res) => {
    // res: 1
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
1
```
