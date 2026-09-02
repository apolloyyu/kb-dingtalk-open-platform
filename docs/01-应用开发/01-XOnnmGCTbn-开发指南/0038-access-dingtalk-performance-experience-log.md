---
title: "接入钉钉性能体验日志"
source_url: "https://open.dingtalk.com/document/dingstart/access-dingtalk-performance-experience-log"
namespace: "dingstart"
slug: "access-dingtalk-performance-experience-log"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 性能优化（ISV应用） > 接入钉钉性能体验日志"
doc_id: "vXMJQKdoLK"
updated_at: "2026-01-22 20:01:14"
---

> Source: https://open.dingtalk.com/document/dingstart/access-dingtalk-performance-experience-log
> Path: 应用开发 / 开发指南 / 开发网页应用 > 性能优化（ISV应用） > 接入钉钉性能体验日志
> Updated: 2026-01-22 20:01:14

# 接入钉钉性能体验日志

## **一、背景信息**

为提升系统运行效率与用户体验，建议接入钉钉性能体验日志能力。通过该能力，开发者可实时监控应用的运行状态，快速定位页面加载慢、接口响应延迟等性能瓶颈，进而优化关键路径。

## 二、适用对象与前置条件

### 适用对象

本方案适用于以下类型的应用：

- 第三方企业应用

### 前置条件

在开始集成前，请确认已完成以下配置：

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com)，进入目标应用详情页。
2. 确保应用已添加 `biz.user.get` JSAPI 权限（用于上报用户信息时鉴权），且调用前端 `dd.config` 时包含该 API。
3. 获取以下参数：

   - `isvAppId`：可在 **应用详情页 > 凭证与基础信息** 中查看“三方企业应用AppId”。
   - `corpId`：可在企业后台 > 企业信息 页面获取。
   - `agentId`、`timeStamp`、`nonceStr`、`signature`：由服务端生成签名后提供，用于 JSAPI 鉴权。

> ⚠️ 注意：JSAPI 鉴权需企业管理员授权并完成安全域名配置，否则将无法成功初始化。

## 三、接入采集 SDK

1. 在页面 HTML 的 `<body>` 结尾处，通过 `<script>` 标签引入SDK，并添加 `defer` 属性以延迟执行，避免阻塞主流程。

   ```
   <script src="https://o.alicdn.com/dingding/bird/index.js" defer></script>
   ```
2. 在 HTML 内或者入口 index.js 处，初始化 \_\_BIRD\_CONFIG 对象。

   ```
   window.__BIRD_CONFIG = window.__BIRD_CONFIG || {};
   __BIRD_CONFIG.tags = {
     isvAppId: 'xxx', // // 取自新版应用详情页的“凭证与基础信息”中的三方企业应用AppId
   };
   __BIRD_CONFIG.disableReport = true; // 取消自动上报
   ```

   isv应用的appId可登录开发者后台，选择对应应用的应用详情查看：

   1. 应用详情新版 - 凭证与基础信息，取值原三方企业应用AppId;
   2. 应用详情旧版 - 应用信息，取值应用凭证的AppId;
3. 在页面首屏依赖的关键资源加载完成后（如核心接口返回、DOM 渲染完毕），调用 `send()` 方法触发日志上报。

   ```
   const reportPerformance = () => {
     setTimeout(() => {
       const { send } = window.__BIRD || {};
       
       window.performance && window.performance.mark("FMP");
       typeof send === 'function' && send();
     }, 500); // 延迟500ms确保脚本初始化
   };

   if (document.readyState === 'complete') {
     // 页面已加载完成，直接执行
     reportPerformance();
   } else {
     // 页面还在加载，等待load事件
     window.addEventListener('load', reportPerformance);
   }
   ```

## **四、埋点字段**

基础埋点只会采集浏览器默认的性能数据，如果需要针对接口、资源加载有更细致的数据，需要手动上报下面的埋点：

### **字段列表**

| **字段描述** | **值** |
| --- | --- |
| HTML header执行 | Custom\_htmlHeaderStart |
| 内联的style开始执行 | Custom\_inlineStyleStart |
| 内联的style执行结束 | Custom\_inlineStyleEnd |
| 同步Style开始加载 | Custom\_linkStyleStart |
| 同步的Style执行结束 | Custom\_linkStyleEnd |
| 内联的js开始执行 | Custom\_inlineJsStart |
| 内联的js执行结束 | Custom\_inlineJsEnd |
| HTML预渲染解析 | Custom\_preRenderParseStart |
| HTML预渲染开始 | Custom\_preRenderStart |
| HTML预渲染结束 | Custom\_preRenderEnd |
| 同步JS开始加载 | Custom\_linkJsStart |
| 同步JS执行结束 | Custom\_linkJsEnd |
| 异步js开始执行 | Custom\_linkJsLoadStart |
| 异步js执行结束 | Custom\_linkJsLoadEnd |
| 首个JS入口 | Custom\_firstJsEntry |
| 接口请求前 | Custom\_rtStart |
| 接口请求后 | Custom\_rtEnd |
| 主要内容出现的时间 | FMP |

### **埋点方法调用示例**

1、更多埋点调用方式

```
window.performance.mark("Custom_htmlHeaderStart")
```

2、自定义埋点示例

用于应用采集自定义的数据，不会被展示到可视化报表，只记录相关数据

```
window.performance.mark("dingding_user_init")
```

## **五、注意事项**

如果用户信息上报，需要授权biz.user.get的JSAPI之后，才能够采集到用户的信息

```
// 前端dd.config鉴权
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/2.10.3/dingtalk.open.js"></script>

<script>
	window.dd.config({
		agentId: 'xxx', // 必填，微应用ID
        corpId: 'xxx',//必填，企业ID
        timeStamp: 1736749852931, // 必填，生成签名的时间戳，由服务端返回
        nonceStr: 'xxx', // 必填，自定义固定字符串，和服务端生成签名保持一致
        signature: 'xxx', // 必填，签名
        type: 0,
        jsApiList : [
          'biz.user.get', // 固定填写
        ],
	});
</script>
```
