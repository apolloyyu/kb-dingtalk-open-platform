---
title: "scanCard"
source_url: "https://open.dingtalk.com/document/development/jsapi-scan-card"
namespace: "development"
slug: "jsapi-scan-card"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 扫码 > scanCard"
doc_id: "sa1pktShQN"
updated_at: "2025-08-27 18:08:02"
---

> Source: https://open.dingtalk.com/document/development/jsapi-scan-card
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 扫码 > scanCard
> Updated: 2025-08-27 18:08:02

# scanCard

调用scanCard扫名片。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11698) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11698) |

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

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `ADDRESS`（string，必填）：地址。
- `COMPANY`（string，必填）：公司。
- `NAME`（string，必填）：姓名。
- `MPHONE`（string，必填）：手机号。
- `PHONE`（string，必填）：电话。
- `IMAGE`（string，必填）：名片图片地址，可供用户手动上传名片。
- `POSITION`（string，必填）：职位。

## **示例****代码**

### 默认出入参

```
dd.scanCard({
  success: (res) => {
    const { NAME, IMAGE, PHONE, MPHONE, ADDRESS, COMPANY, POSITION } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "NAME": "李乔",
  "IMAGE": "http://www.taobao.com/xxx.jpg",
  "PHONE": "01087654321",
  "MPHONE": "861333567890",
  "ADDRESS": "深圳市南山区软件产业基地",
  "COMPANY": "深圳市李乔科技有限公司",
  "POSITION": "CEO"
}
```
