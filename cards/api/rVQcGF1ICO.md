# 获取企业内部网页应用列表

doc_id: rVQcGF1ICO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/innerWebApps
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_get_microapp_list

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: app_type(String), offset(Integer), size(Integer)

## Body
- none

## Returns
- optional: appList(Array), agentId(Long), name(String), desc(String), icon(String), homepageLink(String), pcHomepageLink(String), ompLink(String), appId(Long), appStatus(Integer), developType(Integer), robotInfo(Object), robotCode(String), coolAppInfo(Array), coolAppCode(String), unifiedAppId(String)

## Limits
- 本次最多返回的应用数量，取值范围为 `1`～`1000`。 **[!NOTE]** - 传入 `offset` 或 `size` 任意一个参数时启用分页，未传 `size` 时按 `100` 处理。 - 两个参数均不传时返回全部符合条件的应用。
- - `offset` 表示跳过的符合当前筛选条件的应用数量，从 `0` 开始。`size` 表示本次最多返回数量，取值范围为 `1`～`1000`。
- - 连续分页时，保持 `app_type` 和 `size` 不变，每次将 `offset` 加上本次实际返回数量。返回数量小于 `size` 或 `appList` 为空数组时，可结束查询。

source_url: https://open.dingtalk.com/document/development/api-listinnerwebapps
updated_at: 2026-10-27 18:04:44
