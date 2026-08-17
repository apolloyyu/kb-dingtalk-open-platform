---
title: "获取地图整体的视野范围(getRegion)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-getregion"
namespace: "development"
slug: "mapcontext-getregion"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 获取地图整体的视野范围(getRegion)"
doc_id: "JDaJMRZSYf"
updated_at: "2025-09-17 21:00:41"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-getregion
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 获取地图整体的视野范围(getRegion)
> Updated: 2025-09-17 21:00:41

# 获取地图整体的视野范围(getRegion)

使用**MapContext.getRegion**可获取地图东北角、西南角的经纬度，从而获取地图整体的视野范围。

![original ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4554199951/p163574.png)

> **[!IMPORTANT]**
>
> IDE 模拟器暂不支持模拟，请以真机调试效果为准。

## 示例代码

```
// .js
this.mapCtx = dd.createMapContext('map');
this.mapCtx.getRegion({
  success: res => {
    console.log(res);
  }
});
```

## **success 返回值**

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| southwest | Object | 地图的西南角经纬度。 |
| northeast | Object | 地图的东北角经纬度。 |

**返回值示例**

```
{
  "northeast":{"latitude":39.90159974373447,"longitude":116.39376148581508},
  "southwest":{"latitude":39.89839488008665,"longitude":116.38624861836435}
}
```

## **兼容性**

使用 **dd.canIUse('createMapContext.return.****getRegion****')**进行可用性判断。
