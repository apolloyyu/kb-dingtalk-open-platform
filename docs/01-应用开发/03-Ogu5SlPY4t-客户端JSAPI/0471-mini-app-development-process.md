---
title: "开发流程"
source_url: "https://open.dingtalk.com/document/development/mini-app-development-process"
namespace: "development"
slug: "mini-app-development-process"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发流程"
doc_id: "XROpePtt4V"
updated_at: "2025-09-17 20:58:07"
---

> Source: https://open.dingtalk.com/document/development/mini-app-development-process
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发流程
> Updated: 2025-09-17 20:58:07

# 开发流程

自定义组件功能可将需要复用的功能模块抽象成自定义组件，从而在不同页面中复用。一个自定义组件由axml、js、acss、json组成。

创建并使用自定义组件有以下 4 个步骤：

1. 新建自定义组件文件夹。
2. 在 `.json` 文件中声明自定义组件。
3. 使用 `Component` 函数，注册自定义组件。
4. 使用自定义组件。

## 步骤一：新建自定义组件文件夹

1. 在小程序IDE中打开一个空白或已有项目，然后在左侧文件栏新建一个`components`文件夹。
2. 右键单击`components`文件夹，然后选择**新建小程序组件**。

   ![新建小程序组件 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2166994061/p180277.png)
3. 在弹出的页面中，输入组件名例如index。IDE会自动生成自定义组件所需的文件。

   ![自定义组件文件夹](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9415994061/p180278.png)

## 步骤二：声明自定义组件

组件配置文件 `index.json` 用于声明当前目录是个自定义组件。开发者需要在`.json`文件中指明自定义组件的依赖。

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

## 步骤三：注册自定义组件

`index.js` 用于注册一个组件对象。开发者需要在`.js`文件中调用Component定义组件。如下：

```
Component({
  mixins:[{ didMount() {}, }], // minxin 方便复用代码
  data: {y:2},  // 组件内部数据
  props:{x:1},  // 可给外部传入的属性添加默认值
  didUpdate(prevProps,prevData){}, // 生命周期函数
  didUnmount(){},
  methods:{  // 自定义方法
    onMyClick(ev){
      dd.alert({});
      this.props.onXX({ ...ev, e2:1});
    },
  },
})
```

## 步骤四：使用组件

声明好一个组件后，即可在其他页面上使用。

先在页面配置中说明要使用哪个自定义组件，主要指定组件标签名字和组件所在路径。

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

然后在页面中引用组件即可。

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
