---
title: "支付"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-payment"
namespace: "development"
slug: "mini-program-jsapi-payment"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 支付"
doc_id: "M4xF5wxlxS"
updated_at: "2025-09-17 21:01:15"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-payment
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 支付
> Updated: 2025-09-17 21:01:15

# 支付

调用**dd.pay**发起支付。

钉钉集成了[支付宝移动支付SDK](https://docs.open.alipay.com/204/105051/)并对支付SDK的接口做了JS形式的包装，开发者可以使用该接口可以唤起支付宝或者支付宝SDK内置的支付页面完成支付功能。

该接口只是对支付宝移动支付SDK的支付接口做了JS形式封装，支付流程的打通还需要开发者根据[支付宝相关文档](https://docs.open.alipay.com/204/105051/)完成。

## 示例代码

```
dd.pay({
    info:'xxx', // 订单信息
    has_alipay:'', // 默认值false，true表示支付串中指定了支付账号，不需要走绑定支付宝流程
    success: res => {
        /*{
            memo: 'xxxx', // 保留参数，一般无内容
            result: 'xxxx', // 本次操作返回的结果数据
            resultStatus: '' // 本次操作的状态返回值，标识本次调用的结果
        }*/
    },
    fail: err =>{
        dd.alert({
            content:JSON.stringify(err)
        })
    }
})
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| info | String | 需要构建的订单信息，参考支付宝文档：[https://doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.CKTNjZ&treeId=59&articleId=103663&docType=1](https://docs.open.alipay.com/204/105465/) |
| has\_alipay | String | true表示支付串中指定了支付账号，不需要走绑定支付宝流程。  **默认值**：false。 |

## 返回结果

透传支付宝支付接口处理订单的结果，请按支付宝文档正确处理订单信息。

| **参数** | **说明** |
| --- | --- |
| memo | 保留参数，一般无内容。 |
| result | 本次操作返回的结果数据。 |
| resultStatus | 本次操作的状态返回值，标识本次调用的结果，参考：[https://doc.open.alipay.com/doc2/detail.htm?spm=a219a.7629140.0.0.MMxZUF&treeId=59&articleId=103671&docType=1](https://docs.open.alipay.com/204/105301/) |
