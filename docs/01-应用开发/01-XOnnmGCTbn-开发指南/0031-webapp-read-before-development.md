---
title: "客户端SDK介绍"
source_url: "https://open.dingtalk.com/document/dingstart/webapp-read-before-development"
namespace: "dingstart"
slug: "webapp-read-before-development"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 客户端SDK介绍"
doc_id: "e4xV94sxz4"
updated_at: "2026-05-13 08:58:24"
---

> Source: https://open.dingtalk.com/document/dingstart/webapp-read-before-development
> Path: 应用开发 / 开发指南 / 开发网页应用 > 客户端SDK介绍
> Updated: 2026-05-13 08:58:24

# 客户端SDK介绍

钉钉客户端SDK提供了一套简单易用的API，帮助开发者快速集成钉钉原生能力到第三方应用中。通过该SDK，可以实现通讯、身份验证、设备调用等功能的无缝对接。

## SDK架构设计

钉钉客户端SDK采用模块化设计，主要包括以下核心组件：

- **基础模块**：负责SDK初始化、版本检测与运行环境判断。
- **通信模块**：封装了与钉钉客户端的数据交互协议，确保数据传输稳定高效。
- **安全模块**：处理权限校验和敏感接口访问控制，保障调用安全性。

推荐调用路径为：引入依赖 → 初始化配置 → 权限申请 → 功能调用 → 错误监听。

## 方式一：使用npm引入（推荐）

> **[!NOTE]**
>
> 建议在全局上下文（如main.js或app.js）中完成引入，确保后续页面均可访问。

1. 使用npm安装，在项目根目录执行以下命令安装SDK：

   ```
   npm install dingtalk-jsapi --save
   ```

   > dingtalk-jsapi 3.0.27 版本后支持一段式，例如：chooseChat，同时也支持三段式，例如：biz.contact.choose。
2. 加载 dingtalk-jsapi：

   ```
   import * as dd from 'dingtalk-jsapi'; // 此方式为整体加载，也可按需进行加载
   ```
3. 安装完成后，请检查`package.json`中是否已添加对应依赖项，预期输出如下：

   ```
   "dependencies": {
     "@dd-sdk/client": "^2.0.0"
   }
   ```

## **方式二：使用cdn引入（不推荐）**

浏览器引入，在浏览器中使用 script 和 link 标签直接引入文件，并使用全局变量 dd。

```
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/3.1.0/dingtalk.open.js"></script>
```

> **[!NOTE]**
>
> 不推荐使用浏览器引入方法，这样无法按需加载，而且难以获得底层依赖模块的 bug 快速修复支持，如当前使用CDN方式，建议迁移至npm方案。

## API调用规范

dingtalk-jsapi 3.0.27 版本后支持两种调用方式：一段式和三段式。

- **一段式**：指方法名为单一动词的形式，例如 `chooseChat`，适用于简单场景下的快捷调用。
- **三段式**：指模块.子模块.方法名的形式，例如 `biz.contact.choose`，结构清晰，便于分类管理，是官方推荐的调用方式。

首次使用前需在钉钉开放平台申请相应权限，并在应用配置中启用对应能力开关。

## 快速入门：选择联系人完整示例

本示例演示如何通过 SDK 实现“选择联系人”功能，包含权限申请、API调用、结果处理及错误监听的完整流程。

### 前置准备

- 确认应用类型为**企业内部应用**或**第三方企业应用**。
- 已开通权限：`biz.contact.choose`
- 开发环境已通过 npm 引入 `dingtalk-jsapi`
- 获取企业ID（corpId）：可在钉钉开放平台首页查看。

### 示例代码

```
import * as dd from 'dingtalk-jsapi';

// 1. 发起权限请求（建议在页面加载时提前获取）
async function requestPermission() {
  try {
    const authCode = await dd.runtime.permission.requestAuthCode({
      corpId: 'your_corp_id', // 企业ID，多企业场景下必填
    });
    console.log('授权成功，authCode:', authCode);
  } catch (error) {
    console.error('权限申请失败:', error);
    alert('请允许授权后继续操作');
  }
}

// 2. 调用选择联系人功能
async function selectContacts() {
  try {
    // 使用官方推荐的三段式调用
    const result = await dd.biz.contact.choose({
      startWithOrg: true,        // 是否显示组织架构
      multiple: true,            // 是否多选

      users: [ ],                 // 默认已选用户

      disabledUsers: [ ],         // 不可选用户

      title: '选择协作成员'       // 页面标题
    });

    // 3. 处理返回结果
    if (result && result.users && result.users.length > 0) {
      console.log('选中的联系人:', result.users);
      alert(`已选择 ${result.users.length} 名成员`);
    } else {
      console.log('用户未选择任何联系人');
    }
  } catch (error) {
    // 4. 错误监听与处理
    switch (error.errCode) {
      case 12:
        console.warn('用户取消操作');
        break;
      case 10:
        console.error('权限不足，请检查应用配置');
        break;
      default:
        console.error('未知错误:', error);
    }
  }
}

// 页面初始化时请求权限
requestPermission();

// 触发选择联系人（例如绑定按钮点击事件）
document.getElementById('selectBtn').addEventListener('click', selectContacts);
```

### 示例说明

- **权限申请**：调用`dd.runtime.permission.requestAuthCode`获取临时凭证，用于鉴权。
- **功能调用**：使用三段式`dd.biz.contact.choose`打开联系人选择器。
- **结果处理**：返回对象包含`users`数组，字段包括`userId`，`name`，`avatar`等。
- **错误监听**：常见错误码参考新版接口错误码文档（如 errCode=12 表示用户取消）。
