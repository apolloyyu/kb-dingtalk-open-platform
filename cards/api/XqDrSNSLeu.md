# 常见问题

doc_id: XqDrSNSLeu
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks
api_version: v2-new
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
- 高亮块的`children`只能是`BlockElement`数组。调用插入块元素接口时，在`children`中传入子段落：
- 不同类型块元素的`children`类型不同：段落块的`children`只能是行内元素；高亮块的`children`只能是块元素。
- `columns`的`children`只能是 **BlockElement 数组**，不能是行内元素。
- > 首次调用可能需要在应用中申请「通讯录」相关权限。获取到 `operatorId` 后建议将其保存下来（如配置为环境变量），避免每次都通过接口获取。
- AccessToken 的有效期为 **7200 秒（2 小时）**。过期后需要重新调用 获取企业内部应用的accessToken接口获取新的 Token。
- - 在 Token 过期前 5 分钟主动刷新；
- - **超时处理**：网络请求设置合理的超时时间（建议 30 秒），超时后进行重试。

source_url: https://open.dingtalk.com/document/development/documentation-faq
updated_at: 2026-11-11 17:26:43
