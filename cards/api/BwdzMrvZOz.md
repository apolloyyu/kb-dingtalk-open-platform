# 企业活跃用户统计列表（部门维度）

doc_id: BwdzMrvZOz
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/kac/datav/dept/dau/list
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- request (Object, required): 请求对象。
- data_id (String, required): 日期标识。 例如：20220101。
- size (Number, required): 每页最大条目数，最大值100。
- cursor (Number, required): 分页游标。 - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上传调用返回的next_cursor。
- optional: deptId(String), superDeptId(String)

## Returns
- optional: errcode(Number), errmsg(String), result(Object), data(Object[]), daily_active_users(Number), dept_id(Number), dept_name(String), contacts_number(Number), pc_active_users(Number), app_active_users(Number), has_more(Boolean), next_cursor(Number)

## Limits
- 每页最大条目数，最大值100。
- > 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的数据资产类OpenAPI接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过钉钉数据资产平台获取相应的数据服务。

source_url: https://open.dingtalk.com/document/development/query-the-statistics-of-active-users-in-a-department-of
updated_at: 2026-08-27 14:07:43
