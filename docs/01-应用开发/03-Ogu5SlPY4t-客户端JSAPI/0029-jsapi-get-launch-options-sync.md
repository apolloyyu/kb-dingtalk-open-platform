---
title: "getLaunchOptionsSync"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-launch-options-sync"
namespace: "development"
slug: "jsapi-get-launch-options-sync"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 基础 > getLaunchOptionsSync"
doc_id: "KdIjNadHAJ"
updated_at: "2025-08-27 18:04:57"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-launch-options-sync
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 基础 > getLaunchOptionsSync
> Updated: 2025-08-27 18:04:57

# getLaunchOptionsSync

调用dd.getLaunchOptionsSync获取小程序启动时的参数。

获取小程序启动时的参数。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10027) |

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

### 字段说明

- `query`（object，必填）：当前小程序的 query，从启动参数的 query 字段解析而来。
- `scene`（string，必填）：该字段暂无使用场景，可忽略。  
    
    
  > 说明 IDE模拟器可获取该字段值为"0000"，真机不支持获取该字段。
- `path`（string，必填）：当前小程序启动时进入的页面路径地址。

## **示例****代码**

### 默认出入参

```
const res = dd.getLaunchOptionsSync();
const { path, query, scene } = res;
```

返回对象示例：

```
{ "path": `path示例值`, "query": { "param1": "sss" }, "scene": "create" }
```
