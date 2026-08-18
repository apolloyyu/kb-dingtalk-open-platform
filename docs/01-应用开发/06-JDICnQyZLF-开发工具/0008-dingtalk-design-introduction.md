---
title: "简介"
source_url: "https://open.dingtalk.com/document/download/dingtalk-design-introduction"
namespace: "download"
slug: "dingtalk-design-introduction"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > DingTalk Design CLI > 简介"
doc_id: "9iWoMDbhRT"
updated_at: "2026-08-18 09:13:14"
---

> Source: https://open.dingtalk.com/document/download/dingtalk-design-introduction
> Path: 应用开发 / 开发工具 / 开发者工具 > DingTalk Design CLI > 简介
> Updated: 2026-08-18 09:13:14

# 简介

本文介绍DingTalk Design CLI工具的基本概念和常见命令。

## 基本概念

DingTalk Design CLI是钉钉前端应用研发命令行工具，提供以下能力：

- 提供小程序、H5微应用、工作台组件的初始化能力。
- 提供小程序和工作台组件的本地构建、开发调试、预览、校验和上传等能力。
- 提供H5微应用本地模拟器开发的能力

## 能力介绍

使用DingTalk Design CLI的能力，可以开发不同的应用类型，开发者可进行自主选择：

- **小程序**：如需使用DingTalk Design CLI工具开发小程序，请参考[开发小程序](0010-develop-mini-program-applications.md)。
- **H5微应用**：如需使用DingTalk Design CLI工具开发H5微应用，请参考[开发H5微应用](0011-develop-h5-micro-applications.md)。
- **工作台组件**：如需使用DingTalk Design CLI工具开发工作台组件，请参考[开发工作台组件](0012-console-components.md)。

## 常规用法

你可以通过以下命令使用DingTalk Design CLI工具。

```
$ ding <command> [options]
# 例如：
# ding init
```

目前支持的常见命令有：

| 命令 | 说明 |
| --- | --- |
| init | 初始化一个小程序、H5微应用、工作台组件，项目目录下会包含一个`ding.config.json`配置文件。 |
| dev | 开发调试小程序、H5微应用、工作台组件。 |
| preview | 生成小程序、工作台组件的调试二维码。 |
| upload | 上传小程序、工作台组件项目到开发者后台。 |
| lint | 校验小程序、h5微应用、工作台组件。  **[!NOTE]**  本地校验时，小程序、H5微应用的校验规则是项目目录中的eslint配置文件。工作台组件的校验规则等同于提交上架会进行的校验规则。 |

### ding init

创建一个钉钉应用，可以是小程序、h5、工作台组件。

#### **命令参数**

