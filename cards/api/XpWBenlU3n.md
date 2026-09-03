# 创建钉工牌电子码

doc_id: XpWBenlU3n
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/finance/payCodes/userInstances
api_version: v2-new
app_types: 第三方企业应用
permissions: Finance.PayCode.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- requestId (String, required): 请求ID。
- codeIdentity (String, required): 码标识，取值： - **DT_VISITOR**：访客码 - **DT_CONFERENCE**：会展码
- status (String, required): 状态，传入关闭状态需要用户手动开启后才会渲染二维码。 - **OPEN**：开启 - **CLOSED**：关闭 - **INVALID**：失效
- corpId (String, required): 企业corpId。可在钉钉开发者后台首页查看。
- userCorpRelationType (String, required): 用户和企业的关系类型，用于区分内部员工，外部联系人，无关系普通用户。 - **INTERNAL_STAFF**：企业内部员工 - **EXTERNAL_CONTACT**：外部联系人 - **NO_RELATION**：普通用户与组织无关
- userIdentity (String, required): 用户身份标识。取值和userCorpRelationType参数值有关。 - 如果是企业内部用户，通过获取部门用户详情接口传用户的userId。 - 如果是外部联系人通过获取外部联系人列表接口传外部联系人的userid。 - 如果是无关系用户需传入用户手机号，手机号需带有国家码，例如86-xxxxxxxxxxx。
- gmtExpired (String, required): 临时码过期时间。 格式：yyyy-MM-dd HH:mm:ss。
- availableTimes (Array, required): 有效时间列表，对于连续时间段，只需传入一个对象即可。 过期时间必须晚于最晚结束时间。
- gmtStart (String, required): 开始时间。 格式：yyyy-MM-dd HH:mm:ss。
- gmtEnd (String, required): 结束时间。 格式：yyyy-MM-dd HH:mm:ss。
- extInfo (Map, required): 扩展参数。 以下四个字段必传： - **applicantName**：申请人名称 - **applyTime**：申请时间，格式：yyyy-MM-dd HH:mm:ss - **visitorName**：访客名称 - **visitorMobile**：访客手机号 示例： ``` { "applicantName":"xx", "applyTime":"2021-10-25 12:12:12", "visitorName":"小红", "visitorMobile":"86-12345678901" } ```
- optional: codeValue(String), codeValueType(String)

## Returns
- optional: codeId(String), codeDetailUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-user-code-instance
updated_at: 2026-06-04 19:11:55
