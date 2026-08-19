---
title: "打开钉钉投屏"
source_url: "https://open.dingtalk.com/document/development/open-dingtalk-screen"
namespace: "development"
slug: "open-dingtalk-screen"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开钉钉投屏"
doc_id: "IZp5NhRr2O"
updated_at: "2026-01-23 10:07:04"
---

> Source: https://open.dingtalk.com/document/development/open-dingtalk-screen
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开钉钉投屏
> Updated: 2026-01-23 10:07:04

# 打开钉钉投屏

本协议用于通过AppLink方式启动钉钉投屏功能，适用于支持该协议的客户端版本。 调用时即使无自定义字段，也须遵循标准AppLink结构规范。

## **使用场景**

当开发者希望在自有应用或网页中集成“一键启动钉钉投屏”功能时，可通过以下AppLink协议唤起钉钉客户端，并自动进入投屏准备状态。该能力主要适用于企业内部应用，在会议协作、远程演示、培训分享等需要快速连接大屏的业务场景中提升操作效率。

- 会议协作：企业内部系统集成一键投屏，提升会议室使用体验。
- 教学互动：教育平台通过链接触发教师端投屏，便于课堂内容展示。
- 远程办公：远程协作工具中嵌入投屏入口，方便用户共享屏幕。

请注意：建议在HTTPS环境下使用，确保协议链接可被正确识别和唤起。此外，设备需已安装钉钉客户端，并满足最低版本要求（Android/iOS ≥6.5.45），否则将无法正常跳转。

## 扫码体验

使用移动端钉钉扫描下方二维码，快速体验投屏启动功能：

![exported_qrcode_image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3407373371/p885145.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/action/focus_start_projection
```

## **字段说明**

- 本协议无字段参数，无需拼接额外查询参数。直接使用上述链接即可触发。
- 调用前提：设备必须安装钉钉客户端，且版本不低于6.5.45。
- 若未安装钉钉或版本不达标，建议开发者提前进行兼容性检测，并提示用户前往官方渠道下载或更新应用，以保障功能可用性。
