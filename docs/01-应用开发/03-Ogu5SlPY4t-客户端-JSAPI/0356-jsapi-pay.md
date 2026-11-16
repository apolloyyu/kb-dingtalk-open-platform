---
title: "pay"
source_url: "https://open.dingtalk.com/document/development/jsapi-pay"
namespace: "development"
slug: "jsapi-pay"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "移动支付 > pay"
doc_id: "BQDNAbyK6Q"
updated_at: "2025-08-27 18:08:22"
---

> Source: https://open.dingtalk.com/document/development/jsapi-pay
> Path: 应用开发 / 客户端 JSAPI / 移动支付 > pay
> Updated: 2025-08-27 18:08:22

# pay

调用pay，唤起支付宝或者支付宝SDK内置的支付页面完成支付功能。

> 该接口只是对支付宝移动支付SDK的支付接口做了JS形式封装，支付流程的打通还需要开发者根据[支付宝相关文档](https://opendocs.alipay.com/open/204/105051/)完成。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11521) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `info`（string，必填）：需要构建的订单信息，参考[支付宝文档](https://doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.CKTNjZ&treeId=59&articleId=103663&docType=1)。
- `has_alipay`（string，必填）：true表示支付串中指定了支付账号，不需要走绑定支付宝流程。 默认值：false。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `memo`（string，必填）：保留参数，一般无内容。
- `result`（string，必填）：本次操作返回的结果数据。
- `resultStatus`（string，必填）：本次操作的状态返回值，标识本次调用的结果，详见[客户端返回码](https://doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.MMxZUF&treeId=59&articleId=103671&docType=1)。

## **示例****代码**

### 默认出入参

```
dd.pay({
  info: 'xxx',
  has_alipay: 'false',
  success: (res) => {
    const { memo, result, resultStatus } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "memo": "mmm", "result": "xxx", "resultStatus": "9000" }
```
