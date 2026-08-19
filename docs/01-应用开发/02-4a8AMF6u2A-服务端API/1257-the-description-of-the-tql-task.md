---
title: "任务筛选TQL说明"
source_url: "https://open.dingtalk.com/document/development/the-description-of-the-tql-task"
namespace: "development"
slug: "the-description-of-the-tql-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务筛选TQL说明"
doc_id: "fVF1YCec90"
updated_at: "2025-09-23 19:26:09"
---

> Source: https://open.dingtalk.com/document/development/the-description-of-the-tql-task
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务筛选TQL说明
> Updated: 2025-09-23 19:26:09

# 任务筛选TQL说明

本文介绍了项目下任务筛选使用TQL的内容。

## TQL**语法介绍**

TQL（Teambition Query Language）是一种搜索DSL(Domain Specific Language)，用于Teambition搜索语句简化，目前已覆盖高级搜索场景和项目下任务筛选。

企业内部应用项目下查询任务的接口，可以传入TQL来查询结果。

- [查询项目中的任务](1229-query-tasks-in-a-project.md)

## **TQL语法格式**

TQL是一个字符串，由**筛选字段**和**排序字段**两部分组成。

TQL语法的格式为：**筛选字段 + 操作符 + 值 +** **ORDER BY +** **排序字段 + 升序/降序**

## **筛选字段**

### **支持的筛选字段列表**

| **筛选字段** | **操作符** | **说明** |
| --- | --- | --- |
| taskflowstatusId 或者 tfsId | - = - != - IN - NOT IN | 任务状态ID。 |
| scenariofieldconfigId 或者 sfcId | - = - != - IN - NOT IN | 任务类型ID。 |
| tagId | - = - != - IN - NOT IN | 标签ID。 |
| priority | - = - != - IN - NOT IN | 优先级ID。 |
| tasklistId | - = - != - IN - NOT IN | 任务分组ID。 |
| stageId | - = - != - IN - NOT IN | 任务列表（自定义）ID。 |
| executorId | - = - != - IN - NOT IN | 执行者userId。 |
| creatorId | - = - != - IN - NOT IN | 创建者userId。 |
| involveMembers | - = - != - IN - NOT IN | 参与者userId。 |
| accomplished | - = - != - > - >= - < - <= | 完成时间。 |
| startDate | - = - != - > - >= - < - <= | 开始时间。 |
| dueDate | - = - != - > - >= - < - <= | 截止时间。 |
| created | - = - != - > - >= - < - <= | 创建时间。 |
| updated | - = - != - > - >= - < - <= | 更新时间。 |
| sprintId | - = - != - IN - NOT IN | 迭代Id。 |
| cf:id （number） | - = - != - > - >= - < - <= | 自定义字段（数字类型）。 |
| cf:id （text） | - = - != | 自定义字段（文本类型）。 |
| cf:id （date） | - = - != - > - >= - < - <= | 自定义字段（日期类型）。 |
| cf:id （cascading） | - = - != - IN - NOT IN - CONTAIN - NOT CONTAIN | 自定义字段（层级类型）。 |
| cf:id （MultiSelect） | - = - != - IN - NOT IN | 自定义字段（多选类型）。 |
| cf:id （radio） | - = - != - IN - NOT IN | 自定义字段（单选类型）。 |
| text | - ~ | 任务标题&备注。 |
| taskLayer | - = | - **taskLayer = onlyTopLevel**：顶层父任务。 - **taskLayer = exceptTopLevel**：非顶层父任务 |
| exceedDueDate | - = | - **exceedDueDate = true**：已逾期 |

### **筛选字段间的逻辑运算符列表**

| **逻辑运算符** | **说明** |
| --- | --- |
| AND | 表达式之间「**且**」的关系。 |
| OR | 表达式之间「**或**」的关系。 |

### **筛选字段支持的操作符含义列表**

| **操作符** | **说明** |
| --- | --- |
| ~ | 模糊匹配。 |
| !~ | 模糊不匹配。 |
| = | 等于。 |
| != | 不等于。 |
| > | 大于。 |
| >= | 大于等于。 |
| < | 小于。 |
| <= | 小于等于。 |
| IN | 存在于选项中。 |
| NOT IN | 不存在于选项中。 |
| CONTAIN | 含子选项（用于层级字段）。 |
| NOT CONTAIN | 不含子选项（用于层级字段）。 |

