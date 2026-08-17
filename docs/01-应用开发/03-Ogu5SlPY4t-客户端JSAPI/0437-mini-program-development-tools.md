---
title: "小程序开发工具"
source_url: "https://open.dingtalk.com/document/development/mini-program-development-tools"
namespace: "development"
slug: "mini-program-development-tools"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序开发工具"
doc_id: "MOnRTtxhkk"
updated_at: "2025-09-17 20:57:46"
---

> Source: https://open.dingtalk.com/document/development/mini-program-development-tools
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序开发工具
> Updated: 2025-09-17 20:57:46

# 小程序开发工具

小程序开发者工具（简称 IDE）是阿里集团一站式小程序研发工具，提供了编码、调试、测试、上传、项目管理等功能。IDE支持钉钉小程序开发。

## 下载IDE

[小程序开发工具](https://open.dingtalk.com/document/resourcedownload/miniapp-tool#topic-1949239)

## 项目创建

打开IDE后，选择**新建项目**或者**打开项目**（比如已有项目或Demo），选择要开发的应用类型：![resize,w_1066 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6644199951/p163464.png)

如果你初次编写小程序代码，可以使用我们提供的“组件/API示例”模板创建项目。![resize,w_1084 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6644199951/p163465.png)

单击**下一步**填写项目名称和项目路径，然后点击**完成**即可。

## 代码编写

打开项目，会默认进入代码编辑模式。从左到右，依次是文件操作区、代码编辑区和预览区。![resize,w_1192 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6644199951/p163466.png)

- 代码编辑

  代码编辑区可以对当前项目进行代码编写和文件的添加、删除以及重命名等基本操作。
- 实时预览

  在代码编辑区修改任何代码都会重新编译，然后自动刷新应用。
- 自动补全

  IDE工具针对dd接口和axml提供了大量的自动补全提示，以帮助开发者提高效率。

## 本地调试

**预览区**

这里可真实模拟在钉钉应用里的表现，并针对绝大部分的API提供了模拟功能。

**调试模式**

点击下方的“调试器”，可切换到调试模式。![resize,w_1212 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7644199951/p163467.png)

小程序调试工具提供了axml和acss的支持，支持组件层级、属性回写等功能；同时也包含了Chrome调试工具中的网络请求、DOM元素检查、源码Debug等。

**出错反馈**

当开发者在axml或者配置文件里编译出错时，保存后会对错误的信息以redbox的形式呈现给开发者。

## 真机预览

使用“钉钉扫码登录”并“关联应用”后，在**开发者工具**右上角单击“**预览**”按钮，选择“**确认推送**”，生成预览二维码，使用手机钉钉扫码预览即可。

> **[!IMPORTANT]**
>
> 请确保左上角已经正确关联了应用和组织，才能推送成功。

![resize,w_1236 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7644199951/p163468.png)![resize,w_1236 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7644199951/p163469.png)

## 真机调试

在IDE上用手机扫码进行真机预览后，ios和android均可以进行真机调试。

#### **在IOS上真机调试**

调试面板的开关在小程序右上角菜单中，选择**打开调试面板**，如下图：![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7644199951/p163470.png)

单击后需要重新进入小程序后调试面板才会生效，这时在小程序通过console就可以打印出调试信息，在下图中显示：![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7644199951/p163471.png)

**在Android上真机调试**

调试面板开关在界面右下角，直接点开即可查看调试信息：![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7644199951/p163472.png)

点击右下角“调试面板”，即可看到调试信息，如下图：![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8644199951/p163473.png)

## 发布版本

在开发者工具右上角点击“**上传”**按钮即可。![resize,w_1246 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8644199951/p163474.png)![resize,w_1246 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8644199951/p163475.png)

发布成功后，可以在开发者后台小程序的**版本管理**进行灰度、发布到线上等版本管理。![resize,w_1254 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8644199951/p163476.png)

## 框架以及组件库

钉钉小程序为开发者提供了标准化的基础框架以及丰富的组件，开发者可以通过组合这些基础组件进行业务开发。

| 名称 | 参考 |
| --- | --- |
| 开发框架 | 请参考[小程序框架概述](https://open.dingtalk.com/document/orgapp/overview-of-mini-program-framework)。 |
| 组件库 | 请参考[view 视图容器](https://open.dingtalk.com/document/orgapp/dd-view-container)。 |
| 基础能力API | 请参考[JSAPI总览](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-overview)。 |
