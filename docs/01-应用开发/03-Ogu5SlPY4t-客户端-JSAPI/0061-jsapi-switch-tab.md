---
title: "switchTab"
source_url: "https://open.dingtalk.com/document/development/jsapi-switch-tab"
namespace: "development"
slug: "jsapi-switch-tab"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 路由 > switchTab"
doc_id: "OF7JPFomYj"
updated_at: "2025-08-27 18:05:10"
---

> Source: https://open.dingtalk.com/document/development/jsapi-switch-tab
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 路由 > switchTab
> Updated: 2025-08-27 18:05:10

# switchTab

调用switchTab，跳转到指定 tabBar 页面，并关闭其他所有非 tabBar 页面。

只能跳转在app.json里配置的tabbar页面，例如app.json中配置了叫”我的“的Tab页面，如下：

```
// app.json
{
  "tabBar": {
    "items": [{
      "pagePath": "user",
      "name": "我的"
    }]
  }
}
```

这样调用switchTab才可以跳转到”我的“这个tab，代码如下：

```
dd.switchTab({
  url: '/user'
})
```

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11539) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `url`（string，必填）：跳转的 tabBar 页面的路径（需在 app.json 的 tabBar 字段定义的页面）。  
    
  > 路径后不能带参数。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.switchTab({
  url: '/user',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
