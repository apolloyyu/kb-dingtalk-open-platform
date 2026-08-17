---
title: "删除存储信息"
source_url: "https://open.dingtalk.com/document/development/delete-storage-information"
namespace: "development"
slug: "delete-storage-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 存储 > 删除存储信息"
doc_id: "4IAEk7qf53"
updated_at: "2025-09-17 20:56:47"
---

> Source: https://open.dingtalk.com/document/development/delete-storage-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 存储 > 删除存储信息
> Updated: 2025-09-17 20:56:47

# 删除存储信息

调用**util.domainStorage.removeItem**删除存储信息。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=util.domainStorage.removeItem)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.util.domainStorage.removeItem({
     name:'key' , // 存储信息的key值
     onSuccess : function(info) {
          alert(JSON.stringify(info));
     },
     onFail : function(err) {
          alert(JSON.stringify(err));
     }
 });
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| name | String | 存储信息的key值。 |
