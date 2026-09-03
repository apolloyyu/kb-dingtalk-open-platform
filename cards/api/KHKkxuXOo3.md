# 计件报工

doc_id: KHKkxuXOo3
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/manufacturing/users/{userId}/jobs
api_version: v2-new
app_types: 第三方企业应用
permissions: Manufacture.JobBook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 员工钉钉userid。

## Query params
- none

## Body
- qualifiedQuantity (String, required): 合格数量。
- uuid (String, required): 随机字符串，唯一标识，用于幂等及更新。
- mesAppKey (String, required): **mes**系统唯一标识。
- instNo (String, required): 工单编号。
- manufactureDate (String, required): 生产日期时间，格式：`yyyy-MM-dd HH:mm:ss`。
- optional: scrappedQuantity(String), productSpecification(String), reworkableQuantity(String), userName(String), productName(String), productEnName(String), extend(String), productCode(String), processName(String), processEnName(String), dingCorpId(String), isBatchJob(String), userNameList(String), userIdList(String), unitPrice(String)

## Returns
- optional: httpCode(String), uuid(String), content(String), errorMsg(String), errorLevel(Integer), errorCode(String), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/riqing-monthly-settlement-piece-rate-reporting-interface
updated_at: 2026-06-04 19:11:18
