---
title: "VPN服务扩展"
source_url: "https://open.dingtalk.com/document/development/vpn-service-extensions-harmonyos"
namespace: "development"
slug: "vpn-service-extensions-harmonyos"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "使用扩展点 > VPN服务扩展 > VPN服务扩展"
doc_id: "diiwuBJ3ke"
updated_at: "2026-08-18 09:08:01"
---

> Source: https://open.dingtalk.com/document/development/vpn-service-extensions-harmonyos
> Path: 专属版客户端插件 / HarmonyOS 插件 / 使用扩展点 > VPN服务扩展 > VPN服务扩展
> Updated: 2026-08-18 09:08:01

# VPN服务扩展

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| dingtalk\_bundles$vpn\_extension | DTExtension | HarmonyOS |

## **功能说明**

当你的插件用于开发一个安全网络 VPN 时，将会期望使用VpnExtensionAbility，该扩展点将用于该项功能。

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| invoke() | 入参：   - API = 'onCreate'：ApiParams.context 为VpnExtensionAbility。 - API = 'onDestroy'：ApiParams.context 为VpnExtensionAbility。   返回值：无 |

## **代码示例**

```
export class TCVpnExtension extends DTExtension {

  async invoke(params: ApiParams): Promise<ApiData> {
    switch (params.api) {
      case 'onCreate':
        if (params.context instanceof VpnExtensionAbility) {
          setupVpn(params.context)
        }
        break
        
      case 'onDestroy':
        if (params.context instanceof VpnExtensionAbility) {
          destroyVpn(params.context)
        }
        break
    }
    return new ApiData()
  }
}
```

请在模块的 Index.ets 文件中导出类，并关联 dingtalk-bundle.json5 配置：

```
  "extensions": [
    {
      "class": "TCVpnExtension",
      "bind": "dingtalk_bundles$vpn_extension"
    }
  ]
```

同时，在 dingtalk-bundle.json5 配置开启 VPN 特性：

```
"features": [
    { 
      "id": "vpn" 
    }
],
```
