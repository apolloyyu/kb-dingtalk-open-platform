---
title: "本地安装OpenClaw"
source_url: "https://open.dingtalk.com/document/development/install-openclaw-locally"
namespace: "development"
slug: "install-openclaw-locally"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "高级集成 > OpenClaw 常用部署方式 > 本地安装 OpenClaw"
doc_id: "extDn0AnNy"
updated_at: "2026-07-14 09:22:36"
---

> Source: https://open.dingtalk.com/document/development/install-openclaw-locally
> Path: 应用开发 / 钉钉CLI / 高级集成 > OpenClaw 常用部署方式 > 本地安装 OpenClaw
> Updated: 2026-07-14 09:22:36

# 本地安装OpenClaw

## **前提条件**

- 已经完成了钉钉应用和机器人的创建与发布。
- 已经获取了钉钉应用的Client ID和Client Secret，用于后续使用。
- 通过快捷方式创建的OpenClaw机器人已自动获得`Card.Streaming.Write`、`Card.Instance.Write`和`qyapi_robot_sendmsg`权限点。
- 已经安装了[Node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)，版本最低v22.22.0。
- 已经正确安装了[Git](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)工具

如果你不想安装，可以直接使用阿里云的[Openclaw 一键部署 (原 Clawdbot)](https://www.aliyun.com/activity/ecs/clawdbot?userCode=oq2t54oi)，部署之后可以直接跳到[对接钉钉](https://developer.aliyun.com/article/1709772#%E5%AF%B9%E6%8E%A5%E9%92%89%E9%92%89)。

> **[!IMPORTANT]**
>
> 在本地安装OpenClaw部署方式，仅支持MAC系统安装，暂不支持WIndows系统。

## **步骤一：安装 OpenClaw**

### **安装****服务**

1. 使用官方脚本安装：

   ```
   curl -fsSL https://openclaw.bot/install.sh | bash
   ```

   服务器在国内，如果安装失败的话，可能需要解决网络问题。

   其他平台安装方式请参考[Openclaw 安装文档 (原 Clawdbot)](https://docs.openclaw.ai/install)。

   执行上面脚本后，你会看到如下图输出：

   > **[!NOTE]**
   >
   > 如果是首次安装，时间会很长，请耐心等待。

   ![OpenClaw 钉钉教程 - 安装过程初始化界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055526.webp)

   如果最后输出如下内容：

   ```
   → npm install failed; cleaning up and retrying...
   ```

   > **[!IMPORTANT]**
   >
   > 新的脚本服务器内存要求比较高，如果出错的话，建议使用 `swap` 把硬盘空间当作交互内存使用。

   成功之后，输出如下图片：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055527.png)
2. 第一个选项选择 `yes`，就是询问是否知道风险。
3. 第二步选择 `QuickStart`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055528.png)
4. 第三步选择模型服务商，选择 `Qwen`，免费额度充足，适合入门使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055529.png)
5. 选择千问模型后，会提供一个链接，复制并在浏览器中打开，如下图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055530.png)

   打开浏览器后，会看到如下界面。由于我已登录过，所以显示账户信息；如果尚未登录，按照提示完成登录即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055531.png)
6. 登录完成后，会出现以下选项，提示选择对应的千问模型，如下图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055532.png)
7. 选择默认模型即可。接下来会提示选择 channel，可以先选择`Skip for now`，后续再添加。

   ![369590c940c522343ffec348c912f372](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3658162771/p1056753.png)
8. 选择 skills，选择 `No`，如下图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055536.png)
9. 继续下面选择 hooks，使用`空格`选择 `Skip for now`，如下图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055537.png)
10. 等待安装完成，最后出现以下选项，这里选择 `TUI`：

    ![OpenClaw 钉钉教程 - 选择 TUI 终端界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055538.webp)

    如果看到 TUI聊天界面，说明安装成功，可以尝试输入`Hello` 进行测试。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055539.png)
11. 然后使用 `ctrl+c` 先关闭，后续可以再设置。

### **查看服务**

使用下方命令查看：

```
openclaw status
```

服务启动成功后，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055540.png)

### **访问 Web UI 面板**

在浏览器打开 `http://127.0.0.1:18789/`, 你会看到 Dashboard 了，如下图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055541.png)

图中显示的是未授权状态，回到服务器，输入以下命令：

```
openclaw dashboard
```

执行后，会看到下方的面板数据：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055542.png)

复制对应的 `Dashboard URL` 到浏览器打开，即可正常查看聊天记录。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055544.png)

恭喜你，至此 Openclaw (原 Clawdbot) 已安装完成，可以正常访问了。

聊天框里面首次输入`Hello`, `Clawdbot`会询问你他应该叫什么，应该叫你什么。就是你需要给它设置名字，还有 bot该叫你什么。此时可以在聊天框中输入以下内容：

```
Name: Openclaw

My Name: Boss
```

## **步骤二：OpenClaw和钉钉机器人打通**

### **安装钉钉插件**

首先安装钉钉官方插件，输入以下命令直接运行 OpenClaw 插件安装命令，OpenClaw 会自动处理下载、安装依赖和注册。

