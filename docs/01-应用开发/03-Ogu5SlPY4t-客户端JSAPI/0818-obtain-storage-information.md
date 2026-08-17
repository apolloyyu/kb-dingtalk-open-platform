---
title: "获取存储信息"
source_url: "https://open.dingtalk.com/document/development/obtain-storage-information"
namespace: "development"
slug: "obtain-storage-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 存储 > 获取存储信息"
doc_id: "MmCMZZYzYR"
updated_at: "2025-09-17 20:56:47"
---

> Source: https://open.dingtalk.com/document/development/obtain-storage-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 存储 > 获取存储信息
> Updated: 2025-09-17 20:56:47

# 获取存储信息

调用**util.domainStorage.getItem**获取存储信息。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=util.domainStorage.getItem)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.util.domainStorage.getItem({
     name:'key' , // 存储信息的key值
     onSuccess : function(info) {
        /*{
             value: 'value' // 获取存储的信息
         }*/
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

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| value | String | name对应的存储信息。 |
