---
title: "JSAPI标准输入输出对象"
source_url: "https://open.dingtalk.com/document/development/jsapi-input-output-object"
namespace: "development"
slug: "jsapi-input-output-object"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "JSAPI标准输入输出对象"
doc_id: "W9uhpzT9fW"
updated_at: "2026-08-27 14:50:31"
---

> Source: https://open.dingtalk.com/document/development/jsapi-input-output-object
> Path: 应用开发 / 客户端 JSAPI / JSAPI标准输入输出对象
> Updated: 2026-08-27 14:50:31

# JSAPI标准输入输出对象

钉钉 JSAPI 有支持三种调用形式：异步调用、同步调用（结果同步返回），同步调用（结果通过回调参数返回）。

## **异步调用**

### **示例**

```
dd.asyncApi({
 inputParam1,
 inputParam2,
 success: (res) => {
 const outputParam1 = res.outputParam1;
 const outputParam2 = res.outputParam2;
 },
 fail: (res) => {
 console.log(`error ${res}`);
 },
 complete: () => {
 },
})

// 真实案例
dd.confirm({
 title: '温馨提示',
 content: '您是否想查询快递单号：1234567890',
 confirmButtonText: '马上查询',
 cancelButtonText: '暂不需要',
 success: (res) => {
 console.log(`result is ${res}`);
 },
 fail: (res) => {
 console.log(`error ${res}`);
 },
 complete: () => {
 },
});
```

### **输入**

所有异步调用的入参中都包含以下三个参数：

| 名称 | 数据类型 | 必填 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| success | function | 否 |  | 接口调用成功的回调函数。 |
| fail | function | 否 |  | 接口调用失败的回调函数。 |
| complete | function | 否 |  | 接口调用完成的回调函数（成功或失败都会执行），该回调发生在 `success` 和 `fail` 之后。 |

### **输出**

`success`返回对象`res`的结果因不同的JSAPI而异，详见每个JSAPI文档中的「返回值」部分。`fail`返回对象`res`的统一格式如下：

| 名称 | 数据类型 | 描述 |
| --- | --- | --- |
| error | number | 小程序专属。  **[!IMPORTANT]**  已经废弃，但可以继续使用，内容和errorCode相同。  错误码，参考JSAPI文档的错误码部分，**示例值**：400002。 |
| errorCode | number | 错误码，参考JSAPI文档的错误码部分，**示例值**：400002。 |
| errorMessage | string | 错误描述。 |

`complete`没有返回对象。

## **同步调用****（结果同步返回）**

### **示例**

```
const res = dd.xxxSync(param1, param2, ..., paramN);
console.log(`result is ${res}`);

// 真实案例
const res = dd.getStorageSync({
  key: 'city',
});
console.log(`result is ${res}`);
```

### **输入**

无标准输入，参考JSAPI文档的「参数说明」部分。

### **输出**

无标准输出，参考JSAPI文档的「返回值」部分。

## **同步调用**（结果通过回调参数返回）

### **示例**

```
dd.onXxxx(param1, param2, ..., paramN, (res) => {
  const outputParam1 = res.outputParam1;
  const outputParam2 = res.outputParam2;
});

// 真实案例
dd.onBluetoothDeviceFound((res) => {
  const { RSSI, name, deviceId, localName, deviceName, advertisData } = res;
});
```

### **输入**

入参的最后一个一定是一个 callback function ，用于接收api的结果返回值，其他入参参考JSAPI文档的「参数说明」部分。

### **输出**

最后一个入参 callback function 的回调入参部分（实例中的`res`部分），回调返回的内容参考JSAPI文档的「返回值」部分。
