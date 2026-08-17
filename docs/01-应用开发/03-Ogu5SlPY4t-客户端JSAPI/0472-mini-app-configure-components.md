---
title: "组件配置"
source_url: "https://open.dingtalk.com/document/development/mini-app-configure-components"
namespace: "development"
slug: "mini-app-configure-components"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件配置"
doc_id: "sgWHHkgaej"
updated_at: "2025-09-17 20:58:08"
---

> Source: https://open.dingtalk.com/document/development/mini-app-configure-components
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件配置
> Updated: 2025-09-17 20:58:08

# 组件配置

开发者需要在.json文件和.js文件中添加组件配置。

开发者需要在.json文件中指明自定义组件的依赖。

```
{
  "component": true,
  "usingComponents": {
    "c1":"../x/index"
  }
}
```

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| component | Boolean | 是 | 指明是组件。 |
| usingComponents | Object | 否 | 指明依赖的组件所在的路径： 项目绝对路径以 / 开头，相对路径以 ./ 或者 ../ 开头，npm 路径不以 / 开头。 |

开发者需要在`.js`文件中调用Component定义组件。

```
Component({
  mixins:[{ didMount() {}, }],
  data: {y:2},
  props:{x:1},
  didUpdate(prevProps,prevData){},
  didUnmount(){},
  methods:{
    onMyClick(ev){
      dd.alert({});
      this.props.onXX({ ...ev, e2:1});
    },
  },
})
```
