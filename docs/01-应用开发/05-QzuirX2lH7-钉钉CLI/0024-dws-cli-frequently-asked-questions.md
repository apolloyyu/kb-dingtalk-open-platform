---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/dws-cli-frequently-asked-questions"
namespace: "development"
slug: "dws-cli-frequently-asked-questions"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "常见问题"
doc_id: "nWQwMZwEmA"
updated_at: "2026-08-12 09:20:57"
---

> Source: https://open.dingtalk.com/document/development/dws-cli-frequently-asked-questions
> Path: 应用开发 / 钉钉CLI / 常见问题
> Updated: 2026-08-12 09:20:57

# 常见问题

- **组织中的 dws CLI权限默认是开启的还是关闭的？**

  默认是关闭的。dws 遵循企业统一管控规则，需要组织主管理员在开发者后台的"CLI 访问管理"里手动开启"允许成员通过 CLI 访问其个人数据"开关，成员才能登录使用。
- **dws CLI支持的用户类型是什么？**

  目前支持已加入组织的钉钉用户。
- **企业管理员有办法控制 CLI 权限吗？**

  可以。管理员在开发者后台能控制三件事：是否允许成员通过 CLI 访问个人数据、允许成员访问哪些数据范围、组织开放哪些CLI权限。
- **安装后提示"命令不存在"怎么办？**  
  确认 dws 所在目录已加入系统 PATH。Windows 推荐用 npm install -g dingtalk-workspace-cli 安装，npm 装的可执行文件目录可以用 npm root -g 查全局路径。
- **dws 登录会一直有效吗？会不会经常掉登录？**  
  不会，正常使用 30 天内不用重新扫码
- **一台电脑能同时登录多个组织或账号吗？**  
  一台电脑支持同时登录一个账号及该账号下的多个组织
- **dws CLI 会产生费用吗？？**  
  dws CLI 开源版本，暂时未计入收费体系，请开发者放心使用。
- **如何在 Dify、Cursor、Codex、Qoder 等 AI工具里使用钉钉dws CLI**  
  在任何 AI 工具里使用 ，通常需要2步，按需安装第3步：

  1. **安装 CLI**：

     ```
     curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.sh | sh
     ```
  2. **登录**

     ```
     dws auth login           # 有浏览器的环境
     dws auth login --device  # Docker / SSH / CI 等无头环境
     ```
  3. **把 Skill 分发到你的 AI 工具（可选）**

     ```
     dws skill setup --mode mono --target all --yes
     ```
- **dws CLI和千问办公里内置的钉钉能力是什么关系？**

  这些平台里内置的钉钉能力底层都是这套 dws CLI 构建的。如果你已经在这些平台里用钉钉技能，不需要单独装 dws，可以直接使用。
- **DWS CLI能读取群聊消息吗？为什么有时候读到"加密消息"？**

  支持读取群聊和单聊消息，但暂不支持加密消息解密**。**
- **DWS CLI支持创建 OA 审批单吗？**

  已在 v1.0.57 中支持，如需使用请执行dws upgrade命令更新至新版本。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0781446871/p1094436.png)![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0781446871/p1094437.png)
- **想做一个自动回复消息的机器人，dws CLI 能做吗？**

  可以，请参见文档：[5分钟配置：给自己配个嘴替AI 机器人](0005-ai-bot-configuration-guide.md)。
