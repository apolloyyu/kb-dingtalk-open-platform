---
title: "授权套件SDK"
source_url: "https://open.dingtalk.com/document/development/unified-licensing-suite-sdk"
namespace: "development"
slug: "unified-licensing-suite-sdk"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "API 调用指南 > 授权套件 > 授权套件SDK"
doc_id: "851TXxaWYY"
updated_at: "2026-07-02 10:35:11"
---

> Source: https://open.dingtalk.com/document/development/unified-licensing-suite-sdk
> Path: 应用开发 / 服务端 API / API 调用指南 > 授权套件 > 授权套件SDK
> Updated: 2026-07-02 10:35:11

# 授权套件SDK

本文介绍了如何使用钉钉统一授权套件SDK。

## **版本要求**

钉钉统一授权套件SDK要求，钉钉版本需要在**6.3.35及以上**。低版本需提示用户升级客户端，你可以通过以下方式判断钉钉版本。

```
import { getENV, } from 'dingtalk-jsapi/lib/env';
import { compareVersion, } from 'dingtalk-jsapi/lib/sdk/sdkLib';

const { platform, version, appType, } = getENV();
/**
 * 判断当前app版本是否支持使用SDK
 * @return {boolean}
 */
function isAuthSDKSupport() {
  return compareVersion(version, '6.3.35');
}
```

## **一、****安装授权套件SDK**

1. 执行以下命令，下载安装SDK（dingtalk-design-libs需要版本在0.1.0及以上）。

   ```
   npm install dingtalk-design-libs --save
   ```
2. 下载完成后，直接在代码中导入即可。

   ```
   import { openAuth } from 'dingtalk-design-libs/biz/openAuth';
   ```

## **二、应用授权接入**

> **[!NOTE]**
>
> 一旦用户明确同意过授权，其授权关系会记录在后台，直到用户主动取消授权。

可以通过以下步骤使用钉钉统一授权套件引导用户授权相关信息。

1. 引入钉钉统一授权套件SDK。

   ```
   import { openAuth } from 'dingtalk-design-libs/biz/openAuth';
   ```
2. 在需要用户授权时直接调用**openAuth**即可，请求示例如下：

   ```
   openAuth({
     clientId:'dingwlanwxxx', // 应用ID(唯一标识)
     corpId:'', // 当前组织的corpId
     rpcScope:'Calendar.Event.Write,Calendar.Event.Read,Contact.User.Read', 
     fieldScope:'Contact.User.mobile',
     type:0 // 0 表示授权个人信息；1 标识授权组织信息
   }).then((res)=>{
   // 处理返回数据
   })
   ```

### **请求参数**

