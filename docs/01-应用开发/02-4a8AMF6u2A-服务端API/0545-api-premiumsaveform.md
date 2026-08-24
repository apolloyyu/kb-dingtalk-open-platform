---
title: "创建或更新数据表单模板"
source_url: "https://open.dingtalk.com/document/development/api-premiumsaveform"
namespace: "development"
slug: "api-premiumsaveform"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 数据表单 > 表单模板 > 创建或更新数据表单模板"
doc_id: "3SXrx7U5DH"
updated_at: "2026-06-03 10:13:02"
---

> Source: https://open.dingtalk.com/document/development/api-premiumsaveform
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 数据表单 > 表单模板 > 创建或更新数据表单模板
> Updated: 2026-06-03 10:13:02

# 创建或更新数据表单模板

调用本接口，创建或更新数据表单模板。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

- 调用该接口创建的数据表单模板，使用的模板名称和接口返回的processCode值，请务必注意保存，方便后续调用其他接口使用。
- 数据表单模板仅支持文档下方所展示的表单组件，其他组件均不支持。

更新表单模板时需指定ProcessCode。

- 未填写该参数，表示新建一个模板。
- 填写该参数，表示更新所传值对应的审批模板。

**如何获取processCode**：在钉钉管理后台-审批模板查看，新旧版钉钉管理后台，获取方式不同：可参见[OA审批概述-名词解释-processCode](https://open.dingtalk.com/document/orgapp/workflow-overview)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/dataForms/templates |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 否 | 模板code，更新表单模板时需指定ProcessCode。   - 未填写该参数，表示新建一个模板。 - 填写该参数，表示更新所传值对应的审批模板。   **如何获取processCode**：在钉钉管理后台-审批模板查看。    新旧版钉钉管理后台，获取方式不同：可参见[名词解释-processCode](0473-workflow-overview.md)。  **新版钉钉管理后台**：在审批模板编辑页-基础设置-页面底部查看。 **旧版钉钉管理后台**：在审批模板编辑页的URL中查看。 |
| name | String | 是 | 表单模板名称。 |
| description | String | 否 | 表单模板描述。 |
| formComponents | Array | 是 | 表单控件列表，单一表单最大组件个数不超过200。 |
| FormComponent | FormComponent | 是 | 表单控件列表。详情请参考**FormComponent参数补充说明**。 |
| userId | String | 是 | 操作人userId，需为管理员。 |

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 返回的表单模板信息。 |
| processCode | String | 表单模板Code，企业内唯一 。    生成企业内唯一的数据表单模板编码，可使用此**processCode**发起数据表单实例。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "processCode" : "PROC-abcdef-example"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | processcode.error | processCode对应的表单不存在 | processCode对应的表单不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | processes.error | 获取模板列表失败 | 获取模板列表失败 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | system.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | user.not.exist | 用户不存在 | 用户不存在 |
| 500 | system.error | 系统错误 | 系统错误 |
| 500 | param.error | %s | 参数错误 |
| 500 | template.error | 表单模板已停用，联系管理员启用 | 表单模板已停用，联系管理员启用 |
| 500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验失败，未开通或过期 |
| 500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 请求过于频繁，稍后重试 |
