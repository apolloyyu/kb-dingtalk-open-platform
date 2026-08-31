---
title: "渠道配置"
source_url: "https://open.dingtalk.com/document/development/interconnections-channel"
namespace: "development"
slug: "interconnections-channel"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 客联配置 > 渠道配置"
doc_id: "hnsIm6ZeeC"
updated_at: "2025-09-24 20:35:07"
---

> Source: https://open.dingtalk.com/document/development/interconnections-channel
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 钉钉客联 > 客联配置 > 渠道配置
> Updated: 2025-09-24 20:35:07

# 渠道配置

## **可见性设置**

1. 点击**应用管理**，找到**第三方应用**分组，鼠标悬停在“钉钉客联”应用上，点击出现的**设置**按钮。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7037178571/p1011126.png)
2. 登录[钉钉管理后台](https://oa.dingtalk.com/)，配置“钉钉客联”应用的可见范围。支持设置为仅部分员工可见，设置完成后点击**提交**以保存更改。

   > **[!NOTE]**
   >
   > - 仅管理员和子管理员可访问钉钉管理后台。若当前账号是多个组织的管理员，请先选择需开通“钉钉客联”的目标组织。
   > - 员工在使用钉钉客联进行聊天前，管理员必须为其开启应用可见权限。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7037178571/p1011127.png)

## **新建渠道**

1. 打开钉钉客户端并进入工作台，然后在“未分组应用”中查找并点击“钉钉客联”应用。

   > **[!NOTE]**
   >
   > - 如果当前账号拥有多个组织的管理权限，请确保已切换至已开通“钉钉客联”的组织后再进入工作台。
   > - 产品开通后，默认会出现在“未分组应用”中，仅管理员有权限操作。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7037178571/p1011124.png)
2. 在左侧导航栏点击**渠道配置**，进入配置页面后，点击**新建渠道**按钮。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7037178571/p1011125.png)

   - **渠道名称**：开发者自定义名称，用于区分不同的对接场景。
   - **渠道类型**：

     - **微信小程序**：专用于微信小程序接入场景，请仅在此类情况下选择。
     - **APP**：适用于除微信小程序外的所有其他场景，包括Web端、企业自有App、抖音小程序、Microsoft Teams等。
   - **页面类型**：两种类型的会话页面布局和样式不同。

     - **移动端**：适用于微信小程序、公众号、自有App等移动端环境。
     - **PC端**：适用于Web端、桌面应用等电脑端环境。
     - **（选填）群二维码**：用于外部用户通过扫描二维码加入群聊的场景。扫码后将跳转至对应群会话页面；若用户尚未入群，则自动加入。

       - 当渠道类型为“微信小程序”时，系统将自动生成跳转链接，需将该链接添加至微信小程序管理后台的业务域名白名单中，否则，微信扫码无法跳转。
       - 当渠道类型为自建APP，需要客户开发者主动生成一个地址并填入，用于APP扫码识别。
3. 填写完成后，点击 **保存并配置页面 ，**会进入下一项 **页面配置**。
4. 填写完基本信息后，点击**保存**并配置页面，系统将跳转至页面配置界面，直接**保存**并返回即可。

   > **[!NOTE]**
   >
   > - 此步骤可暂时忽略跳过，更多信息可参考[页面配置](1843-interconnections-page.md#8a3623d30eunh)。
   > - 通过页面配置，可实现页面UI风格自定义。
   > - 通过设置自定义扩展点，可实现H5与业务应用之间的跳转。
5. 返回到渠道列表页面，点击复制渠道Code（ChannelCode）并保存。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7037178571/p1011123.png)
