---
title: "IntersectionObserver.observe"
source_url: "https://open.dingtalk.com/document/development/jsapi-intersection-observer-observe"
namespace: "development"
slug: "jsapi-intersection-observer-observe"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > IntersectionObserver.observe"
doc_id: "CZSYZwwors"
updated_at: "2025-08-27 18:06:14"
---

> Source: https://open.dingtalk.com/document/development/jsapi-intersection-observer-observe
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 节点查询 > IntersectionObserver.observe
> Updated: 2025-08-27 18:06:14

# IntersectionObserver.observe

调用IntersectionObserver.observe，指定目标节点并开始监听相交状态变化情况。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10037) |

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

- `targetSelector`（string，必填）：选择器。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `time`（number，必填）：相交检测时的时间戳。
- `relativeRect`（object，必填）：参照区域的边界。
- `relativeRect.left`（number，必填）：左边界。
- `relativeRect.right`（number，必填）：右边界。
- `relativeRect.top`（number，必填）：上边界。
- `relativeRect.bottom`（number，必填）：下边界。
- `intersectionRect`（object，必填）：相交区域的边界。
- `intersectionRect.left`（number，必填）：左边界。
- `intersectionRect.right`（number，必填）：右边界。
- `intersectionRect.top`（number，必填）：上边界。
- `intersectionRect.bottom`（number，必填）：下边界。
- `intersectionRatio`（number，必填）：相交比例。
- `boundingClientRect`（object，必填）：目标边界。
- `boundingClientRect.left`（number，必填）：左边界。
- `boundingClientRect.right`（number，必填）：右边界。
- `boundingClientRect.top`（number，必填）：上边界。
- `boundingClientRect.bottom`（number，必填）：下边界。

## **示例****代码**

### 默认出入参

```
const intersectionObserver = dd.IntersectionObserver();

intersectionObserver.observe('xxId', (res) => {
  const {
    time,
    relativeRect,
    intersectionRect,
    intersectionRatio,
    boundingClientRect,
  } = res;
});
```

`callback`返回对象示例：

```
{
  "time": 1677725294970,
  "relativeRect": { "top": 50, "left": 0, "right": 100, "bottom": 200 },
  "intersectionRect": { "top": 50, "left": 0, "right": 100, "bottom": 200 },
  "intersectionRatio": 0.5,
  "boundingClientRect": { "top": 50, "left": 0, "right": 100, "bottom": 200 }
}
```