> **[!NOTE]**
>
> 时间有可能比较久，请耐心等待即可。

```
openclaw plugins install @dingtalk-real-ai/dingtalk-connector
```

效果如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055546.png)

### **在** OpenClaw **中添加钉钉配置**

#### **方式一：**在 `~/.openclaw/openclaw.json` 中添加配置

完成上方步骤后，你需要在 `~/.openclaw/openclaw.json` 文件中添加`channels/dingtalk-connector`、`gateway/auth` 和 `gateway/http/endpoints`3 个配置项属性：

> **[!NOTE]**
>
> 下方已省略其他配置项，只提供了核心配置项及需要配置钉钉的相关属性内容。

通过终端应用，在终端中输入执行 `vim ~/.openclaw/openclaw.json`进入文件编辑：

```
{
  "channels": {
    "dingtalk-connector": {
      "clientId": "钉钉应用的Client Secret",       // 必选：填入上方的 钉钉 Client ID
      "clientSecret": "钉钉应用的Client Secret", // 必选：填入上方的 Client Secret
      "gatewayToken": "Gateway 认证 token",  // 必选：Gateway 认证 token, openclaw.json配置中 gateway.auth.token 的值 
      "gatewayPassword": "",              // 可选：Gateway 认证 password（与 token 二选一）
      "sessionTimeout": 1800000           // 可选：会话超时(ms)，默认 30 分钟
    }
  },
  "gateway": { // gateway通常是已有的节点，配置时注意把http部分追加到已有节点下
    "auth": {
      "mode": "token",
      "token": "Gateway 认证 token" // 必选：一般是安装时默认就有
    },
    "http": {
      "endpoints": {
        "chatCompletions": {
          "enabled": true // 必选
        }
      }
    }
  }
}
```

#### **方式二：本地AI工具自动配置**

通过本地的AI工具（本示例以Qoder IDE为例），帮助完成配置。在Qoder IDE中输入下方文本内容：

*我现在想使用openclaw对接钉钉，请按照我下方的json配置和注释，在我的~/.openclaw/openclaw.json 中添加下方“channels/dingtalk-connector、gateway/auth 和 gateway/http/endpoints”3 个配置属性，不要改动其他属性。并最后帮我展示整个openclaw.json文件，让我可以人工修改查验相关内容。相关json配置和注释如下：*`... ... 这是一处 json 数据占位。需要提前修改方式一中的 json 配置信息，修改clientId和clientSecret后，复制放到这里 ... ...`*。*

案例如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3658162771/p1056780.png)

工具执行效果如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3658162771/p1056781.png)

#### **重启 Gateway**

执行以下命令：

```
openclaw gateway restart
```

重启需等待一段时间，直至出现“Restarted LaunchAgent: gui/502/ai.openclaw.gateway”提示，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055553.png)

验证：

```
openclaw plugins list  # 确认 dingtalk-connector 已加载
```

## **常见问题**

- **Q：出现 405 错误**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055554.png)

  需要在 `~/.openclaw/openclaw.json` 中启用 chatCompletions 端点：

  ```
  {
    "gateway": { // gateway通常是已有的节点，配置时注意把http部分追加到已有节点下
      "http": {
        "endpoints": {
          "chatCompletions": {
            "enabled": true
          }
        }
      }
    }
  }
  ```

  mac 电脑上执行 `vim ~/.openclaw/openclaw.json`，进行修改。修改完成后，执行 openclaw gateway restart
- **Q：出现 401 错误**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055555.png)

  检查 `~/.openclaw/openclaw.json` 中的gateway.auth鉴权的 token/password 是否正确：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1474622771/p1055557.png)
- **Q：钉钉机器人无响应**

  - 确认 Gateway 正在运行：`curl http://127.0.0.1:18789/health`
  - 确认机器人配置为 **Stream 模式**（非 Webhook）
  - 确认 AppKey/AppSecret 正确
- **Q：AI Card 不显示，只有纯文本**

  需要开通权限 `Card.Streaming.Write` 和 `Card.Instance.Write`，并重新发布应用。
- **Q：升级后出现插件加载异常或配置不生效**

  由于官方两次更名（Clawdbot → Moltbot → OpenClaw），旧版本（0.4.0 以下）的 connector 插件可能与新版本不兼容。建议按以下步骤处理：

  1. 先检查 `~/.openclaw/openclaw.json`（或旧版的 `~/.clawdbot/clawdbot.json`、`~/.moltbot/moltbot.json`），如果其中存在 dingtalk 相关的 JSON 节点（如 `channels.dingtalk`、`plugins.entries.dingtalk` 等），请将这些节点全部删除。
  2. 然后清除旧插件并重新安装：

  ```
  rm -rf ~/.clawdbot/extensions/dingtalk-connector
  rm -rf ~/.moltbot/extensions/dingtalk-connector
  rm -rf ~/.openclaw/extensions/dingtalk-connector
  openclaw plugins install @dingtalk-real-ai/dingtalk-connector
  ```
- **Q：图片不显示**

  1. 确认 `enableMediaUpload: true`（默认开启）
  2. 检查日志 `[DingTalk][Media]` 相关输出
  3. 确认钉钉应用有图片上传权限
