# 获取数字化证书

doc_id: v1kWWoqBMK
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/cert/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_edu_digital_cert_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 学校老师的userId，可调用获取人员列表接口获取userid参数值。

## Returns
- optional: result(OpenQueryCertResponse), current_cert_level(Number), cert_datas(Certdata[]), cert_status(Number), can_cert(Boolean), cert_level(Number), practical_task_data(OpenPracticalTaskData[]), finish(Boolean), task_code(String), errcode(Number), errmsg(String), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-digital-certificate
updated_at: 2026-06-08 09:48:24
