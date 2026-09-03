# 获取表单 schema

doc_id: 0FcWJCMDIi
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/forms/schemas/processCodes
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- processCode (String, required): 表单的唯一码，，调用创建或更新审批表单模板接口或OA审批概述-名词解释获取。
- optional: appUuid(String)

## Body
- none

## Returns
- optional: result(Object), creatorUserId(String), appUuid(String), formCode(String), formUuid(String), name(String), memo(String), ownerIdType(String), schemaContent(Object), title(String), icon(String), items(Array), componentName(String), props(Object), id(String), tableViewMode(String), label(String), bizAlias(String), required(Boolean), placeholder(String), options(Array of String), appId(Long), durationLabel(String), pushToCalendar(Integer), align(String), statField(Array), upper(Boolean), unit(String), hideLabel(Boolean), objOptions(Array), value(String), format(String), pushToAttendance(Boolean), labelEditableFreeze(Boolean), push(Object), pushSwitch(Integer), pushTag(String), attendanceRule(Integer), commonBizType(String), requiredEditableFreeze(Boolean), extract(Boolean), link(String), payEnable(Boolean), hidden(Boolean), bizType(String), staffStatusEnabled(Boolean), actionName(String), attendTypeLabel(String), childFieldVisible(Map<String, Boolean>), notPrint(String), verticalPrint(Boolean), duration(Boolean), holidayOptions(Array of Object), useCalendar(Boolean), hiddenInApprovalDetail(Boolean), disabled(Boolean), asyncCondition(Boolean), behaviorLinkage(Array), targets(Array), fieldId(String), behavior(String), showAttendOptions(Boolean), notUpper(String), fieldsInfo(String), eSign(Boolean), mainTitle(String), formula(String), choice(Integer), children(Array), appType(Integer), engineType(Integer), status(String), listOrder(Integer), customSetting(String), procType(String), visibleRange(String), gmtCreate(String), gmtModified(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-form-schema
updated_at: 2026-06-03 10:12:21
