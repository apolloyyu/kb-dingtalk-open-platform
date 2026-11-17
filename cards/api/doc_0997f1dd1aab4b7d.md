# 分页查询看鉴 BV 设备列表

doc_id: doc_0997f1dd1aab4b7d
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/bv/kanjian/devices
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.KanJian.Device.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: cursor(String), pageSize(Long)

## Body
- none

## Returns
- optional: result(Object), hasMore(Boolean), items(Array), bindUserId(String), deviceName(String), deviceSn(String), nextCursor(String)

## Limits
- 每页条数，默认10条，最小为1，最大为50。

source_url: https://open.dingtalk.com/document/development/api-listkanjiandevices
updated_at: 2026-11-17 17:35:22
