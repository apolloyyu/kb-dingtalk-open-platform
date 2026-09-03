# 添加权限

doc_id: 9tMIdlAdNV
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/storage/spaces/dentries/{dentryUuid}/permissions
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.Permission.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- dentryUuid (String, required): 文件uuid：可调用搜索文件接口或获取dentryUuid信息接口，获取返回参数`dentryUuid`字段。

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- roleId (String, required): 角色id，枚举值： - **OWNER**：拥有者，具有以下权限点： - PermissionPrivilegeEnum.INFO - PermissionPrivilegeEnum.LIST - PermissionPrivilegeEnum.PREVIEW - PermissionPrivilegeEnum.READ - PermissionPrivilegeEnum.WRITE - PermissionPrivilegeEnum.DOWNLOAD - PermissionPrivilegeEnum.ADD -
- members (Array, required): 权限成员列表，最多30个。
- type (String, required): 权限成员类型，枚举值： - **ORG**：企业 - **DEPT**：部门 - **TAG**：自定义tag - **CONVERSATION**：会话 - **USER**：用户 - **DYNAMIC_GROUP**：动态用户组
- id (String, required): 权限成员id： - `type=ORG`时，id为企业ID - `type=DEPT`时，id为部门ID - `type=TAG`时，id为标签ID - `type=CONVERSATION`时，id为会话ID - `type=USER`时，id为员工userId - `type=DYNAMIC_GROUP`时，id为动态用户组groupCode
- optional: corpId(String), name(String), option(Object), duration(Long)

## Returns
- optional: success(Boolean)

## Limits
- 权限成员列表，最多30个。
- 有效时间（秒）。 - 目前仅OwnerType为APP的Space支持临时权限。 - 最大值3600。

source_url: https://open.dingtalk.com/document/development/add-permissions-file
updated_at: 2026-07-08 14:38:35
