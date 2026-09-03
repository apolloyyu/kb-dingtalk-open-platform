# 预览审批流程

doc_id: ITfMvR6egr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/processes/preview
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- appType (String, required): 应用编码。
- systemToken (String, required): 应用密钥，在应用数据中获取。 <props="intl">只发布虚商站
- userId (String, required): 用户的userid。
- formUuid (String, required): 表单ID。
- formDataJson (String, required): 表单数据，示例：`"{\"textField_jcpm6agt\": \"单行\",\"employeeField_jcos0sar\": [\"workno\"]}"` - key：流程组件标识，宜搭表单编辑页面，高级设置中查看。 - value：流程组件内的值。
- optional: language(String), processCode(String), departmentId(String)

## Returns
- optional: result(Array), processInstanceId(String), showName(String), operatorNickName(String), activeTimeGMT(String), operateTimeGMT(String), operateType(String), operatorStatus(String), remark(String), taskHoldTimeGMT(Long), type(String), operatorName(String), operatorUserId(String), activityId(String), taskType(String), taskExecuteType(String), size(Integer), operatorDisplayName(String), files(String), action(String), actionExit(String), dataId(Long), taskId(String), digitalSign(String), operatorPhotoUrl(String), domains(Array of Any)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-previewpublishedprocess
updated_at: 2026-06-02 09:41:49
