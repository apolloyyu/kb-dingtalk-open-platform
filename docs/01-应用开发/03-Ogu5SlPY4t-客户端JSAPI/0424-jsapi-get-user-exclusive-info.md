---
title: "getUserExclusiveInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-user-exclusive-info"
namespace: "development"
slug: "jsapi-get-user-exclusive-info"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "专属开放 > getUserExclusiveInfo"
doc_id: "kwKf89mOyx"
updated_at: "2025-08-27 18:08:48"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-user-exclusive-info
> Path: 应用开发 / 客户端JSAPI / 专属开放 > getUserExclusiveInfo
> Updated: 2025-08-27 18:08:48

# getUserExclusiveInfo

调用getUserExclusiveInfo，获取钉钉客户端是否为专属钉钉。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.15 | 6.0.15 | 7.0.0 | 6.0.17 | 6.0.17 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11644) |
| 小程序 | 6.0.15 | 6.0.15 | 7.0.0 | 6.0.17 | 6.0.17 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11644) |

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

- `isExclusiveApp`（number，必填）：客户端类型：  
    
  \* 0：标准钉钉  
  \* 1：专属钉钉

## **示例****代码**

### 默认出入参

```
dd.getUserExclusiveInfo();
```

`success`返回对象示例：

```
{ "isExclusiveApp": 1 }
```
