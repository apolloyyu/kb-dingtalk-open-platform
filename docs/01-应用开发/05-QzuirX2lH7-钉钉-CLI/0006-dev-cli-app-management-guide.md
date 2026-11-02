---
title: "开发者命令行 · CLI 应用管理指南"
source_url: "https://open.dingtalk.com/document/development/dev-cli-app-management-guide"
namespace: "development"
slug: "dev-cli-app-management-guide"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "新手入门 > 命令速查 > 开发者命令行 · CLI 应用管理指南"
doc_id: "JhNOrF0vs1"
updated_at: "2026-06-26 17:11:34"
---

> Source: https://open.dingtalk.com/document/development/dev-cli-app-management-guide
> Path: 应用开发 / 钉钉 CLI / 新手入门 > 命令速查 > 开发者命令行 · CLI 应用管理指南
> Updated: 2026-06-26 17:11:34

# 开发者命令行 · CLI 应用管理指南

> **[!NOTE]**
>
> - 建应用、配权限、加成员、挂机器人、发布上线，一行命令搞定。
> - 不开后台，不写 SDK，不翻文档。

## 这是什么

`dws dev`是钉钉 CLI（`dingtalk-workspace-cli`）内置的**开放平台应用管理**命令组。你可以在终端里用一行命令完成过去需要登录开发者后台、逐页点击才能做到的事情：

```
创建应用 → 配权限 → 加成员 → 挂机器人 → 发版上线 → 接到本地调试
```

全程不离开编辑器，不翻文档，不写一行 SDK 代码。

## 安装

```
# macOS / Linux
curl -fsSL https://gitee.com/DingTalk-Real-AI/dingtalk-workspace-cli/raw/main/scripts/install.sh | sh

# Windows (PowerShell)
irm https://gitee.com/DingTalk-Real-AI/dingtalk-workspace-cli/raw/main/scripts/install.ps1 | iex
```

安装完成后登录授权：

```
dws auth login
```

## 核心概念：应用是一棵树

在开放平台，一个**企业内部应用**就是一个容器，所有能力挂在它下面：

```
企业内部应用（主键 unifiedAppId）
├── 凭证 ─── appKey / appSecret（调 OpenAPI 的身份）
├── 权限 ─── 权限点 scopeValue（授权一组 API）
├── 成员 ─── 开发者 / 管理员角色
├── 安全 ─── IP 白名单 / 登录重定向
├── 能力扩展
│   ├── 网页应用 ─── 钉钉内打开的 H5 页面
│   └── 机器人 ──── 群聊 / 单聊收发消息
└── 版本 ─── 配置变更的生效通道（改配置 ≠ 上线）
```

**所有**`dws dev`**命令都是对这棵树上某个节点的操作。**

## 命令速查表

| **你想做什么** | **命令** | **说明** |
| --- | --- | --- |
| 查看所有应用 | `dws dev app list` | 支持按名称 / appKey 过滤 |
| 创建应用 | `dws dev app create --name "我的应用"` | 返回 unifiedAppId |
| 查看应用详情 | `dws dev app get --unified-app-id <ID>` | 查状态、凭证等 |
| 获取凭证 | `dws dev app credentials get --unified-app-id <ID>` | 拿 appKey / appSecret |
| 配权限 | `dws dev app permission add --scope-values <权限点>` | 按 scopeValue 申请 |
| 加成员 | `dws dev app member add --user-id <UID>` | 添加开发者等角色 |
| 配网页应用 | `dws dev app webapp config --mobile-url <URL>` | 设置 H5 首页地址 |
| 配机器人 | `dws dev app robot config --name "助手"` | 首次创建 / 修改配置 |
| 启用机器人 | `dws dev app robot enable` | 开启机器人能力 |
| 创建版本 | `dws dev app version create` | 打包变更为一个版本 |
| 预检审批 | `dws dev app version check-approval` | 看是否需要审批 |
| 发布版本 | `dws dev app version publish` | 上线生效 |
| 查版本状态 | `dws dev app version status` | RELEASE 才算生效 |
| 本地调试 | `dws dev connect` | 把机器人接到本地 Agent |

