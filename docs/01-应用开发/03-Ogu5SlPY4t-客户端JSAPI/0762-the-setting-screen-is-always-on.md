---
title: "设置屏幕常亮"
source_url: "https://open.dingtalk.com/document/development/the-setting-screen-is-always-on"
namespace: "development"
slug: "the-setting-screen-is-always-on"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 设置屏幕常亮"
doc_id: "k6X0sBylGN"
updated_at: "2025-09-17 20:56:07"
---

> Source: https://open.dingtalk.com/document/development/the-setting-screen-is-always-on
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 设置屏幕常亮
> Updated: 2025-09-17 20:56:07

# 设置屏幕常亮

调用**biz.util.setScreenKeepOn**设置屏幕常亮，防止熄屏。

> **[!NOTE]**
>
> H5容器关闭后自动失效。

## 使用说明

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持（钉钉版本≥5.1.26） | 支持（钉钉版本≥5.1.26） | 不支持 |

```
dd.biz.util.setScreenKeepOn({
    isKeep:true,
    onSuccess: function() {},
    onFail: function() {}
   }
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| isKeep | Boolean | 是 | 是否保持常亮，默认值**false**。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |
