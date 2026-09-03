# 静态推荐数据同步

doc_id: ciNsLY8Ipt
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/recommend/create
api_version: v1-oapi
app_types: 第三方企业应用
permissions: edu_study_log_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- thumbnail (String, required): 缩略图url地址。
- type (String, required): 类型。 - **1**：词汇 - **2**：课文 - **3**：题目 - **4**：考试 - **5**：知识点 - **6**：课程 - **7**：其他
- title (String, required): 内容标题。
- userid (String, required): 当前用户的userId。
- period_code (String, required): 学段编码，可通过获取学段元数据列表接口获取period_code参数值。
- return_url (String, required): 回跳地址。
- out_content_id (String, required): ISV侧内容唯一ID。 **[!NOTE]** 由ISV回传得到。
- optional: summary(String), class_id(Number), subject_code(String), textbook_code(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/statically-recommended-data-synchronization
updated_at: 2026-06-08 09:48:00
