# 获取数据表单schema

doc_id: iNfpZrGv9d
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/dataForms/schema/formCodes
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- processCode (String, required): 数据表单模板ID。 通过OA审批概述-名词解释获取。
- optional: appUuid(String)

## Body
- none

## Returns
- optional: result(Object), creatorUserId(String), formCode(String), name(String), memo(String), schemaContent(Object), title(String), icon(String), items(Array), componentName(String), props(Object), id(String), tableViewMode(String), label(String), bizAlias(String), required(Boolean), placeholder(String), options(Array of String), appId(Long), durationLabel(String), pushToCalendar(Integer), align(String), statField(Array), upper(Boolean), unit(String), hideLabel(Boolean), objOptions(Array), value(String), format(String), pushToAttendance(Boolean), labelEditableFreeze(Boolean), push(Object), pushSwitch(Integer), pushTag(String), attendanceRule(Integer), commonBizType(String), requiredEditableFreeze(Boolean), extract(Boolean), link(String), payEnable(Boolean), hidden(Boolean), bizType(String), staffStatusEnabled(Boolean), actionName(String), attendTypeLabel(String), childFieldVisible(Map<String, Boolean>), notPrint(String), verticalPrint(Boolean), duration(Boolean), holidayOptions(Array of Object), useCalendar(Boolean), hiddenInApprovalDetail(Boolean), disabled(Boolean), asyncCondition(Boolean), behaviorLinkage(Array), targets(Array), fieldId(String), behavior(String), showAttendOptions(Boolean), notUpper(String), fieldsInfo(String), eSign(Boolean), mainTitle(String), formula(String), choice(Integer), children(Array), appType(Integer), status(String), gmtCreate(String), gmtModified(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumgetformschema
updated_at: 2026-06-03 10:13:03
