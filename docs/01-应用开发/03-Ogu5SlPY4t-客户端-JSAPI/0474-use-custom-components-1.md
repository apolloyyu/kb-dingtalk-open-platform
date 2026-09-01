---
title: "使用自定义组件"
source_url: "https://open.dingtalk.com/document/development/use-custom-components-1"
namespace: "development"
slug: "use-custom-components-1"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 使用自定义组件"
doc_id: "ziO83kM0qC"
updated_at: "2026-09-01 09:16:30"
---

> Source: https://open.dingtalk.com/document/development/use-custom-components-1
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 使用自定义组件
> Updated: 2026-09-01 09:16:30

# 使用自定义组件

## 引用自定义组件

```
// page.json 注意，不是在app.json里配置
{
  "usingComponents":{
    "your-custom-component":"mini-antui/es/list/index",
    "your-custom-component2":"/components/card/index",
    "your-custom-component3":"./result/index",
    "your-custom-component4":"../result/index"
  }
}

// 项目绝对路径以 / 开头，相对路径以 ./ 或者 ../ 开头，npm 路径不以 / 开头
```

## 使用自定义组件

```
// page.axml
<list>
  <view slot="header">列表头部</view>
  <block a:for="{{items}}">
    <list-item key="item-{{index}}">
      {{item.title}}
      <view class="am-list-brief">{{item.brief}}</view>
    </list-item>
  </block>
  <view slot="footer">列表尾部</view>
</list>
```
