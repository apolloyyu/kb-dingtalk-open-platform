---
title: "知识库权限变更"
source_url: "https://open.dingtalk.com/document/development/change-of-knowledge-base-access-rights"
namespace: "development"
slug: "change-of-knowledge-base-access-rights"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 使用教程 > 知识库权限变更"
doc_id: "e7jhgL5M5g"
updated_at: "2026-04-08 20:23:51"
---

> Source: https://open.dingtalk.com/document/development/change-of-knowledge-base-access-rights
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 使用教程 > 知识库权限变更
> Updated: 2026-04-08 20:23:51

# 知识库权限变更

本文档详细介绍了如何对知识库中的文档、文件或文件夹进行权限变更操作。

## 功能说明

本文档介绍如何对知识库中的文档、文件或文件夹进行权限变更操作，包括：

- **添加权限** — 为成员授予文件/文件夹的访问权限
- **删除权限** — 移除成员对文件/文件夹的访问权限
- **修改权限** — 变更成员对文件/文件夹的权限角色
- **设置权限继承模式** — 控制文件/文件夹是否继承父节点的权限
- **获取权限继承模式** — 查询当前文件/文件夹的权限继承模式

> **核心概念**：所有权限操作都基于文件的 `dentryUuid`（文件唯一标识）进行，操作者需要具备对应文件的权限管理能力。

## **权限说明**

以下是不同成员类型和权限角色的介绍，及不同角色所对应的能力。

### 权限角色（roleId）

进行权限变更时，需要指定权限角色：

| roleId | 角色名称 | 能力说明 |
| --- | --- | --- |
| **OWNER** | 拥有者 | 最高权限，可读写、管理权限、分配权限 |
| **MANAGER** | 管理者 | 可读写、管理权限（不含分配权限） |
| **EDITOR** | 编辑者 | 可查看、编辑、下载、添加 |
| **DOWNLOADER** | 查看下载者 | 可查看、下载 |
| **READER** | 仅可查看者 | 仅可查看，不可下载 |

### 权限成员类型（members.type）

| type 值 | 说明 | members.id 含义 |
| --- | --- | --- |
| **USER** | 用户 | 员工 userId |
| **ORG** | 企业 | 企业 ID |
| **DEPT** | 部门 | 部门 ID |
| **TAG** | 自定义标签 | 标签 ID |
| **CONVERSATION** | 会话 | 会话 ID |

## 功能实现：添加权限

调用接口 `POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions`，为指定成员授予对文件/文件夹的访问权限。

