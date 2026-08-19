---
title: "调用频次与限流"
source_url: "https://open.dingtalk.com/document/development/how-to-process-api-throttling-on-the-dingtalk-server"
namespace: "development"
slug: "how-to-process-api-throttling-on-the-dingtalk-server"
group: "应用开发"
tab: "服务端API"
breadcrumb: "平台公告与计费 > 资源与计费 > API调用量配额 > 调用频次与限流"
doc_id: "KXfGRhShDv"
updated_at: "2026-05-09 11:48:59"
---

> Source: https://open.dingtalk.com/document/development/how-to-process-api-throttling-on-the-dingtalk-server
> Path: 应用开发 / 服务端API / 平台公告与计费 > 资源与计费 > API调用量配额 > 调用频次与限流
> Updated: 2026-05-09 11:48:59

# 调用频次与限流

本文介绍了钉钉服务端API限流的触发条件和解决办法。

为防止应用程序错误而引发钉钉服务器负载异常，默认情况下，企业内部应用，或者委托某服务商做定制内部应用，每个服务端接口调用都有频率限制，当超过任一维度限制时，调用对应接口时都会返回对应错误码。

## **接口的每月调用次数限制**

> **[!NOTE]**
>
> 标准版钉钉组织，该组织内所有企业内部应用、委托第三方定制开发企业内部应用，除不纳入每月调用量限制的接口（包括获取访问凭证接口、身份验证接口、通讯录接口等，详细接口请查看[不纳入调用量限制的接口清单](1432-basic-interfaces-such-as-log-off-and-address-book.md)）之外，其他接口累计可调用次数调整为5000次/月。

### **触发条件**

标准版钉钉组织，如果超出上述每月调用次数限制。旧版服务端api返回错误码90020，新版服务端api返回错误码Forbidden.AccessDenied.ApiCountLimitForOrg。

### **解决办法**

- **通用：**可联系钉钉客户经理、钉钉城市经理或钉钉的区域服务商，升级到[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)或[钉钉专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)的扩容权益来解决。

## **接口的IP维度频次限流**

> **[!NOTE]**
>
> 由于钉钉接口的安全保护策略，每个IP在规定时间内调用钉钉接口的次数有限制，如果当前IP调用钉钉接口超出规定时间内的次数限制，会返回相应信息并被禁止调用。

### **触发条件**

每个IP，调用钉钉任意接口，超过20秒10000次，将会触发限流，当前IP的调用将会被禁止5分钟。触发此限流不会返回对应的错误码，返回的是一个html页面。信息示例如下：

```
{
   "status":1111,
   "wait":5,
   "source":"x5",
   "punish":"deny",
   "uuid":"xxx"
}
```

### **解决办法**

- **通用：**建议调用方根据OpenAPI调用量准备足够的出口IP。

## **接口的应用维度QPS限流**

> **[!NOTE]**
>
> 标准版钉钉组织调用钉钉接口，每秒调用次数不能超过20次，如果当前秒调用次数超过20，会触发相应错误，请确保每秒调用频次不超过20。

### **触发条件**

每个应用，调用每个接口，超过最高频率时，将会触发限流。旧版服务端api返回错误码90018，新版服务端api返回错误码Forbidden.AccessDenied.QpsLimitForAppkeyAndApi。

### **解决办法**

- **通用**

  - 因为qps限流限制时间是1秒，所以当遇到限流错误时，可以在程序中sleep 1秒，然后继续执行。
  - **队列调用**：针对单个应用API的QPS限流，可通过队列调用的方式解决。
- **主动单机限流**：这个是根本上解决限流的方法，如果是单个服务器调用钉钉的服务端api，可以使用类似**Guava RateLimiter**的限流sdk，来自由控制调用频率。
- **主动分布式限流**：如果是多个服务器调用钉钉的服务端api，可以使用分布式缓存，其中缓存的key是当前的秒级时间戳，value就是调用次数。

## **接口的全局维度QPS限流**

> **[!NOTE]**
>
> 由于钉钉接口的安全保护策略，每秒被调用次数有限制，当所有钉钉组织应用同时调用某个接口的次数超出该接口每秒被调用次数的限制，会触发响应错误。

### **触发条件**

当钉钉所有企业的所有应用调用同一个接口超过最高频率时，将会触发限流。旧版服务端api返回错误码90002，新版服务端api返回错误码Forbidden.AccessDenied.QpsLimitForApi。

### **解决办法**

- **通用**：因为qps限流限制时间是1秒，所以当遇到限流错误时，可以在程序中sleep 1秒，然后继续执行。
- **错峰策略**：一些定时调钉钉api的程序，可以避开钉钉的整点高峰期，比如在整点+10分的时候定时执行。
