---
title: "获取设备唯一ID"
source_url: "https://open.dingtalk.com/document/development/obtain-the-unique-device-id"
namespace: "development"
slug: "obtain-the-unique-device-id"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取设备唯一ID"
doc_id: "haV7kQAx2d"
updated_at: "2025-10-15 17:02:28"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-unique-device-id
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取设备唯一ID
> Updated: 2025-10-15 17:02:28

# 获取设备唯一ID

## **基础信息**

获取用户设备唯一ID。

| **API名称** | **调用方式** | **支持的平台** |
| --- | --- | --- |
| dd.device.getUUID | 同步调用 | Android、iOS、HarmonyOS |

## **入参**

无

## **返回结果**

String类型。

> **[!IMPORTANT]**
>
> 设备ID仅保证一次安装期间的唯一。如果APP被卸载重装或者清除APP数据后，设备ID会发生变更。

## **示例代码**

Android-Java

```
ApiRequest request = new ApiRequest();
request.api = "dd.device.getUUID";

ApiResponse response = bundleContext.invokeSyncApi(request);
if (response != null) {
    String deviceId = response.getString();
}
```

Object C

```
id<DTKExternalNativeAPIServiceProtocol> handler = DTKExternalGetImpl(@"your_bundle_id", DTKExternalNativeAPIServiceProtocol);
NSString *apiName = @"dd.device.getUUID";
[handler invokeNativeAPI:apiName
            requestParam:^(id<DTKExternalAPIRequest>  _Nonnull param, id<DTKExternalAPIContext>  _Nonnull context) {}
                callback:^(NSDictionary * _Nonnull response) {
        NSString *UUID = response[@"UUID"];
        NSLog(@"dd.device.getUUID:%@", UUID);
}];
```

arkts

```
myBundle.invokeApi({ api: 'dd.device.getUUID'})
.then((data) => { 
  const uuid = data.getString('UUID')
})
.catch((e: Error) => { 
  myBundle.toast(`用例失败：${e.message}`) 
})
```
