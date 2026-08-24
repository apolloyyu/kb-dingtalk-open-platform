---
title: "setNavigationIcon"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-navigation-icon"
namespace: "development"
slug: "jsapi-set-navigation-icon"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 导航栏 > setNavigationIcon"
doc_id: "CehfZuH06o"
updated_at: "2025-08-27 18:05:01"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-navigation-icon
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 导航栏 > setNavigationIcon
> Updated: 2025-08-27 18:05:01

# setNavigationIcon

调用setNavigationIcon标题栏添加问号图标。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177931.png)

如图使用该api设置标题边的icon

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11609) |
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

- `showIcon`（boolean，必填）：是否显示icon。
- `iconIndex`（number，必填）：显示的iconIndex，可选值如下图  
    
  ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9025204061/p177951.png)

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.setNavigationIcon({
  showIcon: true,
  iconIndex: 101,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