| **参数** | **类型** | **是否必须** | **示例值** | **描述** |
| --- | --- | --- | --- | --- |
| clientId | string | 是 | f1dLkxxx | 应用ID：   - 企业内部应用或第三方企业应用使用[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 - 第三方个人应用使用[App ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#c0e465e9857uj)。 - 定制应用使用[CustomKey](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 |
| corpId | string | 是 | ding123xxxx | 当前组织的corpId。   - 企业内部应用，填写当前应用所在的企业CorpId。 - 第三方企业应用，填写当前应用所在授权企业的CorpId。 - 第三方个人应用，填写当前个人应用所在的企业CorpId。 |
| rpcScope | string | 否 | Contact.User.Read | 接口scope列表。  **[!NOTE]**   - 多个scope使用英文逗号分隔。 - rpcScope与fieldScope至少传一项。 |
| fieldScope | string | 否 | Contact.User.mobile | 字段scope列表。  **[!NOTE]**  多个scope使用英文逗号分隔。  rpcScope与fieldScope至少传一项。 |
| type | string | 是 | 0 | 授权类型：   - **0**：申请个人授权 - **1**：申请组织授权 |
| from | string | 否 | alicloud | 请求来源。  **[!NOTE]**  由调用方设置的位置标识，可自定义。 |

## **三、****响应信息**

返回示例如下：

- 授权完成

  ```
  {
   status: 'ok',
   result: {
   authCode:'xxxxxxx' // 如果是组织授权（type=1），则不返回该值
   }
  }
  ```
- 拒绝授权

  ```
  {
      status: 'cancel',
      result: null
  }
  ```
- 向管理员发送了授权申请，等待授权（只在组织授权场景下出现）

  ```
  {
      status: 'toAdmin',
      result: null
  }
  ```
- 授权异常

  ```
  {
      status: 'failed',
      result: null
  }
  ```

### **返回参数**

| **字段名** | **类型** | **示例值** | **描述** |
| --- | --- | --- | --- |
| status | string | ok | 授权结果：   - **ok：**授权成功 - **toAdmin：**向管理员发送授权申请，等待授权 - **failed：**授权异常 - **cancel：**主动取消授权 |
| result | Object |  | 返回结果。 |
| result.authCode | string | mrtjjwdmxxx | 个人临时授权码。  **[!NOTE]**  当type=0时，授权成功会返回。 |

### **错误码**

#### **参数错误**

| **错误码code** | **错误原因** |
| --- | --- |
| 400001 | 空请求。 |
| 400006 | clientId参数必填。 |
| 400007 | corpId参数必填。 |
| 400008 | uid为空，请联系钉钉。 |

#### **权限点相关错误**

| **错误码code** | **错误原因** |
| --- | --- |
| 500201 | 权限点code错误。 |
| 500202 | rpcScope参数需要填写rpc类型的权限点。 |
| 500203 | fieldScope参数需要填写field类型的权限点。 |
| 500204 | 组织授权需要填写组织类型的权限点。 |
| 500205 | 个人授权需要填写个人类型的权限点 |

#### **应用相关错误**

| **错误码code** | **错误原因** |
| --- | --- |
| 500101 | 应用不存在。 |
| 500102 | 应用未添加任何权限点。 |
| 500103 | 获取应用信息失败。 |
| 500104 | 应用未添加该权限点，请在开发者后台添加。 |
| 500105 | 获取应用供应商组织信息失败。 |

#### **授权相关错误**

| **错误码code** | **错误原因** |
| --- | --- |
| 500401 | 获取授权人角色失败。 |
| 500402 | 非当前组织管理员。 |
| 500403 | 企业未开通授权此应用。 |
| 500404 | 更新授权记录失败。 |

## 四、取消授权（第三方个人应用）

打开取消授权页面的方式和打开授权页面方式一致，只有path值不同，示例代码如下：

```
openAuthMiniApp({
    path:'pages/cancel/index',
    extraData:{
        clientId:'xxxxxx',
        ext:'{}',
        from:'' // 'aliCloud'
    }
})
```

## 授权套件SDK参数说明

### **请求信息**

请求示例：

```
openAuthMiniApp({
    panelHeight: 'percent75',
    path: 'pages/home/home', //不要改,这里是小程序dingwlanwvdmrtjjwdmd下的一个页面地址
    extraData:{
        clientId:'dingwlanwxxx', // 应用ID(唯一标识)
        rpcScope:'Contact.User.Read',//获取用户个人信息接口对应的权限点
        fieldScope:'Contact.User.mobile',//用户个人手机号信息字段对应的权限点
        type:0,//非必传，固定值0，表示通用授权。
        ext: JSON.stringify({}),//非必传，扩展字段。
        from:'testxxx' //请求来源，由调用方设置的唯一标识。
    }
})
```

参数说明：

| 参数 | 类型 | 是否必须 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| panelHeight | string | 是 | percent75 | 浮窗高度。  **[!NOTE]**  取值可以是屏幕占比百分比，也可以是确定的高度。例如：   - **percent50**：表示占比屏幕的50%，数字在`(0-100]`之间，大于或小于边界按边界处理。 - **1000**：表示确切的高度，单位为pt(非px)。如果不设置或者设置为0，则显示效果为全屏浮窗。 |
| path | string | 是 | pages/home/home | 授权套件打开的页面，取值。   - **pages/home/home**：打开授权页面 - **pages/cancel/index**：取消授权页面 |
| clientId | string | 是 | f1dLkxxx | 应用ID。   - 企业内部应用使用**AppKey** - 第三方企业应用使用**SuiteKey** - 第三方个人应用使用**AppId** - 定制应用使用**CustomKey** |
| rpcScope | string | 否 | Contact.User.Read | 接口scope列表，使用英文逗号分隔。  **[!NOTE]**  **rpcScope**与**fieldScope**至少传一项。 |
| fieldScope | string | 否 | Contact.User.mobile | 字段scope列表，使用英文逗号分隔。  **[!NOTE]**  **rpcScope**与**fieldScope**至少传一项。 |
| type | string | 否 | 0 | 固定值0，表示通用授权。 |
| from | string | 是 | alicloud | 请求来源，由调用方设置的唯一标识。 |
| ext | string | 否 | {} | 扩展字段。 |

### 返回信息

返回示例：

- 同意授权

  ```
  {
      status: 'ok',
      result: {
          authCode:'xxxxxxx'
      }
  }
  ```
- 拒绝授权

  ```
  {
      status: 'cancel',
      result: null
  }
  ```
- 授权异常

  ```
  {
      status: 'failed',
      result: null
  }
  ```

参数说明：

| 字段名 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| status | string | ok | 授权结果。   - **ok**：授权成功 - **failed**：授权异常 - **cancel**：主动取消授权 |
| result | object |  | 返回结果。 |
| result.authCode | string | mrtjjwdmxxx | 访问个人数据的临时授权码。 |

## 授权有效期

一旦用户明确同意过授权，其授权关系会记录在后台，直到用户主动取消授权。

## 相关链接

- [小程序调用Demo](https://github.com/open-dingtalk/eapp-auth-demo)
- [H5调用（React）Demo](https://github.com/open-dingtalk/eapp-auth-demo/blob/master/react_demo.js)
- [H5调用（Vue）Demo](https://github.com/open-dingtalk/eapp-auth-demo/blob/master/vue_demo.vue)
