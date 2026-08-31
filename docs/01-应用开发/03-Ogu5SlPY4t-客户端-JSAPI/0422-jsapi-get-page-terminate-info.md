---
title: "getPageTerminateInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-page-terminate-info"
namespace: "development"
slug: "jsapi-get-page-terminate-info"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 内存不足处理 > getPageTerminateInfo"
doc_id: "Gv3415gtWI"
updated_at: "2025-10-16 15:45:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-page-terminate-info
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 内存不足处理 > getPageTerminateInfo
> Updated: 2025-10-16 15:45:36

# getPageTerminateInfo

获取WebView崩溃信息

获取 WebView 崩溃次数，判断是否发生了崩溃

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11927) |
| 小程序 | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11927) |

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

### 出参

- `terminateTimes`（number，必填）：WebView 崩溃次数，注意：页面跳转后次数不会重置

## **示例****代码**

### 默认Demo标题

```
dd.getPageTerminateInfo({
  success: (res) => {
    const { terminateTimes } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "terminateTimes": 83 }
```
