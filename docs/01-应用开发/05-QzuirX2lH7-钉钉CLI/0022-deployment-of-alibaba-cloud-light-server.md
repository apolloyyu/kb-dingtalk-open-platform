---
title: "阿里云轻量服务器部署"
source_url: "https://open.dingtalk.com/document/development/deployment-of-alibaba-cloud-light-server"
namespace: "development"
slug: "deployment-of-alibaba-cloud-light-server"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "高级集成 > OpenClaw 常用部署方式 > 阿里云轻量服务器部署"
doc_id: "hAiYYyqsoT"
updated_at: "2026-07-14 09:22:36"
---

> Source: https://open.dingtalk.com/document/development/deployment-of-alibaba-cloud-light-server
> Path: 应用开发 / 钉钉CLI / 高级集成 > OpenClaw 常用部署方式 > 阿里云轻量服务器部署
> Updated: 2026-07-14 09:22:36

# 阿里云轻量服务器部署

## **前提条件**

- 已经完成了钉钉应用和机器人的创建与发布。
- 已经获取了钉钉应用的Client ID和Client Secret，用于后续使用。
- 通过快捷方式创建的OpenClaw机器人已自动获得`Card.Streaming.Write`、`Card.Instance.Write`和`qyapi_robot_sendmsg`权限点。

## **步骤一：购买 OpenClaw 套餐**

> **[!NOTE]**
>
> 如果已购买轻量应用服务器，可以跳过此步骤，以重置系统的方式部署OpenClaw（重置系统时选择应用镜像下的OpenClaw镜像），但重置系统会清除轻量应用服务器上的系统盘数据，请根据需要做好数据备份。具体操作，请参见[重置系统](https://help.aliyun.com/zh/simple-application-server/user-guide/reset-a-simple-application-server)。

1. [购买预装OpenClaw应用的轻量应用服务器](https://swasnext.console.aliyun.com/buy?regionId=us-east-1&planId=swas.s.c2m2s40b1.linux&imageId=bb90a88c7bac4cf48f7c49ccfcd44614&amount=1&duration=12&autoRenew=false#/)。

   > **[!NOTE]**
   >
   > 该应用镜像基于Alibaba Cloud Linux 3.2104 LTS 64位操作系统，来源于阿里云计算巢。
2. 在**轻量应用服务器**页面，预置了资源配置，如要更改配置项，请参考下面内容。

   - **实例**：内存必须2GiB及以上，可以根据自己的需求切换套餐。
   - **地域**：默认**美国（弗吉尼亚）**。
   - **购买配置**：默认12个月，可以根据自己的需求切换时长。

## **步骤二：配置OpenClaw**

1. 在[轻量应用服务器-控制台](https://swasnext.console.aliyun.com/servers)，单击服务器卡片中的实例ID，在**服务器概览**页面单击**应用详情**页签。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055787.png)
2. 在**OpenClaw使用步骤**区域中，单击**端口放通**下的**执行命令**，可开放获取OpenClaw服务运行端口的防火墙。

   > **[!IMPORTANT]**
   >
   > - 为了防止恶意扫描与定向攻击，OpenClaw 在初始化时不再使用固定的默认端口，而是自动生成一个随机端口，可在控制台[查看OpenClaw的端口号](#919a08364eg66)。
   > - 端口放通将使服务暴露于公网，支持一键关闭 WebUI 公网访问，详见[阿里云轻量服务器部署](#342265d2f8fkl)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055789.png)
3. 单击**配置OpenClaw**下的**执行命令**配置百炼API key。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055792.png)

   目前支持配置两种类型的百炼API Key：

   1. [Coding Plan](https://help.aliyun.com/zh/model-studio/coding-plan)**套餐专属 API Key**（推荐）：采用固定月费模式，提供月度请求额度，超出时段限额的调用会报错且不计费用，可避免产生超出预期的费用。

      > **[!NOTE]**
      >
      > Coding Plan 目前支持`qwen3.5-plus`、`kimi-k2.5`、`MiniMax-M2.5`、`glm-5`等模型，详细的模型列表请参考[Coding Plan概述](https://help.aliyun.com/zh/model-studio/coding-plan#dc0d98da6ev4j)。
   2. **按Token用量计费的百炼API Key**。

      API Key配置方式包括系统推荐及手动输入。系统推荐会列出百炼Coding Plan的API Key（成本可控），及离服务器最近的百炼模型服务的API Key（时延较低）。若需使用其他地域或者其他账号的API Key可选择手动输入。

      - **系统推荐（下拉选择）**

        | **轻量应用服务器所在地域** | **系统推荐的百炼API Key对应地域** | **Coding Plan的API key对应地域** |
        | --- | --- | --- |
        | 中国内地地域 | 华北2（北京） | 华北2（北京） |
        | 美国及欧洲地域 | 美国（弗吉尼亚） |
        | 中国香港及其他亚洲地域 | 新加坡 |
      - **手动输入**

        单击按钮切换至手动输入，输入百炼API Key并选择该API Key对应地域。

        > **[!NOTE]**
        >
        > 手动配置需确保选择的API Key对应地域正确，否则会导致模型无法正常调用。

        ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055793.png)
4. 单击**访问WebUI面板**下的**执行命令**，获取OpenClaw WebUI的地址，可以在Web页面与OpenClaw的Agent对话。

   > **[!NOTE]**
   >
   > 可根据需求参考[阿里云轻量服务器部署](#342265d2f8fkl)一键关闭WebUI的公网访问权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055798.png)
5. （可选）在**应用详情** **>** **基础配置** > **查看Token**中单击**执行命令**，查看并保存Token。

   > **[!IMPORTANT]**
   >
   > 请勿泄露包含 Token 的完整 URL。该链接包含身份验证凭据，任何持有此链接的人都能直接绕过登录验证，获得 OpenClaw 控制台的管理员权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055800.png)

## **步骤三：服务器控制台配置钉钉应用**

> **[!NOTE]**
>
> 该功能仅支持镜像版本为**OpenClaw 2026.2.9**及以上的实例。可在轻量应用服务器概览页的**基本信息** > **镜像信息**中查看当前实例的镜像版本。

1. 进入[轻量应用服务器-控制台](https://swasnext.console.aliyun.com/servers)，单击配置了OpenClaw的服务器卡片中的实例ID，在**服务器概览**页面单击**应用详情**页签。
2. 在**通道配置****>****钉钉**中填写已保存的钉钉应用的 **Client ID** 和 **Client Secret**，并单击**应用**，等待命令执行成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055807.png)
3. 至此，你已经完成了在阿里云轻量服务器中的部署操作。

## **常见问题**

- **如何重启OpenClaw网关？**

  当遇到连接中断或服务不可用等场景时，可在控制台页面重启OpenClaw网关。在**应用详情****>****基础配置****>****重启OpenClaw网关**中单击**执行命令**。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055808.png)
- **如何查看OpenClaw的端口号？**

  为了防止恶意扫描与定向攻击，OpenClaw 在初始化时不再使用固定的默认端口，而是自动生成一个随机端口。在**应用详情****>****基础配置****>****查看端口**中单击**执行命令**查看OpenClaw的端口号。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055809.png)
- **如何开启/关闭OpenClaw WebUI的公网访问？**

  用户可根据自身需求一键关闭OpenClaw WebUI的公网访问权限。在**应用详情****>****基础配置****>****公网访问**中单击**开启/关闭**控制OpenClaw WebUI的公网访问能力。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8252052771/p1055812.png)
