# 删除看鉴任务

doc_id: doc_8bdd9290df024b5f
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/dvi/bv/kanjian/tasks
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.KanJian.Task.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- taskId (String, required): 主任务 ID，可通过分页查询看鉴任务列表接口获取。
- operatorUserId (String, required): 操作人 userId。

## Body
- none

## Returns
- optional: result(Object), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-deletekanjiantask
updated_at: 2026-11-17 17:35:16
