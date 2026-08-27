---
title: "createDingForPC"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-ding-for-pc"
namespace: "development"
slug: "jsapi-create-ding-for-pc"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "DING > createDingForPC"
doc_id: "PEqfHq7PJ1"
updated_at: "2025-08-27 18:08:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-ding-for-pc
> Path: 应用开发 / 客户端JSAPI / DING > createDingForPC
> Updated: 2025-08-27 18:08:56

# createDingForPC

调用createDingForPC，实现DING1.0发钉。

DING 1.0只支持PC端发钉。

> Android端和iOS端 DING 1.0已不再维护，建议使用[DING 2.0](https://open.dingtalk.com/document/orgapp/jsapi-createDing)发钉接口。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11653) |
| 小程序 | 不支持 | 不支持 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11653) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `corpId`（string，必填）：企业id。
- `users`（array，必填）：需要发送到的用户的userid列表。
- `type`（number）：附件类型：  
    
  \* 1：图片  
  \* 2：链接
- `alertType`（number）：钉提醒类型：  
    
  \* 0：电话  
  \* 1：短信  
  \* 2：应用内
- `alertDate`（object）：钉提醒时间。
- `alertDate.format`（string）：日期格式
- `alertDate.value`（string）：日期时间和格式要对应
- `attachment`（object）：附件信息。
- `attachment.images`（array）：图片附件列表
- `text`（string）：消息体。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.createDingForPC({
  text: '钉消息内容',
  type: 1,
  users: ['03333', '04333'],
  corpId: 'ding1234xxxxx',
  alertDate: { value: '2015-05-09 08:00', format: 'yyyy-MM-dd HH:mm' },
  alertType: 1,
  attachment: { images: ['https://xxx.com/example1.png'] },
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
