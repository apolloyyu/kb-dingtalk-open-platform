# 查询设备列表

doc_id: PTEZl1JYFe
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartdevice/device/querylist
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_smart_device_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- page_query_vo (PageQueryVo, required): 列表查询对象，包含分页参数和产品标识。
- pk (String, required): 产品的唯一标识。该参数需线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。
- cursor (Number, required): 游标地址，第一页填0。
- size (Number, required): 分页大小，最大支持20条记录每页。

## Returns
- optional: result(PageResult), next_cursor(Number), has_more(Boolean), list(DeviceDetailVO[]), corp_id(String), device_mac(String), nick(String), device_id(String), device_name(String), pk(String), userid(String), ext(String), sn(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 分页大小，最大支持20条记录每页。

source_url: https://open.dingtalk.com/document/development/intelligent-hardware-list-query
updated_at: 2026-06-03 09:53:24
