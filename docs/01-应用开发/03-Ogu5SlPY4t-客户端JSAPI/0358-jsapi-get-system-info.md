---
title: "getSystemInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-system-info"
namespace: "development"
slug: "jsapi-get-system-info"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 系统信息 > getSystemInfo"
doc_id: "BtGMGTHova"
updated_at: "2025-10-21 16:36:10"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-system-info
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 系统信息 > getSystemInfo
> Updated: 2025-10-21 16:36:10

# getSystemInfo

调用getSystemInfo，获取系统信息。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10140) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 7.0.0 | 7.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10140) |

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
    
  > 桌面端不支持该字段。
- `app`（string，必填）：应用名。
- `brand`（string，必填）：手机品牌。  
    
  > 桌面端不支持该字段。
- `pixelRatio`（number）：设备像素比。
- `windowWidth`（number）：窗口宽度。
- `windowHeight`（number）：窗口高度。
- `language`（string）：钉钉设置的语言。  
  > 仅小程序应用返回。
- `version`（string）：系统版本号。  
    
  > 小程序全局 API 调用时为钉钉版本号
- `storage`（string）：设备磁盘容量。
- `currentBattery`（string）：当前电量百分比。  
    
  > 桌面端不支持该字段。
- `system`（string）：系统版本。
- `platform`（string）：系统名。
- `screenWidth`（number）：屏幕宽度。
- `screenHeight`（number）：屏幕高度。
- `fontSizeSetting`（number）：用户设置字体大小。
- `orientation`（number，必填）：\* 0：竖屏  
  \* 1： 横屏  
    
  > 桌面端不支持该字段。
- `titleBarHeight`（number，必填）：标题栏高度。  
    
  > 桌面端不支持该字段。
- `statusBarHeight`（number，必填）：状态栏高度。  
    
  > 桌面端不支持该字段。

## **示例****代码**

### 默认出入参

```
dd.getSystemInfo({
  success: (res) => {
    const {
      app,
      brand,
      model,
      system,
      storage,
      version,
      language,
      platform,
      pixelRatio,
      orientation,
      screenWidth,
      windowWidth,
      screenHeight,
      windowHeight,
      currentBattery,
      titleBarHeight,
      fontSizeSetting,
      statusBarHeight,
    } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "app": "DingTalk",
  "brand": "iPhone",
  "model": "iPhone13,2",
  "system": "16.1.1",
  "storage": "119.09 GB",
  "version": "15",
  "language": "zh_CN",
  "platform": "iOS",
  "pixelRatio": 3,
  "orientation": 0,
  "screenWidth": 390,
  "windowWidth": 390,
  "screenHeight": 844,
  "windowHeight": 753,
  "currentBattery": "84%",
  "titleBarHeight": 44,
  "fontSizeSetting": 17,
  "statusBarHeight": 47
}
```
