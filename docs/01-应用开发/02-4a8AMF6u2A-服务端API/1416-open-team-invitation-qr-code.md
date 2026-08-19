---
title: "打开团队邀请二维码"
source_url: "https://open.dingtalk.com/document/development/open-team-invitation-qr-code"
namespace: "development"
slug: "open-team-invitation-qr-code"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开团队邀请二维码"
doc_id: "jbBXjBPs8L"
updated_at: "2026-07-21 09:26:24"
---

> Source: https://open.dingtalk.com/document/development/open-team-invitation-qr-code
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开团队邀请二维码
> Updated: 2026-07-21 09:26:24

# 打开团队邀请二维码

本文档介绍如何通过 AppLink 协议在钉钉客户端中打开团队邀请二维码页面。该功能适用于企业内部应用或第三方应用，允许开发者通过构造特定 URL Schema 直接唤起钉钉客户端并跳转至指定企业的团队邀请页，便于成员快速加入群组。

## **使用场景**

- 当企业希望从外部 H5 页面引导用户加入团队群聊时，可通过该协议生成跳转链接。
- 第三方服务商为多个客户企业提供集成服务时，可动态拼接 corpId 构造个性化邀请入口。
- 应用内嵌 Web 页面需要实现“一键打开团队邀请码”功能，提升成员拉新效率。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/group_invite_qrcode
```

该 URL 是钉钉 AppLink 的标准跳转路径，用于触发客户端打开团队邀请二维码页面。需附加参数`corpId`指定目标企业。

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/group\_invite\_qrcode | corpId | 是 | 指定团队的corpId，可参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。  **[!NOTE]**  当前访问用户，必须在该corpId企业下，否则无法正常打开团队邀请二维码页面。 |

## **使用示例**

```
https://applink.dingtalk.com/page/group_invite_qrcode?corpId=ding16b*****8e4f7c288
```

**注意事项**：

- 不支持外部联系人直接使用；非企业成员点击后将无法打开页面。
- 无明确调用频次限制，但建议避免高频生成链接以防止风控拦截。
- 错误表现形式：跳转失败、页面空白、提示“您没有权限访问此页面”等。
