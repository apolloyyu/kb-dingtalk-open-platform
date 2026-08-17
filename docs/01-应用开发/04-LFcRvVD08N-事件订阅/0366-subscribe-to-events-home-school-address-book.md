---
title: "家校通讯录事件"
source_url: "https://open.dingtalk.com/document/development/subscribe-to-events-home-school-address-book"
namespace: "development"
slug: "subscribe-to-events-home-school-address-book"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 家校通讯录事件"
doc_id: "woLE2iyJpg"
updated_at: "2025-12-08 15:47:06"
---

> Source: https://open.dingtalk.com/document/development/subscribe-to-events-home-school-address-book
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 家校通讯录事件
> Updated: 2025-12-08 15:47:06

# 家校通讯录事件

本文介绍了家校通讯录相关的RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 家校通讯录数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 50 | xxxxx\_0 | corpxxxx | 无具体业务含义，只与其他属性构成唯一索引。  拼接规则：  人员关系事件： u\_r\_${id}\_${action}  监护人身份事件：g\_${id}\_${action}  学生身份事件： s\_${id}\_${action}  老师身份事件： t\_${id}\_${action}  示例：g\_1233\_insert | 50 | 家校通讯录2.0，部门信息变更 |
| 51 | xxxxx\_0 | corpxxxx | 无业务含义，只是与其他字段组成唯一索引。  拼接规则：d\_${id}\_${action} | 51 | 家校通讯录2.0，人员信息变更 |
| 25 | xxxxx\_0 | corpxxxx | userid或者deptid | 25 | 家校通讯录1.0(Deprecated)信息变更。  **[!IMPORTANT]**  家校通讯录升级，请查看家校通讯录2.0数据推送。 |

## biz\_type=50

家校通讯录2.0，部门变更推送。subscribe\_id, corp\_id, biz\_id, biz\_type组成唯一索引。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 无业务含义，只是与其他字段组成唯一索引。  拼接规则：d\_${id}\_${action} |
| biz\_type | 业务类型。家校通讯录部门变更的值为50。 |
| biz\_data | 数据为Json格式。 |

biz\_data主要包括家校通讯录架构中各个部门发生变更时的信息。主要包括新增，更新，删除（毕业）：

- **edu\_dept\_insert：部门节点新增**

  | 名称 | 类型 | 示例 | 说明 |
  | --- | --- | --- | --- |
  | dept\_id | String | 12345 | 部门ID。 |
  | contact\_type | String | classic | 家校通讯录类型。  - classic: 传统经典4层结构。校区/学段/年级/班级。 - custom：自定义结构，但是叶子节点仍旧是班级。 |
  | name | String | 一年级2班（苹果班） | 部门名称。 |
  | nick | String | 苹果班 | 部门别名。 |
  | dept\_type | String | grade | 部门类型：  - **campus：**校区/学院 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：没有业务含义，只是一个部门节点。 |
  | chain | string | [123,456] | 从顶层部门到当前节点部门的部门链，其内容不包含当前节点。  如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区： []。 |
  | feature | String |  | 部门feature，JSON格式。  各种节点部门存在不同的属性。 |
  | syncAction | String | edu\_dept\_insert | 事件类型。  syncAction为edu\_dept\_insert表示新增部门节点。 |
  | errcode | Number | 0 | 返回码。 |
  | errmsg | String | ok | 返回码描述。 |
- **edu\_dept\_update：被更新的部门节点以及其当前最新相关信息**

  | 名称 | 类型 | 示例 | 说明 |
  | --- | --- | --- | --- |
  | dept\_id | String | 12345 | 部门ID。 |
  | contact\_type | String | classic | 家校通讯录类型。  - classic: 传统经典4层结构。校区/学段/年级/班级。 - custom：自定义结构，但是叶子节点仍旧是班级。 |
  | name | String | 一年级2班（苹果班） | 部门名称。 |
  | nick | String | 苹果班 | 部门别名。 |
  | dept\_type | String | grade | 部门类型：  - **campus：**校区/学院 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：没有业务含义，只是一个部门节点。 |
  | chain | string | [123,456] | 从顶层部门到当前节点部门的部门链，其内容不包含当前节点。  如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区： []。 |
  | feature | String |  | 部门feature，JSON格式。  各种节点部门存在不同的属性。 |
  | syncAction | String | edu\_dept\_update | 事件类型。 |
  | errcode | Number | 0 | 返回码。 |
  | errmsg | String | ok | 返回码描述。 |
- **edu\_dept\_delete：被删除的部门节点**

  | 名称 | 类型 | 示例 | 说明 |
  | --- | --- | --- | --- |
  | dept\_id | Number | 12345 | 部门节点ID。 |
  | is\_graduate | Number | 0 | **0**：表示正常的删除。  **1**：表示毕业。 |
  | syncAction | String | edu\_dept\_delete | 事件类型。 |
  | errcode | Number | 0 | 返回码。 |
  | errmsg | String | ok | 返回码描述。 |

