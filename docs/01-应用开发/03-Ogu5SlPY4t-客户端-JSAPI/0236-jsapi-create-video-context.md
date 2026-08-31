---
title: "createVideoContext"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-video-context"
namespace: "development"
slug: "jsapi-create-video-context"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 视频 > createVideoContext"
doc_id: "Fb65AdTzi1"
updated_at: "2025-08-27 18:06:49"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-video-context
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 视频 > createVideoContext
> Updated: 2025-08-27 18:06:49

# createVideoContext

调用dd.createVideoContext(videoId)创建并返回一个 video上下文对象videoContext，videoId 为 video 组件的 id 属性设置的值。

.axml示例代码：

```
<video id="v"  class="source-video-content"  src="{{videoUrl}}" 
onTimeUpdate="onTimeUpdate"  objectFit="contain" style="width: 200px; 
height: 200px"  enableNative="{{true}}"> </video>
<button onTap="pause">pause</button>
<button onTap="seek30s">seek30s</button>
```

.js示例代码：

```
Page({
  data: {
    videoUrl:'xxx'
  },
  onTimeUpdate(e) {
    console.log('onTimeUpdate: currentTime' + e.detail.currentTime)
  },
  pause() {
    let ctx = dd.createVideoContext('v');
    ctx.pause();
  },
  seek30s() {
    let ctx = dd.createVideoContext('v');
    ctx.seek(30);
  }
});
```

### videoContext方法

| 方法名 | 参数 | 类型 | 说明 |
| --- | --- | --- | --- |
| play | - | - | 播放。 |
| pause | - | - | 暂停。 |
| stop | - | - | 终止。 |
| seek | position | Number | 定位，单位为秒（s）。 |
| mute | ison | Boolean | 切换静音状态。 |
| requestFullScreen | direction | Number | 进入全屏。0：正常竖屏。90：横屏。-90：反向横屏。 |
| exitFullScreen | - | - | 退出全屏。 |
| snapshot | quality | String | 截图，可选值 raw compressed。 |
| playbackRate | rate | Number | 设置倍速播放（0.5 <= rate <= 2.0）。 |

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10200) |

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

- `id`（string，必填）：videoId。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.createVideoContext('video');
```