> **[!NOTE]**
>
> 所有写操作建议先加`--dry-run`预览参数，确认后换`--yes`执行。

## 实战演示：从零创建一个 AI 机器人

以下是一个完整的真实操作过程—创建应用、配机器人、走版本发布，全程在终端完成。

### Step 1：查看当前应用列表

```
$ dws dev app list --format json
```

```
{
  "hasMore": false,
  "items": [
    {
      "name": "xxx-预发",
      "desc": "你的管理秘书",
      "unifiedAppId": "a07c3e37-...",
      "creatorName": "xxx"
    },
    {
      "name": "xxx",
      "desc": "你的管理秘书",
      "unifiedAppId": "db90989c-...",
      "creatorName": "xxx"
    }
  ]
}
```

> 一条命令看到企业所有内部应用，包括 `unifiedAppId`（后续所有操作的主键）。

---

### Step 2：创建应用（先 dry-run 再执行）

**先预览参数，不实际执行：**

```
$ dws dev app create --name "AI客服助手-demo" --desc "演示用应用" --format json --dry-run
```

```
{
  "invocation": {
    "dry_run": true,
    "tool": "create_dev_app",
    "params": {
      "desc": "演示用应用",
      "name": "AI客服助手-demo"
    }
  },
  "response": {
    "dry_run": true,
    "note": "execution skipped by --dry-run"
  }
}
```

> **[!NOTE]**
>
> `--dry-run` 让你在执行前确认参数无误。确认后换 `--yes`：

**正式创建：**

```
$ dws dev app create --name "AI客服助手-demo" --desc "演示用应用" --format json --yes
```

```
{
  "appKey": "dingxxxxxxxxxx",
  "name": "AI客服助手-demo",
  "desc": "演示用应用",
  "unifiedAppId": "3cb7e6b1-..."
}
```

> **[!NOTE]**
>
> 应用创建完成，拿到 `unifiedAppId`。后续所有操作都用它定位这个应用。

### Step 3：配置机器人

```
$ dws dev app robot config --unified-app-id "3cb7e6b1-..." --name "AI客服小助手" --brief "智能客服机器人" --format json --yes
```

```
{
  "success": true,
  "operation": "CREATED",
  "robotCode": "dingxxxxxxxxxx",
  "robotStatus": "ONLINE",
  "configured": true,
  "unifiedAppId": "3cb7e6b1-..."
}
```

> **[!NOTE]**
>
> - 一行命令完成机器人创建和配置。`robotStatus: "ONLINE"` 表示机器人能力已开启。
> - 但还不能在钉钉里搜到——需要**版本发布**才算上线。

### Step 4：创建版本

```
$ dws dev app version create --unified-app-id "3cb7e6b1-..." --format json --yes
```

```
{
  "version": "1.0.0",
  "versionId": "28dd7568-...",
  "versionStatus": "INIT"
}
```

> **[!NOTE]**
>
> 把当前的配置变更（包括刚配的机器人）打包成版本 `1.0.0`。

### Step 5：预检审批

```
$ dws dev app version check-approval --unified-app-id "3cb7e6b1-..." --version-id "28dd7568-..." --format json
```

```
{
  "requiresApproval": true,
  "completionState": "WAITING_FOR_APPROVER_SELECTION",
  "approvalPromptText": "版本发布需要审批，请选择一位审批人（共 57 位）：\nA. xxx ...\nB. xxx ...",
  "nextSteps": [
    {
      "id": "select_approver",
      "blocking": true,
      "requiresUserInput": true,
      "doneWhen": "用户从 approvalOptions 中选择一位审批人"
    },
    {
      "id": "publish_version",
      "command": "dws dev app version publish --approver-user-id <selectedUserId> --yes"
    }
  ]
}
```

