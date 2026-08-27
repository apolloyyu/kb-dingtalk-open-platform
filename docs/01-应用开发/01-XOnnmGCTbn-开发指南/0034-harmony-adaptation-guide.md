---
title: "鸿蒙适配指南"
source_url: "https://open.dingtalk.com/document/dingstart/harmony-adaptation-guide"
namespace: "dingstart"
slug: "harmony-adaptation-guide"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 鸿蒙适配指南"
doc_id: "2ITkceJT3k"
updated_at: "2026-06-30 09:00:38"
---

> Source: https://open.dingtalk.com/document/dingstart/harmony-adaptation-guide
> Path: 应用开发 / 开发指南 / 开发网页应用 > 鸿蒙适配指南
> Updated: 2026-06-30 09:00:38

# 鸿蒙适配指南

本文档将根据5个清晰的步骤，用最直白的语言，指引你在鸿蒙系统中完成钉钉 JSAPI的调用。

## **第一步：更新“武器库” (升级SDK)**

在开始之前，你必须确保你的开发工具是最新的，否则你的代码在鸿蒙系统里会“报错”。

- 核心任务：把项目里的 [dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)  包升级到 3.0.45 或更高版本。
- 怎么操作：

  - 如果你用 npm：在终端运行 `npm install dingtalk-jsapi@latest --save`
  - 如果你用 yarn：运行 `yarn upgrade dingtalk-jsapi --latest`
  - 如果你用 pnpm：运行 `pnpm update dingtalk-jsapi --latest`

如果你的项目里其他依赖包偷偷引入了旧版本的 `dingtalk-jsapi`，你需要强制“锁定”版本。

- **npm方式**：在 `package.json` 里加一个 `"overrides"` 字段，强制指定版本为 `^3.0.45`。

  ```
  {
    "overrides": {
      "dingtalk-jsapi": "^3.0.45"
    }
  }
  ```
- **yarn方式**：在 `package.json` 里加一个 `"resolutions"` 字段，强制指定版本为 `^3.0.45`。

  ```
  {
    "resolutions": {
      "dingtalk-jsapi": "^3.0.45"
    }
  }
  ```
- **pnpm方式：**在 `package.json` 的 `pnpm` 节点下配置 `overrides`。

  ```
  {
    "pnpm": {
      "overrides": {
        "dingtalk-jsapi": "^3.0.45"
      }
    }
  }
  ```

## **第二步：检查“兼容性” (别踩坑)**

不是所有的功能在鸿蒙上都能直接用，你需要先看看你正在用的 JSAPI（钉钉提供的网页接口）是否支持鸿蒙。

操作方法：

1. 打开钉钉开放平台的 [JSAPI文档](../03-Ogu5SlPY4t-客户端JSAPI/0001-jsapi-overview.md)。
2. 找到你代码里用到的所有接口。
3. 查看接口详情里的 “支持说明” 栏目。
4. 确认 Harmony 一列显示的是支持（通常是 7.0.0 版本及以上）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2292754371/p890481.png)

## **第三步：编写“通用”代码 (逻辑适配)**

很多老代码会针对安卓（Android）和苹果（iOS）写不同的逻辑。现在多了个鸿蒙（Harmony），你的代码得学会“认识”它。

### **如何判断用户是鸿蒙系统？**

你可以用这 3 种方法中的任意一种（推荐第一种）：

- 方法 A（最推荐，用SDK判断）

  通过 dingtalk-jsapi sdk来判断是否鸿蒙系统。

  ```
  import { env } from 'dingtalk-jsapi/core';
  import { ENV_ENUM } from 'dingtalk-jsapi/lib/env';

  const isHarmony = env.platform === ENV_ENUM.harmony;
  if (isHarmony) {
    // 这里写鸿蒙特有的逻辑
  }
  ```
- 方法 B（通过浏览器标识判断）

  Web 页面中通过 navigator.userAgent 判断是否鸿蒙系统。

  ```
  // Web中通过navigator.userAgent判断是否鸿蒙系统

  const isHarmony = /OpenHarmony/i.test(navigator.userAgent)
  ```
- 方法 C（小程序专用）

  小程序中通过读取 getSystemInfo 中的 platform 来判断是否鸿蒙系统。

  ```
  // 小程序通过读取getSystemInfo中的platform来判断是否鸿蒙系统。
  const systemInfo = dd.getSystemInfoSync();
  const isHarmony = systemInfo.platform === 'OpenHarmony';
  ```

### **检查你的**`switch`**语句**

如果你的代码里有像下面这样的逻辑，请务必检查 `default` 分支：

```
switch (env.platform) {
  case ENV_ENUM.android: // 安卓逻辑
    break;
  case ENV_ENUM.ios: // 苹果逻辑
    break;
  default: 
    // 这里！这里！这里！
    // 请确认这里的逻辑鸿蒙系统也能正常运行，不要让鸿蒙掉进坑里。
}
```

## **第四步：真机“体检” (调试运行)**

写完代码不能只在电脑上看，必须拿真机测试，确保在鸿蒙手机上能跑通。

### **准备工作**

下载并安装最新版本[钉钉鸿蒙客户端](https://www.dingtalk.com/download#/)。

### **调试方式**

- **网页应用（微应用）**：使用钉钉提供的“[微应用四端调试工具—网页版](../06-JDICnQyZLF-开发工具/0006-micro-application-four-terminal-debugging-tool-web-edition.md)”。
- **小程序**：使用“[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)”。

  - **真机预览：**通过[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)的“预览”进行调试。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2307123371/p882197.png)
  - **真机调试：**升级钉钉客户端版本到**7.6.30**+。

    - 打开 「帮助」 > 「本地配置」，输入如下配置，保存并重启：

      ```
      {
        "DD_PROJECT_100": [
          {
            "keyPath": "enableRemoteX",
            "priority": 1000,
            "value": true
          },
          {
            "keyPath": "supportsAppxNG",
            "priority": 1000,
            "value": true
          }
        ]
      }
      ```

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8845579371/p916371.png)
    - 单击「真机调试」，等待小程序编译完成并生成调试二维码。使用钉钉「扫一扫」扫码调试。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8845579371/p916379.png)
    - 真机效果。

      ![image-4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8845579371/p916388.png)

## **第五步：****开启鸿蒙适配开关并重新发布****应用**

1. 应用适配完成后，单击对应应用，进入应用详情页面。

   > 如果你还未创建应用，详情参考[应用创建与配置](0007-create-application.md)文档。
2. 单击**基础信息** > **凭证与基础信息**，在**操作系统模块**中，开启“鸿蒙系统”开关。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2307123371/p882216.png)
3. 开启“鸿蒙系统”开关后，单击**应用发布** > **版本管理与发布**，在发布页面，创建新版本，完成发布操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2307123371/p882219.png)

## **常见问题急救包**

| **问题现象** | **可能原因** | **解决方案** |
| --- | --- | --- |
| **报错 4040** `Do not support the current environment` | SDK版本太低 | 请务必执行**第一步**，升级 `dingtalk-jsapi` 到最新版。 |
| 代码在模拟器跑得好好的，真机报错 | 未开启后台开关 | 请检查**第五步**，确保在开发者后台开启了鸿蒙适配开关。 |
