---
title: "深度集成：OpenClaw调用钉钉MCP"
source_url: "https://open.dingtalk.com/document/development/openclaw-invokes-dingtalk-mcp"
namespace: "development"
slug: "openclaw-invokes-dingtalk-mcp"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "高级集成 > OpenClaw 框架集成 > 深度集成：OpenClaw调用钉钉MCP"
doc_id: "228Sw1pcmx"
updated_at: "2026-07-24 09:14:15"
---

> Source: https://open.dingtalk.com/document/development/openclaw-invokes-dingtalk-mcp
> Path: 应用开发 / 钉钉CLI / 高级集成 > OpenClaw 框架集成 > 深度集成：OpenClaw调用钉钉MCP
> Updated: 2026-07-24 09:14:15

# 深度集成：OpenClaw调用钉钉MCP

您可以通过接入钉钉 MCP，让 OpenClaw 获得钉钉的操作能力，比如日程预约、AI表格操作等。接入后，OpenClaw 会在对话中自动调用对应的钉钉服务。

## **钉钉提供哪些MCP 服务**

MCP 服务广场是钉钉“AI 能力中心”的对外服务门户，其中包含100+精选和众多钉钉官方MCP能力，覆盖从基础办公到垂直行业全场景的MCP服务生态，提供**标准化、即插即用的 AI 能力集合**。 支持开发者低成本集成，快速构建智能客服、自动化流程、行业解决方案等应用。

可点击链接[访问 MCP 广场](https://mcp.dingtalk.com/#/)。

## **如何获取钉钉MCP服务**

### **步骤 1：访问钉钉 MCP 广场**

打开浏览器，访问：<https://mcp.dingtalk.com>

### **步骤 2：登录钉钉账号**

点击页面右上角「登录」，使用企业管理员或具备权限的钉钉账号登录。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055502.png)

### **步骤 3：选择企业**

在顶部切换到需要操作的企业。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055503.png)

### **步骤 4：查找MCP 服务**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055505.png)

### **步骤 5：获取 MCP 服务 URL**

点击进入指定MCP，如钉钉AI表格，在页面右侧点击获取MCP Server服务配置，并点击复制获取MCP Server URL。

**示例如下**：

```
https://mcp-gw.dingtalk.com/server/xxxxxxxxxxxxxxxx?key=yyyyyyyy
```

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055506.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055507.png)

## **钉钉MCP集成到OpenClaw**

### **方式一：**OpenClaw自动安装

将获取的MCP Server URL直接输入给OpenClaw ，OpenClaw会自动安装。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055508.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055509.png)

### **方式二：手动安装mcporter**

#### **情形一：本地安装的OpenClaw安装****mcporter CLI**

1. 打开电脑本地终端。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055510.png)
2. 复制下方命令行，并点击Enter执行。

   ```
   npm install -g mcporter
   ```

   出现下方结果，表示安装成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055511.png)
3. 验证mcporter安装是否成功，终端输入以下命令。

   ```
   mcporter --version
   ```

   出现如图所示结果，即表示安装成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055515.png)

#### **情形二：云服务器安装的****OpenClaw安装****mcporter CLI**

1. 登录云服务器的命令行，复制下方命令行，并点击Enter执行。

   ```
   npm install -g mcporter
   ```

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055517.png)
2. 输入以下命令验证安装结果。

   ```
   mcporter --version
   ```

   出现对应版本号即表示安装成功，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9374622771/p1055519.png)

## **添加钉钉MCP服务（手动安装）**

添加 MCP 服务

```
# 添加MCP服务
mcporter config add dingtalk-contacts --url "<你的MCP Server URL>"
```

**示例**：

```
# 添加钉钉通讯录
mcporter config add dingtalk-contacts --url "https://mcp-gw.dingtalk.com/server/3c8fe1xxxxf4e2fxxxxx?key=xxxxx"

# 添加钉钉日历
mcporter config add dingtalk-calendar --url "https://mcp-gw.dingtalk.com/server/e4e22xxxxfcaa4exxxxx?key=xxxxx"
```

**验证配置**：

```
# 查看已配置的服务
mcporter config list

# 查看某个服务的可用工具
mcporter call dingtalk-contacts list_tools --output json
mcporter call dingtalk-calendar list_tools --output json
```

## **OpenClaw使用钉钉MCP**

### **方式一：直接对话使用**

> **[!NOTE]**
>
> 对话中涉及到的MCP能力，需要提前配置，才可以正常运行。

在 OpenClaw 对话中直接告诉我你的需求，例如：

- "帮我查一下张三的user\_id"
- "预订一间明天下午3点的会议室"
- "帮我创建一个明天上午10点的会议，邀请张三和李四"

### **方式二：在代码/脚本中调用**

```
import subprocess
import json

def call_dingtalk_mcp(server, tool, args):
    """调用钉钉 MCP"""
    cmd = ["mcporter", "call", server, tool, "--args", json.dumps(args), "--output", "json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

# 调用示例：搜索成员
result = call_dingtalk_mcp(
    "dingtalk-contacts",
    "search_user_by_key_word",
    {"keyWord": "张三"}
)
print(result)
```

## **场景示例：钉钉日程管理**

本场景同时使用「钉钉通讯录」和「钉钉日历」两个 MCP 服务，完成创建会议、邀请参与人、预订会议室的完整流程。

### **通讯录 MCP - 可用工具**

| **工具名** | **功能** |
| --- | --- |
| search\_user\_by\_key\_word | 按照关键词搜索成员user\_id |
| get\_user\_info\_by\_user\_ids | 获取用户详情 |
| get\_sub\_depts\_by\_dept\_id | 获取子部门列表 |
| get\_dept\_user\_list | 获取部门成员列表 |
| get\_current\_user\_profile | 获取当前登录用户的基本信息（姓名、工号、手机号、组织信息、所属部门、角色等） |
| search\_user\_by\_mobile | 通过手机号搜索用户名称和 userId |
| search\_dept\_by\_keyword | 根据关键词模糊搜索部门 |
| get\_dept\_members\_by\_deptId | 获取指定部门下的所有成员（userId 和显示名称） |

### **日历 MCP - 可用工具**

| **工具名** | **功能** |
| --- | --- |
| create\_calendar\_event | 创建日程 |
| list\_calendar\_events | 查询日程列表 |
| update\_calendar\_event | 更新日程 |
| delete\_calendar\_event | 删除日程 |
| query\_busy\_status | 查询闲忙状态 |
| query\_available\_meeting\_room | 查询空闲会议室 |
| add\_meeting\_room | 预订会议室 |
| add\_calendar\_participant | 添加参与人 |
| remove\_calendar\_participant | 移除参与人 |

### **使用示例**

在 OpenClaw 对话中或者通过钉钉机器人直接告诉我你的需求，例如：

- "帮我创建一个明天上午10点的会议，邀请张三和李四"
- "预订一间明天下午3点的会议室"

## **常见问题**

- **Q1：mcporter 命令找不到？**

  ```
  # 检查安装位置
  which mcporter

  # 重新安装
  npm uninstall -g mcporter && npm install -g mcporter
  ```
- **Q2：MCP URL 失效？**

  钉钉 MCP URL 可以被重置，访问 <https://mcp.dingtalk.com>可以检查。

## **相关资源**

- 钉钉 MCP 广场：<https://mcp.dingtalk.com>
- mcporter GitHub：<https://github.com/steipete/mcporter>
