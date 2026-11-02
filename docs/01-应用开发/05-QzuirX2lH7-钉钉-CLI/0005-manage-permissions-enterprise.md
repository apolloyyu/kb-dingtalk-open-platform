---
title: "如何单独管理企业自建Agent的权限"
source_url: "https://open.dingtalk.com/document/development/manage-permissions-enterprise"
namespace: "development"
slug: "manage-permissions-enterprise"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "新手入门 > 权限管理 > 如何单独管理企业自建Agent的权限"
doc_id: "Z6AOhsjLM9"
updated_at: "2026-11-02 15:22:45"
---

> Source: https://open.dingtalk.com/document/development/manage-permissions-enterprise
> Path: 应用开发 / 钉钉 CLI / 新手入门 > 权限管理 > 如何单独管理企业自建Agent的权限
> Updated: 2026-11-02 15:22:45

# 如何单独管理企业自建Agent的权限

本文介绍了企业管理员如何单独管理企业自建Agent的DWS CLI权限。

## **说明**

本文面向企业管理员，介绍如何在钉钉开发者后台的 CLI 设置（Agent 管理）中，添加企业自建 Agent，为企业自建 Agent 调用 DWS CLI 能力建立可信身份与管控基础，实现单独管理企业自建Agent的DWS CLI权限。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0695423971/p1109322.png)

## **接入前准备**

### **配置与安装**

开始添加前，请确认以下事项：

- **应用已发布**：企业内部应用必须在开发者平台完成发布，未发布的应用不可用于本流程；
- **已取得应用凭证**：已创建企业内部应用，并取得应用的 `clientId` 与 `clientSecret`；

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0695423971/p1109323.png)
- **已配置应用安全设置重定向地址**：在应用安全设置中配置以下重定向地址：`http://127.0.0.1,https://login.dingtalk.com`；

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0695423971/p1109324.png)
- **DWS CLI 已安装**：已安装并可正常执行命令。

### **凭证安全要求**

- `clientSecret` 仅应由应用负责人或管理员通过可信渠道提供。
- 不要在文档、群聊、代码仓库、日志或截图中明文保存和传播 `clientSecret`。
- 不要将真实凭证写入示例命令或接入文档。

## 企业自建应用接入Agent管理

1. 访问[钉钉开发者后台](https://open-dev.dingtalk.com/fe/old?hash=%23%2FdeveloperSettings#/developerSettings)。
2. 依次选择导航栏**更多**> **基本信息** > 左侧 **CLI 设置**，找到**Agent 管理**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0695423971/p1109326.png)
3. 在**Agent 管理**卡片点击**添加**按钮，按页面提示选择企业自建应用 / Agent 进行添加。

   > **[!NOTE]**
   >
   > 添加前请再次确认：
   >
   > - 应用已经发布。
   > - 应用安全设置中已配置 `http://127.0.0.1,https://login.dingtalk.com`。
   > - 填写的应用身份与后续登录时使用的 `clientId` 一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0695423971/p1109327.png)

## **添加后的渠道管控**

添加成功后，企业自建 Agent 会作为独立渠道出现在「Agent 管理」列表中，管理员可对其进行与千问办公等单独渠道一致的管控：

- **启用开关**：控制该自建 Agent 渠道的 DWS CLI 能力是否可用；
- **生效范围**：支持全员可用，或按部门、角色圈选人员范围；
- **权限范围管控**：支持按业务分类限定该渠道能用到哪些权限项。

未通过本流程添加、成员以个人身份直接使用 CLI 登录的渠道，统一归入「其他渠道」进行管控。

## **使用企业自建应用 / Agent登录**

需要进行管控的自建应用 / Agent，主要区别在于登录时是否指定应用：

- 未指定应用：按 DWS CLI 默认方式登录，管控归入「其他渠道」；
- 指定企业自建应用：登录身份按该应用的 `clientId` 绑定，管理员可对该渠道单独设置 DWS 生效范围与人员范围。

### **默认应用 / Agent 登录**

不指定企业自建应用时，按 DWS CLI 默认登录流程完成认证。

```
dws auth login
```

### **指定企业自建应用 / Agent 登录**

OAuth 登录：适用于本机可正常打开浏览器并完成授权的环境，执行后按终端提示在浏览器中完成授权。

```
dws auth login --client-id <clientId> --client-secret <clientSecret>
```

设备码模式：适用于服务器、远程终端或其他无法直接打开浏览器的环境，执行后按终端提示，在可访问浏览器的设备上完成设备码认证。

```
dws auth login --client-id <clientId> --client-secret <clientSecret> --device
```

渠道身份由登录时的 `clientId` 识别，只需在登录时传一次，后续命令无需重复传参，也无需配置其他渠道类参数。

## **更改事件订阅方式**

企业自建 Agent 完成添加后，原Agent中的事件订阅监听需要进行企业自建应用的适配。

**示例：监听别人 @ 当前用户的消息**

自建应用事件监听需增加 `--stream-ticket-mode custom`

```
dws event consume user_im_message_receive_at \
  --stream-ticket-mode custom \
  --profile '<corpId>:<userId>' \
  --flatten \
  --duration 30m
```

## **常见问题（FAQ）**

- **Q1：添加时找不到目标应用？**

  确认该应用为本组织的企业内部应用且已发布；未发布的应用不会出现在可添加列表中。
- **Q2：添加成功但成员无法使用？**

  按顺序检查：① 该自建 Agent 渠道的启用开关是否开启 → ② 生效范围是否包含该成员 → ③ CLI 管控配置中对应权限项的可用范围是否包含该成员。
- **Q3：可以添加多个自建 Agent 吗？**

  可以。每个自建应用作为独立渠道单独管控，人员范围与权限范围互相独立。
- **Q4：添加企业自建应用后，未收到事件订阅**

  自建应用事件监听需增加 `--stream-ticket-mode custom`
