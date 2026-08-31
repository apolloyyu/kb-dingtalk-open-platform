---
title: "群相关跳转协议"
source_url: "https://open.dingtalk.com/document/dingstart/group-jump-protocol"
namespace: "dingstart"
slug: "group-jump-protocol"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 开发参考 > 群相关跳转协议"
doc_id: "XevUZYKvLm"
updated_at: "2026-01-29 14:52:31"
---

> Source: https://open.dingtalk.com/document/dingstart/group-jump-protocol
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 开发参考 > 群相关跳转协议
> Updated: 2026-01-29 14:52:31

# 群相关跳转协议

## 常用跳转协议

| 跳转页面 | 链接 | 参数 | 示例 |
| --- | --- | --- | --- |
| PC端侧边栏 | dingtalk://dingtalkclient/page/link?url=URL&pc\_slide=true | - **url**：跳转链接，需要进行urlencode。 - **pc\_slide**：固定值**true**。 | dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.dingtalk.com%2F&pc\_slide=true |
| PC端弹窗 | dingtalk://dingtalkclient/page/link?url=URL&popup\_wnd=true&title=TITLE&width=WIDTH&height=HEIGHT | - **url**：跳转链接，需要进行urlencode。 - **popup\_wnd**：固定值**true**。 - **title**：弹窗的标题，需要进行urlencode。 - **width**：宽。 - **height**：高。 | dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.dingtalk.com%2F&popup\_wnd=true&title=%E6%B5%8B%E8%AF%95&width=700&height=800 |
| 移动端半浮层 | dingtalk://dingtalkclient/action/im\_open\_hybrid\_panel?panelHeight=percent60&hybridType=online&pageUrl=URL | - **panelHeight**：浮层高度，取值为（percent0~ percent100）。 - **hybridType**：类型，固定值**online**。 - **pageUrl**：跳转链接，需要进行urlencode。 | dingtalk://dingtalkclient/action/im\_open\_hybrid\_panel?panelHeight=percent60&hybridType=online&pageUrl=https%3A%2F%2Fwww.dingtalk.com%2F |
| 移动端全屏 | dingtalk://dingtalkclient/page/link?url=URL | - **url**：跳转链接，需要进行urlencode。 | dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.dingtalk.com%2F |

开发者需要基于自己应用的实际场景和在群内用户使用时的具体需求来拼装一个群应用链接。

需要开发者通过链接参数来组装。例如从移动端页面的打开方式(推入页面、弹出页面等)，到PC端的页面跳转逻辑(打开新容器或者左滑页面)，都是通过链接参数的配置来实现的。

## 跳转到H5页面

### link(侧边栏/容器划出)

示例：

```
dingtalk://dingtalkclient/page/link?dd_mode=push&pc_slide=true&url=http%3a%2f%2fomsdevdingtalkf.zjk.taeapp.com%2findex.html%3fcorpid%3d$CORPID$%26dd_nav_bgcolor%3dffff943e%2f%23%2fgroup-plugin%3fcorpid%3d$CORPID$%26openConversationId%3d$DOUBLE_ENCCID$%26dd_nav_bgcolor%3dffff943e%26pluginType%3d3%26appid%3d6397
```

参数说明：

| 参数 | 说明 |
| --- | --- |
| url | 页面URL，必须做urlencode。 |
| dd\_mode | iOS端使用。   - push：iOS从左向右推入一个容器 - present：iOS从下向上弹出一个容器 |
| pc\_slide | pc\_slide=true 时，PC 端会在应用内打开这个 URL。 |

## 跳转到应用

### openapp(如工作台、浏览器、左划面板)

示例：

```
dingtalk://dingtalkclient/action/openapp?corpid=$CORPID$&container_type=work_platform&app_id=3204&redirect_type=emit_params&params=&redirect_url=https%3A%2F%2Ftestt2.wmnetwork.cc%2Fmanage%2Findex%3Fmid%3Dwfp40mx9
```

参数说明：

