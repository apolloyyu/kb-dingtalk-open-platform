---
title: "微应用调试工具—RC版"
source_url: "https://open.dingtalk.com/document/download/h5-debug"
namespace: "download"
slug: "h5-debug"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > 微应用调试工具 > 微应用调试工具—RC版"
doc_id: "gezGfkawwC"
updated_at: "2026-09-15 09:35:31"
---

> Source: https://open.dingtalk.com/document/download/h5-debug
> Path: 应用开发 / 开发工具 / 开发者工具 > 微应用调试工具 > 微应用调试工具—RC版
> Updated: 2026-09-15 09:35:31

# 微应用调试工具—RC版

钉钉 RC 版是钉钉开放平台推出的用于调试钉钉微应用的调试工具，你可以使用使用钉钉 RC 版调试正在开发或已开发完成的H5微应用。

> **[!IMPORTANT]**
>
> 该工具已经暂停维护，建议优先使用[微应用四端调试工具—网页版](0006-micro-application-four-terminal-debugging-tool-web-edition.md)或[vConsole](https://www.kancloud.cn/york_web/web_node_plugin_document/2232008)进行调试。

## 开发调试包下载

| 微应用 | Android/Windows | iOS/Mac |
| --- | --- | --- |
| 移动端微应用调试 | Android调试包：  <https://download.alicdn.com/wireless/dingtalk/latest/rimet_10006337.apk> | 暂无 |
| PC端微应用调试 | Windows调试包：  <https://dtapp-pub.dingtalk.com/dingtalk-desktop/win_installer/RC/DingTalk_v7.6.45-RC.250214002.exe> | 暂无 |

## Android调试工具

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，单击目标应用。
2. 单击**基础信息** > **成员管理** > **添加角色**，将开发者添加为开发者角色。
3. 下载调试安装包：[Android调试](https://download.alicdn.com/wireless/dingtalk/latest/rimet_10006337.apk)。
4. 在手机上打开H5调试开关。

   > **[!IMPORTANT]**
   >
   > 机型不同，打开调试开关的方法不同。开发者需按照对应手机的打开方式进行操作，一般是Android系统的开发者选项-USB调试。
5. 打开钉钉设置页面，选择**通用**。
6. 打开**开发者选项**页面，然后打开**微应用调试**。
7. 手机连接到电脑，打开chrome，chrome://inspect 开始调试。具体调试方法请参考[Chrome开发者工具文档](https://developers.google.com/web/tools/chrome-devtools/remote-debugging/?hl=zh-cn)。

## Windows调试工具

> **[!IMPORTANT]**
>
> 1. 开发者只能调试自己创建的应用。
> 2. 开发者已[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，单击目标应用。
2. 单击**基础信息** > **成员管理** > **添加角色**，将开发者添加为开发者角色。
3. 单击**应用能力 > 网页应用**，然后配置PC端首页地址并保存。

   > **[!IMPORTANT]**
   >
   > 需确保调试的H5微应用已配置了PC端首页地址，否则在**RC版钉钉客户端**工作台看不到该应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5155159371/p799974.png)
4. 下载调试安装包：[Windows调试包](https://dtapp-pub.dingtalk.com/dingtalk-desktop/win_installer/RC/DingTalk_v7.6.45-RC.250214002.exe)。
5. 打开钉钉工作台页面。
6. 在工作台页面，将企业切换到要调试的微应用的组织。

   ![切换组织](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6784369951/p163854.png)
7. 在微应用页面，鼠标左键点击该微应用，然后按F2，即可打开微应用调试面板。

   > **[!NOTE]**
   >
   > - 部分Windows上需先按住鼠标右键，再按下F2。
   > - 如果该应用在RC版本客户端不显示，可以尝试在钉钉RC客户端的**设置页面**中清除缓存。
