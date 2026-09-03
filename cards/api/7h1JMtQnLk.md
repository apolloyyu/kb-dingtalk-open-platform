# 大模型推理服务（文生文模型）

doc_id: 7h1JMtQnLk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/aiPaaS/ai/complete
api_version: v2-new
app_types: 第三方企业应用
permissions: AIPaaS.Model.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- model (String, required): 模型名称： - `qwen-plus` - `qwq-plus` - `qwen3-235b`
- messages (Array, required): 消息数组信息。
- role (String, required): 角色信息： - system：系统参数 - user：用户参数
- content (String, required): prompt 信息。
- optional: temperature(double), top_p(double), max_tokens(Integer), enable_search(Boolean), stream(Boolean)

## Returns
- optional: created(Long), model(String), id(String), choices(Array), finishReason(String), message(Object), role(String), content(String), reasoning_content(String), usage(Object), total_tokens(Integer), prompt_tokens(Integer), completion_tokens(Integer)

## Limits
- 请求返回的最大 Token 数， `max_tokens` 的设置不会影响大模型的生成过程，但如果模型生成的 Token 数超过了设定的 `max_tokens`，本次请求将返回截断后的内容。 **[!NOTE]** - **默认值**: 模型的最大输出长度 - **最大值**: 模型的最大输出长度 - 请根据具体需求合理设置 `max_tokens` 的值，以达到预期效果。

source_url: https://open.dingtalk.com/document/development/api-exclusivemodelcompleteservice
updated_at: 2026-06-03 09:16:29
