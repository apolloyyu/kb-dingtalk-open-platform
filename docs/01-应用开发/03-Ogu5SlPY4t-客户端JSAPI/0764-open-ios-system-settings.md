---
title: "打开iOS系统设置"
source_url: "https://open.dingtalk.com/document/development/open-ios-system-settings"
namespace: "development"
slug: "open-ios-system-settings"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 打开iOS系统设置"
doc_id: "IU6BNUBiBc"
updated_at: "2025-09-17 20:56:08"
---

> Source: https://open.dingtalk.com/document/development/open-ios-system-settings
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 打开iOS系统设置
> Updated: 2025-09-17 20:56:08

# 打开iOS系统设置

调用**device.base.openSystemSetting**打开iOS系统设置页面。

## 使用说明

| 客户端 | Android | iOS | PC | **是否需鉴权** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不支持 | 支持（钉钉版本≥6.3.15） | 不支持 | 否 |

```
dd.device.base.openSystemSetting({
    onSuccess : function() {
    },
    onFail : function() {
    }
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |
