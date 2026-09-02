---
title: "链接转卡片"
source_url: "https://open.dingtalk.com/document/development/link-dingtalk-chat"
namespace: "development"
slug: "link-dingtalk-chat"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 常见问题 > 链接转卡片"
doc_id: "faH5rmy91q"
updated_at: "2026-07-22 16:25:15"
---

> Source: https://open.dingtalk.com/document/development/link-dingtalk-chat
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 常见问题 > 链接转卡片
> Updated: 2026-07-22 16:25:15

# 链接转卡片

钉钉支持在聊天中发送链接时自动转换为链接卡片消息，以丰富消息内容，提升消息阅读者查看效率。

## **实现原理**

钉钉会尝试访问和分析聊天输入框中的链接的网页内容，并根据OGP协议（全称Open Graph Data协议）提取其中的标签作为分享标签的内容。显示效果如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5178074871/p483767.png)

OGP协议是一套Metatags的规格，用来标注页面，告诉我们你的网页快照。帮助社交app高效并准确的获取网页中的核心链接、标题、主图、正文摘要等信息，使得该网页在社交分享中有更好的展现体验。

如果网页不支持OGP，那么基于算法和规则来提取网页中标题、主图、正文摘要，准确性无法做到100%，体验也不能充分保证。尤其是有部分页面html采用前端js渲染，而不是服务端渲染，会导致无法提取主图、正文摘要，链接卡片体验感不好。

## **如何适配Open Graph Data**

只需要在页面的HTML标签中增加以下meta标签即可。

```
<!-- Place this data between the <head> tags of your website -->

<!-- Open Graph data -->
<meta property="og:title" content="Title Here" />
<meta property="og:url" content="http://www.example.com/" />
<meta property="og:image" content="http://example.com/image.jpg" />
<meta property="og:description" content="Description Here" />
```

> **[!IMPORTANT]**
>
> 出于性能和体验考虑，链接转卡片服务不支持执行HTML中的js，上述Metatags必须在服务端渲染。

## **推荐使用场景**

在电商体系中，经常会有一些活动页面和H5游戏页面，整个页面内容都在前端通过js渲染。导致链接分享到钉钉时，钉钉无法有效的从访问到的HTML信息中，提取有效的主图和正文摘要，使得分享卡片体验非常差，影响传播效果。

而通过适配OGP协议，只需在Metatags中进行简单的适配，即可获得较好的体验，同时，分享卡片样式可以灵活的自定义。

淘宝、支付宝已经在多个电商活动、H5游戏中通过适配OGP协议，改善了传播体验。

目前已有很多网页可以支持OGP协议。

- [阿里云官网](https://www.aliyun.com)
- [钉钉](https://www.dingtalk.com/)
- [苹果官网](https://www.apple.com)

## **参考示例**

可以参考网站 [https://www.apple.com](https://www.apple.com/)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7553897661/p510097.png)

## **常见问题**

- **通过js动态渲染的meta头，是否可以支持？**

  答：当前不保证支持，受限于访问方式，建议由服务端渲染meta头。
- **我们网站移动端和PC端页面是不一样的，是否都需要适配？**

  答：是的，都需要适配好相应的meta头，钉钉访问时，会根据访问效果，不定期调整访问策略，可能是移动端的User-Agent，也可能是PC端的User-Agent，以提升访问效果，优化链接卡片体验。
- **我们网站适配OGP后，是否只在钉钉上有好的链接卡片体验？**

  答：不仅仅是钉钉，OGP是个开放协议，包括Facebook在内的大量社交app都支持了OGP协议，如果网页适配了OGP协议，那么在这些app中都会有非常好的链接卡片体验。
- **钉钉上链接转卡片服务会提升哪些场景下链接体验？**

  答：除了上面描述的聊天之外，通过手机浏览器分享到钉钉（例如Safari中分享到钉钉），或者钉钉聊天中打开链接的页面，分享到钉钉。这些场景都会通过OGP协议提取链接卡片信息，实现更好的分享体验。
- **如果我不需要卡片，需要原始链接怎么办？**

  答：升级到钉钉最新版本，可以在链接卡片上看到复制按钮，通过复制按钮，可以复制原始的链接。
- **如果不希望消息中链接被转成卡片，可以怎么做？**

  答：当前可以有两种方式，一种是发送代码，以代码形式发送的链接不会被转成卡片消息，另一种是文字和链接一起发送，也不会被自动转换。
- **钉钉链接转卡片是否有缓存？我们网页中信息已经更新了，但是转换出来的链接卡片还是旧的。**

  答：目前在服务端访问时没有缓存，但是为了提升体验，在客户端上（包括移动端和桌面端）有内存缓存，重启钉钉后，缓存自动失效。

  > **[!IMPORTANT]**
  >
  > 已经转成卡片的消息不再更新，如果测试的话，可以重新发一次来验证。
- **我们内网链接不希望被访问怎么办？**

  答：钉钉链接卡片的访问，采用的是阿里云公有云服务器，内网网站正常做好网络隔离、权限控制即可。例如仅限内网用户访问，或者设置必须合法登录才能访问等。
- **我们内网链接希望转成更友好的卡片消息怎么办？**

  答：为了避免企业内网信息泄漏，钉钉链接转卡片服务不会针对内网做穿透等访问，暂时不会提供针对内网的访问服务和方案。如果希望内网页面有个好的链接卡片样式，可以针对未登录用户，参考上述技术描述，增加相应的OGP Metatags来自定义链接卡片样式。
- **该服务的预览有什么标识吗？**

  答：可以通过这个User-Agent来识别：DingTalk-LinkService/1.0
- **我们网站是正常的，为什么链接转卡片后标题/描述中出现类似“验证码”、“当前请求存在恶意行为已被系统拦截……”等异常信息？**

  答：请检查网站的安全策略模块，是否把钉钉的预览自动加入到黑名单中。

  > **[!NOTE]**
  >
  > 可以通过上面的User-Agent来识别钉钉预览服务。

## **参考资料**

- [Must-Have Social Meta Tags for Twitter, Google+, Facebook and More](https://moz.com/blog/meta-data-templates-123)
- [OGP, The Open Graph protocol](http://ogp.me/)

  > **[!NOTE]**
  >
  > 如果因为网络原因无法访问，请尝试可用的网络加速方式。
