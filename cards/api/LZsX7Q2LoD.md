# 创建或更新业务分组

doc_id: LZsX7Q2LoD
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processCentres/directories
api_version: v2-new
app_types: 第三方企业应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- bizGroup (String, required): 业务分组ID，调用方提供的自定义唯一分组标识。 为了保证不同三方系统同步的业务分组ID在钉钉侧唯一，钉钉侧将对业务传递的分组ID进行逻辑转换，规则如下：${应用appId} + _ + ${bizGroup}。
- operateUserId (String, required): 操作人userId。
- name (String, required): 分组名称。
- name18n (String, required): 支持国际化的分组名称，json字符串格式。
- optional: description(String)

## Returns
- optional: result(Object), dirId(String), bizGroup(String), success(Boolean)

## Limits
- - 单个组织在同一个应用内最多支持创建10个分组。

source_url: https://open.dingtalk.com/document/development/api-premiuminsertorupdatedir
updated_at: 2026-06-03 10:12:58
