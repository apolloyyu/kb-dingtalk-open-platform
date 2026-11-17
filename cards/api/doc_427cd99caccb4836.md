# 创建看鉴任务

doc_id: doc_427cd99caccb4836
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/bv/kanjian/tasks
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.KanJian.Task.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- description (String, required): 任务描述，作为任务指令。
- executorUserIds (Array of String, required): 执行者。
- operatorUserId (String, required): 操作人 userId，作为任务创建人。
- adminUserIds (Array of String, required): 管理员userId。
- optional: subTasks(Array), instruction(String), name(String), taskId(String), reportContent(String)

## Returns
- optional: result(Object), taskId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createkanjiantask
updated_at: 2026-11-17 17:35:15
