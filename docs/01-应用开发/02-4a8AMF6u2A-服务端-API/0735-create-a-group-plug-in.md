---
title: "创建快捷入口（群插件）"
source_url: "https://open.dingtalk.com/document/development/create-a-group-plug-in"
namespace: "development"
slug: "create-a-group-plug-in"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 使用教程 > 创建快捷入口（群插件）"
doc_id: "CV0YFFqTan"
updated_at: "2025-09-25 21:14:05"
---

> Source: https://open.dingtalk.com/document/development/create-a-group-plug-in
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 使用教程 > 创建快捷入口（群插件）
> Updated: 2025-09-25 21:14:05

# 创建快捷入口（群插件）

本文介绍如何创建快捷入口。

## 什么是快捷入口（群插件）

快捷入口（群插件）为场景群及对应的群模板的核心组成部分，是串联业务的关键节点。

一个场景群通常会配置多个插件，指向一个业务场景中的不同流程和节点，这样就可以在一个群中快速地找到和使用该业务场景相关的全部服务。例如如一个项目群，就会将【今日任务】、【项目进度管理】、【需求列表】等业务节点作为插件配置到群内，方便进行项目管理。

用户在群内点击插件入口时，将会带上群的相关参数，开发者将据此确定是谁在哪个群内在什么时间点击了哪个具体插件。以此，产品方案商能够实现高度智能化和指向明确的业务服务。

> **[!IMPORTANT]**
>
> 场景群的群插件链接所支持的页面链接，仅限群所属企业自研的**钉钉企业内部应用**页面链接或安装的**第三方企业应用**页面链接，此外不支持其他链接作为群插件。

## 创建群插件

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/index)。
2. 在**开发者后台**页面，选择**场景群**，点击创建**群插件**。![创建群插件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3513939361/p367979.png)
3. 新建**群插件**并点击**新建**，等待审核通过。

   > **[!NOTE]**
   >
   > - 审核时效，工作日12小时内审批完成。

   设置不同的群插件链接不同，支持在钉钉工作台、侧边栏、外部浏览器等打开链接：

   | 打开方式 | 设置链接 |
   | --- | --- |
   | 在钉钉工作台打开群插件 | dingtalk://dingtalkclient/action/openapp?corpid=dingxxxxxxxxxxx&**container\_type=work\_platform**&app\_id=0\_140444xxxxx&redirect\_type=jump&redirect\_url=https%3A%2F%2Fding-doc.dingtalk.com%2F |
   | 侧边栏打开群插件 | dingtalk://dingtalkclient/action/openapp?corpid=dingxxxxxxxxxxx&**container\_type=slide\_panel**&app\_id=0\_140444xxxxx&redirect\_type=jump&redirect\_url=https%3A%2F%2Fding-doc.dingtalk.com%2F |
   | 外部浏览器打开群插件 | dingtalk://dingtalkclient/action/openapp?corpid=dingxxxxxxxxxxx&con**tainer\_type=browser**&app\_id=0\_140444xxxxx&redirect\_type=jump&redirect\_url=https%3A%2F%2Fding-doc.dingtalk.com%2F |

   ![群插件url设置 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9564899361/p371644.png)

## **构造快捷入口链接**

快捷入口（群插件）为一个具有业务能力的钉钉链接，开发者需要基于自己微应用的实际场景和在群内用户使用时的具体需求来拼装一个快捷入口链接。

快捷入口名字最多支持4个字符，快捷入口链接所具有的能力非常多，但需要开发者通过链接参数来组装。例如从移动端页面的打开方式(推入页面、弹出页面等)，到PC端的页面跳转逻辑(打开新容器或者左滑页面)，都是通过链接参数的配置来实现的。

- **跳转到H5页面**

  link(侧边栏/容器划出)

  示例：

  ```
  dingtalk://dingtalkclient/page/link?dd_mode=push&pc_slide=true&url=http%3a%2f%2fomsdevdingtalkf.zjk.taeapp.com%2findex.html%3fcorpid%3d$CORPID$%26dd_nav_bgcolor%3dffff943e%2f%23%2fgroup-plugin%3fcorpid%3d$CORPID$%26openConversationId%3d$DOUBLE_ENCCID$%26dd_nav_bgcolor%3dffff943e%26pluginType%3d3%26appid%3d6397
  ```

  参数说明：

  | 参数 | 说明 |
  | --- | --- |
  | url | 页面URL，必须做urlencode。 |
  | dd\_mode | iOS端使用。  - push：iOS从左向右推入一个容器 - present：iOS从下向上弹出一个容器 |
  | pc\_slide | pc\_slide=true 时，PC 端会在应用内打开这个 URL。 |
