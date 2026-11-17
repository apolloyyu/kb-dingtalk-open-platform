---
title: "getThirdAppUserCustomData"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-third-app-user-custom-data"
namespace: "development"
slug: "jsapi-get-third-app-user-custom-data"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "音频会议 > getThirdAppUserCustomData"
doc_id: "7ggGVlwzx8"
updated_at: "2025-08-27 18:08:41"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-third-app-user-custom-data
> Path: 应用开发 / 客户端 JSAPI / 音频会议 > getThirdAppUserCustomData
> Updated: 2025-08-27 18:08:41

# getThirdAppUserCustomData

会议扩展应用获取用户的业务自定义信息

1. 会议扩展应用是指，企业可以在开发者后台开发H5或小程序酷应用，用户可以在会议设置面板中点击使用此酷应用，例如用下面的例子：
   ![1.jpg](https://img.alicdn.com/imgextra/i3/O1CN011RjpGX1RUGFziRqmr_!!6000000002114-2-tps-541-539.png)
2. 用户打开会议扩展应用后，通过此JSAPI获取会议用户的业务自定义信息。该业务自定义信息通过[创建用户专属短链](https://open.dingtalk.com/document/orgapp/api-createcustomshortlink) 服务端OpenAPI 接口写入，生成用户的专属短链，通过该短链入会的用户会绑定短链对应的业务自定义信息。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.5.35 | 7.5.35 | 7.6.0 | 7.6.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11856) |
| 小程序 | 7.5.35 | 7.5.35 | 7.6.0 | 7.6.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11856) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 否 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `thirdAppId`（string，必填）：会议扩展应用的appId，从开发者后台对应的微应用基础信息页面获取：  
  - 企业自建应用为原企业内部应用AgentId  
  - 第三方企业应用为原三方企业应用AppId。
- `coolAppCode`（string，必填）：会议扩展应用的酷应用id，从开发者后台对应的酷应用页面获取。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### userCustomData

（string）用户的业务自定义信息 示例：`Q09PTEFQUC0wLTEwMjcxMTdENkRDNjIxMzY3N0E5MDAwWA`

## **示例****代码**

### 默认Demo标题

```
const res = dd.getThirdAppUserCustomData({
  thirdAppId: '2818774410',
  coolAppCode: 'COOLAPP-0-1027117D6DC6213677A9000X',
});
console.log(res);
// res: '{"userCustomData":"Q09PTEFQUC0wLTEwMjcxMTdENkRDNjIxMzY3N0E5MDAwWA"}'
```

返回对象示例：

```
"Q09PTEFQUC0wLTEwMjcxMTdENkRDNjIxMzY3N0E5MDAwWA"
```
