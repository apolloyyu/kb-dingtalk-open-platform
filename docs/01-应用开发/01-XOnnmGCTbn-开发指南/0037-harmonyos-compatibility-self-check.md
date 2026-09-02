---
title: "鸿蒙自查手册"
source_url: "https://open.dingtalk.com/document/dingstart/harmonyos-compatibility-self-check"
namespace: "dingstart"
slug: "harmonyos-compatibility-self-check"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 鸿蒙自查手册"
doc_id: "tAN2wEzkyM"
updated_at: "2026-06-30 09:00:39"
---

> Source: https://open.dingtalk.com/document/dingstart/harmonyos-compatibility-self-check
> Path: 应用开发 / 开发指南 / 开发网页应用 > 鸿蒙自查手册
> Updated: 2026-06-30 09:00:39

# 鸿蒙自查手册

## **问题排查思路**

- 三方应用，如果调用了开放的jsapi，并且在Android/iOS端可以调通，但是在鸿蒙平台调用失败，可能存在鸿蒙适配问题，可以尝试开启“兼容模式”（“兼容模式”适配了Android和鸿蒙平台）；
- 如果兼容模式可解决，建议升级dingtalk-jsapi版本，以彻底适配鸿蒙；
- 如果兼容模式未解决，可能存在代码逻辑问题。首先建议开发者自查，根据h5应用/小程序应用的前端日志或者开启调试，来进行排查；
- 如果开发者在自查过程中，仍然没有进展，可反馈至钉钉。

## **问题处理步骤**

### **步骤一：**开启兼容模式

#### **兼容模式：**

步骤：我的->设置与隐私->通用->使用兼容管理->开启兼容模式

![image.jpeg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9321872871/p1034683.jpeg)![image.jpeg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9321872871/p1034685.jpeg)![image.jpeg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9321872871/p1034682.jpeg)

#### **开启兼容模式解决的问题：**

1、通过修改ua使鸿蒙设备携带Android标识，从而能够正常使用平台的API接口和功能模块，使得依赖平台类型判断的业务流程能够在鸿蒙设备上正常执行；

2、解决了低版本dingtalk-jsapi中，没有支持鸿蒙平台导致的功能不可用问题。

#### **兼容模式的原理：**

UA处理机制：

```
// App启动时的UA处理逻辑
function initApp() {
  ...
  let originalUA = 获取当前设备原始UA;
  let deviceType = detectDeviceType(originalUA);
  
  // 兼容模式开关逻辑
  if (deviceType === "HarmonyOS" && compatibilityModeEnabled()) {
    // 鸿蒙端特殊处理，在鸿蒙UA中插入Android标识
    originalUA = appendAndroidTag(originalUA);
    setModifiedUserAgent(originalUA);
  } else {
    // 其他端继续使用原始UA
    setModifiedUserAgent(originalUA);
  }
  
  // 继续应用初始化
  continueInitialization();
  ...
}
```

平台类型检测逻辑：

```
// 平台类型检测函数
function detectPlatformType() {
  const ua = getUserAgent();
  
  // 兼容模式下的鸿蒙设备会被识别为Android
  if (ua.includes("Android")) {
    return "Android";
  } else if (ua.includes("iOS") || ua.includes("iPhone") || ua.includes("iPad")) {
    return "IOS";
  } else if (ua.includes("HarmonyOS")) {
    return "HarmonyOS";
  }
  
  return "Unknown";
}
```

解决的问题：

```
// 示例：API调用场景
function callPlatformSpecificAPI() {
  // 解决API平台判断问题
  const platformType = detectPlatformType();
  
  // 在兼容模式下，api对可用性进行判断时，因为添加了Android字段会判断为可用
  if (isApiAvailable(platformType)) {
    return sdk.callMethod();
  } else {
    return sdk.error();
  }
}
```

1、开启兼容模式后，如果可以解决问题，建议参考步骤二，升级dingtalk-jsapi；

2、开启兼容模式后，如果仍未解决问题，请转到步骤三。

#### **其他情况：**

