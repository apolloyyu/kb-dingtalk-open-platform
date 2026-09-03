# 发起宜搭审批流程

doc_id: w2yqFRi6wt
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/processes/instances/start
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Process.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户的userId，可通过获取部门用户userid列表接口获取。
- formUuid (String, required): 页面编码，获取方式可参考下图所示：
- formDataJson (String, required): 表单数据，示例： `"{\"textField_jcpm6agt\": \"单行\",\"employeeField_jcos0sar\": [\"workno\"]}"` - key：流程组件标识，宜搭表单编辑页面，高级设置中查看。 - value：流程组件内的值。
- optional: language(String), processCode(String), departmentId(String), processData(String), useAlias(Boolean)

## Returns
- optional: result(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-startinstance-v2
updated_at: 2026-06-15 10:44:16
