---
title: "开发 HarmonyOS 插件"
source_url: "https://open.dingtalk.com/document/development/create-plug-in-project"
namespace: "development"
slug: "create-plug-in-project"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "开发 HarmonyOS 插件"
doc_id: "blFrFnwVwg"
updated_at: "2026-08-12 09:20:42"
---

> Source: https://open.dingtalk.com/document/development/create-plug-in-project
> Path: 专属版客户端插件 / HarmonyOS 插件 / 开发 HarmonyOS 插件
> Updated: 2026-08-12 09:20:42

# 开发 HarmonyOS 插件

## **前提条件**

- 本地环境已经安装DevEco Studio。
- 下载壳工程：[DingTalk-DevEnv-2025-04-27.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250922/rwifce/DingTalk-DevEnv-2025-04-27.zip)
- 参考示例工程：[DingTalk-DevEnv-Example.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250923/uqgtty/DingTalk-DevEnv-Example.zip)

## **创建插件工程**

1. 下载壳工程，并解压到本地。
2. 使用DevEco Studio打开壳工程。

   > **[!NOTE]**
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9616230671/p1009384.png)
   >
   > 壳工程是一个标准的鸿蒙项目，其中
   >
   > - dingtalk：用于编译出HSP格式的调试模块，开发插件时可忽略。
   > - repository：开放API和编译插件存放目录。假如需要升级最新openapi版本时，可下载最新的壳工程zip包，解压后替换目录中的文件即可（替换后务必同步修改工程中的oh-package.json5 文件）。
3. 使用命令行创建第一个插件工程，确定插件的BundleID。

   > **[!IMPORTANT]**
   >
   > - 为了避免重复，我们建议采用类似“公司\_产品”的格式填写。支持字母、数字、下划线，请勿使用其他特殊字符，示例： demo\_vpn。
   > - 禁止包含“DingTalk”、“Alibaba”等钉钉相关特殊字符串。
4. 在根目录中，使用命令行`hvigorw createDingtalkBundle -p bundleId=XXXX`，创建插件模块。如下图示例。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9616230671/p1009428.png)

   执行完成后，可以看到项目中多了一个子模块“bundle\_demo\_vpn”。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9616230671/p1009432.png)

   > **[!NOTE]**
   >
   > - 假如需要修改BundleID，请同时修改工程中“dingtalk-bundle.json5”和“Bundle.ets”两个文件中的值。
   > - 命令创建的子工程名称默认格式：bundle\_{BundleID}。
   > - **请不要开启字节码方式编译，字节码方式编译存在较多问题，不建议使用。**

## **编写插件功能**

1. 了解插件工程相关文件

   插件工程中自动生成的钉钉相关的文件主要有两个：Bundle.ets和dingtalk-bundle.json5。其中

   （1）Bundle.ets

   核心定义了钉钉平台相关的全局对象：`myBundle: DTOpenBundle`。该对象提供了平台能力接口，比如调用平台开放api、路由打开页面等。

   （2）dingtalk-bundle.json5

   该文件是插件工程的描述文件，所有新增的扩展点实现类、页面、依赖项均需要在此文件中描述声明。
2. 参照文档[新建页面和路由](0004-new-page-and-route.md)编写设置页面。示例如下：

   ```
   import { DTOpenPage, DTOpenPageConfig, DTOpenPageParam } from "@dingtalk/bundle_openapi"

   export class VpnSettingPage extends DTOpenPage {
     getPageBuilder(): WrappedBuilder<[DTOpenPageParam]> { 
       return wrapBuilder(settingBuilder) 
     }
     getPageConfig(): DTOpenPageConfig {
       return { title: 'VPN设置' }
     }
   }

   @Builder
   function settingBuilder(params: DTOpenPageParam) {
     SettingPageContent({ params: params })
   }

   @ComponentV2
   struct SettingPageContent {
     @Require
     @Param
     params: DTOpenPageParam

     build() {
       Column() {
         Text("Hello, Dingtalk")
       }
     }
   }
   ```

   在Index.ets中导出VpnSettingPage类，以及在dingtalk-bundle.json5中添加插件配置：

   ```
     "pages": [
       {
         "class": "VpnSettingPage",
         "routePath": "vpn_settings"
       }
     ],
   ```
3. 使用设置项扩展点[设置项扩展点（HarmonyOS）](0008-set-item-extension-point-harmonyos.md),参照指导文档添加代码。示例如下：

   ```
   export class VpnSettingMenu extends DTExtension {
     private data = new ApiData()

     constructor() {
       super()
       this.data = new ApiData()
         .put('title', 'VPN设置项')
         .put('subtitle', '未开启')
         .put('group', 'safe')
     }

     getData(): ApiData {
       return this.data
     }

     async invoke(params: ApiParams): Promise<ApiData> {
       if (params.api === 'click' && params.context) {
         myBundle.routePage({
           component: params.context as CustomComponent,
           path: 'vpn_settings'
         })
       }
       return new ApiData()
     }
   }
   ```

   同样，请务必在Index.ets文件中导出类VpnSettingMenu，以及在dingtalk-bundle.json5中添加配置:

   ```
   "extensions": [
     {
       "class": "VpnSettingMenu",
       "bind": "settings$setting_items"
     }
   ],
   ```

## **编译生成产物**

1. 了解编译插件

   壳工程项目中在hvigor-config.json5中已经添加好了编译插件依赖，如果更新编译插件版本时，请务必修改此处引用路径。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1716230671/p1009534.png)
2. 使用DevEco Studio的Build工具，编译子模块。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1716230671/p1009540.png)

   编译完成后，可以在插件的“build/default/outputs/default/”目录中看到编译产物hdeb文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1716230671/p1009542.png)

   拷贝\*.hdeb文件后，可用于上传发布到钉钉打包平台。
