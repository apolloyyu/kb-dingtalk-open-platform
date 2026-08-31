---
title: "JSAPI调用教程"
source_url: "https://open.dingtalk.com/document/development/client-jsapi-call-tutorial"
namespace: "development"
slug: "client-jsapi-call-tutorial"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "JSAPI调用教程"
doc_id: "b4cxQmjy3N"
updated_at: "2026-07-22 16:25:05"
---

> Source: https://open.dingtalk.com/document/development/client-jsapi-call-tutorial
> Path: 应用开发 / 客户端 JSAPI / JSAPI调用教程
> Updated: 2026-07-22 16:25:05

# JSAPI调用教程

本教程以企业内部应用为例，通过调用 `createDing`（发起DING）接口展示完整的客户端API调用流程。其他客户端API可参考此文档进行调用。

## **前置工作**

- 根据实际开发的应用类型，引入小程序或H5应用钉钉客户端SDK，详细的SDK引入方式、版本说明和兼容性信息，请参考[版本对比与迁移](0004-comparison-client-apis.md)。
- 已经了解开放平台的[基础概念](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)和[应用类型](../01-XOnnmGCTbn-开发指南/0002-application-type-introduction.md)。

## **步骤一：创建钉钉应用**

1. 访问[开发者后台](https://open-dev.dingtalk.com/?spm=dd_developers.header.unLogin.openDevBtn&hash=%23%2F#/)，单击**应用开发** > **钉钉应用** > **创建应用**。

   > **[!NOTE]**
   >
   > 本示例已企业内部应用为例，第三方企业应用和第三方个人应用创建路径一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7516308771/p1071962.png)
2. 填写应用信息，并单击**保存**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5967308771/p1071963.png)

   | **配置项** | **是否必选** | **配置说明** |
   | --- | --- | --- |
   | **应用名称** | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | **应用描述** | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
3. 进入应用详情页，在**基础信息** > **凭证与基础信息**，查看应用凭证与基础信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7516308771/p1071964.png)
4. 保存应用的**Client ID**和**Client Secret**，用于后续接口调用使用。

   > **[!NOTE]**
   >
   > **Client ID**和**Client Secret**获取可参考[基础概念](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)中说明，获取后请妥善保管，避免泄露。

## **步骤二：引入客户端SDK**

在调用任何客户端API之前，需要先引入钉钉客户端SDK。详细的SDK引入方式、版本说明和兼容性信息，请参考[版本对比与迁移](0004-comparison-client-apis.md#undefined)中的"客户端SDK"章节。

快速开始（推荐npm方式）：

```
<bash>
npm install dingtalk-jsapi --save
```

```
<javascript>
import dd from 'dingtalk-jsapi';
```

## **步骤三：鉴权配置**

> **[!NOTE]**
>
> - 该步骤只适用于H5微应用，小程序无需鉴权。
> - 鉴权的参数和配置说明，可参考[JSAPI鉴权](0002-jsapi-authentication.md)文档说明。

鉴权示例代码如下：

```
// 1. 从服务端获取签名参数（timestamp, nonceStr, signature, agentId等）
// 这些参数需要通过服务端调用钉钉服务端API获取
const configParams = {
  agentId: 'your_agent_id',
  corpId: 'your_corp_id',
  timeStamp: timestamp,
  nonceStr: nonceStr,
  signature: signature,
  jsApiList: ['createDing'] // 声明需要调用的API
};

// 2. 调用dd.config完成鉴权
dd.config(configParams);

// 3. 监听鉴权结果
dd.ready(() => {
  console.log('鉴权成功，可以调用API');
});

dd.error((err) => {
  console.error('鉴权失败', err);
});
```

## **步骤四：API 调用示例**

本文以[createDing](0265-jsapi-create-ding.md)发起DING消息为例，支持唤起DING、任务、日程等创建界面。

> 限制：目前发钉只支持客户端调用，不支持直接通过服务端发钉。

### **调用示例**

- **H5微应用示例**

  ```
  import dd from 'dingtalk-jsapi';

  // 第一步：完成鉴权（仅H5需要）
  dd.config({
    agentId: 'your_agent_id',
    corpId: 'your_corp_id',
    timeStamp: timestamp,
    nonceStr: nonceStr,
    signature: signature,
    jsApiList: ['createDing']
  });

  dd.ready(() => {
    // 第二步：调用createDing
    dd.createDing({
      users: ['03333', '04333'], // 必填：接收者的userid列表
      type: 1, // 可选：附件类型，1=图片，2=链接
      alertType: 1, // 可选：提醒类型，0=电话，1=短信，2=应用内
      text: '这是一条测试DING消息', // 可选：消息内容
      corpId: 'dingxxxxxxxxxxxxx', // 可选：企业corpId
      onSuccess: (result) => {
        console.log('发起DING成功', result);
      },
      onFail: (err) => {
        console.error('发起DING失败', err);
      }
    });
  });
  ```
- **小程序示例**

  ```
  import dd from 'dingtalk-jsapi';

  // 小程序无需鉴权，直接调用
  dd.createDing({
    users: ['03333', '04333'], // 必填：接收者的userid列表
    type: 1, // 可选：附件类型，1=图片，2=链接
    alertType: 1, // 可选：提醒类型，0=电话，1=短信，2=应用内
    text: '这是一条测试DING消息', // 可选：消息内容
    corpId: 'dingxxxxxxxxxxxxx', // 可选：企业corpId
    onSuccess: (result) => {
      console.log('发起DING成功', result);
    },
    onFail: (err) => {
      console.error('发起DING失败', err);
    }
  });
  ```

### **返回结果**

调用成功后，`onSuccess` 回调会被触发。如果调用失败，`onFail` 回调会返回错误信息。

### **常见问题与调试**

#### **API调用失败的可能原因**

- 未鉴权：H5应用必须先调用 `dd.config` 完成鉴权才能调用API
- 权限不足：检查应用是否已申请所需权限
- 参数错误：确认必填参数（如 `users`）是否正确传递
- 用户不存在：确认传入的userid是否有效且无拼写错误
- SDK版本过低：建议使用最新版本的 `dingtalk-jsapi`

#### **如何判断API是否可用**

在调用API之前，可以先判断当前环境是否支持该API：

```
<javascript>

  if (dd.biz && dd.biz.ding && dd.biz.ding.create) {  
    // API可用，可以调用  
    dd.biz.ding.create({...});
  } else {  
    console.error('当前环境不支持createDing API');
  }
```

#### 获取当前企业的corpId

如果需要动态获取当前访问用户的企业corpId，可以使用：

```
<javascript>

  dd.runtime.permission.requestAuthCode({  
    corpId: 'your_corp_id', 
    onSuccess: (result) => {    
      console.log('授权码', result.code);  
    }
  });
```

或者使用基础API：

```
<javascript>
const corpId = dd.env.corpId; // 同步获取当前企业的corpId
```
