---
title: "获取录音管理器"
source_url: "https://open.dingtalk.com/document/development/dd-getrecordermanager"
namespace: "development"
slug: "dd-getrecordermanager"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 录音管理 > 获取录音管理器"
doc_id: "yORyvI1N8U"
updated_at: "2025-09-17 20:59:00"
---

> Source: https://open.dingtalk.com/document/development/dd-getrecordermanager
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 录音管理 > 获取录音管理器
> Updated: 2025-09-17 20:59:00

# 获取录音管理器

调用**dd.getRecorderManager**获取当前小程序全局唯一的录音管理器 recordManager。

## 使用方法

```
const recorderManager = dd.getRecorderManager()
```

## 使用限制

此API在钉钉客户端版本7.0.10开始支持。开发者可以通过canIUse函数判断端上是否支持此能力。

| **应用能力** | **Android** | **iOS** | **Mac** | **Windows** |
| --- | --- | --- | --- | --- |
| 小程序 | 7.0.10 | 7.0.10 | 不支持 | 不支持 |

```
if (dd.canIUse('getRecorderManager')) {     // 端上支持
    const recorderManager = dd.getRecorderManager()    
} else {     // 端上不支持
    dd.alert({ content: '请升级钉钉版本至7.0.10以支持录音功能' })    
}
```

## **recorderManager方法**

| **方法名** | **参数** | **说明** |
| --- | --- | --- |
| start | duration：录音时长，单位为秒（s），最长支持60秒音频录制。  **[!NOTE]**  该参数在Android端必填。 | 开始录音，当页面不可见时，录音自动停止。 |
| stop | - | 停止录音。 |
| pause | - | 暂停录音。 |
| resume | - | 继续录音，即恢复之前暂停的录音。 |

## **recorderManager回调**

| **回调名** | **回调参数** | **说明** |
| --- | --- | --- |
| onstart | - | 录音开始时的回调。 |
| onstop | tempFilePath：录音文件地址 | 录音停止时的回调。 |
| onerror | errorCode：错误码  errorMessage：错误信息 | 录音错误时的回调。 |
| onpause | - | 监听录音暂停事件。 |
| onresume | - | 监听录音继续事件。 |

## **错误码**

| **errorCode** | **errorMessage** |
| --- | --- |
| 20001 | 已经正在录音中，不能同时再录音。 |
| 13 | 保存录音文件失败。 |
| 2 | 参数错误。 |
| 5 | 没有读写权限。 |

## **示例代码**

```
startRecord() {
    let rm = dd.getRecorderManager()
    rm.onstart = (res) => {
      dd.alert({
        content: 'record onStart'
      })
      console.log('onstart', res)
    }
    rm.onerror = (err) => {
      dd.alert({
        content: 'onerror'
      })
    }
    rm.start({
      duration: 10
    })
  },
  pauseRecord() {
    let rm = dd.getRecorderManager()
    rm.onpause = (res) => {
      dd.alert({
        content: 'onpause'
      })
      console.log('onpause', res)
    }
    rm.pause();
  },
  resumeRecord() {
    let rm = dd.getRecorderManager()
    rm.onresume = (res) => {
      dd.alert({
        content: 'onresume'
      })
      console.log('onresume', res)
    }
    rm.resume();
  },
  stopRecord() {
    let rm = dd.getRecorderManager()
    rm.onstop = (res) => {
      dd.alert({
        content: 'tempFilePath: ' + res.tempFilePath
      })
      console.log('onstop', res)
    }
    rm.stop();
  }
```
