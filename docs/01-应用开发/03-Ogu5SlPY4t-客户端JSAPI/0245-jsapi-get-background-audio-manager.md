---
title: "getBackgroundAudioManager"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-background-audio-manager"
namespace: "development"
slug: "jsapi-get-background-audio-manager"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 音频 > getBackgroundAudioManager"
doc_id: "iMZMq845zx"
updated_at: "2025-08-27 18:06:55"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-background-audio-manager
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 音频 > getBackgroundAudioManager
> Updated: 2025-08-27 18:06:55

# getBackgroundAudioManager

调用dd.getBackgroundAudioManager获取当前小程序全局唯一的背景音频管理。当小程序切入后台时，音频可以背景播放。

```
Page({
    data:{
        title:'abc',
        src:'http://music.xxxx/url?id=317151.mp3',
        coverImgUrl:'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg',
    },
    onLoad(){
        let manager = dd.getBackgroundAudioManager()
        let events =  ["onPlay","onPause","onStop","onEnded","onTimeUpdate","onError","onWaiting"]
        events.forEach(item => {
            manager[item] = function(event){
                console.log('EVENT:',item, event)
            }
        })
    },
    start() {
        let manager = dd.getBackgroundAudioManager()
        manager.title = this.data.title
        manager.coverImgUrl = this.data.coverImgUrl
        manager.src = this.data.src
    }
})
```

### backgroundAudioManager属性

| 属性名 | 属性类型 | 读写特性 | 说明 |
| --- | --- | --- | --- |
| src | String | 读/写 | 音频文件地址，支持类型有mp3/wav/aac/m4a格式。当设置此值时，音频就会开始播放。 |
| title | String | 读/写 | 音频标题。 |
| coverImgUrl | String | 读/写 | 引用播放封面图片地址。 |
| paused | Boolean | 读 | 音频是否暂停。 |
| duration | Number | 读 | 当前音频的总长度，单位是秒。 |
| currentTime | Number | 读 | 当前音频播放的位置，单位是秒。 |

### backgroundAudioManager方法

| 方法名 | 参数 | 说明 |
| --- | --- | --- |
| play | - | 播放。 |
| pause | - | 暂停。 |
| stop | - | 停止。 |
| seek | position | 跳转到指定位置position，以秒为单位。 |
| onPlay | - | 监听背景音频播放事件。 |
| onCanplay | - | 监听背景音频进入可以播放状态。但不保证后面可以流畅播放。 |
| onWaiting | - | 监听音频加载中事件。当音频因为数据不足，需要停下来加载时会触发。 |
| onPause | - | 监听背景音频暂停事件。 |
| onStop | - | 监听背景音频停止事件。 |
| onEnded | - | 监听背景音频结束事件。 |
| onTimeUpdate | - | 监听背景音频播放进度更新事件。 |
| onError | - | 监听背景音频错误事件。 |
| onSeeking | - | 监听背景音频开始播放进度跳转事件。 |
| onSeeked | - | 监听背景音频完成播放进度跳转操作。 |
| onNext | - | 监听用户在系统音乐播放面板点击下一曲事件。 |
| onPrev | - | 监听用户在系统音乐播放面板点击上一曲事件。 |

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10222) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 10001 | 系统错误 |
| 10002 | 网络错误 |
| 10003 | 文件错误 |
| 10004 | 格式错误 |

## **示例****代码**

### 默认出入参

```
const res = dd.getBackgroundAudioManager({});
console.log(res);
// res: `undefined示例值`
```

返回对象示例：

```
`undefined示例值`
```
