---
title: "获取H5容器启动时间"
source_url: "https://open.dingtalk.com/document/development/obtains-the-h5-container-startup-time"
namespace: "development"
slug: "obtains-the-h5-container-startup-time"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取H5容器启动时间"
doc_id: "hBCsMXwkRA"
updated_at: "2025-09-17 20:56:08"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-h5-container-startup-time
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取H5容器启动时间
> Updated: 2025-09-17 20:56:08

# 获取H5容器启动时间

调用**runtime.monitor.getLoadTime**获取H5容器启动时间。

## 使用说明

| **客户端** | Android | iOS | PC |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥6.0.10.x） | 支持（钉钉版本≥6.0.10.x） | 不支持 |

```
dd.runtime.monitor.getLoadTime({
    type:'RuntimeLaunchTime',
    onSuccess: function() {},
    onFail: function() {}
   }
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| type | String | 是 | - **RuntimeLaunchTime**：容器启动耗时。 - **PageLoadTime**：容器启动时间，从init到第一个页面加载成功。 - **RuntimeStartLoadTime**：容器初始化到容器中的webview开始加载web资源的耗时。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| time | Number | 所查询对应的时间。 |
| type | String | - **RuntimeLaunchTime**：容器启动耗时。 - **PageLoadTime**：容器启动时间，从init到第一个页面加载成功。 - **RuntimeStartLoadTime**：容器初始化到容器中的webview开始加载web资源的耗时。 |

### 失败

| error | 描述 |
| --- | --- |
| 3 | 内部错误。 |
