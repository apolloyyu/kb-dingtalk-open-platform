---
title: "同步存储数据"
source_url: "https://open.dingtalk.com/document/development/api-datasync"
namespace: "development"
slug: "api-datasync"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 同步存储数据"
doc_id: "CKait4oTVw"
updated_at: "2026-06-02 19:19:55"
---

> Source: https://open.dingtalk.com/document/development/api-datasync
> Path: 应用开发 / 服务端 API / 专属钉钉 > 同步存储数据
> Updated: 2026-06-02 19:19:55

# 同步存储数据

为应用同步数据到专属存储。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/datas/sync |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Common.ReadWrite-专属钉钉基础数据读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| sql | String | 是 | sql 语句。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/datas/sync HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7fdb7cf6b1aa340186809206a55a4a0d
Content-Type:application/json

{
  "sql" : "select id from connect_test"
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| rowsAffected | Integer | 影响行数。 |
| dataList | Array of Object | 代表数据的 map。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "rowsAffected" : 1,
  "dataList" : [ {
    "id" : 101
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | function.not.open | 企业未开通相应功能 | 企业未开通相应功能 |
| 400 | sql.format.error | sql格式错误 | sql格式错误 |
| 500 | system.busy | 系统繁忙 | 内部服务发生的异常情况 |
