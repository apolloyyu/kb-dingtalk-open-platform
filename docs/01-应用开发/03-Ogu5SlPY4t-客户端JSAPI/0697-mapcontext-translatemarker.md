---
title: "平移点标记(translateMarker)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-translatemarker"
namespace: "development"
slug: "mapcontext-translatemarker"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 平移点标记(translateMarker)"
doc_id: "3NO3YdDg7U"
updated_at: "2025-09-17 21:00:45"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-translatemarker
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 平移点标记(translateMarker)
> Updated: 2025-09-17 21:00:45

# 平移点标记(translateMarker)

**MapContext.translateMarker**用于平移点标记（marker）。

对同一个 markerId，在 translateMarker 没调用 animationEnd 之前再次调动无法生效，需要在调用 animationEnd 之后再调用一次动画，方才有效。

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.translateMarker({
    markerId:0, // 必填
    destination:{
        longitude:120.2,latitude:30.3 // 必填
    },
    autoRotate:true, // 选填，默认true
    rotate:90,  // 选填，在autoRotate为false的情况下才有效，不填默认是0
    duration:900,  // 选填，单位ms，默认1000 ms
    animationEnd() {
        console.log('animation end')
      }   //function 动画结束回调    
});
```

## **入参**

入参为 Object 类型，属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| markerId | Number | 是 | 指定 marker。 |
| destination | Object | 是 | 指定 marker 移动到的目标点。 |
| autoRotate | Boolean | 否 | 移动过程中是否自动旋转marker。 |
| rotate | Number | 否 | marker 的旋转角度.  **默认值**：0。 |
| duration | Number | 否 | 动画持续时长。  **默认值**：1000。 |
| animationEnd | Function | 否 | 动画结束回调函数。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数（调用成功、失败都会执行）。 |

**destination 的结构**

| **属性** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| longitude | Number | 是 | 经度。 |
| latitude | Number | 是 | 纬度。 |

## **兼容性**

使用 **dd.canIUse('createMapContext.return.****translateMarker****')** 进行可用性判断。
