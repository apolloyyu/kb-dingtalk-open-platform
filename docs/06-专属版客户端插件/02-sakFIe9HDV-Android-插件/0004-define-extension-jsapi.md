---
title: "开发自定义JSAPI"
source_url: "https://open.dingtalk.com/document/development/define-extension-jsapi"
namespace: "development"
slug: "define-extension-jsapi"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 开发自定义JSAPI"
doc_id: "QsoF34ben2"
updated_at: "2026-08-12 09:20:46"
---

> Source: https://open.dingtalk.com/document/development/define-extension-jsapi
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 开发自定义JSAPI
> Updated: 2026-08-12 09:20:46

# 开发自定义JSAPI

当你开发的插件是期望给 H5 微应用/小程序扩展能力时，可参考本文定义扩展 JSAPI 。

## **基本原理**

基于钉钉开放框架，插件 SDK 内部可自定义扩展 JSAPI ， H5 微应用/小程序可通过开放框架的扩展 JsBridge 调用专属插件 SDK 的类。如下图所示：

![流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9890753661/p490334.jpg)

## **接口说明**

| **接口类** | **描述** |
| --- | --- |
| JsModule | 定义JSMethod的具体实现类。 |
| JsSubject | 定义具有观察者模式的对象类。 |
| JsRequest | JSAPI请求的入参封装类，可从中获取前端请求的参数详情。 |
| JsResponse | 插件SDK返回结果给前端应用使用。 |

> **[!NOTE]**
>
> JsModule和JsSubject的区别：
>
> - JsModule主要定义常规的下行调用，前端应用主动发起调用插件SDK代码并返回结果的场景。
> - JsSubject主要定义上行调用，前端应用可发起建立通道并持续监听插件SDK内部数据变更的场景，插件SDK可以持续不断地将新数据主动通知到前端应用（比如文件下载进度等）。

### **JsModule**

| **接口函数** | **说明** |
| --- | --- |
| startActivityForResult() | 用于期望在JSAPI中启动Activity并获取返回结果的场景。  **[!NOTE]**  启动Activity时，请勿使用FLAG\_ACTIVITY\_NEW\_TASK的方式。 |
| onActivityResult() | 配合startActivityForResult使用，对应结果回调 |

### **JsSubject**

| **接口函数** | **说明** |
| --- | --- |
| onSubscribe() | 前端应用发起订阅事件（subscribe）时调用 |
| onRelease() | 前端应用发起退订（unsubscribe）时调用 |
| notifyEvent() | 主动通知前端应用数据（JSON格式） |
| notifyFailed() | 主动通知前端应用异常（JSON格式） |

## **前提条件**

