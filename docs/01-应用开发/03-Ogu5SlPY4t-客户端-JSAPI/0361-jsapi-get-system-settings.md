---
title: "getSystemSettings"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-system-settings"
namespace: "development"
slug: "jsapi-get-system-settings"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 系统信息 > getSystemSettings"
doc_id: "rbk6wZ0nO0"
updated_at: "2025-08-27 18:07:30"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-system-settings
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 系统信息 > getSystemSettings
> Updated: 2025-08-27 18:07:30

# getSystemSettings

调用getSystemSettings，打开系统设置。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 4.6.36 | 6.3.15 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11671) |
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

- `action`（string）：Android系统中action的概念。  
  例如：\*\*android.settings.BLUETOOTH\_SETTINGS\*\*：打开蓝牙设置页面  
  更多action参考[详情](https://developer.android.com/reference/android/provider/Settings?spm=ding\_open\_doc.document.0.0.51e94a97hKpRAM)。  
    
  > 仅Android系统需要填写。
- `param`（string）：Android系统中跳转系统应用所需的extra参数。  
    
  > 仅Android系统需要填写。
- `data`（string）：Android系统中跳转系统应用所需的data参数。  
    
  > 仅Android系统需要填写。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.getSystemSettings({
  data: 'data param',
  param: '"extended data',
  action: 'android.settings.BLUETOOTH_SETTINGS',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
