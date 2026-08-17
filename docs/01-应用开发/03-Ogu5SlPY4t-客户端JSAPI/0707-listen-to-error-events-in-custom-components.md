---
title: "监听自定义组件内的error事件"
source_url: "https://open.dingtalk.com/document/development/listen-to-error-events-in-custom-components"
namespace: "development"
slug: "listen-to-error-events-in-custom-components"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 应用级事件 > 监听自定义组件内的error事件"
doc_id: "l23eD4z9DY"
updated_at: "2025-09-17 21:00:53"
---

> Source: https://open.dingtalk.com/document/development/listen-to-error-events-in-custom-components
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 应用级事件 > 监听自定义组件内的error事件
> Updated: 2025-09-17 21:00:53

# 监听自定义组件内的error事件

调用**dd.onComponentError**监听小程序自定义组件内部JS代码的error事件。

## 扫码体验

![监听小程序自定义组件内部 JS 代码的 error 事件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2411855461/p407124.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。

## 示例代码

> **[!NOTE]**
>
> 示例代码以小程序index页面引入component自定义组件的用法为例。

### component的axml示例代码

```
<view>
  <button size="default" type="primary" onTap="handleError">触发自定义组件异常</button>
</view>
```

### component的js示例代码

```
Component({
  mixins: [],
  data: {
  },
  props: {},
  didMount() {},
  didUpdate() {},
  didUnmount() {},
  methods: {
    handleError(){
      throw new Error('component error');
    }
  },
});
```

### index.axml示例代码

```
<view>
  <view class="page-description"></view>
  <view class="page-section">
    <view class="page-section-title">自定义组件</view>
    <view class="page-section-demo">
      <my-component />
      <button size="default" type="primary" onTap="handleCancel">取消监听</button>
    </view>
  </view>
</view>
```

### index.js示例代码

```
Page({
  data: {},
  onLoad() {
    dd.onComponentError(this.callBack);
  },
  callBack(error, method, component){
    dd.alert({
      title:"监听自定义组件内的error异常",
      content:JSON.stringify(error)+JSON.stringify(method)+JSON.stringify(component),
    });
  },
  handleCancel(){
    dd.offComponentError(this.callBack);
  },
});
```

## 入参说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| 回调函数 | Function | 自定义组件内部 JS 代码运行抛出错误时的回调函数。 |

## 回调函数说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| error | Error | 标准error对象。 |
| method | String | 抛出错误的具体方法。 |
| component | Component | Component实例。 |