- `-a, --appType <appType>`：（可选）指定应用类型，值可以为**mp** | **h5** | **plugin**。
- `-t, --template <template>`：（可选）指定模板，模板的key可以从[Git](https://github.com/open-dingtalk/dd-application-template)上查阅，例如：**plugin\_default**，则模板**key**为**default**。
- `-l, --language <language>`：（可选）指定模板语言，值可以为**javascript** | **typescript**（有些模板可能没有**typescript**语言版本）。
- `--skip-install <skip-install>`：（可选）若指定则不自动安装依赖。
- `-o, --outDir <outDir>`：（可选）输出目录，若不指定时，将默认在当前目录新建。
- `--cwd [cwd]`：（可选）当前的工作目录, 默认值是`process.cwd()`。

### ding preview

生成二维码，扫码预览本地构建出来的小程序或工作台组件。

#### 命令参数

`--miniAppId <miniAppId>`：（可选）钉钉小程序或工作台组件的**miniAppId**。默认从当前工作目录下的 ding.config.json 中读取

`--token <token>`：（可选）API访问凭证，默认从当前工作目录下的`ding.config.json`中读取，生成方式参考[获取工作台API访问凭证](https://open.dingtalk.com/document/app/used-to-obtain-the-application-authorization-without-api-token)。

`-d, --debug`：（可选）生成真机调试二维码，可配合**ChromeDevtools**进行真机调试

`--cwd [cwd]`：（可选）当前的工作目录, 默认值是`process.cwd()`。

### ding lint

校验钉钉小程序、h5、工作台组件的代码规范和平台要求规范。

钉钉小程序、h5默认是调用`package.json`中**scripts**的`lint`命令。

工作台组件会校验组件内使用的JSAPI、使用的样式、变量等是否符合平台要求规范。

### ding upload

上传小程序、工作台组件项目到开发者后台。

#### 命令参数

`--miniAppId <miniAppId>`：（可选）钉钉小程序或工作台组件的**miniAppId**。默认从当前工作目录下的 ding.config.json 中读取

`--token <token>`：（可选）API访问凭证，默认从当前工作目录下的`ding.config.json`中读取，生成方式参考[调用工作台 API](../../08-工作台/02-Qzb8Lpee2t-使用教程/0013-call-the-workbench-api.md)。

`--cwd [cwd]`：（可选）当前的工作目录, 默认值是`process.cwd()`。

### ding dev

开发调试小程序、H5微应用、工作台组件。

不同的应用类型，具备的默认subCommand命令不同，如下表所示：

| 应用类型 | subCommand 子命令 |
| --- | --- |
| H5微应用 | `- updateConfig`：更新`ding.config.json`。  例如：   ``` ding dev updateConfig miniAppId 500000xxxxxx ```   `- lint`：校验当前代码是否符合eslint规范（工作台组件除eslint规范外，会有额外的校验规则）。  `- web`：可以在Web浏览器调试H5微应用 |
| 小程序 | `- updateConfig`：更新`ding.config.json。`  例如：   ``` ding dev updateConfig miniAppId 500000xxxxxx ```   `- lint`：校验当前代码是否符合eslint规范（工作台组件除**eslint**规范外，会有额外的校验规则）。  `- ide`：本地打开IDE lite版。  `- qrcode`：生成预览二维码。  `- qrcode:debug`：生成真机调试二维码。  `- upload`：上传小程序或工作台组件到开发者后台。 |
| 工作台组件 | `- updateConfig` : 更新`ding.config.json`。  例如：   ``` ding dev updateConfig miniAppId 500000xxxxxx ```   `- lint`：校验当前代码是否符合eslint规范（工作台组件除**eslint**规范外，会有额外的校验规则）  `- ide`：本地打开**IDE lite**版。  `- qrcode`：生成预览二维码。  - qrcode:debug：生成真机调试二维码。  `- upload`：上传小程序或工作台组件到开发者后台。  `- createPluginComponent`：在本地快速创建一个组件。  `- pluginH5Bundle`：本地访问通过H5Pro打包后的组件**bundle**。 |

## H5微应用特有subCommand

### Web beta功能

在Web浏览器调试H5微应用，支持在Web浏览器调试常用JSAPI、样式、网络请求、日志输出等。目前仅支持调试单页应用。

> **[!NOTE]**
>
> 此功能需要安装特定版本DingTalk Design CLI。

例如：

```
ding dev web
```

执行该命令后，会默认在本地10003端口打开H5微应用本地模拟器，H5微应用本地模拟器支持常用的JSAPI。

H5微应用本地模拟器支持常用的JSAPI，并且不需要JSAPI鉴权也可以调通需要鉴权的JSAPI，开发者可以在Web浏览器中像开发调试普通H5应用一样便捷地调试钉钉H5微应用。

![web截图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0955042461/p385357.png)

### 内测功能

如果开发者不想使用DingTalk-Design-CLI提供的模板进行开发，但又希望可以使用上H5微应用本地模拟器功能，该subCommoand也提供了一个额外的配置参数来解决，如下：

```
ding dev web --targetH5Url {你本地调试的页面链接}
```

你本地调试的页面链接需要在**Response Headers**中配置`Access-Control-Allow-Origin: *`。

- 如果你使用的是**Webpack-dev-server**来挂载你本地调试的页面链接，那么可以参考[webpack](https://webpack.docschina.org/configuration/dev-server/#devserverheaders)进行配置自定义的**Response Header**。
- 如果使用的是**vue-cli**初始化的项目，需要在项目目录下添加**vue.config.js**，并补充如下配置：

  ```
  module.exports = {
      configureWebpack: {        
          devServer: {
            headers: {
              'Access-Control-Allow-Origin': '*'            
            }
          }
      },
  }
  ```

> **[!NOTE]**
>
> --targetH5Url参数是一个内测功能，在使用过程中遇到问题请联系我们。

## 小程序特有subCommand

### ide

本地打开**IDE lite**版。

```
ding dev ide
```

![ide lite版](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0281894461/p385374.png)

### qrcode

生成预览二维码。

```
ding dev qrcode
```

![预览二维码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385384.png)

### qrcode:debug

生成真机调试二维码，手机扫描生成的**真机调试二维码**后，可以在**调试工具页面**调试小程序。

```
ding dev qrcode:debug
```

生成的真机调试二维码如下图所示：

![真机调试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385398.png)

调试工具页面如下：

![调试工具页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1955042461/p385418.png)

### upload

上传小程序或工作台组件到开发者后台。

```
ding dev upload
```

![上传小程序](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385425.png)

## 工作台组件特有subCommand

### ide

本地打开IDE lite版。

```
本地打开IDE lite版
```

![idelite界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385461.png)

### qrcode

生成预览二维码。

```
ding dev qrcode
```

![预览二维码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385462.png)

### qrcode:debug

生成真机调试二维码，手机扫描生成的**真机调试二维码**后，可以在**调试工具页面**调试小程序。

```
ding dev qrcode:debug
```

生成的真机调试二维码如下图所示：

![真机调试二维码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385464.png)

真机调试工具页面如下：

![真机调试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1955042461/p385644.png)

### upload

上传小程序或工作台组件到开发者后台。

```
ding dev upload
```

![上传工作台组件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1281894461/p385735.png)

### createPluginComponent

在本地快速创建一个组件。

```
ding dev createPluginComponent
```

使用该命令，增加一个组件会自动完成以下的步骤，便于开发者快速创建一个组件：

1. 在**${pluginRoot}/components**目录下新增组件模板。
2. 在**${miniprogramRoot}/pages/index/index.json**中插入组件引用。
3. 在**${pluginRoot}/plugin.json**中插入组件引用。
4. 在**miniprogram/pages/index/index.axml**中插入组件**axml**。
5. 在**ding.config.json**中增加**mock**配置。

![快速创建组件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2281894461/p385752.png)

### pluginH5Bundle

执行该命令后，会将小程序插件dsl转换为React并最终产出一个bundle文件。

```
ding dev pluginH5Bundle
```

![转化工作台组件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2281894461/p385753.png)

## 通用subCommand

### updateConfig

更新`ding.config.json`，

例如：

```
ding dev updateConfig miniappId 500000xxxxx
```

![更新ding.config.json](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2281894461/p385756.png)

### lint

校验当前代码是否符合**eslint**规范。

> **[!NOTE]**
>
> 工作台组件除eslint规范外，会有额外的校验规则。

例如：

```
ding dev lint
```

![检验规范](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2281894461/p385758.png)

## **常见问题**

- **存量项目如何使用DingTalk Design CLI？**

  建议使用DingTalk Design CLI来初始化一个新的项目，获得更完善的开发体验。如果暂时无法迁移，则需要在存量项目中新建`ding.config.json`配置文件，配置文件中需要填入相关的参数。

## 联系我们

如果你在使用DingTalk Design CLI过程中遇到问题或者有其他建议，你可以通过以下方式联系我们：

- 通过GitHub提交issue咨询或反馈：

  - GitHub地址：[https://github.com/open-dingtalk/dingtalk-design-cli](https://github.com/open-dingtalk/dingtalk-fe-cli)
  - 提issue地址：[https://github.com/open-dingtalk/dingtalk-design-cli/issues](https://github.com/open-dingtalk/dingtalk-fe-cli/issues)
