---
title: "开发规范"
source_url: "https://open.dingtalk.com/document/dingstart/development-specification"
namespace: "dingstart"
slug: "development-specification"
group: "工作台"
tab: "使用教程"
breadcrumb: "合作伙伴教程 > 第三方全码组件 > 组件规范 > 开发规范"
doc_id: "L0HlGrrIJc"
updated_at: "2025-10-21 14:11:19"
---

> Source: https://open.dingtalk.com/document/dingstart/development-specification
> Path: 工作台 / 使用教程 / 合作伙伴教程 > 第三方全码组件 > 组件规范 > 开发规范
> Updated: 2025-10-21 14:11:19

# 开发规范

## 支持组件特性

### 标题栏的标准化（必选）

钉钉将组件的标题区整体做了接管，开发者只需要提供内容，钉钉会统一在营销态和运行态支持标题、图标、管理的展示。

> **[!NOTE]**
>
> - 如后期设计规范升级，工作台会统一修改组件外框等样式，为减少组件未来的维护成本，请使用**config.json**中**quickSetting**的标准设置。
> - 如使用了旧的配置，请同步删除。

![标题栏的标准化](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300383.png)

使用标准标题栏及卡片样式，只需要增加**config.json**中的**quickSetting**配置即可，配置如下：

```
{
    "pluginComponentName": "project-select-view",
    "name": "对应下图中的title",
    "icon": "对应下图中的icon",
    "previewUrl": "https://img.alicdn.com/tfs/TB1KcAWdrj1gK0jSZFOXXc7GpXa-750-100.jpg",
    "previewHeight": 200,        
  // 工作台组件的快速设置选项   
    "quickSetting": {
        "useStandardHead": true,     // 使用工作台组件标准标题栏，请所有组件升级到此设置
        "useStandardContainer": true,   // 使用工作台组件标准样式，请所有组件升级到此设置
        "containerType": "standard",    // 组件是标准高度的组件值设置为standard，2倍高度的组件值为doubleHeight
    },
    "props": {

    }
}
```

设置**quickSetting**后，只需开发组件内容区，如下图所示：

![quickSetting](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300389.png)

- **icon**：组件的config.json里的icon（图示中①）。
- **name**：组件的config.json里的name（图示中②）。
- **link**：点击标题跳转链接，组件上架时提交给验收人员（图示中③）。
- **manage**：右侧管理，自动注入，开发者无需提供（图示中④）。

### darkmode支持（必选）

**方案**：

- `mode=dark`时请使用dark样式适配，其他值请暂时不要做其他处理。
- 开发者后台调试设计器里的预览二维码，支持darkmock模式，可使用此功能进行dark模式的验证。

  可取值组件的**this.props.mode**为`dark`时代表**darkmode**状态，如下图所示：

  ![darkmode支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300402.png)

  样式代码示例：

  ```
  .title-area {
    position:relative;
    font-size: 32rpx;
    color: rgba(23, 26, 29, 1);
  }

  .dark .title-area {
    color: rgba(255,255,255,0.96);
  }
  ```

### 组件三种状态支持（必选）

在使用`sdk.request`时，需要`try catch`包裹，接口错误的情况下，需要展示组件的异常态。

> **[!NOTE]**
>
> 目前code为10002表示网关黑名单异常，其它code是接口本身异常。

代码示例：![组件三种状态支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300403.png)

- 当组件关联的应用未被安装，但组件被投放到工作台时，组件状态为营销态。
- 当组件所属的解决方案未被安装，但组件被投放到工作台时，组件状态为营销态。

```
// 营销态判断条件
this.props.componentProps.promotionState === 'STANDARD_WORKTAB'
```

**注意**：

- 营销态请按照营销态的设计稿来开发。
- 营销态时，组件不能请求`sdk.request`（强行请求会发生非预期情况）。
- 营销态时，组件被点击不能跳转自己的应用内地址（此时应用未开通，如果跳转会报错），需要跳转到tryoutAddress（工作台自动注入给组件），代码示例如下：

  ```
  // 营销态时打开试用地址的示例代码
  if (this.props.componentProps.promotionState === 'STANDARD_WORKTAB') {
   getSdk().openApp({
     url: this.props.componentProps.tryoutAddress,
    });
  }
  ```

  非营销态和接口正常的情况下，按照设计规范展示正常态。

### 国际化支持（可选）

**方案**：

