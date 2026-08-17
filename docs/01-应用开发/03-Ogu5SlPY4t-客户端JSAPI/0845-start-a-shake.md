---
title: "启动摇一摇"
source_url: "https://open.dingtalk.com/document/development/start-a-shake"
namespace: "development"
slug: "start-a-shake"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 摇一摇 > 启动摇一摇"
doc_id: "xw1pNuNHyJ"
updated_at: "2025-09-17 20:57:06"
---

> Source: https://open.dingtalk.com/document/development/start-a-shake
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 摇一摇 > 启动摇一摇
> Updated: 2025-09-17 20:57:06

# 启动摇一摇

调用**device.accelerometer.watchShake**启动摇一摇。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.accelerometer.watchShake)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.accelerometer.watchShake({
    sensitivity: 20,//振动幅度，Number类型，加速度变化超过这个值后触发shake
    frequency: 150,//采样间隔(毫秒)，Number类型，指每隔多长时间对加速度进行一次采样，然后对比前后变化，判断是否触发shake
    callbackDelay: 3000,//触发『摇一摇』后的等待时间(毫秒)，Number类型，防止频繁调用
    onSuccess : function(result) {
        /*
        {}
        */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| sensitivity | Number | 振动幅度，加速度变化超过这个值后触发shake。 |
| frequency | Number | 采样间隔(毫秒)，指每隔多长时间对加速度进行一次采样， 然后对比前后变化，判断是否触发shake。 |
| callbackDelay | Number | 触发『摇一摇』后的等待时间(毫秒)，防止频繁调用。 |
