# 获取企业内部应用的access_token

doc_id: FRuKfO9tOP
completeness: full
archived: true
method: GET
endpoint: https://oapi.dingtalk.com/gettoken
api_version: v1-oapi
app_types: 企业内部应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- appkey (String, required): 已创建的企业内部应用的 Client ID，获取方式可参考Client ID/Client Secret文档说明。
- appsecret (String, required): 已创建的企业内部应用的 Client Secre ，获取方式可参考Client ID/Client Secret文档说明。

## Body
- none

## Returns
- optional: access_token(String), expires_in(Number), errmsg(String), errcode(Number)

## Limits
- 生成的access_token。 **[!NOTE]** 在使用access_token时，请注意： - access_token的有效期为7200秒（2小时），有效期内重复获取会返回相同结果并自动续期，过期后获取会返回新的access_token。 - 开发者需要缓存access_token，用于后续接口的调用。因为每个应用的access_token是彼此独立的，所以进行缓存时需要区分应用来进行存储。 - 不能频繁调用gettoken接口，否则会受到频率拦截。

source_url: https://open.dingtalk.com/document/development/obtain-orgapp-token
updated_at: 2026-08-25 09:36:29
