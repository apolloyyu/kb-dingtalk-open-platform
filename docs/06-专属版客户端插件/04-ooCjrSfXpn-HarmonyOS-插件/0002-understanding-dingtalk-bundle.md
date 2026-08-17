---
title: "了解dingtalk-bundle.json5"
source_url: "https://open.dingtalk.com/document/development/understanding-dingtalk-bundle"
namespace: "development"
slug: "understanding-dingtalk-bundle"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "HarmonyOS 插件 > 了解dingtalk-bundle.json5"
doc_id: "pB2A3IKo28"
updated_at: "2026-08-12 09:20:49"
---

> Source: https://open.dingtalk.com/document/development/understanding-dingtalk-bundle
> Path: 专属版客户端插件 / HarmonyOS 插件 / HarmonyOS 插件 > 了解dingtalk-bundle.json5
> Updated: 2026-08-12 09:20:49

# 了解dingtalk-bundle.json5

## **概要说明**

插件开发中的扩展点实现类、额外新增依赖项、新增的页面等，为了能够成功被钉钉框架识别，需要提前在dingtalk-bundle.json5文件中声明。每个专属插件工程需要定义一个 dingtalk-bundle.json5 文件（路径在./src/main/ets 根目录中）

> **[!IMPORTANT]**
>
> dingtalk-bundle.json5 文件的默认生成路径是`./src/main/ets/` ，请不要挪动或者重命名该文件。

## **详细说明**

dingtalk-bundle.json5 文件支持的各个字段说明如下表格：

| 字段 | 说明 |
| --- | --- |
| bundleId | String 类型，专属插件的 BundleID，必须同“Bundle.ets”文件中保持一致。 |
| extensions | Array 类型，声明扩展点的实现类使用。   - class：关联的扩展点实现类名，类必须在Index.ets中声明导出。 - bind：绑定的扩展点 ID。   示例：   ``` "extensions": [   {     "class": "VpnSettingMenu",     "bind": "settings$setting_items"   } ], ``` |
| pages | Array 类型，声明插件自建的页面使用。   - class：关联的 DTOpenPage 页面配置类名 - routePath：页面路由 path   示例：   ``` "pages": [   {     "class": "VpnSettingPage",     "routePath": "vpn_settings"   } ], ``` |
| features | Array 类型，声明需要开启的特性使用。   - id：特性 ID。  **[!NOTE]**  支持的特性清单：    - 'vpn'：配合VPN扩展点使用。   示例：   ``` "features": [   {     "id": "vpn"   } ], ``` |
| dependencies | Map 类型，插件额外依赖清单。在 oh-package.json5 声明的额外依赖，只是用于编译插件，为了能让钉钉编译框架识别到需要的额外依赖，仍需要在 dingtalk-bundle.json5 中声明。  示例：   ``` "dependencies": {   "@alibaba/fastjson": "1.0.0",   "@demo/localfile": "file:../libs/localfile.har", }, ``` |
