---
title: "取消当前页面的离开二次确认"
source_url: "https://open.dingtalk.com/document/development/dd-disableleaveconfirm"
namespace: "development"
slug: "dd-disableleaveconfirm"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 离开页面二次确认 > 取消当前页面的离开二次确认"
doc_id: "6LXSt2Vg6U"
updated_at: "2025-09-17 20:59:18"
---

> Source: https://open.dingtalk.com/document/development/dd-disableleaveconfirm
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 离开页面二次确认 > 取消当前页面的离开二次确认
> Updated: 2025-09-17 20:59:18

# 取消当前页面的离开二次确认

调用**dd.disableLeaveConfirm**取消当前页面的离开二次确认配置。

> **[!NOTE]**
>
> 当前页面指调用dd.enableLeaveConfirm及dd.disableLeaveConfirm时**小程序栈顶页面**，与**该 JSAPI 在哪个 page 实例下调用无关。**

## 示例代码

```
dd.disableLeaveConfirm({
    success: function(){},
  fail: function(){},
  complete: function(){}
})
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| success | Function | 成功回调。 |
| fail | Function | 错误回调。 |
| complete | Function | 完成回调。 |

## 兼容性

**平台**

| **平台** | **iOS** | **Android** | **Mac** | **Windows** |
| --- | --- | --- | --- | --- |
| **兼容平台** | 钉钉版本≥4.7.10 | 钉钉版本≥4.7.10 | 不支持 | 不支持 |

**兼容性判断**

请使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('enableLeaveConfirm') 和[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('disableLeaveConfirm') 进行兼容性判断。