- **跳转到微应用**

  openapp(如工作台、浏览器、左划面板)

  示例：

  ```
  dingtalk://dingtalkclient/action/openapp?corpid=$CORPID$&container_type=work_platform&app_id=3204&redirect_type=emit_params&params=&redirect_url=https%3A%2F%2Ftestt2.wmnetwork.cc%2Fmanage%2Findex%3Fmid%3Dwfp40mx9
  ```

  参数说明：

  | 参数 | 说明 |
  | --- | --- |
  | container\_type | 展现的容器：  - browser: 浏览器 - slide\_panel：左划面板 - work\_platform：工作台 |
  | corpid | 企业的corpid。 |
  | app\_id | - 第三方企业应用 应填写appId，appId查看。  - 企业自建应用 应填写0\_agentId，由数字0、下划线和agentId拼接组成。agentId可在应用详情中查看。 |
  | redirect\_type | 跳转类型：  - jump：直接打开redirect\_url - emit\_params: 发射事件的方式 |
  | params | 参数，首次打开要将此参数加到跳转url的参数列表内。 |
  | redirect\_url | 跳转url，需要urlEncode。 |
  | slide\_panel\_option | 左划面板的参数 PC版独有。  例如: { "width": 500, / 侧边栏宽度 /"showAppPage": true, / 是否显示网页 /} |
