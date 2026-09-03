# 创建联系人数据

doc_id: zj5fR1PTqZ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/contact/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- instance (ObjectDataInstanceVo, required): 联系人数据。
- creator_userid (String, required): 记录创建人的userId。
- data (String, required): 联系人数据内容，JSON格式字符串。传参格式详见新增和更新联系人字段格式说明V1。
- optional: extend_data(String), provider_corpid(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), result(ObjectDataCreateDto), instance_id(String), contact_unionid(String), contact_userid(String)

## Limits
- - 一个客户下最多存在30个联系人。
- - 同一个手机号最多存在5个联系人。

source_url: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-create-crm-contact-data
updated_at: 2026-08-28 10:26:48
