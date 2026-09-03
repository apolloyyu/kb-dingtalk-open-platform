# 创建荣誉勋章模板

doc_id: vTuBAXoHAi
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/orgCulture/honors/templates
api_version: v2-new
app_types: 第三方企业应用
permissions: OrgCulture.Honor.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 创建荣誉勋章模板的管理员所在组织的userId信息。 需要主管理员角色或者子管理员角色。
- medalName (String, required): 荣誉勋章名称。 - 最大长度10字符 。 - 不支持表情图标等。
- medalDesc (String, required): 荣誉勋章描述。 - 最大长度30字符 。 - 不支持表情图标等。
- medalMediaId (String, required): 荣誉勋章图片，可调用上传媒体文件接口获取出参`media_id`参数字段。 - 图片尺寸 900\*900，不超过1M，支持PNG 。 - 图片请使用钉钉媒体资源标识符media_id。
- avatarFrameMediaId (String, required): 头像挂件，可调用上传媒体文件接口获取出参`media_id`参数字段。 - 图片尺寸 240\*240，不超过1M，支持PNG。 - 图片请使用钉钉媒体资源标识符media_id。
- defaultBgColor (String, required): 背景颜色: - #FFFBB4 - #FFE7BC - #FFDAF4 - #DAF6A8 - #E4D7FF - #BFDFFF - #B9F2D6 仅以上颜色可选。

## Returns
- optional: success(Boolean), result(Object), honorId(String)

## Limits
- 荣誉勋章名称。 - 最大长度10字符 。 - 不支持表情图标等。
- 荣誉勋章描述。 - 最大长度30字符 。 - 不支持表情图标等。
- 荣誉勋章图片，可调用上传媒体文件接口获取出参`media_id`参数字段。 - 图片尺寸 900\*900，不超过1M，支持PNG 。 - 图片请使用钉钉媒体资源标识符media_id。
- 头像挂件，可调用上传媒体文件接口获取出参`media_id`参数字段。 - 图片尺寸 240\*240，不超过1M，支持PNG。 - 图片请使用钉钉媒体资源标识符media_id。
- > - 创建企业荣誉勋章模板，会流入钉钉后台进行审核，一般5个工作日内审核完毕。
- > - 企业每周的审核次数有限制（标准版每周10次/专业版每周20次），超过后接口会报错。如有特殊原因希望提高审核次数上限，请联系我们申请并讲明原因。
- 5. 上传素材中不得包含涉黄、涉政等违规的内容（包含但不仅限于图片、文字）。

source_url: https://open.dingtalk.com/document/development/create-medal-of-honor-template
updated_at: 2026-06-04 19:10:41
