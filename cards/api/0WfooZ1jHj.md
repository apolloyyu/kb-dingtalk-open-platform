# 退回宜搭审批流程

doc_id: 0WfooZ1jHj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/processes/instances/restartInstance
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.Process.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- targetActivityId (String, required): 目标退回节点，通过 获取审批记录 接口获取节点ID。
- formUuid (String, required): 表单唯一编码。
- systemToken (String, required): 应用密钥，在应用数据中获取。
- procInstanceId (String, required): 实例ID。
- currentActivityId (String, required): 当前审批节点，通过 获取审批记录 接口获取节点ID。
- userId (String, required): 用户的userId。
- appType (String, required): 应用编码，获取方式如下图：
- taskId (String, required): 任务ID，通过 获取审批记录 接口获取。
- optional: remark(String), envProfile(String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-restartinstance
updated_at: 2026-06-04 19:08:58
