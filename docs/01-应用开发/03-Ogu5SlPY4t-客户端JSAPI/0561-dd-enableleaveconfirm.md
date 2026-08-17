---
title: "离开二次确认配置"
source_url: "https://open.dingtalk.com/document/development/dd-enableleaveconfirm"
namespace: "development"
slug: "dd-enableleaveconfirm"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 离开页面二次确认 > 离开二次确认配置"
doc_id: "Edu0xGbFeA"
updated_at: "2025-09-17 20:59:17"
---

> Source: https://open.dingtalk.com/document/development/dd-enableleaveconfirm
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 离开页面二次确认 > 离开二次确认配置
> Updated: 2025-09-17 20:59:17

# 离开二次确认配置

调用**dd.enableLeaveConfirm**对当前页面进行离开二次确认。

> **[!NOTE]**
>
> 当前页面指调用dd.enableLeaveConfirm及dd.disableLeaveConfirm时**小程序栈顶页面**，与**该 JSAPI 在哪个 page 实例下调用无关。**

## 示例代码

```
dd.enableLeaveConfirm({
    effect: ['back', 'close'],
  info: {
    title: '忘记提交？',
    content: '当前页面内容尚未提交，离开将导致内容丢失，确认离开吗？'
  },
  success: function(){},
  fail: function(){},
  complete: function(){}
})
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| effect | Array<'back' | 'close'> | 指定生效场景：   - **back**: 点击返回。 - **close**：点击关闭。 |
| info | {  title: string,  content: string  } | - **title**：指定弹窗标题。 - **content**:：指定弹窗内容。   **推荐：title字段不超过8个中文字符长度，content 不超过40个中文字符长度。** |
| success | Function | 成功回调。 |
| fail | Function | 错误回调。 |
| complete | Function | 完成回调。 |

## 兼容性

**平台：**

| **平台** | **iOS** | **Android** | **Mac** | **Windows** |
| --- | --- | --- | --- | --- |
| **兼容平台** | 钉钉版本≥4.7.10 | 钉钉版本≥4.7.10 | 不支持 | 不支持 |

**兼容性判断：**

请使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('enableLeaveConfirm') 和[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('disableLeaveConfirm') 进行兼容性判断。
