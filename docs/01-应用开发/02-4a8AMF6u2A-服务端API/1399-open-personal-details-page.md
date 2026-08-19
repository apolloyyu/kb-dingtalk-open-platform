---
title: "打开个人详情页"
source_url: "https://open.dingtalk.com/document/development/open-personal-details-page"
namespace: "development"
slug: "open-personal-details-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开个人详情页"
doc_id: "ZjRlJKdxOu"
updated_at: "2026-01-22 20:17:44"
---

> Source: https://open.dingtalk.com/document/development/open-personal-details-page
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开个人详情页
> Updated: 2026-01-22 20:17:44

# 打开个人详情页

AppLink协议支持通过指定链接快速打开钉钉内的个人详情页，适用于客户管理、员工通讯录等场景。该功能允许开发者构造特定格式的URL，在支持的客户端环境中实现一键跳转至目标用户的个人信息界面。

## **使用场景**

- 在企业应用中，当需要从外部系统快速访问某位员工或联系人的钉钉个人资料时，可通过预置的AppLink链接直接唤起钉钉App。
- 成功跳转后将展示其个人详情页，提升操作效率和用户体验。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验跳转效果：

![qrcode (4)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6209375761/p556511.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/profile
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/profile | phone | 是 | 员工的手机号，请填写正确的手机号信息。 |

## 注意事项

- **隐私权限控制**：仅当当前用户有权查看目标员工联系方式时，才能成功跳转并显示相关信息；否则客户端可能提示“无权访问”。
- **手机号有效性校验**：请确保传入的`phone`参数为有效的手机号格式，且在企业通讯录中真实存在，否则跳转将失败。
- **非企业员工行为**：若目标用户非本企业成员，即使号码正确也无法打开其钉钉详情页。
- **跨平台兼容性**：目前仅Android与iOS客户端支持此功能（≥6.5.45版本），macOS与Windows端暂不支持。

## **使用示例**

> **[!NOTE]**
>
> 请填写正确的手机号信息。

构造标准AppLink URL：

```
https://applink.dingtalk.com/page/profile?phone=155****3240
```

**验证方法**：

- 将构造好的URL嵌入H5页面或生成二维码。
- 使用移动端钉钉打开该链接。
- 客户端应自动唤起并跳转至对应用户的个人详情页。
- 若未响应，请检查以下内容：

  - URL格式是否符合规范；
  - 当前网络状态是否正常；
  - 手机号是否为企业通讯录内有效号码；
  - 当前用户是否有权限查看该员工信息；
  - 客户端版本是否满足最低要求（≥6.5.45）。
