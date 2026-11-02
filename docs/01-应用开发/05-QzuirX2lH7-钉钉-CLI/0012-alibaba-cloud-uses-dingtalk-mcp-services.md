---
title: "阿里云百炼使用钉钉MCP服务"
source_url: "https://open.dingtalk.com/document/development/alibaba-cloud-uses-dingtalk-mcp-services"
namespace: "development"
slug: "alibaba-cloud-uses-dingtalk-mcp-services"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "进阶实战 > MCP 服务接入 > 阿里云百炼使用钉钉MCP服务"
doc_id: "Ib3gxduS9e"
updated_at: "2026-05-19 16:40:40"
---

> Source: https://open.dingtalk.com/document/development/alibaba-cloud-uses-dingtalk-mcp-services
> Path: 应用开发 / 钉钉 CLI / 进阶实战 > MCP 服务接入 > 阿里云百炼使用钉钉MCP服务
> Updated: 2026-05-19 16:40:40

# 阿里云百炼使用钉钉MCP服务

本文介绍了开发者如何在钉钉外的Agent中使用钉钉MCP的流程。

## **准备工作**

- [访问 MCP 广场](https://mcp.dingtalk.com/#/)选择服务，并确定好目标服务。
- 已经开通了阿里云百炼，且已经登录了[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing/?spm=5176.42028462.nav-v2-dropdown-menu-0.d_main_2_1_1.41a1154aRVMa98&tab=mcp&scm=20140722.M_10904461._.V_1#/mcp-market)。
- 部分MCP服务需要申请权限。

## **操作步骤**

1. 登录[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing/?spm=5176.42028462.nav-v2-dropdown-menu-0.d_main_2_1_1.41a1154aRVMa98&tab=mcp&scm=20140722.M_10904461._.V_1#/mcp-market)。
2. 依次选择**MCP 管理/MCP 广场** > **创建MCP** > 选择**脚本部署**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9000959671/p1050060.png)
3. 使用钉钉 MCP 市场的 MCP Service 配置信息在百炼中进行 MCP 服务配置，点击“提交部署”。

   > **[!NOTE]**
   >
   > 百炼MCP安装方式为"type": "streamableHttp" ，与钉钉MCP Service配置中的"type":"streamable-http"具有一定的差异。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9000959671/p1050079.png)
4. 依次选择**应用管理** > **创建应用** > **立即创建**， 创建智能体应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9000959671/p1050077.png)
5. 点击**MCP服务** > 选择**自定义MCP**，然后选择已经创建的MCP服务。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9000959671/p1050081.png)
6. 调用MCP服务工具。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9000959671/p1050085.png)