> **[!NOTE]**
>
> CLI 会告诉你是否需要审批，并列出候选审批人。**选哪个审批人由你决定**，CLI 不会替你选。

### Step 6：发布上线

```
# 选好审批人后，提交发布
$ dws dev app version publish --unified-app-id "3cb7e6b1-..." --version-id "28dd7568-..." --approver-user-id "<userId>" --format json --yes

# 查状态，等 versionStatus = RELEASE 就上线了
$ dws dev app version status --unified-app-id "3cb7e6b1-..." --version-id "28dd7568-..." --format json
```

> **[!NOTE]**
>
> 审批通过后 `versionStatus` 变为 `RELEASE`，机器人就能在钉钉中被搜索到、加到群里了。

### Step 7（可选）：接到本地调试

```
$ dws dev connect --unified-app-id "3cb7e6b1-..."
```

> **[!NOTE]**
>
> 用 Stream 长连接把机器人消息转到本地 Agent 处理。用户在钉钉里 @机器人，消息实时到你本地终端。

## 完整流程时序图

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4905642871/p1084165.png)

## 生效模型：改配置 ≠ 上线

这是很多开发者踩的坑：配了权限 / 机器人，但在钉钉里"没生效"。原因是**配置变更需要走版本发布才上线**：

```
改配置（permission add / robot config / webapp config ...）
  ↓
version create（打包变更）
  ↓
version check-approval（预检是否要审批）
  ↓
version publish（提交发布，需审批时选审批人）
  ↓
versionStatus = RELEASE → 线上生效 ✅
```

**常见问题自查**：

| **现象** | **原因** | **解决** |
| --- | --- | --- |
| 权限加了还报错 | 版本未发布到 RELEASE | `version create` → `publish` |
| 机器人搜不到 | 版本未发布到 RELEASE | 同上 |
| `robotStatus=UNCONFIGURED` | 还没配过机器人 | 用 `robot config` 创建 |
| `robotStatus=OFFLINE` | 机器人已停用 | 用 `robot enable` 启用 |

## 与开发者后台的对照

| **过去你要做的** | **现在一行搞定** |
| --- | --- |
| 登录后台 → 创建应用 → 填表单 | `dws dev app create --name "xxx" --yes` |
| 进应用 → 权限管理 → 勾选权限 → 提交 | `dws dev app permission add --scope-values "xxx" --yes` |
| 进应用 → 成员管理 → 添加开发者 | `dws dev app member add --user-id "xxx" --yes` |
| 进应用 → 机器人配置 → 填名称 → 保存 | `dws dev app robot config --name "xxx" --yes` |
| 进应用 → 版本管理 → 创建 → 发布 | `dws dev app version create` + `publish` |
| 下载 SDK → 写连接代码 → 启动服务 | `dws dev connect --unified-app-id <ID>` |

## 最佳实践

1. **先**`--dry-run`**再**`--yes`— 写操作先预览参数，确认无误再执行
2. **写完回读确认** — 每步操作后用`get`/`status`验证结果
3. **审批人由你选** — CLI 会列出候选审批人，你来拍板，不会自动替你选
4. **密钥注意保密** —`appSecret`/`clientSecret`是敏感信息，不要外泄
5. **查参数用 schema** —`dws schema dev.app.<method>`查看命令参数定义
6. **遇到错误查文档** — `dws dev doc search --keyword "<错误码>"` 搜索开放平台文档

## 更多资源

- **命令帮助**：`dws dev app --help`
- **参数查询**：`dws schema dev.app.<method>`（如`dws schema dev.app.robot.config`）
- **Gitee**：[DingTalk-Real-AI/dingtalk-workspace-cli](https://gitee.com/DingTalk-Real-AI/dingtalk-workspace-cli)
- **GitHub**：[DingTalk-Real-AI/dingtalk-workspace-cli](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli)
