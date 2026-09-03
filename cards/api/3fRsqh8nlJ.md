# 生产单

doc_id: 3fRsqh8nlJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/productions
api_version: v2-new
app_types: 第三方企业应用
permissions: Jzcrm.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- datatype (Long, required): 数据类型，固定值**156**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- sch_title (String, required): 主题。
- sch_number (String, required): 单号。
- sch_starttime (String, required): 开始日期。
- sch_planendtime (String, required): 计划完成时间。
- optional: msgid(Long), data(Object), sch_customerid(String), sch_htid(String), sch_endtime(String), sch_principal(String), sch_makeemp(String), sch_remark(String), sch_statesstr(String), sch_finished(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-a-production-order
updated_at: 2026-06-04 19:10:51
