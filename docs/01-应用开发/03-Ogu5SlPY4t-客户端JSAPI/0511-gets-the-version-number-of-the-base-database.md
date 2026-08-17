---
title: "获取基础库版本号"
source_url: "https://open.dingtalk.com/document/development/gets-the-version-number-of-the-base-database"
namespace: "development"
slug: "gets-the-version-number-of-the-base-database"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > 获取基础库版本号"
doc_id: "cHWLr8DbJG"
updated_at: "2025-09-17 20:58:42"
---

> Source: https://open.dingtalk.com/document/development/gets-the-version-number-of-the-base-database
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > 获取基础库版本号
> Updated: 2025-09-17 20:58:42

# 获取基础库版本号

使用本接口获取基础库版本号。

小程序引擎版本不同，获取基础库版本号的API不同。目前钉钉小程序有V1引擎和V2引擎。

- **v1 引擎**

  dd.SDKVersion
- **v2 引擎**

  dd.ExtSDKVersion
- **兼容写法**

  const version = dd.ExtSDKVersion || dd.SDKVersion;

## **示例代码**

> **[!IMPORTANT]**
>
> 仅供参考，代码逻辑请勿依赖此值。

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

## **返回值**

为 String 类型，表示基础库版本号。
