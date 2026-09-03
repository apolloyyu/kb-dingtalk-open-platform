# 出库单

doc_id: EuF996fVML
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/outstocks
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
- datatype (Long, required): 数据类型，固定值**191**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- libiodate (String, required): 出库日期。
- stocklibid (String, required): 出库仓库。
- libiostate (String, required): 出库状态。
- billno (String, required): 出库单号。
- empid (String, required): 经办人。
- child_mx (String, required): 产品明细，json格式。
- optional: msgid(Long), data(Object), customerid(String), inorout(String), libioname(String), orderid(String), askempid(String), remark(String), auditreson(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-an-issue-ticket
updated_at: 2026-06-02 20:01:04
