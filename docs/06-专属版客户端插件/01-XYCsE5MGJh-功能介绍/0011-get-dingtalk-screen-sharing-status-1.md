---
title: "获取钉钉屏幕分享状态"
source_url: "https://open.dingtalk.com/document/development/get-dingtalk-screen-sharing-status-1"
namespace: "development"
slug: "get-dingtalk-screen-sharing-status-1"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取钉钉屏幕分享状态"
doc_id: "CqwwEua5WG"
updated_at: "2025-10-15 17:02:31"
---

> Source: https://open.dingtalk.com/document/development/get-dingtalk-screen-sharing-status-1
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取钉钉屏幕分享状态
> Updated: 2025-10-15 17:02:31

# 获取钉钉屏幕分享状态

## **基础信息**

常用于安全沙箱场景，假如你的安全沙箱提供了防止截屏的能力，那么在用户视频会议期间，为了能够做到屏幕分享需要在此期间特殊处理（比如暂时关闭禁止截屏功能）。

| **API名称** | **调用方式** | **支持的平台** |
| --- | --- | --- |
| dd.conference.getScreenCastStatus | 异步调用 | Android、iOS、HarmonyOS |

## **入参**

无

## **返回结果**

返回Map数据。

| **参数** | **类型** | **描述** |
| --- | --- | --- |
| isCasting | String | 0：未分享； 1：正在分享屏幕中。 |

## **变更事件**

**Android / HarmonyOS 平台**

由于屏幕分享是实时的，为了能够及时做出业务处理，Android/Harmony平台上可以监听事件通知。

> **[!NOTE]**
>
> 变更事件需要先使用dd.conference.getScreenCastStatus API触发截屏状态获取后，后续方可收到事件通知。

Android-Java

```
// 变更事件监听
@Event(event={"conference.screenshare.change"})
public class ExclusiveReceiver implements EventReceiver {

    @Override
    public void onEvent(String event, Bundle bundle) {
        String isCasting = bundle.getString("isCasting");
        ...
    }
}
```

arkts

```
interface ScreenModel {
  isCasting?: boolean
}

myBundle.onEvent('conference.screenshare.change', (model: ScreenModel) => {
  console.error('tc', `receive event: ${model.isCasting}`)
})
```

## **示例代码**

Android-Java

```
ApiRequest request = new ApiRequest();
request.api = "dd.conference.getScreenCastStatus";
ApiResponse response = bundleContext.invokeApi(request);
Map<String, String> resMap = response.getMapResult();
String isCasting = resMap.get("isCasting");
... ...
```

Object C

```
id<DTKExternalNativeAPIServiceProtocol> handler = DTKExternalGetImpl(@"your_bundle_id", DTKExternalNativeAPIServiceProtocol);
NSString *apiName = @"dd.conference.getScreenCastStatus";
[handler invokeNativeAPI:apiName
            requestParam:^(id<DTKExternalAPIRequest>  _Nonnull param, id<DTKExternalAPIContext>  _Nonnull context) { }
                callback:^(NSDictionary * _Nonnull response) {
    NSString *isCasting = response[@"isCasting"];
}];
```

arkts

```
myBundle.invokeApi({
  api: "dd.conference.getScreenCastStatus"
}as ApiRequest).then((result) => {
  console.warn('testcase', `result=${result.getBool('isCasting')}`)
}).catch((e: Error) => {
})
```
