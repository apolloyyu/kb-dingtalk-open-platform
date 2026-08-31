---
title: "脚本服务和 UI 页面"
source_url: "https://open.dingtalk.com/document/dingstart/develop-document-coolapp-script-services-and-ui-pages"
namespace: "dingstart"
slug: "develop-document-coolapp-script-services-and-ui-pages"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发文档酷应用 > 脚本服务和 UI 页面"
doc_id: "4zElYIIetC"
updated_at: "2026-06-30 09:01:06"
---

> Source: https://open.dingtalk.com/document/dingstart/develop-document-coolapp-script-services-and-ui-pages
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发文档酷应用 > 脚本服务和 UI 页面
> Updated: 2026-06-30 09:01:06

# 脚本服务和 UI 页面

如果你想开发文档酷应用相关功能，可依据文档操作步骤进行开发。

## **背景信息**

文档酷应用由脚本服务页面和 UI页面两部分组成，你可通过编写脚本服务页面实现对文档的读写操作，通过编写UI页面实现在钉钉文档中展示可交互的自定义UI界面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6621872871/p562978.png)

## **操作步骤**

### **使用 DingTalk Design CLI 开发**

> **[!NOTE]**
>
> DingTalk Design CLI 提供以下能力：
>
> - 提供文档酷应用项目初始化能力。
> - 提供文档酷应用项目本地构建、开发调试能力。

1. 全局安装DingTalk Design CLI。

   ```
   npm install dingtalk-design-cli@1.0.10 -g

   # OR

   yarn global add dingtalk-design-cli@1.0.10
   ```
2. 通过以下命令初始化一个本地项目。

   ```
   ding init -o dingtalk-docs-cool-app-demo
   ```
3. 选择应用类型，需选择「文档酷应用」。
4. 选择模板类型为`default`。
5. 选择开发语言为`javascript`。
6. 进入`dingtalk-docs-cool-app-demo`项目目录。
7. 执行`ding dev`开启调试。
8. 根据脚手架指引，在命令行中执行**document <钉钉文档地址>**，可以自动打开钉钉文档，在确认安装文档酷应用后进行文档酷应用调试。

   > **[!NOTE]**
   >
   > 「钉钉文档地址」展示如下图：
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6621872871/p561411.png)
9. 安装文档酷应用。
10. 启用并使用文档酷应用。

    ![文档酷应用0303](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7106528761/p577019.gif)

### **使用文档酷应用JSAPI开发**

1. 使用npm安装依赖`dingtalk-docs-cool-app`。

   ```
   npm install dingtalk-docs-cool-app --save
   ```
2. 开发文档酷应用：

   - 搭建脚本服务页面，你可通过搭建脚本服务页面实现读写钉钉文档模型相关的业务需求：

     - 定义脚本函数：你可创建独立的js文件进行脚本函数的定义和注册。使用文档酷应用 JSAPI 提供的全局变量 DingdocsScript 访问文档对象模型 Workbook ，然后调用钉钉文档模型 API 实现文档操作，最后使用 DingdocsScript.registerScript 注册脚本函数。

       你可通过调用全局变量「DingdocsScript」注册脚本服务。

       ```
       /* 脚本函数js文件 */

       /*global DingdocsScript*/
       // 定义脚本函数
       function insertSheet() {
         const Workbook = DingdocsScript.workbook;
         const sheet = Workbook.insertSheet();
         sheet.activate();
       }

       // 注册脚本函数
       DingdocsScript.registerScript('insertSheet', insertSheet);
       ```
     - 初始化脚本服务页面：在使用脚本服务前，你需在脚本服务页面中调用initScript初始化脚本服务，导入脚本函数。

       调用[initScript](../03-Ogu5SlPY4t-客户端-JSAPI/0278-initialize-script-service.md)接口初始化脚本服务，向scriptUrl中注入全局变量「DingdocsScript」。

       ```
       /* 脚本服务页面 */

       import { initScript } from 'dingtalk-docs-cool-app';
       initScript({
         scriptUrl: '脚本函数js文件地址',
       })
       ```
   - 搭建 UI 页面：你可通过搭建UI页面实现在钉钉文档中展示个性化交互面板，在载入UI页面时，你需调用[initView](../03-Ogu5SlPY4t-客户端-JSAPI/0279-initialize-ui-interface.md)接口初始化UI页面。

     ```
     /* UI页面 */

     /*global Dingdocs*/
     import { initView } from 'dingtalk-docs-cool-app';
     initView({
      	onReady: () => {
       },
     })
     ```

     之后你可在UI页面中访问全局变量「Dingdocs」，借助Dingdocs提供的api与脚本服务页面进行交互，实现调用脚本服务页面注册的脚本函数。

     ```
     Dingdocs.script.run('insertSheet').then((res) => {})
     ```

     也可以通过「Dingdocs」与钉钉文档界面进行交互，实现例如弹出对话框容器等效果。

     ```
     Dingdocs.workbook.host.showDialog('http://www.example.com/dialog.html')
     ```
