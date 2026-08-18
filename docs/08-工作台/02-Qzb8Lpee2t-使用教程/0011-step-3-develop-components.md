---
title: "开发流程"
source_url: "https://open.dingtalk.com/document/dingstart/step-3-develop-components"
namespace: "dingstart"
slug: "step-3-develop-components"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 开发流程"
doc_id: "AdoYh6yRLn"
updated_at: "2026-08-18 09:12:00"
---

> Source: https://open.dingtalk.com/document/dingstart/step-3-develop-components
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 开发流程
> Updated: 2026-08-18 09:12:00

# 开发流程

## **步骤一：环境准备**

### **第一步：安装DingTalk CLI**

请参考以下步骤完成 DingTalk Design CLI 工具的安装：

1. 执行以下命令，检查 Node.js 版本

   > **[!NOTE]**
   >
   > DingTalk Design CLI 需要使用 Node.js 12.15.x 或更高版本。如果你未安装[Node.js](https://nodejs.org/en)，请前往 Node.js 官网下载并安装。

   ```
   node -v
   ```
2. 执行以下命令，安装 CLI 工具。

   ```
   npm install dingtalk-design-cli -g
   # or
   yarn global add dingtalk-design-cli
   ```
3. 执行以下命令，检查 CLI 工具是否安装成功。

   ```
   ding -v
   ```

   如图返回 dingtalk-design-cli 版本号，表示安装成功。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0280640071/p739456.png)

### **第二步：安装小程序开发 IDE**

安装方式可以查看[小程序开发工具](../../01-应用开发/06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)。

> **[!NOTE]**
>
> 确保小程序IDE的版本不低于 1.12.19。

## **步骤二：创建组件**

> **[!NOTE]**
>
> 组件是定制工作台组件的载体，一个插件里可以包含多个定制工作台组件（建议 10 个以内），具体哪些组件归属于一个插件可以按项目情况由开发者自行决定。

### **第一步：创建组件**

根据以下操作创建一个小程序插件：

1. 登录[开发者后台](https://open-dev.dingtalk.com)，打开[插件管理](https://open-dev.dingtalk.com/v1/fe/old#/bench-plugin)页面。
2. 单击**创建全码组件。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739502.png)
3. 根据实际开发情况添加插件信息。

   ![screencapture-open-dev-dingtalk-v1-fe-old-2023-11-20-14_46_57.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739504.png)

### **第二步：初始化组件代码**

1. 使用 CLI 工具创建脚手架，执行以下命令，进行初始化。myapp 是文件夹名称。

   ```
   ding init -o myapp
   ```
2. 应用类型选择「插件」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739507.png)
3. 模板仓库选择「定制工作台组件默认模板」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739508.png)
4. 选择开发语言，建议选择「javascript」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739509.png)

### **第三步：使用小程序开发者工具**

1. 选择「小程序插件」，单击「打开项目」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739514.png)
2. 选择第二步中本地初始化好的「myapp」项目。
3. 项目类型选择「工作台组件」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739516.png)
4. 左上角单击「选择关联应用」，选中第一步中在管理后台创建好的工作台组件。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5273640071/p739520.png)

## **步骤三：开发组件**

> **[!IMPORTANT]**
>
> 初始化后的项目文件，目录结构和文件名称不要修改，只修改 plugin/components 目录下的文件和
>
> plugin.json，否则会造成组件运行失败的情况。

文件目录结构，说明如下：

- **项目目录**

  ```
  ├── miniprogram // 本地预览入口，和组件实际运行无关
  ├── plugin // 组件代码目录
  │   ├── components // 组件代码
  │   │   ├── componentA
  │   │   │   ├── config.json
  │   │   │   ├── index.acss
  │   │   │   ├── index.axml
  │   │   │   ├── index.js
  │   │   │   └── index.json
  │   │   ├── componentB
  │   │   │   ├── config.json
  │   │   │   ├── index.acss
  │   │   │   ├── index.axml
  │   │   │   ├── index.js
  │   │   │   └── index.json
  │   │   └── plugin.json // 组件配置，插件根据plugin.json中的publicComponents来识别组件
  └── otherUtil.js
  ```
- **单个组件目录**

  ```
  index.json  // 组件配置文件
  index.acss  // 样式表
  index.axml  // 布局
  index.js    // 业务逻辑
  config.json // 组件在定制工作台设计器里的描述文件，只有需要在设计器上展示的组件才需要这个文件
  ```

### **第一步：本地开发组件**

在小程序 IDE 右侧，可以预览组件，表示运行成功。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1423840071/p739544.png)

### **第二步：配置组件信息**

config.json 是组件在定制工作台设计器上的描述文件。设计器上拖入和配置组件时，会从 config.json 中读取信息，拼装在整个页面的描述文件中，保存后供运行态加载，从而渲染出组件的运行态。

