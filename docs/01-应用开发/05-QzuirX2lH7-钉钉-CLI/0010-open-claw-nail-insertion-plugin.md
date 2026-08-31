---
title: "Open Claw钉钉插件"
source_url: "https://open.dingtalk.com/document/development/open-claw-nail-insertion-plugin"
namespace: "development"
slug: "open-claw-nail-insertion-plugin"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "高级集成 > OpenClaw 框架集成 > Open Claw钉钉插件"
doc_id: "pToVvtQxOI"
updated_at: "2026-07-22 16:25:42"
---

> Source: https://open.dingtalk.com/document/development/open-claw-nail-insertion-plugin
> Path: 应用开发 / 钉钉 CLI / 高级集成 > OpenClaw 框架集成 > Open Claw钉钉插件
> Updated: 2026-07-22 16:25:42

# Open Claw钉钉插件

## 场景介绍

你是否遇到过这样的困扰：AI 助手很聪明，但它无法直接读取你的钉钉文档、无法查看你的日程安排、也无法理解群聊里的上下文？你不得不反复复制粘贴，效率大打折扣。

现在，钉钉 OpenClaw 官方插件来了！

只需一次授权，OpenClaw 就能以你的身份安全地访问钉钉生态。它能帮你： 📄 提交日志、查历史日志 ， 📅 智能协调日程与会议时间，💬 向用户/群发送强提醒

**你说一句话，它就在钉钉里帮你把活儿干了。**

## **官方插件能力**

| **能力类别** | **具体能力** |
| --- | --- |
| 消息收发 | ✅接收群/私聊消息  ✅向当前会话（群/人）自动回复  ✅发送文本、Markdown（有限）、@成员 |
| 会话上下文 | ✅自动识别 conversationId / userId  ✅解析 sender 名称、ID、群名 |
| 身份与权限 | ✅使用你的钉钉登录态（OAuth 2.0）  ✅自动携带 scope 权限（**如 chat:group:send, calendar:read）** |
| 日历 & 会议 | ✅创建/查/改日程、自动带钉钉会议链接、DING 提醒 |
| ✅查询自己/他人忙闲状态（用于会议协调） |
| ✅查企业会议室列表 |
| 群聊 & 成员 | ✅列出你加入的群、查群基本信息 |
| ✅查指定群成员列表（含 openId） |
| AI 表格 | ✅创建表格、读写行数据、条件查询 |
| 待办（Task） | ✅创建个人/群待办、查状态、设截止时间 |
| 日志（日报/周报） | ✅提交日志、查历史日志（按模板） |
| DING 消息 | ✅向用户/群发送强提醒 DING（带跳转） |
| 文件 & 云盘 | ✅上传/下载文件到钉钉云盘、列目录 |
| 系统管理 | ✅登录/查看授权状态 |

此外，钉钉官方插件还支持更好的互动体验，支持**流式输出卡片回复**、**识别合并转发消息**、**发表情**等，欢迎体验！日历、会议、AI 表格等功能，预计下周上线，敬请期待！🎉

## 安全与隐私

### 重要提示

本插件目前处于快速迭代期，建议优先使用个人钉钉账号进行体验，避免在企业生产环境中直接使用，以防数据泄露风险。

### **组织合规提醒**

若计划在公司账号或群组中部署，请严格遵守公司的**信息安全红线**。避免发生数据泄露、权限突破、侵犯隐私等后果。

**其他操作风险：**

- **警惕“幻觉”**： 它有时会误解您的意图，关键信息请务必二次核实。
- **部分操作不可逆转：**部分操作一旦执行即不可撤回。请始终保持“人在回路”，坚持先预览、后确认。
- **权限授予：**推荐授予完成任务所必需的权限，定期审查授权范围。

### 使用建议

我们推荐您先从个人账号开始“调教”数字分身。待团队的安全隔离机制完善后，再逐步拓展至工作流。使用过程中遇到任何问题或体验不佳的地方，欢迎随时向我们反馈，我们正在持续快速迭代中！

## 从 0 安装钉钉插件

### 步骤一：安装并配置 OpenClaw

1. 在终端中输入以下命令：

   - **Linux/macOS：**

     ```
     curl -fsSL https://openclaw.ai/install.sh | bash
     ```
   - **Windows**

     ```
     iwr -useb https://openclaw.ai/install.ps1 | iex
     ```
