---
title: "家校通讯录2.0数据推送"
source_url: "https://open.dingtalk.com/document/development/home-school-address-book-2-0-data-push"
namespace: "development"
slug: "home-school-address-book-2-0-data-push"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > 家校通讯录2.0数据推送"
doc_id: "dTFuhlnna9"
updated_at: "2026-01-08 20:07:19"
---

> Source: https://open.dingtalk.com/document/development/home-school-address-book-2-0-data-push
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > 家校通讯录2.0数据推送
> Updated: 2026-01-08 20:07:19

# 家校通讯录2.0数据推送

## 术语表

| **术语** | **说明** |
| --- | --- |
| **biz\_type** | 业务类型标识符。用于区分不同类别的数据变更事件。家校通讯录2.0中：  • `50` 表示部门变更  • `51` 表示人员变更 |
| **subscribe\_id** | 订阅ID，由套件suiteid + "\_0" 组成，表示当前订阅的唯一标识。 |
| **corp\_id** | 企业Corp ID，指开通该微应用的企业在钉钉平台中的唯一标识。 |
| **biz\_id** | 业务ID，无实际业务含义，仅与 `subscribe_id`, `corp_id`, `biz_type` 共同构成数据库唯一索引。  拼接规则根据事件类型而定（如 d\_开头表示部门，g\_/s\_/t\_/u\_r\_ 表示不同身份或关系）。 |
| **syncAction** | 同步动作字段，表示具体触发的事件类型，例如 `edu_dept_insert`、`edu_user_relation_update` 等。 |
| **contact\_type** | 通讯录结构类型，表示家校通讯录采用的组织模式：  • `classic`：传统四层结构（校区/学段/年级/班级）  • `custom`：自定义结构，但叶子节点仍为班级 |

## **家校通讯录数据推送**

| 类型 | **业务类型biz\_type** | **说明** |
| --- | --- | --- |
| 家校通讯录2.0数据推送 | 50 | 家校通讯录2.0，部门变更推送。  推荐开发者使用。 |
| 51 | 家校通讯录2.0，人员变更推送。  推荐开发者使用。 |
| 家校通讯录1.0数据推送 | 25 | 家校通讯录1.0接口升级，请开发者优先使用“家校通讯录2.0”接口。对于家校通讯录1.0接口，计划于2020年8月7日将文档下线，接口暂不会下线，之前已使用老接口的应用可以正常调用。 |

## 部门推送

`subscribe_id`, `corp_id`, `biz_id`, `biz_type` 四者组成唯一索引，用于标识每一条推送记录。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 无业务含义，只是与其他字段组成唯一索引。  拼接规则：d\_${id}\_${action} |
| biz\_type | 业务类型。家校通讯录部门变更的值为50。 |
| biz\_data | 数据为Json格式。 |

### **edu\_dept\_insert：部门节点新增**

| 名称 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| dept\_id | String | 12345 | 部门ID。 |
| contact\_type | String | classic | 家校通讯录类型：   - **classic**：传统四层结构（校区/学段/年级/班级） - **custom**：自定义结构，但叶子节点仍为班级。 |
| name | String | 一年级2班(苹果班) | 部门名称。 |
| nick | String | 苹果班 | 部门别名。 |
| dept\_type | String | grade | 部门类型：   - **campus：**校区/学院 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：没有业务含义，只是一个部门节点。 |
| chain | string | [123,456] | 从顶层部门到当前节点部门的部门链，其内容不包含当前节点。  如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区: []。 |
| feature | String |  | 部门feature，JSON格式。  各种节点部门存在不同的属性。 |
| syncAction | String | edu\_dept\_insert | 事件类型。  syncAction为edu\_dept\_insert表示新增部门节点。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **edu\_dept\_update：部门更新**

> **[!NOTE]**
>
> 被更新的部门节点以及其当前最新相关信息。

| 名称 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| dept\_id | String | 12345 | 部门ID。 |
| contact\_type | String | classic | 家校通讯录类型：   - **classic**：传统四层结构（校区/学段/年级/班级） - **custom**：自定义结构，但叶子节点仍为班级。 |
| name | String | 一年级2班(苹果班) | 部门名称。 |
| nick | String | 苹果班 | 部门别名。 |
| dept\_type | String | grade | 部门类型：   - **campus：**校区/学院 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：没有业务含义，只是一个部门节点。 |
| chain | string | [123,456] | 从顶层部门到当前节点部门的部门链，其内容不包含当前节点。  如classic类型下的班级：[校区id，学段id，年级id]；如classic类型下的校区：[]。 |
| feature | String |  | 部门feature，JSON格式。各种节点部门存在不同的属性。 |
| syncAction | String | edu\_dept\_update | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### edu\_dept\_delete：部门删除

