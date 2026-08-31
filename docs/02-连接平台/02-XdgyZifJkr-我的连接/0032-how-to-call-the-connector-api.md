---
title: "如何调用连接器API"
source_url: "https://open.dingtalk.com/document/connection/how-to-call-the-connector-api"
namespace: "connection"
slug: "how-to-call-the-connector-api"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > API参考 > 如何调用连接器API"
doc_id: "7zc9oOt4uk"
updated_at: "2025-09-23 19:20:33"
---

> Source: https://open.dingtalk.com/document/connection/how-to-call-the-connector-api
> Path: 连接平台 / 我的连接 / 开发参考 > API参考 > 如何调用连接器API
> Updated: 2025-09-23 19:20:33

# 如何调用连接器API

调用连接器API前，需要先获取API调用凭证。

## 接口调用流程

在调用连接器API前，您需要完成以下准备工作：

1. 获取应用的access\_token。access\_token相当于是身份凭证。调用接口时，通过access\_token来鉴权调用者身份。

   - 自建连接器可使用任一企业内部应用生成的access\_token，详情请参考[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)。
   - 三方连接器请使用关联的三方企业应用生成的acceess\_token，详情请参考[获取第三方应用授权企业的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)。
2. 调用服务端接口，请参考[发送连接器事件](0033-dingtalk-connector-data-synchronization-interface.md)。

## 调用方式

钉钉开放平台提供了API Explorer和SDK方便开发者调用服务端API。

- API Explorer：

  API Explorer是可视化在线API调用工具，可实时查看API请求和返回结果。访问地址：<https://open-dev.dingtalk.com/apiExplorer>
- SDK:

  钉钉开放平台提供了Java、PHP、Python、.NET SDK供开发者使用。单击[服务端SDK下载](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。
