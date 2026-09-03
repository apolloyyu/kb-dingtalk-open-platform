# 学习推荐数据回流

doc_id: Bcs2VKxort
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/recommend/return
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
- result_value (String, required): 结果分值。
- thumbnail (String, required): 媒体缩略图链接。
- type (String, required): 类型。 - **1**：词汇 - **2**：课文 - **3**：题目 - **4**：考试 - **5**：知识点 - **6**：课程 - **7**：其他
- title (String, required): 内容标题。
- userid (String, required): 学习孩子的userId。
- return_url (String, required): 回跳地址。
- result_type (Number, required): 结果分值类型。 - **1**：对错 - **2**：百分打分 - **3**：百分比打分 - **4**：数值
- out_content_id (String, required): ISV侧内容唯一ID。 **[!NOTE]** 由ISV回传得到。
- out_tx_id (String, required): 外部提交唯一ID。 **[!NOTE]** 由ISV回传得到。
- optional: summary(String), class_id(Number), subject_code(String), textbook_code(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/learn-to-recommend-data-backflow
updated_at: 2026-06-08 09:47:58
