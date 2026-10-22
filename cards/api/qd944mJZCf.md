# 联系人管理：个人与企业的联系人全生命周期管理

doc_id: qd944mJZCf
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectmeta/contact/describe
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- none

## Limits
- - 百人名单逐条录入耗时3～4小时，严重影响活动后的黄金跟进窗口。
- - **批量导入提效**：通过批量新增接口一次性导入活动收集的数百条联系人数据，将录入时间从半天缩短至5分钟以内，确保销售团队在活动当天即可启动跟进。
- - 沉睡会员（超过12个月无互动）占比达30%以上，影响系统性能和营销精准度。
- - 手动逐条核对更新效率低，一个运营人员一天最多处理200条记录。
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - `relationList`：联系人数据列表，最大值10。
- - `maxResults`：分页大小，最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/crm-contact-data-operation-process
updated_at: 2026-10-22 17:12:12
