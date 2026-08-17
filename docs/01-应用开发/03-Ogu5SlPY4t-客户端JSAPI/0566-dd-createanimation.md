---
title: "创建动画实例"
source_url: "https://open.dingtalk.com/document/development/dd-createanimation"
namespace: "development"
slug: "dd-createanimation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 动画 > 创建动画实例"
doc_id: "TNgHE112Ua"
updated_at: "2025-09-17 20:59:22"
---

> Source: https://open.dingtalk.com/document/development/dd-createanimation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 动画 > 创建动画实例
> Updated: 2025-09-17 20:59:22

# 创建动画实例

调用**dd.createAnimation**创建动画实例。调用实例的方法来描述动画，最后通过动画实例的export方法将动画数据导出并传递给组件的animation属性。

> **[!IMPORTANT]**
>
> `export` 方法调用后会清掉之前的动画操作。

## **扫码体验**

![1595556263163-4 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1209903061/p172096.png)

## **示例代码**

.axml示例代码：

```
<view animation="{{animationInfo}}" style="background:yellow;height:100rpx;width:100rpx"></view>
```

.js示例代码

```
Page({
  data: {
    animationInfo: {}
  },
  onShow(){
    var animation = dd.createAnimation({
      duration: 1000,
        timeFunction: 'ease-in-out',
    });

    this.animation = animation;

    animation.scale(3,3).rotate(60).step();

    this.setData({
      animationInfo:animation.export()
    });

    setTimeout(function() {
      animation.translate(35).step();
      this.setData({
        animationInfo:animation.export(),
      });
    }.bind(this), 1500);
  },
  rotateAndScale () {
    // 旋转同时放大
    this.animation.rotate(60).scale(3, 3).step();
    this.setData({
      animationInfo: this.animation.export(),
    });
  },
  rotateThenScale () {
    // 先旋转后放大
    this.animation.rotate(60).step();
    this.animation.scale(3, 3).step();
    this.setData({
      animationInfo: this.animation.export(),
    });
  },
  rotateAndScaleThenTranslate () {
    // 先旋转同时放大，然后平移
    this.animation.rotate(60).scale(3, 3).step();
    this.animation.translate(100, 100).step({ duration: 2000 });
    this.setData({
      animationInfo: this.animation.export()
    });
  }
})
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| duration | Integer | 否 | 动画的持续时间，单位 ms。  **默认值** ：400。 |
| timeFunction | String | 否 | 定义动画的效果，有效值："linear"，"ease"，"ease-in"，"ease-in-out"，ease-out"，"step-start"，"step-end"。  **默认值**："linear"。 |
| delay | Integer | 否 | 动画延迟时间，单位 ms。  **默认值**：0。 |
| transformOrigin | String | 否 | 设置transform-origin。  **默认值**："50"。 |

## **动画实例方法**

动画实例可以调用以下方法来描述动画，调用结束后会返回实例本身，支持链式调用的写法。

**样式**

| **方法** | **参数** | **说明** |
| --- | --- | --- |
| opacity | value | 透明度，参数范围 0~1。 |
| backgroundColor | color | 颜色值。 |
| width | length | 长度值，如果传入数字则默认单位为 px ，可传入其他自定义单位的长度值。 |
| height | length | 同上。 |
| top | length | 同上。 |
| left | length | 同上。 |
| bottom | length | 同上。 |
| right | length | 同上。 |

**旋转**

| **方法** | **参数** | **说明** |
| --- | --- | --- |
| rotate | deg | deg 范围 -180 ~ 180，从原点顺时针旋转一个 deg 角度。 |
| rotateX | deg | deg 范围 -180 ~ 180，在 X 轴旋转一个 deg 角度。 |
| rotateY | deg | deg 范围 -180 ~ 180，在 Y 轴旋转一个 deg 角度。 |
| rotateZ | deg | deg 范围 -180 ~ 180，在 Z 轴旋转一个deg角度 |
| rotate3d | (x, y , z, deg) | 同 [transform-function rotate3d。](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d) |

**缩放**

| **方法** | **参数** | **说明** |
| --- | --- | --- |
| scale | sx, [sy] | 只有一个参数时，表示在 X 轴、Y 轴同时缩放 sx 倍；两个参数时表示在 X 轴缩放 sx 倍，在 Y 轴缩放 sy 倍。 |
| scaleX | sx | 在 X 轴缩放 sx 倍。 |
| scaleY | sy | 在 Y 轴缩放 sy 倍。 |
| scaleZ | sz | 在 Z 轴缩放 sy 倍。 |
| scale3d | (sx, sy, sz) | 在 X 轴缩放 sx 倍，在 Y 轴缩放sy 倍，在 Z 轴缩放 sz 倍。 |

**偏移**

| **方法** | **参数** | **说明** |
| --- | --- | --- |
| translate | tx, [ty] | 只有一个参数时，表示在 X 轴偏移 tx；两个参数时，表示在 X 轴偏移 tx，在 Y 轴偏移 ty，单位均为 px。 |
| translateX | tx | 在 X 轴偏移 tx，单位 px。 |
| translateY | ty | 在 Y 轴偏移 ty，单位 px。 |
| translateZ | tz | 在 Z 轴偏移 tz，单位 px。 |
| translate3d | (tx, ty, tz) | 在 X 轴偏移 tx，在 Y 轴偏移 ty，在Z轴偏移 tz，单位 px。 |

**倾斜**

| **方法** | **参数** | **说明** |
| --- | --- | --- |
| skew | ax, [ay] | 参数范围 -180 ~ 180。只有一个参数时，Y 轴坐标不变，X 轴坐标延顺时针倾斜 ax 度；两个参数时，分别在 X 轴倾斜 ax 度，在 Y 轴倾斜 ay 度。 |
| skewX | ax | 参数范围 -180 ~ 180。Y 轴坐标不变，X 轴坐标沿顺时针倾斜 ax 度。 |
| skewY | ay | 参数范围 -180 ~ 180。X 轴坐标不变，Y 轴坐标沿顺时针倾斜 ay 度。 |

**矩阵变形**

| **方法** | **参数** | **说明** |
| --- | --- | --- |
| matrix | (a,b,c,d,tx,ty) | 同 [transform-function](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix)。 |
| matrix3d |  | 同 [transform-function matrix3d](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix3d)。 |

**动画队列**

- 调用动画操作方法后需要要调用 `step()` 来表示一组动画完成，在一组动画中可以调用任意多个动画方法，一组动画中的所有动画会同时开始，当一组动画完成后才会进行下一组动画。
- `step()` 可以传入一个跟 `dd.createAnimation()` 一样的配置参数用于指定当前组动画的配置。
