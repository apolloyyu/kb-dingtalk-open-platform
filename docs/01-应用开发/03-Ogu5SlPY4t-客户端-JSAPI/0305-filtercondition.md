---
title: "FilterCondition"
source_url: "https://open.dingtalk.com/document/development/filtercondition"
namespace: "development"
slug: "filtercondition"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > API参考文档 > FilterCondition"
doc_id: "HHCcM4KpgO"
updated_at: "2025-08-27 18:09:37"
---

> Source: https://open.dingtalk.com/document/development/filtercondition
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > API参考文档 > FilterCondition
> Updated: 2025-08-27 18:09:37

# FilterCondition

## API描述

筛选条件。用于FilterCriteriaBuilder或者FilterCriteria的相关API中指定筛选条件。

## 属性说明

| 属性 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| operator | String | 是 | 筛选条件的运算符，可选以下值   - equal：相等。 - not-equal: 不相等。 - contains：包含。 - not-contains：不包含。 - starts-with：从...开始。 - not-starts-with：不是从...开始。 - ends-with：以...结束。 - not-ends-with：不是以...结束。 - greater：大于。 - greater-equal：大于等于。 - less：小于。 - less-equal：小于等于。 |
| value | string | number | 是 | 筛选条件的值。 |