2. 安装完成后，阅读安全审计建议，输入 `Yes` 确认：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070748.png)
3. 选中 `QuickStart` 开始快速配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070749.png)
4. 下拉菜单，选择适配的模型。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070751.png)
5. 获取API key：以qwen为例，前往百炼[Coding Plan概述](https://help.aliyun.com/zh/model-studio/coding-plan)网站购买，点击创建 API key：[大模型服务平台百炼控制台](https://bailian.console.aliyun.com/cn-beijing/?spm=5176.30260724.0.0.15c71883S6YawZ&tab=demohouse#/api-key)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070757.png)
6. 复制 API key，并在模型中填入 API key。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070758.png)
7. 请直接按回车键选择“Keep current”以保持当前配置。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070760.png)

### 步骤二：安装钉钉官方插件

1. 在终端中运行以下指令，启动钉钉连接器安装向导：

   ```
   npx -y @dingtalk-real-ai/dingtalk-connector install
   ```
2. 此时，屏幕终端上会出现二维码。请打开**钉钉手机 App** 扫一扫终端二维码：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070761.png)
3. 扫码后，点击 **一键创建新机器人。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070756.png)
4. **创建机器人的界面：**PC端，钉钉搜索框搜索设定的机器人名称，找到机器人并对话。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070762.png)
5. **验证成功：**在钉钉中给机器人发送一条消息（如“你好”），若收到回复，即表示安装大功告成！

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070763.png)

## **验证安装是否成功**

1. 安装成功后，可以终端打开 OpenClaw Dashboard URL，正常显示管理后台则代表安装成功。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070753.png)
2. 在管理后台的聊天页面进行对话验证，若助手可以正常响应，则说明配置成功。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9019996771/p1070750.png)

## **升级钉钉插件版本**

为提供更优质的用户体验，钉钉团队正在快速优化迭代官方插件，升级钉钉插件方法如下。

1. 运行 `openclaw -v` 命令查看已安装的 OpenClaw 的版本，新版插件对 OpenClaw 的版本要求如下。若低于该版本，插件运行可能出现异常，可执行 `npm install -g openclaw`命令升级。

   - **Linux**/**macOS：****2026.4.9** 及以上
   - **Windows：****2026.4.9** 及以上
2. 在终端中运行以下命令升级钉钉官方插件到最新版本：

   ```
   npx -y @dingtalk-real-ai/dingtalk-connector@0.8.14 install
   ```

   若执行该命令行出错，可在命令行前 增加 `sudo` 重新执行。

   ```
   sudo npx -y @dingtalk-real-ai/dingtalk-connector@0.8.14 install
   ```

## **常见问题**

- **插件安装失败**

  - **问题原因**：OpenClaw 版本与 connector 版本不兼容，或 npm 源不可达。
  - **解决方案**：确保版本匹配后，使用 `install-npm.sh` 或 `install-beta.sh` 脚本安装，检查网络是否能正常访问 npm 源。
- **macOS 安装报错**`Also not a valid hook pack`

  - **问题原因**：苹果电脑上 `openclaw.plugin.json` 缺失或格式错误。
  - **解决方案**：确认该文件存在且格式正确，检查 Node.js 版本是否满足要求，必要时重新安装 OpenClaw 主程序。
- **Linux 服务器安装报错**`package.json missing openclaw.hooks`

  - **问题原因**：阿里云 Linux 服务器上安装路径不正确或文件权限不足。
  - **解决方案**：确认 `openclaw.plugin.json` 中包含 `openclaw.hooks` 配置，检查当前用户对安装目录的读写权限。
- **特定版本未发布到 npm**

  - **问题原因**：`0.8.10` 版本未发布到 npm 仓库，导致安装时找不到包。
  - **解决方案**：使用已发布的稳定版本（如 `0.8.12`、`0.8.13`），或通过 `install-beta.sh` 安装最新 beta 版本。
- **安装后配置校验失败**`must NOT have additional properties`

  - **问题原因**：配置文件中包含 schema 未定义的字段，导致校验不通过。
  - **解决方案**：对照 `openclaw.plugin.json` 中的配置示例，移除多余属性，注意字段名的大小写和层级结构。
