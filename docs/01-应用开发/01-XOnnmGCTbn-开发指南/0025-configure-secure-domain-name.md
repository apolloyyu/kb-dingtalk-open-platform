---
title: "（可选）配置安全域名"
source_url: "https://open.dingtalk.com/document/dingstart/configure-secure-domain-name"
namespace: "dingstart"
slug: "configure-secure-domain-name"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发小程序应用 > （可选）配置安全域名"
doc_id: "d76FMTefML"
updated_at: "2026-06-30 09:00:30"
---

> Source: https://open.dingtalk.com/document/dingstart/configure-secure-domain-name
> Path: 应用开发 / 开发指南 / 开发小程序应用 > （可选）配置安全域名
> Updated: 2026-06-30 09:00:30

# （可选）配置安全域名

如果小程序前端需要与服务端进行网络通信，或者需要使用 web-view 组件内嵌网页页面，必须配置安全域名。本文档将指导您完成 HTTP 可信域名和 Webview 可信域名的配置流程，并说明相关限制与注意事项。

## 适用对象

本功能适用于所有使用小程序网络通信能力的企业内部应用和第三方企业应用。仅支持拥有管理员权限或具备开发者权限的账号进行安全域名配置。

## **前提条件**

1. 已完成[应用创建与配置](0007-create-application.md)流程。
2. 应用类型为企业内部应用或第三方企业应用（根据实际场景选择）。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **安全设置**。
3. 在“安全域名”区域选择需要添加的域名类型并填写域名：

   - **HTTP 可信域名**：如果小程序前端需要与服务端进行网络通信，需在此处配置一个或多个服务端域名或 IP 地址。仅允许通过已配置的域名或 IP 进行网络通信。
   - **Webview 可信域名**：若小程序使用web-view 组件加载网页内容，需将目标网页地址的主域名添加至此列表。

     > **[!NOTE]**
     >
     > web-view 组件内仅支持 http 或者 https 协议的网页页面地址，不支持其他协议地址。
4. 填写完毕后，单击**保存**，完成安全域名配置。

## 验证方法

配置完成后，建议通过以下方式验证是否生效：

1. 在小程序中调用[httpRequest](../03-Ogu5SlPY4t-客户端JSAPI/0010-jsapi-http-request.md)接口，向已配置的 HTTP 可信域名发起请求，检查控制台日志是否有网络错误。
2. 使用 web-view 组件加载已配置的 Webview 可信域名页面，确认页面能正常显示。

## 注意事项

- 安全域名更新后，必须使用钉钉开发者工具重新构建并上传小程序包，否则更改不会生效。
- 小程序使用[httpRequest](../03-Ogu5SlPY4t-客户端JSAPI/0010-jsapi-http-request.md)API请求的服务地址域名，都必须在 HTTP 安全域名中配置。
- 建议避免使用 IP 地址作为生产环境域名，部分客户端策略可能限制 IP 直接访问。
- 所有线上环境应强制使用 HTTPS 加密传输，保障数据安全。
