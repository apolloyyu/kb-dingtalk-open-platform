---
title: "MapContext.changeMarkers"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-change-markers"
namespace: "development"
slug: "jsapi-map-context-change-markers"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.changeMarkers"
doc_id: "MFlXqkWusT"
updated_at: "2025-08-27 18:05:53"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-change-markers
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > MapContext.changeMarkers
> Updated: 2025-08-27 18:05:53

# MapContext.changeMarkers

使用MapContext.changeMarkers用于添加、删除、更新指定的标记（marker）。

## 兼容性

使用 dd.canIUse('createMapContext.return.changeMarkers')进行可用性判断。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10123) |

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

- `add`（array）：需要添加的 marker 数组。
- `add[].id`（number，必填）：标记id
- `add[].width`（number，必填）：宽度
- `add[].height`（number，必填）：高度
- `add[].iconPath`（string，必填）：图标文件路径
- `add[].latitude`（number，必填）：经度
- `add[].longitude`（number，必填）：纬度
- `remove`（array）：需要删除的 marker 数组。
- `remove[].id`（number，必填）：标记id
- `remove[].width`（number，必填）：宽度
- `remove[].height`（number，必填）：高度
- `remove[].iconPath`（string，必填）：图标文件路径
- `remove[].latitude`（number，必填）：经度
- `remove[].longitude`（number，必填）：纬度
- `update`（array）：需要更新的 marker 数组。
- `update[].id`（number，必填）：标记id
- `update[].width`（number，必填）：宽度
- `update[].height`（number，必填）：高度
- `update[].iconPath`（string，必填）：图标文件路径
- `update[].latitude`（number，必填）：经度
- `update[].longitude`（number，必填）：纬度

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 新增标记

```
const mapContext = dd.createMapContext();

mapContext.changeMarkers({
  add: [
    {
      iconPath: '/image/green_tri.png',
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
    },
    {
      iconPath: '/image/green_tri.png',
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
      customCallout: {
        type: 1,
        time: '1',
      },
      fixedPoint: {
        originX: 400,
        originY: 400,
      },
      iconAppendStr: '黄龙时代广场黄龙时代广场黄龙时代广场黄龙时代广场test',
    },
  ],
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```

### 修改标记

```
const mapContext = dd.createMapContext();

mapContext.changeMarkers({
  update: [
    {
      iconPath: '/image/green_tri.png',
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
    },
    {
      iconPath: '/image/green_tri.png',
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
      customCallout: { type: 1, time: '1' },
      fixedPoint: { originX: 400, originY: 400 },
      iconAppendStr: '黄龙时代广场黄龙时代广场黄龙时代广场黄龙时代广场test',
    },
  ],
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```

### 删除标记

```
const mapContext = dd.createMapContext();

mapContext.changeMarkers({
  remove: [
    {
      iconPath: '/image/green_tri.png',
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
    },
    {
      iconPath: '/image/green_tri.png',
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
      customCallout: { type: 1, time: '1' },
      fixedPoint: { originX: 400, originY: 400 },
      iconAppendStr: '黄龙时代广场黄龙时代广场黄龙时代广场黄龙时代广场test',
    },
  ],
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