| 参数 | 说明 |
| --- | --- |
| container\_type | 展现的容器：   - **browser**: 浏览器 - **slide\_panel**：左划面板 - **work\_platform**：工作台 |
| corpid | 企业的corpid。 |
| app\_id | - 第三方企业应用：应填写appId，appId查看，参考[基础概念-AppId](0001-basic-concepts-beta.md#f20a795ad844u)。 - 企业内部应用：应填写0\_agentId，由数字0、下划线和agentId拼接组成。agentId可在应用详情中查看，参考[基础概念-AgentId](0001-basic-concepts-beta.md#884d363067bnq)。 |
| redirect\_type | 跳转类型：   - **jump**：直接打开redirect\_url - **emit\_params**: 发射事件的方式 |
| params | 参数，首次打开要将此参数加到跳转url的参数列表内。 |
| redirect\_url | 跳转url，需要urlencode。 |
| slide\_panel\_option | 左划面板的参数 PC版独有。   - **width**：侧边栏宽度 - **showAppPage**：展示页面   例如：{"width": 500,"showAppPage":true}  **[!NOTE]**  {"width":500,"showAppPage":true}需要urlencode。 |

## 跳转到小程序

小程序 scheme支持跳转到第三方企业应用小程序、第三方个人应用小程序，请参考[小程序 scheme](../03-Ogu5SlPY4t-客户端-JSAPI/0463-scheme-of-mini-programs-1.md)。

| 跳转到应用类型 | 小程序schema是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |
| 第三方个人应用 | 支持 |

## 如何通过链接获取来源群信息

### **指定特殊打开方式**

开发者需要基于自己应用的实际场景和在群内用户使用时的具体需求来拼装一个应用链接出来。需要开发者通过链接参数来组装。例如从移动端页面的打开方式(推入页面、弹出页面等)，到PC端的页面跳转逻辑(打开新容器或者左滑页面)，都是通过链接参数的配置来实现的。

以下以项目群为例，详细说明一个链接是如何拼装出来的。

dingtalk://dingtalkclient/page/link?url=https%3a%2f%2fding-doc.dingtalk.com%2fdoc%23%2fpqkq0u%2feluagw%2f$CORPID$%2f$DOUBLE\_ENCCID$

- **开发者的目标页面地址：**

  ```
  https%3a%2f%2fding-doc.dingtalk.com%2fdoc%23%2fpqkq0u%2feluagw
  ```

  - 当你使用了钉钉统一跳转协议，这一部分将作为“钉钉统一跳转协议”地址的入参，所以需要经过urlEncode。
  - 当你没有使用钉钉统一跳转协议，可直接使用原始Url作为地址。不需要urlEncode。
- **钉钉统一跳转协议（可选）**

  ```
  dingtalk://dingtalkclient/page/link?url=
  ```

  - 这个部分决定了会以什么方式打开你指定的页面。目前支持的有“浏览器打开”、“侧边栏打开”等，每种方式对应的统一跳转协议的path不一样。
  - 部分统一跳转协议path，只在部分平台客户端可用，比如侧边栏打开只在pc和mac端可用。
- **地址动参（可选）**

  ```
  $CORPID$ $DOUBLE_ENCCID$
  ```

  - 设置了这个动参，当用户点击这个访问开发者的地址时，url里的这部分动参可以替换为群上下文的信息，比如corpid和 openConversationId。

    目前可支持的动参如下：

    | 参数 | 说明 |
    | --- | --- |
    | $CORPID$ | 动态替换企业ID（corpId） |
    | $ENCCID$ | 动态替换成开放群ID（openConversationId）。  仅当不使用钉钉统一跳转协议时使用该动参。 |
    | $DOUBLE\_ENCCID$ | 动态替换成开放群ID（openConversationId），区别在于二次urlencode，用于多次协议透传跳转urldecode。  仅当使用钉钉统一跳转协议时使用该动参。 |

    $DOUBLE\_ENCCID$二次url加解密是因为：钉钉以“dingtalk://”有一层内部协议，在解析这层协议需要加密一次；url参数后面的业务https协议透传给下游容器使用的时候也需要加解密一次；由于消费方2次解析需要，所以产生url时候也需要2次加密。

    示例产生url： urlencode（钉钉url？xxx=xxx & url = urlencode（业务url））

    示例解析url： a、urldecode（钉钉url）-> 得到业务url；b、urldecode（业务url）-> 可用参数
