---
title: "Filter"
source_url: "https://open.dingtalk.com/document/development/filter"
namespace: "development"
slug: "filter"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > API参考文档 > Filter"
doc_id: "EtQna8CGPv"
updated_at: "2025-08-27 18:09:33"
---

> Source: https://open.dingtalk.com/document/development/filter
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > API参考文档 > Filter
> Updated: 2025-08-27 18:09:33

# Filter

## getId()

获取 ID。

### 返回结果

string - ID。

### 示例代码

```
const filterId = filter.getId();
```

## getRange()

获取当前筛选区域。

### 返回结果

Range | null - 筛选所在的 Range。

### 示例代码

```
const range = filter.getRange();
```

## delete()

移除当前 filter。

### 返回结果

void -

### 示例代码

```
filter.delete();
```

## getColumnFilterCriteria(column)

获取指定列的筛选规则实例。

### 返回结果

FilterCriteria | null - 筛选规则。

### 参数说明

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| column | number | 是 | 相对于 filterRange 首列的偏移量。 |

### 示例代码

```
const filterCriteria = filter.getColumnFilterCriteria(0);
```

## setColumnFilterCriteria(column, filterCriteria)

设置指定列的筛选规则。

### 返回结果

Filter - 当前Filter实例。

### 参数说明

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| column | number | 是 | 相对于筛选区域首列的偏移量。 |
| filterCriteria | FilterCriteria | 是 | 筛选规则。 |

### 示例代码

```
const criteria = Workbook.newFilterCriteriaBuilder().
 setVisibleValues(['A', 'B', 'C']).
  build();
filter.setColumnFilterCriteria(0, criteria);
```

## clearColumnFilterCriteria(column)

移除指定列的筛选规则。

### 返回结果

Filter - 当前Filter实例。

### 参数说明

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| column | number | 是 | 相对于筛选区域首列的偏移量。 |

### 示例代码

```
filter.clearColumnFilterCriteria(0);
```

## sort(field)

筛选排序。

### 返回结果

Filter - 当前Filter实例。

### 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| 参数 | 类型 | 说明 |
| field | SortField | number    类型是number时，指定排序按照筛选区域的首列的偏移量，降序排序 | 排序规则。 |

### 示例代码

```
filter.sort({ column: 0, ascending: false });
filter.sort(0);
```

## getColumnSortState(column)

获取排序状态。

### 返回结果

'none' | 'ascending' | 'descending' - 排序状态，依次代表无排序、升序和降序。

### 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| column | number | 相对于筛选区域首列的偏移量。 |

### 示例代码

```
const state = filter.getColumnSortState(0);
```