- 组件内处理国际化逻辑。
- 加载组件时，会传入变量locale，例如zh\_CN,en\_US等。
- 组件需要在didUpdate里处理locale变更逻辑。

如下图中，组件需内部实现compI18n，处理国际化：

![国际化支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300406.png)

## 支持PC工作台

标准工作台组件目前支持移动端和PC端工作台的功能、数据和体验统一对齐，平台具备将移动端组件在PC端使用的能力。存量组件请对组件编码规范做一次排查优化，以便平台能统一识别组件代码，实现组件在移动端和PC端的复用。

PC端示意图：

![PC端示意图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300407.png)

### 代码规范

- **AXML**

  - 语法要符合小程序标准，例如属性定义不能使用中文冒号（：）。
- **JS**

  - JSAPI需使用： `import 'dingtalk-jsapi/entry/union'`。
  - 语法要符合小程序标准，例如主入口文件不能使用export。
  - 不能对原型链props修改。
  - 不能动态创建函数new function。
  - 不能使用eval。
  - 如果支持PC，请参照本文中JSAPI改造部分的说明，选择同时支持移动和PC的API使用。
  - PC或移动环境，取值组件的`props.config.platform = 'pc' / 'android' / 'ios'`。
  - 线上使用JSAPI前找@悦铭开通一下JSAPI权限。
- **acss**

  - 字号、尺寸等单位需要使用相对单位rpx。
- **config.json&pc.config.json**

  - 支持PC需单独提供一个配置文件，命名：pc.config.json

    如设计规范升级，工作台会统一修改组件外框等样式，减少组件未来的维护成本。配置说明如下：

    ```
    {
        "pluginComponentName": "project-select-view",
        "name": "对应下图中的title",
        "icon": "对应下图中的icon",
        "previewUrl": "https://img.alicdn.com/tfs/TB1KcAWdrj1gK0jSZFOXXc7GpXa-750-100.jpg",
        "previewHeight": 200,        
      // 工作台组件的快速设置选项   
        "quickSetting": {
            "useStandardHead": true,     // 使用工作台组件标准标题栏，请所有组件升级到此设置
            "useStandardContainer": true,   // 使用工作台组件标准样式，请所有组件升级到此设置
            "containerType": "standard",    // 组件是标准高度的组件值设置为standard，2倍高度的组件值为doubleHeight
        },
        "props": {

        }
    }
    ```

    ![quickSetting ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300389.png)

    标题栏配置说明：

    - **icon**：组件的config.json里的icon（图示中①）。
    - **name**：组件的config.json里的name（图示中②）。
    - **link**：点击标题跳转链接，组件上架时提交给验收人员（图示中③）。
    - **manage**：右侧管理，自动注入，开发者无需提供（图示中④）。
- **静态资源**

  - 不支持打包静态资源，可以对图片做CDN处理，使用图片链接。
- **openApp兼容PC端使用参数说明**

  组件内链接在PC端和移动端的打开方式具有差异，可做兼容处理：

  ```
  export enum OpenType {
   // 使用侧边栏直接打开链接
   OPEN_SLIDE_PANEL = 'open_slide_panel',
    // 将链接转为二维码后在侧边栏显示
   OPEN_SLIDE_PANEL_QRCODE = 'open_slide_panel_qrcode',
    // 将链接转为短链二维码后在侧边栏显示
    // 注：小程序链接使用短链二维码可能会出现打不开的问题，
    // 建议使用'open_slide_panel_qrcode'方式
    OPEN_SLIDE_PANEL_SHORT_URL_QRCODE = 'open_slide_panel_short_url_qrcode', 
   // 将链接使用工作台新建选项卡打开
    OPEN_PC_APP = 'open_dd_tab',
   // 将链接使用端外浏览器打开
    OPEN_EXTERNAL_BROWSER = 'open_external_browser', 
  }
  interface opt extends IAppDetailModel {
   url: string;
    name?: string; // 如果侧边栏打开则需要提供一个title
    openType?: string;
    // pc端必传，pc端若不传默认为'open_slide_panel_qrcode'方式打开链接
  }
  openApp({
   url,
    name,
    openType,
  })
  ```
