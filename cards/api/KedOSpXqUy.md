# 保存人员扩展属性

doc_id: KedOSpXqUy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/industry/medicals/users/{userId}/extends
api_version: v2-new
app_types: 企业内部应用
permissions: Medical.ContactExt.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- userId (String, required): 发起请求的用户的userid。

## Query params
- userExtendKey (String, required): 用户拓展字段key，最大长度32字符。 - **Job**：职称。 - **UserProb**：属性。
- userExtendValue (String, required): 用户扩展字段value，最大长度128字符。 - 当**userExtendKey**取值为**Job**时，**userExtendValue**取值为： - **1**：主任医师。 - **2**：副主任医师。 - **3**：主治医师。 - **4**：住院医师。 - **5**：尚未考医师职称。 - **6**：主任药师。 - **7**：副主任药师。 - **8**：主管药师。 - **9**：药师。 - **10**：药士。 - **11**：主任护师。 - **12**：副主任护师。 - **13**
- optional: userDisplayName(String)

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- 用户拓展字段key，最大长度32字符。 - **Job**：职称。 - **UserProb**：属性。
- 用户扩展字段value，最大长度128字符。 - 当**userExtendKey**取值为**Job**时，**userExtendValue**取值为： - **1**：主任医师。 - **2**：副主任医师。 - **3**：主治医师。 - **4**：住院医师。 - **5**：尚未考医师职称。 - **6**：主任药师。 - **7**：副主任药师。 - **8**：主管药师。 - **9**：药师。 - **10**：药士。 - **11**：主任护师。 - **
- 字段展示名称最大长度256字符。

source_url: https://open.dingtalk.com/document/development/personnel-extension-property-error
updated_at: 2026-06-04 19:11:18
