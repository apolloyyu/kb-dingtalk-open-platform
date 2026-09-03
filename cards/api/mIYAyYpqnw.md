# 创建园区项目

doc_id: mIYAyYpqnw
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/industry/campuses/projects
api_version: v2-new
app_types: 第三方企业应用
permissions: Industry.Campus.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- campusName (String, required): 园区项目的名称。
- creatorUnionId (String, required): 创建人的unionId，可调用查询用户详情接口获取。
- optional: belongProjectGroupId(Long), telephone(String), description(String), area(double), country(String), provId(Integer), cityId(Integer), countyId(Integer), address(String), capacity(Integer), orderStartTime(Long), orderEndTime(Long), orderInfo(String), extend(String), location(String)

## Returns
- optional: campusCorpId(String), campusDeptId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-campus-project
updated_at: 2026-06-03 09:07:34
