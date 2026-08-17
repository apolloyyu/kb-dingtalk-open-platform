---
title: "获取专属配置"
source_url: "https://open.dingtalk.com/document/development/get-exclusive-configuration"
namespace: "development"
slug: "get-exclusive-configuration"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取专属配置"
doc_id: "XHDXlsoAco"
updated_at: "2025-10-15 17:02:29"
---

> Source: https://open.dingtalk.com/document/development/get-exclusive-configuration
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取专属配置
> Updated: 2025-10-15 17:02:29

# 获取专属配置

## **基础信息**

获取插件SDK的专属配置参数，配置参数需同钉钉方约定，并配置在钉钉平台上，登录后可获取。

> **[!NOTE]**
>
> 只支持在主进程中使用，需要登录态（由于首次下发会有延迟，onLogin事件中建议延迟2s获取）。

| **API名称** | **调用方式** | **支持的平台** |
| --- | --- | --- |
| dd.exclusive.getConfig | 异步调用 | Android、iOS |

## **入参**

无

## **返回结果**

String 类型。

> **[!IMPORTANT]**
>
> 返回值是一个JSON格式的字符串，Key-Value均为插件开发者提供的信息，钉钉平台仅做透传。

## **示例代码**

Android-Java

```
ApiRequest request = new ApiRequest();
request.api = "dd.exclusive.getConfig";

ApiResponse apiResponse = bundleContext.invokeApi(request);
if (apiResponse != null && apiResponse.isSuccess()) {
    // 成功处理
    String jsonResult = apiResponse.getString();
    JSONObject json = new JSONObject(jsonResult);
    json.optString("xxxx");
    // 注意此处的Json异常处理 
    // ... ...
}
```

Object C

```
id<DTKExternalNativeAPIServiceProtocol> handler = DTKExternalGetImpl(@"your_bundle_id", DTKExternalNativeAPIServiceProtocol);
NSString *apiName = @"dd.exclusive.getConfig";
[handler invokeNativeAPI:apiName
            requestParam:^(id<DTKExternalAPIRequest>  _Nonnull param, id<DTKExternalAPIContext>  _Nonnull context) { }
                callback:^(NSDictionary * _Nonnull response) {
    //为JSON格式，请根据实际需求解析使用
    NSDictionary *data = response[@"data"];
}];
```