## biz\_type=51

家校通讯录2.0，人员变更推送。

subscribe\_id, corp\_id, biz\_id, biz\_type组成唯一索引。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 无具体业务含义，只与其他属性构成唯一索引。  拼接规则：   - 人员关系事件：u\_r\_${id}\_${action} - 监护人身份事件：g\_${id}\_${action} - 学生身份事件：s\_${id}\_${action} - 老师身份事件：t\_${id}\_${action}   示例：g\_1233\_insert |
| biz\_type | 业务类型，家校通讯录人员变更的值为51。 |
| biz\_data | 数据为Json格式。 |

家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。

> **[!NOTE]**
>
> 关系目前只有监护人与学生的关系。

- **人员身份biz\_data说明**

  - **edu\_user\_insert：在某个班级中新增人员身份**

    | 名称 | 类型 | 示例 | 说明 |
    | --- | --- | --- | --- |
    | userid | String | 123344 | 用户的userid。 |
    | unionid | String | FzyqbxFafVOEEEE5kGv93wiEiE | unionid, 无手机号的学生为""。 |
    | role | String | teacher | 此人在家校的角色类型：  - **teacher**：老师角色 - **guardian**：监护人角色 - **student**：学生角色 |
    | name | String | 小明爸爸 | 此人在此班级的项目。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | feature | String |  | 各个角色下存在不同属性，JSON格式。 |
    | └ is\_adviser |  |  | 是否班主任，老师角色下有效。 |
    | └ student\_no |  |  | 学号，学生角色下有效。  此值如果班级中设置了学号则有值，否则无值。 |
    | syncAction | String | edu\_user\_insert | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_update：在某个班级中人员相关身份的变更**

    | 名称 | 类型 | 示例 | 说明 |
    | --- | --- | --- | --- |
    | userid | String | 123344 | 用户的userid。 |
    | role | String | teacher | 此人在家校的角色类型：  - **teacher**：老师角色 - **guardian**：监护人角色 - **student**：学生角色 |
    | name | String | 小明爸爸 | 此人在此班级的项目。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | feature | String |  | 各个角色下存在不同属性，JSON格式。 |
    | └ is\_adviser |  |  | 是否班主任，老师角色下有效。 |
    | └ student\_no |  |  | 学号，学生角色下有效。 |
    | syncAction | String | edu\_user\_update | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_delete：在某个班级中人员身份的删除**

    | **名称** | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | userid | String | 123456 | 用户的userid。 |
    | role | String | teacher | 此人在家校的角色类型。  - **teacher：**老师角色 - **guardian：**监护人。 - **student：**学生 |
    | class\_id | Number | 12345 | 班级ID。 |
    | is\_graduate | Number | 0 | - **0**：表示正常的删除。 - **1**：表示由于毕业业务导致的人员删除。 |
    | feature | String |  | 扩展属性，老师身份提前下有效。 |
    | |\_ is\_adviser | Integer | 0 | 是否是班主任。只有在teacher的角色下有效。  - **0**: 非班主任身份 - **1**：班主任身份 |
    | syncAction | String | edu\_user\_delete | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
- **人员关系biz\_data说明**

  - **edu\_user\_relation\_insert**

    此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${from}是${to}的 ${relationName}。

    示例：在班级12345中，"123457896"是"34567890"的"爸爸"。在家校场景下，from为监护人，to为学生。

    | 名称 | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | from\_userid | String | 123457896 | 用户的userid。 |
    | to\_userid | String | 34567890 | 用户的userid。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | relation\_code | String | F | 关系code。 |
    | relation\_name | String | 爸爸 | 关系名。 |
    | syncAction | String | edu\_user\_relation\_insert | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_relation\_update**

    此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，将${from}与${to}的关系更新为 ${relationName}。

    示例：在班级12345中，将"123457896"的"34567890"关系更新为"妈妈"。在家校场景下，from为监护人，to为学生。

    | 名称 | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | from\_userid | String | 123457896 | 用户的userid。 |
    | to\_userid | String | 34567890 | 用户的userid。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | relation\_code | String | M | 关系code。 |
    | relation\_name | String | 妈妈 | 关系名。 |
    | syncAction | String | edu\_user\_relation\_update | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_relation\_delete**

    此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，将${from}是${to}的 ${relationName}的关系删除。

    示例：在班级12345中，删除"123457896"是"34567890"的"爸爸"这样一层关系。在家校场景下，from为监护人，to为学生。

    | 名称 | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | from\_userid | String | 123457896 | 用户的userid。 |
    | to\_userid | String | 34567890 | 用户的userid。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | relation\_code | String | M | 关系code。 |
    | relation\_name | String | 妈妈 | 关系名。 |
    | syncAction | String | edu\_user\_relation\_delete | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
