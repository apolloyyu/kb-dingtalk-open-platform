# 获取年报数据

doc_id: dnZKannTqH
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/kac/datav/annual_report/get
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
- year (String, required): 年份标识。
- type (Number, required): 年报的数据维度。 - **1**：企业维度 - **2**：部门维度 - **3**：员工维度 **[!NOTE]** 员工维度的数据需要额外授权，请联系对接BD。
- optional: user_id(String), dept_id(Number)

## Returns
- optional: result(Object), isw_msg_click_cnt_1y(String), max_step_count_1y(Number), min_process_duration_1y(String), send_calendar_user_cnt_1y(Number), join_calendar_user_cnt_1y(Number), create_process_cnt_1y(Number), use_smartwork_cnt_1y(Number), send_ding_cnt_1y(Number), recv_ding_cnt_1y(Number), new_group_cnt_1y(Number), join_calendar_cnt_1y(Number), act_usr_days_1y(Number), send_group_file_message_cnt_1y(Number), send_ding_user_cnt_1y(Number), send_group_msg_user_cnt_1y(Number), join_group_cnt_1y(Number), avg_process_duration_1y(String), send_report_user_cnt_1y(Number), start_succ_video_conf_len_1y(Number), create_doc_cnt_1y(Number), send_message_group_cnt_1y(Number), create_smartwork_cnt_1y(Number), send_calendar_cnt_1y(Number), at_me_msg_cnt_1y(Number), send_report_cnt_1y(Number), corp_app_process_inst_cnt_1y(Number), send_group_msg_cnt_1y(Number), use_doc_user_cnt_1y(Number), join_succ_voip_conf_user_cnt_1y(Number), join_succ_video_conf_user_cnt_1y(Number), outside_days_1y(Number), inner_group_cnt_1y(Number), process_inst_operate_cnt_1y(Number), process_inst_submit_cnt_1y(Number), at_check_days_1y(Number), live_join_succ_time_len_1y(String), live_join_succ_cnt_1y(Number), join_succ_voip_conf_len_1y(String), join_succ_voip_conf_num_1y(Number), join_succ_video_conf_len_1y(String), join_succ_video_conf_num_1y(Number), use_micro_app_cnt_1y(Number), general_form_user_cnt_1y(Number), use_micro_user_cnt_1y(Number), errmsg(String), errcode(Number), request_id(String)

## Limits
- > 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的数据资产类OpenAPI接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过钉钉数据资产平台获取相应的数据服务。
- > 日常查询只能查询上一个年度已经生产的数据，数据不会动态更新。

source_url: https://open.dingtalk.com/document/development/obtain-annual-report-data
updated_at: 2026-08-27 14:09:17
