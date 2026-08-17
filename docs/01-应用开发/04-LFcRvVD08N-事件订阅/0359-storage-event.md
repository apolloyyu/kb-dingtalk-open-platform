---
title: "存储事件"
source_url: "https://open.dingtalk.com/document/development/storage-event"
namespace: "development"
slug: "storage-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 存储事件"
doc_id: "jgWyZOPBdz"
updated_at: "2025-10-16 15:06:35"
---

> Source: https://open.dingtalk.com/document/development/storage-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 存储事件
> Updated: 2025-10-16 15:06:35

# 存储事件

本文介绍了存储事件回调的RDS和SyncHTTP推送的数据格式。

> **[!NOTE]**
>
> 如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/isvapp/subscribe-to-file-change-events)。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 233 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=233的数据格式解释。 | 233 | 文件或文件夹添加事件。 |
| 234 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=234的数据格式解释。 | 234 | 文件或文件夹更新事件。 |
| 235 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=235的数据格式解释。 | 235 | 文件或文件夹删除事件。 |

## biz\_type=233

当biz\_type=233时，数据为文件或文件夹添加相关数据，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值233，表示文件或文件夹添加相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "storage_dentry_create",
  "UnionId": "xx",
  "eventScope": "ORG",
  "eventScopeId": "xx",
  "dentryId":"xx",
  "spaceId":"xx",
  "extension":"pdf",
  "type": "FILE"
}
```

字段说明：

| 参数 | 说明 |
| --- | --- |
| syncAction | 事件类型：   - **storage\_dentry\_create**：文件或文件夹添加事件 |
| UnionId | 操作用户unionId。 |
| eventScope | 订阅范围：   - **ORG**: 企业 - **SPACE**: 空间 |
| eventScopeId | 订阅ID。  **[!NOTE]**   - 当`eventScope`为**ORG**时，对应授权开通第三方企业应用的企业corpId。 - 当`eventScope`为**SPACE**时，对应空间id。 |
| dentryId | 文件Id。 |
| spaceId | 空间Id。 |
| extension | 后缀信息。 |
| type | 文件类型：   - **FILE**：文件 - **FOLDER**：文件夹 |

## biz\_type=234

当biz\_type=234时，数据为文件更新相关数据，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值234。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "storage_dentry_update",
  "UnionId": "xx",
  "eventScope": "ORG",
  "eventScopeId": "xx",
  "dentryId":"xx",
  "spaceId":"xx",
  "extension":"pdf",
  "type": "FILE"
}
```

字段说明：

| 参数 | 说明 |
| --- | --- |
| syncAction | 事件类型：   - **storage\_dentry\_update**：文件或文件夹更新事件 |
| UnionId | 操作用户unionId。 |
| eventScope | 订阅范围：   - **ORG**: 企业 - **SPACE**: 空间 |
| eventScopeId | 订阅ID。  **[!NOTE]**   - 当`eventScope`为**ORG**时，对应授权开通第三方企业应用的企业corpId。 - 当`eventScope`为**SPACE**时，对应空间id。 |
| dentryId | 文件Id。 |
| spaceId | 空间Id。 |
| extension | 后缀信息。 |
| type | 文件类型：   - **FILE**：文件 - **FOLDER**：文件夹 |

## biz\_type=235

当biz\_type=235时，数据为文件删除相关数据，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值235。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "storage_dentry_delete",
  "UnionId": "xx",
  "eventScope": "ORG",
  "eventScopeId": "xx",
  "dentryId":"xx",
  "spaceId":"xx",
  "extension":"pdf",
  "type": "FILE"
}
```

字段说明：

| 参数 | 说明 |
| --- | --- |
| syncAction | 事件类型：   - **storage\_dentry\_delete**：文件或文件夹删除事件 |
| UnionId | 操作用户unionId。 |
| eventScope | 订阅范围   - **ORG**: 企业 - **SPACE**: 空间 |
| eventScopeId | 订阅ID。  **[!NOTE]**   - 当`eventScope`为**ORG**时，对应授权开通第三方企业应用的企业corpId。 - 当`eventScope`为**SPACE**时，对应空间id。 |
| dentryId | 文件Id。 |
| spaceId | 空间Id。 |
| extension | 后缀信息。 |
| type | 文件类型：   - **FILE**：文件 - **FOLDER**：文件夹 |
