---
title: "小程序的 JavaScript 引擎"
source_url: "https://open.dingtalk.com/document/development/the-javascript-engine-for-mini-programs-1"
namespace: "development"
slug: "the-javascript-engine-for-mini-programs-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > 小程序的 JavaScript 引擎"
doc_id: "Hm2zUoMPvk"
updated_at: "2025-09-17 20:58:13"
---

> Source: https://open.dingtalk.com/document/development/the-javascript-engine-for-mini-programs-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > 小程序的 JavaScript 引擎
> Updated: 2025-09-17 20:58:13

# 小程序的 JavaScript 引擎

小程序的 JavaScript 代码分为逻辑层脚本和 sjs 脚本，它们运行在相同的 JavaScript 引擎的不同线程中。

## 运行引擎

在不同操作系统上，小程序的 JavaScript 引擎是不同的。在 iOS 平台上，脚本运行在操作系统提供的 JavaScriptCore 引擎上；而在 Android 平台上，脚本则运行在钉钉提供的 V8 引擎上（目前使用的 V8 引擎版本为 v6.9）。

钉钉小程序通过对开发者上传的代码进行 [babel](https://babeljs.io/) 转换（注意，node\_modules 内的代码不会转换），使 JavaScript 引擎支持绝大多数 ES2015 的新特性。但是对于 ES2015 扩展的内置对象，小程序并未在 JavaScript 引擎上提供 polyfill，因此会导致在不同平台的 JavaScript 引擎中，对不同的 ES2015 扩展的内置对象支持存在差异。

开发者需要避免使用 JavaScript 引擎不支持的内置对象。 如果必须使用，可自己提供内置对象的 polyfill（Polyfill ：用于实现浏览器或其他 JavaScript 引擎不支持的原生 API 的代码 ）。

> **[!IMPORTANT]**
>
> 小程序引擎中禁止访问 globalThis、global ，因此无法直接使用 [babel-polyfill](https://babeljs.io/docs/en/babel-polyfill)。

## 客户端操作系统对主要 ES2015 扩展内置对象支持情况

下表是各个操作系统对主要 ES2015 扩展的内置对象的支持情况：

| Object | iOS 8 | iOS 9 | iOS 10 及以上 | Android |
| --- | --- | --- | --- | --- |
| Object.is | 不支持 | 支持 | 支持 | 支持 |
| Object.assign | 不支持 | 支持 | 支持 | 支持 |
| Object.keys | 支持 | 支持 | 支持 | 支持 |
| Object.getOwnPropertyDescriptor | 支持 | 支持 | 支持 | 支持 |
| Object.getOwnPropertyNames | 支持 | 支持 | 支持 | 支持 |
| Object.getOwnPropertySymbols | 不支持 | 支持 | 支持 | 支持 |

| String | iOS 8 | iOS 9 | iOS 10 及以上 | Android |
| --- | --- | --- | --- | --- |
| String.prototype.codePointAt | 不支持 | 支持 | 支持 | 支持 |
| String.prototype.normalize | 不支持 | 不支持 | 支持 | 支持 |
| String.prototype.includes | 不支持 | 支持 | 支持 | 支持 |
| String.prototype.startsWith | 不支持 | 支持 | 支持 | 支持 |
| String.prototype.endsWith | 不支持 | 支持 | 支持 | 支持 |
| String.prototype.repeat | 不支持 | 支持 | 支持 | 支持 |
| String.fromCodePoint | 不支持 | 支持 | 支持 | 支持 |

| Array | iOS 8 | iOS 9 | iOS 10 及以上 | Android |
| --- | --- | --- | --- | --- |
| Array.prototype.copyWithin | 不支持 | 支持 | 支持 | 支持 |
| Array.prototype.find | 支持 | 支持 | 支持 | 支持 |
| Array.prototype.findIndex | 支持 | 支持 | 支持 | 支持 |
| Array.prototype.fill | 支持 | 支持 | 支持 | 支持 |
| Array.prototype.entries | 支持 | 支持 | 支持 | 支持 |
| Array.prototype.keys | 支持 | 支持 | 支持 | 支持 |
| Array.prototype.values | 不支持 | 支持 | 支持 | 不支持 |
| Array.prototype.includes | 不支持 | 支持 | 支持 | 支持 |
| Array.from | 不支持 | 支持 | 支持 | 支持 |
| Array.of | 不支持 | 支持 | 支持 | 支持 |

| Number | iOS 8 | iOS 9 | iOS 10 及以上 | Android |
| --- | --- | --- | --- | --- |
| Number.isFinite | 不支持 | 支持 | 支持 | 支持 |
| Number.isNaN | 不支持 | 支持 | 支持 | 支持 |
| Number.parseInt | 不支持 | 支持 | 支持 | 支持 |
| Number.parseFloat | 不支持 | 支持 | 支持 | 支持 |
| Number.isInteger | 不支持 | 支持 | 支持 | 支持 |
| Number.EPSILON | 不支持 | 支持 | 支持 | 支持 |
| Number.isSafeInteger | 不支持 | 支持 | 支持 | 支持 |

| Math | iOS 8 | iOS 9 | iOS 10 及以上 | Android |
| --- | --- | --- | --- | --- |
| Math.trunc | 支持 | 支持 | 支持 | 支持 |
| Math.sign | 不支持 | 支持 | 支持 | 支持 |
| Math.cbrt | 支持 | 支持 | 支持 | 支持 |
| Math.clz32 | 支持 | 支持 | 支持 | 支持 |
| Math.imul | 支持 | 支持 | 支持 | 支持 |
| Math.fround | 支持 | 支持 | 支持 | 支持 |
| Math.hypot | 支持 | 支持 | 支持 | 支持 |
| Math.expm1 | 支持 | 支持 | 支持 | 支持 |
| Math.log1p | 支持 | 支持 | 支持 | 支持 |
| Math.log10 | 支持 | 支持 | 支持 | 支持 |
| Math.log2 | 支持 | 支持 | 支持 | 支持 |
| Math.sinh | 支持 | 支持 | 支持 | 支持 |
| Math.cosh | 支持 | 支持 | 支持 | 支持 |
| Math.tanh | 支持 | 支持 | 支持 | 支持 |
| Math.asinh | 支持 | 支持 | 支持 | 支持 |
| Math.acosh | 支持 | 支持 | 支持 | 支持 |
| Math.atanh | 支持 | 支持 | 支持 | 支持 |

| 内置对象 | iOS 8 | iOS 9 | iOS 10及以上 | Android |
| --- | --- | --- | --- | --- |
| Set | 支持 | 支持 | 支持 | 支持 |
| Map | 支持 | 支持 | 支持 | 支持 |
| Proxy | 不支持 | 不支持 | 支持 | 支持 |
| Reflect | 不支持 | 不支持 | 支持 | 支持 |
| Promise | 支持 | 支持 | 支持 | 支持 |

开发者也可使用 [caniuse](https://caniuse.com/) 和 [node.green](https://node.green/) 查看相关特性在 iOS 和 V8 下的支持情况。

## 对动态执行脚本的限制

出于安全考虑，小程序限制了部分 ES 的语法和 API ：

- 不支持 eval 使用
- setTimeout 和 setInterval 函数仅支持函数做回调参数，不可动态执行代码
- 不支持使用 new Function 创建函数

## 模块名保留字

小程序的逻辑层支持 ES2015 模块化语法，但是将浏览器部分内置对象名（如 window、document）作保留字使用，以应对未来的不时之需，这些保留字不可用做模块名。保留字有：globalThis、global、AlipayJSBridge、fetch、self、window、document、location、XMLHttpRequest。

## 相关文档

- [babel](https://babeljs.io/)
- [babel-polyfill](https://babeljs.io/docs/en/babel-polyfill)
