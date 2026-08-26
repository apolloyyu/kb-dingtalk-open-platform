---
title: "消息链接说明"
source_url: "https://open.dingtalk.com/document/development/message-description-service-desk"
namespace: "development"
slug: "message-description-service-desk"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 员工服务台 > 消息链接说明"
doc_id: "ehlW3AMaUr"
updated_at: "2025-12-08 10:06:39"
---

> Source: https://open.dingtalk.com/document/development/message-description-service-desk
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 员工服务台 > 消息链接说明
> Updated: 2025-12-08 10:06:39

# 消息链接说明

本文介绍了消息链接的打开方式。

## 消息链接在PC端侧边栏或外部浏览器打开

在PC客户端点击消息中的URL链接时，希望控制链接的打开方式，可以使用以下方式：

```
dingtalk://dingtalkclient/page/link?url=http%3A%2F%2Fwww.dingtalk.com&pc_slide=true
```

**参数说明：**

| **参数** | 描述 |
| --- | --- |
| url | 要打开的链接，必须urlEncode。 |
| pc\_slide | - true：表示在PC客户端侧边栏打开 - false：表示在浏览器打开 |

## 消息链接在PC端工作台打开

当消息中的URL链接是某个微应用链接时，希望在PC端工作台打开，可以使用以下方式：

```
dingtalk://dingtalkclient/action/openapp?corpid=免登企业corpId&container_type=work_platform&app_id=0_应用agentid&redirect_type=jump&redirect_url=跳转url
```

**参数说明：**

| **参数** | 描述 |
| --- | --- |
| corpid | 免登微应用用户的所属企业。 |
| container\_type | 使用哪种方式打开链接：   - **work\_platform**：表示用工作台打开 |
| app\_id | 第三方企业应用应填写appId，企业自建应用填写0\_agentId，由数字0、下划线和agentId拼接组成。其中appId，agentId可在应用详情中查看。 |
| redirect\_type | 此场景下输入**jump**。 |
| redirect\_url | 要跳转的地址，必须urlEncode。 |

## 小程序链接

小程序发送消息，点击消息链接跳转到小程序，支持的应用场景如下：

| 应用类型 | 工作通知消息 | 企业群消息 | 普通消息 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 不支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 不支持 |
| 第三方个人应用 | — | — | 支持 |

跳转到小程序的消息链接格式如下：

```
 eapp://page?query
```

例如：eapp://pages/index/index?param1=aa&param2=bb

**参数说明：**

- 只有在小程序发送消息时才支持该链接，微应用发送消息时不支持。
- 跳转的目标小程序，需要发布线上版本，才可以保证能正常跳转。
- page表示小程序的页面地址, 例如pages/index/index, 这个page必须是app.json配置中pages下的路径。

  > **[!NOTE]**
  >
  > 跳转的目标小程序，需要发布线上版本，才可以保证能正常跳转。

  ![page参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9760798951/p158178.png)
- query表示page页面onLoad的query参数。例如param1=aa&param2=bb, 当参数值有特殊字符时需要使用urlEncode进行编码处理。
