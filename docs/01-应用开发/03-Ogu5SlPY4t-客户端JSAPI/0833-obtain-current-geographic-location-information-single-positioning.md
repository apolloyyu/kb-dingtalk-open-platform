---
title: "获取当前地理位置信息（单次定位）"
source_url: "https://open.dingtalk.com/document/development/obtain-current-geographic-location-information-single-positioning"
namespace: "development"
slug: "obtain-current-geographic-location-information-single-positioning"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 获取当前地理位置信息（单次定位）"
doc_id: "T0EI4A00fr"
updated_at: "2025-09-17 20:56:58"
---

> Source: https://open.dingtalk.com/document/development/obtain-current-geographic-location-information-single-positioning
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 获取当前地理位置信息（单次定位）
> Updated: 2025-09-17 20:56:58

# 获取当前地理位置信息（单次定位）

调用**device.geolocation.get**获取当前地理位置信息（单次定位）。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.geolocation.get)在线调试该接口。

## 使用说明

Android客户端返回坐标是高德坐标；

iOS客户端2.7.6及以后版本支持返回高德坐标；iOS客户端低于2.7.6版本仅支持返回标准坐标，如需使用高德坐标，可对返回的坐标做转换，具体请参考[坐标转换APIDemo演示页面](http://lbs.amap.com/api/javascript-api/example/p/1602-2/)。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.geolocation.get({
    targetAccuracy : Number,
    coordinate : Number,
    withReGeocode : Boolean,
    useCache:true, //默认是true，如果需要频繁获取地理位置，请设置false
    onSuccess : function(result) {
        /* 高德坐标 result 结构
        {
            longitude : Number,
            latitude : Number,
            accuracy : Number,
            address : String,
            province : String,
            city : String,
            district : String,
            road : String,
            netType : String,
            operatorType : String,
            locationType：1,
            errorMessage : String,
            errorCode : Number,
            isWifiEnabled : Boolean,
            isGpsEnabled : Boolean,
            isFromMock : Boolean,
            provider : wifi|lbs|gps,
            isMobileEnabled : Boolean
        }
        */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| targetAccuracy | Number | 期望定位精度半径(单位米)，定位结果尽量满足该参数要求，但是不一定能保证小于该误差，开发者需要读取返回结果的 accuracy 字段校验坐标精度。  **[!NOTE]**  建议按照业务需求设置定位精度，推荐采用200m，可获得较好的精度和较短的响应时长。 |
| coordinate | Number | - **1**：获取高德坐标 - **0**：获取标准坐标   **[!NOTE]**  推荐使用高德坐标，标准坐标没有 **address**字段。 |
| withReGeocode | Boolean | 是否需要带有逆地理编码信息。  **[!NOTE]**  该功能需要网络请求，请根据自己的业务场景使用。 |
| useCache | Boolean | 是否缓存地理位置信息。默认是**true**。  如果为**true**，客户端会对定位的地理位置信息缓存，在缓存期内 (2分钟) 再次定位会返回旧的定位。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| longitude | 经度。 |
| latitude | 纬度。 |
| accuracy | 实际的定位精度半径 (单位米)。 |
| address | 格式化地址，如：北京市朝阳区南磨房镇北京国家广告产业园区。  **[!IMPORTANT]**  如需返回该参数，请使用高德坐标并将**withReGeocode**参数设置为**true**。 |
| province | 省份，如：北京市。  **[!IMPORTANT]**  如需返回该参数，请使用高德坐标并将**withReGeocode**参数设置为**true**。 |
| city | 城市，如：北京市。 |
| district | 行政区，如：朝阳区。 |
| road | 街道，如：西大望路甲12-2号楼。 |
| netType | 当前设备网络类型，如：wifi、3g等。 |
| operatorType | 当前设备使用移动运营商，如：CMCC等。 |
| locationType | 定位来源。   - 1：GPS定位结果 - 2：返回上次定位结果 - 3：缓存定位结果 - 4：Wifi定位结果 - 5：基站定位结果 |
| errorMessage | 返回码描述。 |
| errorCode | 返回码。 |
| isWifiEnabled | 仅Android支持，wifi设置是否开启，不保证已连接上。 |
| isGpsEnabled | 仅Android支持，gps设置是否开启，不保证已连接上。 |
| isFromMock | 仅Android支持，定位返回的经纬度是否是模拟的结果。 |
| provider | 仅Android支持，我们使用的是混合定位，具体定位提供者有wifi、lbs、gps这三种。 |
| isMobileEnabled | 仅Android支持，移动网络是设置是否开启，不保证已连接上。 |
