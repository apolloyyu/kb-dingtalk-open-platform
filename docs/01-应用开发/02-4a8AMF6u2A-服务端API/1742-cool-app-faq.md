---
title: "酷应用常见问题"
source_url: "https://open.dingtalk.com/document/development/cool-app-faq"
namespace: "development"
slug: "cool-app-faq"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 酷应用 > 酷应用常见问题"
doc_id: "FAUX5RCiUC"
updated_at: "2025-10-21 18:15:14"
---

> Source: https://open.dingtalk.com/document/development/cool-app-faq
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 酷应用 > 酷应用常见问题
> Updated: 2025-10-21 18:15:14

# 酷应用常见问题

本文介绍了酷应用常见问题。

## 不同项目类型在群里显示不同快捷入口

答：做项目管理时有多种项目类型，针对不同的项目类型，新建的条目是不一样的，能够决定针对不同的项目类型在群里显示不同的新建的快捷入口。最多可以添加3个快捷入口。![iShot2022-06-09 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6292584561/p448300.png)

## 酷应用是免费的吗？

答：是免费的。

## 如果要申请共创怎么联系？

答：可以联系对应类目小二申请共创，如何联系类目小二，参见[运营支持](https://open.dingtalk.com/document/contactus/mr22h2#topic-1949249)。

## 酷应用精准投放的策略有哪些维度，每个维度具体指标是什么？

答：可以从组织画像，群画像维度进行投放，具体可以联系类目小二。

## 安装酷应用后会返回群主与企业管理员信息吗？

答：安装酷应用后，可以获取到哪些信息，取决于应用本身调用了哪些开放接口。

## 第三方企业应用和企业内部应用在申请接口权限上有区别吗？第三方企业应用是否会有较多限制?

答：有区别。

- 企业内部应用权限申请，请参考[添加接口调用权限](https://open.dingtalk.com/document/orgapp/add-api-permission)。
- 第三方企业应用权限申请，请参考[添加接口调用权限](https://open.dingtalk.com/document/isvapp/add-interface-call-permissions)。

## **如何设计酷应用？**

答：酷应用设计源文件已开放。包含酷应用设计建议及通用样式规范，助力应用酷化体验更优。以及群置顶 、动态卡片、工作台、个人profile、移动端半屏容器和桌面端侧边栏等6个场域设计建议和设计案例模板。可前往[酷应用设计规范](https://ding.design/#/cate/1/page/818)查看下载。

## 如果用户购买的50人，群里有60人怎么办呢，会有使用限制么?

​答：超额的人群无法使用。

## 酷应用的开发是否需要定制开发服务商的资质？

答：取决于开发的应用类型。

- 企业内部使用，可以通过企业内部应用进行开发，不需要服务商的资质。开发流程参见[群聊酷应用开发流程](https://open.dingtalk.com/document/orgapp/group-chat-cool-app-overview)。
- 第三方企业应用，是需要[产品方案商](https://open.dingtalk.com/document/operation-specification/become-an-application-service-provider)资质。开发流程参见[群扩展](https://open.dingtalk.com/document/orgapp/group-chat-cool-app-overview)、[消息菜单](https://open.dingtalk.com/document/isvapp/message-menu-summary)[消息菜单](https://open.dingtalk.com/document/orgapp/message-menu-overview)。
- 委托定制的链路暂不支持。

## 群管理员不是钉钉管理员也可以使用酷应用，群管理员可以购买吗？

答：目前不可以。

## 超链接酷应用创建后，为什么不能修改和删除？

​答：目前在开发者后台不支持修改已经创建的酷应用链接，这一问题会在后续更新版本中进行修复，请关注[酷应用更新日志](https://open.dingtalk.com/document/changelog/cool-application-update-log#topic-2214722)。

## 在应用内选择成员并自动建群的功能，功能是否已开放？

​答：功能已开放，请参见[创建群聊并安装酷应用入群](https://open.dingtalk.com/document/orgapp/create-a-group-chat-and-install-cool-applications-into-the)。

## 群内酷应用和群插件是类似的吗？

答：群插件被称为会话快捷栏，指在群会话框下面快捷栏中的按钮，这些按钮是群内的开放功能，这些功能以酷应用集成的形式绑定在酷应用中。

因此，酷应用和群插件是包含的关系，即一个酷应用可以包含多个群插件，当酷应用安装到群内，就会将开发者开发的群插件也安装到群内。

## 钉钉互动卡片如何支持所有格式？

答：在互动卡片普通版中，可以选择“富文本”组件，参考[互动卡片普通版搭建平台](https://open.dingtalk.com/document/resourcedownload/ding-card-interactive-card-building-platform-new#topic-2215433)，基本可以和大部分Markdown的渲染能力对齐，后续根据用户需求再进行迭代和调整。

## PC端使用的应用功能需要较大的屏幕展现，PC半屏可以自行设置宽度吗？是否有其他的解决方案？

答：PC半屏又称为会话内的侧边栏，目前侧边栏的宽度是受限的。PC端除了通过侧边栏打开页面，还可以通过独立页面以及浏览器打开页面，未来更新内容，请关注[酷应用更新日志](https://open.dingtalk.com/document/changelog/cool-application-update-log#topic-2214722)。
