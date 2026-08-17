---
title: "一键创建钉钉应用扫码接入流程"
source_url: "https://open.dingtalk.com/document/development/creat-dingtalk-application-scan-process"
namespace: "development"
slug: "creat-dingtalk-application-scan-process"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "进阶实战 > Agent 场景案例库 > 快速创建入口 > 一键创建钉钉应用扫码接入流程"
doc_id: "x2RwzPxqkm"
updated_at: "2026-04-24 14:39:18"
---

> Source: https://open.dingtalk.com/document/development/creat-dingtalk-application-scan-process
> Path: 应用开发 / 钉钉CLI / 进阶实战 > Agent 场景案例库 > 快速创建入口 > 一键创建钉钉应用扫码接入流程
> Updated: 2026-04-24 14:39:18

# 一键创建钉钉应用扫码接入流程

本文档描述钉钉应用注册过程中基于 **Device Flow** 的扫码授权协议，供接入方（客户端或插件）实现对接。该流程允许用户通过钉钉 App 完成授权，从而为客户端自动颁发应用凭证（`client_id` 与 `client_secret`），用于后续创建 OpenClaw 机器人。

## 流程概览

整个流程图如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9909996771/p1070747.png)

1. **初始化请求**  
   客户端调用 [一键创建钉钉应用扫码接入流程](#3de4c4722cer2) 接口，获取临时凭证 `nonce`（可选传入 `source` 参数标识来源）。
2. **获取设备授权信息**  
   使用 `nonce` 调用 `开始授权 (begin)` 接口，获取以下关键字段：

   - `device_code`：设备唯一标识，用于后续轮询
   - `user_code`：用户展示码（通常为短数字），用于在钉钉中验证身份
   - `verification_uri`：用户授权页面的 URL，原始URI
   - `verification_uri_complete`：用户授权页面的完整 URL，可引导用户打开进行扫码或输入操作
3. **引导用户授权**  
   根据当前使用场景（桌面端或移动端），向用户展示对应的链接或二维码，引导其使用钉钉扫码或输入 `user_code` 完成授权。
4. **轮询授权状态**  
   客户端以 `device_code` 为参数，按指定间隔（建议 `interval = 5 秒`）调用 `poll` 接口查询授权状态。
5. **处理授权结果**

   - 当返回 `status = "SUCCESS"` 时，获取 `client_id` 和 `client_secret`，可用于创建 OpenClaw 机器人，流程结束。
   - 当返回 `status = "FAIL"` 或 `"EXPIRED"` 时，停止轮询，并向用户提示授权失败或已过期。

## 环境地址

| 环境 | Base URL |
| --- | --- |
| 线上 | `https://oapi.dingtalk.com` |

所有接口均为 `POST`，请求 `Content-Type: application/json`，无需 access\_token。

## 初始化 (init)

- **接口路径**：`/app/registration/init`
- **请求类型**：**POST**
- **请求参数**：

  | 字段 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | source | String | 否 | 来源标识，用于前端渲染不同文案/样式，当前已支持的值：`qoderWork`、`openClaw`等。  **[!NOTE]**  - 该参数可选填，若未填写URI 中不带 source 参数也不影响调用。 - **需要定制source，可扫描下方二维码入群后，联系钉钉小二进行申请**：  image |
- **请求示例**：

  ```
  POST /app/registration/init
  Content-Type: application/json

  {
    "source": "具体值请联系钉钉小二申请"
  }
  ```
- **响应参数**

  | 字段 | 类型 | 说明 |
  | --- | --- | --- |
  | errcode | Number | 错误码，0表示成功。 |
  | errmsg | String | 错误信息，成功时为 "ok"。 |
  | nonce | String | 一次性令牌，用于下一步 begin 接口，5 分钟内有效。 |
  | expires\_in | Number | nonce 有效期（秒），当前为 300。 |
- **响应示例**

  ```
  {
    "errcode": 0,
    "errmsg": "ok",
    "nonce": "nr_a1b2c3d4e5f6...",
    "expires_in": 300
  }
  ```

## 开始授权 (begin)

- **接口路径**：`/app/registration/begin`
- **请求类型**：**POST**
- **请求参数**：

  | 字段 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | nonce | String | 是 | [初始化 (init)](#6ece09e34c1rc) 接口返回的 nonce，一次性使用。 |
- **请求示例**

  ```
  {
    "nonce": "nr_a1b2c3d4e5f6..."
  }
  ```
- **响应参数**

  > **[!NOTE]**
  >
  > 当 init 时传入了有效的 source，URI 中会携带 `&source=xxx`,其中`verification_uri_complete` 适合生成二维码使用。

  | 字段 | 类型 | 说明 |
  | --- | --- | --- |
  | errcode | Number | 错误码，0 表示成功。 |
  | errmsg | String | 错误信息。 |
  | device\_code | String | 设备码，用于 poll 接口轮询，加密传输。 |
  | user\_code | String | 用户码，格式 `XXXX-XXXX-XXXX`，展示给用户。 |
  | verification\_uri | String | 基础链接（不含 user\_code）。 |
  | verification\_uri\_complete | String | 完整链接（含 user\_code），可直接生成二维码。 |
  | expires\_in | Number | device\_code 有效期（秒），当前为 7200（2小时）。 |
  | interval | Number | 建议轮询间隔（秒），当前为 5。 |
- **响应示例**

  ```
  {
    "errcode": 0,
    "errmsg": "ok",
    "device_code": "ahVWM44X7Qxxxxho5wwSbE4...",
    "user_code": "MUEU-DEKR-5TN3",
    "verification_uri": "https://pre-open-dev.xxxxeClawRobot&isHideOuterFrame=true&source=qoderWork",
    "verification_uri_complete": "https://pre-open-dev.dingtalk.com/fe/apxxxxxe=qoderWork",
    "expires_in": 7200,
    "interval": 5
  }
  ```

## 轮询结果 (poll)

- **接口路径**：`/app/registration/poll`
- **请求类型**：**POST**
- **请求参数**：

  | 字段 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | device\_code | String | 是 | begin 接口返回的 device\_code。 |
- **请求示例**

  ```
  {
    "device_code": "ahVWM44X7xxxxwwSbE4..."
  }
  ```
- **响应参数**

  | 字段 | 类型 | 说明 |
  | --- | --- | --- |
  | errcode | Number | 错误码，0 表示成功。 |
  | errmsg | String | 错误信息。 |
  | status | String | 当前状态，见下表。 |
  | client\_id | String | 应用 clientId，仅 status=SUCCESS 时返回。 |
  | client\_secret | String | 应用 clientSecret，仅 status=SUCCESS 时返回。 |
  | fail\_reason | String | 失败原因，仅 status=FAIL 时返回。 |

  **status 状态说明**

  | 状态值 | 含义 | 插件行为 |
  | --- | --- | --- |
  | WAITING | 等待用户扫码/授权中 | 继续按 interval 间隔轮询。 |
  | SUCCESS | 授权成功，应用创建完成 | 停止轮询，读取 client\_id / client\_secret。 |
  | FAIL | 授权失败 | 停止轮询，展示 fail\_reason。 |
  | EXPIRED | device\_code 已过期 | 停止轮询，提示用户重新发起流程。 |
- **响应示例（等待中）**

  ```
  {
    "errcode": 0,
    "errmsg": "ok",
    "status": "WAITING"
  }
  ```
- **响应示例（成功）**

  ```
  {
    "errcode": 0,
    "errmsg": "ok",
    "status": "SUCCESS",
    "client_id": "dingxxxxxx",
    "client_secret": "xxxxxxxxxxxxxxxx"
  }
  ```
- **响应示例（失败）**

  ```
  {
    "errcode": 0,
    "errmsg": "ok",
    "status": "FAIL",
    "fail_reason": "用户拒绝授权"
  }
  ```
- **响应示例（过期）**

  ```
  {
    "errcode": 0,
    "errmsg": "ok",
    "status": "EXPIRED"
  }
  ```

## 注意事项

- 所有接口的 errcode != 0 时均表示服务端异常，errmsg 中包含具体原因。
- nonce 5 分钟内未使用会自动过期，需重新调用 init。
- nonce 为一次性使用，begin 成功后即失效。
- device\_code 2 小时后过期，poll 返回 EXPIRED。
- 建议插件在 poll 轮询超过 expires\_in（7200秒）后主动停止。
- `device_code` 和 `user_code` 具有时效性（通常为 10 分钟），请在有效期内完成用户授权与轮询。
- 用户需在钉钉 App 中登录同一组织账号，方可完成授权。
- 所有接口均需通过 HTTPS 调用，确保通信安全。
- 建议在 UI 中明确告知用户操作指引，例如：“请打开钉钉扫描下方二维码完成授权”。