请先扫码加入“钉钉native定制扩展开放”组织，申请通过后点击[下载最新的调试环境](https://alidocs.dingtalk.com/i/nodes/AY39rGpMPmeVNOPZZKloJOZkXKnaoNQ7)。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632059.png)

> **[!NOTE]**
>
> 申请时请务必明确说明：开发者所在公司 + 开发的项目。未说明的将不予通过。

## **开发步骤**

### **步骤一：定义文档打开JSAPI**

**使用JsModule定义文档打开JSAPI，**我们定义JSAPI：“file.open”，并使用内部的自研 Activity 打开文档。

```
@JSModule
  public class JsModuleFile extends JsModule {
		
    @JSMethod("file.open")
    public void fileOpen(final JsRequest jsRequest, final JsResponse jsResponse) {
      Intent intent = new Intent(jsRequest.context, ExampleEditDocActivity.class);
      if (jsRequest.params != null) {
        intent.putExtra("filePath", jsRequest.params.optString("filePath"));
        intent.putExtra("token", jsRequest.params.optString("token"));
      }
      // 使用自研Activity打开文档
      startActivityForResult(jsRequest, jsResponse, intent, REQUEST_CODE);
      // 通知H5打开结果
      jsResponse.notifySuccess(null);
    }
    
  }
```

关键步骤：

- 使用Dingtalk DevKit工具新建一个JsModule类（同样可以直接手动创建，注意使用注解@JSModule）
- 使用@JSMethod("jsapi name")定义扩展JSAPI，被标记的函数形态固定如下：

`public void fun(final JsRequest jsRequest, final JsResponse jsResponse) ;`

- 使用JsRequest取出前端应用传递过来的入参并校验合法性
- 使用JsResponse返回结果（可同步或异步返回）
- 假如需要接受Activity的返回值，可重载onActivityResult()函数

> **[!IMPORTANT]**
>
> 如果使用startActivity的方式，可能会出现返回后小程序页面被系统回收清理，因此建议优先使用startActivityForResult()方式打开Activity。

### **步骤二：建立文档编辑状态监听隧道**

我们定义JSSubject：“file.editstate”，H5微应用/小程序应用可订阅主题监听文档状态。

```
@JSSubject("file.editstate")
  public class JsSubjectEditState extends JsSubject {
    
    @Override
    public void onSubscribe(final JsRequest jsRequest, final JsResponse jsResponse) {
      // 假设我们有一个文档管理类用于管理文档状态
      FileManager.getInstance().registerStateListener(new FileStateListener() {
        @Override
        public void onStateChange(String state) {
          // 状态变更时主动通知小程序
          jsResponse.notifyEvent(json);
        }
      })
        }

    @Override
    public void onRelease(JsRequest jsRequest) {
      // 释放相关资源
      ... ...
    }
  }
```

关键步骤：

- 使用Dingtalk DevKit工具新建JsSubject子类（同样使用注解@JSSubject可以手动创建）
- 实现接口onSubject，处理来自前端应用的状态监听任务
- 持续使用jsResponse将状态值通知给H5/小程序应用
- 实现接口onRelease释放资源

### **步骤三：调试 JSAPI 代码**

在你的前端应用还没准备好时，可以先使用钉钉官方提供的小程序调用你的SDK。

1. 工作台请切换到“钉钉Native定制扩展开放”组织。
2. 点击工作台应用“专属插件JSAPI调试”。

如下图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632060.png) ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632061.png)

假如你的账号无法加入该组织，也可以通过扫码唤起小程序：

![deployCode_1687682700230.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1904867861/p685922.png)

- BundleID：可不填，请参考本文**更多信息**中的描述。
- API：插件 SDK 中 JsMethod 定义的 JSAPI 值。
- 参数：输入参数名和参数值，然后点击“添加参数”将 kv 值添加的请求中，可添加多个。
- 执行：根据上面的输入发起 JSAPI 调用。

> **[!NOTE]**
>
> 扩展 JSAPI 默认不支持钉钉账号**登录前**调用，如果有需求，请联系钉钉侧项目经理申请开通。

### **步骤四：前端调用JSAPI**

#### **调用 JSAPI 打开文档**

```
JSAPI:  exclusive.sdk.invoke
入参：
  - bundle_id: sdk对应的 bundle_id
  - api：sdk定义的jsapi，比如 "demo.file.delete"
  - request_params：请求的参数
  - 其他：业务参数

import * as dd from 'dingtalk-jsapi';
dd._invoke(
  "exclusive.sdk.invoke",
  {
    bundle_id:'此处填写正确的ID', -- 可选
api: 'file.open' ,	-- 必需
request_params: {
  ... ...
}
  
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

#### **监听文档编辑状态**

监听和取消监听请务必成对使用。

```
JSAPI:  exclusive.sdk.subscribe, exclusive.sdk.unsubscribe
入参：
  - bundle_id: sdk对应的 bundle_id
  - subject_id: JsSubject的id，比如示例中的"file.editstate"
  - request_params: 请求附带的参数
  - 其他：业务参数可自行约定

import * as dd from 'dingtalk-jsapi';
dd._invoke(
  "exclusive.sdk.subscribe",
  {
    bundle_id:'填写正确的ID',	--  可选
subject_id: 'file.editstate' ,	-- 必需
request_params: {
  ... ...
}
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

## **更多信息**

- 定义的 JSAPI 请避免使用同钉钉关键词相同的参数名，比如“bundle\_id”、“api”、“subject\_id”，即 request\_params 对象中的key不能包含以上关键词。
- 前端调用指定了 bundle\_id 参数时，代表将会从指定的插件中查询注册的 JSAPI 并调用，请确认专属插件中的 bundle\_id 和前端调用传入的值是否相同。
- 前端调用时 bundle\_id 可忽略，忽略后将会调用第一个 JSAPI 的专属插件。假如你的应用中存在多个专属插件注册了相同的 JSAPI 时，调用时可能会不符合你的预期。
