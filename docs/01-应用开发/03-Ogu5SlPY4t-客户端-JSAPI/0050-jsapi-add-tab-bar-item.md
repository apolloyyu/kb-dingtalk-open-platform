---
title: "addTabBarItem"
source_url: "https://open.dingtalk.com/document/development/jsapi-add-tab-bar-item"
namespace: "development"
slug: "jsapi-add-tab-bar-item"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > TabBar > addTabBarItem"
doc_id: "vlRGzprZEg"
updated_at: "2025-08-27 18:05:03"
---

> Source: https://open.dingtalk.com/document/development/jsapi-add-tab-bar-item
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > TabBar > addTabBarItem
> Updated: 2025-08-27 18:05:03

# addTabBarItem

调用addTabBarItem，添加tabBar页面。

使用该接口请注意：

- addTabBarItem最多调用90次。
- addTabBarItem 调用时，要保证当前小程序展示的是TabBar上的页面；否则调用会报错，错误码 11。
- addTabBarItem 不可对主 tabBar 页面进行替换。
- tabBar 最多为 5个。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10058) |

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

- `name`（string，必填）：tab标题。
- `index`（number，必填）：tem插入位置，原位置的页面将后移一个位置，从 0 开始。
- `icon`（string）：图标。
- `activeIcon`（string）：选中时的图标。
- `pagePath`（string，必填）：TabItem对应的页面路径，需要配置在小程序配置文件中。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.addTabBarItem({
  icon: '/image/icon-hom.png',
  name: '日志',
  index: 1,
  pagePath: 'pages/logs/logs',
  activeIcon: '/image/icon-home-selected.png',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
