---
title: "map 地图"
source_url: "https://open.dingtalk.com/document/development/mini-app-map-map-1"
namespace: "development"
slug: "mini-app-map-map-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 地图 > map 地图"
doc_id: "THcEOU2GvC"
updated_at: "2025-09-17 20:58:33"
---

> Source: https://open.dingtalk.com/document/development/mini-app-map-map-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 地图 > map 地图
> Updated: 2025-09-17 20:58:33

# map 地图

本文介绍地图组件的使用。

同一个页面需要展示多个 map 组件时，需要使用不同的 ID 。

map 组件是由客户端创建的原生组件，可以通过 **dd.canIUse('inPageRenderType.map')** 判断当前 map 组件是否支持同层渲染判断。支持同层渲染时，map 组件可被其他组件覆盖，否则原生组件的层级是最高的，页面中的其他组件无论设置 z-index 为多少，都无法在原生组件之上。

**扫码体验**

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6154199951/p163531.png)

## 注意事项

- 目前只支持高德地图 style 。
- 请勿在[scroll-view 可滚动视图区域](https://open.dingtalk.com/document/orgapp/scroll-view-the-scrollable-area)中使用 map 组件。
- css 动画对 map 组件无效。
- 缩小或者放大了地图比例尺之后，若再次设置 data 经纬度到一个地点，请在 onRegionChange 函数中重新设置 data 的 scale 值，否则会出现拖动地图区域后，重新加载导致地图比例尺又变回缩放前的大小，具体请参照示例代码 regionchange 函数部分。
- 基础库 1.24.13 开始支持 optimize 属性，开启 optimize 后，开发者不需要再监听 onRegionChange 来更新 scale 属性值以保证缩放比例不变。此特性在客户端 5.1.2 以上支持，可通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('map.optimize')进行检测。基础库版本号获取方法，请参考[获取基础库版本号](https://open.dingtalk.com/document/orgapp/gets-the-version-number-of-the-base-database)。
- 小程序不支持获取当前地图的经纬度。

## **示例代码**

.axml示例代码：

```
<view class="page">
  <block a:if="{{mapV2Enable}}">
    <view class="page-section">
      <view class="page-section-demo">
        <map
          id="map"
          longitude="{{longitude}}"
          latitude="{{latitude}}"
          scale="{{scale}}"
          controls="{{controls}}"
          onControlTap="controltap"
          markers="{{markers}}"
          onMarkerTap="markertap"
          polyline="{{polyline}}"
          polygon="{{polygon}}"
          circles="{{circles}}"
          onRegionChange="regionchange"
          onTap="tap"
          onCalloutTap="callouttap"
          show-location style="width: 100%; height: 200px;"
          include-points="{{includePoints}}"
          ground-overlays="{{groundOverlays}}">
        </map>
      </view>
    </view>
    <view class="page-section-btns">
      <view onTap="demoResetMap">恢复</view>
      <view onTap="demoGetCenterLocation">获取中心点坐标</view>
      <view onTap="demoMoveToLocation">回到定位点</view>
    </view>
    <view class="page-section-btns">
      <view onTap="demoMarkerAnimation">Marker 动画</view>
      <view onTap="demoMarkerLabel">Label</view>
      <view onTap="demoMarkerCustomCallout">CustomCallout</view>
    </view>
    <view class="page-section-btns">
      <view onTap="demoMarkerAppendStr">文字Marker</view>
      <view onTap="demoTrafficOverlay">路况展示</view>
      <view onTap="demoShowRoute">步行路线规划</view>
    </view>
    <view class="page-section-btns">
      <view onTap="demoCompass">指南针</view>
      <view onTap="demoScale">比例尺</view>
      <view onTap="demoGesture">手势</view>
    </view>
    <view class="page-section-btns">
      <view onTap="demoPolyline">线</view>
      <view onTap="demoPolygon">多边形</view>
      <view onTap="demoCircle">圆</view>
    </view>
    <view class="page-section-btns">
    </view>
  </block>
  <view class="page-section empty" a:else>
    <view class="text-line">
      当前版本不支持地图组件，请安装最新版本钉钉客户端并开启 V2 引擎。
    </view>
    <view class="text-line">
      V2 引擎开启方式请参考钉钉开放平台小程序引擎升级计划相关文档。
    </view>
</view>
</view>
```

.js示例代码：

```
const mapV2Message = '客户端版本过低，请升级客户端并开启V2引擎。'

const markers = [{
  id: 0,
  latitude: 30.266786,
  longitude: 120.10675,
  width: 19,
  height: 31,
  iconPath: '/image/mark_bs.png',
  callout: {
    content: 'callout',
  },
}];

const animMarker = [{
  id: 1,
  latitude: 30.266786,
  longitude: 120.10675,
  width: 19,
  height: 31,

  iconPath: '/image/mark_bs.png',

  fixedPoint:{
    originX: 200,
    originY: 150,
  },
  markerLevel: 2
}];

const labelMarker = [{
  id: 2,
  latitude: 30.266786,
  longitude: 120.10675,
  width: 19,
  height: 31,
  iconPath: '/image/mark_bs.png',
  label:{
    content:"Hello Label",
    color:"#00FF00",
    fontSize:14,
    borderRadius:3,
    bgColor:"#ffffff",
    padding:10,
  },
  markerLevel: 2
}];
const customCalloutMarker = [{
  id: 3,
  latitude: 30.266786,
  longitude: 120.10675,
  width: 19,
  height: 31,
  iconPath: '/image/mark_bs.png',
  "customCallout":{
    "type": 2,
    "descList": [{
      "desc": "预计",
      "descColor": "#333333"
    }, {
      "desc": "5分钟",
      "descColor": "#108EE9"
    }, {
      "desc": "到达",
      "descColor": "#333333"
    }],
    "isShow": 1
  },
  markerLevel: 2
}];

const iconAppendStrMarker = [{
  id: 34,
  latitude: 30.266786,
  longitude: 120.10675,
  width: 19,
  height: 31,
  iconAppendStr:"iconAppendStr",
  markerLevel: 2
}];

var myTrafficEnabled = 0;
var myCompassEnabled = 0;
var myScaleEnabled = 0;
var myGestureEnabled = 0;

const longitude = 120.10675;
const latitude = 30.266786;
const includePoints = [{
  latitude: 30.266786,
  longitude: 120.10675,
}];

Page({
  data: {
    scale: 14,
    longitude,
    latitude,
    includePoints,
    mapV2Enable: dd.canIUse('map.optimize'),
  },
  onReady() {
    // 使用 dd.createMapContext 获取 map 上下文
    this.mapCtx = dd.createMapContext('map');
  },
  demoResetMap() {
    this.setData({
      scale: 14,
      longitude,
      latitude,
      includePoints,
      'groundOverlays':[],
      circles:[],
      polygon:[],
      polyline:[],
    });
    if (dd.canIUse('createMapContext.return.clearRoute')) {
      this.mapCtx.clearRoute();
    }
  },
  demoGetCenterLocation() {
    if (dd.canIUse('createMapContext')) {
      this.mapCtx.getCenterLocation({
        success: (res) => {
          dd.alert({
            content: 'longitude:' + res.longitude + '\nlatitude:' + res.latitude + '\nscale:' + res.scale,
          });
          console.log(res.longitude);
          console.log(res.latitude);
          console.log(res.scale);
        },
      });
    }
  },
  demoMoveToLocation() {
    if (dd.canIUse('createMapContext')) {
      this.mapCtx.moveToLocation();
    }
  },
  demoMarkerAnimation() {
    if (!dd.canIUse('createMapContext.return.updateComponents')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message
      });
      return;
    } 
    this.mapCtx.updateComponents({
      'markers':animMarker,
    });
    this.mapCtx.updateComponents({
      command:{
        markerAnim:[{markerId:1,type:0},],
      }
    });
  },
  demoMarkerLabel() {
    if (!dd.canIUse('createMapContext.return.updateComponents')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message 
      });
      return;
    } 
    this.mapCtx.updateComponents({
      scale: 14,
      longitude,
      latitude,
      includePoints,
      'markers':labelMarker,
    });
  },
  demoMarkerCustomCallout() {
    if (!dd.canIUse('createMapContext.return.updateComponents')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message 
      });
      return;
    } 
    this.mapCtx.updateComponents({
      scale: 14,
      longitude,
      latitude,
      includePoints,
      'markers':customCalloutMarker,
    });
  },
  demoMarkerAppendStr() {
    if (!dd.canIUse('createMapContext.return.updateComponents')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message 
      });
      return;
    }
    this.mapCtx.updateComponents({
      scale: 14,
      longitude,
      latitude,
      includePoints,
      'markers':iconAppendStrMarker,
    });
  },
  demoTrafficOverlay() {
    if (!dd.canIUse('createMapContext.return.updateComponents')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message
      });
      return;
    } 
    myTrafficEnabled = (myTrafficEnabled+1) %2;
    this.mapCtx.updateComponents({setting:{trafficEnabled:myTrafficEnabled}});
  },
  demoShowRoute() {
    if (!dd.canIUse('createMapContext.return.showRoute')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message
      });
      return;
    } 
    this.mapCtx.showRoute({
      startLat:30.257839, 
      startLng:120.062726,
      endLat:30.256718,
      endLng:120.059985,
      zIndex:4,
      routeColor:'#FFB90F',
      iconPath: "/image/map_alr.png",
      iconWidth:10,
      routeWidth:10
     });
  },
  demoCompass() {
    if (dd.canIUse('createMapContext')) {
      myCompassEnabled = (myCompassEnabled+1) %2;
      this.mapCtx.showsCompass({isShowsCompass:myCompassEnabled});
    }
  },
  demoScale() {
    if (dd.canIUse('createMapContext')) {
      myScaleEnabled = (myScaleEnabled+1) %2;
      this.mapCtx.showsScale({isShowsScale:myScaleEnabled});
    }
  },
  demoGesture() {
    if (dd.canIUse('createMapContext')) {
      myGestureEnabled = (myGestureEnabled+1) %2;
      this.mapCtx.gestureEnable({isGestureEnable:myGestureEnabled});
    }
  },
  demoPolyline() {
    if (!dd.canIUse('map.polyline')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message
      });
      return;
    }
    this.setData({
      scale: 16,
      longitude,
      latitude,
      polyline: [{
        points: [{// 右上
          latitude: 30.264786,
          longitude: 120.10775,
        },{// 左下
          latitude: 30.268786,
          longitude: 120.10575,
        }],
        color: '#FF0000DD',
        width: 10,
        dottedLine: false,
        iconPath: "/image/map_alr.png",
        iconWidth:10,
      }],
    });
  },
  demoPolygon() {
    if (!dd.canIUse('map.polygon')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message
      });
      return;
    }
    this.setData({
      scale: 16,
      longitude,
      latitude,
      polygon: [{
        points: [{// 右上
          latitude: 30.264786,
          longitude: 120.10775,
        },{// 右下
          latitude: 30.268786,
          longitude: 120.10775,
        },{// 左下
          latitude: 30.268786,
          longitude: 120.10575,
        },{// 左上
          latitude: 30.264786,
          longitude: 120.10575,
        }],
        fillColor: '#BB0000DD',
        width: 5,
      }],
    });
    
  },
  demoCircle() {
    if (!dd.canIUse('map.circles')) {
      dd.alert({ 
        title: '不支持',
        content: mapV2Message
      });
      return;
    }
    this.setData({
      scale: 16,
      longitude,
      latitude,
      circles: [{
        longitude,
        latitude,
        color: '#BB76FF88',
        fillColor: '#BB76FF33',
        radius: 100,
        strokeWidth:3,
    }]
    });
  },
  regionchange(e) {
    console.log('regionchange', e);
  },
  markertap(e) {
    console.log('marker tap', e);
  },
  controltap(e) {
    console.log('control tap', e);
  },
  tap() {
    console.log('tap');
  },
  callouttap(e) {
    console.log('callout tap', e);
  },
});
```

## 属性

| **属性** | **类型** | **说明** |
| --- | --- | --- |
| style | String | 内联样式 。 |
| class | String | 样式名 。 |
| latitude | Number | 中心纬度。 |
| longitude | Number | 中心经度。 |
| scale | Number | 缩放级别，取值范围为 5-18 。  **默认值**：16。 |
| skew | Number | 倾斜角度，范围 0 ~ 40 , 关于 z 轴的倾角。  **默认值**：0。  **最低版本**：1.24.13。 |
| rotate | Number | 倾斜角度，范围 0 ~ 40 , 关于 z 轴的倾角。  **默认值**：0。  **最低版本**：1.24.13。 |
| markers | Array | 覆盖物，在地图上的一个点绘制图标。 |
| polyline | Array | 覆盖物，多个连贯点的集合（路线）。  **最低版本**：1.24.13。 |
| circles | Array | 覆盖物，圆。  **最低版本**：1.24.13。 |
| controls | Array | 在地图 View 之上的一个控件。  **最低版本**：1.24.13。 |
| polygon | Array | 覆盖物，多边形。  **最低版本**：1.24.13。 |
| show-location | Boolean | 是否显示带有方向的当前定位点。 |
| include-points | Array | 视野将进行小范围延伸包含传入的坐标。  **最低版本**：1.24.13。   ``` [{     latitude: 30.279383,     longitude: 120.131441 }] ``` |
| include-padding | Object | 视野在地图 padding 范围内展示。  **最低版本**：1.24.13。   ``` {     left:0, right:0,     top:0, bottom:0 } ``` |
| ground-overlays | Array | 覆盖物，自定义贴图。  **最低版本**：1.24.13。   ``` [{     // 右上，左下     'include-points':[{         latitude: 39.935029,         longitude: 116.384377,     },{         latitude: 39.939577,         longitude: 116.388331,     }],     image:'/image/overlay.png',     alpha:0.25,     zIndex:1 }] ``` |
| tile-overlay | Object | 覆盖物，网格贴图。  **最低版本**：1.24.13。   ``` {     url:'http://xxx',     type:0, // url类型     tileWidth:256,     tileHeight:256,     zIndex:1, } ``` |
| custom-map-style | String | 设置地图样式。   - **default**：默认样式。 - **light**：精简样式。   **最低版本**：1.24.13。 |
| setting | Object | 设置。  **最低版本**：1.24.13。   ``` {  // 手势  gestureEnable: 1,  // 比例尺  showScale: 1,  // 指南针  showCompass: 1,  //双手下滑  tiltGesturesEnabled: 1,  // 交通路况展示  trafficEnabled: 0,  // 地图 POI 信息  showMapText: 0,  // 高德地图 logo 位置  logoPosition: {   centerX: 150,   centerY: 90  } } ``` |
| onMarkerTap | EventHandle | 点击 Marker 时触发。   ``` {     markerId,     latitude,     longitude,  } ``` |
| onCalloutTap | EventHandle | 点击 Marker 对应的 callout 时触发。  **最低版本**：1.24.13。   ``` {     markerId,     latitude,     longitude,  } ``` |
| onControlTap | EventHandle | 点击 control 时触发。  **最低版本**：1.24.13。   ``` {     controlId } ``` |
| onRegionChange | EventHandle | 视野发生变化时触发。  **最低版本**：1.24.13。   ``` {     type: "begin/end",      latitude,     longitude,      scale } ``` |
| onTap | EventHandle | 点击地图时触发。   ``` {     latitude,     longitude,  } ``` |

## **markers**

标记点，用于在地图上显示标记的位置。

> **[!IMPORTANT]**
>
> - 可利用该参数显示多个定位点。
> - 地点标注不支持设置英文。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| id | Number | 否 | 标记点 id，点击事件回调会返回此 id。 |
| latitude | Float | 是 | 纬度，范围 -90 ~ 90。 |
| longitude | Float | 是 | 经度，范围 -180 ~ 180。 |
| title | String | 否 | 标注点名。 |
| iconPath | String | 是 | 显示的图标，项目目录下的图片路径，不能用相对路径只能用 / 开头的绝对路径。示例：/pages/image/test.jpg。 |
| rotate | Number | 否 | 旋转角度，顺时针旋转的角度，范围 0 ~ 360。  **默认值**： 0。 |
| alpha | Number | 否 | 标注的透明度，是否透明。  **默认值**： 1。 |
| width | Number | 否 | 标注图标宽度，默认为图片的实际宽度。 |
| height | Number | 否 | 标注图标高度，默认为图片的实际高度。 |
| displayRanges | Array | 否 | 标明在特定地图缩放级别下展示，默认所有级别下都展示；指定只在特定级别范围展示。  **最低版本**：1.24.13。   ``` [{    "from": 10,     "to": 15  }] ``` |
| callout | Object | 否 | 自定义标记点上方的气泡窗口，marker 上的气泡，地图上最多同时展示一个，绑定 onCalloutTap。  **最低版本**：1.24.13。   ``` {     content:"xxx" } ``` |
| anchorX | Double | 否 | 经纬度在标注图标的锚点-横向值，需要与anchorY成对出现，anchorX 表示横向(0-1)，anchorX:0.5,anchorY:1表示底边中点。 |
| anchorY | Double | 否 | 经纬度在标注图标的锚点-竖向值，需要与anchorY成对出现，anchorY 表示竖向(0-1)，anchorX:0.5,anchorY:1表示底边中点。 |
| customCallout | Object | 否 | callout 背景自定义，目前只支持高德地图 style。  **最低版本**：1.24.13。   ``` {  "type": 2,  "descList": [{   "desc": "预计",   "descColor": "#333333"  }, {   "desc": "5分钟",   "descColor": "#108EE9"  }, {   "desc": "到达",   "descColor": "#333333"  }],  "isShow": 1 } ``` |
| iconAppendStr | String | 否 | marker 图片可以来源于 View，和 iconPath 一起使用，会将 iconPath 对应的图片及该字符串共同生成一个图片，当成 marker 的图标。 |
| iconAppendStrColor | String | 否 | marker 图片可以来源于 View，底部描述文本颜色。  **默认值**：#33B276。 |
| fixedPoint | Object | 否 | 基于屏幕位置扎点，基于屏幕位置扎点。   ``` {     //距离地图左上角的像素数,Number     originX:100,      originY:100   } ``` |
| markerLevel | Number | 否 | marker 在地图上的绘制层级，与地图上其他覆盖物统一的 Z 坐标系。  **最低版本**：1.24.13。 |
| label | Object | 否 | marker 上的气泡，marker 上的气泡，地图上可同时展示多个，绑定 onMarkerTap。  **最低版本**：1.24.13。   ``` {     content:"Hello Label",     color:"#000000",     fontSize:12,     borderRadius:"3",     bgColor:"#ffffff",     padding:5, } ``` |
| style | Object | 否 | 自定义 marker 样式，自定义 marker 的样式和内容。  **最低版本**：1.24.13。 |

## **polygon**

用于构造多边形对象。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| points | Array | 是 | 经纬度数组。   ``` [{  latitude: 0,  longitude: 0 }] ``` |
| color | String | 否 | 线的颜色。用 8 位十六进制表示，后两位表示 alpha 值，如：#eeeeeeAA。 |
| fillColor | String | 否 | 填充色。用 8 位十六进制表示，后两位表示 alpha 值，如：#eeeeeeAA。 |
| width | Number | 否 | 线的宽度。 |
| displayRanges | Array | 否 | 标明在特定地图缩放级别下展示。默认所有级别下都展示。  指定只在特定级别范围展示。   ``` [{   "from": 12,   "to": 17  }] ``` |

## **polyline**

用于指定一系列坐标点，从数组第一项连线至最后一项。

| **属性** | **类型** | 是否必填 | 说明 |
| --- | --- | --- | --- |
| points | Array | 是 | 经纬度数组。   ``` [{  latitude: 0,  longitude: 0 }] ``` |
| color | String | 否 | 线的颜色，用 8 位十六进制表示，后两位表示 alpha 值，如：#eeeeeeAA。 |
| width | Number | 否 | 线的宽度。 |
| dottedLine | Boolean | 否 | 是否虚线。  **默认值**： false。 |
| iconWidth | Number | 否 | 使用纹理时的宽度。 |
| zIndex | Number | - | 覆盖物的 Z 轴坐标。 |
| iconPath | String | - | 项目目录下的图片路径，可以用相对路径写法，以'/'开头则表示相对小程序根目录， 如果有 iconPath，会忽略 color。  但是 iconPath 可以和 colorList 联合使用，这样纹理会浮在彩虹线上方，为避免覆盖彩虹线，纹理图片背景色可以设置透明。  **[!NOTE]**  要求对应的贴图形状为正方形，尺寸为宽高是 2 的整数幂，如 16\*16、64\*64。 |
| colorList | Array | - | 彩虹线，分段依据points。例如 points 有5个点，那么 colorList 就应该传 4 个颜色值，依此类推。如果 colorList 数量小于4，那么剩下的线路颜色和最后一个颜色一样。   ``` [  "#AAAAAA",  "#BBBBBB" ] ``` |

## **circles**

用于在地图上显示圆。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| latitude | Float | 是 | 纬度，范围 -90 ~ 90。 |
| longitude | Float | 是 | 经度，范围 -180 ~ 180。 |
| color | String | 否 | 描边的颜色，用 8 位十六进制表示，后两位表示 alpha 值，如：#eeeeeeAA。 |
| fillColor | String | 否 | 填充颜色，用 8 位十六进制表示，后两位表示 alpha 值，如：#eeeeeeAA。 |
| radius | Number | 是 | 半径（米）。 |
| strokeWidth | Number | 否 | 描边的宽度。 |

## **controls**

用于在地图上显示控件，控件不随着地图移动。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| id | Number | 否 | 控件 id，点击事件回调会返回此 id。 |
| position | Object | 是 | 控件在地图的位置。 |
| iconPath | String | 是 | 项目目录下的图片路径，可以用相对路径写法，以'/'开头则表示相对小程序根目录。 |
| clickable | Boolean | 否 | 是否可点击。  **默认值**：**false**。 |

## **position**

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| left | Number | 否 | 距离地图的左边界多远。  **默认值**：**0**。 |
| top | Number | 否 | 距离地图的上边界多远。  **默认值**：**0**。 |
| width | Number | 否 | 控件宽度，默认为图片宽度。 |
| height | Number | 否 | 控件高度，默认为图片高度。 |

## **callout**

自定义标记点上方的气泡窗口。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| content | String | 否 | 内容。  **默认值**：null。 |

## **customCallout**

自定义 callout 背景。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| type | Number | 是 | 样式类型：   - **0**：为黑色 style - **1**：为白色 style - **2**：为背景+文本   original |
| time | String | 是 | 时间值。 |
| descList | Array | 是 | 描述数组。   ``` {     "type": 0,     "time": "3",     "descList": [{          "desc": "点击立即打车",         "descColor": "#ffffff"      }],     "isShow": 1  } ``` |

**fixedPoint**

基于屏幕位置的扎点。

| **属性** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| originX | Number | 是 | 横向像素点，距离地图左上角的像素数值，从 0 开始。 |
| originY | Number | 是 | 纵向像素点，距离地图左上角的像素数值，从 0 开始。 |

地图组件的经纬度是必需设置的, 若未设置经纬度，则默认是北京的经纬度。

## Marker 图鉴

**Marker 样式优先级说明**：

- customCallout，callout 与 label 互斥，优先级排序为：label > customCallout > callout。
- style 与 icon 互斥，优先级排序为：style > iconAppendStr；style > icon。

**style**

| **结构** | **图片示例** |
| --- | --- |
| ``` {     type:1,     text1:"Style1",     icon1:'xxx',     icon2:'xxx' } ``` | 1537428922033-7f44ea7c-6f28-43cc-a5d0-80cc4cf0213b.png |
| ``` {     type:2,     text1:"Style2",     icon1:'xxx',     icon2:'xxx' } ``` | 1537428730637-bd21f41b-3352-4c42-a2ba-0dca4012b0e3.png |
| ``` {     type:3,     icon:xxx,  //选填     text:xxx,  //必填     color:xxx,  //默认#33B276     bgColor:xxx,  //默认#FFFFFF       gravity:"left/center/right", //默认 center     fontType:"small/standard/large"  //默认standard } ``` | original |

**customCallout**

| **结构** | **图片示例** |
| --- | --- |
| ```   "type": 0,     "time": "3",     "descList": [{          "desc": "点击立即打车",         "descColor": "#ffffff"      }],     "isShow": 1 ``` | 1537429397117-959401db-99f0-48b1-a15d-9817d441d978.png |
| ``` {      "type": 1,     "time": "3",     "descList": [{          "desc": "点击立即打车",         "descColor": "#333333"      }],     "isShow": 1  } ``` | 1537429638548-7a7dd421-7bc7-4849-8498-e8a9a3381618.png |
| ``` {  "type": 2,  "descList": [{   "desc": "预计",   "descColor": "#333333"  }, {   "desc": "5分钟",   "descColor": "#108EE9"  }, {   "desc": "到达",   "descColor": "#333333"  }],  "isShow": 1 } ``` | 1537429638548-7a7dd421-7bc7-4849-8498-e8a9a3381618.png 1537429958605-eff755af-bc25-40bd-b697-1d4c2e1be712.png |

**label**

| **属性** | **是否必填** | **说明** |
| --- | --- | --- |
| content | 是 | - |
| color | 否 | 默认"#000000"。 |
| fontsize | 否 | 默认14。 |
| borderRadius | 否 | 默认20。 |
| bgColor | 否 | 默认"#FFFFFF"。 |
| padding | 否 | 默认10。 |

## 兼容性

- **是否支持地图组件**

  通过 dd.canIUse('map') 进行判断。
- **是否支持特定属性**

  明确指定了**最低版本**的属性，需要通过 canIUse 进行属性兼容性判断。

  如 **polyline** 属性，需要通过 dd.canIUse('map.polyline') 进行可用性判断。

  对于 makers 下的 **customCallout** 属性则需要通过dd.canIUse('map.makers.customCallout') 进行可用性判断。

## 常见问题

- **map 组件如何跳转到高德的 app 中去进行导航？**

  可使用[使用内置地图查看位置](https://open.dingtalk.com/document/orgapp/dd-openlocation)。
- **map 组件 optimize 属性设置了 true 后如何获取 scale 值？**

  optimize 属性设置了 true 后，如果需要获取 scale 值，必须要使用 onRegionChange。
- **map组件是否支持海外功能？**

  目前不支持。
- **如何手动在地图上绘制多边形区域？**

  可以使用 polygon 进行绘制。
- **iconAppendStr 里的文字能不能换行？**

  不支持。
- **地图组件里，设置了路径之后， 如何更改起点终点的 icon？**

  目前不支持更改。

  ![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7154199951/p163540.png)

## 错误码

错误码信息请参见：

- [Andriod 地图错误码对照表](https://lbs.amap.com/api/android-sdk/guide/map-tools/error-code)
- [iOS 地图错误码对照](https://lbs.amap.com/api/ios-sdk/guide/map-tool/errorcode/)
