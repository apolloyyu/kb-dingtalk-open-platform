---
title: "setNavigationLeft"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-navigation-left"
namespace: "development"
slug: "jsapi-set-navigation-left"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 导航栏 > setNavigationLeft"
doc_id: "OcMlwIvSs0"
updated_at: "2025-08-27 18:05:02"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-navigation-left
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 导航栏 > setNavigationLeft
> Updated: 2025-08-27 18:05:02

# setNavigationLeft

调用setNavigationLeft设置左侧导航按钮文本。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7605834061/p177959.png)

如图设置左侧操作区的文案和行为

PC端：只在SlidePanel里起作用

PC端左侧按钮点击事件，添加监听回调函数

```
//添加监听回调函数
dd.on('leftBtnClick', handleFn);
```

左侧按钮点击事件，移除相应handleFn的监听回调函数

```
//移除相应handleFn的监听回调函数
dd.off('leftBtnClick', handleFn);
```

该API在Android、iOS端半屏容器中不予支持。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11610) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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

- `text`（string，必填）：控制显示文本，空字符串表示显示默认文本。
- `control`（boolean）：是否控制点击事件(PC端不可用)：   
   \* true：控制   
   \* false（默认）：不控制

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.setNavigationLeft({
  text: '返回',
  control: true,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
