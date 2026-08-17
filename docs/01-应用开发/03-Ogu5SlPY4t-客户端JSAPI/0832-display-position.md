---
title: "展示位置"
source_url: "https://open.dingtalk.com/document/development/display-position"
namespace: "development"
slug: "display-position"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 展示位置"
doc_id: "KEbV36thTE"
updated_at: "2025-09-17 20:56:57"
---

> Source: https://open.dingtalk.com/document/development/display-position
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 展示位置
> Updated: 2025-09-17 20:56:57

# 展示位置

调用**biz.map.view**展示传入的经纬度位置。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.map.view)在线调试该接口。

## 使用说明

唤起地图页面，展示传入的经纬度位置。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.map.view({
    latitude: 39.903578, // 纬度
    longitude: 116.473565, // 经度
    title: "北京国家广告产业园" // 地址/POI名称
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| latitude | Number | 需要和longitude组合成合法经纬度，高德坐标。 |
| longitude | Number | 需要和latitude组合成合法经纬度，高德坐标。 |
| title | String | 在地图锚点气泡显示的文案。 |
