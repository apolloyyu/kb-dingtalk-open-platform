---
title: "场景示例"
source_url: "https://open.dingtalk.com/document/dingstart/standardization-of-title-blocks-1"
namespace: "dingstart"
slug: "standardization-of-title-blocks-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 场景示例"
doc_id: "LuDZwLxoS7"
updated_at: "2026-08-19 09:12:28"
---

> Source: https://open.dingtalk.com/document/dingstart/standardization-of-title-blocks-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 场景示例
> Updated: 2026-08-19 09:12:28

# 场景示例

## **标题栏的标准化**

钉钉将组件的标题区整体做了接管，开发者只需要提供内容，钉钉会统一在营销态和运行态支持标题、图标、管理的展示。

> **[!NOTE]**
>
> - 如后期设计规范升级，工作台会统一修改组件外框等样式，为减少组件未来的维护成本，请使用 **config.json** 中 **quickSetting** 的标准设置。
> - 如使用了旧的配置，请同步删除。

![标题栏的标准化](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300383.png)

使用标准标题栏及卡片样式，只需要增加 **config.json** 中的 **quickSetting** 配置即可，配置如下：

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

设置 **quickSetting** 后，只需开发组件内容区，如下图所示：

![quickSetting](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300389.png)

- **icon**：组件的 config.json 里的 icon（图示中①）。
- **name**：组件的 config.json 里的 name（图示中②）。
- **link**：点击标题跳转链接，组件上架时提交给验收人员（图示中③）。
- **manage**：右侧管理，自动注入，开发者无需提供（图示中④）。

## **深色模式**

> **[!NOTE]**
>
> 组件必须要支持深色模式，否则在钉钉深色模式下页面不可用。

### **场景描述**

| 深色模式 | 浅色模式 |
| --- | --- |
| IMG_4153.PNG | IMG_4154.PNG |

### **实现方案**

组件被工作台页面集成后，会被自动注入 **this.props.mode** 属性。

| mode值 | 说明 |
| --- | --- |
| dark | 深色模式 |
| light | 浅色模式 |

### **示例代码**

#### **axml 示例代码**

给组件的 className 设置“{{mode}}”变量，当此时为深色模式时，该组件的 className为'dark'。

| 代码 | image.png |
| --- | --- |
| 实际渲染 | image.png |

#### **acss 示例代码**

```
// 浅色模式时，字体颜色为黑色
.title-area {
  color: #000000;
}

// 深色模式时，字体颜色为白色
.dark .title-area {
  color: #FFFFFF;
}
```

## **组件三种状态支持**

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
- 营销态时，组件被点击不能跳转自己的应用内地址（此时应用未开通，如果跳转会报错），需要跳转到 tryoutAddress（工作台自动注入给组件），代码示例如下：

  ```
  // 营销态时打开试用地址的示例代码
  if (this.props.componentProps.promotionState === 'STANDARD_WORKTAB') {
   getSdk().openApp({
     url: this.props.componentProps.tryoutAddress,
    });
  }
  ```

  非营销态和接口正常的情况下，按照设计规范展示正常态。

## **国际化支持**

**方案**

- 组件内处理国际化逻辑。
- 加载组件时，会传入变量 locale，例如 zh\_CN、en\_US 等。
- 组件需要在 didUpdate 里处理 locale 变更逻辑。

如下图中，组件需内部实现 compI18n，处理国际化：

![国际化支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300406.png)

## **支持 PC 工作台**

### **介绍**

标准工作台组件目前支持移动端和 PC 端工作台的功能、数据和体验统一对齐，平台具备将移动端组件在PC端使用的能力。存量组件请对组件编码规范做一次排查优化，以便平台能统一识别组件代码，实现组件在移动端和 PC 端的复用。

PC 端示意图：

![PC端示意图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300407.png)

### **代码规范**

- **AXML**

  - 语法要符合小程序标准，例如属性定义不能使用中文冒号（：）。
- **JS**

  - JSAPI需使用： `import 'dingtalk-jsapi/entry/union'`。
  - 语法要符合小程序标准，例如主入口文件不能使用 export。
  - 不能对原型链 props 修改。
  - 不能动态创建函数 new function。
  - 不能使用 eval。
  - 不能使用 dd 方式调用 jsapi。
  - 如果支持 PC，请参照本文中 JSAPI 改造部分的说明，选择同时支持移动和 PC 的 API 使用。
  - PC 或移动环境，取值组件的`props.config.platform = 'pc' / 'android' / 'ios'`。
  - 线上使用 JSAPI 前找@悦铭开通一下 JSAPI 权限。
- **acss**

  - 字号、尺寸等单位需要使用相对单位 rpx。
