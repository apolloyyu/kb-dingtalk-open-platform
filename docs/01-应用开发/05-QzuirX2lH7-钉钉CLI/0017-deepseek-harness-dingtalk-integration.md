---
title: "DeepSeek Harness 钉钉插件"
source_url: "https://open.dingtalk.com/document/development/deepseek-harness-dingtalk-integration"
namespace: "development"
slug: "deepseek-harness-dingtalk-integration"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "高级集成 > DeepSeek Harness 框架集成 > DeepSeek Harness 钉钉插件"
doc_id: "p0HW4DFjSl"
updated_at: "2026-08-25 17:54:50"
---

> Source: https://open.dingtalk.com/document/development/deepseek-harness-dingtalk-integration
> Path: 应用开发 / 钉钉CLI / 高级集成 > DeepSeek Harness 框架集成 > DeepSeek Harness 钉钉插件
> Updated: 2026-08-25 17:54:50

# DeepSeek Harness 钉钉插件

## 场景介绍

**离开电脑，也能在钉钉里让 DeepSeek Harness（DSH）继续工作。**

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)可以在电脑上执行编码、测试和排障任务。钉钉连接器通过 Stream 长连接将本机 DSH Web Agent 接入钉钉，无需暴露公网回调地址。

接入后，你可以在钉钉私聊或允许的群聊中发起任务、查看回复、补充信息，并处理 Agent 提问、Plan Review 和敏感操作审批。开启可选的 DWS 能力后，DSH 还可调用钉钉日历、群聊、待办等工具。

| image | image | image |
| --- | --- | --- |
| image | image | image |

> **[!NOTE]**
>
> DeepSeek Harness 钉钉插件由 DingTalk Real AI 公开维护，不是 DeepSeek 官方组件。本文中的“连接器”和“插件”均指 npm 包 `@dingtalk-real-ai/dsh-dingtalk`。

## 连接器能力

| **能力类别** | **具体能力** |
| --- | --- |
| 消息接入 | ✅通过 Stream 长连接接收钉钉私聊和按策略允许的群聊，无需暴露公网回调地址。  ✅支持 AI Card 流式回复；不可用时降级为 Markdown 或文本。 |
| 任务与会话 | ✅持久化 DSH session，重启后可继续会话。  ✅支持模型切换、工作区切换、取消任务和消息排队。 |
| 人机协同 | ✅承接 DSH 原生用户提问和 Plan Review。  ✅敏感操作采用 fail-closed 审批；未确认、无效确认或非管理员操作均不会放行。 |
| 身份与访问范围 | ✅通过一次性口令绑定唯一管理员。  ✅可按发送者和群聊分别配置全部允许、禁止或白名单；群聊会话按成员隔离。 |
| 多机器人 | ✅单个 `dsh web` 可同时连接多个钉钉机器人。  ✅每个机器人使用独立凭据、Stream 连接、管理员绑定和运行状态。 |
| 图片输入 | ✅支持纯图片及图片文字混排的 `richText` 输入。  ✅提供 `auto`、`always`、`never` 三种模式；模型适配器和实际网关仍须支持图片。 |
| 钉钉工具 | ✅可选挂载 DWS 工具和随包提供的 DWS skill。  ✅DWS 未安装或未登录时，普通钉钉消息能力仍可使用。 |
| 诊断 | ✅提供联网诊断 `doctor` 和不发起网络请求的 `doctor --offline`。 |

> **[!NOTE]**
>
> 第一版只支持 DSH `web` profile。macOS 和 Linux 为正式支持平台，Windows 为实验性平台。

## 从 0 安装钉钉连接器

### 步骤一：运行安装向导

在终端运行：

```
npx @dingtalk-real-ai/dsh-dingtalk@latest setup
```

1. 检测是否安装 DeepSeek Harness ，未安装可一键安装。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097199.png)
2. 已安装则自动完成 钉钉连接器 的下载安装，进入下一步。

   > **[!NOTE]**
   >
   > 当前会自动检测Node.js 版本，安装连接器时要求 Node.js 版本须满足 `22.19.0` || `>=24.0.0`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097200.png)

`npx` 会为本次执行下载并运行 CLI，但不会把 `dsh-dingtalk` 写入 shell 的 PATH。以后重新配置或运行诊断时，仍需使用完整的 `npx` 命令。

向导会检查运行环境，并将当前精确版本的连接器安装到 DSH `web` profile。若检查未通过，请根据终端提示处理后重新运行。

### 步骤二：扫码创建钉钉应用

