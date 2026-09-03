# 更新联系人数据

doc_id: eF5DC1oGaf
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectdata/contact/update
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
- data (String, required): 联系人数据内容，JSON格式字符串。传参格式详见新增和更新联系人字段格式说明V1。
- instance_id (String, required): 联系人数据ID，可通过根据指定条件查询联系人数据接口获取。
- modifier_userid (String, required): 钉钉用户userId。
- optional: extend_data(String)

## Returns
- optional: result(ObjectDataCreateDto), instance_id(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- - 一个客户下最多存在30个联系人。
- - 同一个手机号最多存在5个联系人。

source_url: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-update-crm-contact-data
updated_at: 2026-08-28 10:26:51