- **config.json&pc.config.json**

  - 支持 PC 需单独提供一个配置文件，命名：pc.config.json。

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

    - **icon**：组件的 config.json 里的 icon（图示中①）。
    - **name**：组件的 config.json 里的 name（图示中②）。
    - **link**：点击标题跳转链接，组件上架时提交给验收人员（图示中③）。
    - **manage**：右侧管理，自动注入，开发者无需提供（图示中④）。
- **静态资源**

  - 不支持打包静态资源，可以对图片做 CDN 处理，使用图片链接。
- **openApp 兼容 PC 端使用参数说明**

  组件内链接在 PC 端和移动端的打开方式具有差异，可做兼容处理：

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
- **JSAPI 改造**

  如组件中都是使用的工作台的，则不需要做处理。如单独使用的 JSAPI，请关注下面内容。

  同时支持移动端和 PC 端的 JSAPI 如下，共 26 个，分别如下：

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

  如果之前组件中通过 dd.XXX 的方式使用了列表中的 JSAPI，需要转换成三段式，通过 npm 包 dingtalk-jsapi 来引入对应的 JSAPI，例如 alert 的引入方式如下：

  ```
  import alert from 'dingtalk-jsapi/api/device/notification/alert';
  ```

  PC 端和移动端可用的 JSAPI 与 dingtalk-jsapi 的引用路径的映射关系如下：

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

  JSAPI 使用文档：[JSAPI 总览](../../01-应用开发/03-Ogu5SlPY4t-客户端JSAPI/0001-jsapi-overview.md)。

  > **[!NOTE]**
  >
  > 如果之前自建组件使用了上述列表之外的 JSAPI，PC端将无法正常调用，目前尚未有其它的替代方案。

## **组件间通信**

> **[!NOTE]**
>
> 在同一个页面内的组件可进行通信。用一个应用中的全局的事件机制来实现。

例如：组件 A 要将数据传递给组件 B。事件名用 / 命名，以防和其他服务商的组件冲突。namespace 建议用公司的英文名。

代码示例如下。

```
import { getSdk, getLifecycleSdk, } from '../../api/sdk';

/** 组件A要把数据传给组件B **/

// 组件A
Component({
  ...
    methods: {
  changeProject(e){
    // 切换项目后，向全局发送项目id变化事件，事件名需要按照固定格式 <namespace>/<eventType>
    getSdk().triggerCustomEvent('dingtalk/changeProject', e.detail.value);
  }
}
});

// 组件B
Component({
  didMount(){
    getLifecycleSdk().didMount(this.props.componentName);
    // 在组件初始化时注册事件的监听器，便于在事件触发时获取到数据
    this.changeProject = (projectId) => {
      // do everything you like
    };
    getSdk().listenCustomEvent('dingtalk/changeProject', this.changeProject);
  },
  // 由于didMount可能会触发多次，因此需要在didUnmount时进行注销操作
  didUnmount() {
    getLifecycleSdk().didUnmount(this.props.componentName);
    getSdk().removeCustomEvent('dingtalk/changeProject', this.changeProject);
  }
  ...
});
```

## **刷新组件数据**

组件里不允许进行轮询，因为工作台是个常驻小程序，未正确清理的轮询可能造成内存泄漏引起工作台崩溃。

### **示例**

如果需要刷新数据，可以监听页面 **onShow** 事件，该事件会在工作台首页非首次展现出来时触发。

```
import { getSdk, getLifecycleSdk, } from '../../api/sdk';

Component({
    didMount() {
        getLifecycleSdk().didMount(this.props.componentName);
        // 初次渲染时获取一次数据
        this.fetchData();

      	/*
          事件绑定的函数需要明确this指向。
          如果写成listenCustomEvent('onShow', this.fetchData) 的话，
          在fetchData方法中获取到this已经不在当前作用域，所以要bind一下
        **/
      	this.refreshData = this.fetchData.bind(this);
        getSdk().listenCustomEvent('onShow', this.refreshData);
    },
    didUnmount() {
        getLifecycleSdk().didUnmount(this.props.componentName);
        // 由于didMount可能会触发多次，因此需要在didUnmount时清理绑定的事件
      	// 其次如果模块销毁时没有清除事件监听，可能会造成内存泄漏
        getSdk().removeCustomEvent('onShow', this.refreshData);
    },
    method: {
        async fetchData() {
            const data = await getSdk().request(this.props.componentProps.gateWayApi, {});
            ...
        }
    },
});
```

### **onShow 事件触发机制**

> **[!IMPORTANT]**
>
> 由于 **onShow** 触发频率较高可能对服务端产生压力，请谨慎评估需要用到本 SDK 的场景。

- 首次进入工作台时不会触发。
- 再次切换到工作台时触发。

  例如：钉钉底下 tab 切换到聊天，再切换到工作台时触发。在工作台上打开应用，再关闭应用回到工作台时触发。
