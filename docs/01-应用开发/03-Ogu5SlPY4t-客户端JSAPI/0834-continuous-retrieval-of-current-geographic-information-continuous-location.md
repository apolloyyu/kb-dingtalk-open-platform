---
title: "连续获取当前地理位置信息（持续定位）"
source_url: "https://open.dingtalk.com/document/development/continuous-retrieval-of-current-geographic-information-continuous-location"
namespace: "development"
slug: "continuous-retrieval-of-current-geographic-information-continuous-location"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 连续获取当前地理位置信息（持续定位）"
doc_id: "YKJijbxEFJ"
updated_at: "2025-09-17 20:56:59"
---

> Source: https://open.dingtalk.com/document/development/continuous-retrieval-of-current-geographic-information-continuous-location
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 连续获取当前地理位置信息（持续定位）
> Updated: 2025-09-17 20:56:59

# 连续获取当前地理位置信息（持续定位）

调用**device.geolocation.start**连续获取当前地理位置信息（持续定位）。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.geolocation.start)在线调试该接口。

## 使用说明

用于对定位精度要求较高以及需要持续更新用户位置的场景，通过持续接收callback方式，获取用户当前的位置信息。连续定位功能，由三个接口组成，开始连续定位(start)、停止连续定位(stop)、以及获取当前定位状态(status)。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.geolocation.start({
    targetAccuracy : Number, // 期望精确度
    iOSDistanceFilter: Number, // 变更感知精度(iOS端参数)
    useCache: Boolean, // 是否使用缓存(Android端参数)
    withReGeocode : Boolean, // 是否返回逆地理信息,默认否
    callBackInterval : Number, //回传时间间隔，ms
    sceneId: String, // 定位场景id,
    onSuccess : function(result) {
        /*  结果同dd.device.geolocation.get */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| targetAccuracy | Number | 期望定位精度半径(单位米)定位结果尽量满足该参数要求，不保证小于该误差，开发者需要读取返回结果的 accuracy 字段校验坐标精度。  **[!NOTE]**  建议按照业务需求设置定位精度，推荐采用200m，可获得较好的精度和较短的响应时长。 |
| iOSDistanceFilter | Number | iOS端位置变更敏感度，单位为m，此值会影响iOS端callback回调速率。 |
| useCache | Boolean | 是否缓存地理位置信息。   - **true**（默认）：设置true，客户端缓存定位的地理位置信息，在缓存期内(分钟)再次定位会返回旧的定位。 - **false**：设置false，不缓存地址位置信息。 |
| withReGeocode | Boolean | 是否需要带有逆地理编码信息。  **[!NOTE]**  该功能需要网络请求，请根据自己的业务场景使用。 |
| callBackInterval | Number | 数据回传最小时间间隔，单位ms。 |
| sceneId | String | 定位场景id。  **[!NOTE]**  对于同一id，不可连续start，否则会报错。不同scenceId互不影响。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| longitude | 经度。 |
| latitude | 纬度。 |
| accuracy | 实际的定位精度半径 (单位米)。 |
| address | 格式化地址，如：北京市朝阳区南磨房镇北京国家广告产业园区。  **[!IMPORTANT]**  如需返回该参数，请使用高德坐标并将**withReGeocode**参数设置为**true**。 |
| province | 省份，如：北京市。  **[!IMPORTANT]**  如需返回该参数，请使用高德坐标并将**withReGeocode**参数设置为**true**。 |
| city | 城市，直辖市会返回空。 |
| district | 行政区，如：朝阳区。 |
| road | 街道，如：西大望路甲12-2号楼。 |
| netType | 当前设备网络类型，如：wifi、3g等。 |
| operatorType | 当前设备使用移动运营商，如：CMCC等。 |
| errorMessage | 返回码描述。 |
| errorCode | 返回码。 |
| isWifiEnabled | 仅Android支持，wifi设置是否开启，不保证已连接上。 |
| isGpsEnabled | 仅Android支持，gps设置是否开启，不保证已连接上。 |
| isFromMock | 仅Android支持，定位返回的经纬度是否是模拟的结果。 |
| provider | 仅Android支持，我们使用的是混合定位，具体定位提供者有wifi、lbs、gps这三种。 |
| isMobileEnabled | 仅Android支持，移动网络是设置是否开启，不保证已连接上。 |
