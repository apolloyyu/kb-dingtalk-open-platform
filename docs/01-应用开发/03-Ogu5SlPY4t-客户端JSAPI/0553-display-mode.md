---
title: "显示模式"
source_url: "https://open.dingtalk.com/document/development/display-mode"
namespace: "development"
slug: "display-mode"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 显示模式"
doc_id: "KSuD0jM0K4"
updated_at: "2025-09-17 20:59:12"
---

> Source: https://open.dingtalk.com/document/development/display-mode
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 显示模式
> Updated: 2025-09-17 20:59:12

# 显示模式

调用**dd.getColorSchemeSync**获取钉钉当前显示模式。返回当前系统的显示模式"light" 或 "dark"。

## 使用方法

```
const colorScheme = dd.canIUse("getColorSchemeSync") ? dd.getColorSchemeSync() : "light";
// use colorScheme
```

## 监听显示模式事件

通过 `dd.onColorSchemeChange` 监听显示模式变化，通过 `dd.offColorSchemeChange` 解除绑定。

代码示例：

```
Page({
  colorSchemeChangeHandler({ colorScheme }) {
        // use colorScheme
    },
  
    onLoad() {
    dd.onColorSchemeChange(this.colorSchemeChangeHandler);
  },
  
  unbind() {
    dd.onColorSchemeChange(this.colorSchemeChangeHandler);
  },
});
```

## 兼容性判断

调用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)("getColorSchemeSync") 进行兼容性判断。
