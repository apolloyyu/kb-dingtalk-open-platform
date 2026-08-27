---
title: "navigateTo"
source_url: "https://open.dingtalk.com/document/development/jsapi-navigate-to"
namespace: "development"
slug: "jsapi-navigate-to"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 路由 > navigateTo"
doc_id: "FgILyAeJrE"
updated_at: "2025-08-27 18:05:08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-navigate-to
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 路由 > navigateTo
> Updated: 2025-08-27 18:05:08

# navigateTo

调用navigateTo，跳转到应用内的某个指定页面，并保留当前页面。可以使用navigateBack返回到原来页面。

> 页面最大深度为5，即可连续调用 5 次 navigateTo。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10033) |

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

- `url`（string，必填）：需要跳转的应用内非 tabBar 的目标页面路径，路径后可以带参数。  
    
    
  > 参数规则如下：路径与参数之间使用“?”分隔，参数键与参数值用=相连，不同参数必须用”&“分隔；如 `path?key1=value1&key2=value2`。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.navigateTo({
  url: '/demo/my?id=233',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
