# 工作通知消息管理：发送、查询与撤回开发实践

doc_id: uykrgz2Wnq
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2
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
- - **阅读状态黑盒**： 无法得知哪些员工已读、哪些未读，催办只能盲目群发提醒，已读员工被重复打扰产生反感情绪。
- - **状态无法追踪：** 邮件发送后无法确认员工是否阅读，HR需逐一电话确认，3000人/年的确认工作量耗费2名专职人力。
- - **指令传达不及时：** 通过微信群或邮件下发运营指令，部分店长未及时查看导致活动上线延迟，月度平均延误3.2天，直接影响促销效果。
- - **执行进度不可视：** 总部无法确认各门店是否已接收并执行指令，需逐店电话核实，500家门店的核实周期长达2天，管理盲区大。
- - **运营指令秒级下达：** 促销指令通过钉钉工作通知直达店长手机端，活动上线延迟从3.2天缩短至当天，执行及时率提升至98%。
- - **500店执行可视化：** 总部实时掌握所有门店的阅读和执行状态，未读门店自动标记提醒，核实周期从2天缩短至实时。
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

source_url: https://open.dingtalk.com/document/development/work-notice-option
updated_at: 2026-10-16 09:23:11
