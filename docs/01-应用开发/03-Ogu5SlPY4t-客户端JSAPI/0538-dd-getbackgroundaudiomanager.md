---
title: "获取背景音频管理"
source_url: "https://open.dingtalk.com/document/development/dd-getbackgroundaudiomanager"
namespace: "development"
slug: "dd-getbackgroundaudiomanager"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 背景音频管理 > 获取背景音频管理"
doc_id: "xxlQi1f23E"
updated_at: "2025-09-17 20:59:01"
---

> Source: https://open.dingtalk.com/document/development/dd-getbackgroundaudiomanager
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 背景音频管理 > 获取背景音频管理
> Updated: 2025-09-17 20:59:01

# 获取背景音频管理

调用**dd.getBackgroundAudioManager**获取当前小程序全局唯一的背景音频管理。当小程序切入后台时，音频可以背景播放。

## 使用方法

```
let backgroundAudioManager = dd.getBackgroundAudioManager()
```

## **示例代码**

```
Page({
    data:{
        title:'abc',
        src:'http://music.xxxx/url?id=317151.mp3',
        coverImgUrl:'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg',
    },
    onLoad(){
        let manager = dd.getBackgroundAudioManager()
        let events =  ["onCanplay","onPlay","onPause","onStop","onEnded","onTimeUpdate","onError","onWaiting","onSeeking","onSeeked","onPrev","onNext"]
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

## **backgroundAudioManager属性**

| **属性名** | **属性类型** | **读写特性** | **说明** |
| --- | --- | --- | --- |
| src | String | 读/写 | 音频文件地址，支持类型有mp3/wav/aac/m4a格式。当设置此值时，音频就会开始播放。 |
| title | String | 读/写 | 音频标题。 |
| coverImgUrl | String | 读/写 | 引用播放封面图片地址。 |
| paused | Boolean | 读 | 音频是否暂停。 |
| duration | Number | 读 | 当前音频的总长度，单位是秒。 |
| currentTime | Number | 读 | 当前音频播放的位置，单位是秒。 |

## **backgroundAudioManager方法**

| **方法名** | **参数** | **说明** |
| --- | --- | --- |
| play | - | 播放。 |
| pause | - | 暂停。 |
| stop | - | 停止。 |
| seek | position | 跳转到指定位置position，以秒为单位。 |
| onCanplay | - | 监听背景音频进入可以播放事件。  **[!NOTE]**  不保证后面可以流畅播放。 |
| onWaiting | - | 监听音频加载中事件。  **[!NOTE]**  当音频因为数据不足，需要停下来加载时会触发。 |
| onPlay | - | 监听背景音频播放事件。 |
| onPause | - | 监听背景音频暂停事件。 |
| onStop | - | 监听背景音频停止事件。 |
| onSeeking | - | 监听背景音频开始播放进度跳转事件。 |
| onSeeked | - | 监听背景音频完成播放进度跳转事件。 |
| onEnded | - | 监听背景音频结束事件。 |
| onPrev | - | 监听用户在系统音乐播放面板点击上一曲事件。 |
| onNext | - | 监听用户在系统音乐播放面板点击下一曲事件。 |
| onTimeUpdate | - | 监听背景音频播放进度更新事件。 |
| onError | - | 监听背景音频错误事件。 |

## **错误码**

| **error** | **说明** |
| --- | --- |
| 10001 | 系统错误。 |
| 10002 | 网络错误。 |
| 10003 | 文件错误。 |
| 10004 | 格式错误。 |
