---
title: "DING 1.0 发钉"
source_url: "https://open.dingtalk.com/document/development/ding-1-0-hair-pin"
namespace: "development"
slug: "ding-1-0-hair-pin"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > DING > DING 1.0 发钉"
doc_id: "BWZ91U8RV7"
updated_at: "2025-09-17 20:56:42"
---

> Source: https://open.dingtalk.com/document/development/ding-1-0-hair-pin
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > DING > DING 1.0 发钉
> Updated: 2025-09-17 20:56:42

# DING 1.0 发钉

调用**biz.ding.create**实现DING 1.0发钉。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.ding.post)在线调试该接口。

## 使用说明

**DING 1.0只支持PC端发钉**。Android端和iOS端 DING 1.0已不再维护，建议使用DING 2.0发钉接口。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

## 参数说明

- 图片类型

  ```
  dd.biz.ding.post({
      users : ['100', '101'],//用户列表，userid
      corpId: 'dingb4ff1079f84f8d54', //加密的企业id
      type: 1, //钉类型 1：image  2：link
      alertType: 2,
      alertDate: {"format":"yyyy-MM-dd HH:mm","value":"2015-05-09 08:00"},
      attachment: {
          images: [''], //只取第一个image
      }, //附件信息
      text: '', //消息体
      onSuccess : function() {},
      onFail : function() {}
  })
  ```

  | 参数 | 类型 | 说明 |
  | --- | --- | --- |
  | users | Array[String] | 用户的userid列表。 |
  | corpId | String | 企业的corpid。 |
  | type | Number | Number为整数。附件类型：  - **1**：图片image - **2**：链接link |
  | alertType | Number | 钉提醒类型：  - **0**：电话 - **1**：短信 - **2**：应用内 |
  | alertDate | Object | 钉提醒时间。 |
  | attachment | Object | 附件信息。 |
  | text | String | 消息体。 |
- Link类型

  ```
  dd.biz.ding.post({
      users : ['100', '101'],//用户列表，userid
      corpId: 'dingb4ff1079fxxxx', //企业id
      type: 2, //钉类型 1：image  2：link
      alertType: 2,
      alertDate: {"format":"yyyy-MM-dd HH:mm","value":"2015-05-09 08:00"},
      attachment: {
          title: '', //附件的标题
          url: '', //附件点击后跳转url
          image: '', //附件显示时的图片 【可选】
          text: '', //附件显示时的消息体 【可选】
          showInApp: false, // 跳转url在PC客户端上的打开方式，true：从PC容器内打开，false：跳转到浏览器打开 【可选】
      }
      text: '', //消息体
      onSuccess : function() {},
      onFail : function() {}
  })
  ```

  | 参数 | 类型 | 说明 |
  | --- | --- | --- |
  | users | Array[String] | 用户的userid列表。 |
  | corpId | String | 企业的corpid。 |
  | type | Number | Number为整数。钉类型 1：image 2：link |
  | alertType | Number | 钉提醒类型：  - **0**：电话 - **1**：短信 - **2**：应用内 |
  | alertDate | Object | 钉提醒时间。 |
  | attachment | Object | 附件信息。 |
  | text | String | 消息体。 |
