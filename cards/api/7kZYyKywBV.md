# 更新目标规则下的考核任务

doc_id: 7kZYyKywBV
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/agoal/perfTasks
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Entity.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: PerfTask(PerfTask)

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalperftaskupdate
updated_at: 2026-06-15 10:41:01
