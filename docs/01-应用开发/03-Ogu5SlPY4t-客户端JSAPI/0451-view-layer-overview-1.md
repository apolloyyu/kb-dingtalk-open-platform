---
title: "视图层概述"
source_url: "https://open.dingtalk.com/document/development/view-layer-overview-1"
namespace: "development"
slug: "view-layer-overview-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 视图层概述"
doc_id: "vODEBKoVbZ"
updated_at: "2025-09-17 20:57:56"
---

> Source: https://open.dingtalk.com/document/development/view-layer-overview-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 视图层概述
> Updated: 2025-09-17 20:57:56

# 视图层概述

视图文件的后缀名是`axml`，定义了页面的标签结构。AXML是小程序框架设计的一套标签语言，用于描述小程序页面的结构。

AXML语法可分为五个部分：

- **数据绑定**

  ```
  <view> {{message}} </view>
  ```

  ```
  // page.js
  Page({
    data: {
      message: 'Hello dingtalk!'
    }
  })
  ```

- **列表渲染**

  ```
  <view a:for="{{items}}"> {{item}} </view>
  ```

  ```
  // page.js
  Page({
    data: {
      items: [1, 2, 3, 4, 5, 6, 7]
    }
  })
  ```
- **条件渲染**

  ```
  <view a:if="{{view == 'WEBVIEW'}}"> WEBVIEW </view>
  <view a:elif="{{view == 'APP'}}"> APP </view>
  <view a:else> dingtalk </view>
  ```

  ```
  // page.js
  Page({
    data: {
      view: 'dingtalk'
    }
  })
  ```

- **模板**

  ```
  <template name="staffName">
    <view>
      FirstName: {{firstName}}, LastName: {{lastName}}
    </view>
  </template>

  <template is="staffName" data="{{...staffA}}"></template>
  <template is="staffName" data="{{...staffB}}"></template>
  <template is="staffName" data="{{...staffC}}"></template>
  ```

  ```
  // page.js
  Page({
    data: {
      staffA: {firstName: 'san', lastName: 'zhang'},
      staffB: {firstName: 'si', lastName: 'li'},
      staffC: {firstName: 'wu', lastName: 'wang'},
    },
  })
  ```
- **事件**

  ```
  <view onTap="add"> {{count}} </view>
  ```

  ```
  Page({
    data: {
      count: 1
    },
    add(e) {
      this.setData({
        count: this.data.count + 1
      })
    }
  })
  ```
