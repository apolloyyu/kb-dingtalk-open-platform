# 场景群机器人消息推送：群助手自动化通知与业务提醒

doc_id: ItyRrLUMsj
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2
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
- - **业务异常告警：** 电商订单支付失败、物流延迟、库存低于阈值等异常事件需第一时间通知运营团队，传统方式依赖人工监控和转发，响应延迟高达30分钟以上。
- - **异常响应延迟：** 日均异常事件40+起（支付失败/物流停滞/差评预警），ERP系统仅记录日志无主动通知，运营人员需每2小时手动登录系统查看，平均发现延迟90分钟，错过最佳处理窗口导致客户投诉率上升15%。
- - **信息分散难协同：** 同一订单的支付、物流、客服异常分散在三套系统中，运营主管需在三个群分别转发消息才能同步信息，单次异常协调耗时15分钟，跨部门响应效率低下。
- - **秒级触达：** 异常事件从发生到群通知推送延迟从90分钟缩短至3秒，客户投诉率从15%降至2%。
- - **聚合呈现：** 三平台异常统一推送至同一场景群，运营主管无需切换系统即可掌握全局，单次异常协调耗时从15分钟降至2分钟。
- - **进度更新滞后：** 日均理赔案件60+笔，核保/赔付状态变更仅记录在CRM系统，经纪人需主动登录查询才能获知进展，平均获知延迟4小时，客户反复电话追问增加沟通成本。
- - **团队协作低效：** 一个复杂理赔案件涉及核保部、理赔部、财务部多方协作，进度信息分散在各环节负责人手中，主管需逐一电话确认才能掌握整体进度，每日浪费40分钟无效沟通。
- - **实时同步：** 理赔状态变更从系统记录到群通知推送延迟从4小时缩短至5秒，客户电话追问量下降70%。

source_url: https://open.dingtalk.com/document/development/group-assistant-sends-a-message
updated_at: 2026-10-14 09:16:58
