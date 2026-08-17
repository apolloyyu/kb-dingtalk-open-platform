---
title: "首页生命周期扩展（HarmonyOS）"
source_url: "https://open.dingtalk.com/document/development/home-lifecycle-extensions-harmonyos"
namespace: "development"
slug: "home-lifecycle-extensions-harmonyos"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "使用扩展点 > 首页生命周期扩展"
doc_id: "dwnDZfFRDG"
updated_at: "2026-08-12 09:20:55"
---

> Source: https://open.dingtalk.com/document/development/home-lifecycle-extensions-harmonyos
> Path: 专属版客户端插件 / HarmonyOS 插件 / 使用扩展点 > 首页生命周期扩展
> Updated: 2026-08-12 09:20:55

# 首页生命周期扩展（HarmonyOS）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| home\_extensions$lifecycles | DTExtension | HarmonyOS |

## **功能说明**

当专属 App 唤起进入前台时，该插件可监听钉钉首页的生命周期（onAboutToAppear、onAboutToDisAppear）事件。该插件常用于在首页创建时执行操作，比如期望在钉钉进程重启后建立VPN通道的场景。

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| invoke() | 入参：   - API = 'onAboutToAppear'：ApiParams.context 为首页关联的页面 Component。 - API = 'onAboutToDisAppear'：ApiParams.context 为首页关联的页面 Component。   返回值：无 |

## **代码示例**

```
export class TCHomeLifecycle extends DTExtension {

  async invoke(params: ApiParams): Promise<ApiData> {
    switch (params.api) {
      case 'onAboutToAppear':
        myBundle.toast('用例：HomeLifecycle 验证成功。')
        break
    }
    return new ApiData()
  }
}
```

请在模块的 Index.ets 文件中导出类，并关联 `dingtalk-bundle.json5` 配置：

```
"extensions": [
  {
    "class": "TCHomeLifecycle",
    "bind": "home_extensions$lifecycles"
  }
]
```