- **跳转到小程序**

  1. **通用参数 (open\_micro\_app 和 open\_mini\_app 都支持)**

     | 参数 | 是否必填 | 说明 |
     | --- | --- | --- |
     | appId | 和 agent\_id 二选一，如果同时存在，优先用 app\_id | 微应用id，注意不是小程序ID，isv应用使用此id。 |
     | page | 否 | 小程序的page地址，可以加get参数。默认为小程序首页。 |
     | query | 否 | 小程序的启动参数，可以在 App 的 onLaunch / onShow 回调里获取。  启动小程序时，客户端默认加上corpId参数，所以业务方不可以填corpId，会被覆盖掉。 |
     | containerType | 否 | PC 端专用参数，有以下几个选项：  - browser: 浏览器 - slide\_panel（默认值）：左划面板 - work\_platform：工作台 - mobile: 引导到移动端 |
     | title | 否 | PC端专用参数，用来显示title。 |
     | source | 否 | 来源（只用于需要从服务端拉取包时用）：  - debug：真机调试版 - trial：体验版 |
     | version | 否 | 版本号。 |
     | ddMode | 否 | 小程序启动转场方式。  - push： 推入方式 - present：弹出方式 - float：浮层方式 - pop：弹框方式(pop view) 如果不传，客户端按照默认转场方式启动。客户端v4.5.8版本开始灰度。float和pop，v4.6.35(20190624)版本开始灰度 |
     | mainTask | 否 | 仅**安卓客户端**需要。  取值为“true”或者“false”，默认false。  如果传值为“true”,表示和钉钉主Task一个Task，不再保活  客户端4.6.3版本支持 |
     | ddJointNavi | 否 | 配置导航栏样式。如果配置这个会覆盖ddMode的逻辑。  android & iOS：“0”或者“1”、“1001”。  - 0：老的导航栏 - 1：新的导航栏 - 1001：只有返回键和标题的导航栏 |
     | keepAlive | 否 | 可配置**true**或者**false**，默认**true**。  如果配置了mainTask 为true，不再处理这个key。 |
     | ddFocus | 否 | 可配置**true**或者**false**，默认**true**。  如果配置为**true**，容器会在初始化时先禁止内部元素获取焦点的行为。 |
     | ddEnableWX | 否 | 是否支持weex渲染。  支持weex渲染的情况下，如果页面有配置weex渲染模式，则可以启动weex加载页面 |
     | ddForceAsync | 否 | 是否强制异步启动。  强制异步启动时，如果本地有离线包，则不会触发同步更新，强制异步更新启动（解决断网环境启动问题）。 |
     | animated | 否 | 取值**0**和**1**，异步启动是否有转场动画(同步启动场景忽略此参数)，默认**1**。  v4.6.36版本上线。 |

     **ddMode=float 浮窗时，可支持的参数**

     | 参数 | 是否必填 | 说明 |
     | --- | --- | --- |
     | panelHeight | 否 | 浮窗高度，可以是屏幕占比百分比，也可以是确定的高度。  - percent50，含义是占比屏幕的50%，数字在(0-100]之间，大于小于边界按边界处理。 - 1000，含义是确切的高度单位为pt(非px)。 - 如果不设置或者设置为0，则显示效果为全屏浮窗。 |
     | containerType | 否 | 此场景下额外增加两个值：  - miniApp（默认）：小程序 - online：在线H5 |
     | miniAppId | 配合containerType决定 | 小程序appId。 |
     | page | 配合containerType决定 | URL encode后的页面地址。  如果是小程序，则是小程序的page。  如果是在线H5，则是url地址。 |
     | coverVisible | 否，默认显示，配置false，不显示 | - true（默认）：显示遮罩层 - false：不显示遮罩层默认显示 |

     **ddMode=pop 弹层时，可支持的参数**

     | 参数 | 是否必填 | 说明 |
     | --- | --- | --- |
     | width | 是 | 弹层宽度。 |
     | height | 是 | 弹层高度。 |
     | clear | 否 | 背景是否透明，默认不透明。 |
     | containerType | 否 | 此场景下额外增加两个值：  - miniApp（默认）：小程序 - online：在线H5 |
     | miniAppId | 配合containerType决定 | 小程序appId。 |
     | page | 配合containerType决定 | URL encode后的页面地址。  如果是小程序，则是小程序的page。  如果是在线H5，则是url地址。 |
  2. **打开微应用 scheme（企业小程序专用 scheme）**

     scheme：`dingtalk://dingtalkclient/action/open_micro_app`

     `基本参数同通用参数列表。`

     灰度控制逻辑应该放在这个 scheme 的 handler 里

     ​

     | 参数 | 是否必填 | 说明 |
     | --- | --- | --- |
     | corpId | 是 | 企业的corpid。  **[!IMPORTANT]**  优先级高，会覆盖掉query里的corpId。 |
     | appId | 和 agent\_id 二选一  如果同时存在，优先用appid | 微应用id，注意不是小程序ID，isv应用用此id。 |
     | agentId | 和 app\_id 二选一 | 企业自建应用的agent\_id。 |
     | fallbackUrl | 否  不支持 H5 的微应用，不用填此参数，在 H5 和小程序灰度阶段的，必填此参数 | H5 的地址，不支持小程序的微应用，直接使用这个地址。 |
     | ddFocus | 否 | 如果配置为true，容器会在初始化时先禁止内部元素获取焦点的行为，默认为false。 |
     | ddForceAsync | 否 | 是否强制异步启动。强制异步启动时，如果本地有离线包，则不会触发同步更新，强制异步更新启动（解决断网环境启动问题）。 |

     PC端测试case：

     - 在slide panel打开url，无title

       ```
       dingtalk://dingtalkclient/action/open_micro_app?corpId=11233&app_id=123&fallback_url=https%3A%2F%2Fwww.dingtalk.com&container_type=slide_panel
       ```
     - 在slide panel打开url，无title

       ```
       dingtalk://dingtalkclient/action/open_micro_app?corpId=11233&app_id=123&fallback_url=https%3A%2F%2Fwww.dingtalk.com
       ```
     - 在browser打开url

       ```
       dingtalk://dingtalkclient/action/open_micro_app?corpId=11233&app_id=123&fallback_url=https%3A%2F%2Fwww.dingtalk.com&container_type=browser
       ```
     - 在slide panel打开url，有title

       ```
       https://www.dingtalk.com?micro_app_scheme=dingtalk%3A%2F%2Fdingtalkclient%2Faction%2Fopen_micro_app%3F%0AcorpId%3D11233%26app_id%3D123%26container_type%3Dslide_panel%26title%3Dtest_title
       ```
     - 在browser打开url

       ```
       https://www.dingtalk.com?micro_app_scheme=dingtalk%3A%2F%2Fdingtalkclient%2Faction%2Fopen_micro_app%3F%0AcorpId%3D11233%26app_id%3D123%26container_type%3Dbrowser%26title%3Dtest_title
       ```
  3. 开启小程序schema (个人小程序专用 scheme)

     scheme：`dingtalk://dingtalkclient/action/open_mini_app`

     基本参数同通用参数列表。

     | 参数 | 是否必填 | 说明 |
     | --- | --- | --- |
     | miniAppId | 是 | 小程序id。 |
  4. **小程序调试scheme**

     scheme：`dingtalk://dingtalkclient/action/dev_mini_app`

     主要用于调试小程序，以及appx框架开发。通过此方式打开的小程序，直接通过url启动主文档。不会进入包管理流程，也不会触发保活逻辑。miniAppId仅用于做接口校验等。

     > **[!IMPORTANT]**
     >
     > 参数都已经过encode，注意解码。

     | 参数 | 说明 |
     | --- | --- |
     | url | encode之后的 小程序主文档url，客户端会调用nebulaSDK打开此链接。 |
     | miniAppId | 小程序appId |
     | isTinyApp | 是否小程序，通过http方式打开必须传YES |
     | enableDSL | 使用小程序，取值YES或NO |
     | enableWK | 使用WK，取值YES或NO |
     | packageManager | 包管理服务  - 默认钉钉接口 - alipay\_online: 支付宝生产环境 - alipay\_dev：支付宝开发环境 |
     | keepAlive | 是否保活，默认为true。 |

