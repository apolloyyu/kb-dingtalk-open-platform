# 清空回收站

doc_id: Fjypn0se7Q
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/recycleBins/{recycleBinId}/clear
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
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/empty-the-recycle-bin
updated_at: 2026-06-04 19:09:46