1. 插件安装完成后，需要有机器人来作为渠道进行收发消息。首次安装时，向导提供两种接入方式：

   - **扫码创建应用（推荐）**：终端显示二维码后，用手机钉钉扫码并按页面提示完成创建。
   - **填写已有凭据**：手动输入已有应用的 Client ID 和 Client Secret（已有应用需要有相关卡片、消息等权限）。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097203.png)
2. 手机钉钉会打开机器人创建页，确认组织、机器人名称和简介后，点击**创建**。

   | image | image |
   | --- | --- |
3. 创建完成后，页面会显示 Client ID 和 Client Secret，无需复制，已经自动写入到本地中。

   > **[!NOTE]**
   >
   > 请妥善保存，切勿发送到聊天、文档或 Issue。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097205.png)
4. 向导会将凭据写入 `$DSH_HOME/.credentials.yaml`。

   > **[!NOTE]**
   >
   > - 未自定义 `DSH_HOME` 时，默认路径为 `~/.dsh/.credentials.yaml`。
   > - Client Secret 不会在配置菜单或诊断结果中回显。

### 步骤三：配置 DWS、图片和访问范围

向导会继续配置以下能力：

| **配置项** | **可选项** | **建议** |
| --- | --- | --- |
| DWS 工具 | - **y**：启用 - **n**：不启用 | 按需开启；普通消息不依赖 DWS。 |
| 图片处理 | - **Auto**（推荐）：按当前 DSH 模型能力判断。 - **Always**：跳过连接器检查。 - **Never**：禁用图片输入。   **[!NOTE]**   - 图片模式只控制连接器是否接收图片，不能把纯文本模型变成视觉模型。 - 只有模型适配器和实际网关均支持图片时，图片任务才能成功. - 不要仅使用 `always` 强行绕过检查。 | 优先使用 `Auto`。 |
| 发送者范围 | - 所有人（默认并推荐） - 仅管理员 - 仅指定 sender staffId | 测试机器人可使用默认值；公司账号或真实项目建议仅管理员或指定成员。 |
| 群聊范围 | - 所有群（默认并推荐） - 禁止群聊 - 仅指定群 openConversationId | 按最小必要范围开放。 |

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9186367871/p1096969.png)

运行时可查看下图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097207.png)

> **[!NOTE]**
>
> - 首次安装默认允许所有发送者和所有群聊。
> - 若机器人用于公司账号或真实项目，建议改为仅管理员或指定成员，并限制可响应的群聊。

若开启 DWS，向导会检查 DWS CLI 和登录状态。DWS 未登录时，可稍后在本机执行：

```
dws auth login
```

### 步骤四：启动 DSH Web

配置完成后，向导会询问是否立即启动 `dsh web`。启动后，请等待日志出现 `connect success` 和 `stream connected`：

![DSH Web 启动并连接钉钉机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286367871/p1096980.png)

如果选择稍后启动，可以手动运行：

```
dsh web
```

> **[!NOTE]**
>
> 运行期间需保持该进程和电脑网络在线，进程停止、电脑休眠或网络中断后，机器人会暂时离线，不会在云端继续执行任务。需要停止时，在运行 `dsh web` 的终端按 `Ctrl+C`。

### 步骤五：绑定唯一管理员

安装向导会为尚未绑定的机器人生成一次性命令：

```
/bind <一次性口令>
```

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097210.png)

在十分钟内使用管理员账号**私聊**机器人发送完整命令。

> **[!IMPORTANT]**
>
> 切勿将绑定命令发到群聊。

![在机器人私聊中完成管理员绑定](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1096985.png)

收到绑定成功回执后，该账号成为机器人的唯一管理员。聊天访问范围与敏感审批权限相互独立：即使允许其他成员使用机器人，敏感操作仍只接受绑定管理员审批；未回答、无效回复和非管理员回复均不会放行。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1097214.png)

## 验证安装是否成功

在钉钉中私聊机器人发送一条测试消息，例如：

```
你好，你是谁？
```

如果机器人通过 AI Card、Markdown 或文本返回结果，说明钉钉 Stream、DSH 会话和模型链路已经打通。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0961567871/p1096987.png)

完整验收应同时满足：

- 日志出现 `connect success` 和 `stream connected`；
- 管理员绑定成功；
- 真实测试消息得到回复。

也可以用 `doctor` 一次性自动检查以上各项，诊断会按机器人分别检查凭据、运行状态、管理员绑定和卡片能力：

```
# 联网验证钉钉凭据和本机运行状态
npx @dingtalk-real-ai/dsh-dingtalk@latest doctor

# 仅检查本地配置，不发起网络请求
npx @dingtalk-real-ai/dsh-dingtalk@latest doctor --offline
```

