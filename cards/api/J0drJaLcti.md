# 批量删除回收项

doc_id: J0drJaLcti
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/recycleBins/{recycleBinId}/recycleItems/batchRemove
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.RecycleBin.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- recycleBinId (String, required): 回收站Id，可调用获取回收站信息接口获取。

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- recycleItemIds (Array of String, required): 回收项Id列表，最大值50，调用获取回收项列表接口获取id参数值。

## Returns
- optional: success(Boolean)

## Limits
- 回收项Id列表，最大值50，调用获取回收项列表接口获取id参数值。

source_url: https://open.dingtalk.com/document/development/batch-delete-recycle-items
updated_at: 2026-06-04 19:09:45
