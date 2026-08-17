---
title: "支付接口"
source_url: "https://open.dingtalk.com/document/development/payment-interface"
namespace: "development"
slug: "payment-interface"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 支付 > 支付接口"
doc_id: "F82Ko5Yo8S"
updated_at: "2025-09-17 20:57:15"
---

> Source: https://open.dingtalk.com/document/development/payment-interface
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 支付 > 支付接口
> Updated: 2025-09-17 20:57:15

# 支付接口

调用**biz.alipay.pay**支付接口。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.alipay.pay)在线调试该接口。

## 使用说明

钉钉集成了[支付宝移动支付SDK](https://opendocs.alipay.com/open/54/104509)并对支付SDK的接口做了JS形式的包装，开发者可以使用该接口唤起支付宝或者支付宝SDK内置的支付页面完成支付功能。

该接口只是对支付宝移动支付SDK的支付接口做了JS形式的封装，支付流程的打通还需要开发者根据[支付宝相关文档](https://opendocs.alipay.com/open/204)完成。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.alipay.pay({
    info: 'xxxx', // 订单信息，
    onSuccess: function (result) {
        {
            memo: 'xxxx', // 保留参数，一般无内容
            result: 'xxxx', // 本次操作返回的结果数据
            resultStatus: '' // 本次操作的状态返回值，标识本次调用的结果
        }
    },
    onFail: function (err) {

    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| info | String | 需要构建的订单信息，详情可参考[同步通知参数说明](https://opendocs.alipay.com/pre-open/01x3kc)。 |

## 返回结果

透传支付宝支付接口处理订单的结果，请按支付宝文档正确处理订单信息。

| 参数 | 说明 |
| --- | --- |
| memo | 保留参数，一般无内容。 |
| result | 本次操作返回的结果数据。 |
| resultStatus | 本次操作的状态返回值，标识本次调用的结果，详情可参考[同步通知参数说明](https://opendocs.alipay.com/pre-open/01x3ke)。 |
