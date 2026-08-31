---
title: "MapContext.getRegion"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-get-region"
namespace: "development"
slug: "jsapi-map-context-get-region"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.getRegion"
doc_id: "5O60Zv74MZ"
updated_at: "2025-08-27 18:05:55"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-get-region
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > MapContext.getRegion
> Updated: 2025-08-27 18:05:55

# MapContext.getRegion

使用MapContext.getRegion可获取地图东北角、西南角的经纬度，从而获取地图整体的视野范围。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4554199951/p163574.png)

### 重要

IDE 模拟器暂不支持模拟，请以真机调试效果为准。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10128) |

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

- `northeast`（object，必填）：地图的东北角经纬度。
- `northeast.latitude`（number，必填）：经度
- `northeast.longitude`（number，必填）：纬度
- `southwest`（object，必填）：地图的西南角经纬度。
- `southwest.latitude`（number，必填）：经度
- `southwest.longitude`（number，必填）：纬度

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.getRegion({
  success: (res) => {
    const { northeast, southwest } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "northeast": {
    "latitude": 39.89839488008665,
    "longitude": 116.38624861836435
  },
  "southwest": {
    "latitude": 39.90159974373447,
    "longitude": 116.39376148581508
  }
}
```
