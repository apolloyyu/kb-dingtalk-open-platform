---
title: "使用事件链实现卡片互动"
source_url: "https://open.dingtalk.com/document/development/using-event-chains-for-card-interaction"
namespace: "development"
slug: "using-event-chains-for-card-interaction"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "搭建平台 > 使用教程 > 使用事件链实现卡片互动"
doc_id: "0vRvkXkehk"
updated_at: "2026-05-19 17:05:16"
---

> Source: https://open.dingtalk.com/document/development/using-event-chains-for-card-interaction
> Path: 互动卡片 / 模板搭建卡片 / 搭建平台 > 使用教程 > 使用事件链实现卡片互动
> Updated: 2026-05-19 17:05:16

# 使用事件链实现卡片互动

本文基于一个会议邀请卡片，介绍了如何使用事件链绑定卡片事件以及如何通过响应回传请求事件来实现卡片互动。

## 步骤一：添加交互组件并设置可见性

这是一个会议邀请卡片的需求，需要在卡片上展示会议的基本信息以及一个“确认参加”按钮，参会者点击该按钮后，按钮文案需要变成“已确认”，且按钮需要变成不可点击状态。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837088.png)![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8261286271/p837101.png)

在之前的教程中，我们已经完成了部分卡片的搭建，接下来我们需要添加一个按钮组件，供用户点击操作。这里要注意，这个按钮需要有两种状态，且两种按钮状态所对应的文案也有所不同。

要实现这个需求我们有两种方法。第一种方案是将按钮的文案、颜色与禁用状态等均绑定变量，不过这种方式需要定义三个变量，稍微显得有些复杂。

第二种方案是我们搭建两个不同的按钮，通过一个布尔类型的变量来控制它们的可见性。这种方式逻辑比较简明，搭建难度较低，在实际的卡片场景中应用也较为广泛，所以我们选择这种方式作为演示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837102.png)

因为是否确认参会的状态对于每一个参与者是不同的，所以，这个变量需要设置成私有的。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837103.png)

要注意的是，元素的可见性只有在预览模式下才会生效，在搭建模式下，所有元素都是可见的。在可见性设置完成后，我们可以切换到预览模式，预览卡片样式。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837104.png)

至此，我们完成了这个卡片模板所有的静态元素的搭建。

## 步骤二：使用事件链绑定卡片交互事件

卡片按钮有多种交互事件可供绑定

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837105.png)

回传请求是唯一一种可以与业务服务端通信的事件，业务服务端在收到来自卡片的请求后，可以根据收到的参数来对卡片进行对应的更新操作。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837106.png)

事件链本身不是一个单一的事件，而是一系列事件的组合，我们可以在事件链中配置各种事件的串行与并行逻辑。需要特别注意的是，事件链中添加的多个事件虽然会依次执行，但是后一个事件并不会等待前一个事件的结束，所以本质上相当于并行的逻辑。如果希望实现串行的效果，需要在前一个事件中配置“事件回调”。

对于我们这个应用场景，我们选择事件链作为点击事件。我们先配置一个“回传请求”，在回传请求成功后，再配置一个弹窗提示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837107.png)

目前只有“容器”组件和“按钮”组件支持点击事件的配置，在搭建卡片模板的过程中，我们遇到的比较常见的问题是，用户希望在其他类型的组件上也支持点击事件。如果遇到这种情况，最便捷的解决方案是给这个目标元素的外层嵌套一个“容器”组件，然后在这个嵌套的“容器”组件上绑定点击事件即可。

## 步骤三：注册卡片回调

目前钉钉提供了基于HTTP服务的回调和基于Stream模式的回调两种回调模式。

使用HTTP回调模式，需要开发者提供一个公网可访问的域名，钉钉会通过http请求将回调信息发送到开发者应用程序。

使用Stream回调模式，开发者可以做到"五零接入"，即零公网IP，零域名，零证书，零网关，零内网穿透工具，开发者通过钉钉SDK建立到钉钉的TCP持久连接，钉钉通过TCP连接推送回调信息到开发者应用程序。

两种回调的使用方式可以参考卡片文档中 操作流程 / 卡片互动 / 事件回调部分。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837108.png)

依照我们之前案例的操作方式，我们在机器人监听函数中，监听meeting的信息，以推送我们刚刚搭建的会议邀请卡片。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837109.png)

然后，我们配置卡片回传请求的监听函数。我们可以通过读取回传请求参数中我们传入的action字段，来判定具体执行哪种操作。在这里，我们为发起回传请求事件的用户设置私有变量，来改变他的卡片状态。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837110.png)

接下来，我们在测试组织中测试一下我们刚刚的这张会议邀请卡片逻辑。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2561286271/p837111.png)

可以看到，第一位用户点击了卡片上的“确认”按钮后，他自己的会议邀请状态发生了变更，同时卡片按钮的状态也发生了变化，这样，我们就实现了会议邀请这样一个业务需求。

## 视频演示

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240920/ljcjpj/%E4%BD%BF%E7%94%A8%E4%BA%8B%E4%BB%B6%E9%93%BE%E5%AE%9E%E7%8E%B0%E5%8D%A1%E7%89%87%E4%BA%92%E5%8A%A8.mp4)
