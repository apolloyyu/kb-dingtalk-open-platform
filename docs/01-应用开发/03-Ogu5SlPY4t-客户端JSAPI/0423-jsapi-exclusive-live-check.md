---
title: "exclusiveLiveCheck"
source_url: "https://open.dingtalk.com/document/development/jsapi-exclusive-live-check"
namespace: "development"
slug: "jsapi-exclusive-live-check"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "专属开放 > exclusiveLiveCheck"
doc_id: "9MdZZuRsQD"
updated_at: "2025-08-27 18:08:47"
---

> Source: https://open.dingtalk.com/document/development/jsapi-exclusive-live-check
> Path: 应用开发 / 客户端JSAPI / 专属开放 > exclusiveLiveCheck
> Updated: 2025-08-27 18:08:47

# exclusiveLiveCheck

调用exclusiveLiveCheck，专属实人认证，通过人脸活体实现账号、人和身份信息的多重比对，人脸比对。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.5.40 | 6.5.40 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11641) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `agentId`（string，必填）：钉钉应用agentId。
- `corpId`（string，必填）：当前企业的corpId。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `photoStatus`（number，必填）：是否对比成功：  
    
  \* 1：对比验证成功   
  \* 2：对比验证失败

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |

## **示例****代码**

### 默认出入参

```
dd.exclusiveLiveCheck({
  corpId: 'ding1234',
  agentId: '278xxxxx',
  success: (res) => {
    const { photoStatus } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "photoStatus": 1 }
```