若出现警告或失败，请先按提示处理，再重新发送真实测试消息。

## 日常使用与重新配置

### 在指定工作区执行任务

机器人默认在连接器配置的工作区执行任务。如果项目位于其他目录，可以先在对应钉钉会话发送：

```
/cd /absolute/path/to/project
```

> **[!NOTE]**
>
> - 收到"新任务在该目录执行"后，再发送实际任务。
> - 把文件放入目录不会触发后台扫描或自动执行。
> - 只有你主动发送的消息会开始任务。

恢复默认工作区：

```
/cd reset
```

### 重新打开配置菜单

重复执行 `setup` 不会重置连接器，只会重新打开配置菜单：

```
npx @dingtalk-real-ai/dsh-dingtalk@latest setup
```

配置菜单支持：

- 新增钉钉机器人；
- 修改指定机器人的应用凭据；
- 修改 DWS、图片和访问范围；
- 查看或重新生成管理员绑定口令；
- 运行只读诊断。

单个 `dsh web` 可以连接多个机器人。各机器人的应用凭据、Stream 连接、管理员绑定、会话映射和消息去重状态互相隔离。

## 常见问题

- **如何升级连接器版本**

  先用`npm view @dingtalk-real-ai/dsh-dingtalk version`确认 npm 已发布目标版本，再重新运行`npx @dingtalk-real-ai/dsh-dingtalk@latest setup`。升级后重启`dsh web`，确认日志重新建立 Stream 连接，再发送一条真实测试消息。
- **Node.js 版本不受支持**

  当前当前版本须满足 `22.19.0 || >=24.0.0`。升级后重新执行 `setup`。向导会在修改插件配置前停止，可直接重试。
- **执行过** `npx`**，但终端提示** `dsh-dingtalk: command not found`

  `npx` 只运行本次下载的 CLI，不会创建永久命令。请继续使用完整的 `npx @dingtalk-real-ai/dsh-dingtalk@latest ...` 命令。
- **机器人突然离线或不再回复**

  检查 `dsh web` 是否仍在运行，以及电脑是否休眠或断网。恢复后重新启动 `dsh web`，确认出现 `connect success` 和 `stream connected`，再发送真实测试消息。
- **绑定口令提示无效或已过期**

  口令仅十分钟有效，并且必须由预期管理员在机器人私聊中发送。使用兼容版本重新运行 `setup` 生成新口令；若当前 npm 版本仍受步骤一的兼容问题影响，请等待更新，不要手动修改凭据文件。
- `doctor` **提示凭据文件包含无效条目** `version`

  这是连接器 `0.5.0` 与 DSH v1 凭据格式的已知兼容问题。不要手动修改或复制 Client Secret；先检查 npm 版本。若仍为 `0.5.0`，请跳过 `doctor`，通过 Stream 日志、管理员绑定和真实消息回复验证主链路。
- **普通聊天正常，但日历、群聊或待办工具不可用**

  DWS 默认关闭，或本机 DWS CLI 尚未安装、未登录。使用兼容版本重新运行 `setup` 开启 DWS，并在本机执行 `dws auth login`。DWS 状态不会影响普通消息链路。
- **发送图片后提示模型不支持**

  DWS 默认关闭，或本机 DWS CLI 尚未安装、未登录。使用兼容版本重新运行 `setup` 开启 DWS，并在本机执行 `dws auth login`。DWS 状态不会影响普通消息链路。
- **群成员可以聊天，但无法批准敏感操作**

  聊天访问范围和敏感审批权限是两套独立控制。敏感审批只接受绑定管理员；群成员在群聊中触发的请求应由管理员在同一群处理，普通成员私聊触发的敏感操作会直接拒绝。
- **Windows 上出现兼容性问题**

  第一版把 Windows 标记为实验性平台，正式支持平台为 macOS 和 Linux。请通过 GitHub Issue 反馈系统版本、Node.js 版本、DSH 版本、连接器版本、不含凭据的日志和复现步骤。

## 支持与反馈

- 项目源码：[DingTalk-Real-AI/dsh-dingtalk](https://github.com/DingTalk-Real-AI/dsh-dingtalk)
- 问题反馈：[GitHub Issues](https://github.com/DingTalk-Real-AI/dsh-dingtalk/issues)
- DeepSeek Harness：[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

> **[!IMPORTANT]**
>
> 请使用 GitHub Private vulnerability reporting，不要在公开 Issue 中提交 Client Secret、二维码、绑定口令、用户消息或其他敏感数据。
