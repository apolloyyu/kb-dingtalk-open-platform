# 设置权限继承模式

doc_id: 4SBiv7k5J6
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v2.0/storage/spaces/dentries/{dentryUuid}/permissions/inheritances
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.Permission.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过调用获取企业内部应用的accessToken接口获取。

## Path params
- dentryUuid (String, required): 文件uuid，可调用搜索文件或获取 dentryUuid 信息接口，获取返回参数`dentryUuid`字段。

## Query params
- unionId (String, required): 用户的unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- inheritance (String, required): 权限继承模式，枚举值： - **PASS_ON**：传递，当前文件(夹)会继承所有父节点的权限，然后结合当前文件(夹)上的权限，相同成员权限取最大。 - **BREAK**: 打断，权限的传递在当前节点做一个打断。 - 不支持OWNER和MANAGER的打断 - 默认权限继承模式

## Returns
- optional: success(Boolean)

## Limits
- 权限继承模式，枚举值： - **PASS_ON**：传递，当前文件(夹)会继承所有父节点的权限，然后结合当前文件(夹)上的权限，相同成员权限取最大。 - **BREAK**: 打断，权限的传递在当前节点做一个打断。 - 不支持OWNER和MANAGER的打断 - 默认权限继承模式

source_url: https://open.dingtalk.com/document/development/set-permission-inheritance-mode
updated_at: 2026-06-08 11:40:28
