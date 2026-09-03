# 查询园区项目信息

doc_id: NNxYjTXO4e
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/industry/campuses/projectInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: Industry.Campus.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- campusDeptId (Long, required): 园区项目的部门ID，可调用创建园区项目接口获取campusDeptId参数值。

## Body
- none

## Returns
- optional: campusName(String), campusCorpId(String), campusDeptId(Long), belongProjectGroupId(String), telephone(String), description(String), area(double), country(String), provId(Integer), cityId(Integer), countyId(Integer), address(String), location(String), capacity(String), orderStartTime(Long), orderEndTime(Long), orderInfo(String), extend(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-a-project-in-a-specified-campus
updated_at: 2026-06-04 19:11:17
