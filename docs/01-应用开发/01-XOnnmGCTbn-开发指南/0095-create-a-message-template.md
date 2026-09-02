---
title: "创建消息模板"
source_url: "https://open.dingtalk.com/document/dingstart/create-a-message-template"
namespace: "dingstart"
slug: "create-a-message-template"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 创建消息模板"
doc_id: "H8BLfcUp6M"
updated_at: "2026-07-22 16:55:30"
---

> Source: https://open.dingtalk.com/document/dingstart/create-a-message-template
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 创建消息模板
> Updated: 2026-07-22 16:55:30

# 创建消息模板

在发送互动卡片消息前，需要先创建消息模板。

## 创建模板

1. 登录[钉钉企业管理后台](https://oa.dingtalk.com)。
2. 进入[钉钉互动卡片搭建平台](https://h5.dingtalk.com/interactive-card-builder/index.html#/)，在搭建平台上则可以看到当前组织内所创建的所有互动消息模板。
3. 单击右上角的**新增模板**创建新的模板。

   ![新增模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3305430161/p208340.png)
4. 创建完模板之后会生成一个模板ID ，后续发送卡片会使用到该模板ID。

## 编辑模板

模板创建完成之后会自动跳转到模板编辑页面，模板编辑页面由三部分组成，分别是：左边的组件、变量设置区，中间的编辑画板区，右边的组件设置区，如下图所示：![编辑页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8140319361/p203849.png)

这里我们以搭建一个审批卡片为例，展示一下如何通过可视化搭建的方式来快速搭建一个卡片：

![审批卡片例子](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3627468061/p204627.png)

### **设置头部**

在左边的组件库中找到**卡片头部**，并且拖拽到中间的画板中，在画板中选中卡片头部组件，即可在右边的设置区域设置组件的属性，如卡片标题，标题颜色等：

![设置卡片标题](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3627468061/p204632.png)

### **设置内容**

和卡片头部组件类似，卡片内容的搭建也是通过拖拽相应的内容组件到画板中，并且设置相关属性。在左边的组件库中找到“标题“组件，并且拖拽到画板中，在设置区域设置标题的内容。标题内容既可以设置静态内容，也可以设置动态内容。动态内容通过占位符的形式来表达，如下图：

![设置动态内容](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3627468061/p204635.png)当设置完标题内容之后，还需要为动态内容创建变量，这样才可以通过变量的形式来替换占位符的内容。在编辑器左边打开“变量列表“的 Tab ，并且新增两个字符串类型的变量，分别是“user“ 和 “approval“：

![新增变量](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4627468061/p204638.png)为了能够更加真实地模拟发出去的卡片，你还可以在变量列表的 Tab 里增加 mock 数据，如对 “user“ 和 “approval“ 变量增加 mock 数据，这样就能在中间的画板上看到实际替换效果：

![设置 mock 数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4627468061/p204641.png)

> **[!IMPORTANT]**
>
> mock 数据只是帮助你在搭建卡片的过程中更好地预览搭建效果，在真实发送卡片时数据以发卡片时所使用的数据为准。

卡片的正文设置方式和标题一样，这里我们新增三行正文，并且设置对应的变量：

![设置正文](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4627468061/p204648.png)如果内容需要支持国际化，那么可以在右边内容输入区域开启“支持国际化“的选项，同时输入对应的其他语言的内容。设置完毕之后，可以通过中间画板上方的 toolbar 来模拟对应的语言：

![国际化支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4627468061/p204650.png)目前支持设置7种语言，分别是：简体中文、繁体中文、英文、日文、越南文、泰文、印尼文，分别对应钉钉客户端所支持的7种语言。当钉钉客户端所使用的语言发生改变时，卡片内容也会根据所设置的内容发生相应的变化。

> **[!IMPORTANT]**
>
> 当某个语言没有设置对应的内容时，会使用简体中文的内容作为默认文案。

以上则完成了审批卡片的内容部分的搭建。除了上面所使用到的组件之外，你也可以使用平台提供的其他组件，如辅助信息、图片、布局容器等组件，使用方式和标题组件类似。

### **设置操作区**

在左边组件库里找到“横排按钮“组件，并拖拽到画布当中，在右边的组件设置区域即可修改、增加按钮。这里我们创建两个按钮，分别是红色的“拒绝“以及蓝色的“同意“按钮：

![按钮](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9533888061/p204662.png)按钮的点击事件有两种响应方式，一种是链接跳转，一种是回传数据。

链接跳转的响应方式需要配置所需要跳转的 URL ，URL 可以是一个多平台统一的链接，也可以根据不同的平台来配置不同的链接。如果是回传数据的响应方式，那么可以配置回传的具体参数。当用户点击了按钮之后，卡片会向你在开放平台注册的回调地址发送一个请求，表明用户点击了当前的按钮。

如果按钮的状态设置成**禁用**模式，那么按钮的点击事件会被忽略，即用户点击按钮后不会有任何响应。

## 发布模板

![发布卡片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0633888061/p204665.png)

当卡片编辑完成之后即可进入发布阶段。点击右上角的**发布**按钮，会弹出确认弹窗。当发布完成之后，卡片就能使用了。

> **[!IMPORTANT]**
>
> 目前卡片模板一旦发布之后无法再次编辑，所以请确保在完成卡片内容编辑之后再发布。如果想临时保存卡片的编辑状态，可以点击右上角的**保存**按钮，下次可以继续接着编辑。
