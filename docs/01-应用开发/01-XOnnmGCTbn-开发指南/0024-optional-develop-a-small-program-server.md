---
title: "（可选）开发小程序服务端"
source_url: "https://open.dingtalk.com/document/dingstart/optional-develop-a-small-program-server"
namespace: "dingstart"
slug: "optional-develop-a-small-program-server"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发小程序应用 > （可选）开发小程序服务端"
doc_id: "q0OjrkNfMA"
updated_at: "2026-06-30 09:00:29"
---

> Source: https://open.dingtalk.com/document/dingstart/optional-develop-a-small-program-server
> Path: 应用开发 / 开发指南 / 开发小程序应用 > （可选）开发小程序服务端
> Updated: 2026-06-30 09:00:29

# （可选）开发小程序服务端

本文档适用于**企业内部应用**和**第三方企业应用**的开发者，用于指导如何搭建和配置小程序服务端，实现免登、事件订阅及调用钉钉服务端 API。在开始前，请确保您具备以下权限与信息：

- 已登录[开发者后台](https://open-dev.dingtalk.com/#/)并拥有目标应用的管理权限；
- 能够获取应用的关键凭证（如 `Client ID`、`Client Secret`）；
- 理解 `access_token` 的作用及其获取方式：详见[获取访问凭证（accessToken）](../02-4a8AMF6u2A-服务端-API/0028-authorization-overview.md)；
- 了解用户唯一标识 `unionId` 的含义与获取路径：详见 [unionId介绍](0001-basic-concepts-beta.md#9dc00a3569e13)。

## 适用对象与权限说明

本文档主要面向**企业内部应用**和**第三方企业应用**服务端开发人员。此类应用由开发者自行开发并部署。

### 权限要求

- **管理员权限**：配置安全设置（如出口 IP）、申请 API 权限、开启事件订阅等功能需企业管理员或具备相应权限的角色操作。
- **access\_token 获取条件**：通过`Client ID` 和`Client Secret`调用接口获取，用于后续 API 调用的身份认证。
- **unionId 说明**：表示用户在钉钉体系内的唯一身份标识，可通过免登流程中的 `code` 换取用户信息接口获得。

建议提前熟悉 [基础概念](0001-basic-concepts-beta.md) 和 [应用类型与能力说明](0002-application-type-introduction.md)。

## 流程概览

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **安全设置**，填写服务端出口 IP。

   > **[!NOTE]**
   >
   > 服务端出口 IP 是指调用钉钉服务端 API 时所使用的服务器公网 IP 地址列表。若未正确配置，当发起 API 请求时，将返回如下错误提示：
   >
   > > 访问ip不在白名单之中，request ip=\*\*\*.\*\*\*.\*\*\*.\*\*\*, appKey(dingxxx)

   建议将生产环境和服务测试环境的所有可能出口 IP 添加至此处，支持多个 IP 以换行分隔。
3. 实现免登

   用户无需输入账号密码即可完成身份验证。推荐使用“扫码登录”或“静默授权”模式。

   详细流程请参考：[网页应用（H5微应用）免登](../02-4a8AMF6u2A-服务端-API/0018-enterprise-internal-application-logon-free.md)。
4. 申请接口调用权限。

   根据业务需求，在应用详情页中为应用添加所需的 API 权限。例如：发送机器人消息、读取组织架构、创建日程等。

   操作路径：**权限管理** > **添加接口调用权限**

   详情参考：[添加接口调用权限](../02-4a8AMF6u2A-服务端-API/0003-add-api-permission.md)。
5. 选择合适的事件推送方式并完成接入。

   通过事件订阅机制，开发者可以实时接收钉钉平台发生的各类事件通知（如用户加入企业、群消息发送、审批状态变更等），实现异步数据同步和自动化响应。

   企业内部应用支持两种方式接收钉钉推送的回调事件：HTTP 推送和 Stream 模式推送。

   详情参考：[配置 HTTP 推送（不推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#58bfd87c4fupu)和 [配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)。
6. 调用服务端 API，进行业务集成。

   在完成上述配置后，即可使用 `access_token` 调用钉钉开放能力，例如发送群机器人消息、创建审批实例、查询考勤记录等。

   示例：调用机器人接口发送文本消息

   详情参考：[服务端SDK下载](../02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。

## 验证与调试

### 发送测试消息验证机器人接口

1. 使用 Postman 或代码调用 `/v1.0/robot/groupMessages/send` 接口发送一条测试消息。
2. 观察目标群聊是否成功接收到消息。
3. 若失败，检查：

   - `access_token` 是否过期
   - 当前 IP 是否在白名单内
   - 应用是否已授权相关 API 权限

### 常见错误排查路径

| 错误现象 | 可能原因 | 解决方案 |
| --- | --- | --- |
| `访问ip不在白名单之中` | 服务器实际出口 IP 未添加 | 登录开发者后台，在**安全设置**中补充 IP |
| `invalid access_token` | token 过期或获取失败 | 重新调用获取接口，注意缓存有效期（通常为 2 小时） |
| `no api permission` | 缺少对应 API 权限 | 进入**权限管理**添加所需权限并提交审核（如需要） |

建议结合[全局错误码](../02-4a8AMF6u2A-服务端-API/0013-server-api-error-codes-1.md)快速定位问题。
