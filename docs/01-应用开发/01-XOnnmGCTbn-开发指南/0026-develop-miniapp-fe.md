---
title: "开发小程序前端"
source_url: "https://open.dingtalk.com/document/dingstart/develop-miniapp-fe"
namespace: "dingstart"
slug: "develop-miniapp-fe"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发小程序应用 > 开发小程序前端"
doc_id: "9bd1iheaYa"
updated_at: "2026-06-30 09:00:31"
---

> Source: https://open.dingtalk.com/document/dingstart/develop-miniapp-fe
> Path: 应用开发 / 开发指南 / 开发小程序应用 > 开发小程序前端
> Updated: 2026-06-30 09:00:31

# 开发小程序前端

在钉钉开发者工具中，您可以进行小程序的开发、调试、预览和发布等操作。本文将为您详细介绍如何使用钉钉开发者工具完成小程序前端开发的全流程。更多有关钉钉开发者工具的信息，参考[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)。

## **前提条件**

需要完成[应用创建与配置](0007-create-application.md)流程。

## **操作步骤**

1. 下载并安装[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)，并在左侧菜单栏中选择小程序。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037201.png)
2. 在选择端时，选择钉钉，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037202.png)
3. 在选择模板时，可选择空白模板，也可选择官方的模板，推荐使用空白模板。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037204.png)
4. 在新建项目中，选择应用类型，并填写项目的基本信息后，点击**完成**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037206.png)
5. 点击左上角**登录**按钮后，使用钉钉账号扫码登录。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037209.png)
6. 登录成功后，选择应用类型和关联应用。

   > **[!NOTE]**
   >
   > 项目初始化完成后，工具将自动加载项目结构，包括 `app.json`（全局配置）、`pages/`（页面目录）等标准文件夹或文件夹，小程序框架说明可参考[钉钉小程序框架](../03-Ogu5SlPY4t-客户端-JSAPI/0431-mini-app-directory-structure-of-mini-programs.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037211.png)
7. 使用前端框架编写小程序前端组件界面，实现小程序的交互和展示。

   > **[!NOTE]**
   >
   > 你可以参考[小程序基础组件](../03-Ogu5SlPY4t-客户端-JSAPI/0476-mini-app-dd-view-container.md)、和[钉钉设计开放资源](https://open.dingtalk.com/document/design_latest)引入样式和 UI 组件，设计小程序页面，提高用户体验。
8. 编写过程中，你可以随时在右侧进行预览。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5552376671/p1037213.png)

   - 手机端真机预览：单击预览按钮，待二维码生成完毕后，使用手机钉钉扫码。
   - PC端真机预览：单击预览按钮，待二维码生成完毕后，单击二维码可复制二维码链接地址，然后在PC钉钉客户端钉钉聊天框内粘贴该地址并访问。

## **后续步骤**

小程序开发和调试完成后，你需要进行[上传小程序](0027-upload-miniapp.md)。

## 最佳实践建议

- 保持代码结构清晰，按功能模块组织页面与组件。
- 使用常量文件统一管理 API 地址和配置项，便于维护。
- 对复杂逻辑进行封装，提升代码复用率。
- 定期清理无用代码和注释，减少包体积。
- 发布前进行全面回归测试，保障用户体验稳定。
