---
title: "打开审批首页"
source_url: "https://open.dingtalk.com/document/development/open-approval-home-page"
namespace: "development"
slug: "open-approval-home-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开审批首页"
doc_id: "DfXOy5syb6"
updated_at: "2022-12-28"
---

> Source: https://open.dingtalk.com/document/development/open-approval-home-page
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开审批首页
> Updated: 2022-12-28

# 打开审批首页

本功能支持从第三方业务系统直接跳转至钉钉官方OA审批首页，实现无缝集成与快捷访问。

## 使用场景

适用于企业内部应用和第三方企业应用，在员工处理外部系统流程后可一键进入钉钉审批中心。

典型使用场景包括：

- 业务系统（如ERP、CRM）中完成数据提交后，自动跳转至钉钉审批首页处理相关流程；
- 第三方ISV应用为多个企业提供审批入口集成服务，统一通过`from`参数标识来源；
- 移动端或PC端多平台一致体验，支持Android、iOS、Mac、Windows四端对齐。

调用该跳转链接需确保当前用户已在钉钉客户端登录，并具备访问审批功能的权限（如企业成员身份）。管理员无需额外配置接口权限，但需确保应用已正确安装并启用。

![](https://img.alicdn.com/imgextra/i2/O1CN014YJdKP22JOgpHQ1S7_!!6000000007099-0-tps-1319-934.jpg)

## 协议

```
https://applink.dingtalk.com/approval/home
```

该协议为标准HTTP/HTTPS跳转链接，通过URL Query参数传递必要信息。参数说明如下：

- `corpId`：标识目标企业，确保跳转至正确的组织架构下的审批首页。
- `from`：标识请求来源应用，用于行为追踪与安全校验。

为保障安全性，不建议在公开页面暴露完整的跳转链接，尤其是包含敏感企业信息的corpId。推荐在受控环境中（如已登录的企业门户内）进行跳转调用。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **Mac** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | 7.0.30 | 7.0.30 | 7.0.30 | 7.0.30 |

## **字段说明**

| **名称** | **类型** | **是否必填** | **示例值** | **描述** |
| --- | --- | --- | --- | --- |
| corpId | String | 是 | ding16b\*\*\*\*c288 | 企业corpId，可参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。 |
| from | String | 是 | ding\*\*\*\*lxhgn | 请求来源，建议传开发者后台的应用key：   - 企业内部应用，填写应用的 [ClientID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（appKey）。 - 第三方企业应用，填写应用 [ClientID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（suiteKey）。 |

> **[!NOTE]**
>
> `from` 参数虽无严格校验机制，但错误填写可能导致数据统计异常或来源不可追溯，建议严格按照规范传值。

## **使用示例**

**确认前置条件**：

- 已创建企业内部应用或第三方企业应用；
- 应用已完成发布或调试配置；
- 当前操作用户为企业成员且拥有审批访问权限；
- 已获取企业的`corpId`和应用的`appKey`/`suiteKey`，位于“凭证与基础信息”模块。

> **[!NOTE]**
>
> 使用前请确认填写参数是否正确。

**构造跳转链接**：

将获取到的参数代入协议模板：

```
https://applink.dingtalk.com/approval/home?corpId=ding16b24****8e4f7c288&from=dingm****klxhgn
```

验证跳转结果：

- 在已登录钉钉的浏览器或客户端中点击该链接；
- 成功时应直接打开钉钉OA审批首页；
- 可检查页面是否显示当前企业的待办审批列表，确认企业上下文正确加载。
