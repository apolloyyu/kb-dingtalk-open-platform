# 提交文件

doc_id: XazD1mswsn
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/storage/spaces/files/{parentDentryUuid}/commit
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.File.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- parentDentryUuid (String, required): 父节点dentryUuid，可调用搜索文件或获取 dentryUuid 信息接口，获取返回参数`dentryUuid`字段。 如果是空间根目录，填空间根目录的dentryUuid。

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取。

## Body
- uploadKey (String, required): 添加文件唯一标识，调用获取文件上传信息接口获取uploadKey参数值。
- name (String, required): 文件的名称，带后缀。命名有以下要求： - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、
- value (String, required): 属性值。
- visibility (String, required): 属性可见性： - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见
- optional: option(Object), size(Long), conflictStrategy(String), appProperties(Array), convertToOnlineDoc(Boolean), convertToOnlineDocTargetDocumentType(String), classificationLabelId(String)

## Returns
- optional: dentry(Object), id(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), properties(Object), readOnly(Boolean), appProperties(Map<String, Array>), value(String), visibility(String), uuid(String), partitionType(String), storageDriver(String), thumbnail(Object), width(Integer), height(Integer), url(String), category(String)

## Limits
- 当前文件的应用属性列表，最大值3。
- 属性可见性： - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见
- 属性可见性。 - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见

source_url: https://open.dingtalk.com/document/development/submittal-file
updated_at: 2026-08-19 17:20:26
