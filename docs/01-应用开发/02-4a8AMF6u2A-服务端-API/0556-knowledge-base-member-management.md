---
title: "知识库成员管理"
source_url: "https://open.dingtalk.com/document/development/knowledge-base-member-management"
namespace: "development"
slug: "knowledge-base-member-management"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 使用教程 > 知识库成员管理"
doc_id: "Wr4um2g2Xi"
updated_at: "2026-04-08 20:23:06"
---

> Source: https://open.dingtalk.com/document/development/knowledge-base-member-management
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 使用教程 > 知识库成员管理
> Updated: 2026-04-08 20:23:06

# 知识库成员管理

在企业知识库的日常运营中，随着团队协作需求的变化，管理员经常需要灵活调整知识库的访问权限——例如新员工入职需要加入知识库、成员角色调整、人员离职后需要撤销访问等。通过知识库成员管理接口，你可以程序化地完成这些操作，实现知识库权限的自动化管理。

## **使用场景**

通过下方的场景选择合适的流程进行接入：

- **场景一**：新员工入职、外部协作者加入、或某个部门/群组需要访问知识库时，管理员可通过此流程批量添加成员并指定角色。
- **场景二**：成员晋升为管理员、或需要限制某成员的操作权限时，可通过此流程变更其角色。
- **场景三**：成员离职、项目结束、或需要撤销某人/某部门的访问权限时，通过此流程将其从知识库中移除。
- **场景四**：企业希望将某个知识库（如公司规章制度、产品手册）开放给所有员工访问，无需逐一添加成员。
- **场景五**：需要审计知识库权限、排查权限问题，或在批量操作前确认成员现有角色时使用。

## 权限说明

### 权限角色（roleId）

| roleId | 角色名称 | 能力说明 |
| --- | --- | --- |
| **OWNER** | 所有者 | 最高权限，可读写、管理成员、转让知识库 |
| **MANAGER** | 管理员 | 可读写、管理成员（不含转让） |
| **EDITOR** | 编辑者 | 可查看、编辑、上传内容 |
| **DOWNLOADER** | 查看下载者 | 可查看并下载内容 |
| **READER** | 仅可查看者 | 仅可查看内容，不可下载 |

> **说明**：**OWNER** 角色不可通过接口添加或移除，知识库创建者默认为所有者。

### 成员类型（members.type）

| type 值 | 说明 | members.id 含义 |
| --- | --- | --- |
| **USER** | 用户 | 员工 userId |
| **DEPT** | 部门 | 部门 deptId，需同时传 corpId |
| **CONVERSATION** | 群会话 | 钉钉群 chatId |
| **ORG** | 企业全员 | 企业corpId，仅支持 **EDITOR**、**DOWNLOADER**、**READER** 角色 |

---

## 场景一：为新成员授予知识库访问权限

1. 调用[获取知识库列表](0560-get-knowledge-base-list.md)接口，从返回结果中获取目标知识库的`rootNodeId`字段，即知识库根节点的`dentryUuid`。
2. 获取成员 ID：

   - 添加**用户**：调用[查询用户详情](0056-query-user-details.md)接口获取`userId`，或通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)批量获取；
   - 添加**部门**：调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取`deptId`；
   - 添加**群会话**：使用群的`chatId`。
3. 调用[添加权限](0681-add-permissions-file.md)接口，根据业务需要选择合适的角色（如协作编辑选 **EDITOR**，只读访问选 **READER**），将成员加入知识库。

   > **提示**：单次请求最多传 30 个成员，超出需分批调用。

   ```
   POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions?unionId={操作者unionId} HTTP/1.1
   Host: api.dingtalk.com
   x-acs-dingtalk-access-token: {ACCESS_TOKEN}
   Content-Type: application/json

   {
     "roleId": "EDITOR",
     "members": [
       { "type": "USER", "id": "员工userId" },
       { "type": "DEPT", "id": "部门deptId", "corpId": "企业corpId" }
     ]
   }
   ```

## 场景二：调整成员在知识库中的角色

1. 如需确认成员当前角色，可先调用[获取权限列表](0684-get-permission-list.md)接口查看。
2. 调用[修改权限](0683-modify-permissions-file.md)接口，指定成员和目标角色，完成角色变更。

   > **说明**：同一成员在同一知识库只能拥有一个角色，变更后旧角色自动替换。

   ```
   PUT /v2.0/storage/spaces/dentries/{dentryUuid}/permissions?unionId={操作者unionId} HTTP/1.1
   Host: api.dingtalk.com
   x-acs-dingtalk-access-token: {ACCESS_TOKEN}
   Content-Type: application/json

   {
     "roleId": "MANAGER",
     "members": [
       { "type": "USER", "id": "员工userId" }
     ]
   }
   ```

## 场景三：移除成员的知识库访问权限

1. 确认成员当前持有的角色，调用[获取权限列表](0684-get-permission-list.md)接口，获取该成员当前的角色（`roleId`），移除时需与实际持有角色一致。
2. 调用[删除权限](0682-delete-permissions-file.md)接口。

   > **注意**：`roleId`必须与成员当前实际持有的角色一致，否则操作无效。**OWNER** 角色不可移除。

   ```
   POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/remove?unionId={操作者unionId} HTTP/1.1
   Host: api.dingtalk.com
   x-acs-dingtalk-access-token: {ACCESS_TOKEN}
   Content-Type: application/json

   {
     "roleId": "EDITOR",
     "members": [
       { "type": "USER", "id": "员工userId" }
     ]
   }
   ```

## 场景四：将知识库设置为企业全员可访问

调用[添加权限](0681-add-permissions-file.md)接口，将成员类型设为 **ORG**，并指定对应的公开角色。

> **说明**：**ORG** 类型授权后，企业全员均可按指定角色访问该知识库。**ORG** 类型成员不会出现在成员列表查询结果中。若需撤销全员访问，同样调用移除接口，`type`传 **ORG** 即可。

```
POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions?unionId={操作者unionId} HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: {ACCESS_TOKEN}
Content-Type: application/json

{
  "roleId": "READER",
  "members": [
    { "type": "ORG" }
  ]
}
```

## 场景五：查询知识库当前成员列表

调用[获取权限列表](0684-get-permission-list.md)接口，支持按角色过滤，结果支持分页。

```
POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/query?unionId={操作者unionId} HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: {ACCESS_TOKEN}
Content-Type: application/json

{
  "option": {
    "maxResults": 30,
    "filterRoleIds": ["MANAGER", "EDITOR"]
  }
}
```

返回结果中，每条记录包含成员的类型、ID、名称及其角色信息。若`nextToken`不为空，说明还有更多数据，将`nextToken`传入下次请求继续获取。

## 注意事项

- 操作者需具备知识库的 **OWNER** 或 **MANAGER** 权限，否则接口会返回权限不足错误。
- **OWNER** 角色不可通过接口添加或移除，知识库创建者默认为所有者。
- 移除成员时，`roleId`必须与成员当前实际持有的角色一致，否则操作无效。
- 单次请求 `members`列表最多传 30 个成员，超出需分批调用。
