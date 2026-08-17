---
title: "dd.canIUse"
source_url: "https://open.dingtalk.com/document/development/dd-caniuse"
namespace: "development"
slug: "dd-caniuse"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > dd.canIUse"
doc_id: "Vk5cfGvDff"
updated_at: "2025-09-17 20:58:41"
---

> Source: https://open.dingtalk.com/document/development/dd-caniuse
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > dd.canIUse
> Updated: 2025-09-17 20:58:41

# dd.canIUse

使用**dd.canIUse**接口判断小程序的 API、入参或返回值、组件、属性等在当前钉钉版本是否支持。

## 示例代码

```
// 新增 API 是否可用
dd.canIUse('editPicture')
// API 新增属性是否可用
dd.canIUse('getLocation.object.type')
// API 返回值新增属性是否可用
dd.canIUse('getSystemInfo.return.brand')
// 新增组件「关注生活号」是否可用
dd.canIUse('open-avatar')
// 组件新增属性值是否可用
dd.canIUse('button.open-type.share')
```

## **入参**

参数使用 `${API}.${type}.${param}.${option}` 或者 `${component}.${attribute}.${option}` 方式来调用。

| **类型** | 说明 |
| --- | --- |
| API | 表示 API 的名称，不包括 dd. 的名称。  例如：开发者希望判断`dd.getFileInfo`，只需传入**getFileInfo**。 |
| type | 取值 object/return/callback表示 API 的判断类型。 |
| param | 表示参数的某一个属性名。 |
| option | 表示参数属性的具体属性值。 |
| component | 表示组件名称。 |
| attribute | 表示组件属性名。 |
| option | 表示组件属性值。 |

## **返****回值**

为 **Boolean** 类型，表示是否支持。
