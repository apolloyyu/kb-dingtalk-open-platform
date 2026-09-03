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

source_url: https://open.dingtalk.com/document/development/documentation-faq
updated_at: 2026-03-31 10:01:36
