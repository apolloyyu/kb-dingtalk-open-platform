---
title: "地图定位"
source_url: "https://open.dingtalk.com/document/development/map-positioning"
namespace: "development"
slug: "map-positioning"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 地图定位"
doc_id: "ZIqoYM12Ap"
updated_at: "2025-09-17 20:56:56"
---

> Source: https://open.dingtalk.com/document/development/map-positioning
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 地图定位
> Updated: 2025-09-17 20:56:56

# 地图定位

调用**biz.map.locate**地图定位。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.map.locate)在线调试该接口。

## 使用说明

唤起地图页面，获取设备位置及设备附近的POI信息；若传入的经纬度合法，则显示当前的位置信息及其附近的POI信息。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.map.locate({
    latitude: 39.903578, // 纬度，非必须
    longitude: 116.473565, // 经度，非必须
    scope: 500, // 限制搜索POI的范围；设备位置为中心，scope为搜索半径
    onSuccess: function (result) {
        /* result 结构 */
        {
            province: 'xxx', // POI所在省会，可能为空
            provinceCode: 'xxx', // POI所在省会编码，可能为空
            city: 'xxx', // POI所在城市，可能为空
            cityCode: 'xxx', // POI所在城市编码，可能为空
            adName: 'xxx', // POI所在区名称，可能为空
            adCode: 'xxx', // POI所在区编码，可能为空
            distance: 'xxx', // POI与设备位置的距离
            postCode: 'xxx', // POI的邮编，可能为空
            snippet: 'xxx', // POI的街道地址，可能为空
            title: 'xxx', // POI的名称
            latitude: 39.903578, // POI的纬度
            longitude: 116.473565, // POI的经度
        }
    },
    onFail: function (err) {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| latitude | Number | 非必须，需要和longitude组合成合法经纬度，高德坐标。 |
| longitude | Number | 非必须，需要和latitude组合成合法经纬度，高德坐标。 |
| scope | Number | 搜索范围，建议不要设置过低，否则可能搜索不到POI。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| longitude | POI的经度，高德坐标。 |
| latitude | POI的纬度，高德坐标。 |
| title | POI的名称。 |
| province | POI所在省会，可能为空。 |
| provinceCode | POI所在省会编码，可能为空。 |
| city | POI所在城市，可能为空。 |
| cityCode | POI所在城市的编码，可能为空。 |
| adName | POI所在区，可能为空。 |
| adCode | POI所在区的编码，可能为空。 |
| postCode | POI的邮编，可能为空。 |
| snippet | POI的街道地址，可能为空。 |
