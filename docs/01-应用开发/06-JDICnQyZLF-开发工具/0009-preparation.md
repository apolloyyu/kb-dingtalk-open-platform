---
title: "准备工作"
source_url: "https://open.dingtalk.com/document/download/preparation"
namespace: "download"
slug: "preparation"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > DingTalk Design CLI > 准备工作"
doc_id: "7TUdGOHv9R"
updated_at: "2026-08-18 09:13:15"
---

> Source: https://open.dingtalk.com/document/download/preparation
> Path: 应用开发 / 开发工具 / 开发者工具 > DingTalk Design CLI > 准备工作
> Updated: 2026-08-18 09:13:15

# 准备工作

在使用 DingTalk Design CLI 前，请确保开发环境满足以下条件，以保障工具的正常安装与运行。

## 适用对象

本工具适用于以下开发者：

- 钉钉企业内部应用的前端开发人员
- 第三方ISV服务商，需进行定制化组件或主题开发
- 参与基于 DingTalk Design 设计体系进行 UI 组件库构建和维护的技术团队

该CLI工具主要用于快速搭建符合钉钉设计规范的UI组件、主题包及可视化模块，支持高效生成标准化资源。

## **准备工作**

在使用 DingTalk Design CLI 前，请确保开发环境满足以下条件，以保障工具的正常安装与运行。

### **检查 Node.js 版本**

DingTalk Design CLI 依赖 Node.js 环境，**请确保已安装 Node.js 12.15.x 或更高版本**。可通过终端执行 `node -v` 命令查看当前版本。

> **[!NOTE]**
>
> 若未安装，请访问 [Node.js 官网](https://nodejs.org/en/) 下载并安装 LTS 版本，以获得最佳兼容性与稳定性。

```
node -v
```

建议使用 Node.js v16.x ~ v18.x 系列版本，避免因过低或过高版本导致依赖冲突。

### **安装 CLI 工具**

使用 npm 包管理器全局安装 DingTalk Design CLI：

```
npm i dingtalk-design-cli@latest -g
```

安装完成后，执行以下命令验证是否成功安装并输出版本号：

```
ding -v
```

如正确显示版本信息（例如 `@dingtalk/design-cli/1.2.0 darwin-x64 node-v18.17.0`），表示安装成功。

## 命令列表

| **命令** | **用途说明** |
| --- | --- |
| `ding -v` | 查看当前 CLI 版本号 |
| `ding help` | 显示帮助文档与可用命令列表 |
| `ding init` | 初始化一个新的组件或主题项目，自动生成模板结构与配置文件 |
| `ding dev` | 启动本地开发服务器，支持热更新与实时预览 |
| `ding build` | 构建生产环境资源，输出标准化的组件包或主题包 |
| `ding preview` | 对已有构建结果启动本地预览服务 |
| `ding login` | （可选）登录钉钉开发者账号，用于关联组件市场发布权限 |

建议结合 `--help` 参数查看各子命令的详细选项，例如：`ding build --help`。

## 常见问题

- **命令未找到：**`ding: command not found`

  **原因**：npm 全局 bin 目录未加入系统 PATH 环境变量

  **解决方案**：

  1. 检查 npm 全局路径：通常返回如 `/Users/username/.nvm/versions/node/v18.17.0`，其下的 `bin` 目录需加入 PATH。
  2. 在 shell 配置文件（`.zshrc` / `.bashrc`）中添加：
- **版本过旧或缓存污染**

  **建议操作**：

  ```
  npm uninstall -g dingtalk-design-cli
  npm cache clean --force
  npm i dingtalk-design-cli@latest -g
  ```
