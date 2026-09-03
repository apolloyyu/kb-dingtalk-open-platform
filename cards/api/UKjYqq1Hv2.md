# 检查用户是否完成所有任务

doc_id: UKjYqq1Hv2
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/occupationauth/userTasks/check
api_version: v2-new
app_types: 第三方个人应用
permissions: DigitalManager.TaskStatus.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。

## Path params
- none

## Query params
- provinceCode (String, required): 省级任务对接入。

## Body
- none

## Returns
- optional: status(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/docking-of-provincial-practical-exercises-for-digital-managers
updated_at: 2026-06-04 19:12:04
