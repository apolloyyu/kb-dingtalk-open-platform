---
title: "设置左侧导航按钮文本"
source_url: "https://open.dingtalk.com/document/development/set-left-navigation-button-text"
namespace: "development"
slug: "set-left-navigation-button-text"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 设置左侧导航按钮文本"
doc_id: "kk4IcTG8tB"
updated_at: "2025-09-17 20:56:25"
---

> Source: https://open.dingtalk.com/document/development/set-left-navigation-button-text
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 设置左侧导航按钮文本
> Updated: 2025-09-17 20:56:25

# 设置左侧导航按钮文本

调用**biz.navigation.setLeft**设置左侧导航按钮文本。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.navigation.setLeft)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 支持 | 支持 |

- Android：导航栏左侧显示的是标题，若想在Android设备上拦截返回按钮的行为，请参考事件回调。
- iOS端：

  ![返回](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7605834061/p177959.png)

  ```
  dd.biz.navigation.setLeft({
      control: true,//是否控制点击事件，true 控制，false 不控制， 默认false
      text: '',//控制显示文本，空字符串表示显示默认文本
      onSuccess : function(result) {
          /*
          {}
          */
          //如果control为true，则onSuccess将在发生按钮点击事件被回调
      },
      onFail : function(err) {}
  });
  ```

  | 参数 | 类型 | 说明 |
  | --- | --- | --- |
  | control | Boolean | 是否控制点击事件：  - **true**：控制 - **false**（默认）：不控制 |
  | text | String | 控制显示文本，空字符串表示显示默认文本。 |
- PC端：只在SlidePanel里起作用

  ```
  dd.biz.navigation.setLeft({
      text: "lalala",//显示文字信息
      onSuccess : function(result) {
          /**/
      },
      onFail : function() {}
  })
  ```

  | 参数 | 类型 | 说明 |
  | --- | --- | --- |
  | text | String | 显示文字信息。 |

## PC端左侧按钮点击事件，添加监听回调函数

```
//添加监听回调函数
dd.on('leftBtnClick', handleFn);
```

## 左侧按钮点击事件，移除相应handleFn的监听回调函数

```
//移除相应handleFn的监听回调函数
dd.off('leftBtnClick', handleFn);
```
