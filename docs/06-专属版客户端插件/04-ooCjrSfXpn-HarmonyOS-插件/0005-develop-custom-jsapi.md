---
title: "开发自定义JSAPI"
source_url: "https://open.dingtalk.com/document/development/develop-custom-jsapi"
namespace: "development"
slug: "develop-custom-jsapi"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "HarmonyOS 插件 > 开发自定义JSAPI"
doc_id: "PIWuZUXndm"
updated_at: "2025-10-15 17:02:14"
---

> Source: https://open.dingtalk.com/document/development/develop-custom-jsapi
> Path: 专属版客户端插件 / HarmonyOS 插件 / HarmonyOS 插件 > 开发自定义JSAPI
> Updated: 2025-10-15 17:02:14

# 开发自定义JSAPI

当你开发的插件是期望给 H5 微应用/小程序扩展能力时，可参考本文定义扩展 JSAPI 。

## **基本原理**

基于钉钉开放框架，插件 SDK 内部可自定义扩展 JSAPI ， H5 微应用/小程序可通过开放框架的扩展 JsBridge 调用专属插件 SDK 的类。如下图所示：

![流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9890753661/p490334.jpg)

## **扩展点信息**

框架提供了两种能力：

- JSApiExtension：定义下行调用，即前端应用主动发起调用插件SDK代码并返回结果的场景。
- JSSubjectExtension：定义上行调用，即前端应用可发起建立通道并持续监听插件SDK内部数据变更的场景，插件SDK可以持续不断地将新数据主动通知到前端应用（比如文件下载进度等）

| **扩展点编码** | **接口类** | **支持的版本** |
| --- | --- | --- |
| dingtalk\_bundles$jsapi | JSApiExtension | v7.6.40 |
| dingtalk\_bundles$jssubject | JSSubjectExtension | v7.6.40 |

## **扩展JSAPI（JSApiExtension）**

该扩展点用于定义扩展 JSAPI。主要定义常规的下行调用，即前端应用主动发起调用插件SDK代码并返回结果的场景。

> **[!NOTE]**
>
> 专属插件中可以定义多个 JSApiExtension，一个 JSApiExtension 类中可以处理多个 JSAPI，请根据自身业务划分。

**接口说明：**

| **名称** | **说明** |
| --- | --- |
| getSupportApis(): string[] | 必须实现。  入参：无  返回值：返回可支持的 JSAPI 数组。 |
| invoke(req: JSApiRequest) | 必须实现。  入参：JSApiRequest   - component: CustomComponent，页面上下文 - api: string，调用的 jsapi 名称 - bundleId?: string 专属插件 ID - params?: Object，前端调用时传入的参数   返回值：JSApiResponse   - data：Object，期望返回给前端的数据 |

**示例代码：**

- 示例API：tc.infomation：可给前端页面返回插件基础信息；
- 示例API：tc.openSetting：前端打开插件自定义的设置页面；

```
export class ExampleJSApiExtension extends JSApiExtension {

  getSupportApis(): string[] {
    return[ "tc.infomation", "tc.openSetting" ]
  }

  invoke(request: JSApiRequest): Promise<JSApiResponse> {
    switch(request.api) {
      case 'tc.infomation':
        return this._information(request)

      case 'tc.openSetting':
        myBundle.routePage({
          component: request.component,
          path: "settings"
        })
        return this.success()

      default:
        return this.failed("API还未实现，敬请期待")
    }
  }

  private async _information(request: JSApiRequest): Promise<JSApiResponse> {
    interface Result {
      url: string,
      list: string[]
    }
    return this.success({
      url: "https://testcase.com",
      list: [
        "dingtalk",
        "alibaba"
      ]
    } as Result)
  }
}
```

同样，仍需要在Index.ets中导出 ExampleJSApiExtension 以及 在dingtalk-bundle.json5 添加扩展配置信息。

```
  "extensions": [
    {
      "class": "ExampleJSApiExtension",
      "bind": "dingtalk_bundles$jsapi"
    }
  ],
```

## **扩展Subject（JSSubjectExtension）**

定义上行调用，即前端应用可发起建立通道并持续监听插件SDK内部数据变更的场景，插件SDK可以持续不断地将新数据主动通知到前端应用（比如文件下载进度等）。

**接口说明：**

| **名称** | **说明** |
| --- | --- |
| subjectId(): string | 必须实现。  入参：无  返回值：返回可订阅的主题 ID。 |
| subscribe(req: JSSubjectRequest) | 必须实现。  入参：JSApiRequest   - component: CustomComponent，页面上下文 - subjectId: string，调用方期望订阅的主题 ID - bundleId?: string 专属插件 ID - callback?: Function，用于持续给前端返回数据的回调函数 |
| release() | 建议实现，当调用方主动取消订阅或者页面销毁时会回调，用于释放资源 |

**示例代码：**

示例中演示了通过定时器持续跟前端页面返回数据。

```
export class ExampleJSSubjectExtension extends JSSubjectExtension {

  private _request?: JSSubjectRequest
  private timerId: number | undefined

  subjectId(): string {
    return 'testcase'
  }

  async subscribe(request: JSSubjectRequest): Promise<JSApiResponse> {
    interface PostResp {
      count: number
    }
    
    // 去重处理，避免资源泄露
    if (this._request) {
      return this.failed('重复订阅')
    }
    this._request = request
    const data: PostResp = { count: 0 }
    this.timerId = setInterval(() => {
      data.count ++
      this._request?.postData(data)
    }, 1000);
    return new JSApiResponse()
  }

  async release(request: JSSubjectRequest): Promise<JSApiResponse> {
    // 清理现场，避免造成内存泄露
    this._request = undefined
    if (this.timerId) {
      clearInterval(this.timerId)
      this.timerId = undefined
    }
    return new JSApiResponse()
  }
}
```

同样，仍需要在Index.ets中导出 ExampleJSApiExtension 以及 在dingtalk-bundle.json5 添加扩展配置信息。

```
  "extensions": [
    {
      "class": "ExampleJSSubjectExtension",
      "bind": "dingtalk_bundles$jssubject"
    }
  ],
```

## **执行测试**

可以通过扫码唤起小程序：

![deployCode_1687682700230.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1904867861/p685922.png)

- **BundleID**：可不填，请参考本文**更多信息**中的描述。
- **API**：插件 SDK 中 JsMethod 定义的 JSAPI 值。
- **参数**：输入参数名和参数值，然后点击“添加参数”将 kv 值添加的请求中，可添加多个。
- **执行**：根据上面的输入发起 JSAPI 调用。

> **[!NOTE]**
>
> 扩展 JSAPI 默认不支持钉钉账号**登录前**调用，如果有需求，请联系钉钉侧项目经理申请开通。
