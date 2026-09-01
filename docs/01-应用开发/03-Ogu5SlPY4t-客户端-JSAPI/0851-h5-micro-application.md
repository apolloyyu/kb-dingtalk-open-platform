---
title: "h5微应用"
source_url: "https://open.dingtalk.com/document/development/h5-micro-application"
namespace: "development"
slug: "h5-micro-application"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 常见问题 > h5微应用"
doc_id: "C51XPJoIXO"
updated_at: "2026-07-22 16:25:13"
---

> Source: https://open.dingtalk.com/document/development/h5-micro-application
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 常见问题 > h5微应用
> Updated: 2026-07-22 16:25:13

# h5微应用

本文介绍了H5微应用的常见问题。

- **H5微应用是否支持去掉钉钉自带的导航栏？**

  答：若需去掉钉钉自带的导航栏，可以考虑通过[微应用页面全屏展示](0827-full-screen-display-of-microapplication-page.md)来实现。
- **获取微应用免登授权码报错{ errorCode: 9, errorMessage: "对应企业没有 xxx 域名微应用" }**

  答：调用[获取微应用免登授权码](0716-obtain-the-micro-application-exemption-authorization-code.md)接口出现上述报错时，其可能原因包括但不限于以下几点：

  - corpid入参不正确
  - H5微应用中应用首页地址跳转到非本应用服务器页面(跳转到重定向页面)也会报上述错误异常
  - 根据入参的corpid值未检测出该企业下H5微应用-开发管理-应用首页地址中有上述错误信息中的域名(需确保微应用中应用首页地址中域名有错误信息中的提示域名则正常)。
- 导航栏背景色设置色差问题

  答：Android端[设置导航栏颜色](0746-set-the-navigation-bar-color.md)出现背景色差是策略设计如此，起到颜色过渡的效果。![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/W4j6OJrPZyAeO3p8/img/88475552-de89-4a58-a01c-877ce03a41cb.png)
- 钉钉iOS H5微应用缓存不更新

  答：更新钉钉H5微应用出现未能更新完成的可能原因包括但不限于以下情况：

  - 缓存更新目前基本都是由操作系统/Web内核控制，由于Android与iOS平台不同，细节略有差别；
  - HTTP的缓存协议是标准开放协议(很多系统都有实现)，需要企业自行排查下配置协议情况。
  - 如希望系统发布可立即同步到新版，建议通过在请求URL上加时间戳的方式进行，这样能使本地缓存废弃来保证尽早生效为新版。
- **H5微应用唤起摄像拍照如何实现?**

  答：目前H5微应用未提供拍照API文档，可使用input实现：<input type="file" name="pic" accept="image/\*" capture="user">。目前针对accept属性v6.5.20版本已支持，multiple暂不支持。
- **调用JSAPI 时提示Not in DingTalk PC webview**

  答：微应用开发 调用JSAPI 时提示上述错误的原因可能如下：

  钉钉目前提供的前端H5 JSAPI，需要在钉钉容器环境内打开，如果环境不正确会报上述错误。

  例如：需要在钉钉移动端Android端、iOS端打开，或者钉钉PC端 Windows端、mac端打开等，在浏览器里打开会报错。
- **调用biz.util.share分享的页面，安卓与iOS表示不一致**

  答：调用[分享](0742-share-1.md)出现上述原因可能如下:

  由于设计原因，https链接在iOS上分享样式不是卡片样式，如果URL使用https协议iOS端不会解析成卡片样式 使其安卓与iOS页面不一致。
- **H5微应用调用预览钉盘文件，审批附件图片提示：图片已被删除**

  答：调用[预览钉盘文件](0785-preview-nail-plate-file.md)出现上述错误的原因可能如下:

  查看上传的审批附件时:excel、word文件格式不需要授权即可预览，但图片格式需[授权预览审批附件](https://open.dingtalk.com/document/orgapp/preview-authorization-attachment-pop)才可以正常预览。
- **调用H5微应用接口报错{errorCode: "7",errorMessage: "API not authed"}**

  答：调用微应用jsapi接口报上述错误的原因可能如下:

  因未JSAPI鉴权导致，需先完成[JSAPI鉴权](0002-jsapi-authentication.md)。