> **[!NOTE]**
>
> 接口请参考[添加权限](0681-add-permissions-file.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**需要传入：**

- `dentryUuid`（Path）：目标文件/文件夹的唯一标识，通过[搜索文件](0638-search-for-files.md)接口获取；
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取；
- `roleId`（Body）：要授予的权限角色，如 **EDITOR**；
- `members`（Body）：要授权的成员列表，每个成员需指定 `type`（成员类型）和 `id`（成员 ID）。

**HTTP示例**：

```
POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions?unionId=操作者unionId HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json

{
  "roleId": "EDITOR",
  "members": [
    {
      "type": "USER",
      "id": "员工userId",
      "corpId": "企业corpId"
    }
  ]
}
```

## 功能实现：修改权限

调用接口 `PUT /v2.0/storage/spaces/dentries/{dentryUuid}/permissions`，将指定成员的权限角色变更为新的角色。

**降低权限时的重要限制**：如果成员的当前权限是**继承自父节点**，且父节点继承来的权限角色**高于**目前想要设置的目标角色，则修改不会生效。

- **示例**：父目录给某用户授予了**EDITOR**权限，在子文件夹上将其修改为**READER**会失败，因为继承的 **EDITOR** 权限仍然生效。
- **解决方案**：需要先对该文件/文件夹调用[设置权限继承模式](0685-set-permission-inheritance-mode.md)接口，将继承模式设为**BREAK**（打断），切断父节点权限的传递，再进行权限修改。

> **[!NOTE]**
>
> 接口请参考[修改权限](0683-modify-permissions-file.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**需要传入：**

- `dentryUuid`（Path）：目标文件/文件夹的唯一标识，通过[搜索文件](0638-search-for-files.md)接口获取；
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取；
- `roleId`（Body）：修改后的目标权限角色（如从**EDITOR**改为**READER**）；
- `members`（Body）：要修改权限的成员列表。

**HTTP示例**：

```
PUT /v2.0/storage/spaces/dentries/{dentryUuid}/permissions?unionId=操作者unionId HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json

{
  "roleId": "READER",
  "members": [
    {
      "type": "USER",
      "id": "员工userId",
      "corpId": "企业corpId"
    }
  ]
}
```

## 功能实现：删除权限

调用接口 `POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/remove`，移除指定成员对文件/文件夹的访问权限。

> **[!NOTE]**
>
> 接口请参考[删除权限](0682-delete-permissions-file.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**需要传入：**

- `dentryUuid`（Path）：目标文件/文件夹的唯一标识，通过[搜索文件](0638-search-for-files.md)接口获取；
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取；
- `roleId`（Body）：要删除的权限角色（必须与成员当前实际持有的角色一致）；
- `members`（Body）：要删除权限的成员列表。

**HTTP示例**：

```
POST /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/remove?unionId=操作者unionId HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json

{
  "roleId": "EDITOR",
  "members": [
    {
      "type": "USER",
      "id": "员工userId",
      "corpId": "企业corpId"
    }
  ]
}
```

## 功能实现：设置权限继承模式

调用接口 `PUT /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/inheritances`，控制文件/文件夹是否继承父节点的权限。

**两种继承模式：**

- **PASS\_ON**（传递）：当前节点继承所有父节点的权限，相同成员权限取最大值（**默认模式**）；
- **BREAK**（打断）：在当前节点打断权限传递，不再继承父节点权限，适合需要单独设置独立权限的场景。

> **[!NOTE]**
>
> - `BREAK`模式不支持对`OWNER`和`MANAGER`角色打断。
> - 接口请参考[设置权限继承模式](0685-set-permission-inheritance-mode.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**需要传入：**

- `dentryUuid`（Path）：目标文件/文件夹的唯一标识，通过[搜索文件](0638-search-for-files.md)接口获取；
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取；
- `inheritance`（Body）：继承模式**PASS\_ON**或**BREAK**。

**HTTP示例**：

```
PUT /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/inheritances?unionId=操作者unionId HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json

{
  "inheritance": "BREAK"
}
```

## 功能实现：获取权限继承模式

调用接口 `GET /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/inheritances`，查询当前文件/文件夹的权限继承模式。

> **[!NOTE]**
>
> - 接口会返回`inheritance`字段，值为**PASS\_ON**（传递）或**BREAK**（打断）。
> - 接口请参考[获取权限继承模式](0686-get-permission-inheritance-mode.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**需要传入：**

- `dentryUuid`（Path）：目标文件/文件夹的唯一标识，通过[搜索文件](0638-search-for-files.md)接口获取；
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取；

**HTTP示例**：

```
GET /v2.0/storage/spaces/dentries/{dentryUuid}/permissions/inheritances?unionId=操作者unionId HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json
```

## 典型场景及操作步骤

### 场景一：给某用户添加文件编辑权限

1. 通过[搜索文件](0638-search-for-files.md)接口，获取目标文件的 `dentryUuid`；
2. 通过[查询用户详情](0056-query-user-details.md)接口，获取目标用户的`userId`和操作者的`unionId`
3. 调用[添加权限](0681-add-permissions-file.md)接口，`roleId = "EDITOR"`，`members[0].type = "USER"`，`members[0].id = 目标用户 userId`。

### 场景二：将某用户的权限从编辑者降级为只读

1. 通过[搜索文件](0638-search-for-files.md)接口，获取目标文件的 `dentryUuid`；
2. 通过[查询用户详情](0056-query-user-details.md)接口，获取目标用户的`userId`；
3. 调用[修改权限](0683-modify-permissions-file.md)接口，`roleId = "READER"`，`members`指定目标用户。

### 场景三：移除某用户对文件的所有权限

1. 通过[搜索文件](0638-search-for-files.md)接口，获取目标文件的 `dentryUuid`；
2. 通过[查询用户详情](0056-query-user-details.md)接口，获取目标用户的`userId`；
3. 调用[删除权限](0682-delete-permissions-file.md)接口，`roleId` 填写该用户当前持有的权限角色，`members` 指定目标用户。

### 场景四：为某个子文件夹设置独立权限（不继承父目录）

1. 通过[搜索文件](0638-search-for-files.md)接口，获取子文件夹的 `dentryUuid`；
2. 调用[设置权限继承模式](0685-set-permission-inheritance-mode.md)接口，`inheritance = "BREAK"`打断权限继承；
3. 再调用[添加权限](0681-add-permissions-file.md)接口，单独为该文件夹配置所需的权限成员和角色。

## 注意事项

- 操作者（`unionId`）需要具备对应文件的权限管理能力，否则会返回权限不足错误。
- 删除权限时，`roleId` 必须与成员当前实际持有的权限角色一致，否则操作无效。
- **OWNER**和**MANAGER**角色的权限不支持通过 **BREAK** 模式打断继承。
- `members`列表单次最多传 30 个成员，超出需分批调用。
- 目前所有权限接口仅企业内部应用支持，第三方应用暂不支持。