当删除某个部门（如班级撤销或毕业）时触发。

| 名称 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| dept\_id | Number | 12345 | 部门节点ID。 |
| is\_graduate | Number | 0 | - **0**：表示正常的删除。 - **1**：表示毕业。 |
| syncAction | String | edu\_dept\_delete | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 人员推送

`subscribe_id`, `corp_id`, `biz_id`, `biz_type` 四者组成唯一索引。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 无具体业务含义，只与其他属性构成唯一索引。  拼接规则：   - 人员关系事件：`u_r_${id}_${action}` - 监护人身份事件：`g_${id}_${action}` - 学生身份事件：`s_${id}_${action}` - 老师身份事件：`t_${id}_${action}`   示例：`g_1233_insert` |
| biz\_type | 业务类型，家校通讯录人员变更的值为51。 |
| biz\_data | 数据为 JSON 格式，包含人员身份或关系变更详情。 |

> **[!NOTE]**
>
> 关系目前只有监护人与学生的关系。

### **edu\_user\_insert：**人员身份新增

当用户被添加到某个班级并赋予特定角色（如学生、老师、监护人）时触发。

| 名称 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| userid | String | 123344 | 用户的userid。 |
| unionid | String | Fzyqxxx93wiEiE | unionid，无手机号的学生为""。 |
| role | String | teacher | 此人在家校的角色类型：   - **teacher**：老师角色 - **guardian**：监护人角色 - **student**：学生角色 |
| name | String | 小明爸爸 | 此人在此班级的项目。 |
| class\_id | Number | 12345 | 班级ID。 |
| feature | String |  | 各个角色下存在不同属性，JSON格式。 |
| └ is\_adviser |  |  | 是否班主任，老师角色下有效。 |
| └ student\_no |  |  | 学号，学生角色下有效。此值如果班级中设置了学号则有值，否则无值。 |
| syncAction | String | edu\_user\_insert | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **edu\_user\_update：**人员身份更新

当用户在班级内的角色信息发生变更时触发，推送更新后的完整信息。

| 名称 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| userid | String | 123344 | 用户的userid。 |
| role | String | teacher | 此人在家校的角色类型：   - **teacher**：老师角色 - **guardian**：监护人角色 - **student**：学生角色 |
| name | String | 小明爸爸 | 此人在此班级的项目。 |
| class\_id | Number | 12345 | 班级ID。 |
| feature | String |  | 各个角色下存在不同属性，JSON格式。 |
| └ is\_adviser |  |  | 是否班主任，老师角色下有效。 |
| └ student\_no |  |  | 学号，学生角色下有效。 |
| syncAction | String | edu\_user\_update | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **edu\_user\_delete：**人员身份删除

当用户从班级中移除其某一角色时触发。

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| userid | String | 123456 | 用户的userid。 |
| role | String | teacher | 此人在家校的角色类型。   - **teacher：**老师角色 - **guardian：**监护人。 - **student：**学生 |
| class\_id | Number | 12345 | 班级ID。 |
| is\_graduate | Number | 0 | - **0**：表示正常的删除。 - **1**：表示由于毕业业务导致的人员删除。 |
| feature | String |  | 扩展属性，老师身份提前下有效。 |
| └ is\_adviser | Integer | 0 | 是否是班主任。只有在teacher的角色下有效。   - **0**：非班主任身份 - **1**：班主任身份 |
| syncAction | String | edu\_user\_delete | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **edu\_user\_relation\_insert：**监护人关系新增

在家校场景下，建立监护人与学生的关系时触发。

> 可理解为表达式：在班级 `${class_id}` 中，`${from_userid}` 是 `${to_userid}` 的 `${relation_name}`。

示例：在班级 `12345` 中，“123457896”是“34567890”的“爸爸”。

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

### **edu\_user\_relation\_update：**监护人关系更新

当监护人与学生的关系发生变化时触发（如称谓修改）。

> 表达式：在班级 `${class_id}` 中，将 `${from_userid}` 与 `${to_userid}` 的关系更新为 `${relation_name}`。

示例：将“张伟”与“张小明”的关系由“爸爸”更新为“妈妈”。

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

### **edu\_user\_relation\_delete：**监护人关系删除

解除监护人与学生之间的绑定关系时触发。

> 表达式：在班级 `${class_id}` 中，删除 `${from_userid}` 是 `${to_userid}` 的 `${relation_name}` 这一关系。

示例：删除“1234”是“34”的“妈妈”这一关系。

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
