---
title: "无网弱网解决方案"
source_url: "https://open.dingtalk.com/document/dingstart/weak-network-solution-without-network"
namespace: "dingstart"
slug: "weak-network-solution-without-network"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 性能优化（ISV应用） > 无网弱网解决方案"
doc_id: "n70qzGWbHd"
updated_at: "2026-06-30 09:00:40"
---

> Source: https://open.dingtalk.com/document/dingstart/weak-network-solution-without-network
> Path: 应用开发 / 开发指南 / 开发网页应用 > 性能优化（ISV应用） > 无网弱网解决方案
> Updated: 2026-06-30 09:00:40

# 无网弱网解决方案

资源离线能力，解决无网弱网资源加载的问题，可以让H5在无网弱网的时候也能够访问。

## **准备内容**

1. 需要有公网可访问的页面链接，链接需要.html或者.htm结尾，例如：`https://www.dingtalk.com/xiangchen-test/xiangchen-webapp-test/mpa-demo/index.html`。
2. 需要产出一个 ZIP 包，可以参考下面使用步骤的第 6 步。

## **操作步骤**

1. 参考[应用创建与配置](0007-create-application.md)，创建一个企业内部应用。
2. 在应用详情页，单击**应用能力** > **添加应用能力**，选择网页应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0421872871/p973620.png)
3. 添加应用能力完成后，即可跳转至 H5 应用配置信息页面。配置应用入口。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0421872871/p973626.png)

   配置完成后，单击保存。
4. 配置完成后，必须要先发布一个版本，单击**应用发布** > **版本管理与发布** > **创建新版本**，并完成版本发布。
5. 开启离线包管理，获取离线包ID。

   > **[!NOTE]**
   >
   > 该权益属于一对一支持功能，请联系您的钉钉客户经理开通试用或购买**。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9852410571/p973647.png)
6. 本地环境构建 ZIP 包：

   1. 安装CLI工具。

      ```
      npm install dingtalk-h5package-opensdk --save-dev
      ```
   2. 在项目工程中，创建离线包打包配置文件 localresource.json，文件示例如下：

      > 下方链接仅为示例，具体链接请根据实际开发环境配置。

      - 示例页面链接：https://www.example.com/index.html
      - 示例页面资源：

        - https://www.example.com/home/index.js
        - https://www.example.com/home/index.css
      - 示例dist目录结构，文件夹路径和页面资源访问路径完成一致。

        ```
        ├── dist
        │ ├── index.html
        │ └── home
        │ │ ├── index.js
        │ │ └── index.css
        └── localresource.json
        ```
      - 示例localresource.json配置，无法在dist目录存储的，可以将链接配置到externalAssets字段。

        ```
        {
          "miniAppId": "992****5621", // 离线包ID
          // 线上资源URL和本地文件、目录映射关系。key 为本地资源对应的线上资源URL路径，值 为本地资源目录。
          "assets": {
            // 键值为目录。此配置意思是将 ./dist 目录下的资源添加到 https://www.example.com/myapp 路径下
            "https://www.example.com/myapp": "./dist"
          },
          // 依赖的外部URL列表。
          "externalAssets": [
            "https://unpkg.com/react@16.7.0/umd/react.production.min.js",
            "https://unpkg.com/vue@3.2.45/dist/vue.global.js",
            "https://unpkg.com/jquery@3.6.1/dist/jquery.js"
          ]
        }
        ```
   3. 在项目工程下运行打包命令，在本地输出格式 zip 的资源文件。

      ```
      npx h5package pack
      ```
7. 构建完成后，上传离线包。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9852410571/p973655.png)
8. 上传完成后，单击发布即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9852410571/p973670.png)

   > 支持回退到上一版本。