如果在使用dingtalk-jsapi之前就进行了ua的判断，需要针对鸿蒙系统进行额外的适配，在这种情况下不建议开启兼容模式，防止出现业务逻辑优先进入其他分支的情况。

```
const ua = getUserAgent();
// 如果在代码中优先判断了ua,又开启兼容模式,就会使预期进入HarmonyOS的分支进入Android
if(ua.includes("Android")){
  ...（实际进入的分支）
  // 调用dingtalk-jsapi中的apiA;
} else if (ua.includes("iOS") || ua.includes("iPhone") || ua.includes("iPad")) {
  // 调用dingtalk-jsapi中的apiB;
  ...
} else if (ua.includes("HarmonyOS")) {
  // 调用dingtalk-jsapi中的apiC;
  ...（想要进入的分支）
}...
```

### 步骤二：升级dingtalk-jsapi

```
npm install dingtalk-jsapi@latest --save
```

```
yarn upgrade dingtalk-jsapi --latest
```

```
pnpm update dingtalk-jsapi --latest
```

当项目中依赖的npm包依赖了旧版本 dingtalk-jsapi 时，需要将其升级到最新版本。

```
{
  "overrides": {
    "dingtalk-jsapi": "^3.0.45"
  }
}
```

```
{
  "resolutions": {
    "dingtalk-jsapi": "^3.0.45"
  }
}
```

```
{
  "pnpm": {
    "overrides": {
      "dingtalk-jsapi": "^3.0.45"
    }
  }
}
```

#### **版本升级说明：**

1、3.0.45及其以上的dingtalk-jsapi版本，支持纯血鸿蒙，详情参考[鸿蒙适配指南](0036-harmony-adaptation-guide.md)。

2、升级跨度比较大的版本，参考[客户端 API 更新日志](https://open.dingtalk.com/document/dinglog/client-log)。

### **步骤三：客户端侧获取前端打印日志**

1. 在端侧，点击[钉钉-诊断与还原](https://tms.dingtalk.com/markets/dingtalk/logupload)链接。
2. 用户可通过如下3个页面，进行前端日志获取和清理；

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9321872871/p1043303.png)![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9321872871/p1034684.png) ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9321872871/p1034681.png)
3. 功能一：保存h5开发日志到本地，功能二：清理h5开发日志。
4. 如果点击“h5开发日志”显示“敬请期待”，请联系钉钉客服，开通对应的权限。

### **步骤四：**开启鸿蒙适配开关，重新发布并在鸿蒙端测试

1. 应用适配完成后，点击对应应用，进入应用详情界面。
2. 单击基础信息>凭证与基础信息，在操作系统模块中，开启“鸿蒙系统”开关。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803787671/p1043304.png)
3. 开启“鸿蒙系统”开关后，单击应用发布 > 版本管理与发布，在发布页面，创建新版本，完成发布操作。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8132787671/p1034678.png)
4. 如果使用的是旧版的微应用后台参考下图开启“适配鸿蒙”按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803787671/p1043305.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803787671/p1043306.png)
5. 在鸿蒙端进行测试，如果不再弹出“适配鸿蒙”的弹窗，代表适配已完成。

### **步骤五：向钉钉提交问题**

走完以上流程如过还不能解决您的问题，请按照下面内容描述问题，联系钉钉:

- 是否为单一系统问题;
- 描述清晰的流程，提供能准确反映问题现象的截图或录屏;
- 该问题是否必现;
- 出现该问题的用户信息和发生该问题的时间。

### **常见问题**

- 旧版本无法找到发布按钮?

  答：在进入后台页面时会出现是否使用新版的提示，建议使用新版来进行应用的版本发布。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8132787671/p1034680.png)
- 鸿蒙打开h5时，处理相同域名的请求时丢失cookie？

  答：请确认请求是否跨域，鸿蒙web组件比安卓有更加严格的跨域请求校验。

  当Cookie的SameSite属性未指定时，默认值为SameSite=Lax。这种设置下，Cookie仅在用户导航到其源站点时发送，不会在跨站请求中发送。
