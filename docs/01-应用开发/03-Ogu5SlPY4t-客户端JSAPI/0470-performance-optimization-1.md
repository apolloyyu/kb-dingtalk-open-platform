---
title: "性能优化建议"
source_url: "https://open.dingtalk.com/document/development/performance-optimization-1"
namespace: "development"
slug: "performance-optimization-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > 性能优化建议"
doc_id: "UPAbqpfRCu"
updated_at: "2025-09-17 20:58:14"
---

> Source: https://open.dingtalk.com/document/development/performance-optimization-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > 性能优化建议
> Updated: 2025-09-17 20:58:14

# 性能优化建议

## 优化setData逻辑

每次 setData 数据量要小，不要直接修改 this.data 然后整个 set，这样会导致传输数据量过大影响渲染性能。

推荐指定路径设置数据：

```
this.setData({
  'array[0]': 1,
  'obj.x':2,
});
```

而不是

```
const array = this.data.array.concat();
array[0] = 1;
const obj={...this.data.obj};
obj.x=2;
this.setData({array,obj});
```

更不是（违反不可变数据原则）

```
this.data.array[0]=1;
this.data.obj.x=2;
this.setData(this.data)
```

## 使用 key

在 for 中使用 key 来提高性能。

示例代码：

```
<view a:for="{{array}}" key="{{item.id}}"></view>
<block a:for="{{array}}"><view key="{{item.id}}"></view></block>
```

> **[!IMPORTANT]**
>
> key 不能设置在 block 上。
