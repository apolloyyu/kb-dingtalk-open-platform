---
title: "showCallMenu"
source_url: "https://open.dingtalk.com/document/development/jsapi-show-call-menu"
namespace: "development"
slug: "jsapi-show-call-menu"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "办公电话 > showCallMenu"
doc_id: "iZq0MOfCA5"
updated_at: "2025-08-27 18:08:38"
---

> Source: https://open.dingtalk.com/document/development/jsapi-show-call-menu
> Path: 应用开发 / 客户端 JSAPI / 办公电话 > showCallMenu
> Updated: 2025-08-27 18:08:38

# showCallMenu

调用dd.showCallMenu唤起拨打电话菜单。

调用效果如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1200805061/p163590.png)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10159) |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10159) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `phoneNumber`（string，必填）：期望拨打的电话号码。
- `showDingCall`（boolean）：是否显示钉钉电话。
- `code`（string）：国家代号，中国是+86。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.showCallMenu({
  code: '+86',
  phoneNumber: '13800000000',
  showDingCall: false,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
