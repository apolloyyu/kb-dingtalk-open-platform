---
title: "openPageInWorkBenchForPC"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-page-in-work-bench-for-pc"
namespace: "development"
slug: "jsapi-open-page-in-work-bench-for-pc"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 跳转 > openPageInWorkBenchForPC"
doc_id: "hQbj2PE2J5"
updated_at: "2025-08-27 18:06:31"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-page-in-work-bench-for-pc
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 跳转 > openPageInWorkBenchForPC
> Updated: 2025-08-27 18:06:31

# openPageInWorkBenchForPC

调用openPageInWorkBenchForPC在PC端打开新弹窗页面。

在钉钉电脑客户端工作台的微应用页面内调用本接口，调用效果如下图所示，钉钉客户端会弹出一个弹窗页面，弹窗页面内打开指定的页面地址。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1575492561/p425990.png)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 6.0.8 | 6.0.8 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11694) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `app_url`（string，必填）：弹窗页面的链接地址。
- `app_info`（object）：弹窗页面的配置信息。
- `app_info.app_tab_key`（string，必填）：弹窗页面的Id。
- `app_info.app_active_if_exist`（boolean，必填）：如果弹窗页面存在，是否切换到该页面：  
    
  \* true：切换  
  \* false：不切换
- `app_info.app_refresh_if_exist`（boolean，必填）：如果弹窗页面存在，是否刷新该页面：  
    
  \* true：刷新  
  \* false：不刷新

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `body`（boolean，必填）：调用成功时，返回结果为{"body":true}。

## **示例****代码**

### 默认出入参

```
dd.openPageInWorkBenchForPC({
  app_url: 'https://www.dingtalk.com',
  app_info: {
    app_tab_key: '123',
    app_active_if_exist: true,
    app_refresh_if_exist: true,
  },
  success: (res) => {
    const { body } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "body": true }
```
