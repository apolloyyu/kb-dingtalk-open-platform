---
title: "其他参考"
source_url: "https://open.dingtalk.com/document/dingstart/call-the-workbench-api"
namespace: "dingstart"
slug: "call-the-workbench-api"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 其他参考"
doc_id: "SO2afwaWFW"
updated_at: "2026-08-19 09:12:29"
---

> Source: https://open.dingtalk.com/document/dingstart/call-the-workbench-api
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 其他参考
> Updated: 2026-08-19 09:12:29

# 其他参考

调用工作台API前，需要先获取API调用凭证并申请接口权限。

## **打开应用或链接**

如何在组件内打开其他应用或者链接，通过调用 **getSdk().openApp** 方法。

### **移动端**

跳转的应用可以是网页应用（原H5微应用），可以是小程序应用，也可以是应用中的某个页面地址。

> **[!NOTE]**
>
> 如果想要打开外部链接，可以先将外部链接注册成钉钉的H5微应用，再跳转到该微应用。

```
// 打开微应用
getSdk().openApp({
  // 要跳转的应用的完整链接，小程序应用是dingtalk开头的链接
  url: '',
});
```

### **PC 端**

组件内链接在PC端和移动端的打开方式具有差异。

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

## **调用工作台 API**

### **开放能力**

在调用DingTalk OpenAPI中的工作台相关接口前，必须从开放平台获取访问凭证API Token，这个访问凭证包含你的企业信息以及可调用的接口权限，目前可调用工作台相关的接口如下：

- [获取工作台插件检验的规则信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1001-you-can-call-this-operation-to-obtain-the-information-about.md)
- [获取工作台插件权限点](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1000-obtain-the-permissions-of-the-workbench-plug-in.md)

### **获取访问凭证API Token**

API Token是由钉钉开放平台颁发，用来调用钉钉开放平台提供的应用管理能力。在调用钉钉开放平台提供的应用管理能力前，需要通过以下步骤，获取API Token：

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 在开发者后台首页，单击**生成TOKEN**，用于生成持久的API Token。

   > **[!NOTE]**
   >
   > - 重新生成API Token之后，之前的API Token会失效。
   > - 同一企业同一时间生效的API Token只有一个。

   ![获取API Token](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3700594261/p290038.png)
3. （可选）生成Token后，单击后面的设置图标，设置Token的IP白名单。

   > **[!NOTE]**
   >
   > 出于安全性考虑，钉钉开放平台提供了生成Token和设置Token生效的IP白名单功能，降低了因Token泄漏导致的安全风险。

   ![设置IP白名单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3700594261/p290039.png)

### **权限申请**

通过以下步骤添加工作台相关接口权限：

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/index)，然后单击目标应用，进入**应用详情**页。
2. 在**应用详情**页，单击**权限管理**，然后选择**工作台**。
3. 选择工作台相关接口权限，最后单击**申请权限**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8137405171/p786690.png)

### **接口调用流程**

如下图所示，在调用工作台API前，您需要完成以下准备工作：

1. 添加接口调用权限。应用创建后默认只开放登录和消息通知接口的调用权限，您需要根据开发需要，添加对应的接口使用权限。
2. 获取应用的access\_token。access\_token相当于是身份凭证。调用接口时，通过access\_token来鉴权调用者身份。

   - 企业内部应用请参考[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)。
   - 第三方企业应用请参考[获取第三方应用授权企业的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)。

     ![调用流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5025515361/p132205.png)

### **调用方式**

钉钉开放平台提供了API Explorer和SDK方便开发者调用服务端API。

- API Explorer：

  API Explorer是可视化在线API调用工具，可实时查看API请求和返回结果。访问地址：<https://open-dev.dingtalk.com/apiExplorer>
- SDK:

  钉钉开放平台提供了Java、PHP、Python、.NET SDK供开发者使用。单击[服务端SDK下载](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。

## **其他 JSAPI 参考**

### **查看地图位置**

**openLocation**

更多参数内容。请参考[使用内置地图查看位置](../../01-应用开发/03-Ogu5SlPY4t-客户端-JSAPI/0325-jsapi-open-location.md)。

```
getSdk().openLocation({
    longitude: '120.126293',
    latitude: '30.274653',
    name: '黄龙万科中心',
    address: '学院路77号',
});
```

### **扫码**

**scan**

更多参数内容。请参考[扫码](../../01-应用开发/03-Ogu5SlPY4t-客户端-JSAPI/0406-jsapi-scan.md)。

```
getSdk().scan({
    type: 'qr',
    success: (res) => {
       dd.alert({ title: res.code });
    },
});
```
