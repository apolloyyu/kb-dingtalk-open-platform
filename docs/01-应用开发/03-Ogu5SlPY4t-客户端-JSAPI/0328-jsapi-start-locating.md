---
title: "startLocating"
source_url: "https://open.dingtalk.com/document/development/jsapi-start-locating"
namespace: "development"
slug: "jsapi-start-locating"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "位置服务 > startLocating"
doc_id: "WgHtLWQkdL"
updated_at: "2025-08-27 18:07:16"
---

> Source: https://open.dingtalk.com/document/development/jsapi-start-locating
> Path: 应用开发 / 客户端 JSAPI / 位置服务 > startLocating
> Updated: 2025-08-27 18:07:16

# startLocating

调用startLocating，连续获取当前地理位置信息（持续定位）。

用于对定位精度要求较高以及需要持续更新用户位置的场景，通过持续接收callback方式，获取用户当前的位置信息。连续定位功能，由三个接口组成，开始连续定位(startLocating)、停止连续定位(stopLocating)、以及获取当前定位状态(getLocatingStatus)。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11678) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11678) |

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

- `targetAccuracy`（number，必填）：期望定位精度半径(单位米)定位结果尽量满足该参数要求，不保证小于该误差，开发者需要读取返回结果的 accuracy 字段校验坐标精度。  
    
  > 建议按照业务需求设置定位精度，推荐采用200m，可获得较好的精度和较短的响应时长。
- `iOSDistanceFilter`（number，必填）：iOS端位置变更敏感度，单位为m，此值会影响iOS端callback回调速率。  
    
  > iOS端参数。
- `useCache`（boolean，必填）：是否使用缓存：  
    
  \* true：默认值，设置true，客户端缓存定位的地理位置信息，在缓存期内(分钟)再次定位会返回旧的定位。  
  \* false：设置false，不缓存地址位置信息。  
    
  > Android端参数。
- `withReGeocode`（boolean，必填）：是否需要带有逆地理编码信息。  
    
  > \* 默认为false。  
  > \* 该功能需要网络请求，请根据自己的业务场景使用。
- `callBackInterval`（number，必填）：回传时间间隔，单位ms。
- `sceneId`（string，必填）：定位场景id。  
    
  > 对于同一id，不可连续start，否则会报错。不同scenceId互不影响。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `longitude`（number）：经度。
- `latitude`（number）：纬度。
- `accuracy`（number）：实际的定位精度半径 (单位米)。
- `address`（string）：格式化地址。  
    
  > 如需返回该参数，请使用高德坐标并将\*\*withReGeocode\*\*参数设置为\*\*true\*\*。
- `province`（string）：省份。  
    
  > 如需返回该参数，请使用高德坐标并将\*\*withReGeocode\*\*参数设置为\*\*true\*\*。
- `city`（string）：城市。  
    
  > 直辖市会返回空。
- `district`（string）：行政区。
- `road`（string）：街道。
- `netType`（string）：当前设备网络类型。
- `operatorType`（string）：当前设备使用移动运营商。
- `locationType`（number）：位置类型：  
    
  \* 1：GPS定位结果  
  \* 2：返回上次定位结果  
  \* 3：缓存定位结果   
  \* 4：Wifi定位结果  
  \* 5：基站定位结果
- `errorMessage`（string）：返回码描述。
- `errorCode`（number）：返回码。
- `isWifiEnabled`（boolean）：wifi设置是否开启，不保证已连接上。  
    
  > 仅Android支持。
- `isGpsEnabled`（boolean）：gps设置是否开启，不保证已连接上。  
    
  > 仅Android支持。
- `isFromMock`（boolean）：定位返回的经纬度是否是模拟的结果。  
    
  > 仅Android支持。
- `provider`（string）：混合定位，具体定位提供者有wifi、lbs、gps这三种。
- `isMobileEnabled`（boolean）：移动网络是设置是否开启，不保证已连接上。  
    
  > 仅Android支持。

## **示例****代码**

### 默认出入参

```
dd.startLocating({
  sceneId: '****',
  useCache: true,
  withReGeocode: fal,
  targetAccuracy: 200,
  callBackInterval: 1000,
  iOSDistanceFilter: Number,
  success: (res) => {
    const {
      city,
      road,
      address,
      netType,
      accuracy,
      district,
      latitude,
      provider,
      province,
      errorCode,
      longitude,
      isFromMock,
      errorMessage,
      isGpsEnabled,
      locationType,
      operatorType,
      isWifiEnabled,
      isMobileEnabled,
    } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{"loc":{"start":{"line":1,"column":165},"end":{"line":1,"column":168}},"codeFrame":"> 1 | {city:'北京市',road:'西大望路甲12-2号楼。',address:'如：北京市朝阳区南磨房镇北京国家广告产业园区。',netType:'wifi',accuracy:200,district:'朝阳区',latitude:119.,provider:'wifi',province:'北京市',errorCode:返回码,longitude:100,isFromMock:true,errorMessage:'返回码描述',isGpsEnabled:true,locationType:1,operatorType:'CMCC',isWifiEnabled:true,isMobileEnabled:true,}\n    |                                                                                                                                                                     ^^^"}
```
