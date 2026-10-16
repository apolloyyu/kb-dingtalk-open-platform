# 智能人事花名册管理：员工信息获取与补全

doc_id: jLES1yAEEK
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- none

## Limits
- - **信息缺失难发现：** HR需在管理后台逐人打开花名册检查民族、籍贯等字段是否填写，300人逐一排查耗时3天，仍有约8%的缺失记录被遗漏。
- - **补录易出错：** 民族字段为下拉选择型，HR手动输入时频繁出现"汉族"写成"汉"、编码与名称不对应等错误，年审时被退回修改2次。
- - **跨系统不同步：** 花名册补全后需手动导出再导入OA系统，因格式差异导致15条记录丢失，二次核对又耗费1天。
- - **花名册信息一键获取：** 300人员工花名册字段信息通过API批量查询，排查时间从3天缩短至5分钟，效率提升99%。
- - **字段标准不统一：** 不同时期入职的律师花名册中民族字段填写格式不一（有的填"汉族"、有的填"1"、有的留空），行政人员需逐条人工校对，季度上报前耗费2天整理。
- - **历史数据纠错困难：** 已提交的错误数据无法追溯原始值，只能联系律师本人确认后再手动修改，沟通成本高且响应慢。
- - **员工档案实时查询：** 入职即触发花名册完整性检查，缺失字段当场识别并提示补全，季度上报前整理时间从2天缩短至30分钟。
- - **信息更新即时生效：** 补全操作通过API实时写入花名册，无需导出导入，数据同步延迟从1天降为零。

source_url: https://open.dingtalk.com/document/development/realize-automatic-push-of-employee-birthday-wishes-information
updated_at: 2026-10-16 09:23:15