## 如何通过链接获取来源群信息

- 指定特殊打开方式

  快捷入口（群插件）为一个带有业务能力的dingtalk链接，开发者需要基于自己微应用的实际场景和在群内用户使用时的具体需求来拼装一个群插件链接出来。插件名字最多支持4个字，插件链接里面所具有的能力非常多，但需要开发者通过链接参数来组装。例如从移动端页面的打开方式(推入页面、弹出页面等)，到PC端的页面跳转逻辑(打开新容器或者左滑页面)，都是通过链接参数的配置来实现的。

  以下以项目群的快捷入口为例，详细说明一个快捷入口链接是如何拼装出来的。

  <dingtalk://dingtalkclient/page/link?url=https%3a%2f%2fding-doc.dingtalk.com%2fdoc%23%2fpqkq0u%2feluagw%2f$CORPID$%2f$DOUBLE_ENCCID$>

  - **开发者的目标页面地址：**https%3a%2f%2fding-doc.dingtalk.com%2fdoc%23%2fpqkq0u%2feluagw

    - 当你使用了钉钉统一跳转协议，这一部分将作为“钉钉统一跳转协议”地址的入参，所以需要经过urlEncode。
    - 当你没有使用钉钉统一跳转协议，可直接使用原始Url作为快捷入口的地址。不需要urlEncode。
  - **钉钉统一跳转协议（可选）**dingtalk://dingtalkclient/page/link?url=

    - 这个部分决定了会以什么方式打开你指定的页面。目前支持的有“浏览器打开”、“侧边栏打开”等，每种方式对应的统一跳转协议的path不一样。
    - 部分统一跳转协议path，只在部分平台客户端可用，比如侧边栏打开只在pc和mac端可用。
  - 快捷入口**地址动参（可选）** $CORPID$ $DOUBLE\_ENCCID$

    - 设置了这个动参，当用户点击这个快捷入口访问开发者的地址时，url里的这部分动参可以替换为群上下文的信息，比如corpid和 openConversationId。

      目前可支持的动参如下：

      | 参数 | 说明 |
      | --- | --- |
      | $CORPID$ | 动态替换企业ID（corpId） |
      | $ENCCID$ | 动态替换成开放群ID（openConversationId）。  仅当不使用钉钉统一跳转协议时使用该动参。 |
      | $DOUBLE\_ENCCID$ | 动态替换成开放群ID（openConversationId），区别在于二次urlencode，用于多次协议透传跳转urldecode。  仅当使用钉钉统一跳转协议时使用该动参。 |

      $DOUBLE\_ENCCID$二次url加解密是因为：钉钉以“dingtalk://”有一层内部协议，在解析这层协议需要加密一次；url参数后面的业务https协议透传给下游容器使用的时候也需要加解密一次；由于消费方2次解析需要，所以产生url时候也需要2次加密。

      示例产生url： urlencode（钉钉url？xxx=xxx & url = urlencode（业务url））

      示例解析url： a、urldecode（钉钉url）-> 得到业务url；b、urldecode（业务url）-> 可用参数
