---
title: "ExtSDKVersion"
source_url: "https://open.dingtalk.com/document/development/jsapi-ext-sdk-version"
namespace: "development"
slug: "jsapi-ext-sdk-version"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 基础 > ExtSDKVersion"
doc_id: "RjZwVkGEv2"
updated_at: "2025-08-27 18:04:55"
---

> Source: https://open.dingtalk.com/document/development/jsapi-ext-sdk-version
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 基础 > ExtSDKVersion
> Updated: 2025-08-27 18:04:55

# ExtSDKVersion

使用本接口获取基础库版本号。

小程序引擎版本不同，获取基础库版本号的API不同。目前钉钉小程序有V1引擎和V2引擎。

v1 引擎

dd.SDKVersion

v2 引擎

dd.ExtSDKVersion

兼容写法

const version = dd.ExtSDKVersion || dd.SDKVersion;

参考：

```
// page/API/sdk-version/sdk-version.js
Page({
  getSDKVersion() {
    dd.alert({
      content: dd.ExtSDKVersion || dd.SDKVersion,
    });
  }, 
});
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10005) |

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

（string）基础库版本号。 示例：`1.25.28`

## **示例****代码**

### 默认出入参

```
const res = dd.ExtSDKVersion();
console.log(res);
// res: '1.25.28'
```

返回对象示例：

```
"1.25.28"
```
