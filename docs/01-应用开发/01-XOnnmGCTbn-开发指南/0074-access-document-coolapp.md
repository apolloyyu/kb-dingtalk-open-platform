---
title: "接入文档酷应用"
source_url: "https://open.dingtalk.com/document/dingstart/access-document-coolapp"
namespace: "dingstart"
slug: "access-document-coolapp"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发文档酷应用 > 接入文档酷应用"
doc_id: "A8B490ozrG"
updated_at: "2026-01-29 14:49:52"
---

> Source: https://open.dingtalk.com/document/dingstart/access-document-coolapp
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发文档酷应用 > 接入文档酷应用
> Updated: 2026-01-29 14:49:52

# 接入文档酷应用

本文档指导开发者将酷应用扩展至钉钉文档场景，实现与电子表格（如钉钉在线Excel）的深度集成。文档酷应用允许企业在工作表中通过菜单项启动侧边栏、执行脚本服务等操作，提升数据协作和业务自动化能力。

## **前提条件**

需要完成[创建酷应用](https://open.dingtalk.com/document/dingstart/create-coolapp)流程。

## **操作步骤**

1. 选择**扩展到文档。**。
2. 完善文档酷应用基本信息。
3. 上传文档酷应用Manifest文件，Manifest文件定义了文档酷应用的基础行为，详情参见[配置文档酷应用Manifest](0075-configure-document-coolapp-manifest.md)，示例如下：

   ```
   {
     "workbook": {
       "scriptService": {
         "url": "https://www.example.com/script.html"
       },
       "menus": [
         {
           "name": "启动",
           "action": {
             "type": "open-side-bar",
             "url": "https://www.example.com/sidebar.html"
           }
         }
       ]
     }
   }
   ```
4. 确定配置信息完成后，单击**保存**。
5. 单击**发布**，完成文档酷应用发布操作。

## **后续步骤**

文档酷应用完成发布后，需要完成[发布应用](0019-publish-dingtalk-application.md)，以便企业成员正式使用。建议发布前进行沙箱环境测试，确保功能稳定性和安全性。
