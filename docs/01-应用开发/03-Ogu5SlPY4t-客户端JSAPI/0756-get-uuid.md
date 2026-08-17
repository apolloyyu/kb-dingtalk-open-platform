---
title: "获取uuid"
source_url: "https://open.dingtalk.com/document/development/get-uuid"
namespace: "development"
slug: "get-uuid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取uuid"
doc_id: "v2CCQY5f8m"
updated_at: "2025-09-17 20:56:04"
---

> Source: https://open.dingtalk.com/document/development/get-uuid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取uuid
> Updated: 2025-09-17 20:56:04

# 获取uuid

调用**device.base.getUUID**获取uuid。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.base.getUUID)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持 | 支持 | 不支持 |

```
dd.device.base.getUUID({
    onSuccess : function(data) {
        /*
        {
            uuid: '3udbhg98ddlljokkkl' //
        }
        */
    },
    onFail : function(err) {}
});
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| uuid | 通用唯一识别码。 |
