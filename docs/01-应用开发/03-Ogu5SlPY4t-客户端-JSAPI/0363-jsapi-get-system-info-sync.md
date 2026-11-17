---
title: "getSystemInfoSync"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-system-info-sync"
namespace: "development"
slug: "jsapi-get-system-info-sync"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 系统信息 > getSystemInfoSync"
doc_id: "OXlPc1D9PA"
updated_at: "2025-08-27 18:07:30"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-system-info-sync
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 系统信息 > getSystemInfoSync
> Updated: 2025-08-27 18:07:30

# getSystemInfoSync

调用dd.getSystemInfoSync获取手机系统信息的同步接口。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10141) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `model`（string）：手机型号。
- `app`（string，必填）：应用名。
- `brand`（string，必填）：手机品牌。
- `pixelRatio`（number）：设备像素比。
- `windowWidth`（number）：窗口宽度。
- `windowHeight`（number）：窗口高度。
- `language`（string）：钉钉设置的语言。
- `version`（string）：钉钉版本号。
- `storage`（string）：设备磁盘容量。
- `currentBattery`（string）：当前电量百分比。
- `system`（string）：系统版本。
- `paltform`（string）：系统名。
- `screenWidth`（number）：屏幕宽度。
- `screenHeight`（number）：屏幕高度。
- `fontSizeSetting`（number）：用户设置字体大小。
- `isIphoneXSeries`（boolean，必填）：是否是iphone手机。
- `lowPowerMode`（boolean，必填）：是否是低电量模式。
- `orientation`（number，必填）：\* 0：竖屏  
  \* 1： 横屏
- `titleBarHeight`（number，必填）：标题栏高度。
- `statusBarHeight`（number，必填）：状态栏高度。

## **示例****代码**

### 默认出入参

```
const res = dd.getSystemInfoSync();
const {
  app,
  brand,
  model,
  system,
  storage,
  version,
  language,
  paltform,
  pixelRatio,
  orientation,
  screenWidth,
  windowWidth,
  lowPowerMode,
  screenHeight,
  windowHeight,
  currentBattery,
  titleBarHeight,
  fontSizeSetting,
  isIphoneXSeries,
  statusBarHeight,
} = res;
```

返回对象示例：

```
{
  "app": "DingTalk",
  "brand": "iPhone",
  "model": "iPhone13,2",
  "system": "16.1.1",
  "storage": "119.09 GB",
  "version": "7.0.1",
  "language": "zh_CN",
  "paltform": "iOS",
  "pixelRatio": 3,
  "orientation": 0,
  "screenWidth": 390,
  "windowWidth": 390,
  "lowPowerMode": false,
  "screenHeight": 844,
  "windowHeight": 753,
  "currentBattery": "84%",
  "titleBarHeight": 44,
  "fontSizeSetting": 17,
  "isIphoneXSeries": true,
  "statusBarHeight": 47
}
```
