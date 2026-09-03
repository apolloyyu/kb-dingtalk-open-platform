# 获取个人或部门钉钉运动数据

doc_id: BfmmburMWs
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/health/stepinfo/list
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- type (Number, required): 获取数据类型。 - **0**：获取用户步数 - **1**：获取部门步数
- object_id (String, required): 查询的用户userId或部门ID。 - 当type为1，输入部门ID - 当type为0，输入userId
- stat_dates (String, required): 时间列表，时间格式是YYYYMMDD，多个日期之间使用英文逗号分割。 **[!NOTE]** 最多可以查询31天的数据。

## Returns
- optional: errcode(Number), request_id(String), stepinfo_list(BasicStepInfoVo[]), stat_date(Number), step_count(Number)

## Limits
- 时间列表，时间格式是YYYYMMDD，多个日期之间使用英文逗号分割。 **[!NOTE]** 最多可以查询31天的数据。
- 调用本接口，查询用户个人或企业部门每天的钉钉运动步数，最多可以查询31天的数据。
- > 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的数据资产类OpenAPI接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过钉钉数据资产平台获取相应的数据服务。

source_url: https://open.dingtalk.com/document/development/queries-individual-or-department-dingtalk-exercise-steps
updated_at: 2026-08-27 14:07:36
