---
title: "客户端SDK介绍"
source_url: "https://open.dingtalk.com/document/dingstart/mini-app-client-jsapi-overview"
namespace: "dingstart"
slug: "mini-app-client-jsapi-overview"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发小程序应用 > 客户端SDK介绍"
doc_id: "YNjp15Z4vJ"
updated_at: "2026-01-22 20:01:12"
---

> Source: https://open.dingtalk.com/document/dingstart/mini-app-client-jsapi-overview
> Path: 应用开发 / 开发指南 / 开发小程序应用 > 客户端SDK介绍
> Updated: 2026-01-22 20:01:12

# 客户端SDK介绍

本SDK适用于钉钉小程序、H5微应用开发者，提供在钉钉客户端内调用原生能力的JavaScript接口。

## **引入方式**

### **方式一：使用npm引入（推荐）**

1. 使用npm安装。

   ```
   npm install dingtalk-jsapi --save
   ```

   > dingtalk-jsapi 3.0.27 版本后支持一段式，例如：chooseChat，同时也支持三段式，例如：biz.contact.choose。
2. 加载 dingtalk-jsapi：

   ```
   import * as dd from 'dingtalk-jsapi'; // 此方式为整体加载，也可按需进行加载
   ```

### **方式二：使用cdn引入（不推荐）**

浏览器引入，在浏览器中使用 script 和 link 标签直接引入文件，并使用全局变量 dd。

```
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/3.1.0/dingtalk.open.js"></script>
```

> **[!NOTE]**
>
> 不推荐使用浏览器引入方法，这样无法按需加载，而且难以获得底层依赖模块的 bug 快速修复支持。

## **使用示例**

通过上方提供的两种方式，在前端引用客户端SDK后，即可调用客户端提供的相关JSAPI的能力，客户端JSAPI总览可参考[客户端API总览](../03-Ogu5SlPY4t-客户端-JSAPI/0001-jsapi-overview.md)。

以下，我们提供了关于免登、调用界面API设置标题、调用位置API获取当前位置的示例，仅供参考：

```
// 示例：完整的小程序初始化与API调用流程
import * as dd from 'dingtalk-jsapi';

// 1. 获取免登授权码
dd.getAuthCode({
  corpId: 'your_corp_id',
  onSuccess: (res) => {
    const authCode = res.authCode;
    console.log('获取authCode:', authCode);
    // 发送到服务端换取用户身份信息
  },
  onFail: (err) => {
    console.error('获取authCode失败:', err);
  }
});

// 2. 调用界面API设置标题
dd.setNavigationTitle({
  title: '我的页面'
});

// 3. 调用位置API获取当前位置
dd.getLocation({
  onSuccess: (res) => {
    console.log('位置信息:', res);
  },
  onFail: (err) => {
    console.error('定位失败:', err);
  }
});
```
