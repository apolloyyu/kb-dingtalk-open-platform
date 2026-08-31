---
title: "getAppIdSync"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-app-id-sync"
namespace: "development"
slug: "jsapi-get-app-id-sync"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 基础 > getAppIdSync"
doc_id: "fXlVpTFjNT"
updated_at: "2025-08-27 18:04:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-app-id-sync
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 基础 > getAppIdSync
> Updated: 2025-08-27 18:04:56

# getAppIdSync

调用dd.getAppIdSync同步获取小程序的AppId，即MiniAppId。

同步获取小程序的AppId，即MiniAppId。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10002) |

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

### appId

（string） 示例：`当前小程序的AppId，即MiniAppId。`

## **示例****代码**

### 默认出入参

```
const res = dd.getAppIdSync();
console.log(res);
// res: '当前小程序的AppId，即MiniAppId。'
```

返回对象示例：

```
"当前小程序的AppId，即MiniAppId。"
```
