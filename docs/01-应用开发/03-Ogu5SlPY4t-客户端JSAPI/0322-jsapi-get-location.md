---
title: "getLocation"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-location"
namespace: "development"
slug: "jsapi-get-location"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "位置服务 > getLocation"
doc_id: "Sq9R155LMz"
updated_at: "2025-08-27 18:07:13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-location
> Path: 应用开发 / 客户端JSAPI / 位置服务 > getLocation
> Updated: 2025-08-27 18:07:13

# getLocation

调用dd.getLocation获取用户当前的地理位置信息。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10256) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10256) |

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

- `targetAccuracy`（string）：期望定位精度半径(单位米)，定位结果尽量满足该参数要求，但是不一定能保证小于该误差，开发者需要读取返回结果的 accuracy 字段校验坐标精度。  
    
  > \* 建议按照业务需求设置定位精度，推荐采用200m，可获得较好的精度和较短的响应时长。  
  > \* H5应用调用参数。
- `coordinate`（string）：\* 1：获取高德坐标  
  \* 0：获取标准坐标  
    
  > H5应用调用参数。
- `withReGeocode`（boolean）：是否需要带有逆地理编码信息。  
    
  > \* H5应用调用参数。  
  > \* 该功能需要网络请求，请根据自己的业务场景使用。
- `useCache`（boolean）：是否缓存地理位置信息，默认是true。   
    
  > \* H5应用调用参数。  
  > \* 若为true，客户端会对定位的地理位置信息缓存，在缓存期内 (2分钟) 再次定位会返回旧的定位。
- `cacheTimeout`（number）：缓存过期时间，单位为秒。  
    
  未过期的缓存数据会直接返回（速度快），缓存过期会重新定位（速度慢）。  
    
  \*\*默认值\*\*：30s  
    
  > 小程序应用调用参数。
- `type`（number）：获取经纬度和详细到区县级别的逆地理编码数据：  
  \* 0：获取经纬度  
  \* 1：默认  
    
  > 小程序应用调用参数。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `longitude`（string，必填）：经度，范围为 -180~180，负数表示西经。
- `latitude`（string，必填）：纬度，范围为 -90~90，负数表示南纬。
- `accuracy`（string，必填）：精确度，单位 米。
- `province`（string，必填）：省份，type>0生效。
- `city`（string，必填）：城市，type>0生效。
- `address`（string，必填）：格式化地址，type>0生效。如：北京市朝阳区南磨房镇北京国家广告产业园区。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 11 | 请确认定位相关权限已开启 |
| 12 | 网络异常，请稍后再试 |
| 13 | 定位失败，请稍后再试 |
| 14 | 业务定位超时 |

## **示例****代码**

### 默认出入参

```
dd.getLocation({
  type: 1,
  useCache: true,
  coordinate: '1',
  cacheTimeout: 20,
  withReGeocode: true,
  targetAccuracy: '200',
  success: (res) => {
    const { city, address, accuracy, latitude, province, longitude } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "city": "杭州市",
  "address": "钱塘区二十四号大街353号",
  "accuracy": "200",
  "latitude": "38.963035",
  "province": "浙江省",
  "longitude": "117.451692"
}
```
