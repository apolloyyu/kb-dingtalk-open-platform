---
title: "开发自定义JSAPI"
source_url: "https://open.dingtalk.com/document/development/client-exclusive-development-custom-jsapi"
namespace: "development"
slug: "client-exclusive-development-custom-jsapi"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "iOS 插件 > 开发自定义JSAPI"
doc_id: "AvuapKEK6h"
updated_at: "2026-08-12 09:20:47"
---

> Source: https://open.dingtalk.com/document/development/client-exclusive-development-custom-jsapi
> Path: 专属版客户端插件 / iOS 插件 / iOS 插件 > 开发自定义JSAPI
> Updated: 2026-08-12 09:20:47

# 开发自定义JSAPI

当你开发的插件是期望给H5应用/小程序扩展能力时，可参考本文定义扩展JSAPI。

## 基本原理

基于钉钉开放框架，插件SDK内部可自定义扩展JSAPI，H5应用/小程序可通过开放框架的扩展JsBridge调用专属插件SDK的类。如下图所示：

![流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9890753661/p490334.jpg)

## **步骤一: 注册JSAPI**

```
DTKExternalJSAPIRegister(bundleId, handler)
```

- **接口文件**：DTKExternalJSAPIProtocol.h
- **参数说明**：

  - bundleId: SDK的bundleId
  - handler：能够处理JSAPI的类名，由SDK实现，专属钉钉收到所有JSAPI请求后，会调用到handler中处理

## **步骤二: 实现JSAPI**

注册的JSAPI会分发到这个方法中来处理：

```
- (void)handleRequest:(id<DTKExternalAPIRequest>)request
 					withContext:(id<DTKExternalJSAPIContext>)context
 						 callback:(DTKExternalAPICallback)callback;
```

- **参数说明**：

  - request

    - apiName：JSAPI的名称
    - requestParams：请求附带的参数
  - context

    - webViewControllerr：容器vc
    - webView：当前view
    - tinyAppUrl：前端页面地址
  - callback

    - 回调给前端的内容

      > **[!IMPORTANT]**
      >
      > 无论成功还是失败，都需要调用callback，告知小程序（H5微应用）。
- **代码示例**：

  ```
  DTKExternalJSAPIRegister(demo_app_id, DTKExternalJSApiDemo)
    @implementation DTKExternalJSApiDemo

    - (void)handleRequest:(nonnull id<DTKExternalAPIRequest>)request
            withContext:(nonnull id<DTKExternalJSAPIContext>)context
               callback:(nonnull DTKExternalAPICallback)callback {
      
                 if ([request.apiName isEqualToString:@"demo.file.delete"]) {
                   NSDictionary *params = request.requestParams;
                   //do something
                   NSDictionary *responseData = @{ @"result": @"good"};
                   if (callback) {
                     callback(responseData);
                   }
                 }
               }
  ```

## **步骤三：调试JSAPI**

在你的前端应用还没准备好时，可以先使用钉钉官方提供的小程序调用你的SDK。

1. 工作台请切换到“钉钉Native定制扩展开放”组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632059.png)
2. 点击工作台应用“专属插件JSAPI调试”，如下图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632060.png)![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632061.png)

   假如你的账号无法加入该组织，也可以通过扫码唤起小程序：

   ![deployCode_1687682700230.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1904867861/p685922.png)

   - BundleID：可不填
   - API：插件SDK中JsMethod定义的JSAPI值
   - 参数：输入参数名和参数值，然后点击“添加参数”将kv值添加的请求中，可添加多个
   - 执行：根据上面的输入发起JSAPI调用

     > **[!NOTE]**
     >
     > 扩展JSAPI默认不支持钉钉账号**登录前**调用，如果有需求，请联系钉钉侧项目经理申请开通。

## **步骤四：前端调用JSAPI**

### **调用Native SDK**

- **JSAPI**: exclusive.sdk.invoke
- **参数说明**：

  - bundle\_id: SDK的bundleId
  - api：SDK定义的JSAPI，比如 "demo.file.delete"
  - request\_params：请求附带的参数
- **代码示例**：

  ```
  import * as dd from 'dingtalk-jsapi';
  dd._invoke(
    "exclusive.sdk.invoke",
    {
      bundle_id:'demo_sdk',
        api: 'demo.file.delete' ,
        request_params: {
        ... ...
      },
      onSuccess : function( event ){
        console.log( JSON.stringify(event))
          },
      onFail:function(failErr) {
        console.log( {failErr} )
          }
    }
  ).then(() => {
         console.log( 'invoke done' )
         }).catch((err) => {
    console.error( JSON.stringify(err) )
    });
  ```

### **监听Native SDK事件**

- **JSAPI**: exclusive.sdk.subscribe、exclusive.sdk.unsubscribe，请务必成对使用
- **参数说明**：

  - bundle\_id: SDK的BundleID
  - subject\_id：监听的事件，比如 "demo.download\_process"
- **代码示例**：

  ```
  import * as dd from 'dingtalk-jsapi';
  dd._invoke(
    "exclusive.sdk.subscribe",
    {
      bundle_id:'demo_sdk',
      subject_id: 'demo.download_process' ,	
      ...,
      ...,
      onSuccess : function( event ){
        console.log( JSON.stringify(event))
      },
      onFail:function(failErr) {
        console.log( {failErr} )
      }
    }
  ).then(() => {
    console.log( 'invoke done' )
  }).catch((err) => {
    console.error( JSON.stringify(err) )
  });
  ```

### **Native SDK发送事件**

- **接口文件**：DTKExternalJSEventProtocol.h
- **参数说明**：

  - eventName：事件名称
  - params：事件参数，透传给JS
- **代码示例**：

  ```
  id<DTKExternalJSEventProtocol> handler = DTKExternalGetImpl(@"your_bundle_id", DTKExternalJSEventProtocol);
  [handler invokeJsEventName:@"demo.download_process" params:@{@"param1" : @"1"}];
  ```
