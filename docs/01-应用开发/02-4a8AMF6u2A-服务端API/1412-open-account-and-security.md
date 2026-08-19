---
title: "打开账号与安全"
source_url: "https://open.dingtalk.com/document/development/open-account-and-security"
namespace: "development"
slug: "open-account-and-security"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开帐号与安全"
doc_id: "hmY5RLbo3C"
updated_at: "2025-12-26 15:07:51"
---

> Source: https://open.dingtalk.com/document/development/open-account-and-security
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开帐号与安全
> Updated: 2025-12-26 15:07:51

# 打开账号与安全

通过AppLink协议可直接跳转至钉钉客户端的“账号与安全”设置页面，便于用户快速管理账号安全相关配置。

## **使用场景**

该协议为无参调用，直接触发页面跳转，无需传递额外字段，适用于需要引导用户进行安全设置的业务场景（如修改密码、绑定手机、开启双重验证等）。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (13)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1629375761/p556485.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/accountSafe
```

## **字段说明**

本协议为无参调用，不支持传递任何查询参数。所有跳转行为均指向统一的安全中心首页，默认展示当前用户的完整安全设置项。
