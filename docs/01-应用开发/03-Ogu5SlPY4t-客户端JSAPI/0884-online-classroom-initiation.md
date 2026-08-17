---
title: "发起在线课堂"
source_url: "https://open.dingtalk.com/document/development/online-classroom-initiation"
namespace: "development"
slug: "online-classroom-initiation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 在线课堂 > 发起在线课堂"
doc_id: "HO4XBh47aw"
updated_at: "2025-09-17 20:57:37"
---

> Source: https://open.dingtalk.com/document/development/online-classroom-initiation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 在线课堂 > 发起在线课堂
> Updated: 2025-09-17 20:57:37

# 发起在线课堂

调用**biz.live.startClassRoom**发起在线课堂。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

使用该接口，发起公开的在线课堂。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 不支持 | 不支持 | 支持（钉钉版本≥5.1.16） |

```
dd.biz.live.startClassRoom({
  startParam: {
    liveUuid:"ee03cba7-xxxxx",
  },
  success:function(result) {
  },
  fail:function(err) {
  }

});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| startParam | Object | 直播的uuid，可以调用[创建直播](https://open.dingtalk.com/document/orgapp/create-live-streaming)接口获取。 |
| onSuccess | Function | 调用成功的回调函数。 |
| onFail | Function | 调用失败的回调函数。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| 1 | 在线课堂已结束。 |
| 2 | 参数错误。 |
