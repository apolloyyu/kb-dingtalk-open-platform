# 获取防截屏操作记录

doc_id: vUEgWYqwPO
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/enterpriseSecurities/userBehaviors/screenshots/query
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.ScreenShot.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- type (Integer, required): 用户行为： - **0**：全部 - **1**：截屏 - **2**：录屏
- platform (Integer, required): 端类型： - **0**：全部 - **1**：iOS - **2**：Android - **3**：Mac - **4**：Windows
- pageSize (Integer, required): 分页大小。 最大值100。
- pageNumber (Long, required): 起始页。 默认从1开始。
- optional: startTime(Long), endTime(Long), userId(String)

## Returns
- optional: data(Array), userName(String), time(Long), type(Integer), pictureUrl(String), platform(Integer), scene(String), userId(String), totalCnt(Integer), dataCnt(Integer)

## Limits
- 开始时间，时间戳，单位毫秒。 默认当前时间前7天。
- 分页大小。 最大值100。
- > 如果用户是普通账号且没有签署协议，则只能获取用户操作行为，不能获取图片的url。

source_url: https://open.dingtalk.com/document/development/obtain-anti-screen-capture-operation-records
updated_at: 2026-06-04 19:10:01