## **排序字段**

| **排序字段** | **升序/降序** | **说明** |
| --- | --- | --- |
| startDate | - ASC - DESC | 开始时间。 |
| dueDate | - ASC - DESC | 截止时间。 |
| accomplished | - ASC - DESC | 完成时间。 |
| created | - ASC - DESC | 创建时间。 |
| updated | - ASC - DESC | 更新时间。 |
| priority | - ASC - DESC | 优先级。 |
| cfPos:id | - ASC - DESC | 按自定义字段排序，目前只支持**日期/数字/文本** 类型。 |
| custom | - ASC - DESC | **「工作流项目按任务状态查看」**/ 「**普通项目按自定义查看」**任务自定义排序，升序/降序效果一致。 |
| isDone | - ASC - DESC | 是否完成。 |
| customPos:tasklist | - ASC - DESC | **按任务分组查看**自定义排序。 |
| customPos:stage | - ASC - DESC | **工作流项目按任务自定义查看**自定义排序。 |
| customPos:sprint | - ASC - DESC | **按任务迭代**自定义排序。 |

## **常见查询示例**

### **时间类型的字段查询语法**

$key$可以为任意时间字段，例如created、dueDate、accomplished。

```
'$key$ = null': 未填写
'$key$ <= endOf(d, -1d)': 今天以前
'$key$ <= endOf(d) AND $key$ >= startOf(d)': 今天
'$key$ <= endOf(d, -1d) AND $key$ >= startOf(d, -1d)': 昨天
'$key$ <= endOf(d, -1d) AND $key$ >= startOf(d, -3d)': 过去3天 
'$key$ <= endOf(d, -1d) AND $key$ >= startOf(d, -7d)': 过去7天
'$key$ <= endOf(d, -1d) AND $key$ >= startOf(d, -30d)': 过去30天
'$key$ <= endOf(d, -1d) AND $key$ >= startOf(d, -90d)': 过去90天
'$key$ <= endOf(d) AND $key$ >= startOf(d, -2d)': 最近3天 
'$key$ <= endOf(d) AND $key$ >= startOf(d, -6d)': 最近7天
'$key$ <= endOf(d, 3d) AND $key$ >= startOf(d, 1d)': 未来3天
'$key$ <= endOf(d, 7d) AND $key$ >= startOf(d, 1d)': 未来7天
'$key$ <= endOf(w) AND $key$ >= startOf(w)': 本周
'$key$ <= endOf(w, -1w) AND $key$ >= startOf(w, -1w)': 上周
'$key$ <= endOf(M) AND $key$ >= startOf(M)': 本月
'$key$ <= endOf(M, null, -1M) AND $key$ >= startOf(M, -1M)': 上月
'$key$ <= endOf(y) AND $key$ >= startOf(y)': 今年,
'$key$ <= endOf(y, null, -1y) AND $key$ >= startOf(y, -1y)': 去年
```

**示例：**

```
今天截止的任务：dueDate <= endOf(d) AND dueDate >= startOf(d)
昨天完成的任务：accomplished <= endOf(d, -1d) AND accomplished >= startOf(d, -1d)
过去两天开始的任务：startDate <= endOf(d) AND startDate >= startOf(d, -2d)
已逾期：exceedDueDate = true
```

### **只返回我可见的任务**

查询语法：myVisible=myVisible(true)

### **层级字段查询说明**

层级字段 包含（含子选项）：选项之间是 and 关系，子选项之间是 or 关系

示例：

```
cf:id CONTAIN A AND cf:id CONTAIN B
```

表达的含义是：包含 A&B 以及 A & B 子选项 (A or A/a or A/a/...) and (B or B/b or B/b/...)

### **通用场景示例**

1. #### **查看今天截止的我执行的任务，并按优先级降序**

   ```
   executorId = id AND dueDate <= endOf(d) AND dueDate >= startOf(d) AND isDone = false  ORDER BY priority  DESC
   ```
2. #### **查看指定迭代的任务，****并按完成时间降序，未完成任务放在最前面**

   ```
   sprintId = id ORDER BY isDone ASC,accomplished DESC
   ```
