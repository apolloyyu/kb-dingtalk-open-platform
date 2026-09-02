---
title: "上传小程序"
source_url: "https://open.dingtalk.com/document/dingstart/upload-miniapp"
namespace: "dingstart"
slug: "upload-miniapp"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发小程序应用 > 上传小程序"
doc_id: "FCg3mWszw3"
updated_at: "2026-06-30 09:00:32"
---

> Source: https://open.dingtalk.com/document/dingstart/upload-miniapp
> Path: 应用开发 / 开发指南 / 开发小程序应用 > 上传小程序
> Updated: 2026-06-30 09:00:32

# 上传小程序

使用钉钉开发者工具完成小程序的开发与调试后，可通过本流程将代码上传至钉钉开放平台，以便后续发布和管理。上传后的版本为开发版本，可用于设置体验版进行测试验证，但不会对普通用户生效。正式上线前需在开发者后台提交审核并发布

## **前提条件**

1. 已完成[应用创建与配置](0007-create-application.md)流程。
2. 已完成[开发小程序前端](0028-develop-miniapp-fe.md)流程。
3. 当前操作者需具备管理员或开发者角色权限，以确保可执行上传及后续发布操作。

## 操作步骤

1. 打开小程序开发工具，确保项目已正确加载并编译通过。
2. 确认当前分支为待上传版本对应的代码分支，避免误传测试或旧版本。
3. 在开发者工具顶部菜单栏中，点击【上传】按钮，触发版本打包与上传流程。

   > **[!NOTE]**
   >
   > 填写版本（建议格式：v1.0.0 - 首次提交），上传成功后，小程序当前运行的版本为开发版本。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2823809671/p1037232.png)
4. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
5. 单击**应用能力** > **小程序**，确认版本上传是否成功。

   > **[!NOTE]**
   >
   > 小程序在正式发布前，可通过设置体验版进行测试。系统会自动生成体验版的二维码，你可以通过二维码来测试和验证小程序。

## **后续步骤**

上传并验证无误后，您需要进行[发布应用](0019-publish-dingtalk-application.md)，提交审核并正式对外发布。

- 发布前建议充分测试核心功能与交互逻辑，确保用户体验稳定。
- 正式发布后，所有授权范围内的用户均可访问该小程序。
