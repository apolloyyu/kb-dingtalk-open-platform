---
title: "小程序 scheme"
source_url: "https://open.dingtalk.com/document/development/scheme-of-mini-programs-1"
namespace: "development"
slug: "scheme-of-mini-programs-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > 小程序 scheme"
doc_id: "sJVbBtoIdu"
updated_at: "2025-09-17 20:58:13"
---

> Source: https://open.dingtalk.com/document/development/scheme-of-mini-programs-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > 小程序 scheme
> Updated: 2025-09-17 20:58:13

# 小程序 scheme

钉钉小程序 scheme 是在钉钉内打开一个指定小程序最方便的方式。

> **[!IMPORTANT]**
>
> scheme 遵循[RFC 3986](https://tools.ietf.org/html/rfc3986) 约定的 URI 规范。需特别注意，应针对拼接的参数进行 encode ，建议使用对应语言下的uri库来完成 scheme 拼接。

小程序scheme规则适用于以下场景：

- 从 H5 跳转到某个小程序。
- 生成一个二维码，供用户通过钉钉扫码打开小程序。

从 H5 跳转到小程序，可以使用dd.biz.util.openLink，详情请参考[打开目标页面](https://open.dingtalk.com/document/orgapp/open-link-on-new-window)。

根据不同业务类型，钉钉小程序分为第三方企业应用、企业内部应用以及第三方个人应用。这三种业务类型的 scheme 存在一些异同。

## 企业内部应用

`dingtalk://dingtalkclient/action/open_micro_app`

支持的参数：

| **参数名** | **是否必填** | **说明** |
| --- | --- | --- |
| corpId | 是 | 小程序应用所在企业的corpId，请参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-bbk-mv0-oxd)。 |
| agentId | 是 | 小程序应用的agentId，请参考[基础概念-AgentId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#884d363067bnq)。 |
| miniAppId | 是 | 小程序的miniAppId，请参考[基础概念-MiniAppId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-567-r47-n7t)。 |
| pVersion | 是 | 协议版本号，目前该字段值必须为1。 |
| packageType | 是 | 包类型号，目前值必须为1。 |

## 第三方企业应用

`dingtalk://dingtalkclient/action/open_micro_app`

支持的参数：

| **参数名** | **是否必填** | **说明** |
| --- | --- | --- |
| corpId | 否 | 已授权开通该应用的企业corpid。  如果不填写，会引导用户进入选择企业的界面。 |
| appId | 是 | 小程序应用的appid，开发者后台第三方企业应用，应用信息里的 appId 字段。  iShot2022-01-04 11 |

## 第三方个人应用

`dingtalk://dingtalkclient/action/open_mini_app`

支持的参数：

| **参数名** | **是否必填** | **说明** |
| --- | --- | --- |
| miniAppId | 是 | 小程序的miniAppId，可以在开发者后台应用基础信息页面查看。 |

![iShot2022-01-04 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5377621461/p379168.png)

## 通用参数

除了上述不同应用类型的特定参数，还有如下的通用参数。

| **参数名** | **是否必填** | **说明** |
| --- | --- | --- |
| page | 否 | 小程序的 page 地址，可以加 get 参数。默认是小程序首页 |

> **[!IMPORTANT]**
>
> get 参数请正确 encode，并在业务代码里校验参数合法性。

## 生成小程序

目前尚未提供生成二维码的 API，开发者可以自行使用其他工具根据 scheme 生成二维码。

## 如何在 scheme 上携带业务参数？

建议通过 page 的 get 参数携带。例如希望通过跳转到个人小程序（id=123）的 pages/index/index 页面，携带业务参数 x 值为 `中文` 则 scheme 应该为：`dingtalk://dingtalkclient/action/open_mini_app?miniAppId=123&page=pages%2Findex%2Findex%3Fx%3D%25E4%25B8%25AD%25E6%2596%2587`

page 参数里的这一堆内容是由 `` encodeURIComponent(`pages/index/index?x=${encodeURIComponent('中文')}`); ``生成的。

> **[!IMPORTANT]**
>
> 要符合 URI 规范，正确encode。确保在各个系统内传递时不出错。通过这样的 scheme，在对应的 Page onLoad 回调里获取参数。
