---
title: "保存流程中心外部集成审批模板"
source_url: "https://open.dingtalk.com/document/development/api-premiumsaveintegratedprocess"
namespace: "development"
slug: "api-premiumsaveintegratedprocess"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 自有 OA 审批 > 审批表单 > 保存流程中心外部集成审批模板"
doc_id: "dJVZyAf6ss"
updated_at: "2026-06-03 10:12:59"
---

> Source: https://open.dingtalk.com/document/development/api-premiumsaveintegratedprocess
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 自有 OA 审批 > 审批表单 > 保存流程中心外部集成审批模板
> Updated: 2026-06-03 10:12:59

# 保存流程中心外部集成审批模板

调用本接口，可以将三方业务系统中的自有审批模板数据同步到钉钉OA审批，同时支持在模板维度进行审批页面托管、自定义业务分组、自定义快捷审批等多个高级功能模块自定义集成配置。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景，查看全部[专享OpenAPI](1442-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md)。

- 每个企业最多创建流程中心200个模板，超过最大数量后调用接口会报错。
- 钉钉客户端展示审批列表时，仅展示模板表单的前三个选项。
- 调用该接口创建的自有审批流模板，使用的模板名称和接口返回的processCode值，请务必注意保存，方便后续调用其他接口使用。
- 自有OA审批模板仅支持文档下方所展示的审批组件，其他组件均不支持。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processCentres/schemas |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 否 | 表单ProcessCode，更新表单模板时需指定ProcessCode，可通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取processCode参数值。      如果传递ProcessCode进行表单组件修改和更新，不允许删除或修改已作为流程设计中条件分支的控件数据。 例如，原表单中存在单选控件【员工类型】作为分支条件，则更新此表单时，不允许修改或删除【员工类型】字段的控件类型。     - 未填写该参数，表示新建一个模板。 - 填写该参数，表示更新所传值对应的审批模板。 |
| name | String | 是 | 表单模板名称。 |
| description | String | 否 | 表单模板描述。 |
| formComponents | Array | 是 | 表单控件列表，详情请参考[FormComponent参数说明](0474-oa-formcomponent-message.md#900adc515fxr6)，单一表单最大组件个数不超过200。支持的控件类型如下：   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件 - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件（表格控件） - **DDAttachment**：附件 - **InnerContactField**：联系人控件 - **RelateField**：关联审批单 - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件 |
| FormComponent | FormComponent | 是 | 表单控件，支持的控件请参考[FormComponent参数说明](0474-oa-formcomponent-message.md#900adc515fxr6)，单一表单最大组件个数不超过200。 |
| processFeatureConfig | Object | 否 | 流程中心集成配置。 |
| features | Array | 否 | 配置列表。 |
| name | String | 否 | 支持三方进行自定义配置的功能模块名称，本接口当前支持：   - **TASK\_EXECUTE**：任务执行模块，即详情页的同意、拒绝按钮 - **SYNC\_BOXSTER**：任务同步待办方式 - **CUSTOM\_SHORTCUT**：待办、卡片通知中的快捷操作按钮 - **CUSTOM\_ACTION\_DEFINITION**：以审批页面托管模式集成时使用，表示获取操作区（按钮）数据的回调地址（按钮渲染） - **CUSTOM\_ACTION\_APPLY**：以审批页面托管模式集成时使用，表示进行审批操作时回调的回调地址（操作审批） |
| pcUrl | String | 否 | 三方自定义的pc端跳转链接。 |
| mobileUrl | String | 否 | 三方自定义的手机端跳转链接。 |
| runType | String | 否 | 运行方式。 当features.name为`TASK_EXECUTE`时，支持   - **ORIGIN**：原生运行，即在官方审批内运行对应功能，将会回调callback中配置的回调接口 - **REDIRECT**：外部跳转运行，需要跳转到三方地址运行对应功能，将会跳转到pcUrl、mobileUrl中配置的地址   当features.name为`SYNC_BOXSTER`时，支持   - **DEFAULT**：默认将审批任务同步待办 - **OUTBIZ\_CUSTOM**：不同步待办，由业务自定义实现   当features.name为`CUSTOM_SHORTCUT`时，支持   - **REDIRECT**：外部跳转运行，打开待办详情页时，将会跳转到三方业务系统详情页地址。在待办列表执行同意/拒绝快捷审批操作时，将会回调callback中配置的回调接口。   当features.name为`AFFILIATION_DIR`时，支持   - **OUTBIZ\_CUSTOM**：指定待办分组，由业务自定义指定待办归属的分类信息   当features.name为`CUSTOM_ACTION_DEFINITION`时，支持   - **OUTBIZ\_CUSTOM**：审批页面托管模式集成时使用，表示在审批详情页获取操作区（按钮）数据的回调地址（按钮渲染），将会回调callback中配置的回调接口。   当features.name为`CUSTOM_ACTION_APPLY`时，支持   - **OUTBIZ\_CUSTOM**：审批页面托管模式集成时使用，表示在审批详情页进行审批操作时回调的回调地址（操作审批），将会回调callback中配置的回调接口。 |
| callback | Object | 否 | 网关回调配置，当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。  网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)。 |
| appUuid | String | 否 | 网关appUuid，当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。  传[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时所属企业corpId值。 |
| apiKey | String | 否 | 网关apiKey，当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。通过[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)内容获取`apiKey`。       - 在网关回调外部接口时，钉钉侧会根据不同业务场景，回传一些业务处理所需的参数给到ISV，ISV在收到回调请求后，若需要解析获取对应参数信息，需要在[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时配置对应的参数key。   例如，TASK\_EXECUTE任务执行模块，即详情页的同意、拒绝按钮配置回调时，钉钉侧回传的固定参数如下：`{"outResult":"agree","processInstanceId":"xxx","activityId":"xxx","corpId":"dingxxx","data":[],"remark":"同意","title":"xxx提交的资产领用申请","taskId":111,"operator":"manager0001"}`。 - ISV在创建数据源时，对应的参数配置需按业务需要填对应的key进行解析：outResult,processInstanceId,activityId,corpId,remark,title,taskId,operator |
| version | String | 否 | 网关接口版本       - 当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。 - 默认传1。 |
| templateConfig | Object | 否 | 流程中心模板配置。 |
| hidden | Boolean | 否 | 是否为隐藏模板：   - **true**：是隐藏模板 - **false**：不是隐藏模板 |
| createInstanceMobileUrl | String | 否 | 表单创建移动端地址。 |
| createInstancePcUrl | String | 否 | 表单创建PC端地址。 |
| templateEditUrl | String | 否 | 模板编辑地址。 |
| disableSendCard | Boolean | 否 | 创建流程中心待处理任务时是否禁用消息卡片通知：   - **true**：禁用，将不发送消息卡片通知 - **false**：默认值，不禁用，将发送消息卡片通知 |

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 表单模板信息。 |
| processCode | String | 保存或更新的表单code。 |

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
| 400 | formschema.error | 流程条件分支中已使用的表单控件不可修改或删除 | 流程条件分支中使用的表单控件的类型不可修改或删除 |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | processcode.error | processCode对应的审批流程不存在 | processCode对应的审批流程不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | parameter.error | 流程中心配置参数错误：%s | 流程中心配置参数错误 |
| 400 | processes.error | 获取模板列表失败 | 获取模板列表失败 |
| 400 | processes.error | 审批流已超过最大数量 | 审批流已超过最大数量 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | internalError | %s | 系统内部错误 |
| 400 | system.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | aflowProcessSetupNoPermission | 无操作审批流的权限，请检查processCode是否正确 | 无操作审批流的权限，请检查processCode是否正确 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 500 | system.error | 系统错误 | 系统错误 |
