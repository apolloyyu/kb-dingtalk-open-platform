---
title: "Web容器生命周期扩展"
source_url: "https://open.dingtalk.com/document/development/web-extensions-harmonyos"
namespace: "development"
slug: "web-extensions-harmonyos"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "使用扩展点 > Web容器生命周期扩展"
doc_id: "ofh2aRydMo"
updated_at: "2026-08-18 09:08:01"
---

> Source: https://open.dingtalk.com/document/development/web-extensions-harmonyos
> Path: 专属版客户端插件 / HarmonyOS 插件 / 使用扩展点 > Web容器生命周期扩展
> Updated: 2026-08-18 09:08:01

# Web容器生命周期扩展

## **基础信息**

| **扩展点编码** | **接口类** | **支持的版本** |
| --- | --- | --- |
| dingtalk\_webapp$lifecycles | DTExtension | >= 7.6.40 |

## **功能说明**

当你的插件期望监听 Web 容器（H5 应用/小程序）的打开和关闭事件时，可使用该扩展点。

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| invokeSync()  （请注意使用同步接口） | 入参：   - API = 'onPageShow' - API = 'onPageHide' - ApiParams ：    - 参数【appId】：Web 应用 agentID 或 AppID   - 参数【type】：Web 应用类型，"h5" ，"mini"。   返回值：无 |

## **代码示例**

```
export class TCWebAppLifecycle extends DTExtension {

  invokeSync(params: ApiParams): ApiData | undefined {
    const appId = params.data?.getString('appId')
    const pageType = params.data?.getString('type')

    switch (params.api) {
      case "onPageShow":
        break

      case "onPageHide":
        break
    }
    return undefined
  }
}
```

请在模块的 Index.ets 文件中导出类，并关联 dingtalk-bundle.json5 配置：

> **[!IMPORTANT]**
>
> - 应用必须是企业内部应用，非企业内部应用无法监听。
> - 在 Pad 和折叠屏场景中，由于鸿蒙系统机制问题，假如 Web 应用在不同的页面栈中时，生命周期可能存在不准确问题，请关注。依赖鸿蒙新 ROM 接口支持，请关注。

```
"extensions": [
  {
    "class": "TCWebAppLifecycle",
    "bind": "dingtalk_webapp$lifecycles"
  }
]
```