**config.json数据结构说明**：必填项必须按照说明填写，否则可能会出现组件上传失败、加载失败等问题。

| 属性名 | 是否必填 | 示例值 | 说明 |
| --- | --- | --- | --- |
| **pluginComponentName** | 是 | project-select-view | 组件名称，该名称必须和插件的配置文件 **plugin.json** 中 **publicComponents** 中定义的组件名保持一致 |
| **name** | 是 | 项目选择 | 组件的中文显示名，用于设计器中组件列表区标志该组件 |
| **icon** | 是 | https://static.dingtalk.com/media/lALOB0o7K8yQzJA\_144\_144.png | 设计器中组件列表区显示的图标，确保图标地址全网可访问 |
| **previewUrl** | 是 | https://img.alicdn.com/tfs/TB1KcAWdrj1gK0jSZFOXXc7GpXa-750-100.jpg | 设计器里展示时用到的静态图片地址，用于在设计器预览区中静态图片占位。截图宽度为 375px，在小程序 IDE 里截图即可 |
| **previewHeight** | 是 | 100 | 设计器预览区中静态图片占位的高度（单位 px ） |
| **setters** | 是 | [] | 设计器需要用到的自定义配置属性，如不需要可以设为[] |
| **props** | 是 | {} | setters 中每个 setter 对应的初始值，如 setters 为[]，可以设为{} |
| **dataSources** | 否 | [] | 如果组件里用到的数据源是固定的，不需要工作台设计者配置，可以用这个字段，将组件与数据源绑定。  详细说明，请参考[什么是数据源](0008-dashboard-overview-workbench.md#aba4b3c7c6w79)。 |

### **第三步：上传组件**

在小程序 IDE 右上角，单击「上传版本」。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5417405171/p739711.png)

## **步骤四：调试插件**

> **[!IMPORTANT]**
>
> - 无论是在开发者设计器中，还是正式的定制工作台设计器中，每次上传新的组件版本后，都需要在设计器里把组件删除后，再重新拖入配置一遍
> - 钉钉 5.0.6 以上的版本才支持插件，可能需要用户升级钉钉版本才能看到插件，在不支持插件的钉钉版本上，会有提示窗提示用户升级到钉钉最新版本

1. 登录[开发者后台](https://open-dev.dingtalk.com/v1/fe/old#/bench-plugin)，并打开[插件管理](https://open-dev.dingtalk.com/v1/fe/old#/bench-plugin)页面。
2. 单击「版本管理」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8004840071/p739713.png)
3. 单击「去设计器调试」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8004840071/p739714.png)
4. 切换到「自建组件」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8004840071/p739715.png)
5. 找到正在开发中的组件，拖入中间提示的空白位置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8004840071/p739716.png)
6. 单击右上角「预览」。

   > **[!NOTE]**
   >
   > 每次上传新的插件版本后，请在设计器里把组件删除，再重新拖入配置一遍使更新生效。这一点无论是开发者设计器，还是正式的工作台设计器，都适用。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8004840071/p739717.png)

## **步骤五：发布插件**

1. 登录[开发者后台](https://open-dev.dingtalk.com/v1/fe/old#/bench-plugin)，并打开[插件管理](https://open-dev.dingtalk.com/v1/fe/old#/bench-plugin)页面。
2. 单击「版本管理」。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8004840071/p739713.png)
3. 单击「提交上架」。

   > **[!NOTE]**
   >
   > 请保证在提交上架之前，已对组件进行了充分的测试。提交申请后，插件状态变为**上架审批中**。
   >
   > 插件将在1分钟内完成自动审核，并将审核结果同步到插件状态面板上，以及通过钉钉小秘书同步给开发者。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6134840071/p739719.png)
4. 审核通过后，插件状态变为**已上架**时，单击**提交发布**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6134840071/p739720.png)
5. 提交发布后，插件状态变为**灰度发布中**。单击**设置灰度**，设置灰度范围：

   > **[!NOTE]**
   >
   > 全量发布前必须进行灰度，如果不需要灰度，可以先设置一个灰度值后，单击全量发布。

   - **灰度百分比**

     - 灰度范围可设置为 1% ~ 70%，超过 70% 时请设置全量发布
   - **灰度组织（可选）**

     - 输入应用新插件的组织的 corpId。多个 corpId 请用（;）分隔
6. 通过灰度测试后，单击**全量发布**完成组件上线。

   > **[!IMPORTANT]**
   >
   > 全量发布后会直接影响线上用户。如果组件修改了config.json，在组件发布后，尽快在正式的工作台设计器里完成删除原组件，重新配置组件的操作，以免线上用户受到影响。
