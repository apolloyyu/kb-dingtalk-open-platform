---
title: "查询插件信息列表"
source_url: "https://open.dingtalk.com/document/development/query-plug-ins"
namespace: "development"
slug: "query-plug-ins"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 应用 > 查询插件信息列表"
doc_id: "lAkP54xiGp"
updated_at: "2026-08-25 13:50:06"
---

> Source: https://open.dingtalk.com/document/development/query-plug-ins
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 应用 > 查询插件信息列表
> Updated: 2026-08-25 13:50:06

# 查询插件信息列表

调用本接口查询插件信息列表。

> **[!IMPORTANT]**
>
> 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 不支持 | — |

## 请求方法

```
GET /v1.0/yida/plugins/infos/{instanceId}?accessKey=String&pageSize=Integer&callerUid=String&pageNumber=Integer HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| instanceId | String | 否 | 实例ID。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| accessKey | String | 否 | 访问密钥。 |
| pageSize | Integer | 否 | 分页大小。 |
| callerUid | String | 否 | 调用者的unionId。 |
| pageNumber | Integer | 否 | 分页页码。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| pageSize | Integer | 分页大小。 |
| pageNumber | Integer | 当前第几页。 |
| totalCount | Long | 总数量。 |
| pluginInfos | Array | 插件详情。 |
| pluginUuid | String | 插件的唯一编码。 |
| pluginTotalAmount | Long | 插件总数量。 |
| pluginName | String | 插件名称。 |
| iconUrl | String | 图标的URL。 |
| pluginPayType | Integer | 插件付费类型。 |
| pluginUsageAmount | Long | 插件使用量。 |
| pluginStatus | Integer | 插件状态。 |
| apps | Array | 应用名称。 |
| appName | String | 应用名称。 |

## 示例

**返回示例**

```
HTTP/1.1 200 OK
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | unclassifiedError | 异常:%s | 通用异常信息 |
