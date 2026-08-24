---
title: "getCachedAPIResponse"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-cached-a-p-i-response"
namespace: "development"
slug: "jsapi-get-cached-a-p-i-response"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 内存不足处理 > getCachedAPIResponse"
doc_id: "ycyLf5VGoj"
updated_at: "2025-10-16 15:45:35"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-cached-a-p-i-response
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 内存不足处理 > getCachedAPIResponse
> Updated: 2025-10-16 15:45:35

# getCachedAPIResponse

获取已缓存的JSAPI返回值

获取当前页面之前调用的、已缓存的 JSAPI 的返回值。需要先调用 enableAPIResponseCache 开启缓存功能。

页面发生跳转后，url 发生变化时，会自动清空缓存。

用于解决内存占用过高导致 WebView 崩溃，用户无法继续操作的问题。
返回值是个字典，key 是 JSAPI 的名称，value 是个数组，数组的每一项是缓存的 JSAPI 返回值。

返回值示例：

```
{
    "biz.util.chooseImage":[
        {
            "cacheTime":1758098405000,
            "cacheData":{
                "files":[
                    {
                        "fileType":"jpg",
                        "path":"https://resource/MjhiYWQyYjQwZjk4NTQzYTFkZWViY2YyZjBjODNiNGQ=.image",
                        "size":203906
                    },
                    {
                        "fileType":"jpg",
                        "path":"https://resource/NjhkYWE0ZDYwMmUwODRmNjY1OGQ4OWViMTQ3ZmRhNGY=.image",
                        "size":129520
                    }
                ],
                "filePaths":[
                    "https://resource/MjhiYWQyYjQwZjk4NTQzYTFkZWViY2YyZjBjODNiNGQ=.image",
                    "https://resource/NjhkYWE0ZDYwMmUwODRmNjY1OGQ4OWViMTQ3ZmRhNGY=.image"
                ]
            }
        },
        {
            "cacheTime":1758098505000,
            "cacheData":{
                "files":"xxx",
                "filePaths":"xxx"
            }
        }
    ]
}
```

# WebView 内存崩溃恢复解决方案

## 问题现象

H5 和小程序上拍照后，有时会发生页面崩溃刷新，导致一直没法上传图片。

## 原因

设备当前内存占用过高时（注意是运行内存，不是磁盘内存），webView 会被系统回收，导致页面刷新。

## 用户侧解决方式

需要降低设备的内存占用，占用的内存可能是钉钉的，也可能是其他 app 的：

1. 关闭钉钉内其他不用的网页
2. 重启钉钉 app（iOS 中上划手势唤起应用切换器，上划关闭应用）
3. 关闭其他 app，释放内存
4. 如果一直不行，需要重启手机，释放系统占用的内存

## 业务侧解决方式

前端开发者需要在用户执行一些耗内存操作前，暂存一下页面数据到 localStorage 里，比如已填写的表单项。

当页面被刷新后，从 localStorage 里读取暂存的数据，恢复到页面上。

当表单提交时，清除暂存的数据。

如果发现页面在短时间内不停被刷新，就提示用户按上面的步骤清理设备内存。

## JSAPI 返回值缓存

当调用一些占用内存很高的 jsapi，例如相机拍照、录像时，jsapi 还没返回，WebView 可能就已经被系统回收然后刷新了，业务没法自己缓存 jsapi 返回值，导致业务流程无法进行下去。

针对涉及拍照等耗内存的 jsapi，钉钉提供了 jsapi 返回值缓存功能，即使 WebView 崩溃了，刷新后页面也能取到上次调用 jsapi 的返回值。取到返回值之后就能继续往下执行业务流程，无需再重新调用 jsapi，避免内存问题。

## 支持的 JSAPI

- biz.util.chooseImage
- biz.util.chooseMedia
- biz.uil.uploadImage
- biz.util.uploadImageFromCamera
- biz.util.uploadMedia
- biz.util.fetchImageData
- biz.util.editPicture
- chooseImage（小程序 JSAPI）
- chooseVideo（小程序 JSAPI）

## 最佳实践

### 场景1: 只有一个地方使用 chooseImage 时

1. 调用 chooseImage 前，暂存业务上下文到 localStorage 中
2. WebView 在 JSAPI 返回前，由于内存问题崩溃刷新
3. 页面刷新后，从 localStorage 里读取是否有暂存的业务上下文，用 getCachedAPIResponse 获取尚未处理的 JSAPI（chooseImage） 返回值，恢复上下文
4. 由于已经拿到了 JSAPI 返回值，无需再调用耗内存的 JSAPI，可以继续执行之后的业务流程

![流程图](https://down-cdn.dingtalk.com/ddmedia/iwElAqNqcGcDBgTRCGQF0Qn8BrCOF58KyVZ-2gjDsRt-58AAB9IAr0wcCAAJqm9wZW4udG9vbHMKAAvSAAaQlQ.jpg)

### 场景2: 有多个地方 chooseImage 时，需要判断崩溃时是哪里在调用 chooseImage

![alt文本](https://down-cdn.dingtalk.com/ddmedia/iwElAqNwbmcDBgTRAtAF0QYIBrBP5MKnBPEqaAjDsaFh_t8AB9IAr0wcCAAJqm9wZW4udG9vbHMKAAvSAAV8_A.png)

1. 业务每次 chooseImage 前，用 localStorage 标记一下此处的 JSAPI 开始调用，JSAPI 回调后清除标记，再用 localStorage 保存 JSAPI 返回值，用 removeCachedAPIResponse 清除 JSAPI 缓存
2. 下次页面崩溃刷新时，从 localStorage 里获取 JSAPI 执行状态，如果有 JSAPI 尚未返回的标记，就用 getCachedAPIResponse 获取 JSAPI 返回值缓存，由于缓存是一个数组，会记录多次，只取最后一次返回值即可

![流程图](https://down-cdn.dingtalk.com/ddmedia/iwElAqNqcGcDBgTRB4wF0Q0XBrCXPn4cF_pyYQjDsn65p1MAB9IAr0wcCAAJqm9wZW4udG9vbHMKAAvSAAe2vg.jpg)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11929) |
| 小程序 | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11929) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）返回值是个字典，key 是每个 JSAPI 的名称，value 是个数组，数组的每一项是缓存的 JSAPI 返回值

## **示例****代码**

### 默认Demo标题

```
dd.getCachedAPIResponse({
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{}
```