- **JSAPI改造**

  如组件中都是使用的工作台的，则不需要做处理。如单独使用的JSAPI，请关注下面内容。

  同时支持移动端和PC端的JSAPI如下，共26个，分别如下：

  ```
  [
    'alert',
    'confirm',
    'showToast',
    'showActionSheet',
    'setStorageSync',
    'getStorageSync',
    'removeStorageSync',
    'setClipboard',
    'createDing',
    'chooseUserFromList',
    'complexChoose',
    'chooseDepartments',
    'chooseExternalUsers',
    'createGroupChat',
    'checkBizCall',
    'chooseChatForNormalMsg',
    'chooseChat',
    'previewFileInDingTalk',
    'uploadAttachmentToDingTalk',
    'chooseDingTalkDir',
    'getAuthCode',
    'inquiryPrice',
    'createOrder',
    'getPayInfo',
    'cancelOrder',
    'openLink'
  ]
  ```

  如果之前组件中通过dd.XXX的方式使用了列表中的JSAPI，需要转换成三段式，通过npm包dingtalk-jsapi来引入对应的JSAPI，例如alert的引入方式如下：

  ```
  import alert from 'dingtalk-jsapi/api/device/notification/alert';
  ```

  PC端和移动端可用的JSAPI与dingtalk-jsapi的引用路径的映射关系如下：

  ```
  alert --> import alert from 'dingtalk-jsapi/api/device/notification/alert'
  confirm --> import confirm from 'dingtalk-jsapi/api/device/notification/confirm'
  showToast --> import showToast from 'dingtalk-jsapi/api/device/notification/toast'
  showActionSheet --> import showActionSheet from 'dingtalk-jsapi/api/device/notification/actionSheet'
  setStorageSync --> import setStorageSync from 'dingtalk-jsapi/api/util/domainStorage/setItem'
  getStorageSync --> import getStorageSync from 'dingtalk-jsapi/api/util/domainStorage/getItem'
  removeStorageSync --> import removeStorageSync from 'dingtalk-jsapi/api/util/domainStorage/removeItem'
  getNetworkType --> import getNetworkType from 'dingtalk-jsapi/api/device/connection/getNetworkType'
  createDing --> import createDing from 'dingtalk-jsapi/api/biz/ding/create'
  chooseUserFromList --> import chooseUserFromList from 'dingtalk-jsapi/api/biz/customContact/choose'
  complexChoose --> import complexChoose from 'dingtalk-jsapi/api/biz/contact/complexPicker'
  chooseDepartments --> import chooseDepartments from 'dingtalk-jsapi/api/biz/contact/departmentsPicker'
  chooseExternalUsers --> import chooseExternalUsers from 'dingtalk-jsapi/api/biz/contact/externalComplexPicker'
  createGroupChat --> import createGroupChat from 'dingtalk-jsapi/api/biz/contact/createGroup'
  checkBizCall --> import checkBizCall from 'dingtalk-jsapi/api/biz/telephone/checkBizCall'
  chooseChatForNormalMsg --> import chooseChatForNormalMsg from 'dingtalk-jsapi/api/biz/chat/pickConversation'
  chooseChat --> import chooseChat from 'dingtalk-jsapi/api/biz/chat/chooseConversationByCorpId'
  previewFileInDingTalk --> import previewFileInDingTalk from 'dingtalk-jsapi/api/biz/cspace/preview'
  uploadAttachmentToDingTalk --> import uploadAttachmentToDingTalk from 'dingtalk-jsapi/api/biz/util/uploadAttachment'
  chooseDingTalkDir --> import chooseDingTalkDir from 'dingtalk-jsapi/api/biz/cspace/chooseSpaceDir'
  getAuthCode --> import getAuthCode from 'dingtalk-jsapi/api/runtime/permission/requestAuthCode'
  inquiryPrice --> import inquiryPrice from 'dingtalk-jsapi/api/biz/store/inquiry'
  createOrder --> import createOrder from 'dingtalk-jsapi/api/biz/store/createOrder'
  getPayInfo --> import getPayInfo from 'dingtalk-jsapi/api/biz/store/getPayUrl'
  cancelOrder --> import cancelOrder from 'dingtalk-jsapi/api/biz/store/closeUnpayOrder'
  openLink --> import openLink from 'dingtalk-jsapi/api/biz/util/openLink'
  ```

  JSAPI使用文档：[H5微应用JSAPI总览](https://open.dingtalk.com/document/orgapp/jsapi-overview)。

  > **[!NOTE]**
  >
  > 如果之前自建组件使用了上述列表之外的JSAPI，PC端将无法正常调用，目前尚未有其它的替代方案。具体诉求可通过[联系我们](https://open.dingtalk.com/document/dingstart/dashboard-model-overview2)加入**标准工作台组件/解决方案接入群**，在群内咨询服务小蜜。
