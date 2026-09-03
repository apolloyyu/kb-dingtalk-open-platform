# 更新设备绑定关系

doc_id: eKUSFjGFoY
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/devices/binding/update
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Device.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 用户userId。
- sn (String, required): 设备SN编号。
- action (String, required): 操作类型： - **bind**：绑定设备到指定的员工 - **unbind**：解绑设备
- teamCode (String, required): 团队编码。 **[!NOTE]** - 绑定场景下，必填参数 - 解绑场景下，可选 （如果一个员工身上绑定了多块设备时必选参数）

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-updatedevicebinding
updated_at: 2026-06-24 13:44:36
